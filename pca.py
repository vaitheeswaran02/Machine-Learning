import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

st.title("PCA Visualization")

# Load CSV directly
data = pd.read_csv("data1.csv")
data = pd.get_dummies(data)

st.write("Dataset Preview:", data.head())

# Split features and target
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Standardize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

st.write(f"Explained variance ratio: {pca.explained_variance_ratio_}")

# Plot PCA result
fig, ax = plt.subplots()
scatter = ax.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis')
ax.set_xlabel("Principal Component 1")
ax.set_ylabel("Principal Component 2")
ax.set_title("PCA Visualization")
legend = ax.legend(*scatter.legend_elements(), title="Classes")
ax.add_artist(legend)

st.pyplot(fig)
