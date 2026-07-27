from sklearn.datasets import load_iris


iris = load_iris()

# Features
X = iris.data

# Target
y = iris.target

print("Shape of X:", X.shape)
print("Shape of y:", y.shape)

print("\nFirst Sample:")
print(X[0])

print("\nFirst Label:")
print(y[0])

print("\nFeature Names:")
print(iris.feature_names)

print("\nTarget Names:")
print(iris.target_names)