# Un référentiel contient tous les fichiers de votre projet
# et l'historique des révisions de chaque fichier. 
# Vous pouvez discuter et gérer le travail de votre projet dans le référentiel.

# Search repositories : Find repositories via various criteria. 
#   This method returns up to 100 results per page.
# When searching for repositories, you can get text match metadata for the name and description fields
#    when you pass the text-match media type. 
# For example, if you want to search for popular Tetris repositories written in assembly code, 
# your query might look like this:
# q=tetris+language:assembly&sort=stars&order=desc
# This query searches for repositories with the word tetris in the name, the description, or the README.
# The results are limited to repositories where the primary language is assembly. 
# The results are sorted by stars in descending order, so that the most popular repositories appear first in the search results.

import requests
import numpy as np
import matplotlib.pyplot as plt
import sklearn

url = 'https://api.github.com/search/repositories?q=microsoft+language:python&sort=forks&per_page=100&page=2'
repositories = requests.get(url)
repo = repositories.json()
# print(repo) : imprime en une seule ligne
items = repo['items']
# forks = items[0] : premier de la liste
forks = [repo['forks_count'] for repo in items]
print(forks)
stars = [repo['stargazers_count'] for repo in items]
print(stars)

# Les tableaux (en anglais, array) peuvent être créés avec numpy.array().
# On utilise des crochets pour délimiter les listes d’éléments dans les tableaux.
stars_array = np.array([stars])
forks_array = np.array([forks])
print(stars_array)
print(forks_array)

model = np.polyfit(forks, stars, 1)
print(model)

plt.scatter(forks, stars)
plt.xlabel('Forks')
plt.ylabel('Stars')
plt.show()

from sklearn.model_selection import train_test_split
forks_train, forks_test, stars_train, stars_test = train_test_split(forks_array, stars_array, test_size=1/5, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(forks_train.reshape(-1,1), stars_train)
LinearRegression()

print(regressor.coef_)
print(regressor.intercept_)

