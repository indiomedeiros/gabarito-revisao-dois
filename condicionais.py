def verificar_maioridade():
    print("======================= MAIORIDADE =======================")

    idade = int(input("Qual é a sua idade? "))
    if(idade >= 18):
        print("Maior de idade")
    else:
        print("Menor de idade")

verificar_maioridade()

def verifica_par():
    print("======================= VERIFICA PAR =======================")

    numero = int(input("Digite um número: "))
    if(numero % 2 == 0):
           print("O número é par!")
    else:
        print("O número é ímpar!")

verifica_par()