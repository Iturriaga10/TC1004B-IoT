user_mes = raw_input("Escribe la fecha en el formato dd-mm-aaaa: ").split("-")
print(user_mes)
mes = int(user_mes[1])
meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 
         7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 
         12:'diciembre'}

if mes > 12:
    print("Mes Invalida")
else:
    print("Dia " + user_mes[0] + " Mes " + meses[mes] + " Anho " + user_mes[2])
