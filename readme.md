
## But

P1根据已知的数据集通过高斯模型进行预测
我将所有的参数都当成了线性的进行预测(其实包括 等参数都不是线性的)
P2从一个爬取的数据集中清洗出需要的数据
从而完成一个可与用户交互的碳排放计算器

### 原理

P1
其中的主要难点在于如何有些列的数据类型为string类型。其中又分为两种一直是这一列的值种类不多，例如 Transmission 这种列我采用了Hot Encoding的方法

```
X = pd.get_dummies(data.drop(columns=['CO2 emissions (g/km)', 'Model']), drop_first=True)
```
另一种则是这一列的种类也特别多，例如Model
对于这列我采用了Target Encoding
```
model_target_mean = data.groupby('Model')['CO2 emissions (g/km)'].mean()
data['Model_Target'] = data['Model'].map(model_target_mean)
data_encoded['Model_Target'] = data['Model'].map(model_target_mean)
```
我的疑问点在于我注意到了 对于例如Modle，cylindre这样的列他们与C02 emission之间的关系都不是线性的!但是我分别尝试了用不加入modle和加入modle这一列分别作为训练集其最后的预测结果体现在人R^2上分别为[0.9953694577584278]和[0.9956066979098889]
其表示为加入modle的效果会更好一些


P2<br>
P2的难点在于<br>
1.清洗数据，我花费了很多天才明白应该如何清洗(因为网上找到的很多清洗数据都非常的初级)<br>
2.明白究竟需要干什么，例如我一开始不能想到对不同种类的食物取平均值而是更想用预测。

##Fonction propose
我在Ols.py文件中提供了<br>
1,fit函数 用于计算estimateur de belta<br>
predict函数用于 根据给出的信息预测二氧化碳排放量
(需要提取用fit计算belta chabeau，我可以将belta 的值直接写入我的文件来达到O(1)预测，但是我偏向于提取计算的方式(如果有关于效率方面的分，请默认我知道这样来提升效率))<br>
2,determination_coefficient
 Calculer le coefficient de détermination R² <br>
 
3,hat_sigma
 Calculer sigma chapeau (variance résiduelle)<br>
 
4,visualize_results<br>
        Visualiser les résultats de prédiction du modèle, y compris la comparaison entre valeurs réelles et prédites, ainsi que le graphe des résidus.
        :param y_true: Valeurs réelles
        :param y_pred: Valeurs prédites
<br>

我在Main.py文件中提供了<br>
calculate<br>
 Exemple d'un programme pour calculer l'empreinte carbone.
    Les valeurs sont basées sur 'means_output.csv' et les entrées utilisateur.
<br>







