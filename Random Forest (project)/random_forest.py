import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import models from scikit learn module:
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, RandomForestRegressor
from sklearn import tree
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

col_names = ['age', 'workclass', 'fnlwgt', 'education', 'education-num',
             'marital-status', 'occupation', 'relationship', 'race', 'sex',
             'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']
df = pd.read_csv('adult.csv', header=None, names=col_names)
print(df.head())

print(df.info())
# Distribution of income
sns.countplot(data=df, x='income')
plt.show()
plt.close()

# Clean columns by stripping extra whitespace for columns of type "object"
for column in df.columns:
    if df[column].dtype == 'object':
        df[column] = df[column].str.strip()

# Create feature dataframe X with feature columns and dummy variables for categorical features
feature_cols = ['age', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week']
X = pd.get_dummies(df[feature_cols], drop_first=True)
# print(X)
# Create output variable y which is binary, 0 when income is less than 50k, 1 when it is greather than 50k
y = np.where(df.income == '<=50K', 0, 1)

# Split data into a train and test set
x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=1, test_size=0.2)

# Instantiate random forest classifier, fit and score with default parameters
rfc = RandomForestClassifier()
rfc.fit(x_train, y_train)
print(rfc.score(x_test, y_test))

# Tune the hyperparameter max_depth over a range from 1-25, save scores for test and train set
np.random.seed(0)
accuracy_train = []
accuracy_test = []

for i in range(1, 26, 1):
    rfc_cg = RandomForestClassifier(max_depth=i)
    rfc_cg.fit(x_train, y_train)
    accuracy_train.append(rfc_cg.score(x_train, y_train))
    rfc_cg.fit(x_test, y_test)
    accuracy_test.append(rfc_cg.score(x_test, y_test))

# Find the best accuracy and at what depth that occurs
best_accuracy = max(accuracy_test)
best_max_depth = accuracy_test.index(best_accuracy)
print("A maior acurácia foi de {}".format(best_accuracy))
print("A profundidade da árvore de decisão ótima é {}".format(best_max_depth))

# Plot the accuracy scores for the test and train set over the range of depth values
max_depth_graph = range(1, 26)
plt.plot(max_depth_graph, accuracy_train, label='treino')
plt.plot(max_depth_graph, accuracy_test, label='teste')
plt.xlabel('Profundidade da árvore')
plt.ylabel('Acurácia')
plt.legend()
plt.show()
plt.close()

# Save the best random forest model and save the feature importances in a dataframe
best_rf = RandomForestClassifier(max_depth=best_max_depth)
best_rf.fit(x_train, y_train)
feature_imp_df = pd.DataFrame(zip(x_train.columns, best_rf.feature_importances_), columns=['feature', 'importance'])
print('As 5 melhores variáveis do modelo random forest:')
print(feature_imp_df.sort_values('importance', ascending=False).iloc[0:5])

# Create two new features, based on education and native country
df['education_bin'] = pd.cut(df['education-num'], [0, 9, 13, 16],
                             labels=['HS or less', 'College to Bachelors', 'Masters or more'])

feature_cols = ['age',
                'capital-gain', 'capital-loss', 'hours-per-week', 'sex', 'race', 'education_bin']
# Use these two new additional features and recreate X and test/train split
X = pd.get_dummies(df[feature_cols], drop_first=True)

x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=1, test_size=0.2)

# Find the best max depth now with the additional two features
np.random.seed(0)
accuracy_train_new = []
accuracy_test_new = []

for i in range(1, 26, 1):
    rfc_new = RandomForestClassifier(max_depth=i)
    rfc_new.fit(x_train, y_train)
    accuracy_train_new.append(rfc_new.score(x_train, y_train))
    rfc_new.fit(x_test, y_test)
    accuracy_test_new.append(rfc_new.score(x_test, y_test))

best_accuracy = max(accuracy_test_new)
depths = accuracy_test_new.index(best_accuracy)
print("A maior acurácia do novo modelo foi de {}".format(best_accuracy))
print("A profundidade da árvore de decisão ótima do novo modelo é {}".format(depths))

# Save the best model and print the two features with the new feature set
max_depth_graph = range(1, 26)
plt.plot(max_depth_graph, accuracy_train_new, label='treino')
plt.plot(max_depth_graph, accuracy_test_new, label='teste')
plt.xlabel('Profundidade da árvore')
plt.ylabel('Acurácia')
plt.legend()
plt.show()
plt.close()

best_rf_new = RandomForestClassifier(max_depth=best_max_depth)
best_rf_new.fit(x_train, y_train)
feature_imp_df = pd.DataFrame(zip(x_train.columns, best_rf_new.feature_importances_), columns=['feature', 'importance'])
print('As 5 melhores variáveis do modelo random forest:')
print(feature_imp_df.sort_values('importance', ascending=False).iloc[0:5])

