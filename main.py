
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

@app.route("/galeria")
def galeria():
    return render_template('galeria.html', galeria=msl.gera_galeria())

@app.route("/servicos")
def servico():
    serv_all = msl.gera_servicos()
    return render_template('servicos.html',cabelo=serv_all[0],pele=serv_all[1],tratamentos=serv_all[2])

@app.route("/downloads")
def downloads():
    return render_template('downloads.html')

@app.route("/inserir", methods=['POST','GET'])
def inserir():
    nome = request.form.get('nome')
    valor = request.form.get('valor')
    desc = request.form.get('descricao')
    delete = request.form.get('delete')
    marca = request.form.get('marca')
    servico = request.form.get('servico')
    classe = request.form.get('classe')
    delete_serv = request.form.get('delete_serv')
    if request.method == 'POST':
        file = request.files['arquivo']
        image_string = base64.b64encode(file.read()).decode('utf-8')
        imagem = request.files['imagem']
        imagem_base64 = base64.b64encode(imagem.read()).decode('utf-8')
    else:
        imagem_base64 = ''
        image_string = ''
    promo = request.form.get('promocao')
    if imagem_base64 != '':
        msl.insere_galeria(imagem_base64)
        return render_template('atualizarbase.html',prod_list=msl.gera_prod_list(),nomes='',valor='',promo='', img='',resp='',marca='',desc='', categoria='', imagem=imagem_base64, resp_serv="Insira/Atualize/Delete o serviço",nome_serv="")
    if servico != None:
        resp = msl.insere_serv(servico,classe,delete_serv)
        return render_template('atualizarbase.html',prod_list=msl.gera_prod_list(),resp_serv=resp,nome_serv=servico,nomes=f'',valor='',promo='', img='',marca='', desc='', categoria='',imagem='', resp='Insira/Atualize/Delete o produto')
    if nome != None:
        res = msl.insere_prod(nome,valor,image_string,promo,delete,marca,desc)
        return render_template('atualizarbase.html',prod_list=msl.gera_prod_list(),nomes=f'{nome}',valor=valor,promo=promo, img=image_string,resp=res,marca=marca,desc=desc, categoria=classe, imagem=imagem_base64, resp_serv="Insira/Atualize/Delete o serviço",nome_serv="")
    else:
        return render_template('atualizarbase.html',prod_list=msl.gera_prod_list(),nomes=f'',valor='',promo='', img='',marca='',desc='', resp='Insira/Atualize/Delete o produto')



@app.route("/att", methods=['POST','GET'])
def attinsert():
    if request.method == 'POST':
        # Lida com o upload do PDF
        if 'ProHair_file' in request.files:
            pdf_file = request.files['ProHair_file']
            if pdf_file.filename != '' and allowed_file(pdf_file.filename):
                caminho_pdf = os.path.join(app.config['UPLOAD_FOLDER'], 'Prohair.pdf')
                pdf_file.save(caminho_pdf)
        if 'fluence_file' in request.files:
            pdf_file = request.files['fluence_file']
            if pdf_file.filename != '' and allowed_file(pdf_file.filename):
                caminho_pdf = os.path.join(app.config['UPLOAD_FOLDER'], 'Fluence.pdf')
                pdf_file.save(caminho_pdf)

        if 'Nuance_file' in request.files:
            pdf_file = request.files['Nuance_file']
            if pdf_file.filename != '' and allowed_file(pdf_file.filename):
                caminho_pdf = os.path.join(app.config['UPLOAD_FOLDER'], 'Nuance.pdf')
                pdf_file.save(caminho_pdf)



    return render_template('atualizatabelas.html')

if __name__ == "__main__":
    app.run()

