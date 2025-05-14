def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Impossible de diviser par 0")
    return a / b


choix = 100
while True:
    print("#" * 10, "Calculatrice", "#" * 10)
    print()
    print(
        "1 - Addition \n2 - Soustraction \n3 - Division \n4 - Multiplication"
    )
    choix = int(input("Saisissez un nombre (0 pour quitter) : "))
    if choix == 0:
        print("Meric d'avoir utilisé notre calculatrice. Au revoir")
        print("#" * 40)
        break
    print()
    a = float(input("premier nombre : "))
    b = float(input("second nombre : "))

    if choix == 1:
        print("résultat :", add(a, b))

    elif choix == 2:
        print("résultat :", subtract(a, b))

    elif choix == 3:
        print("résultat :", multiply(a, b))

    elif choix == 4:
        print("résultat :", divide(a, b))

    print("-" * 30)
