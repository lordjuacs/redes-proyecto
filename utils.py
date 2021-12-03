from random import randint

# función para contar la cantidad de unos
def countOnes(data):
    cont = 0
    for i in data:
        if i == "1":
            cont += 1
    return cont


# función para añadir un string al inicio de otro
def push_front(value, data):
    return value + data


# función para añadir el bit de paridad
def addParityBit(data, dataError):
    if countOnes(data) % 2 == 0:
        dataTransmitted = push_front("0", data)
        dataErrorWithParity = push_front("0", dataError)
    else:
        dataTransmitted = push_front("1", data)
        dataErrorWithParity = push_front("1", dataError)
    return dataTransmitted, dataErrorWithParity


# función para generar aleatoriamente "numErrors" diferentes errores de transmisión
def transmissionError(data, numErrors):
    dataError = data
    possiblePos = [i for i in range(len(data))]
    for i in range(numErrors):
        pos = randint(0, len(possiblePos) - 1)
        posInData = possiblePos[pos]
        possiblePos.remove(posInData)
        bit = data[posInData]
        listAux = list(dataError)
        listAux[posInData] = (str)((int)(not (int)(bit)))
        dataError = "".join(listAux)
    return dataError


# función para generar el parity LRC
def calcParityLRC(v):
    parityLRC = []
    for i in range(len(v[0])):
        suma = 0
        for j in range(len(v)):
            suma += (int)(v[j][i])
        if suma % 2 == 0:
            parityLRC.append("0")
        else:
            parityLRC.append("1")
    return parityLRC


# función para imprimir de forma amigable la matriz resultante en LRC
def displayPretty(v, lrc):
    for i in v:
        print(i)
    print("LRC: ", end="")
    print("".join(lrc).strip())
    print()


# función para añadir "n" "values" al final de un string
def multi_push_back(data, n, value):
    for i in range(n):
        data = data + value
    return data


# función XOR para dos cadenas de bits
def XOR(a, b):
    res = ""
    for i in range(1, len(a)):
        res += str(int(a[i]) ^ int(b[i]))
    return res


# función para dividir módulo 2 en binario
def divMod2(data, divisor):
    crc = data[0 : len(divisor)]
    for i in range(len(divisor), len(data)):
        if crc[0] == "0":
            crc = XOR(crc, "0" * i)
        else:
            crc = XOR(crc, divisor)
        crc += data[i]
    if crc[0] == "0":
        crc = XOR(crc, "0" * i)
    else:
        crc = XOR(crc, divisor)
    return crc


# función para verificar si un string es todo 0, ejemplo: "00000...0"
def checkIfAllZero(data):
    for i in data:
        if i != "0":
            return False
    return True
