import seaborn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the data
transactions = pd.read_csv('transactions_modified.csv')
print(transactions.head())
print(transactions.info())

# How many fraudulent transactions?
print(np.sum(transactions.isFraud[transactions.isFraud == 1]))

# Summary statistics on amount column
print(transactions.amount.describe())

plt.hist(transactions.amount)
plt.xlabel("Amount of money in dollar")
plt.ylabel("Transactions")
plt.title("Evaluating the amount of money in transactions")
plt.show()

# Create isPayment field
transactions['isPayment'] = (transactions['type'].isin(['PAYMENT', 'DEBIT']).astype(int))

# Create isMovement field
transactions['isMovement'] = (transactions['type'].isin(['CASH_OUT', 'TRANSFER']).astype(int))

# Create accountDiff field
transactions['accountDiff'] = abs(transactions.oldbalanceOrg - transactions.oldbalanceDest)

# Create features and label variables
X = transactions[['amount', 'isPayment', 'isMovement', 'accountDiff']]
label = transactions[['isFraud']]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, label, test_size=0.3, random_state = 10)

# Normalize the features variables
scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)

# Fit the model to the training data
model = LogisticRegression()
model.fit(X_train, y_train)

# Score the model on the training data
print(model.score(X_train, y_train))

# Score the model on the test data
print(model.score(X_test, y_test))

# Print the model coefficients
print(model.coef_, model.intercept_)

# New transaction data
transaction1 = np.array([123456.78, 0.0, 1.0, 54670.1])
transaction2 = np.array([98765.43, 1.0, 0.0, 8524.75])
transaction3 = np.array([543678.31, 1.0, 0.0, 510025.5])

# Create a new transaction
your_transactions = np.array([75500.12, 0.0, 1.0, 15002.1])

# Combine new transactions into a single array
# Aqui os arrays precisam ser passados como uma tupla!
sample_transactions = np.stack((transaction1, transaction2, transaction3, your_transactions))

# Normalize the new transactions
scaler = StandardScaler()
scaler.fit(sample_transactions)
sample_transactions = scaler.transform(sample_transactions)

# Predict fraud on the new transactions
pred = model.predict(sample_transactions)
print(pred)

# Show probabilities on the new transactions
pred_prob = model.predict_proba(sample_transactions)
print(pred_prob)
