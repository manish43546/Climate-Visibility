from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="climate-visibility",
    version="1.1.0",
    author="Manish",
    author_email="manish43546@example.com",
    description="ML pipeline to predict maximum visibility distance based on meteorological and geographical data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/manish43546/Climate-Visibility",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.9",
    install_requires=[
        "numpy>=1.24.0",
        "pandas>=2.0.0",
        "scikit-learn>=1.3.0",
        "xgboost>=2.0.0",
        "Flask>=3.0.0",
        "FastAPI>=0.104.0",
        "uvicorn>=0.24.0",
        "pymongo>=4.6.0",
        "boto3>=1.28.0",
        "python-dotenv>=1.0.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.9.0",
            "flake8>=6.1.0",
            "mypy>=1.5.0",
        ],
    },
)