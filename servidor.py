from flask import Flask, render_template_string, request, redirect
import views
from utils import apagar_nota, alternar_favorita


app = Flask(__name__)

# configura a pasta de arquivos estaticos
app.static_folder = 'static'

@app.route('/')
def index():

    return render_template_string(views.index())

@app.route('/submit', methods=['POST'])
def submit_form():
    titulo = request.form.get('titulo')
    detalhes = request.form.get('detalhes')

    views.submit(titulo, detalhes)
    return redirect('/')

@app.route('/delete/<int:identificador>')
def delete(identificador):
    apagar_nota(identificador)
    return redirect('/')

@app.route('/update/<int:identificador>')
def edit(identificador):
    pagina = views.edit(identificador)
    if pagina is None:
        return redirect('/')
    return render_template_string(pagina)

@app.route('/update', methods=['POST'])
def update():
    identificador = request.form.get('id', type=int)
    titulo = request.form.get('titulo')
    detalhes = request.form.get('detalhes')
    views.update(identificador, titulo, detalhes)
    return redirect('/')

@app.route('/favorite/<int:identificador>')
def favorite(identificador):
    alternar_favorita(identificador)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)