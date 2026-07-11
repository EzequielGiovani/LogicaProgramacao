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
        titulo = input("Digite o título do filme: ")
        linhas = f.readlines()
        if titulo == "O Poderoso Chefão":
            linhas_selecionadas = linhas[0:5]
            for linha in linhas_selecionadas:
                print(linha)
        elif titulo == "Interestelar":
            linhas_selecionadas = linhas[6:11]
            for linha in linhas_selecionadas:
                print(linha)
        else:
            linhas_selecionadas = linhas[12:17]
            for linha in linhas_selecionadas:
                print(linha)


def filmes_por_diretor():
    print("Filmes por diretor")

def filmes_por_genero():
    print("Filmes por genêro")

def media_duracao():
    print("Media de duração")
    

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
        media_de_duracao()
    elif opcao == "6":
        print("Saindo...")
        break
    else:
        print(f"Opção inválida!")