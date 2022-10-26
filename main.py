from chatbot_ui import BotUI
import tkinter as tk

def main() :

    """ function to start the app """

    main_window = tk.Tk() # create window

    app = BotUI(root=main_window) # create app object

    main_window.mainloop() # start the app

if __name__ == "__main__":

    main() 
