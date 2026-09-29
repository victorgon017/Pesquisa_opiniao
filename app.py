excelente = 0
bom = 0
ruim = 0
#processamento
for i in range(50):
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite a sua idade: "))
    opiniao = int(input("Digite a sua opinião sobre o atendimento de 1 a 3, excelente, bom e ruim respectivamente: "))
    if opiniao == 1:
        excelente = excelente + 1
    elif opiniao == 2:
        bom = bom + 1
    elif opiniao == 3:
        ruim = ruim + 1
    else:
        print("Opção inválida.")
#saída
print("Quantidade de avaliações excelentes:", excelente)
print("Quantidade de avaliações ruins:", ruim)

 


