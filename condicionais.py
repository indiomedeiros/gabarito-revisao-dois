def verificar_maioridade():
    print("======================= MAIORIDADE =======================")

    idade = int(input("Qual é a sua idade? "))
    if(idade >= 18):
        print("Maior de idade")
    else:
        print("Menor de idade")

verificar_maioridade()