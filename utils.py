import os
import sqlite3

CAMINHO_BANCO = os.path.join(os.path.dirname(__file__), "banco.db")

def conectar_banco():
    return sqlite3.connect(CAMINHO_BANCO)

def init_db():
    with conectar_banco() as banco:
        banco.execute("""
            CREATE TABLE IF NOT EXISTS note (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                favorite INTEGER NOT NULL DEFAULT 0
            )
        """)

def carregar_notas():
    with conectar_banco() as banco:
        banco.row_factory = sqlite3.Row
        notas = banco.execute(
            "SELECT id, title, content, favorite FROM note "
            "ORDER BY favorite DESC, id ASC"
        ).fetchall()

    return [
        {
            "id": nota["id"],
            "titulo": nota["title"],
            "detalhes": nota["content"],
            "favorita": bool(nota["favorite"])
        }
        for nota in notas
    ]

def load_data():
    return carregar_notas()

def load_template(index):
    caminho = os.path.join("static", "templates", index)

    with open(caminho, "r", encoding="utf-8") as arquivo:
        return arquivo.read()

def adiciona_nota(params):
    with conectar_banco() as banco:
        banco.execute(
            "INSERT INTO note (title, content) VALUES (?, ?)",
            (params["titulo"], params["detalhes"])
        )

def buscar_nota(identificador):
    with conectar_banco() as banco:
        banco.row_factory = sqlite3.Row
        nota = banco.execute(
            "SELECT id, title, content, favorite FROM note WHERE id = ?",
            (identificador,)
        ).fetchone()

    if nota is None:
        return None

    return {
        "id": nota["id"],
        "titulo": nota["title"],
        "detalhes": nota["content"],
        "favorita": bool(nota["favorite"])
    }

def apagar_nota(identificador):
    with conectar_banco() as banco:
        banco.execute("DELETE FROM note WHERE id = ?", (identificador,))

def atualizar_nota(identificador, titulo, detalhes):
    with conectar_banco() as banco:
        banco.execute(
            "UPDATE note SET title = ?, content = ? WHERE id = ?",
            (titulo, detalhes, identificador)
        )

def alternar_favorita(identificador):
    with conectar_banco() as banco:
        banco.execute(
            "UPDATE note SET favorite = CASE favorite WHEN 1 THEN 0 ELSE 1 END "
            "WHERE id = ?",
            (identificador,)
        )