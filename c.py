import smtplib
#from decouple impor config
remitente= 'email@gmail.com'
destinatario = 'email@gmail.com'


subject = 'Prueba de Correo'
message= 'Hola desde Python'

# Email con asunto
message = 'Subject: {}\n\n\n {}'.format(subject, message)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('ramirezecho@gmail.com','tuPassword')

# envio del email
server.sendmail(remitente,destinatario, message)

# Cerrar sesion
server.quit()
