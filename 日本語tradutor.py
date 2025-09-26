palavras = {
    "ねこ": "gato",
    "いぬ": "cachorro",
    "みず": "água",
    "たべもの": "comida",
    "のみもの": "bebida",
    "ほん": "livro",
    "がっこう": "escola",
    "せんせい": "professor(a)",
    "ともだち": "amigo(a)",
    "うち": "casa",
    "くるま": "carro",
    "じてんしゃ": "bicicleta",
    "やさい": "vegetal",
    "くだもの": "fruta",
    "て": "mão",
    "あし": "pé",
    "め": "olho",
    "みみ": "orelha",
    "はな": "nariz/flor",  # depende do contexto
    "くち": "boca"
}


while True:

    entrada = input("Digite uma palavra em japonês (Hiragana) ou 'sair' para sair: ")
    if entrada == "sair":
        break
    if entrada in palavras:
        print (" A tradução é:", palavras[entrada])
    else:
        print("Palavra não encontrada")

print("Programa encerrado.")
