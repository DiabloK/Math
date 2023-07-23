from tkinter import *
from math import sqrt
from banco import *
import matplotlib.pyplot as plt
class Menu(object):
    def __init__(self):
        self.tela = Tk()
        self.tela.title("PAC-MEN")
        self.fonte = ("Press Start", 45,)
        self.tela.config(background="black")
        self.tela.geometry("600x600")
        self.texto=Label(self.tela,text="Pitaguras",font=self.fonte,background="black",foreground="yellow")
        self.fonte=("Press Start", 14)
        self.texto1 = Label(self.tela, text="Hipotenusa(Nâo use letras)", font=self.fonte, background="black", foreground="yellow")
        self.texto2 = Label(self.tela, text="Cateto adjacente", font=self.fonte, background="black", foreground="yellow")
        self.texto3 = Label(self.tela, text="Cateto oposto", font=self.fonte, background="black", foreground="yellow")
        self.resultado=Label(self.tela, text="Cateto oposto", font=self.fonte, background="black", foreground="yellow")



        self.botaoUsuario = Button(self.tela, text="Calcular", font=self.fonte,activebackground="black",activeforeground="white",command=self.abrircal,border=8,background="black",foreground="white")
        self.botaoHistorico = Button(self.tela, text="Historico", font=self.fonte,activebackground="black",activeforeground="white",command=self.listar,border=8,background="black",foreground="white")
        self.botaografico = Button(self.tela, text="grafico", font=self.fonte, activebackground="black",activeforeground="white", command=self.Grafico, border=8, background="black", foreground="white")

        self.entra1=Entry(self.tela,font=self.fonte,border=8,background="black",foreground="white")
        self.entra2=Entry(self.tela,font=self.fonte,border=8,background="black",foreground="white")
        self.entra3=Entry(self.tela,font=self.fonte,border=8,background="black",foreground="white")

        self.botaoUsuario.grid(row=7,column=2,sticky='EW')
        self.botaoHistorico.grid(row=8,column=2,sticky='EW')
        self.botaografico.grid(row=9, column=2, sticky='EW')

        self.texto.grid(row=0, column=2, sticky='EW', columnspan=2)
        self.texto1.grid(row=1,column=2,sticky='EW', columnspan=2)
        self.texto2.grid(row=3, column=2, sticky='EW', columnspan=2)
        self.texto3.grid(row=5, column=2, sticky='EW', columnspan=2)

        self.entra1.grid(row=2,column=2,sticky='EW', columnspan=2)
        self.entra2.grid(row=4,column=2,sticky='EW', columnspan=2)
        self.entra3.grid(row=6,column=2,sticky='EW', columnspan=2)

    def rodar(self):
        self.tela.mainloop()
    def abrircal(self):
        entra1=self.entra1.get()
        entra2 = self.entra2.get()
        entra3 = self.entra3.get()
        if(entra1==""):
            if (entra2.isdigit()==True and entra3.isdigit()==True):
                entra2 = float(entra2)
                entra3 = float(entra3)
                if (entra3 != 0 and entra2 != 0):
                    ent=self.hipotenusa(entra2,entra3)
                    self.abrirhist(ent, entra2, entra3)
                    self.resultado['text'] = f"a hiputenusa ={ent}"
                    self.resultado.grid(row=10,column=2,sticky='EW',columnspan=2)
                else:
                    self.resultado['text'] = "um numero digitado e zero"
                    self.resultado.grid(row=10, column=2, sticky='EW', columnspan=2)
            else:
                self.resultado['text'] = "Existe um letra na caixa de texto"
                self.resultado.grid(row=10, column=2, sticky='EW', columnspan=2)
        elif(entra2==""):
            if (entra1.isdigit() == True and entra3.isdigit() == True):
                entra1 = float(entra1)
                entra3 = float(entra3)
                if (entra3 != 0 and entra1 != 0):
                    ent= self.catetoad(entra1, entra3)
                    self.abrirhist(entra1, ent, entra3)
                    self.resultado['text']=f"a cadeto adjacente {ent}"
                    self.resultado.grid(row=10, column=2, sticky='EW', columnspan=2)
                else:
                    self.resultado['text'] = " um numero digitado e zero"
                    self.resultado.grid(row=10, column=2, sticky='EW', columnspan=2)
            else:
                self.resultado['text'] = "Existe um letra na caixa de texto"
                self.resultado.grid(row=10, column=2, sticky='EW', columnspan=2)
        elif(entra3==""):
            if (entra1.isdigit() == True and entra2.isdigit() == True):
                entra1 = float(entra1)
                entra2 = float(entra2)
                if(entra2!=0 and entra1 !=0):
                    ent = self.catetoad(entra1, entra2)
                    self.abrirhist(entra1,entra2,ent)
                    self.resultado['text'] = f"a cadeto oposto {ent}"
                    self.resultado.grid(row=10, column=2, sticky='EW', columnspan=2)
                else:
                    self.resultado['text'] = "um numero digitado e zero"
                    self.resultado.grid(row=10, column=2, sticky='EW', columnspan=2)
            else:
                self.resultado['text'] = "Existe um letra na caixa de texto"
                self.resultado.grid(row=10, column=2, sticky='EW', columnspan=2)

    def hipotenusa(self,catetoA,catetO):
        cateto=catetO*catetO
        cateta=catetoA*catetoA
        hipotenusa=sqrt(cateto+cateta)
        return(hipotenusa)
    def catetoad(self,hipotenusa,catetO):
        hipotenusa=hipotenusa*hipotenusa
        cateto=catetO*catetO
        hipotenusa=sqrt(hipotenusa-cateto)
        return(hipotenusa)
    def abrirhist(self,hipotenusa,catetoAd,catetoO):
            try:
                banco = Banco()
                banco.conectar()
                banco.conexao.execute("INSERT INTO histo (hipotenusa,catetoAd,catetoO) values"
                                      f"('{hipotenusa}', '{catetoAd}', '{catetoO}')")
                banco.conexao.commit()
                banco.desconectar()
                return True
            except sqlite3.Error as erro:
                return erro.args[0]
    def listar(self):
        tempo=self.listar2()
        tela=Tk()
        tela.config(background="black")
        tela.geometry("900x500")
        fonte = ("Press Start", 15,)
        texto=Label(tela, text="HIPOTENUSA||", font=self.fonte, background="black", foreground="yellow")
        texto2= Label(tela, text="CATETO AD||", font=self.fonte, background="black", foreground="yellow")
        texto3= Label(tela, text="CATETO O", font=self.fonte, background="black", foreground="yellow")
        texto.grid(row=0,column=0)
        texto2.grid(row=0, column=1)
        texto3.grid(row=0, column=2)
        contador=0
        for cont in tempo:
            contador=contador+1
            texto4= Label(tela, text=str(cont.hipotenusa), font=self.fonte, background="black", foreground="yellow")
            texto5 = Label(tela, text=str(cont.catetoAd), font=self.fonte, background="black", foreground="yellow")
            texto6 = Label(tela, text=str(cont.catetoO), font=self.fonte, background="black", foreground="yellow")
            texto4.grid(row=contador,column=0)
            texto5.grid(row=contador, column=1)
            texto6.grid(row=contador, column=2)



    def listar2(self):
        listar= list()
        try:
            banco = Banco()
            banco.conectar()
            auxilar = banco.conexao.cursor()
            listaTemp = auxilar.execute("SELECT * FROM histo").fetchall()
            cont=0
            cont2=0
            for tupla in listaTemp:
                produto = hist()
                produto.hipotenusa =float(format(round(tupla[0],2)))
                produto.catetoAd= float(format(round(tupla[1],2)))
                produto.catetoO= float(format(round(tupla[2],2)))
                if (produto.catetoO>cont):
                    cont=produto.catetoO
                    self.x=cont
                elif(produto.catetoAd>cont2):
                    cont2=produto.catetoAd
                    self.y=cont2
                listar.append(produto)
            banco.desconectar()
            return listar
        except sqlite3.Error as erro:
            return erro.args[0]
    def Grafico(self):
        a=self.listar2()
        listaAd=list()
        listO=list()
        listH=list()
        for cont in a:
            listaAd.append(float(cont.catetoAd))
            listO.append(float(cont.catetoO))
            listH.append(float(cont.hipotenusa))

        fig=plt.figure()
        rect=fig.patch
        rect.set_facecolor("blue")

        for inte in listH:
            plt.scatter([0,self.x],[self.y],[listH[inte]],c='g',alpha=0.5)
        plt.title("Pi")
        plt.xlabel("cateto O")
        plt.ylabel("cateto AD")

        plt.show()
class hist(object):
    def __init__(self):
        self.hipotenusa=None
        self.catetoAd=None
        self.catetoO=None
