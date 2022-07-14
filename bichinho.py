# Aqui será importado o Objeto
from pou import Tm

# Também será definidas rodada, para verificar se o bichinho já foi criado
rodada = 0

# Uma verificação, para saber se ele morreu
morreu = False

# Uma Tupla com as opções que serão escolhida pelo usuário
op = ("Dormir", "Brincar", "Beber", "Comer", "Medicar")

# A criação de nosso bichinho virtual
if rodada == 0:
    print("Seu bixinho virtual acabou de nascer")
    print("Qual o nome do seu bixinho")
    nome = input()
    nm = Tm(nome)

    rodada += 1

# O jogo em si, que possui um while que verifica se o bichinho morreu
while morreu == False:
    # Imprime primeiramente o status do bichinho
    nm.status()

    # Depois as opções disponíveis ao usuário
    print(f'O que você desejá fazer mais o {nm.nome}')
    for n in range(0,len(op)):
        print(f"[{n+1}] {op[n]}")
    escolha = int(input()) - 1

    # Aqui vai verificar se o usuário digitou um valor válido
    if escolha >= 0 and escolha <= 4:
        # Aqui verificará o que o usuário dígitou e qual rumo o jogo vai tomar
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

        # Por fim o bichinho vai crescer, e será verificado se atingiu estágios críticos
        nm.crescer()
        nm.verificacao()

        # Se sim o método morreu retornará 0, se não 1
        n = nm.morrer()
        if n == 1:
            morreu = False
        elif n == 0:
            morreu = True
        
        rodada += 1
    # Aqui a resposta para digitar um valor incompatível
    else:
        print('Sua ecolha é inválida!')
        print('Digíte um valor válido!')