from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout

class JogodavelhaApp(App):
    def build(self):
        self.title = "Jogo da Velha"
        Window.size = (700,400)
        return Tela()

class Tela(GridLayout):
    x = 0
    vitoriasX = 0
    vitoriasO = 0
    velha = 0
    tabuleiro = [['','',''],['','',''],['','','']]

    def __init__(self, **kwargs):
        super(Tela,self).__init__(**kwargs)
        self.jogador_da_vez = "X"
        self.lista_botoes = [
            [self.ids.um, self.ids.dois, self.ids.tres], 
            [self.ids.quatro, self.ids.cinco, self.ids.seis],
            [self.ids.sete, self.ids.oito, self.ids.nove]
        ]
        
    def on_release(self, lin, col):
        #so marca se o botão estiver vazio
        if self.lista_botoes[lin][col].text == "":
            #coloquei um text no botao
            self.lista_botoes[lin][col].text = self.jogador_da_vez

            #checa vitoria
            self.checa_vitoria(lin, col)

            #alternei o jogador
            if self.jogador_da_vez == "X":
                self.jogador_da_vez = "O"
            else:
                self.jogador_da_vez = "X"

    def desligabotao(self):
        self.ids.um.disabled = True
        self.ids.dois.disabled = True
        self.ids.tres.disabled = True
        self.ids.quatro.disabled = True
        self.ids.cinco.disabled = True
        self.ids.seis.disabled = True
        self.ids.sete.disabled = True
        self.ids.oito.disabled = True
        self.ids.nove.disabled = True

    def ligabotao(self):
        self.ids.um.disabled = False
        self.ids.dois.disabled = False
        self.ids.tres.disabled = False
        self.ids.quatro.disabled = False
        self.ids.cinco.disabled = False
        self.ids.seis.disabled = False
        self.ids.sete.disabled = False
        self.ids.oito.disabled = False
        self.ids.nove.disabled = False

    def limpabotao(self):
        self.ids.um.text = ""
        self.ids.dois.text = ""
        self.ids.tres.text = ""
        self.ids.quatro.text = ""
        self.ids.cinco.text = ""
        self.ids.seis.text = ""
        self.ids.sete.text = ""
        self.ids.oito.text = ""
        self.ids.nove.text = ""

    def escolha(self):
        if self.jogador_da_vez == "X":
            self.contadorvitoriasX()
        else:
            self.contadorvitoriasO()

    def checa_vitoria(self, lin,  col):
        lb = self.lista_botoes

        #checa a linha
        if lb[lin][0].text == lb[lin][1].text == lb[lin][2].text:
            self.escolha()
            self.desligabotao()
        
        #checa a coluna
        elif lb[0][col].text == lb[1][col].text == lb[2][col].text:
            self.escolha()
            self.desligabotao()

        #checa diagonal principal
        elif lb[0][0].text == "X" and lb[1][1].text == "X" and lb[2][2].text == "X":
            self.escolha()
            self.desligabotao()

        elif lb[0][0].text == "O" and lb[1][1].text == "O" and lb[2][2].text == "O":
            self.escolha()
            self.desligabotao()

        #checa diagonal secundaria
        elif lb[0][2].text == "X" and lb[1][1].text == "X" and lb[2][0].text == "X":
            self.escolha()
            self.desligabotao()

        elif lb[0][2].text == "O" and lb[1][1].text == "O" and lb[2][0].text == "O":
            self.escolha()
            self.desligabotao()

        else: 
            self.x += 1
            if self.x == 9:
                self.contadorvelha()
                self.x = 0
                self.desligabotao()
        return self.x

    def reset(self):
        self.x = 0
        self.jogador_da_vez = 'X'
        self.ligabotao()
        self.resultados()
        self.limpabotao()
        self.mudahistorico()
        self.resettabuleiro()

    def resultados(self):
        x = f"Vitórias\nPlayer X: {self.vitoriasX}"
        self.ids.vitoriaX.text = x
        o = f"Vitórias\nPlayer O: {self.vitoriasO}"
        self.ids.vitoriaO.text = o
        v = f"Velha: {self.velha}"
        self.ids.velha.text = v

    def contadorvitoriasX(self):
        self.vitoriasX += 1

    def contadorvitoriasO(self):
        self.vitoriasO += 1

    def contadorvelha(self):
        self.velha += 1

    def mudahistorico(self):
        self.ids.vum.text = self.tabuleiro[0][0]
        self.ids.vdois.text = self.tabuleiro[0][1]
        self.ids.vtres.text = self.tabuleiro[0][2]
        self.ids.vquatro.text = self.tabuleiro[1][0]
        self.ids.vcinco.text = self.tabuleiro[1][1]
        self.ids.vseis.text = self.tabuleiro[1][2]
        self.ids.vsete.text = self.tabuleiro[2][0]
        self.ids.voito.text = self.tabuleiro[2][1]
        self.ids.vnove.text = self.tabuleiro[2][2]
    
    def tabuleirojogos(self, linha, coluna):
        self.tabuleiro[linha][coluna] = self.jogador_da_vez

    def resettabuleiro(self):
        for i in range (0,3):
            for j in range (0,3):
                self.tabuleiro[i][j] = ""

JogodavelhaApp().run()