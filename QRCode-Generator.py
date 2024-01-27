import qrcode
from tkinter import messagebox, Tk, Label, Entry, Button, Toplevel
from PIL import Image, ImageTk
import os

def exibir_qr_code(url):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    
    # Salvar a imagem temporariamente
    img_path = 'qrExport.png'
    img.save(img_path)

    # Cria uma janela personalizada
    janela = Toplevel()
    janela.title("QR Code Gerado")

    # Carrega a imagem gerada
    imagem_qr = ImageTk.PhotoImage(Image.open(img_path))
    label_imagem = Label(janela, image=imagem_qr)
    label_imagem.image = imagem_qr
    label_imagem.pack()

    # Adiciona uma mensagem informativa
    mensagem = f"QR Code gerado para o endereço:\n{url}"
    label_mensagem = Label(janela, text=mensagem)
    label_mensagem.pack()

    # Remove a imagem temporária após a janela ser fechada
    janela.protocol("WM_DELETE_WINDOW", lambda: [janela.destroy(),os.remove(img_path)])

    janela.mainloop()

def gera_qr_code():
    url = website_entry.get()

    if len(url) == 0:
        messagebox.showinfo(title="Erro!", message="Favor insira uma URL válida") #Messagebox para erro
    else:
        opcao_escolhida = messagebox.askokcancel(
            title=url,
            message=f"O endereço URL é: \n "
                    f"Endereço: {url} \n "
                    f"Pronto para salvar?")

        if opcao_escolhida:
            exibir_qr_code(url)

if __name__ == '__main__':
    window = Tk()
    window.title("Gerador de Código QR")
    window.config(padx=10, pady=100)

    # Labels
    website_label = Label(text="URL:")
    website_label.grid(row=2, column=0)

    # Entradas
    website_entry = Entry(width=35)
    website_entry.grid(row=2, column=1, columnspan=2)
    website_entry.focus()

    add_button = Button(text="Gerar QR Code", width=36, command=gera_qr_code)
    add_button.grid(row=4, column=1, columnspan=2)

    window.mainloop()
