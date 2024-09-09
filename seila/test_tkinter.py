from customtkinter import *
import os

def user_btn():
    user = os.getlogin()
    btn_user.configure(text=f"Usuário: {user}")

def combobox_callback(choice):
    if choice == "Dark mode":
        set_appearance_mode("dark")
    elif choice == "Light mode":
        set_appearance_mode("light")
    elif choice == "System":
        set_appearance_mode("system")

# Configuração da janela principal
app = CTk()
app.geometry("850x500")
app.resizable(False, False)

# Criando widgets
btn_user = CTkLabel(master=app, width=100, height=30, text="", justify=LEFT, fg_color="transparent")
combobox_var = StringVar(value="Dark mode")  # Valor padrão
btn_appear_mode = CTkComboBox(master=app, width=200, height=30, border_width=2, border_color="white",
                              values=["Dark mode", "Light mode", "System"], command=combobox_callback, variable=combobox_var)
btn_tac_semanal = CTkButton(master=app, width=135, height=230, corner_radius=10, border_color="yellow", hover_color="yellow",
                            border_width=2, text="TAC's semanais", text_color="white", fg_color="transparent", cursor="hand2")

# Posicionando widgets
btn_user.place(x=20, y=20)
btn_appear_mode.place(x=630, y=20)
btn_tac_semanal.place(x=20, y=70)

# Exibindo o nome do usuário
user_btn()

# Exibindo a janela
app.mainloop()
