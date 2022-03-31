import random  

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.tentar_novamente = True

    
    def Iniciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
        while self.tentar_novamente == True:
            if int(self.valor_do_chute) > self.valor_aleatorio:
                print('Chute um valor mais baixo! ')
                self.PedirValorAleatorio()
            elif int(self.valor_do_chute) < self.valor_aleatorio:
                print('Chute um valor mais alto!')
                self.PedirValorAleatorio()
            elif int(self.valor_do_chute) == self.valor_aleatorio:
                self.tentar_novamente = False
                print('Parabéns,você acertou!')


    


    def PedirValorAleatorio(self):
        self.valor_do_chute = input('Digite um numero: ')

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(1,25)


chute = ChuteONumero()
chute.Iniciar()
