from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser

# Criar janela
jan = Tk()
jan.title('Painel de Acesso')
jan.geometry('600x300')#o tamanho da janela
jan.configure(background='orange')#Configura a cor da janela
jan.resizable(width=False, height=False)# impede que o tamanho da janela seja alterado
jan.attributes('-alpha', 0.9)# deixando um pouco transparente
jan.iconbitmap(default='icons/Logoicon.ico')# Adiciona o logo icon no canto superior esquerdo

# Carregar imagem
logo = PhotoImage(file='icons/jam.png')#imagem (100x100)

# Criar os widgets da janela separando em dois, direita e esquerda
# separada por uma barra branca
LeftFrame = Frame(jan, width=200, height=300, bg='GREEN', relief='raise')
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg='MIDNIGHTBLUE', relief='raise')
RightFrame.pack(side=RIGHT)
#bg é a cor de fundo
LogoLabel = Label(LeftFrame, image=logo, bg='GREEN')#Exibi um texto ou imagem
LogoLabel.place(x=50, y=100)# posicionando a imagem
# fg é a cor do texto
UserLabel = Label(RightFrame, text='Nome do Usuário:', font=('Century Gothic', 12), bg='MIDNIGHTBLUE', fg='White')
UserLabel.place(x=5, y=110)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=160, y=112)


PassLabel = Label(RightFrame, text='Senha:', font=('Century Gothic', 12), bg='MIDNIGHTBLUE', fg='White')
PassLabel.place(x=5, y=155)

PassEntry = ttk.Entry(RightFrame, width=30, show='*')#width = tamanho máximo do texto, show = mostra * no lugar digitado
PassEntry.place(x=160, y=157)

def login():
    user = UserEntry.get()
    senha = PassEntry.get()

    DataBaser.cursor.execute("""
    SELECT * FROM Users
    WHERE (Usuário = ? and Senha = ?)
    """, (user, senha))
    print('Selecionado')
    verifylogin = DataBaser.cursor.fetchone()
    try:
        if (user in verifylogin and senha in verifylogin):
            messagebox.showinfo(title='Login Info', message='Login Efetuado com Sucesso.')
    except:
        messagebox.showerror(title='Login info', message='Acesso Negado')


def register():
    # Removendo widgets de login
    loginbuttom.place(x=5000)
    cadbuttom.place(x=5000)
    # Inserindo Widgets de cadastro
    nomelabel = Label(RightFrame, text='Nome:', font=('Century Gothic', 12), bg='MIDNIGHTBLUE', fg='White')
    nomelabel.place(x=5, y=20)
    nomeentry = ttk.Entry(RightFrame, width=30)
    nomeentry.place(x=160, y=22)

    EmailLabel = Label(RightFrame, text='Email:', font=('Century Gothic', 12), bg='MIDNIGHTBLUE', fg='White')
    EmailLabel.place(x=5, y=65)
    EmailEntry = ttk.Entry(RightFrame, width=30)
    EmailEntry.place(x=160, y=67)

    def RegisterBD():
        nome = nomeentry.get()
        usuario = UserEntry.get()
        email = EmailEntry.get()
        senha = PassEntry.get()
        if nome == '' or usuario == '' or email == '' or senha == '':
            messagebox.showerror(title='ERRO Ao Registrar', message='Preencha Todos Os Campos Corretamente!')
        else:
            DataBaser.cursor.execute("""
            INSERT INTO Users(Nome, Email, Usuário, Senha) VALUES(?, ?, ?, ?)
            """, (nome, email, usuario, senha))
            DataBaser.conexao.commit()
            messagebox.showinfo(title='Registro da Informação', message='Registrado com Sucesso')


    def voltar():
        #Removendo width de registro
        nomelabel.place(x=5000)
        nomeentry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        voltar.place(x=5000)
        registrar.place(x=5000)
        #Inserindo width de button
        passentry = ttk.Entry(RightFrame, width=30, show='*')  # width = tamanho máximo do texto, show = mostra * no lugar digitado
        passentry.place(x=160, y=157)
        UserEntry = ttk.Entry(RightFrame, width=30)
        UserEntry.place(x=160, y=112)
        loginbuttom.place(x=160, y=210)
        cadbuttom.place(x=254, y=210)

    voltar = ttk.Button(RightFrame, text='Voltar', width=10, command=voltar)
    voltar.place(x=160, y=210)

    registrar = ttk.Button(RightFrame, text='Registrar', width=14, command=RegisterBD)
    registrar.place(x=254, y=210)

# Botões

loginbuttom = ttk.Button(RightFrame, text='Login', width=10, command=login)
loginbuttom.place(x=160, y=210)

cadbuttom = ttk.Button(RightFrame, text='Cadastre-se', width=14, command=register)
cadbuttom.place(x=254, y=210)

jan.mainloop()
