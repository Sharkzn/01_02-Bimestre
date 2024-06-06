num = int(input("Digite um número para ver a tabuada: "))

print(f"Tabuada do {num}:")

for i in range(1, 11):
    """
i = 1
i = 2
i = 3
i = 4
...
i = 10
    """
    print(f"{num} x {i} = {num * i}")

