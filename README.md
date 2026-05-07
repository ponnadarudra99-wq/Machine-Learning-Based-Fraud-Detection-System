# Machine Learning-Based Fraud Detection System

A Machine Learning-based financial fraud detection system developed to classify banking transactions as **Fraudulent** or **Legitimate** using transaction behavior analysis. This project uses **Logistic Regression** for binary classification, **Pickle** for model serialization, and **Streamlit** for real-time fraud prediction deployment.

---

## 📌 Project Overview

Financial fraud is one of the major challenges in digital banking and online transactions. Manual monitoring of thousands of daily transactions is difficult and time-consuming. This project automates fraud detection by analyzing suspicious transaction patterns and classifying transactions as fraudulent or legitimate using Machine Learning techniques.

The model is trained on a synthetic banking transaction dataset generated with realistic fraud-related behavior patterns.

---

## 🎯 Objectives

- Detect fraudulent banking transactions automatically
- Reduce manual fraud verification effort
- Classify suspicious and legitimate transactions
- Deploy a real-time fraud prediction web application

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Logistic Regression
- Pickle
- Streamlit
- Matplotlib
- Jupyter Notebook

---

## 📂 Dataset Information

This project uses a synthetic banking transaction dataset generated using Pandas and randomized fraud behavior rules.

### Dataset Features

| Column Name | Description |
|-------------|-------------|
| Amount | Transaction amount |
| Transaction_Type | Type of banking transaction |
| Account_Age | Account age in months |
| Is_International | International transaction flag (0/1) |
| Is_High_Risk | High risk transaction flag (0/1) |
| Class | Fraud = 1 / Legitimate = 0 |

Dataset File: `professional_fraud_detection_dataset.csv`

---

## ⚙️ Machine Learning Workflow

1. Load CSV dataset using Pandas  
2. Perform feature-target separation  
3. Apply train-test split  
4. Train Logistic Regression classifier  
5. Predict fraud status on unseen transactions  
6. Evaluate model performance using classification metrics  
7. Save trained model using Pickle  
8. Deploy real-time prediction app using Streamlit

---

## 📈 Model Performance

The trained Logistic Regression model achieved strong fraud classification performance on unseen banking transactions.

- **Accuracy:** 91%
- **Precision:** 93%
- **Recall:** 86%
- **F1-Score:** 89%

### Confusion Matrix

```python
[[54 3]
 [6 37]]
```

The model successfully classified both fraudulent and legitimate banking transactions with balanced predictive performance and low misclassification.

---

## 💻 Real-Time Prediction Example

```python
new_transaction = np.array([[3000, 3, 5, 1, 1]])
prediction = model.predict(new_transaction)
```

Output:

```python
Fraud Transaction Detected
```

---

## 🚀 Streamlit Web Application

A Streamlit-based frontend application is integrated with the trained Pickle model where users can enter transaction details and instantly receive fraud prediction results.

### To Run the App

```bash
streamlit run fraud_detection.py
```

---

## 📁 Project Structure

```bash

├── professional_fraud_detection_dataset.csv
├── Fraud_Detection_Project.ipynb
├── fraud_detection_model.pkl
├── fraud_detection.py
└── README.md
```

---

## ✅ Key Features

- Banking fraud transaction analysis
- Logistic Regression-based binary classification
- Synthetic fraud dataset generation
- 91% fraud detection accuracy
- Real-time Streamlit deployment
- Pickle serialized trained model
- Interactive fraud prediction interface

---

## 🔮 Future Enhancements

- Train using real-world banking datasets
- Implement advanced models like Random Forest and XGBoost
- Add fraud analytics dashboard
- Deploy online using cloud platforms

---

## 👨‍💻 Author

**PONNADA RUDRA NAGA TEJA**  
Email: ponnadarudra99@gmail.com  
LinkedIn: linkedin.com/in/ponnada-rudra-naga-teja-586561323  
GitHub: github.com/ponnadarudra99-wq
