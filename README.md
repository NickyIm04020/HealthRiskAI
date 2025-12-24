# 🏥 HealthRiskAI – Interpretable Disease Risk Prediction

### 🧩 Overview
HealthRiskAI is a **production-ready machine learning system** for predicting **chronic disease risk (Diabetes & Cardiovascular)** with **patient-level interpretability**.

It addresses the *black-box problem* in medical AI by combining **XGBoost** with **SHAP-based explanations**, making predictions transparent and actionable.

---

### 🔥 Highlights
- **High Performance:** AUC-ROC of **0.92**
- **Well-Calibrated:** Brier Score **0.12**
- **Explainable AI:** SHAP feature attribution per prediction
- **Deployment Ready:** Modular ML + API design (Lambda-compatible)

---

### 🧠 What It Does
- Predicts disease risk from structured clinical features  
- Explains *why* a patient is high-risk (top contributing factors)  
- Outputs interpretable risk scores suitable for healthcare use  

---

### ⚙️ Tech Stack
- **ML:** Python, XGBoost, Scikit-Learn  
- **Explainability:** SHAP (TreeExplainer)  
- **API:** Flask  
- **Data:** Synthetic clinical dataset  

---

### 🏗️ Project Structure
```

HealthRiskAI/
├── src/        # Model training & evaluation
├── api/        # Flask inference API
└── models/     # Trained XGBoost model

````

---

### 🚀 Quick Start

#### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/HealthRiskAI.git
cd HealthRiskAI
pip install -r requirements.txt
````

#### 2️⃣ Train the Model

```bash
python src/model.py
```

#### 3️⃣ Run the API

```bash
python api/app.py
```

---

### 📡 API Example

**Request**

```bash
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d '{"features":[65,30.5,8.2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}'
```

**Response**

```json
{
  "risk_score": 0.88,
  "risk_level": "High",
  "top_driver_index": 2
}
```

---

### 💡 Why This Project Matters

* Combines **ML accuracy + explainability**
* Demonstrates **end-to-end ML engineering** (Data → Model → API)
* Relevant for **healthcare, fintech risk, and regulated AI systems**

---

### 📄 License

MIT License


