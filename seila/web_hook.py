import tkinter as tk
from tkinter import scrolledtext, messagebox
from playwright.sync_api import sync_playwright

# Função para validar o login
def validate_login(username, password):
    login_url = 'https://auth.dio.me/realms/master/protocol/openid-connect/auth?client_id=spa-core-client&redirect_uri=https%3A%2F%2Fweb.dio.me%2F&state=b6181033-9f69-4928-ad85-63215781c625&response_mode=fragment&response_type=code&scope=openid&nonce=9706266a-6844-415d-ac52-d4b505234f05'  # Substitua com a URL de login
    username_selector = '#username'  # Substitua com o seletor de nome de usuário
    password_selector = '#password'  # Substitua com o seletor de senha
    submit_selector = '#kc-login'  # Substitua com o seletor de botão de submit
    success_selector = '.sc-cWSHoV.gufarm'  # Seletor da classe que indica sucesso

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.goto(login_url)
        page.fill(username_selector, username)
        page.fill(password_selector, password)
        page.click(submit_selector)

        try:
            # Aguarda a presença do seletor de sucesso
            page.wait_for_selector(success_selector, timeout=30000)
            browser.close()
            return True
        except Exception as e:
            print(f"Erro ao verificar login: {e}")
            browser.close()
            return False

# Função para abrir a tela de automação
def open_automation_screen():
    login_window.destroy()
    automation_window = tk.Tk()
    automation_window.title("Tela de Automação")

    # Grid Layout
    automation_window.grid_rowconfigure(1, weight=1)
    automation_window.grid_columnconfigure(0, weight=1)

    # URL Entry
    url_label = tk.Label(automation_window, text="Digite o URL do site:")
    url_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    url_entry = tk.Entry(automation_window, width=80)
    url_entry.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

    # Botão Enviar
    fetch_button = tk.Button(automation_window, text="Enviar", command=lambda: fetch_site_content(url_entry.get(), result_text))
    fetch_button.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

    # Área de texto para resultados
    result_label = tk.Label(automation_window, text="Conteúdo do site:")
    result_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

    result_text = tk.StringVar()
    result_display = scrolledtext.ScrolledText(automation_window, wrap=tk.WORD, width=80, height=20)
    result_display.grid(row=4, column=0, padx=10, pady=5, sticky="nsew")
    result_display.config(state=tk.NORMAL)  # Permite edição para atualizar o texto

    def update_result():
        result_display.config(state=tk.NORMAL)
        result_display.delete(1.0, tk.END)
        result_display.insert(tk.END, result_text.get())
        result_display.config(state=tk.DISABLED)

    result_text.trace_add('write', lambda *args: update_result())

    # Inicia a interface gráfica
    automation_window.mainloop()

# Função para buscar o conteúdo do site
def fetch_site_content(url, result_text):
    if not url:
        result_text.set("Por favor, insira um URL válido.")
        return

    result_text.set("Buscando...")
    root.update_idletasks()  # Atualiza a interface gráfica

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        content = page.content()  # Obtém o HTML da página
        browser.close()

    # Atualiza o texto do resultado
    result_text.set(content[:5000])  # Limita a visualização a 5000 caracteres

# Configuração da tela de login
login_window = tk.Tk()
login_window.title("Tela de Login")

# Grid Layout
login_window.grid_rowconfigure(1, weight=1)
login_window.grid_columnconfigure(0, weight=1)

# Campos de login
username_label = tk.Label(login_window, text="Usuário:")
username_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

username_entry = tk.Entry(login_window, width=50)
username_entry.grid(row=0, column=1, padx=10, pady=5)

password_label = tk.Label(login_window, text="Senha:")
password_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

password_entry = tk.Entry(login_window, show="*", width=50)
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Botão de login
login_button = tk.Button(login_window, text="Login", command=lambda: login(username_entry.get(), password_entry.get()))
login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

def login(username, password):
    if validate_login(username, password):
        open_automation_screen()
    else:
        messagebox.showerror("Erro de Login", "Usuário ou senha incorretos")

# Inicia a interface gráfica de login
login_window.mainloop()
