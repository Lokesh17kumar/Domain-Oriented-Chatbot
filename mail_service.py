""" program to send mail to the User """

# modules
import os
import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailService(object) :
    
    def __init__(self,file_name=None,user_email=None) :

        """ method to initialize the mail requirements """

        self.user_email = user_email # user mail id

        ## CHATBOT MAIL DETAILS
        self.bot_email = "loyolabot@gmail.com" # bot email id

        self.bot_pwd = "Loyola@123" # bot mail passwords

        self.file_path = r"C:\Users\LOKI99\Desktop\python_clg_ project\ChatBot_APP\Chatbot_development_phase\Chatbot_phase_3\pdfs"

        self.file_name = file_name # file name

        self.pdf_file = os.path.join(self.file_path,self.file_name)

        self.subject = "Email from Loyola Bot" # mail subject

        self.body = "This is a auto generated email" # mail body         

        # create a MULTIPART message & set headers
        self.message = MIMEMultipart() # to create multi-part message

        self.message["From"] = self.bot_email # From header

        self.message["To"] = self.user_email # To header

        self.message["Subject"] = self.subject # subject header


        # add body part to mail
        self.message.attach(MIMEText(self.body,"plain"))

        # open the the file & read the data
        with open(self.pdf_file,"rb") as attachment :

            # base part 
            self.attach_part = MIMEBase("application","octet-stream") # file data

            self.attach_part.set_payload(attachment.read()) # to set the entire message object's to payload(content)

        # encode file in ASCII chars to send by mail
        encoders.encode_base64(self.attach_part)

        # add header as key & value pair to attachment part
        self.attach_part.add_header("Content-Disposition",f"atatchment; filename = {self.file_name}")

        # add attachment to message & covert to string
        self.message.attach(self.attach_part)

        self.text = self.message.as_string()


    def  send_mail(self) :

        """ method to send the mail """

        # create secure SSL tunnel/path to send the mail
        context = ssl.create_default_context()

        # setting up gmail server
        server = smtplib.SMTP_SSL("smtp.gmail.com",465,context=context)

        # login the mail with bot mail id and passwords
        server.login(self.bot_email, self.bot_pwd)

        # send mail
        server.sendmail(self.bot_email, self.user_email, self.text)       
