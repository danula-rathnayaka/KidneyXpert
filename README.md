# KidneyXpert

## Overview
**KidneyXpert** is an AI-powered kidney disease classification system utilizing deep learning for automated diagnosis. This project integrates MLflow for experiment tracking and DVC for version control, providing a robust pipeline to evaluate kidney health and detect potential conditions.

## Features
- AI-based kidney disease classification.
- Deep learning model trained using TensorFlow/Keras.
- Flask API for easy interaction.
- Experiment tracking with MLflow.
- Data version control using DVC.

## Installation and Setup
### Step 1: Clone the Repository
```bash
git clone https://github.com/danula-rathnayaka/KidneyXpert.git
cd KidneyXpert
```

### Step 2: Create a Conda Environment
```bash
conda create -n cnncls python=3.8 -y
conda activate cnncls
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

## Running the Application
Before running the application, ensure that the model is built using the `/train` endpoint.

### Step 4: Train the Model
```bash
curl -X POST http://localhost:5000/train
```

### Step 5: Start the Application
```bash
python app.py
```
Now, open your browser and navigate to `http://localhost:5000` to access the application.

## API Endpoints
- **Home Page**: `GET /` - Serves the frontend interface.
- **Train Model**: `POST /train` - Triggers model training using DVC.
- **Predict Disease**: `POST /predict` - Accepts an image input and returns the classification result.


## Model Training Pipeline
KidneyXpert follows a structured pipeline for data processing and model training:

1. **Data Ingestion**: Fetch and preprocess data.
2. **Prepare Base Model**: Create the deep learning architecture.
3. **Train the Model**: Train the model using TensorFlow/Keras.
4. **Evaluate the Model**: Use MLflow to track performance.

---