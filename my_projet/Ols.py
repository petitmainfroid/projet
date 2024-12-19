import numpy as np
import matplotlib.pyplot as plt

class OrdinaryLeastSquares:
    def __init__(self, intercept=True):
        self.intercept = intercept
        self.coefficients = None

    def fit(self, X, y):

        """
        Ajuste un modèle de régression linéaire aux données fournies.
        Paramètres :
            - X : ndarray, n fois p
            - y : ndarray, n fois 1
        """
        X = np.array(X, dtype=float)
        y = np.array(y, dtype=float)
        # Ajouter une constante si l'intercept est inclus
        if self.intercept:
            a = np.array(X)
            dimension = a.shape
            print("X ", dimension)
            X = np.vstack((np.ones((1, dimension[1])), X))
            y = np.hstack((1, y))
            print("dinversssss", (X.T @ X).shape)
        # Calculer l'estimateur des moindres carrés : \beta^ = (X'X)^-1 X'y
        self.coefficients = np.linalg.inv(X.T @ X) @ X.T @ y
        #print("dinver", np.linalg.inv(X.T @ X).shape)
        self.coefficients = self.coefficients.reshape(-1, 1)

    def predict(self, XT):
        """
        Faire des prédictions pour de nouvelles données.
        Paramètres :
            - XT : ndarray, n fois 1 ou n fois p
        """
        return XT @ self.coefficients

    def get_coeffs(self):
        # Retourner les coefficients estimés
        return self.coefficients

    def get_diime_coeffs(self, dim):
        # Retourner le coefficient estimé de la dimension dim
        if self.intercept:
            return self.coefficients[dim + 1]
        else:
            return self.coefficients[dim]

    def determination_coefficient(self, X, y):
        """Calculer le coefficient de détermination R²."""
        y_pred = self.predict(X)
        ss_total = np.sum((y - np.mean(y)) ** 2, axis=0)
        ss_residual = np.sum((y - y_pred) ** 2, axis=0)
        ss_residual = np.array(ss_residual)
        ss_total = np.array(ss_total)
        return 1 - (ss_residual / ss_total)


    def hat_sigma(self, X, y):
        # Calculer sigma chapeau (variance résiduelle)
        inv = np.linalg.inv(X.T @ X)
        H = X @ inv @ X.T  # Matrice chapeau
        hat_beta = inv @ X.T @ y
        estim = H @ y
        return np.linalg.norm(y - estim) ** 2 / (len(y) - 14)

    def visualize_results(self, y_true, y_pred):
        """
        Visualiser les résultats de prédiction du modèle, y compris la comparaison entre valeurs réelles et prédites, ainsi que le graphe des résidus.
        :param y_true: Valeurs réelles
        :param y_pred: Valeurs prédites
        """
        # Comparaison des valeurs réelles et prédites
        plt.figure(figsize=(10, 5))
        plt.scatter(y_true, y_pred, alpha=0.7)
        plt.plot([min(y_true), max(y_true)], [min(y_true), max(y_true)], color='red', linestyle='--')
        plt.xlabel("Valeurs réelles")
        plt.ylabel("Valeurs prédites")
        plt.title("Valeurs réelles vs Prédites")
        plt.show()

        # Graphe des résidus
        residuals = y_true - y_pred
        plt.figure(figsize=(10, 5))
        plt.scatter(y_pred, residuals, alpha=0.7)
        plt.axhline(0, color='red', linestyle='--')
        plt.xlabel("Valeurs prédites")
        plt.ylabel("Résidus")
        plt.title("Résidus vs Valeurs prédites")
        plt.show()
        plt.hist(residuals)

    def voirxety(self, X, y):
        """Visualiser la relation linéaire entre X et Y"""
        for column in X.columns:
            plt.scatter(X[column], y)
            plt.title(f"Variable : {column}")
            plt.xlabel(column)
            plt.ylabel("Cible")
            plt.show()

    def mean_squared_error(self, X, y):
        """
        Calculer l'erreur quadratique moyenne (MSE).

        Paramètres :
        y_true : Valeurs réelles, liste ou tableau numpy
        y_pred : Valeurs prédites, liste ou tableau numpy

        Retourne :
        mse : Valeur de l'erreur quadratique moyenne
        """
        y_pred = self.predict(X)
        y_true = np.array(y)
        y_true = np.array(y_true)
        y_pred = np.array(y_pred)

        # Vérifier que les longueurs des entrées sont égales
        if len(y_true) != len(y_pred):
            raise ValueError("Les valeurs réelles et prédites doivent avoir la même longueur")

        errors = y_true - y_pred
        squared_errors = errors ** 2  # Calcul des erreurs au carré
        mse = np.mean(squared_errors)  # Calcul de la moyenne des erreurs au carré

        return mse
