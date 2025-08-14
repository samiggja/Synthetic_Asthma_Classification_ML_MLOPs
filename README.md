# 🫁 Synthetic Asthma Classification – ML & MLOps Pipeline

An end-to-end **Machine Learning pipeline** for classifying asthma presence and control levels using synthetic patient data.  
The project demonstrates a **modular, production-ready workflow** including data preprocessing, feature engineering, model training, evaluation, and prediction export — ready for integration into healthcare applications.

---

## 📌 Project Overview

This project was built to:
- Explore predictive modeling for **asthma detection and management**
- Demonstrate a **clean, modular ML pipeline**
- Compare multiple classification algorithms
- Prepare deployment-ready outputs

**Best Model Achieved:** 🌟 **Random Forest – 97.65% Accuracy**

---

## 🗂 Pipeline Steps

1. **Data Input**
   - Load dataset `synthetic_asthma_dataset.csv`

2. **Data Preprocessing**
   - Drop unnecessary columns (`Patient_ID`)
   - Handle missing values (Mode imputation)
   - Encode categorical features:
     - **Label Encoding**: `Gender`, `Smoking_Status`, `Allergies`, `Comorbidities`
     - **Ordinal Encoding**: `Air_Pollution_Level`, `Physical_Activity_Level`, `Occupation_Type`, `Asthma_Control_Level`
   - Feature scaling with **StandardScaler**

3. **Model Training**
   - Logistic Regression
   - Support Vector Machine (SVM)
   - Random Forest Classifier

4. **Model Evaluation**
   - Accuracy comparison between models
   - Best model: **Random Forest (97.65%)**

5. **Predictions & Output**
   - Generate predictions with probabilities
   - Save results as `predictions.csv`

---

## 📊 Pipeline Diagram

![Asthma Pipeline](asthma_pipeline_diagram.png)

---

## 🛠 Tech Stack

- **Languages:** Python
- **Libraries:** Pandas, NumPy, scikit-learn
- **Tools:** Jupyter Notebook, Git, MLOps-ready modular structure

---

## 📁 Repository Structure

```plaintext
.
├── Data/                       # Dataset folder
├── src/                        # Modular Python scripts
├── model/                      # Saved models (if applicable)
├── reports/                    # Reports & results
├── predictions.csv             # Final predictions
├── asthma_pipeline_diagram.png # Pipeline diagram
├── LICENSE
└── README.md





🚀 How to Run

Clone the repo:

git clone https://github.com/samiggja/Synthetic_Asthma_Classification_ML_MLOPs.git
cd Synthetic_Asthma_Classification_ML_MLOPs


Install dependencies:

pip install -r requirements.txt


Run the pipeline:

python src/main.py


Check the predictions:
Open predictions.csv for patient predictions and probabilities.

📈 Results
Model	Accuracy
Logistic Regression	93.10%
SVM	96.75%
Random Forest	97.65%
📜 License

This project is licensed under the MIT License — see the LICENSE file for details.
