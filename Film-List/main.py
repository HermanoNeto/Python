import requests, json


def requisicao(Titulo):
    try:
        req=requests.get(f"http://www.omdbapi.com/?t={Titulo}&type=movie&apikey=641baf7e")
        dicionario=json.loads(req.text)
        return dicionario
    except Exception as error:
        print(error)
        return None

def print_detalhes(filme):
    print("Título: ",filme["Title"])
    print("Ano: ",filme["Year"])
    print("Duração: ",filme["Runtime"])
    print("Genero: ",filme["Genre"])
    print("Atores: ",filme["Actors"])
    print("Diretores: ",filme["Director"])
    print("Linguagem: ",filme["Language"])
    print("Sinopse: ",filme["Plot"])
    print("\n")

sair=False
while not sair:
    filme=input("Escreva o nome de um filme\nOu digite SAIR para fechar ").strip()

    if filme=="sair":
        sair=True
    else:
        pesquisa=requisicao(filme)
        if pesquisa["Response"]=="False":
            print("Filme não encontrado")
        else:
            print_detalhes(pesquisa)







