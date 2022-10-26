""" ChatBot User Interface Code """

import tkinter as tk
from bot import Bot
import time 
import os
from tkinter import messagebox as mb



class BotUI(tk.Frame) :

    def __init__(self,root=None,file_path=None) :

        """ method to setup the GUI """

        # initialize the Frame 
        tk.Frame.__init__(self,root)

        self.master = root

        self.master.geometry("500x500+400+50") # main window size

        self.master.title("Loyola Bot")

        self.master.wm_iconbitmap(r"C:\Users\LOKI99\Desktop\python_clg_ project\ChatBot_APP\Chatbot_development_phase\Chatbot_phase_3\chatbot_logo\loyola_logo_new.ico")

        # configuring bg & fg colors
        self.bg1 = "skyblue"
        self.bg2 = "palegreen"
        self.fg1 = "white" 
        self.font = ("Comic Sans MS",15) # font style & size

        ## Menu Bar
        menu = tk.Menu(self.master)

        self.master.config(menu=menu , bd=0)

        # window options
        window_menu = tk.Menu(menu,tearoff=0)

        menu.add_cascade(label="Window",menu=window_menu)

        window_menu.add_command(label="Clear Chat",command=self.clear_chat)

        window_menu.add_command(label="Exit",command=self.exit_app)                         

        # bg color options
        color_menu = tk.Menu(menu,tearoff=0)

        menu.add_cascade(label="Theme",menu=color_menu)

        color_menu.add_command(label="blue",command=self.color_theme_blue)

        color_menu.add_command(label="grey",command=self.color_theme_grey)

        color_menu.add_command(label="dark",command=self.color_theme_dark)

        # output mode
        self.flag_var = tk.IntVar() # flag variable

        self.flag = False

        self.flag_var.set(1) # set default value as 1 i.e, text mode

        output_mode = tk.Menu(menu,tearoff=0)

        menu.add_cascade(label="Output Mode", menu=output_mode)

        output_mode.add_radiobutton(label="text mode", underline=1, variable=self.flag_var, value=1, command=self.output_mode)    

        # links
        link = tk.Menu(menu,tearoff=0)

        menu.add_cascade(label="college links", menu=link)

        link.add_command(label="college website", underline=1, command=self.college_website)

        link.add_command(label="student login", command=self.student_login)

        # help menu bar
        help_options = tk.Menu(menu,tearoff=0)

        menu.add_cascade(label="help",menu=help_options)

        help_options.add_command(label="About app" , command=self.about_app)

        help_options.add_command(label="Project" , command=self.project_desc)


        # creating a frame
        self.text_frame = tk.Frame(self.master,bg="#33313B",bd=7)
        
        self.text_frame.pack(expand=True, fill=tk.BOTH)

        # scrollbar for text box
        self.text_box_scrollbar = tk.Scrollbar(self.text_frame, bd=0)

        self.text_box_scrollbar.pack(fill=tk.Y, side=tk.RIGHT)

        # contains messages
        self.text_box = tk.Text(self.text_frame, yscrollcommand=self.text_box_scrollbar.set,font=("Comic Sans MS",15) ,state=tk.DISABLED,bd=1, padx=6, pady=6, spacing3=8, wrap=tk.WORD, bg=None, relief=tk.GROOVE, width=10, height=1)

        self.text_box.pack(expand=True, fill=tk.BOTH)

        self.text_box_scrollbar.config(command=self.text_box.yview)

        # frame containing user entry field
        self.entry_frame = tk.Frame(self.master,bg="#33313B",bd=1,height=20)

        self.entry_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # entry field
        self.entry_field = tk.Entry(self.entry_frame, bd=8,font=("Comic Sans MS",15),justify=tk.LEFT)

        self.entry_field.pack(fill=tk.X, padx=6, pady=6, ipady=3)

        self.entry_field.bind("<Return>",self.display_query_ans_event) # bind the entry field to the Enter button
                              
        # frame containing send button and emoji button
        self.send_button_frame = tk.Frame(self.master,height=2,bd=0)

        self.send_button_frame.pack(fill=tk.BOTH)

        # send button
        self.send_button = tk.Button(self.send_button_frame,font=("Comic Sans MS",15), text="SEARCH", width=10, relief=tk.GROOVE,fg="#071E3D", bg='#801336',bd=5, command=lambda: self.display_query_ans(None), activebackground="#FFFFFF", activeforeground="#000000")

        self.send_button.pack(side=tk.LEFT, ipady=8)

        # chatbot 
        self.chatbot = Bot()


        self.text_box.configure(state=tk.NORMAL) # 

        self.text_box.insert(tk.END, "Enter your E-mail : ")

        self.text_box.configure(state=tk.DISABLED)

        self.text_box.see(tk.END)

        self.entry_field.delete(0,tk.END)

            
        
    def mail_login(self):

        """ method to get email login detials """

        self.new_win = tk.Toplevel()

        self.new_win.geometry("550x100+200+100")

        self.new_win.title("Email Details")

        self.login_details = tk.Frame(self.new_win,cursor="hand2")

        self.login_details.pack()

        self.label_ = tk.Label(self.login_details, text="Enter Email : ", width=15,font=("ARIAL 14"))

        self.label_.grid(row=0,column=0)

        self.entry_box = tk.Entry(self.login_details, width=30,font=("ARIAL 14"))
        
        self.entry_box.grid(row=1, column=1)

        self.save = tk.Button(self.login_details, text="SAVE", command=self.get_mail_details())

        self.save.grid(row=3, column=1)

        self.close = tk.Button(self.login_details, text="CLOSE", command=self.new_win.destroy)

        self.close.grid(row=3,column=2)

        self.new_win.mainloop()
        

    def get_mail_details(self):

        """ method to retrieve the mail id """

        user_mail_id = str(self.entry_box.get())

        return user_mail_id



    def display_query_ans_event(self,event):

        """ method to display the user query using Enter key"""


        user_query = self.entry_field.get() # retrieve entry field data     

        bot_res = self.chatbot.retrieve_ans(user_query)

        if bot_res == "User mail":

            user_msg = " " + user_query + " \n"

            bot_msg = "BOT : Hi, I am the chatbot for the loyola college.Please feel free to ask any query !!!\n"

            # insert user query into chat log
            self.text_box.configure(state=tk.NORMAL) 

            self.text_box.insert(tk.END, user_msg)

            self.text_box.configure(state=tk.DISABLED)

            self.text_box.see(tk.END)

            # insert bot response into chat log
            self.text_box.configure(state=tk.NORMAL)

            self.text_box.insert(tk.END, bot_msg)

            self.text_box.configure(state=tk.DISABLED)

            self.text_box.see(tk.END)

            self.entry_field.delete(0,tk.END)
            
        else :

            user_msg = "You : {0} \n".format(user_query) # user msg

            bot_msg = "BOT : " + bot_res + "\n" # bot msg
            
            # insert user query into chat log
            self.text_box.configure(state=tk.NORMAL) 

            self.text_box.insert(tk.END, user_msg)

            self.text_box.configure(state=tk.DISABLED)

            self.text_box.see(tk.END)

            # insert bot response into chat log
            self.text_box.configure(state=tk.NORMAL)

            self.text_box.insert(tk.END, bot_msg)

            self.text_box.configure(state=tk.DISABLED)

            self.text_box.see(tk.END)

            self.entry_field.delete(0,tk.END)

            time.sleep(0) # sleep for 0 seconds            

      

    def display_query_ans(self,message) :

        """ method to display the user query """

        user_query = self.entry_field.get() # retrieve entry field data     

        bot_res = self.chatbot.retrieve_ans(user_query)


        if bot_res == "User mail":

            user_msg = " " + user_query + " \n"

            bot_msg = "BOT : Hi, I am the chatbot for the loyola college.\nPlease feel free to ask any query\n"

            # insert user query into chat log
            self.text_box.configure(state=tk.NORMAL) 

            self.text_box.insert(tk.END, user_msg)

            self.text_box.configure(state=tk.DISABLED)

            self.text_box.see(tk.END)

            # insert bot response into chat log
            self.text_box.configure(state=tk.NORMAL)

            self.text_box.insert(tk.END, bot_msg)

            self.text_box.configure(state=tk.DISABLED)

            self.text_box.see(tk.END)

            self.entry_field.delete(0,tk.END)
            
        else :

            user_msg = "You : {0} \n".format(user_query) # user msg

            bot_msg = "BOT : " + bot_res + "\n" # bot msg
            
            # insert user query into chat log
            self.text_box.configure(state=tk.NORMAL) 

            self.text_box.insert(tk.END, user_msg)

            self.text_box.configure(state=tk.DISABLED)

            self.text_box.see(tk.END)

            # insert bot response into chat log
            self.text_box.configure(state=tk.NORMAL)

            self.text_box.insert(tk.END, bot_msg)

            self.text_box.configure(state=tk.DISABLED)

            self.text_box.see(tk.END)

            self.entry_field.delete(0,tk.END)

            time.sleep(0) # sleep for 0 seconds            


        

    def clear_chat(self):
        
        
        """method to clear the chat messages """
    
        # text box is changed to readable & writable state
        self.text_box.config(state=tk.NORMAL)

        # delete the text box content
        self.text_box.delete(1.0, tk.END) 
    
        # text box is changed to readable-only state
        self.text_box.config(state=tk.DISABLED)

    def student_login(self) :

        """ method to open the student login """

        os.system('start "" "http://183.82.101.217:8080/lastudentportal/students/loginManager/youLogin.jsp" ')
    
    def college_website(self) :

        """method to open the college website """

        os.system("@echo off")

        os.system('start "" "https://www.loyolaacademyugpg.ac.in/" ')
    
    
    def about_app(self) :

        """ App description """

        # display the app info using a message box()
        mb.showinfo("Loyola BOT","Just type in the query you want to search")       


    def project_desc(self) :

        """ Project Description """

        # display the project desc. using message box
        mb.showinfo("Loyola BOT Developers","1. P Akshay Raj\n2. Y Lokesh Kumar")
        
        
    def exit_app(self) :

        """  method to close the app """

        exit() # exit python programs


    def output_mode(self) :
        

        self.op_mode = self.flag_var.get() # get flag variable value

        if self.op_mode == 1 :

            self.flag = False # flag variable for thread

        elif self.op_mode == 2:

            self.flag = True # flag variable for thread
    

    def color_theme_dark(self) :

        """ method to change the color theme """

        self.master.config(bg="#2a2b2d")

        self.text_frame.config(bg="#2a2b2d")

        self.text_box.config(bg="#212121", fg="#FFFFFF")

        self.entry_frame.config(bg="#2a2b2d")

        self.entry_field.config(bg="#212121", fg="#FFFFFF", insertbackground="#FFFFFF")

        self.send_button_frame.config(bg="#2a2b2d")

        self.send_button.config(bg="#212121", fg="#FFFFFF", activebackground="#212121", activeforeground="#FFFFFF")

        self.tl_bg = "#212121"

        self.tl_bg2 = "#2a2b2d"

        self.tl_fg = "#FFFFFF"


    def color_theme_blue(self) :

        """ method to change the color theme """

        self.master.config(bg="#202040")

        self.text_frame.config(bg="#202040")

        self.text_box.config(bg="#202060", fg="#FFFFFF")

        self.entry_frame.config(bg="#202040")

        self.entry_field.config(bg="#202060", fg="#FFFFFF", insertbackground="#FFFFFF")

        self.send_button_frame.config(bg="#263b54")

        self.send_button.config(bg="#1c2e44", fg="#FFFFFF" , activebackground="#1c2e44", activeforeground="#ffffff")

        self.tl_bg = "#1c2e44"

        self.tl_bg2 = "#263b54"

        self.tl_fg = "#FFFFFF"


    def color_theme_grey(self) :

        """ method to change the color theme """

        self.master.config(bg="#444444")

        self.text_frame.config(bg="#444444")

        self.text_box.config(bg="#4f4f4f", fg="#ffffff")

        self.entry_frame.config(bg="#444444")

        self.entry_field.config(bg="#4f4f4f", fg="#ffffff", insertbackground="white")

        self.send_button_frame.config(bg="#444444")

        self.send_button.config(bg="#4f4f4f", fg="#ffffff", activebackground="#4f4f4f", activeforeground="#ffffff")

        self.tl_bg = "#4f4f4f"

        self.tl_bg2 = "#444444"

        self.tl_fg = "#ffffff"                     

