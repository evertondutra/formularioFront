from tkinter import *
from tkinter import messagebox, Frame
from tkinter import ttk
import DataBaser

# Criar janela
jan = Tk()
jan.title('Painel de Acesso')
jan.geometry('300x600')  # o tamanho da janela
jan.configure(background='white')  # Configura a cor da janela
jan.resizable(width=False, height=False)  # impede que o tamanho da janela seja alterado
jan.attributes('-alpha', 0.9)  # deixando um pouco transparente
jan.iconbitmap(default='icons/Logoicon.ico')  # Adiciona o logo icon no canto superior esquerdo

# Carregar imagem
logo = PhotoImage(file='icons/jam.png')  # imagem (100x100)

# Criar os widgets da janela separando em dois, direita e esquerda
# separada por uma barra branca
UpFrame: Frame = Frame(jan, width=300, height=200, bg='GREEN', relief='raise')
UpFrame.pack(side=TOP)

LowFrame = Frame(jan, width=300, height=395, bg='MIDNIGHTBLUE', relief='raise')
LowFrame.pack(side=RIGHT)
# bg é a cor de fundo
LogoLabel = Label(UpFrame, image=logo, bg='GREEN')  # Exibi um texto ou imagem
LogoLabel.place(x=100, y=50)  # posicionando a imagem
# fg é a cor do texto

UserLabel = Label(LowFrame, text='Usuário:', font=('Century Gothic', 12), bg='MIDNIGHTBLUE', fg='White')
UserLabel.place(x=5, y=150)

UserEntry = ttk.Entry(LowFrame, width=30)
UserEntry.place(x=100, y=152)

PassLabel = Label(LowFrame, text='Senha:', font=('Century Gothic', 12), bg='MIDNIGHTBLUE', fg='White')
PassLabel.place(x=5, y=185)

PassEntry = ttk.Entry(LowFrame, width=30, show='*')  # width = tmanho máximo do texto, show = mostra * no lugar digitado
PassEntry.place(x=100, y=187)

login_label = Label(LowFrame, text='Faça seu Login', font=('Century Gothic', 16), bg='MIDNIGHTBLUE', fg='yellow')
login_label.place(x=5, y=15)


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
        if user in verifylogin and senha in verifylogin:
            messagebox.showinfo(title='Login Info', message='Login Efetuado com Sucesso.')
    except:
        messagebox.showerror(title='Login info', message='Acesso Negado')


def register():
    # Removendo widgets de login
    loginbuttom.place(x=5000)
    cadbuttom.place(x=5000)
    # Inserindo Widgets de cadastro
    nomelabel = Label(LowFrame, text='Nome:', font=('Century Gothic', 12), bg='MIDNIGHTBLUE', fg='White')
    nomelabel.place(x=5, y=80)
    nomeentry = ttk.Entry(LowFrame, width=30)
    nomeentry.place(x=100, y=82)

    emaillabel = Label(LowFrame, text='Email:', font=('Century Gothic', 12), bg='MIDNIGHTBLUE', fg='White')
    emaillabel.place(x=5, y=115)
    emailentry = ttk.Entry(LowFrame, width=30)
    emailentry.place(x=100, y=117)

    def registerbd():
        nome = nomeentry.get()
        usuario = UserEntry.get()
        email = emailentry.get()
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
        # Removendo width de registro
        cadlabel.place_forget()
        nomelabel.place_forget()
        nomeentry.place_forget()
        emaillabel.place_forget()
        emailentry.place_forget()
        voltar.place(x=2000)
        registrar.place(x=2000)
        # Inserindo width de button
        loginlabel = Label(LowFrame, text='Faça seu Login', font=('Century Gothic', 16), bg='MIDNIGHTBLUE', fg='yellow')
        loginlabel.place(x=5, y=15)
        loginbuttom.place(x=120, y=225)
        cadbuttom.place(x=10, y=355)

    cadlabel = Label(LowFrame, text='Faça seu Cadastro', font=('Century Gothic', 16), bg='MIDNIGHTBLUE', fg='yellow')
    cadlabel.place(x=5, y=15)
    voltar = ttk.Button(LowFrame, text='Voltar', width=10, command=voltar)
    voltar.place(x=10, y=355)

    registrar = ttk.Button(LowFrame, text='Registrar', width=14, command=registerbd)
    registrar.place(x=110, y=225)


# Botões

loginbuttom = ttk.Button(LowFrame, text='Login', width=10, command=login)
loginbuttom.place(x=120, y=225)

cadbuttom = ttk.Button(LowFrame, text='Cadastre-se', width=14, command=register)
cadbuttom.place(x=10, y=355)

jan.mainloop()
