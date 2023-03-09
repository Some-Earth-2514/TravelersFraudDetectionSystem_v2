# importing required libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix

# loading the dataset into a pandas dataframe
data = pd.read_csv('Indemnity fraud 0-1.csv')

# encoding the categorical feature "VEH_PRIMARY_PT_OF_DAMAGE" into numerical values
le = LabelEncoder()
data['VEH_PRIMARY_PT_OF_DAMAGE'] = le.fit_transform(data['VEH_PRIMARY_PT_OF_DAMAGE'])

# splitting the dataset into training and testing data
X = data.drop('FRAUD', axis=1)
y = data['FRAUD']
print(y)

plt.scatter(data['CLAIM_INDEMNITY_EST_AMT'], data['VEH_PRIMARY_PT_OF_DAMAGE'], c=data['FRAUD'])
plt.xlabel('Claim Indemnity Estimated Amount')
plt.ylabel('Vehicle Primary Point of Damage')
plt.title('Fraud Detection Scatter Plot')
# plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# training the logistic regression model on the training data
model = LogisticRegression()
model.fit(X_train, y_train)

# predicting the probability of fraud on the testing data using the trained model
y_pred_prob = model.predict_proba(X_test)[:, 1]
y_pred = np.where(y_pred_prob > 0.5, 1, 0)

score_test = model.score(X_test, y_test)


# evaluating the performance of the model using accuracy, precision, recall, and F1-score
print(y_pred_prob)
print(y_pred)
print(score_test)


print('Accuracy:', accuracy_score(y_test, y_pred))
print('Precision:', precision_score(y_test, y_pred))
print('Recall:', recall_score(y_test, y_pred))
print('F1-score:', f1_score(y_test, y_pred))


cm = confusion_matrix(y_test, y_pred)

sns.heatmap(cm, annot=True, cmap="Blues")
plt.xlabel("Predicted Labels")
plt.ylabel("True Labels")
plt.show()
