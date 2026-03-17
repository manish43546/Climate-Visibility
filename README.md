# Visibility Distance Prediction

An end-to-end ML pipeline to predict maximum visibility distance based on meteorological and geographical data.

## Problem Statement

The objective of this project is to develop a machine learning model that can accurately predict the maximum visibility distance in a given location and weather condition. The model should take into account various weather parameters such as humidity, temperature, wind speed, and atmospheric pressure, as well as geographical features such as elevation, terrain, and land cover. The model should be trained on a large dataset of historical weather and visibility data, and validated using a separate test dataset. The ultimate goal is to provide a tool that can help improve safety and efficiency in various applications such as aviation, transportation, and outdoor activities.

## Tech Stack Used

- **Language**: Python 3.11+
- **Web Framework**: Flask 3.0+
- **API Framework**: FastAPI 0.104+
- **Machine Learning**: XGBoost, Scikit-learn
- **Database**: MongoDB 7.0+
- **Container**: Docker & Docker Compose
- **Cloud**: AWS S3, Azure
- **CI/CD**: GitHub Actions

## Prerequisites

- Python 3.11 or higher
- Docker & Docker Compose (for containerized deployment)
- MongoDB Atlas account (or local MongoDB instance)
- AWS Account (S3 access for model storage)
- Git

## Quick Start

### Option 1: Local Development

#### Step 1: Clone the Repository

```bash
git clone https://github.com/manish43546/Climate-Visibility.git
cd Climate-Visibility
```

#### Step 2: Create Python Virtual Environment

```bash
# Using venv
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

#### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

#### Step 4: Configure Environment Variables

Copy the example environment file and update with your credentials:

```bash
cp .env.example .env
```

Edit `.env` with your values:

```bash
# MongoDB Configuration
MONGO_DB_URL=mongodb+srv://<username>:<password>@cluster.mongodb.net/climate_visibility

# AWS Configuration
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_DEFAULT_REGION=us-east-1

# Flask Configuration
FLASK_PORT=5000
FLASK_DEBUG=False
```

#### Step 5: Run the Application

```bash
python app.py
```

The application will be available at: `http://localhost:5000/`

### Option 2: Docker Deployment (Recommended)

#### Step 1: Clone the Repository

```bash
git clone https://github.com/manish43546/Climate-Visibility.git
cd Climate-Visibility
```

#### Step 2: Configure Environment

```bash
cp .env.example .env
# Edit .env with your AWS and MongoDB credentials
```

#### Step 3: Build and Run with Docker Compose

```bash
docker-compose up -d
```

This will start:
- MongoDB service on port 27017
- Flask application on port 5000

#### Step 4: Verify Deployment

```bash
# Check health
curl http://localhost:5000/health

# Should return:
# {"status": "healthy", "service": "Climate-Visibility"}
```

#### Step 5: Stop Services

```bash
docker-compose down
```

### Option 3: Docker Build Only (Manual)

```bash
docker build \
  --build-arg AWS_ACCESS_KEY_ID=your_access_key \
  --build-arg AWS_SECRET_ACCESS_KEY=your_secret_key \
  --build-arg AWS_DEFAULT_REGION=us-east-1 \
  --build-arg MONGO_DB_URL=mongodb+srv://user:pass@cluster.mongodb.net/db \
  -t climate-visibility:latest .

docker run -d \
  -p 5000:5000 \
  -e MONGO_DB_URL="mongodb+srv://user:pass@cluster.mongodb.net/db" \
  -e AWS_ACCESS_KEY_ID="your_access_key" \
  -e AWS_SECRET_ACCESS_KEY="your_secret_key" \
  -e AWS_DEFAULT_REGION="us-east-1" \
  --name climate-visibility \
  climate-visibility:latest
```

## API Endpoints

### Health Check
```bash
GET http://localhost:5000/health
```
Response:
```json
{
  "status": "healthy",
  "service": "Climate-Visibility"
}
```

### Home
```bash
GET http://localhost:5000/
```
Returns the web UI

### Train Model
```bash
GET/POST http://localhost:5000/train
```
Response:
```json
{
  "message": "Training Successful.",
  "status": "success"
}
```

### Predict Visibility
```bash
GET http://localhost:5000/predict
```
Returns prediction form (GET)

```bash
POST http://localhost:5000/predict
```
Submit form data to get prediction

## Project Structure

```
Climate-Visibility/
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   ├── data_clustering.py
│   │   ├── model_trainer.py
│   │   ├── model_evaluation.py
│   │   └── model_pusher.py
│   ├── pipeline/
│   │   ├── training_pipeline.py
│   │   └── prediction_pipeline.py
│   ├── exception.py
│   └── logger.py
├── templates/
│   ├── index.html
│   ├── predict.html
│   └── result.html
├── static/
│   ├── css/
│   └── js/
├── notebooks/
│   └── exploratory_analysis.ipynb
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── requirements.txt
├── app.py
└── README.md
```

## Key Components

### Data Pipeline
1. **Data Ingestion**: Fetch data from various sources
2. **Data Validation**: Validate data quality and integrity
3. **Data Transformation**: Feature engineering and preprocessing
4. **Data Clustering**: Cluster similar data patterns (K-Means)
5. **Model Training**: Train XGBoost model with GridSearchCV
6. **Model Evaluation**: Evaluate model performance
7. **Model Pusher**: Push model artifacts to S3

### Custom Utilities
- **Logger**: Comprehensive logging for debugging
- **Exception Handler**: Custom exception handling with context

## ML Models Used

- **XGBoost**: For regression/classification tasks
- **K-Means**: For clustering similar weather patterns
- **Logistic Regression**: For binary classification (if applicable)

## Database Schema

### MongoDB Collections

#### Weather Data
```json
{
  "_id": ObjectId,
  "temperature": float,
  "humidity": float,
  "pressure": float,
  "wind_speed": float,
  "location": string,
  "visibility": float,
  "timestamp": datetime
}
```

## Deployment

### AWS Deployment

1. **Using EC2**:
   ```bash
   # SSH into EC2 instance
   ssh -i key.pem ec2-user@instance-ip
   
   # Clone and setup
   git clone https://github.com/manish43546/Climate-Visibility.git
   cd Climate-Visibility
   docker-compose up -d
   ```

2. **Using ECS/Fargate**:
   - Push Docker image to ECR
   - Create ECS task definition
   - Configure load balancer

3. **Using Elastic Beanstalk**:
   ```bash
   eb init -p docker climate-visibility
   eb create
   eb deploy
   ```

### Azure Deployment

1. **Using App Service**:
   - Push to Azure Container Registry
   - Create Web App from container
   - Configure environment variables

2. **Using AKS**:
   - Create AKS cluster
   - Deploy Helm charts
   - Configure ingress controller

## Environment Variables Reference

| Variable | Default | Description |
|----------|---------|-------------|
| `MONGO_DB_URL` | Required | MongoDB connection string |
| `AWS_ACCESS_KEY_ID` | Required | AWS access key |
| `AWS_SECRET_ACCESS_KEY` | Required | AWS secret key |
| `AWS_DEFAULT_REGION` | `us-east-1` | AWS region |
| `FLASK_PORT` | `5000` | Flask server port |
| `FLASK_DEBUG` | `False` | Debug mode (never enable in production) |
| `PYTHONUNBUFFERED` | `1` | Unbuffered Python output |

## Troubleshooting

### MongoDB Connection Error
```
Error: connection refused
Solution: Ensure MongoDB is running and MONGO_DB_URL is correct
```

### AWS Credentials Error
```
Error: Unable to locate credentials
Solution: Verify AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY are set
```

### Port Already in Use
```
Error: Address already in use
Solution: Change FLASK_PORT or kill process using port 5000
```

### Docker Build Fails
```
Error: pip install fails
Solution: Check internet connection and requirements.txt compatibility
```

## Development Guide

### Adding New Features

1. Create feature branch
2. Implement in `src/components/` or `src/pipeline/`
3. Add tests
4. Update README documentation
5. Submit pull request

### Code Standards

- Follow PEP 8 style guide
- Use type hints where possible
- Add docstrings to all functions
- Write unit tests for new features

## Monitoring & Logging

The application includes comprehensive logging:

```python
from src.logger import logging as lg
lg.info("Your log message")
lg.error("Error message")
```

All logs are stored and can be used for debugging and monitoring.

## Performance Optimization

- Model inference is optimized with XGBoost
- Batch prediction support for multiple samples
- Caching mechanisms for frequently accessed data
- Async database operations where applicable

## Security Considerations

✅ **Implemented**:
- Non-root Docker user
- Environment variable secrets management
- HTTPS ready configuration
- Input validation

⚠️ **Recommendations**:
- Use AWS Secrets Manager for credentials
- Enable MongoDB authentication
- Configure rate limiting
- Add API authentication (JWT/OAuth)
- Regular security audits

## Project Architecture

```
┌─────────────────────┐
│   Client (Web UI)   │
└──────────┬──────────┘
           │
┌──────────▼──────────┐
│   Flask Server      │
│   (Port 5000)       │
└──────────┬──────────┘
           │
      ┌────┴────┐
      │          │
┌─────▼──┐  ┌───▼─────┐
│ MongoDB │  │  AWS S3 │
│ (ML DB) │  │ (Models)│
└─────────┘  └─────────┘
```

## Models and Artifacts

- **Trained Model**: `model.pkl` (stored in S3)
- **Scaler Objects**: Feature scalers for normalization
- **Configuration**: Model hyperparameters (YAML)

## License

This project is licensed under the MIT License.

## Contributors

- Manish (manish43546)

## Support

For issues, questions, or suggestions:
1. Check existing GitHub issues
2. Create a new issue with detailed description
3. Include error logs and environment details

## Changelog

### v1.1.0 (Latest)
- ✅ Fixed port configuration (5000)
- ✅ Disabled debug mode for production
- ✅ Added health check endpoint
- ✅ Added graceful shutdown handling
- ✅ Updated dependencies to latest stable versions
- ✅ Added Docker Compose configuration
- ✅ Improved error handling

### v1.0.0
- Initial release