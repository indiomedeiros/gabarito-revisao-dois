def saudar_usuario():
    print("======================= SAUDAÇÃO =======================")
    nome = input("Qual é o seu nome? ")
    print("Olá, " + nome + "! Seja bem-vindo(a)!")

saudar_usuario()

def somar_numeros():
    print("======================= SOMA =======================")
    primeiro_numero = float(input("Digite um número: "))
    segundo_numero = float(input("Digite outro número: "))
    soma = primeiro_numero + segundo_numero
    print("A soma dos números é: " + str(soma))

somar_numeros()