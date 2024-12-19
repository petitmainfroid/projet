But<br>
P1 :<br> Basé sur un ensemble de données connu, effectuer des prédictions en utilisant un modèle gaussien.
J'ai supposé que tous les paramètres sont linéaires pour les prédictions (ce qui n'est pas le cas pour certains paramètres comme Cylindre, Model, etc.).

P2 :<br> Nettoyer un ensemble de données récupéré par web scraping pour créer un calculateur d'émissions de carbone interactif avec l'utilisateur.

Principe
P1 :
La principale difficulté est que certaines colonnes des données sont de type string. Ces colonnes peuvent être classées en deux catégories :

Les colonnes avec peu de catégories, comme Transmission. Pour ces colonnes, j'ai utilisé l'encodage One-Hot :

```
X = pd.get_dummies(data.drop(columns=['CO2 emissions (g/km)', 'Model']), drop_first=True)
```
Les colonnes avec un grand nombre de catégories, comme Model. Pour ces colonnes, j'ai utilisé l'encodage Target :
```
model_target_mean = data.groupby('Model')['CO2 emissions (g/km)'].mean()
data['Model_Target'] = data['Model'].map(model_target_mean)
data_encoded['Model_Target'] = data['Model'].map(model_target_mean)
```
Cependant, une question subsiste : j'ai remarqué que les relations entre certaines colonnes, comme Model ou Cylindre, et les émissions de CO2 ne sont pas linéaires. Mais lorsque j'ai essayé d'entraîner le modèle avec ou sans la colonne Model dans l'ensemble d'entraînement, les résultats (R²) sont respectivement :

Sans Model : [0.9953694577584278]
Avec Model : [0.9956066979098889]
Cela montre que l'ajout de la colonne Model améliore légèrement la performance.

P2 :
Les principales difficultés sont :

Nettoyage des données : J'ai passé beaucoup de temps à comprendre comment nettoyer les données, car les tutoriels en ligne étaient souvent trop basiques.
Compréhension des objectifs : Par exemple, au début, je pensais qu'il fallait effectuer une prédiction pour chaque type d'aliment, alors qu'il suffisait de calculer des moyennes pour chaque catégorie.
Fonctionnalités proposées
Dans le fichier ols.py :

fit :<br>
Cette fonction calcule l'estimateur de β.

predict : <br>
Utilisée pour prédire les émissions de CO2 à partir des informations fournies.
(Je pourrais écrire directement les valeurs de β dans le fichier pour une prédiction en O(1), mais je préfère effectuer le calcul dynamique pour plus de flexibilité. Merci de considérer que j'ai conscience de cette optimisation possible si des points sont attribués pour l'efficacité.)
determination_coefficient :
Calcule le coefficient de détermination R².

hat_sigma :<br>
Calcule σ chapeau (variance résiduelle).<br>

visualize_results :<br>
Visualise les résultats du modèle, y compris :

La comparaison entre les valeurs réelles et prédites.
Le graphe des résidus.
Dans le fichier main.py :

calculate :<br>
Un exemple de programme pour calculer l'empreinte carbone.
Les valeurs sont basées sur le fichier means_output.csv et les entrées de l'utilisateur.
