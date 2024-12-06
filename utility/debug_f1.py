import numpy as np
from sklearn.metrics import f1_score
y_true_empty = [0, 0, 0, 0, 0, 0]
y_pred_empty = [0, 0, 0, 0, 0, 0]
print(f1_score(y_true_empty, y_pred_empty,labels = [0, 1], zero_division=1))
