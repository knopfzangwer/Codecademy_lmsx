from sklearn.datasets import load_breast_cancer
breast_cancer_data = load_breast_cancer()
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from matplotlib import pyplot as plt

# Analisando os dados e os nomes das colunas do dataset
print(breast_cancer_data.feature_names)
print(breast_cancer_data.data[0])
# Visualizando os pontos de saída e qual a variável de saída atribuída
print(breast_cancer_data.target)
print(breast_cancer_data.target_names)
# Separando os dados para treino e validação
training_data, validation_data, training_labels, validation_labels = train_test_split(breast_cancer_data.data, breast_cancer_data.target, test_size = 0.2, random_state = 75)
# Verificando se os dados foram separados corretamente
print(len(training_data), len(training_labels))
# Instanciando o método de classificação KNN na variável classifier
classifier = KNeighborsClassifier(n_neighbors = 3)
# Ajustando o nosso modelo aos pontos de treino
classifier.fit(training_data, training_labels)
# Mostrando qual score obtido para esse valor de k
print(classifier.score(validation_data, validation_labels))
# Encontrando qual o k que obtém a melhor acurácia para esse modelo
find_best_k = []
for k in range(1, 101):
  classifier = KNeighborsClassifier(n_neighbors = k)
  classifier.fit(training_data, training_labels)
  print("Para um k igual a {}".format(k))
  print(classifier.score(validation_data, validation_labels))
  find_best_k.append([k, classifier.score(validation_data, validation_labels)])

max_value = max(find_best_k, key=lambda x: x[1])
print("Valor com melhor score:", max_value[1])
print("Valor k:", max_value[0])

# Criando a lista de k's e obtendo apenas o valor da acurácia para realizar o plot acurácia vs k
k_list = range(1, 101, 1)
accuracies = [sublista[1] for sublista in find_best_k]
plt.plot(k_list, accuracies)
plt.xlabel('k')
plt.ylabel('Validation Accuracy')
plt.title('Breast Cancer Classifier Accuracy')
plt.show()