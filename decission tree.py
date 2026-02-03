import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder

# --------------------------------------------------
# Step 1: Create Dataset
# --------------------------------------------------
data = {
    'Study_Hours': ['High','High','Medium','Low','Low','Medium','Medium','High'],
    'Attendance': ['Good','Average','Good','Poor','Average','Average','Poor','Good'],
    'Assignment': ['Yes','Yes','Yes','No','Yes','Yes','No','Yes'],
    'Test_Score': ['High','Low','High','Low','Low','Low','Low','Low'],
    'Result': ['Pass','Pass','Pass','Fail','Fail','Pass','Fail','Pass']
}

df = pd.DataFrame(data)

# --------------------------------------------------
# Step 2: Label Encoding (SEPARATE encoders)
# --------------------------------------------------
encoders = {}
for col in df.columns:
    encoders[col] = LabelEncoder()
    df[col] = encoders[col].fit_transform(df[col])

print("Encoded Dataset:\n", df)

# --------------------------------------------------
# Step 3: Split Features and Target
# --------------------------------------------------
X = df[['Study_Hours', 'Assignment', 'Attendance', 'Test_Score']]
y = df['Result']

# --------------------------------------------------
# Step 4: Train Decision Tree (Entropy)
# --------------------------------------------------
model = DecisionTreeClassifier(
    criterion='entropy',
    max_depth=2,
    random_state=0
)
model.fit(X, y)
print("\nDecision Tree Model Trained Successfully")

# --------------------------------------------------
# Step 5: Classify New Sample (PROPER encoding)
# --------------------------------------------------
new_sample = pd.DataFrame({
    'Study_Hours': encoders['Study_Hours'].transform(['Medium']),
    'Assignment': encoders['Assignment'].transform(['Yes']),
    'Attendance': encoders['Attendance'].transform(['Good']),
    'Test_Score': encoders['Test_Score'].transform(['Low'])
})

prediction = model.predict(new_sample)

result_label = encoders['Result'].inverse_transform(prediction)
print("\nNew Student Prediction:")
print("Result =", result_label[0])

# --------------------------------------------------
# Step 6: Plot Decision Tree (NO entropy display)
# --------------------------------------------------
plt.figure(figsize=(14, 8))
plot_tree(
    model,
    feature_names=X.columns,
    class_names=encoders['Result'].classes_,
    filled=True,
    rounded=True,
    impurity=False
)
plt.title("Decision Tree (Entropy / ID3)")
plt.show()
