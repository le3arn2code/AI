from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_graphviz
import graphviz

# Load dataset and train model
iris = load_iris()
clf = DecisionTreeClassifier(random_state=0)
clf.fit(iris.data, iris.target)

# Export decision tree to DOT format
dot_data = export_graphviz(
    clf, out_file=None,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True, rounded=True,
    special_characters=True
)

# Generate graph
graph = graphviz.Source(dot_data)
graph.render("iris_tree")  # saves as iris_tree.pdf
print("✅ Decision Tree saved as iris_tree.pdf")
