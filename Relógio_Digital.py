import tkinter as tk
from time import strftime

# Função para atualizar o tempo
def atualiza_tempo():
    tempo_str = strftime('%H:%M:%S %p')  # Formato de 12 horas com AM/PM
    label_tempo.config(text=tempo_str)
    label_tempo.after(1000, atualiza_tempo)  # Atualiza a cada 1000ms (1 segundo)

# Configuração da janela principal
root = tk.Tk()
root.title('Relógio Digital')

# Label para exibir o tempo
label_tempo = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label_tempo.pack(anchor='center')

# Chama a função para iniciar o relógio
atualiza_tempo()

root.mainloop()
