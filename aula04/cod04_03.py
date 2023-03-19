#Operadores relcaionais
nome=input("Digite seu nome: ")
ano_nasc=int(input("Digite o ano em que nasceu: "))
ano_atual=int(input("Digite o ano atual"))
idade=ano_atual-ano_nasc
print(nome,"você tem",idade,"anos de idade, tem mais do que 18 anos?",idade>=18)