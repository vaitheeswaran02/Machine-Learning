import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, ConfusionMatrixDisplay,
    roc_curve, auc
)

st.title("🎓 Student Pass/Fail Prediction")

# -------- LOAD DATA --------
@st.cache_data
def load_data():
    df1 = pd.read_csv("student-mat.csv", sep=';')
    df2 = pd.read_csv("student-por.csv", sep=';')
    return pd.concat([df1, df2])

data = load_data()

# -------- PREPROCESS --------
data['result'] = data['G3'].apply(lambda x: 1 if x >= 10 else 0)

df = data.copy()

le = LabelEncoder()
encoders = {}

for col in df.columns:
    if df[col].dtype == 'object':
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        encoders[col] = le   # save encoder

X = df.drop(['G3', 'result'], axis=1)
y = df['result']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# -------- MODEL --------
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# USER INPUT 
st.subheader(" Enter Student Details")

input_data = {}

for col in X.columns:
    if col == "sex":
        choice = st.selectbox("Select Sex", ["F", "M"])
        input_data[col] = encoders['sex'].transform([choice])[0]
    else:
        input_data[col] = st.number_input(f"{col}", value=0)

# 🚀 PREDICT BUTTON

if st.button("Predict"):

    input_df = pd.DataFrame([input_data])
    input_scaled = scaler.transform(input_df)

    result = model.predict(input_scaled)[0]

    # -------- RESULT --------
    st.subheader("Prediction Result")

    if result == 1:
        st.success("✅ Student will PASS")
    else:
        st.error("❌ Student will FAIL")

    # -------- MODEL EVALUATION --------
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    st.subheader("Evaluation")

    st.write("Accuracy:", accuracy_score(y_test, y_pred))
    st.write("Precision:", precision_score(y_test, y_pred))
    st.write("Recall:", recall_score(y_test, y_pred))
    st.write("F1 Score:", f1_score(y_test, y_pred))

    # -------- CONFUSION MATRIX --------
    st.subheader("Confusion Matrix")

    fig, ax = plt.subplots()
    ConfusionMatrixDisplay(confusion_matrix(y_test, y_pred)).plot(ax=ax)
    st.pyplot(fig)

    # -------- ROC CURVE --------
    st.subheader(" ROC Curve")

    fpr, tpr, _ = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)

    fig2, ax2 = plt.subplots()
    ax2.plot(fpr, tpr, label=f"AUC = {roc_auc:.2f}")
    ax2.plot([0, 1], [0, 1], '--')
    ax2.legend()
    st.pyplot(fig2)