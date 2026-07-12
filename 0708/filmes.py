def menu():
    print(f"\nMenu:")
    print(f"1 - Quantidade total de filmes")
    print(f"2 - Informações de um filme pelo título")
    print(f"3 - FIlmes de um diretor específico")
    print(f"4 - Filmes de um gênero específico")
    print(f"5 - Média de duração dos filmes")
    print(f"6 - Sair")


def adicionar_filme():
    print("Adicionar filme")


def contar_filmes():
    contador = 0
    with open("filmes.txt", "r", encoding="utf-8") as f:
        for linha in f:
            if linha.strip().startswith("Título:"):
                contador += 1
    print(contador)


def info_por_titulo():
    with open("filmes.txt", "r", encoding="utf-8") as f:
        linhas = f.readlines()
        titulo = input("Digite o título do filme: ")
        if titulo == "O Poderoso Chefão":
            linhas_selecionadas = linhas[0:5]
            for linha in linhas_selecionadas:
                print(linha)
        elif titulo == "Interestelar":
            linhas_selecionadas = linhas[6:11]
            for linha in linhas_selecionadas:
                print(linha)
        elif titulo == "Uma Odisseia no espaço":
            linhas_selecionadas = linhas[12:17]
            for linha in linhas_selecionadas:
                print(linha)
        else:
            print("Título inválido!")


def filmes_por_diretor():
    with open("filmes.txt", "r", encoding="utf-8") as f:
        linhas = f.readlines()
        diretor = input("Digite o nome do diretor do filme: ")
        if diretor == "Francis Coppola":
            print(linhas[0])
        elif diretor == "Christopher Nolan": 
            print(linhas[6])
        elif diretor == "Stanley Kubrick":
            print(linhas[12])
        else:
            print("Diretor não encontrado!")
        

def filmes_por_genero():
    with open("filmes.txt", "r", encoding="utf-8") as f:
        linhas = f.readlines()
        genero = input("Digite o genêro de filme que você quer assistir: ")
        if genero == "Crime" or genero == "Drama":
            print(linhas[0])
        elif genero == "Ficção científica":
            print(linhas[6])
            print(linhas[12])
        elif genero == "Aventura":
            print(linhas[6])
        else:
            print("Nenhum filme desse genêro foi encontrado!")


def media_duracao():
    with open("filmes.txt", "r", encoding="utf-8") as f:
        linhas = f.readlines()
        duracao = input(f"Digite a duração do filme que deseja assistir: ")
        if duracao == "175 minutos":
            print(linhas[0])
        elif duracao == "169 minutos":
            print(linhas[6])    
        elif duracao == "142 minutos":
            print(linhas[12])
        else:
            print("Nenhum filme com essa duração encontrado!")   


while True:
    menu()
    opcao = input(f"Escolha uma opção: ").strip()

    if opcao == "0":
        adicionar_filme()
    elif opcao == "1":
        contar_filmes()
    elif opcao == "2":
        info_por_titulo()
    elif opcao == "3":
        filmes_por_diretor()
    elif opcao == "4":
        filmes_por_genero()
    elif opcao == "5":
        media_duracao()
    elif opcao == "6":
        print("Saindo...")
        break
    else:
        print(f"Opção inválida!")