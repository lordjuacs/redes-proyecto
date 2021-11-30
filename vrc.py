from utils import *

# función principal de VRC que genera errores durante la transmisión
def VRC1(data, numErrors):
    dataError = transmissionError(data, numErrors)
    # agregar el bit de paridad
    dataTransmitted, dataErrorTransmitted = addParityBit(data, dataError)
    print("Data:      ", dataTransmitted[0], data)
    print("Data error:", dataErrorTransmitted[0], dataError)
    # VRC: puede detectar errores de 1 bit o de una cantidad impar de bits.
    if countOnes(dataErrorTransmitted) % 2 != 0:
        return "Receiver rejects the data\n"
    else:
        return "Receiver accepts the data\n"


# función principal de VRC que recibe dos cadenas, la primera que es data y la segunda, data con errores.
def VRC2(data, dataError):
    # agregar el bit de paridad
    dataTransmitted, dataErrorTransmitted = addParityBit(data, dataError)
    print("Data:      ", dataTransmitted[0], data)
    print("Data error:", dataErrorTransmitted[0], dataError)
    # VRC: puede detectar errores de 1 bit o de una cantidad impar de bits.
    if countOnes(dataErrorTransmitted) % 2 != 0:
        return "Receiver rejects the data\n"
    else:
        return "Receiver accepts the data\n"
