import joblib
from sklearn.linear_model import LogisticRegression
import numpy as np

X = np.random.rand(20, 5)
y = [1 if x[0] > 0.4 else 0 for x in X]

model = LogisticRegression().fit(X, y)
joblib.dump(model, 'models/outcome_classifier.joblib')
print("Outcome classifier trained.")
