from cs50 import get_float

while True:
    d = get_float("Troco? ")
    if d <= 0:
        print("Digite novamente o troco")
    else:
        break
moedas = 0
moe = d * 100
while moe >= 25:
    moe -= 25
    moedas += 1
while moe >= 10:
    moe -= 10
    moedas += 1
while moe >= 5:
    moe -= 5
    moedas += 1
while moe >= 1:
    moe -= 1
    moedas += 1
print(moedas)