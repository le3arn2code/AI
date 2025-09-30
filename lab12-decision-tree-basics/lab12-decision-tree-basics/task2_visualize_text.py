from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Load dataset and train model
iris = load_iris()
clf = DecisionTreeClassifier(random_state=0)
clf.fit(iris.data, iris.target)

# Text-based representation
text_representation = tree.export_text(clf, feature_names=iris.feature_names)
print(text_representation)
