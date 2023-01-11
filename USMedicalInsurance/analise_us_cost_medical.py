import pandas as pd
import numpy as np
file = pd.read_csv("C:\\Users\\Leonardo Mendes\\Desktop\\Leonardo Xavier\\6. PYTHON\\"
                   "python-portfolio-project-starter-files\\insurance.csv")
# print(file.dtypes)
# print(file.head())

# Armazenando as features em variáveis separadamente
age, sex, bmi, children, smoker, region, charges = file['age'], file['sex'], file['bmi'], file['children'],\
                                                   file['smoker'], file['region'], file['charges']
# Média da idade, bmi e custo do dataset
average_age = np.mean(age)
average_bmi = np.mean(bmi)
average_cost = np.mean(charges)

# Qual o sexo da maioria das pessoas presentes no dataset
qtd_sexo = sex.value_counts()
print("A quantidade de pessoas por sexo é:\n{}".format(qtd_sexo))

# Média do valor do seguro para fumantes baseado na idade fixa e definindo condições para análise
# As condições aceitas para esta função são: >, ==, <;
# Para variável fumante: "yes" ou "no";
def valor_seguro_fumantes_idade_fixa(idade, condicao, fumante):
    if (fumante == "yes") or (fumante == "no"):
        if (condicao == '>') or (condicao == '==') or (condicao == '<'):
            if fumante == 'yes':
                if condicao == "==":
                    fumantes = file.loc[(smoker == fumante) & (age == idade)]
                    valor = np.mean(fumantes['charges'])
                    print("O valor médio do plano de saúde para fumantes de " + str(idade) + " anos é de ${:.2f}.".format(valor))
                elif condicao == ">":
                    fumantes = file.loc[(smoker == fumante) & (age > idade)]
                    valor = np.mean(fumantes['charges'])
                    print("O valor médio do plano de saúde para fumantes com idade superior a "
                      + str(idade) + " anos é de ${:.2f}.".format(valor))
                elif condicao == "<":
                    fumantes = file.loc[(smoker == fumante) & (age < idade)]
                    valor = np.mean(fumantes['charges'])
                    print("O valor médio do plano de saúde para fumantes com idade inferior a "
                      + str(idade) + " anos é de ${:.2f}.".format(valor))
            elif fumante == 'no':
                if condicao == "==":
                    fumantes = file.loc[(smoker == fumante) & (age == idade)]
                    valor = np.mean(fumantes['charges'])
                    print("O valor médio do plano de saúde para não fumantes de " + str(idade) + " anos é de ${:.2f}.".format(valor))
                elif condicao == ">":
                    fumantes = file.loc[(smoker == fumante) & (age > idade)]
                    valor = np.mean(fumantes['charges'])
                    print("O valor médio do plano de saúde para não fumantes com idade superior a "
                      + str(idade) + " anos é de ${:.2f}.".format(valor))
                elif condicao == "<":
                    fumantes = file.loc[(smoker == fumante) & (age < idade)]
                    valor = np.mean(fumantes['charges'])
                    print("O valor médio do plano de saúde para não fumantes com idade inferior a "
                      + str(idade) + " anos é de ${:.2f}.".format(valor))
        else:
            print("Verifique se está utilizando corretamente o operador lógico. Apenas permitido >, == ou <.")
    else:
        print("Identifique corretamente se a pessoa é fumante ou não com 'yes' ou 'no'.")

valor_seguro_fumantes_idade_fixa(30, ">", "yes")

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
