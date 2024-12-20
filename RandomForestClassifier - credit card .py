# -*- coding: utf-8 -*-
"""Data Mining.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EaBHmTAVOEZWw8ygiO82EsmI4-oCKvS_

## CreditCard
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('creditcard.csv')
X = df['Amount'].values.reshape(-1, 1)
y = df['Class']
df

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

cr = classification_report(y_test, y_pred)
print("Classification Report:")
print(cr)

akurasi = accuracy_score(y_test, y_pred)
akurasi = akurasi*100
print(f"Akurasi yang kami dapat adalah {akurasi:.2f}%")

TP = cm[0][0]  # True Positives
FP = cm[0][1]  # False Positives
TN = cm[1][1]  # True Negatives
FN = cm[1][0]  # False Negatives

TPR = TP / (TP + FN)  # True Positive Rate
FPR = FP / (FP + TN)  # False Positive Rate
TNR = TN / (TN + FP)  # True Negative Rate
FNR = FN / (TP + FN)  # False Negative Rate

print("Confusion Matrix:")
print(confusion_matrix)
print("Metrik Kinerja:")
print(f"True Positive Rate (TPR): {TPR:.2f}")
print(f"False Positive Rate (FPR): {FPR:.2f}")
print(f"True Negative Rate (TNR): {TNR:.2f}")
print(f"False Negative Rate (FNR): {FNR:.2f}")

cm_df = pd.DataFrame(cm, index=['Legal(0)', 'Penipuan(1)'], columns=['Prediksi Legal', 'Prediksi Penipuan'])
print(cm_df.to_string())

plt.figure(figsize=(8, 6))
cm_df.plot(kind='bar', color=['pink', 'purple'])
plt.xlabel('Class')
plt.ylabel('Class Hasil Prediksi')
plt.title('Confusion Matrix')
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot([TPR, FPR, TNR, FNR], marker='o', linestyle='-')
plt.xlabel('Metric')
plt.ylabel('Rate')
plt.title('Performance Metrics')
plt.xticks([0, 1, 2, 3], ['TPR', 'FPR', 'TNR', 'FNR'])
plt.grid(True)
plt.show()

cost_fp = 100  # Biaya False Positives (FP)
cost_fn = 100 # Biaya False Negative

rata_kelas= df.groupby('Class')['Amount'].mean()
print(rata_kelas)

FP = cm[0, 1]
FN = cm[1, 0]

costFp = (FP * 88.291022 )
costFn = (FN * 122.211321)
print(costFp)
print(costFn)
total_cost = (FP * cost_fp) + (FN * cost_fn)

print("Total biaya:", total_cost)

cost_metrics = ['FP', 'FN']
values = [costFp, costFn]
plt.bar(cost_metrics, values)
plt.xlabel('Cost Metrics')
plt.ylabel('Values')
plt.title('Perbandingan Cost Metrics')
plt.show()
