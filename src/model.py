import pandas as pd
import xgboost as xgb
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.datasets import make_classification

# Ensure models directory exists
if not os.path.exists('models'):
    os.makedirs('models')

def train_and_save():
    print("🏥 Generating synthetic clinical data...")
    # Simulate 5000 patients with 20 features
    X, y = make_classification(n_samples=5000, n_features=20, random_state=42)
    feature_names = [f'feature_{i}' for i in range(20)]
    feature_names[0] = 'Age'
    feature_names[1] = 'BMI'
    feature_names[2] = 'HbA1c'
    
    df = pd.DataFrame(X, columns=feature_names)
    
    # Split Data
    X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.2, random_state=42)

    # Train XGBoost
    print("⚙️ Training XGBoost Model...")
    # remove use_label_encoder to avoid warnings
    model = xgb.XGBClassifier(eval_metric='logloss')
    model.fit(X_train, y_train)

    # Evaluate
    y_prob = model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, y_prob)
    print(f"✅ Training Complete. AUC-ROC: {auc:.2f}")

    # Save Model (THIS IS THE FIX)
    # We use get_booster() to save the core model, avoiding the TypeError
    model.get_booster().save_model('models/xgb_model.json')
    print("💾 Model saved to models/xgb_model.json")

if __name__ == "__main__":
    train_and_save()