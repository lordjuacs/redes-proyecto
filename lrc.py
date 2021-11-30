from utils import *

# función principal de LRC que recibe dos dataBlock, la primera que es dataBlock y la segunda, dataBlock con errores.
def LRC2(dataBlock, dataBlockError):
    # splittear por espacios en blanco
    v1 = dataBlock.split(" ")
    v2 = dataBlockError.split(" ")
    # obtener longitudes
    n1 = len(dataBlock) - len(v1) + 1
    n2 = len(dataBlockError) - len(v2) + 1
    # no se puede dividir en n/8 bytes
    if n1 % 8 != 0 or n2 % 8 != 0:
        return "Data size is not multiple of 8\n"
    v1LRC = calcParityLRC(v1)
    print("Data block:")
    displayPretty(v1, v1LRC)
    v2LRC = calcParityLRC(v2)
    print("Data block error:")
    displayPretty(v2, v2LRC)
    if v1LRC != v2LRC:
        return "Receiver rejects the data\n"
    else:
        return "Receiver accepts the data\n"
