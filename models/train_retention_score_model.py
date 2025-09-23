import joblib
from sklearn.linear_model import LogisticRegression
import numpy as np

X = np.random.rand(20, 2)
y = [1 if sum(x) > 1 else 0 for x in X]

model = LogisticRegression().fit(X, y)
joblib.dump(model, 'models/retention_score_model.joblib')
print("Retention score model trained.")
