def menu():
    print(f"\nMenu:")
    print(f"1 - Quantidade total de filmes")
    print(f"2 - Informações de um filme pelo título")
    print(f"3 - FIlmes de um diretor específico")
    print(f"4 - Filmes de um gênero específico")
    print(f"5 - Média de duração dos filmes")
    print(f"6 - Sair")

menu()

while True:
    opcao = input(f"Escolha uma opção: ").strip()

    if opcao == "1":
        print(contar_filmes())
    elif opcao == "2":
        print(info_por_titulo())
    elif opcao == "3":
        print(filmes_por_diretor())
    elif opcao == "4":
        print(filmes_por_genero())
    elif opcao == "5":
        print(media_duracao())
    elif opcao == "6":
        print("Saindo...")
        break
    else:
        print(f"Opção inválida!")