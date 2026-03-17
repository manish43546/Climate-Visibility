from flask import Flask, render_template, jsonify, request, send_file, signal, sys
from src.exception import VisibilityException
from src.logger import logging as lg
import os

from src.pipeline.training_pipeline import TraininingPipeline
from src.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)

# Graceful shutdown handlers
def signal_handler(sig, frame):
    """Handle graceful shutdown"""
    lg.info("Shutting down Flask server gracefully...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

# Health check endpoint
@app.route("/health", methods=['GET'])
def health_check():
    """Health check endpoint for deployment orchestration"""
    return jsonify({"status": "healthy", "service": "Climate-Visibility"}), 200

@app.route("/")
def home():
    try:
        return render_template("index.html")
    except Exception as e:
        lg.error(f"Error loading home page: {str(e)}")
        raise VisibilityException(e, sys)

@app.route("/train", methods=['GET', 'POST'])
def train_route():
    """Train the ML model"""
    try:
        train_pipeline = TraininingPipeline()
        train_pipeline.run_pipeline()
        lg.info("Training completed successfully")
        return jsonify({"message": "Training Successful.", "status": "success"})

    except Exception as e:
        lg.error(f"Training failed: {str(e)}")
        raise VisibilityException(e, sys)

@app.route("/predict", methods=['POST', 'GET'])
def predict():
    """Predict visibility based on input parameters"""
    try:
        if request.method == "POST":
            prediction_pipeline = PredictionPipeline(request=request)
            predicted_visibility = prediction_pipeline.run_pipeline()
            lg.info(f"Prediction successful: {predicted_visibility[0]}")
            return render_template("result.html", prediction=f"{predicted_visibility[0]:.3f}")
        elif request.method == "GET":
            return render_template("predict.html")
        else:
            return jsonify({"error": "Method not allowed"}), 405
    
    except Exception as e:
        lg.error(f"Prediction failed: {str(e)}")
        raise VisibilityException(e, sys)

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    lg.warning(f"404 Error: {str(e)}")
    return jsonify({"error": "Page not found"}), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors"""
    lg.error(f"500 Error: {str(e)}")
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    # Validate required environment variables
    required_env_vars = ["MONGO_DB_URL", "AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY", "AWS_DEFAULT_REGION"]
    missing_vars = [var for var in required_env_vars if not os.getenv(var)]
    
    if missing_vars:
        lg.warning(f"Missing environment variables: {', '.join(missing_vars)}")
        lg.info("Using default values if available")
    
    port = 5000  # Changed port to 5000
    debug_mode = False  # Disabled debug mode
    
    lg.info("="*60)
    lg.info("Starting the Flask server")
    lg.info(f"Flask application running on port {port}")
    lg.info(f"Debug mode: {debug_mode}")
    lg.info(f"Click on the link to open the application: http://localhost:{port}/")
    lg.info(f"Health check endpoint: http://localhost:{port}/health")
    lg.info("="*60)
    
    app.run(host="0.0.0.0", port=port, debug=debug_mode)