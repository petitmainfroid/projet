import pandas as pd
import matplotlib.pyplot as plt

def calculate():
    """
    Exemple d'un programme pour calculer l'empreinte carbone.
    Les valeurs sont basées sur 'means_output.csv' et les entrées utilisateur.
    """

    # Lire les données de coefficients de carbone
    data = pd.read_csv('means_output.csv', encoding='latin-1')
    data1 = pd.read_csv('energie.csv', encoding='UTF-8')
    print("qa",data1["french_name"])
    # Questions
    questions = {
        "nourriture": {
            "Légumes": "Combien de kg de légumes avez-vous utilisé ? ",
            "Céréales": "Combien de kg de céréales avez-vous utilisé ? ",
            "Viande": "Combien de kg de viandes avez-vous utilisé ? ",
            "Produits laitiers": "Combien de kg de Produits laitiers avez-vous servis ? ",
            "Produits à base de soja": "Combien de kg de Produits à base de soja  ? ",
            "Fruits": "Combien de kg de Fruits avez-vous utilisé ? ",
            "Alcool": "Combien de litres de boissons alcoolisées avez-vous servis ? ",
            "Boissons": "Combien de litres de boissons non alcoolisées avez-vous utilisés ? ",
        },
        "Transport": {
            "Avion": "Combien Km de avion vous prendre ? ",
            "Bus": "Combien Km de Bus vous prendre ? ",
            "Voiture": "Combien Km de voiture vous prendre ? ",
        },
        "energie": {
            "type": "Quel type d'énergie utilisez-vous (par exemple: Electricité, "
                    "Fioul domestique, Granulés, Gaz naturel - 2022) ? ",
            "qty": "Quantité (en kWh) ? ",
        },
    }

    # Sélection du type d'évaluation
    while True:
        choice = input("Quel type d'évaluation souhaitez-vous faire (hebdomadaire,"
                       " mensuelle, annuelle) ? ").lower()
        if choice in ["hebdomadaire", "mensuelle", "annuelle"]:
            break
        print("Veuillez choisir parmi 'hebdomadaire', 'mensuelle' ou 'annuelle'.")

    # Initialisation
    input_data = {}
    result_list = []
    energie_data = []  # Pour stocker les énergies et leurs quantités

    print("\n\nVeuillez répondre aux questions suivantes :")


    # Collecte des entrées utilisateur
    for category, subcategories in questions.items():
        print(f"\nCatégorie : {category}")
        for subcategory, question in subcategories.items():
            while True:
                try:
                    user_input = input(question).strip()
                    if category == "energie":
                        if subcategory == "type":
                            energie_type = user_input
                        elif subcategory == "qty":
                            energie_qty = float(user_input)
                            energie_data.append({"type": energie_type,
                                                 "qty": energie_qty})
                        break
                    else:
                        value = float(user_input)
                        input_data[subcategory] = value
                        break
                except ValueError:
                    print("Veuillez entrer un nombre valide.")

    # Calcul de l'empreinte carbone
    print("\n\nCalcul de votre empreinte carbone...")
    carbone_empreinte = 0


    for subcategory, value in input_data.items():
        if subcategory in data['categori'].values:
            emission_factor = data.loc[data['categori'] == subcategory,
            'Total poste non décomposé'].values[0]
            emission = value * emission_factor
            carbone_empreinte += emission
            result_list.append({"Catégorie": subcategory, "Quantité": value,
                                "Émission (kg CO2e)": emission})
        else:
            print(f"Catégorie '{subcategory}' non trouvée dans les données.")
    print("qq",energie_type)
    #emission_factor = data1.loc[data1['french_name'] ==energie_type , 'CO2']

    emission_factor = data1.loc[data1['french_name'] == energie_type, 'CO2'].values[0]

    emission = float(energie_data[0]['qty']) * emission_factor
    carbone_empreinte += emission

    # Résultats
    print("\n\n--- Résultat de votre empreinte carbone ---")
    print(f"Votre empreinte carbone {choice} est de {carbone_empreinte:.2f} kg CO2e")
    print(f"Votre empreinte carbone du energie {emission:.2f} kg CO2e")
    # Détails par catégorie
    print("\nDétails par catégorie :")
    for result in result_list:
        print(f" - {result['Catégorie'].capitalize()}"
              f" : {result['Émission (kg CO2e)']:.2f} kg CO2e")


def calculate():
    """
    Exemple d'un programme pour calculer l'empreinte carbone.
    Les valeurs sont basées sur 'means_output.csv' et les entrées utilisateur.
    """

    # Lire les données de coefficients de carbone
    data = pd.read_csv('means_output.csv', encoding='latin-1')
    data1 = pd.read_csv('energie.csv', encoding='UTF-8')
    print("qa", data1["french_name"])

    # Questions
    questions = {
        "nourriture": {
            "Légumes": "Combien de kg de légumes avez-vous utilisé ? ",
            "Céréales": "Combien de kg de céréales avez-vous utilisé ? ",
            "Viande": "Combien de kg de viandes avez-vous utilisé ? ",
            "Produits laitiers": "Combien de kg de Produits laitiers avez-vous servis ? ",
            "Produits à base de soja": "Combien de kg de Produits à base de soja  ? ",
            "Fruits": "Combien de kg de Fruits avez-vous utilisé ? ",
            "Alcool": "Combien de litres de boissons alcoolisées avez-vous servis ? ",
            "Boissons": "Combien de litres de boissons non alcoolisées avez-vous"
                        " utilisés ? ",
        },
        "Transport": {
            "Avion": "Combien Km de avion vous prendre ? ",
            "Bus": "Combien Km de Bus vous prendre ? ",
            "Voiture": "Combien Km de voiture vous prendre ? ",
        },
        "energie": {
            "type": "Quel type d'énergie utilisez-vous (par exemple: Electricité,"
                    " Fioul domestique, Granulés, Gaz naturel - 2022) ? ",
            "qty": "Quantité (en kWh) ? ",
        },
    }

    # Sélection du type d'évaluation
    while True:
        choice = input("Quel type d'évaluation souhaitez-vous faire (hebdomadaire, "
                       "mensuelle, annuelle) ? ").lower()
        if choice in ["hebdomadaire", "mensuelle", "annuelle"]:
            break
        print("Veuillez choisir parmi 'hebdomadaire', 'mensuelle' ou 'annuelle'.")

    # Initialisation
    input_data = {}
    result_list = []
    energie_data = []  # Pour stocker les énergies et leurs quantités

    print("\n\nVeuillez répondre aux questions suivantes :")

    # Collecte des entrées utilisateur
    for category, subcategories in questions.items():
        print(f"\nCatégorie : {category}")
        for subcategory, question in subcategories.items():
            while True:
                try:
                    user_input = input(question).strip()
                    if category == "energie":
                        if subcategory == "type":
                            energie_type = user_input
                        elif subcategory == "qty":
                            energie_qty = float(user_input)
                            energie_data.append({"type": energie_type,
                                                 "qty": energie_qty})
                        break
                    else:
                        value = float(user_input)
                        input_data[subcategory] = value
                        break
                except ValueError:
                    print("Veuillez entrer un nombre valide.")

    # Calcul de l'empreinte carbone
    print("\n\nCalcul de votre empreinte carbone...")
    carbone_empreinte = 0

    for subcategory, value in input_data.items():
        if subcategory in data['categori'].values:
            emission_factor = data.loc[data['categori'] == subcategory,
            'Total poste non décomposé'].values[0]
            emission = value * emission_factor
            carbone_empreinte += emission
            result_list.append({"Catégorie": subcategory, "Quantité": value,
                                "Émission (kg CO2e)": emission})
        else:
            print(f"Catégorie '{subcategory}' non trouvée dans les données.")

    total_energie_emission = 0
    for energie in energie_data:
        if energie['type'] in data1['french_name'].values:
            emission_factor = data1.loc[data1['french_name'] == energie['type'],
            'CO2'].values[0]
            emission = energie['qty'] * emission_factor
            total_energie_emission += emission
        else:
            print(f"Type d'énergie '{energie['type']}' non trouvé dans les données.")

    carbone_empreinte += total_energie_emission

    # Résultats
    print("\n\n--- Résultat de votre empreinte carbone ---")
    print(f"Votre empreinte carbone {choice} est de {carbone_empreinte:.2f} kg CO2e")
    print(f"Votre carbone du egernie {choice} est de {emission:.2f} kg CO2e")

    # Détails par catégorie
    print("\nDétails par catégorie :")
    for result in result_list:
        print(f" - {result['Catégorie'].capitalize()} : "
              f"{result['Émission (kg CO2e)']:.2f} kg CO2e")

    # Préparation des données pour le graphique
    categories = [result['Catégorie'] for result in result_list]
    emissions = [result['Émission (kg CO2e)'] for result in result_list]
    categories.append("Énergie")
    emissions.append(emission)



    # Création d'un graphique en barres empilées avec différentes couleurs
    # pour chaque sous-catégorie
    colors = [
        '#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c', '#98df8a',
        '#d62728', '#ff9896', '#9467bd', '#c5b0d5',
        '#8c564b', '#c49c94'
    ]

    cumulative_emissions = []
    current_index = 0
    plt.figure(figsize=(14, 8))

    # 为每个类别设置起始位置
    x_positions = []
    category_width = 1  # 每个类别的宽度
    offset = 0

    for category, subcategories in questions.items():
        x_positions += [offset + i *
                        (category_width / len(subcategories))
                        for i in range(len(subcategories))]
        offset += category_width + 1  # 添加空隙用于分隔类别

    # 绘制堆叠柱状图
    current_bottom = [0] * len(x_positions)
    color_index = 0

    for category, subcategories in questions.items():
        sub_emissions = emissions[color_index:color_index + len(subcategories)]
        plt.bar(
            x_positions[color_index:color_index + len(subcategories)],
            sub_emissions,
            width=(category_width / len(subcategories)) * 0.8,  # 宽度适中
            color=colors[color_index:color_index + len(subcategories)],
            bottom=current_bottom[color_index:color_index + len(subcategories)],
            label=subcategories.keys()
        )
        # 更新堆叠底部
        for i in range(len(sub_emissions)):
            current_bottom[color_index + i] += sub_emissions[i]
        color_index += len(subcategories)

    # 设置标签
    plt.xticks(
        [x + (category_width / 2) for x in range(0, offset, category_width + 1)],
        questions.keys(),
        rotation=45,
        ha="right",
        fontsize=12
    )
    plt.ylabel("Émissions (kg CO2e)", fontsize=14)
    plt.title("Empreinte carbone par catégorie et sous-catégorie", fontsize=16)
    plt.legend(loc="upper left", fontsize=10, title="Sous-catégories")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    calculate()
