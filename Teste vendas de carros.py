carros = ["Fiat", "Ford", "Chevrolet"]
carros_lux = ["Honda", "Toyota", "Hyundai"]
carros_especiais = ["Ferrari", "Porsche", "Lamborghini"]
new_cars = ["Audi", "BMW", "Mercedez"]
moto = ["Honda", "Yamaha", "Suzuki"]

precos = {
    "Fiat": 20000,
    "Ford": 25000,
    "Chevrolet": 50000,
    "Honda": 50000,
    "Toyota": 55000,
    "Hyundai": 47000,
    "Ferrari": 400000,
    "Porsche": 350000,
    "Lamborghini": 450000,
    "Audi": 60000,
    "BMW": 70000,
    "Mercedez": 80000,
    "Yamaha": 25000,
    "Suzuki": 14000
}

saldo = 100000
Rodolfo = "Você possui R$"

def mostrar_saldo():
    print (f"{Rodolfo} {saldo}")

def tentar_comprar(item):
    global saldo
    if item in precos:
        preco = precos [item]
        if saldo >= preco:
            saldo -= preco
            print ("Compra efetuada com sucesso!")
        else:
            print ("Você não possui saldo o suficiente.")
    else:
        print ("Item não encontrado.")

def exibir_opcoes():
    while True:
        print ("\nEscolha uma opção de compra:")
        print ("1. Carros")
        print ("2. Carros de luxo")
        print ("3. Carros especiais")
        print ("4. Novos carros")
        print ("5. Motos")
        print ("6. Ver saldo")
        print ("7. Sair")

        escolha = input ("Digite o número da opção:")

        if escolha == "1":
            print ("Carros disponíveis:", carros)
            item = input ("Escolha um carro para comprar:")
            tentar_comprar(item)
        elif escolha == "2":
            print ("Carros de luxo disponíveis:", carros_lux)
            item = input ("Escolha um carro de luxo para comprar:")
            tentar_comprar(item)
        elif escolha == "3":
            print ("Carros especiais disponíveis:", carros_especiais)
            item = input ("Escolha um carro especial para comprar:")
            tentar_comprar(item)
        elif escolha == "4":
            print ("Novos carros disponíveis:", new_cars)
            item = input ("Escolha um novo carro para comprar:")
            tentar_comprar(item)
        elif escolha == "5":
            print ("Motos disponíveis:", moto)
            item = input ("Escolha uma moto para comprar:")
            tentar_comprar(item)
        elif escolha == "6":
            print (saldo)
        elif escolha == "7":
            break
        else:
            print ("Opção inválida.Tente novamente.")
exibir_opcoes()