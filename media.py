#o codigo lendo varios alunos e a mesma coisa
#a unica diferença e que ele esta de uma repetição
#de um enquanto
#ler entradas do usuario
situacao = ""
alunos = [] #lista que guardara todos os alunos cadastrados
cont = 0 # variavel que controla a repetição
escolha_usuario = int(input("quantos usuarios você quer cadastrar:")) #variavel que guarda quantas vezes o condigo vai rodar
while cont < escolha_usuario:
    nome = input("digite o nome do aluno")
    faltas = float(input("digite as faltas do aluno"))
    #4 notas
    n1 = float(input("digite a primeira nota do aluno"))
    n2 = float(input("digite a segunda nota do aluno"))
    n3 = float(input("digite a terceira nota do aluno"))
    n4 = float(input("digite a quarta nota do aluno"))

    #calculo da média
    media = (n1+n2+n3+n4)/4

    #logica da situação
    if faltas > 31:
        situacao = "reprovado por falta"
    elif media >= 8:
        situacao = "aprovado"
    elif media >= 5: #recuperação
        recuperacao = float(input("quanto o aluno tirou na recuperção:"))#ler nota da prova de recuperação
        if recuperacao >= (10-media):
            situacao = "aprovado na recuperação"
        else:
            situacao = "reprovado na recuperação"
    else:
     situacao = "reprovado por média"

    #enviar os dados do aluno para a lista alunos
    alunos.append([nome,faltas,media,situacao])
    #relatório
    cont+= 1
print(alunos)