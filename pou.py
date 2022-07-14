# Será importado o Sleep
from time import sleep
# Criado uma classe com o nome Tm, abreviação de Tamaguchi
class Tm:
    # Aqui é usado o construtor inicial com um atributo dinâmico e outros já definido previamente
    def __init__(self, nome):
        # O nome sofrerar um Upercase
        self.nome = str.upper(nome)
        self.energia = 100
        self.fome = 0
        self.sede = 0
        self.saude = 100
        self.sono = 0
        self.exp = 0
        self.humor = 100
        self.idade = 0
    
    # Método dormir
    def dormir(self):
        # Verificará se está nos níveis propício para dormir
        if self.sono < 70:
            print(f"{self.nome}: Não estou com sono!!!")
        else:
            print(f"{self.nome}: Boa noite papai!!!")

            # Retornará os novos valores
            self.sono -= 50
            self.energia += 50
            self.fome += 30
            self.sede += 30
            self.saude += 30
            self.humor += 30

    # Método Brincar
    def brincar(self):
        # Aqui estão elencadas as brincadeiras que o Tamaguchi poderá por hora brincar, e elas serão distribuída pela sua idade
        brincadeiras = ["Pega-pega", "Esconde-esconde", "Andar de Bike", "Gravidade 0", "Polícia e Ladrao", "Verdade e Desafio", "Salada de Fruta", "Brincar", "Trabalhar", "Pagar as Contas", "Tentar Brincar"]
        # Aqui uma vetor que receberá as ações vindas do arquivo "ações.txt"
        acoes = []
        # Aqui abre o arquivo txt 
        acao = open("ações.txt", "rt", encoding="utf-8")

        #E aqui inclui no vetor acima
        for linha in acao:
            linha = str.strip(linha)
            acoes.append(linha)

        # Aqui terá a verificação da idade e das brincadeiras de acordo com a idade
        print("Qual desses jogos você quer brincar: ")
        if self.idade < 6:
            for n in range(0,5):
                print(f"[{n+1}] {brincadeiras[n]}")

        elif self.idade < 16:
            for n in range(5,8):
                print(f"[{n+1}] {brincadeiras[n]}")

        else:
            for n in range(8,11):
                print(f"[{n+1}] {brincadeiras[n]}")

        es = int(input()) - 1
        print(acoes[es])

        # Aqui o retorno de cada brincadeira exercida por ele
        if es == 0:
            sleep(3)
            print("Me pegou ＞︿＜")

            self.energia -= 15
            self.fome += 10
            self.sede += 20
            self.saude += 40 
            self.sono += 10
            self.exp += 10
            self.humor += 30
        elif es == 1:
            sleep(3)
            print("Me achou ＞︿＜")

            self.energia -= 10
            self.fome += 10
            self.sede += 20
            self.saude += 40 
            self.sono += 20
            self.exp += 10
            self.humor += 30
        elif es == 2:
            self.energia -= 50
            self.fome += 50
            self.sede += 70
            self.saude += 50 
            self.sono += 50
            self.exp += 20
            self.humor += 50
        elif es == 3:
            self.energia -= 5
            self.fome += 10
            self.sede += 15
            self.saude += 20 
            self.sono += 10
            self.exp += 10
            self.humor += 20
        elif es == 4:
            sleep(3)
            print("Fui preso X_X")

            self.energia -= 15
            self.fome += 10
            self.sede += 20
            self.saude += 40 
            self.sono += 20
            self.exp += 10
            self.humor += 30
        
        for n in range(5, 6):
            if es == n:
                self.energia -= 5
                self.fome += 10
                self.sede += 20
                self.saude += 40 
                self.sono += 20
                self.exp += 10
                self.humor += 30
        
        if es == 7:
            self.energia -= 30
            self.fome += 30
            self.sede += 80
            self.saude += 100 
            self.sono += 0
            self.exp += 50
            self.humor += 100

        for n in range(8,11):
            if es == n:
                self.energia -= 35
                self.fome += 20
                self.sede += 40
                self.saude -= 40 
                self.sono += 50
                self.exp += 10
                self.humor -= 30
                
    # Aqui é responsável por fazer o Tamaguchi crescer        
    def crescer(self):
        for idade in range(40, 800, 40):
            if self.exp >= idade:
                self.idade +=1
                break
    
    # Aqui Diminui a sede do Tamaguchi
    def beber(self):
        print(f"{self.nome}: Obrigado por me dá de Beber!!!")

        self.exp += 10
        self.sede -= 30
        self.sono += 5
        self.saude += 10
        self.energia -= 10
        self.humor += 10

    # Aqui é a área da comida
    def comer(self, rodada):
        if self.fome < 50:
            print(f"{self.nome}: Não estou com fome!!!")
        else:
            print(f"{self.nome}: Quero Comer Papai, o que você vai fazer hoje???")
            
            # As opções disponíveis e perceba que é dividido pela categoria
            manha = ["Café + Pão", "Café + Leite + Pão + Manteiga", "Tapioca + Ovo + Café + Leite"]
            almoço = ["Macarrao + Almondegas", "Arroz + Creme de Galinha + Salada", "Feijoada"]
            janta = ["Sopa", "Cuz-cuz", "Caldo"]

            r2 = rodada % 2
            r3 = rodada % 3

            # Aqui verificará qual opção demostrar ao usuário
            if r2 == 0:
                for n in range(0, len(almoço)):
                    print(f"[{n + 1}] {almoço[n]}")

            elif r3 == 0:
                for n in range(0, len(janta)):
                    print(f"[{n + 1}] {janta[n]}")

            else:
                for n in range(0, len(manha)):
                    print(f"[{n + 1}] {manha[n]}")
                
            vl = int(input())

            self.exp += vl*10
            self.sede += vl*10
            self.sono += vl*5
            self.saude += vl*5
            self.energia -= 10
            self.humor += vl*3
            self.fome -= vl*10

    # Medicar será usado somente nas últimas ocasiões
    def medicar(self):
        if self.saude > 5:
            print("Você não pode medicar seu filho!")
        else:
            print("Você medicou o seu filho!")

            self.exp += 10
            self.sede += 10
            self.sono += 30
            self.saude += 50
            self.energia -= 30
            self.humor += 50
            self.fome -= 30      

    # Aqui verificará a morte do Tamaguchi e seu motivo
    def morrer(self):
        a = 1
        if self.idade == 20:
            print(f"{self.nome} morreu com {self.idade} ")
            print("Causa da Morte: Idade")
            a = 0

        elif self.saude == 0:
            print(f"{self.nome} morreu com {self.idade} ")
            print("Causa da Morte: Doença")
            a = 0

        elif self.humor == 0:
            print(f"{self.nome} morreu com {self.idade} ")
            print("Causa da Morte: Depressão")
            a = 0

        elif self.sede == 100:
            print(f"{self.nome} morreu com {self.idade} ")
            print("Causa da Morte: Falta d'água")
            a = 0
        
        elif self.fome == 100:
            print(f"{self.nome} morreu com {self.idade} ")
            print("Causa da Morte: Desnutrição")
            a = 0

        elif self.energia == 0:
            print(f"{self.nome} morreu com {self.idade} ")
            print("Causa da Morte: Stress demais")
            a = 0

        return a
        
    # Os Status do Bichinho
    def status(self):
        print(f''' Nome: {self.nome}  |  |  Idade: {self.idade}
        
                        STATUS
        ENERGIA: {self.energia} %
        FOME: {self.fome} %
        SEDE: {self.sede} %
        SAUDE: {self.saude} %
        SONO: {self.sono} %
        EXPERIÊNCIA: {self.exp}
        HUMOR: {self.humor} %
        ''')

    # E as verificações finais
    def verificacao(self):
        if self.energia > 99:
            self.energia = 100
        elif self.energia < 1:
            self.energia = 0

        if self.fome > 99:
            self.fome = 100
        elif self.fome < 1:
            self.fome = 0

        if self.sede > 99:
            self.sede = 100
        elif self.sede < 1:
            self.sede = 0

        if self.saude > 99:
            self.saude = 100
        elif self.saude < 1:
            self.saude = 0
        
        if self.sono > 99:
            self.sono = 100
        elif self.sono < 1:
            self.sono = 0

        if self.humor > 99:
            self.humor = 100
        elif self.humor < 1:
            self.humor = 0

