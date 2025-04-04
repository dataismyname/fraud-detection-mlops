# fraud-detection-mlops

**End-to-end Machine Learning pipeline for real-time fraud detection in a simulated FinTech environment.**

---

## 📌 Overview

This project simulates a production-ready ML pipeline for detecting fraudulent transactions in a financial ecosystem. It integrates modern data architecture patterns like Lambda Architecture, real-time processing with Kafka and Spark, and MLOps practices including CI/CD, containerization, and model deployment using AWS services.

This solution showcases essential skills of a Machine Learning Engineer in the fintech space.

---

## 🚀 Key Features

- Lambda Architecture: batch + streaming + serving layers  
- Apache Spark: big data processing & optimizations  
- Kafka: real-time ingestion and alert streaming  
- Feature Store: offline (Spark+Parquet) + online (Redis)  
- MLOps: model versioning, Docker, GitHub Actions, CI/CD workflows  
- Deployment: FastAPI + AWS Lambda / SageMaker Endpoint  
- Orchestration: Apache Airflow or AWS Glue  
- Monitoring: drift detection, inference logs, basic alerting  

---

## 🧱 Repository Structure

```
fraud-detection-mlops/
├── README.md
├── requirements.txt
├── Makefile
├── .gitignore
├── data/
├── notebooks/
├── src/
│   ├── etl/
│   ├── features/
│   ├── models/
│   ├── inference/
│   └── utils/
├── airflow/
├── docker/
├── .github/
└── docs/
```

---

## 🔧 Getting Started

> Prerequisites:
- Docker & Docker Compose
- Python ≥ 3.9
- (Optional) AWS CLI configured

```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## 📊 Project Stages

1. Data ingestion (batch + streaming)
2. Feature engineering (offline & online)
3. Model training and evaluation
4. Model deployment to a real-time API
5. Monitoring and retraining triggers

Each stage is modular and versioned for reproducibility and MLOps alignment.

---

## 🧠 Why This Project?

This project aims to:
- Showcase the full lifecycle of a fraud detection ML system
- Simulate real production constraints using synthetic and real data
- Demonstrate engineering rigor through automation, reproducibility, and scalability

It is designed to align with core skills expected from ML Engineers in fintech environments.

---

## 📄 License

MIT License (see LICENSE file)
