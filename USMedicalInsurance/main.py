import pandas as pd
import numpy as np
file = pd.read_csv("C:\\Users\\Leonardo Mendes\\Desktop\\Leonardo Xavier\\6. PYTHON\\"
                   "python-portfolio-project-starter-files\\insurance.csv")
# print(file.dtypes)
# print(file.head())

# Armazenando as features em variáveis separadamente
age, sex, bmi, children, smoker, region, charges = file['age'], file['sex'], file['bmi'], file['children'],\
                                                   file['smoker'], file['region'], file['charges']
# Média da idade e bmi do dataset
average_age = np.mean(age)
average_bmi = np.mean(bmi)

# Média do valor do seguro para fumantes abaixo de 30 anos, entre 30 e 50 anos e maior que 50 anos
fumantes_menor_30 = file.loc[(smoker == 'yes') & (age <= 30)]
valor_f_m_30 = np.mean(fumantes_menor_30['charges'])
print("O valor médio do plano de saúde para fumantes abaixo de 30 anos é: {:.2f}".format(valor_f_m_30))

fumantes_entre_30_50 = file.loc[(smoker == 'yes') & (age > 30) & (age <= 50)]
valor_f_m_30_50 = np.mean(fumantes_entre_30_50['charges'])
print("O valor médio do plano de saúde para fumantes entre 30 e 50 anos é: {:.2f}".format(valor_f_m_30_50))

fumantes_maior_50 = file.loc[(smoker == 'yes') & (age > 50)]
valor_f_m_50 = np.mean(fumantes_maior_50['charges'])
print("O valor médio do plano de saúde para fumantes maiores que 50 anos é: {:.2f}".format(valor_f_m_50))

# De onde são os maiores clientes do plano de saúde
# print(pd.unique(region))
qtd_por_regiao = region.value_counts()
print("A quantidade de clientes por região é:\n{}".format(qtd_por_regiao))

# Diferença do custo médio do plano de saúde de fumantes para não fumantes
custo_fumantes = np.mean(file.loc[(smoker == 'yes')]['charges'])
custo_nao_fumantes = np.mean(file.loc[(smoker == 'no')]['charges'])
print("O custo médio do plano de saúde para pessoas fumantes é de ${:.2f},"
      " já para os usuários não fumantes o custo é de ${:.2f}."
      " A diferença entre as médias desses custos é de ${:.2f}.\n"
      .format(custo_fumantes, custo_nao_fumantes, custo_fumantes-custo_nao_fumantes))

# Custo médio do plano de saúde para pessoas que possuem pelo menos um (a) filho (a)
custo_filhos = np.mean(file.loc[(children == 1)]['charges'])
media_idade_pessoas_1filho = np.mean(file.loc[(children == 1)]['age'])
print("O custo médio do plano de saúde para pessoas com 1 filho é de ${:.2f}. A idade média das pessoas que tem 1 filho"
      " é de: {:2f}".format(custo_filhos, media_idade_pessoas_1filho))

# Qual o sexo da maioria das pessoas presentes no dataset
qtd_sexo = sex.value_counts()
print("A quantidade de pessoas por sexo é:\n{}".format(qtd_sexo))