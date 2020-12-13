#Area de 3ntrada de dados do usuario!
#class dados(Nome, Salario, arroz, N_pessoas, Azeite, Feijao, manteiga v_arroz):
usuario = input("diginte o teu nome: ")
Salario =int(input("Quanto voce recebe por mes:"))
arroz = int(input("A Quantidades do arroz em Kg por dia:"))
N_pessoas=int(input("quantos sao na casa:"))
Azeite = int(250)
Feijao=int(400)
manteiga=int(75)
v_arroz=int(1300)
Bar=int(input("Quantos dia por semana sair pra o bar:"))
Divida=int(input("Quanto tem de Divida nesse mes:"))
sonho=input("tens algum objectivo futuro: ")
Celular=5500
m_Celular=1500
m_carro=30000
coputador=8000
pc=15000
#fechamebto
#def muo():
 #   def cosumu_arroz():
if(N_pessoas >= arroz):
    print(f"Senhor(a) {usuario} O cosumu e muito grande /n Aconselho uma poupaça")
    Resultado=( N_pessoas/2)
    print(f"Senhor(a) {usuario} Voces sao {N_pessoas} pessoas  voces podem cosumir {Resultado} por refeicao")
else:
    if(N_pessoas < arroz):
        print()
def calculoprecentagem():
    Total=int(manteiga+Feijao+Azeite+v_arroz)
#    if(Salario < Total):
    prensentagem=(Total*100/Salario)
    print(f"Senhor(a) {usuario} a tua presentagem de cosumu e {prensentagem}%")
#def calculodivida():
Total=int(manteiga+Feijao+Azeite+v_arroz)
div=""
if(Divida ==div):
    Divida=0
else:
    Resu_divida =(Divida+Total)
    if(Resu_divida > Salario):
        print(f"Senhor(a) {usuario} esse mes nao vais poder pagar as dividas")
        if(Resu_divida < Salario):
            print(f"Senhor(a) {suario} esse mes  vais poder pagar todas dividas")
        else:
            if(Resu_divida <= Salario):
                print(f"Senhor(a) {usuario} esse mes  vais poder pagar as dividas mas nao faras{sonho} nem {objectivo}")
                S_divida=input("desejas pagar as dividas?:")
                sim=["Sim","sim","s","S","yes","Yes"]
                nao=["Nao","nao","n","N","No","no"]
                if S_divida in sim:
                    print("voce disse sim")
                else:
                    if S_divida in nao:                                     print("rentirando as dividas das listas")
calculoprecentagem()
