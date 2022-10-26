from DNN_model import ChatbotDNN
from Chatbot_SendMail import EmailService

import warnings

warnings.filterwarnings("ignore")

bot = ChatbotDNN()

user = "lokesh15kumar1999@gmail.com"

bot.fit_model() 

bot.train_model()

while True :

    ques = input("Enter : ")

    ans = str(bot.mail_response(ques))

    print(ans)
    print(type(ans))
    
    mail = EmailService(user_email=user, file_name=ans)

    mail.send_mail()
    
    print("A mail has been sent to you")

    if ans == None :
        break
