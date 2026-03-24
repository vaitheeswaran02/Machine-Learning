import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# Read dataset
data = pd.read_csv("data2.csv")

# Convert categorical to numeric
data = pd.get_dummies(data)

# Take only first 2 features (important for plotting)
X = data.iloc[:, :-1].values[:, :2]
y = data.iloc[:, -1].values

# Train model
model = svm.SVC(kernel='linear')
model.fit(X, y)

# Plot points
plt.scatter(X[:, 0], X[:, 1], c=y)

# Get axis limits
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

# Create grid
xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)

# Predict decision boundary
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = model.decision_function(xy).reshape(XX.shape)

# Plot boundary
ax.contour(XX, YY, Z, levels=[0])

# Labels
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("SVM Decision Boundary")

plt.show()  

=====PCA====================

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Step 1: Read CSV
data = pd.read_csv("data1.csv")

# Step 2: Convert categorical → numeric (if any)
data = pd.get_dummies(data)

# Step 3: Split features and target
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Step 4: Standardize data (IMPORTANT)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 5: Apply PCA (reduce to 2 components)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Step 6: Plot PCA result
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y)

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA Visualization")

plt.show()

====decision treee===

import pandas as pandas
from sklearn.tree import decisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt 

data=pd.read_csv('dataset.csv')

data = pd.get_dumie(data)

x=data iloc[:,:-1]
y=data iloc[:,-1]

model= decisionTreeClassifier
mode.fit(x,y)

print('predict',model.predict(x.iloc[[0]]))
print('accuracy',model.score(x,y))

plt.figire(figsize=(12,7))
tree.plot_tree(model,feature_names=x.column,class_name=['no','yes'],field=true)
plt.show()


=====CANDIDATE ELIMINATION=======

import pandas as pd

# Load dataset
data = pd.read_csv('dataset.csv')
    
# Convert dataframe to list
data_list = data.values.tolist()

# Initialize S and G
S = data_list[0][:-1]   # first row (excluding target)
G = [['?' for _ in range(len(S))]]

# Consistency function
def consistent(h, x):
    for i in range(len(h)):
        if h[i] != '?' and h[i] != x[i]:
            return False
    return True

# Training
for row in data_list:

    if row[-1] == 'Yes':   # Positive example
        # Generalize S
        for i in range(len(S)):
            if S[i] != row[i]:
                S[i] = '?'

        # Remove inconsistent G
        G = [g for g in G if consistent(g, row)]

    else:   # Negative example
        new_G = []
        for g in G:
            if consistent(g, row):
                for i in range(len(S)):
                    if S[i] != row[i]:
                        new_h = ['?' for _ in range(len(S))]
                        new_h[i] = S[i]
                        new_G.append(new_h)
            else:
                new_G.append(g)

        G = new_G

# Output
print("Final S:", S)
print("Final G:", G)