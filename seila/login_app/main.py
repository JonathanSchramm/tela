import tkinter as tk
from view.view import View
from controller.controller import Controller

def main():
    root = tk.Tk()
    app_view = View(root)
    app_controller = Controller(app_view)
    root.mainloop()

if __name__ == "__main__":
    main()
