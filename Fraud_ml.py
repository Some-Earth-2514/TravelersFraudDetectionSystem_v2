import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("Indemnity fraud 0-1.csv")
# df.head()

plt.scatter(df.CLAIM_INDEMNITY_EST_AMT, df.FRAUD, marker="+", color="red")
plt.show()

X_train, X_test, Y_train, Y_test = train_test_split(df[["CLAIM_INDEMNITY_EST_AMT"]], df.FRAUD, test_size=0.9)
print(X_test)

model = LogisticRegression()
model_fit = model.fit(X_train, Y_train)  # training for model

predict_X_test = model.predict(X_test)
print(predict_X_test)

score_test = model.score(X_test, Y_test)
print(score_test)

predict_prob_X_test = model.predict_proba(X_test)
print(predict_prob_X_test)
