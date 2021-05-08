# 7 - Leia uma temperatura em graus Fahrenheit e apresente-a convertida em Celsius.
# C = 5.0 * (F - 32.0) / 9.0

def fah_to_cel():
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = 5 * (fahrenheit - 32) / 9
    print(f"A temperatura em graus Celsius é {celsius} °C")

def main():
    fah_to_cel()

if __name__ == "__main__":
    main()
