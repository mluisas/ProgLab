def corte(lista, altura):
    pedacos = 1
    mais_um = True
    for i in range(len(lista)):
        if lista[i] > altura and mais_um == True:
            pedacos += 1
            mais_um = False
        elif lista[i] < altura:
            mais_um = True
    return pedacos
n = int(input())
alturas = list(map(int, input().split()))
vales = []
cortes = []
for i in range(n):
    if i == 0:
        if alturas[i] < alturas[i + 1]:
            values.append(i)
    elif i < n - 1:
        if alturas[i] < alturas[i + 1] and alturas[i - 1] > alturas[i]:
            values.append(i)
    else:
        if alturas[i - 1] > alturas[i]:
            values.append(i)
for i in vales:
    cortes.append(corte(alturas, i + 0.5))
if vales:
    print(max(cortes))
else:
    print(2)
