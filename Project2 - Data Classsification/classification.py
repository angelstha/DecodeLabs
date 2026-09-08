import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# -----------------------------------
# 1. Load the Iris dataset
# -----------------------------------

iris = load_iris()

X = iris.data
y = iris.target

print("===================================")
print("   IRIS FLOWER CLASSIFICATION AI")
print("===================================")

print("\nDataset loaded successfully!")
print("Number of samples:", len(X))
print("Number of features:", X.shape[1])

print("\nFlower classes:")
for i, name in enumerate(iris.target_names):
    print(i, "=", name)


# -----------------------------------
# 2. Split the dataset
# -----------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\n-----------------------------------")
print("DATASET SPLITTING")
print("-----------------------------------")

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))


# -----------------------------------
# 3. Create the KNN model
# -----------------------------------

model = KNeighborsClassifier(n_neighbors=3)

print("\n-----------------------------------")
print("MODEL")
print("-----------------------------------")

print("Algorithm: K-Nearest Neighbors (KNN)")
print("Number of neighbors:", 3)


# -----------------------------------
# 4. Train the model
# -----------------------------------

model.fit(X_train, y_train)

print("\nModel training completed!")


# -----------------------------------
# 5. Make predictions
# -----------------------------------

y_pred = model.predict(X_test)

print("\n-----------------------------------")
print("ACTUAL VS PREDICTED")
print("-----------------------------------")

for actual, predicted in zip(y_test, y_pred):
    print(
        f"Actual: {iris.target_names[actual]:12} "
        f"Predicted: {iris.target_names[predicted]}"
    )


# -----------------------------------
# 6. Calculate accuracy
# -----------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\n-----------------------------------")
print("MODEL PERFORMANCE")
print("-----------------------------------")

print(f"Accuracy: {accuracy * 100:.2f}%")


# -----------------------------------
# 7. Classification report
# -----------------------------------

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=iris.target_names
    )
)


# -----------------------------------
# 8. Confusion Matrix
# -----------------------------------

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(7, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    xticklabels=iris.target_names,
    yticklabels=iris.target_names
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Iris Flower Classification - Confusion Matrix")

plt.show()


# -----------------------------------
# 9. Test a NEW flower
# -----------------------------------

print("\n===================================")
print("   TEST YOUR OWN FLOWER")
print("===================================")

print("\nEnter the measurements of a flower.")

sepal_length = float(input("Sepal length (cm): "))
sepal_width = float(input("Sepal width (cm): "))
petal_length = float(input("Petal length (cm): "))
petal_width = float(input("Petal width (cm): "))

new_flower = [[
    sepal_length,
    sepal_width,
    petal_length,
    petal_width
]]

prediction = model.predict(new_flower)

predicted_class = iris.target_names[prediction[0]]

print("\n-----------------------------------")
print("AI PREDICTION")
print("-----------------------------------")

print("The AI predicts:", predicted_class)

print("\nPrediction completed!")