
from flask import Flask, redirect, render_template, request
import base64
import backend as msl
import os



app = Flask(__name__, template_folder='templates')
app.config['UPLOAD_FOLDER'] = 'static/archives'
app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'xlsx', 'xls'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']



@app.route("/")
def home():
    return render_template('index.html')

@app.route("/produtos")
def produtos():
    return render_template('produtos.html',produtos=msl.gera_produtos())

@app.route("/contato")
def contato():
    return render_template('contatos.html')

@app.route("/inserir", methods=['POST','GET'])
def inserir():
    nome = request.form.get('nome')
    valor = request.form.get('valor')
    delete = request.form.get('delete')
    if request.method == 'POST':
        file = request.files['arquivo']
        image_string = base64.b64encode(file.read()).decode('utf-8')
    else:
        image_string = ''
    promo = request.form.get('promocao')
    
    if nome != None:
        res = msl.insere_prod(nome,valor,image_string,promo,delete)
        return render_template('atualizarbase.html',nomes=f'{nome}',valor=valor,promo=promo, img=image_string,resp=res)
    else:
        return render_template('atualizarbase.html',nomes=f'',valor='',promo='', img='',resp='Insira/Atualize/Delete o produto')



@app.route("/att", methods=['POST','GET'])
def attinsert():
    if request.method == 'POST':
        # Lida com o upload do PDF
        if 'pdf_file' in request.files:
            pdf_file = request.files['pdf_file']
            if pdf_file.filename != '' and allowed_file(pdf_file.filename):
                caminho_pdf = os.path.join(app.config['UPLOAD_FOLDER'], 'Prohair.pdf')
                pdf_file.save(caminho_pdf)

        # Lida com o upload do Excel
        if 'excel_file' in request.files:
            excel_file = request.files['excel_file']
            if excel_file.filename != '' and allowed_file(excel_file.filename):
                caminho_excel = os.path.join(app.config['UPLOAD_FOLDER'], 'Nuance.xlsx')
                excel_file.save(caminho_excel)

    return render_template('atualizatabelas.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)

