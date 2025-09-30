from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Load dataset and train model
iris = load_iris()
clf = DecisionTreeClassifier(random_state=0)
clf.fit(iris.data, iris.target)

# Feature importances
feature_importances = clf.feature_importances_
for feature, importance in zip(iris.feature_names, feature_importances):
    print(f"Feature: {feature}, Importance: {importance:.2f}")
