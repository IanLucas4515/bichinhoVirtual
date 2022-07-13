from pou import Tm

rodada = 0
morreu = False
op = ["Dormir", "Brincar", "Beber", "Comer", "Medicar"]

if rodada == 0:
    print("Seu bixinho virtual acabou de nascer")
    print("Qual o nome do seu bixinho")
    nome = input()
    nm = Tm(nome)

    rodada += 1

while morreu == False:
    nm.status()

    print(f'O que você desejá fazer mais o {nm.nome}')
    for n in range(0,len(op)):
        print(f"[{n+1}] {op[n]}")
    escolha = int(input()) - 1

    if escolha == 0:
        nm.dormir()
    elif escolha == 1:
        nm.brincar()
    elif escolha == 2:
        nm.beber()
    elif escolha == 3:
        nm.comer(rodada)
    elif escolha == 4:
        nm.medicar()


    nm.crescer()
    nm.verificacao()

    n = nm.morrer()
    if n == 1:
        morreu = False
    elif n == 0:
        morreu = True