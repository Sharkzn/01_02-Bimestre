taxa_brl_para_usd = 5.29 # USD = 5.29 BRL
taxa_usd_para_brl = 1 / taxa_brl_para_usd # 1 BRL = 0.20 USD

while True:
    #Exibe o menu de opções
    print("\n Escolha uma Opção:")
    print("1. BRL para US$")
    print("2. US$ para BRL")
    print("3. sair")

    opção = input("Digite o número da Opção desejada: ")

    if opção == '1':
        Valor_brl = float(input("Digite o valor em (R$): "))
        Valor_usd = Valor_brl / taxa_brl_para_usd
        print(f"R$ {Valor_brl:.2f} é equivalente a US$ {Valor_usd:.2f}")
    elif opção == '2':
        Valor_usd = float(input("Digite o valor em Dólares (US$)"))
        Valor_brl = Valor_usd * taxa_brl_para_usd
        print(f"US$ {Valor_usd:.2f} é equivalente a R$ {Valor_brl:.2f}")
    elif opção == '3':
        print("Saindo...")
        break
    else:
        print("Opção invalida... Tente novamente.")

