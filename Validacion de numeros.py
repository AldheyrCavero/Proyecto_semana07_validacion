def cant_de_divisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores


def lectura_de_numero_natural():
    while True:
        try:
            entrada = input  (" \nIngresar el número natural que necesita: ")
            numero = int(entrada)
            if numero <= 0:
                raise ValueError(" \nEl número tiene que ser un entero positivo.")
            return numero
        except ValueError as ve:
            print(f"Error: {ve}. Porfavor inténtelo de nuevo.")


if __name__ == "__main__":
    # Leer número natural
    numero = lectura_de_numero_natural()

    # Calcular y mostrar los divisores
    divisores = cant_de_divisores(numero)
    print(f"Los divisores de {numero} son los siguientes: \n{divisores}")