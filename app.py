import  streamlit as st 
import pandas as pd
import joblib
import numpy as np
from lime.lime_tabular import LimeTabularExplainer

# -----------------------------
# Load model and feature columns
# -----------------------------
model = joblib.load("student_model.pkl")
feature_columns = joblib.load("feature_columns.pkl")

# -----------------------------
# Create LIME explainer (SAFE METHOD)
# -----------------------------
training_data = np.random.rand(100, len(feature_columns))

explainer = LimeTabularExplainer(
    training_data,
    feature_names=feature_columns,
    class_names=["Fail", "Pass"],
    mode="classification"
)

st.title("🎓 Student Performance Prediction")

st.write("Enter student details:")

# -----------------------------
# User Inputs
# -----------------------------
age = st.slider("Age", 15, 22, 17)
studytime = st.slider("Study Time (1-4)", 1, 4)
absences = st.slider("Absences", 0, 30)
failures = st.slider("Past Failures", 0, 4)
Medu = st.slider("Mother's Education (0-4)", 0, 4)
Fedu = st.slider("Father's Education (0-4)", 0, 4)

sex = st.selectbox("Sex", ['F','M'])
address = st.selectbox("Address", ['U','R'])
famsize = st.selectbox("Family Size", ['LE3','GT3'])
Pstatus = st.selectbox("Parents Together?", ['T','A'])
Mjob = st.selectbox("Mother Job", ['teacher','health','services','other','at_home'])
Fjob = st.selectbox("Father Job", ['teacher','health','services','other','at_home'])
guardian = st.selectbox("Guardian", ['mother','father','other'])

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict"):

    # Base numeric features
    input_dict = {
        'age': age,
        'studytime': studytime,
        'absences': absences,
        'failures': failures,
        'Medu': Medu,
        'Fedu': Fedu
    }

    # Convert to DataFrame
    input_df = pd.DataFrame([input_dict])

    # -----------------------------
    # Handle categorical variables
    # -----------------------------
    cat_data = pd.DataFrame({
        'sex':[sex],
        'address':[address],
        'famsize':[famsize],
        'Pstatus':[Pstatus],
        'Mjob':[Mjob],
        'Fjob':[Fjob],
        'guardian':[guardian]
    })

    cat_encoded = pd.get_dummies(cat_data)

    # Merge numeric + categorical
    input_df = pd.concat([input_df, cat_encoded], axis=1)

    # -----------------------------
    # Align columns with training
    # -----------------------------
    input_df = input_df.reindex(columns=feature_columns, fill_value=0)

    # -----------------------------
    # Prediction
    # -----------------------------
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0]

    # -----------------------------
    # Output
    # -----------------------------
    if prediction == 1:
        st.success("✅ Student will PASS")
    else:
        st.error("❌ Student will FAIL")

    st.write(f"Confidence: {max(probability)*100:.2f}%")

    st.write("### Prediction Probabilities")
    prob_df = pd.DataFrame({
        "Result": ["Fail", "Pass"],
        "Probability": probability
    })
    st.bar_chart(prob_df.set_index("Result"))

    # -----------------------------
    
    # -----------------------------
    st.write("### Why this prediction? (LIME Explanation)")

    exp = explainer.explain_instance(
        input_df.values[0],
        model.predict_proba,
        num_features=5
    )

    st.pyplot(exp.as_pyplot_figure())

# -----------------------------
st.write("---")
st.write("Built with ML + Streamlit 🚀")
