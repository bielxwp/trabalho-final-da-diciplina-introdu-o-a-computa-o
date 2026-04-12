alunos = {}

def cadastrar():
    try:
        quantidade_de_alunos = int(input("Quantos alunos deseja cadastrar?"))
        if quantidade_de_alunos > 0:
            print("ATENÇÂO: se você tentar cadastrar um aluno ja existente \no programa vai excluir as notas associadas a esse aluno e você vai ter que adicionar novamente)")
            #essa parte abaixo não foi requisitada no roteiro, mas implementei para que possa adicionar multiplos alunos de uma só vez
            for i in range(quantidade_de_alunos):
                usuarios = input(f"informe o nome do aluno {i+1}: ")
                alunos[usuarios] = []
            print("Aluno(s) cadastrados(s) com sucesso")
        else:
            print("entrada invalida, digite apenas numeros inteiros maiores ou igual a 1")
    except:
        print("entrada invalida, por favor tente novamente")
def lançar_notas():
    if list(alunos.keys()) != []:
        print("Você escolheu lançar notas")
        print(f"Essa é a lista de alunos cadatrados\n{list(alunos.keys())}")
        alvo = input("Deseja adicionar as notas de qual aluno?(digite o nome do aluno): ")
        if alvo in alunos:
            for j in range(3):
                while True:
                    try:
                        n123 = float(input(f"digite a nota {j+1}:"))
                        alunos[alvo].append(n123)
                        break
                    except:
                        print("entrada invalida, tente novamente, digite apenas numeros")
            print("notas lançadas com sucesso")
        else:
            print("aluno não encontrado")
    else:
        print("erro, nenhum aluno cadastrado")
def listar_alunos():
    print("essa é a lista de alunos cadastrados e suas respectivas notas")
    print(alunos)

def remover_aluno():
    if list(alunos.keys()) != []:
        remover = input((f"deseja remover qual aluno?\n{list(alunos.keys())}\nDigite o nome do aluno:"))
        if remover in list(alunos.keys()):
            for i in list(alunos.keys()):
                if remover == i:
                    alunos.pop(i)
                    print("aluno removido com sucesso")
        else:
            print("entrada invalida, por favor tente novamente")
    else:
        print("erro, nenhum aluno cadastrado")

def media_aluno():
    if list(alunos.keys()) != []:
        m = input(f"deseja ver a media de qual aluno?\nlista de alunos:{list(alunos.keys())}\nDigite o nome do aluno: ")
        if m in alunos:
            if alunos[m] != []:
                for i in list(alunos.keys()):
                    if m == i:
                        print(f"a media do aluno {m} é {sum(alunos[i])/3:.2f}")
            else:
                print("nenhuma nota associada por favor verificar")
        else:
            print("aluno não encontrado")
    else:
        print("erro, voce não cadastrou nenhum aluno")
def media_geral():
    if alunos != {}:
        media_geral = []
        for i in list(alunos.keys()):
            if alunos[i] != []:
                media_indiv = sum(alunos[i])/len(alunos[i])
                media_geral.append(media_indiv)
            else:
                print("algum aluno esta sem nota, verifique")
        if len(media_geral) > 0:
            print(f"A media geral da turma é {sum(media_geral)/len(media_geral):.2f}")
    else:
        print("nenhum aluno ou nenhuma nota adicionada para fazer a media geral")

def situação_aluno():
    if list(alunos.keys()) != []:
        m = input(f"Deseja ver a situação de qual aluno?\n{list(alunos.keys())}\nDigite o nome do aluno: ")
        if m in alunos:
            if alunos[m] != []:
                for i in list(alunos.keys()):
                    if m == i and sum(alunos[i])/3 >= 6+(22/10):#professor essa media minima é por causa da personalização obrigatoria que o roteiro pedia
                        print("Aprovado")
                    elif m == i and sum(alunos[i])/3 >= 5 and sum(alunos[i])/3 < 6+ (22/10):
                        print("Recuperação")
                    elif m == i and sum(alunos[i])/3 <5:
                        print("Reprovado")
            else:
                print("as notas desse aluno ainda não foram lançadas")
        else:
            print("aluno não encontrado")
    else:
        print("nenhum aluno encontrado")

def menu():
    print("\nMENU")
    print("1 - Cadastrar alunos")
    print("2 - Ver lista de alunos cadastrados")
    print("3 - Lançar notas")
    print("4 - Remover um aluno")
    print("5 - Verificar media de um aluno")
    print("6 - Verificar situação de um aluno")
    print("7 - Mostrar media geral da turma")
    print("8 - Sair")
while True:
    menu()
    try:
        op = int(input("Digite a opção desejada: "))
        if op == 1:
            cadastrar()
        elif op == 2:
            listar_alunos()
        elif op == 3:
            lançar_notas()
        elif op == 4:
            remover_aluno()
        elif op == 5:
            media_aluno()
        elif op == 6:
            situação_aluno()
        elif op == 7:
            media_geral()
        elif op == 8:
            break
        else:
            print("opção invalida, tente novamente")
    except:
        print("entrada invalida, tente novamente")
