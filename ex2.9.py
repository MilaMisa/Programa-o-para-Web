data = input("Digite a data (mm/dd/aaaa): ")
partes = data.split('/')

mes = int(partes[0])
dia = int(partes[1])
ano = int(partes[2])

if (dia >= 1 and dia <=31) and (mes >=1 and mes <=12) and ano >= 1000: 
    print("É uma data válida!")
else:
    print("Não é uma data válida!")




