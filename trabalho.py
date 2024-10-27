#trabalho clube PeR, Cartao Cidadao
nome=str(input("Nome:"))
apelido=str(input("Apelido:"))
data_nascimento= print("Data de nascimento")
dia_n= int(input("Dia:"))
mes_n= int(input("Mes:"))
ano_n= int(input("Ano:"))
digitos_cartaocid= print("Cartao de cidadao")
dig1= int(input("Digito 1:"))
dig2= int(input("Digito 2:"))
dig3=int(input("Digito 3:"))
dig4= int(input("Digito 4:"))
dig5= int(input("Digito 5:"))
dig6= int(input("Digito 6:"))
dig7= int(input("Digito 7:"))
dig8=int(input("Digito 8:"))
Check_digit= int(input("Check Digit:"))




print (nome, apelido)
print (dia_n, mes_n, ano_n)
print (dig1,dig2,dig3,dig4,dig5,dig6,dig7,dig8)

if dig1/11 == 1 or dig1/11 == dig1:
    print("Digito 1: Valido")
else:
    print("Digito 1: Invalido")

if dig2/11 == 1 or dig2/11 == dig2:
    print("Digito 2: Valido")
else:
    print("Digito 2: Invalido")

if dig3/11 == 1 or dig3 == dig3:
    print("Digito 3: Valido")
else:
    print("Digito 3: Invalido")

if dig4/11 == 1 or dig4 == dig4:
    print("Digito 4: Valido ")
else:
    print("Digito 4: Invalido")
    
if dig5 == 1 or dig5 == dig5:
    print("Digito 5: Valido")
else:
    print("Digito 5: Invalido")

if dig6/11 == 1 or dig6/11 == dig6:
    print("Digito 6: Valido")
else:
    print("Digito 6: Invalido")

if dig7/11 == 1 or dig7/11 == dig7:
    print("Digito 7: Valido")
else:
    print("Digito 7: Invalido")

if dig8/11 == 1 or dig8/11 == dig8:
    print("Digito 8: Valido")
else:
    print("Digito 8: Invalido")
