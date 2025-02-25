dana = input("Podaj wartość: ")

try:
    if "." in dana:
        dana = float(dana)
        print("To jest liczba zmiennoprzecinkowa (float)")
    else:
        dana = int(dana)
        print("To jest liczba całkowita (int)")
except ValueError:
    if dana.lower() == "true" or dana.lower() == "false":
        print("To jest wartość logiczna (bool)")
    else:
        print("To jest ciąg znaków (str)")