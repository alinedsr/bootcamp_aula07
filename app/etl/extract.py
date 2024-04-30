import csv

path = "../input/produtos_estoque.csv"

def read_csv(path: str) -> list[dict]:
    """
    Função usada para leitura de arquivos do tipo CSV.
    """
    data = []
    with open(path, mode="r", encoding="utf-8") as arquivo:
        leitor_csv = csv.DictReader(arquivo)
        for linha in leitor_csv:
            # Adiciona cada linha (um dicionário) à lista de dados
            data.append(linha)
    return data

#VALIDAÇÃO
# estoque_itens: list[dict]
# estoque_itens = read_csv(path)

# for item in estoque_itens:
#     print(item)