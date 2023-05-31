import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd

# Carregar o conjunto de dados
data = load_breast_cancer()

# Criar um DataFrame usando os dados
df = pd.DataFrame(data.data, columns=data.feature_names)

# Adicionar a coluna de destino ao DataFrame
df['target'] = data.target

# Exibir as primeiras linhas do DataFrame
print(df.head(25))

# Analisando variáveis
no_cancer = df[df['target'] == 0]
print(no_cancer.describe())

cancer = df[df['target'] == 1]
print(cancer.describe())

# Separando o X e Y para ser analisado
X = df[['mean concavity', 'mean concave points', 'worst area']]
Y = df[['target']]

# Realizando a normalização dos dados
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)

# Dividindo os dados em treino e teste
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=27)

# Criando o modelo e ajustando (fit)
model = LogisticRegression()
model.fit(X_train, y_train)

# Saídas
y_pred = model.predict(X_test)
print(y_pred)

# Métricas
# accuracy:
print(accuracy_score(y_test, y_pred))

# precision:
print(precision_score(y_test, y_pred))

# recall:
print(recall_score(y_test, y_pred))

# F1 score
print(f1_score(y_test, y_pred))