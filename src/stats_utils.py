import math
# Analyse des ventes : statistiques et détection d'anomalies
def analyser_ventes(transactions):
    # 1. Nettoyage : on garde uniquement les montants > 0
    valides = [t for t in transactions if t > 0]

    if not valides:
        return {"erreur": "Aucune transaction valide"}

    # 2. Calculs statistiques
    nombre = len(valides)
    somme = sum(valides)
    moyenne = somme / nombre

    triees = sorted(valides)
    milieu = nombre // 2
    if nombre % 2 == 0:
        mediane = (triees[milieu - 1] + triees[milieu]) / 2
    else:
        mediane = triees[milieu]

    variance = sum((t - moyenne) ** 2 for t in valides) / nombre
    ecart_type = math.sqrt(variance)

    # 3. Détection des anomalies : > 2 fois la moyenne
    anomalies = [t for t in valides if t > 2 * moyenne]

    # 4. Dictionnaire de sortie
    return {
        "nombre_transactions": nombre,
        "somme_totale": somme,
        "moyenne": round(moyenne, 2),
        "mediane": mediane,
        "ecart_type": round(ecart_type, 2),
        "minimum": min(valides),
        "maximum": max(valides),
        "anomalies": anomalies,
    }


if __name__ == "__main__":
    donnees_test = [150, 200, 180, -50, 0, 220, 175, 1200, 190, 210]

    resultats = analyser_ventes(donnees_test)

    print("=== Analyse des ventes ===")
    for cle, valeur in resultats.items():
        print(f"{cle} : {valeur}")


def detecter_outliers(outliers):
    if outliers is None or len(outliers) == 0:
        print("pas d'outliers")
    else:
        return(outliers)

print("=== Détection des outliers ===")
outliers=detecter_outliers("anomalies")
print(f"outliers, {outliers}")