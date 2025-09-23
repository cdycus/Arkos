import joblib
from sklearn.linear_model import LogisticRegression
import numpy as np

X = np.random.rand(20, 4)
y = [1 if x[0] > 0.5 else 0 for x in X]

model = LogisticRegression().fit(X, y)
joblib.dump(model, 'models/emotion_model.joblib')
print("Emotion model trained.")
