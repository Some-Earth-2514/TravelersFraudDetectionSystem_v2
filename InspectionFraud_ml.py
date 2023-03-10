import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

df = pd.read_csv("Inspection fraud 0-1.csv")

plt.scatter(df.APPR_DAM_EST_REC_CNT, df.FRAUD, marker="+", color="red")
# plt.show()

X_train, X_test, Y_train, Y_test = train_test_split(df[["APPR_DAM_EST_REC_CNT"]], df.FRAUD, test_size=0.9)

model = LogisticRegression()
model_fit = model.fit(X_train, Y_train)

predict_X_test = model.predict(X_test)
print(predict_X_test)

score_test = model.score(X_test, Y_test)
print(score_test)

predict_prob_X_test = model.predict_proba(X_test)
print(predict_prob_X_test)


cm = confusion_matrix(Y_test, predict_X_test)

sns.heatmap(cm, annot=True, cmap="Blues")
plt.xlabel("Predicted Labels")
plt.ylabel("True Labels")
plt.show()
