import json
import os

def load_data(notes):

    caminho = os.path.join("static", "data", notes)

    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def load_template(index):

    caminho = os.path.join("static", "templates", index)

    with open(caminho, "r", encoding="utf-8") as arquivo:
        return arquivo.read()

def adiciona_nota (params):

    caminho = os.path.join("static", "data", "notes.json")
    anotacoes = load_data("notes.json")
    anotacoes.append(params)

    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(anotacoes, arquivo, ensure_ascii=False, indent=2)