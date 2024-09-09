import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from model.model import Model

class Controller:
    def __init__(self, view):
        self.view = view
        self.model = Model()
        self.setup_view()

    def setup_view(self):
        self.view.login_button.config(command=self.login)
        # Note: fetch_button é configurado apenas depois que a tela de automação é exibida
        # self.view.fetch_button.config(command=self.load_csv)

    def login(self):
        username = self.view.username_entry.get()
        password = self.view.password_entry.get()
        if self.model.validate_login(username, password):
            self.view.show_automation_screen()
            self.view.fetch_button.config(command=self.load_csv)  # Configura o botão aqui
        else:
            messagebox.showerror("Erro de Login", "Usuário ou senha incorretos")

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            df = self.model.read_csv(file_path)
            if df is not None:
                self.view.show_csv_data(df)
            else:
                messagebox.showerror("Erro", "Não foi possível ler o arquivo CSV.")
