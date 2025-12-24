from flask import Flask, request, jsonify
import xgboost as xgb
import shap
import numpy as np
import os

app = Flask(__name__)

# Load Model
model_path = os.path.join(os.getcwd(), 'models/xgb_model.json')
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at {model_path}. Run src/model.py first.")

model = xgb.Booster()
model.load_model(model_path)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = np.array(data['features']).reshape(1, -1)
        
        # --- FIX START: Define names exactly as they were in training ---
        feature_names = [f'feature_{i}' for i in range(20)]
        feature_names[0] = 'Age'
        feature_names[1] = 'BMI'
        feature_names[2] = 'HbA1c'
        
        # Create DMatrix WITH the feature names
        dmatrix = xgb.DMatrix(features, feature_names=feature_names)
        # --- FIX END ---

        # Predict
        prob = model.predict(dmatrix)[0]
        
        # Explain
        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(dmatrix)
        
        return jsonify({
            "risk_score": float(prob),
            "risk_level": "High" if prob > 0.7 else "Low",
            "top_driver_index": int(np.argmax(np.abs(shap_values[0])))
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(port=5000, debug=True)