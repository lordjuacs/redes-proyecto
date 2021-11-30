from utils import *

# función principal de CRC que recibe data, divisor de data y el número de errores
def CRC1(data, divisor, numErrors):
    # generar errores aleatorios durante la transmisión
    dataError = transmissionError(data, numErrors)
    n = len(divisor)
    # agregar n-1 ceros al final de data, tal que n es la longitud del divisor
    dataZero = multi_push_back(data, n - 1, "0")
    # divsión módulo 2 para calcular el crc
    crc = divMod2(dataZero, divisor)
    dataTransmitted = data + crc
    dataErrorTransmitted = dataError + crc
    print("Data:      ", data, crc)
    print("Data error:", dataError, crc)
    # para identificar errores hay que realizar una división módulo 2 entre
    # la data transmitida con error y el divisor
    if not checkIfAllZero(divMod2(dataErrorTransmitted, divisor)):
        return "Receiver rejects the data\n"
    else:
        return "Receiver accepts the data\n"


# función principal de CRC que recibe data, divisor de data y la data corrompida
def CRC2(data, divisor, dataError):
    n = len(divisor)
    # agregar n-1 ceros al final de data, tal que n es la longitud del divisor
    dataZero = multi_push_back(data, n - 1, "0")
    # divsión módulo 2 para calcular el crc
    crc = divMod2(dataZero, divisor)
    dataTransmitted = data + crc
    dataErrorTransmitted = dataError + crc
    print("Data:      ", data, crc)
    print("Data error:", dataError, crc)
    # para identificar errores hay que realizar una división módulo 2 entre
    # la data transmitida con error y el divisor
    if not checkIfAllZero(divMod2(dataErrorTransmitted, divisor)):
        return "Receiver rejects the data\n"
    else:
        return "Receiver accepts the data\n"
