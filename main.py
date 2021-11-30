# los métodos que terminan en 1 reciben como 3er parámetro el número de errores para generarlos aleatoriamente durante la transmisión
# los métodos que terminan en 2 reciben como 3er parámetro la data corrompida para tests exactos
from vrc import VRC1, VRC2
from lrc import LRC2
from crc import CRC1, CRC2

print("VRC\n")
print("Tests aleatorios")
data = "1100001"
print(VRC1(data, 1))
print(VRC1(data, 2))
print(VRC1(data, 3))
print(VRC1(data, 4))
print("Tests del docs")
data = "11010010"
dataError = "11101010"
print(VRC2(data, dataError))
dataError = "11100010"
print(VRC2(data, dataError))
print("\n----------------------------")

print("LRC\n")
print("Tests del docs")
dataBlock = "10100101 00000000 11100111 11010010"
dataBlockError = "10000101 10000100 11100111 11010010"
print(LRC2(dataBlock, dataBlockError))
dataBlockError = "00100001 10000100 11100111 11010010"
print(LRC2(dataBlock, dataBlockError))
dataBlock = "11000010"
dataBlockError = "10000000"
print(LRC2(dataBlock, dataBlockError))
print("\n----------------------------")

print("CRC\n")
print("Tests aleatorios")
data = "100100"
divisor = "1101"
for i in range(len(data)):
    print(i, "error(es)")
    print(CRC1(data, divisor, i))
data = "100100"
divisor = "1101"
dataError = "111110"
print("Test donde decide incorrectamente")
print(CRC2(data, divisor, dataError))
print("\n----------------------------")
