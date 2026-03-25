import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

# PAGE CONFIG 
st.set_page_config(page_title="Student Clustering", layout="wide")

st.title("🎓 Student Clustering System (K-Means)")

# LOAD DATA --
@st.cache_data
def load_data():
    df1 = pd.read_csv("student-mat.csv", sep=';')
    df2 = pd.read_csv("student-por.csv", sep=';')
    return pd.concat([df1, df2])

data = load_data()

st.subheader("📊 Dataset Preview")
st.dataframe(data.head())

#  PREPROCESS
df = data.copy()

le = LabelEncoder()
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = le.fit_transform(df[col])

X = df.drop(['G3'], axis=1)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# SELECT K 
st.subheader("Select Number of Clusters")

k = st.slider("Number of Clusters (K)", 2, 10, 3)

# K-MEANS
kmeans = KMeans(n_clusters=k, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

# SILHOUETTE SCORE 
score = silhouette_score(X_scaled, clusters)

st.subheader("Evaluation")
st.metric("Silhouette Score", round(score, 3))

# PCA FOR VISUALIZATION 
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# CLUSTER PLOT 
st.subheader("Cluster Visualization")

fig, ax = plt.subplots(figsize=(4, 4))  # smaller size
ax.scatter(X_pca[:, 0], X_pca[:, 1], c=clusters)

ax.set_title(f"Clusters (K = {k})")
ax.set_xlabel("PCA Component 1")
ax.set_ylabel("PCA Component 2")

col1, col2, col3 = st.columns([1, 2, 1])  # center
with col2:
    st.pyplot(fig)

#  ELBOW METHOD
st.subheader(" Elbow Method")

wcss = []
K_range = range(1, 11)

for i in K_range:
    km = KMeans(n_clusters=i, random_state=42)
    km.fit(X_scaled)
    wcss.append(km.inertia_)

fig2, ax2 = plt.subplots(figsize=(4, 4))  # smaller size
ax2.plot(K_range, wcss, marker='o')

ax2.set_title("Elbow Graph")
ax2.set_xlabel("Number of Clusters (K)")
ax2.set_ylabel("WCSS")

col1, col2, col3 = st.columns([1, 2, 1])  # center
with col2:
    st.pyplot(fig2)
