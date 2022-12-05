import smtplib

def send_msg(msg):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("tulio.silva@spinengenharia.com.br", "mdkmfllgteymclto")
    server.sendmail("dercarapp@gmail.com","tulio.silva@spinengenharia.com.br",f"Usuário Cadastrado\n\n{msg}".encode('utf-8'))
    print('passo send')