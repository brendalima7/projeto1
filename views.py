from utils import adiciona_nota, atualizar_nota, buscar_nota, load_data, load_template

def index():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(
            id=dados['id'],
            title=dados['titulo'],
            details=dados['detalhes'],
            favorite='favorita' if dados['favorita'] else 'nao-favorita',
            favorite_text='★' if dados['favorita'] else '☆',
            favorite_title='desfavoritar' if dados['favorita'] else 'favoritar'
        )
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def submit(titulo, detalhes):
    params = {
        'titulo': titulo,
        'detalhes': detalhes
    }
    adiciona_nota(params)

def edit(identificador):
    nota = buscar_nota(identificador)
    if nota is None:
        return None

    return load_template('update.html').format(
        id=nota['id'],
        title=nota['titulo'],
        details=nota['detalhes']
    )

def update(identificador, titulo, detalhes):
    atualizar_nota(identificador, titulo, detalhes)
