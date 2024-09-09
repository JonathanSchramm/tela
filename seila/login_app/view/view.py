import tkinter as tk
from tkinter import ttk

class View:
    def __init__(self, root):
        self.root = root
        self.username_entry = None
        self.password_entry = None
        self.login_button = None
        self.fetch_button = None
        self.result_display = None
        self.setup_login_screen()
        self.center_window()

    def setup_login_screen(self):
        self.root.title("Tela de Login")

        # Grid Layout
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Campos de login
        tk.Label(self.root, text="Usuário:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.username_entry = tk.Entry(self.root, width=50)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Senha:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.password_entry = tk.Entry(self.root, show="*", width=50)
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        # Botão de login
        self.login_button = tk.Button(self.root, text="Login")
        self.login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    def show_automation_screen(self):
        self.root.title("Tela de Automação CSV")
        self.clear_screen()

        # Botão para carregar CSV
        tk.Label(self.root, text="Selecione um arquivo CSV:").grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.fetch_button = tk.Button(self.root, text="Carregar CSV")
        self.fetch_button.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        # Área de exibição de dados CSV
        self.result_display = ttk.Treeview(self.root)
        self.result_display.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")

        # Configurar a exibição
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def show_csv_data(self, df):
        if self.result_display is not None:
            self.result_display.destroy()

        # Recria o Treeview
        self.result_display = ttk.Treeview(self.root)
        self.result_display.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")

        # Configure columns
        self.result_display["columns"] = list(df.columns)
        for col in df.columns:
            self.result_display.heading(col, text=col)
            self.result_display.column(col, width=100)

        # Insert data
        for _, row in df.iterrows():
            self.result_display.insert("", "end", values=list(row))

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def center_window(self):
        # Atualiza a geometria da janela após o ajuste dos widgets
        self.root.update_idletasks()
        
        # Obtém a largura e a altura da tela
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Obtém a largura e a altura da janela
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()

        # Calcula a posição x e y para centralizar a janela
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Define a geometria da janela
        self.root.geometry(f'{window_width}x{window_height}+{x}+{y}')
