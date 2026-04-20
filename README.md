<img width="1336" height="812" alt="output2" src="https://github.com/user-attachments/assets/2213c5d9-1f4d-485c-bfe2-23dcec8cb61b" />
<img width="1421" height="743" alt="output1" src="https://github.com/user-attachments/assets/488b7837-a2fb-4f12-a5c8-1e4d79f40a0a" />
<img width="1428" height="854" alt="input2" src="https://github.com/user-attachments/assets/637eb7a0-1a78-481d-a274-4ecb626a7678" />
<img width="1389" height="795" alt="input1" src="https://github.com/user-attachments/assets/5a251a5e-adbf-4867-8d40-13b5e3f85f98" />
# Student-Performance-Prediction-and-Early-Intervention

## Team Members

- **Keerthana V K** — EDA, insights, README  
- **Krishnendhu M S** — Model building (Logistic Regression, Decision Tree, Gradient Boosting)  
- **Theertha Vijayachandran** — Deployment, LIME, app testing  

---

## Project Overview

This project predicts whether a student will **pass or fail** based on demographics, attendance, study time, and prior grades using the **UCI Student Performance dataset**. The goal is to **identify at-risk students early** and provide actionable insights for intervention.  

**Workflow includes:**  
- Data preprocessing and outlier handling  
- Exploratory Data Analysis (EDA)  
- Feature selection and encoding  
- Model building and evaluation (Logistic Regression, Decision Tree, Gradient Boosting)  
- Interpretability using LIME  
- Deployment using Streamlit  

---

## Dataset

- **Source:** [UCI Student Performance dataset](https://archive.ics.uci.edu/ml/datasets/Student+Performance)  
- **Size:** 395 entries, 34 features  
- **Features:**  
  - **Demographics:** age, sex, address, parental education, family size  
  - **Academic history:** G1, G2, failures  
  - **Behavior:** study time, absences, goout, freetime  
  - **Others:** health, alcohol consumption (Dalc, Walc)  
- **Target:** `result` (1 = Pass, 0 = Fail)  

---

## Exploratory Data Analysis (EDA)

- Visualized **Pass vs Fail distribution** using countplots  
- Boxplots for **Study Time vs Result** and **Failures vs Result**  
- Outliers in `studytime`, `absences`, and `failures` handled using **IQR capping**  
- Explored categorical features like `sex`, `address`, `parental education`  
- Correlation heatmap revealed `G1` and `G2` highly correlated with `G3` → removed to avoid **data leakage**  

### Key Insights

- Students with higher absences are more likely to fail  
- Higher parental education positively influences performance  
- Most students have zero past failures  
- Study time positively correlates with passing, but other factors also matter  

---

## Model Overview

- **Models Trained:** Logistic Regression, Decision Tree, Gradient Boosting  
- **Evaluation Metrics:** Accuracy, Precision, Recall, F1-score, Confusion Matrix  
- **Feature Importance & LIME:** Used for **per-student prediction explanations**  

---

## Results Summary

| Model                  | Accuracy |
|------------------------|----------|
| Logistic Regression    | 0.77     |
| Decision Tree          | 0.56     |
| Gradient Boosting      | 0.72     |

### Logistic Regression - Additional Metrics

| Class | Precision | Recall | F1-score | Support |
|-------|----------|--------|----------|---------|
| 0 (Fail) | 0.85   | 0.41   | 0.55     | 27      |
| 1 (Pass) | 0.76   | 0.96   | 0.85     | 52      |

> **Observation:** Logistic Regression effectively identifies passing students (high recall for class 1) but is less effective at detecting failing students (lower recall for class 0).  

---

## Deployment

- **Platform:** Streamlit  
- **Functionality:**  
  - Accepts student data input **manually or via file upload**  
  - Displays **pass/fail prediction, confidence scores, and LIME explanations**  
- **Live Link:** https://student-performance-prediction-and-early-intervention-grxr2ecs.streamlit.app/

---

## Installation

1. **Clone the repository:**  
```bash
git clone https://github.com/Keerthanajp18/Student-Performance-Prediction-and-Early-Intervention.git
