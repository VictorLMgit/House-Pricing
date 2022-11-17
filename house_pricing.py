# -*- coding: utf-8 -*-
"""house_pricing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/VictorLMgit/a12d349c04b1de0245689397b3bfa6be/house_pricing.ipynb
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

"""#Conhecendo o Dataset"""

dataset = pd.read_csv('houses_prices.csv')
dataset.head(5)

# Sem dados nulos
dataset.isnull().sum()

"""#Análises Iniciais (Estatísticas Descritivas)"""

dataset.describe()

"""# Separando variáveis explicativas de dependentes escolhidas para a análise"""

Y = dataset.Prices
Y

dataset.corr()

X = dataset[['Area','Floors', 'Fiber', 'Baths' , 'White Marble']]
X

"""# Analisando Comportamento da variável dependente com seaborn"""

import seaborn as sns

ax = sns.boxplot(data=Y, orient = 'h', width=0.5)
ax.set_title('Preços', fontsize=20)
ax.figure.set_size_inches(12,6)
ax.set_xlabel('Valor', fontsize = 14)

# Nota-se que a variável dependente segue uma distribuição próxima à normal.
ax = sns.histplot(Y)
ax.set_title('Preços', fontsize=20)
ax.figure.set_size_inches(12,6)
ax.set_xlabel('Valor', fontsize = 14)

"""## Comparando a variável dependente com as explicativas

### Price X White Marble
"""

ax = sns.boxplot(y = 'White Marble', x = 'Prices', data=dataset, orient = 'h', width=0.5)
ax.set_title('Price X White Marble')
ax.figure.set_size_inches(12,6)
ax.set_xlabel('Price', fontsize = 14)
ax.set_ylabel('White Marble', fontsize = 14)

"""### Price X Fiber"""

ax = sns.boxplot(y = 'Fiber', x = 'Prices', data=dataset, orient = 'h', width=0.5)
ax.set_title('Price X Fiber')
ax.figure.set_size_inches(12,6)
ax.set_xlabel('Price', fontsize = 14)
ax.set_ylabel('Fiber', fontsize = 14)

"""Price X Floor"""

ax = sns.boxplot(y = 'Floors', x = 'Prices', data=dataset, orient = 'h', width=0.5)
ax.set_title('Price X Floors')
ax.figure.set_size_inches(12,6)
ax.set_xlabel('Price', fontsize = 14)
ax.set_ylabel('Floors', fontsize = 14)

"""###Price X Baths

"""

ax = sns.boxplot(y = 'Baths', x = 'Prices', data=dataset, orient = 'h', width=0.5)
ax.set_title('Price X Baths')
ax.figure.set_size_inches(12,6)
ax.set_xlabel('Price', fontsize = 14)
ax.set_ylabel('Baths', fontsize = 14)

"""### Price X Area"""

# ax = sns.pairplot(dataset, y_vars = 'Prices', x_vars=['Area'], kind='reg')
# ax.fig.suptitle("Dispersão entre as variaveis", fontsize = 20, y = 1.05)
# ax.figure.set_size_inches(20,6)

# ax = sns.pairplot(dataset, y_vars = 'Prices', x_vars=['Floors', 'Fiber', 'Baths' , 'White Marble'], kind='reg')
# ax.fig.suptitle("Dispersão entre as variaveis", fontsize = 20, y = 1.05)
# ax.figure.set_size_inches(20,6)

"""#Estimando um Modelo de Regressão Linear"""

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=2811)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

"""###Importando Bibliotecas de modelos de regressão"""

from sklearn.linear_model import LinearRegression
from sklearn import metrics

"""###Treinando o modelo"""

modelo = LinearRegression()
modelo.fit(X_train, y_train)

"""### Coeficiente de Determinação - R²

O quanto a linha de regressão ajusta-se aos dados.

$$R^2(y, \hat{y}) = 1 - \frac {\sum_{i=0}^{n-1}(y_i-\hat{y}_i)^2}{\sum_{i=0}^{n-1}(y_i-\bar{y}_i)^2}$$
"""

print('R² = {}'.format(modelo.score(X_train, y_train).round(2)))

"""###Prevendo resultados"""

y_predict = modelo.predict(X_test)

X_test[0:1]



"""## Obtendo o coeficiente de determinação (R²) para as previsões do modelo

"""

print("R² = %s" % metrics.r2_score(y_test, y_predict).round(2))

"""## Criando um simulador de preços

"""

Area = 12
Floors = 0
Fiber = 0
Baths = 1
White_Marble = 0
entrada = [[Area, Floors, Fiber, Baths, White_Marble]]
modelo.predict(entrada)

