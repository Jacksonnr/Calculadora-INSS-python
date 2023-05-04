from tkinter import *

class Application:
    def __init__(self, master = None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["pady"] = 20
        self.terceiroContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Calculadora de INSS")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.salarioLabel = Label(self.segundoContainer,text="Salário Bruto ->", font=self.fontePadrao)
        self.salarioLabel.pack(side=LEFT)

        self.salario = Entry(self.segundoContainer)
        self.salario["width"] = 30
        self.salario["font"] = self.fontePadrao
        self.salario.pack(side=LEFT)

        self.calcular = Button(self.terceiroContainer)
        self.calcular["text"] = "Calcular"
        self.calcular["font"] = ("Calibri", "8")
        self.calcular["width"] = 12
        self.calcular["command"] = self.inss
        self.calcular.pack()

        self.mensagem = Label(self.terceiroContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    def inss(self):

      
      salarioInformado = float(self.salario.get())
      calculoPorcentagem = [7.5, 9, 12, 14]
      faixaSalarial = [1302.00, 2571.29, 3856.94, 7507.49]

      if salarioInformado == faixaSalarial [0]:
         desconto = round ((calculoPorcentagem[0] / 100) * salarioInformado, 2)
         salarioInformado = salarioInformado - desconto
         self.mensagem["text"] = f'O desconto do INSS sobre seu salário foi de R$ {desconto}, assim ficando seu salário no valor de R$ {salarioInformado}'

      elif salarioInformado > faixaSalarial [0] and salarioInformado <= faixaSalarial [1]:
         desconto = round (calculoPorcentagem[1] / 100 * (salarioInformado - faixaSalarial [0]) + 97.65, 2)
         salarioInformado = salarioInformado - desconto
         self.mensagem["text"] = f'O desconto do INSS sobre seu salário foi de R$ {desconto}, assim ficando seu salário no valor de R$ {salarioInformado}'

      elif salarioInformado > faixaSalarial [1] and salarioInformado <= faixaSalarial [2]:
         desconto = round (calculoPorcentagem[2] / 100 * (salarioInformado - faixaSalarial [1]) + 97.65 + 114.24, 2)
         salarioInformado = salarioInformado - desconto
         self.mensagem["text"] = f'O desconto do INSS sobre seu salário foi de R$ {desconto}, assim ficando seu salário no valor de R$ {salarioInformado}'

      elif salarioInformado > faixaSalarial [2] and salarioInformado <= faixaSalarial [3]:
         desconto = round (calculoPorcentagem[3] / 100 * (salarioInformado - faixaSalarial [2]) + 97.65 + 114.24 + 154.28, 2)
         salarioInformado = salarioInformado - desconto
         self.mensagem["text"] = f'O desconto do INSS sobre seu salário foi de R$ {desconto}, assim ficando seu salário no valor de R$ {salarioInformado}'

      else: 
         self.mensagem["text"] = 'Faixa salarial inválida!'



root = Tk()
Application(root)
root.mainloop()