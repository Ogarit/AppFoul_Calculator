import customtkinter as CTk


class CalculadoraFaltas:
    def __init__(self, master):

        self.master = master
        self.master.grid_columnconfigure((0, 1), weight=1)
        self.master.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

        # Cria os widgets
        self.horas_label = CTk.CTkLabel(master, text='Horas:', font=('Helvetica', 12))
        self.horas_entry = CTk.CTkEntry(master, width=100)
        self.minutos_label = CTk.CTkLabel(master, text='Minutos:', font=('Helvetica', 12))
        self.minutos_entry = CTk.CTkEntry(master, width=100)
        self.porcentagem_presenca_label = CTk.CTkLabel(master, text='Porcentagem de presença:', font=('Helvetica', 12))
        self.porcentagem_presenca_entry = CTk.CTkEntry(master, width=100)
        self.calcular_button = CTk.CTkButton(master, text='Calcular', command=self.calcular)
        self.resultado_label = CTk.CTkLabel(master, text='Faltas:', font=('Helvetica', 12))
        self.resultado_entry = CTk.CTkEntry(master, width=100)

        # Posiciona os widgets
        self.horas_label.grid(row=0, column=0, sticky='w', padx=10, pady=5)
        self.horas_entry.grid(row=0, column=1, padx=10, pady=5)
        self.minutos_label.grid(row=1, column=0, sticky='w', padx=10, pady=5)
        self.minutos_entry.grid(row=1, column=1, padx=10, pady=5)
        self.porcentagem_presenca_label.grid(row=2, column=0, sticky='w', padx=10, pady=5)
        self.porcentagem_presenca_entry.grid(row=2, column=1, padx=10, pady=5)
        self.calcular_button.grid(row=3, column=0, sticky='e', padx=10, pady=5)
        self.resultado_label.grid(row=4, column=0, sticky='w', padx=10, pady=5)
        self.resultado_entry.grid(row=4, column=1, padx=10, pady=5)

    def calcular(self):
        # Obtém os valores dos widgets
        try:
            horas = self.horas_entry.get() if self.horas_entry.get() != '' else 0
            minutos = self.minutos_entry.get() if self.minutos_entry.get() != '' else 0
            porcentagem_presenca = float(self.porcentagem_presenca_entry.get().replace(',', '.'))

            # Calcula as faltas
            total_minutos = int(horas) * 60 + int(minutos)
            minutos_faltantes = total_minutos * (1 - porcentagem_presenca / 100)

            # Atualiza o resultado
            faltas_horas = int(minutos_faltantes // 60)
            faltas_minutos = int(minutos_faltantes % 60)
            self.resultado_entry.delete(0, 'end')
            self.resultado_entry.insert(0, f'{faltas_horas}:{faltas_minutos:02}')
        except ValueError:
            self.resultado_entry.delete(0, 'end')
            self.resultado_entry.insert(0, 'Erro % de faltas')


def app():
    root = CTk.CTk()
    root.title('Calculadora de faltas')
    root.iconbitmap('1492693845-calculator_83582.ico')

    calculadora = CalculadoraFaltas(root)

    root.mainloop()

if __name__ == '__main__':
    app()
