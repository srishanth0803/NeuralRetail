# NeuralRetail – Retail Demand Forecasting & Customer Intelligence Platform

## Overview

NeuralRetail is an end-to-end Machine Learning and MLOps project developed as part of an internship at Amdox Technologies. The project focuses on retail analytics, demand forecasting, customer churn prediction, customer segmentation, and revenue intelligence using modern Machine Learning, Deep Learning, and MLOps practices.

The platform transforms raw retail transaction data into actionable business insights through automated data pipelines, forecasting models, customer intelligence systems, experiment tracking, and model management workflows.

---

## Project Objectives

* Forecast future product demand using statistical and deep learning models.
* Predict customer churn and identify at-risk customers.
* Segment customers using RFM-based clustering.
* Analyze price elasticity and revenue impact.
* Track experiments and model performance using MLflow.
* Build reproducible MLOps pipelines for model training and evaluation.

---

## Technology Stack

### Programming

* Python 3.11

### Data Processing

* Pandas
* NumPy
* PySpark

### Machine Learning

* Scikit-Learn
* XGBoost
* LightGBM
* Prophet
* NeuralProphet
* PyTorch
* PyTorch Lightning

### Time Series Analysis

* Statsmodels
* Prophet
* NeuralProphet

### Explainability

* SHAP
* LIME

### MLOps

* MLflow
* Git
* GitHub

### Visualization

* Matplotlib
* Seaborn
* Plotly

---

## Dataset

### Source

Online Retail II Dataset

### Key Features

* Invoice Number
* Stock Code
* Description
* Quantity
* Invoice Date
* Unit Price
* Customer ID
* Country

### Dataset Statistics

* More than 500,000 retail transactions
* Multiple years of historical sales data
* Real-world missing values and data quality challenges

---

# Project Architecture

Raw Data
↓
Data Ingestion
↓
Bronze Layer
↓
Data Cleaning
↓
Silver Layer
↓
Feature Engineering
↓
Feature Store
↓
Forecasting + Churn Models
↓
MLflow Tracking
↓
Business Insights

---

# Implemented Modules

## 1. Data Ingestion

### Tasks

* Load Online Retail II dataset
* Validate schema
* Store raw data in Bronze layer

### Output

* online_retail_II_bronze.csv

---

## 2. Data Profiling & EDA

### Analysis Performed

* Missing values
* Outlier detection
* Data distributions
* Correlation analysis
* Duplicate detection

### Generated Reports

* data_profile.html
* data_profile_report.html

### Key Findings

* Missing Customer IDs
* Missing Product Descriptions
* Returns represented by negative quantities
* Strong seasonality in sales

---

## 3. Customer Churn Prediction

### Features

* Recency
* Frequency
* Monetary Value
* Purchase Frequency Decay
* Recency Cliff

### Models

* Random Forest
* XGBoost
* LightGBM
* Stacking Ensemble

### Evaluation Metrics

* AUC-ROC
* Precision
* Recall
* F1 Score

### Results

* AUC: 1.00
* F1 Score: 1.00

---

## 4. Demand Forecasting

### Statistical Models

* Prophet
* NeuralProphet

### Deep Learning Models

* LSTM
* Temporal Fusion Transformer (TFT)

### Analysis

* Stationarity Testing
* ADF Test
* KPSS Test
* STL Decomposition
* ACF Analysis
* PACF Analysis

### Forecast Horizons

* 1 Day
* 7 Days
* 30 Days

### Evaluation Metric

* MAPE

### Best Result

* MAPE ≈ 2.58%

---

## 5. Time Series Diagnostics

### Implemented

* ADF Test
* KPSS Test
* Log Transformation
* Differencing
* STL Decomposition
* Seasonality Analysis

### Generated Outputs

* stl_decomposition.png
* seasonality_components.png
* acf.png
* pacf.png
* differenced_series.csv

---

## 6. Customer Segmentation

### Techniques

* RFM Analysis
* K-Means Clustering
* DBSCAN
* Gaussian Mixture Models

### Outputs

* Customer Segments
* VIP Customers
* High Churn Segments
* Revenue-Based Segments

---

## 7. Explainable AI

### SHAP Analysis

* Global Feature Importance
* Local Predictions
* Beeswarm Plots
* Waterfall Plots

### LIME

* Local Model Explanations

### Outcome

Model decisions translated into business-friendly insights.

---

## 8. Price Elasticity & Revenue Intelligence

### Models

* Log-Log OLS Regression

### Business Questions Answered

* Impact of price changes on demand
* Promotion effectiveness
* Revenue sensitivity analysis

### Outputs

* Elasticity coefficients
* Revenue projections
* Pricing recommendations

---

## 9. MLflow Integration

### Tracked Information

* Parameters
* Metrics
* Models
* Artifacts

### Experiments

* Customer Churn
* Prophet Forecasting
* NeuralProphet Forecasting
* Ensemble Forecasting

---

## Project Folder Structure

NeuralRetail/

├── data/

├── reports/

├── feature_repo/

├── src/

│ ├── ingestion/

│ ├── analysis/

│ ├── churn/

│ ├── forecasting/

│ ├── segmentation/

│ ├── explainability/

│ ├── pricing/

│ ├── mlflow/

│ └── reporting/

├── notebooks/

├── requirements.txt

└── README.md

---

## Results Summary

| Module                   | Metric       | Result |
| ------------------------ | ------------ | ------ |
| Churn Prediction         | AUC-ROC      | 1.00   |
| Churn Prediction         | F1 Score     | 1.00   |
| Demand Forecasting       | MAPE         | 2.58%  |
| Time Series Stationarity | ADF p-value  | 0.0    |
| Time Series Stationarity | KPSS p-value | 0.1    |

---

## Business Impact

### Demand Forecasting

* Better inventory planning
* Reduced stockouts
* Reduced overstocking

### Churn Prediction

* Early identification of at-risk customers
* Improved retention campaigns

### Customer Segmentation

* Personalized marketing strategies
* Better customer targeting

### Price Elasticity

* Revenue optimization
* Smarter pricing decisions

---

## Key Learnings

Throughout this project I gained practical experience in:

* End-to-End Machine Learning Pipelines
* Time Series Forecasting
* Customer Analytics
* Deep Learning for Forecasting
* MLOps Workflows
* Experiment Tracking with MLflow
* Git and GitHub Collaboration
* Feature Engineering
* Explainable AI
* Business Intelligence

---

## Future Enhancements

* Real-time forecasting APIs
* Cloud deployment on AWS
* CI/CD pipelines
* Docker containerization
* Airflow orchestration
* Grafana monitoring dashboards
* Drift detection
* Automated retraining pipelines

---

## Author

SRISHANTH

Machine Learning Intern – Amdox Technologies

GitHub Repository:
https://github.com/srishanth0803/NeuralRetail

---

## License

This project is intended for educational, internship, and portfolio purposes.
