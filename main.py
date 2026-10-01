def calcular_resfriamento(temp_inicial, tempo_minutos):
    taxa_resfriamento = 2.5
    temp_final = temp_inicial - (tempo_minutos * taxa_resfriamento)
    if temp_final < 20:
        temp_final = 20
    return temp_final

def main():
    temp = float(input("Informe a temperatura inicial (C): "))
    minutos = 5
    resultado = calcular_resfriamento(temp, minutos)
    print(f"Temperatura final: {resultado}°C")

if __name__ == "__main__":
    main()