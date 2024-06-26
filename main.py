
from flask import Flask, redirect, render_template, request, session, jsonify, url_for
import base64
import backend as msl
import os




app = Flask(__name__, template_folder='templates')
app.config['UPLOAD_FOLDER'] = 'static/archives'
app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'xlsx', 'xls'}
app.secret_key = '0000'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']



@app.route("/")
def home():
    
    if session.get('admin'):
        if session.get('admin') == 1:
            return render_template('index.html', promo=msl.promo())
        else:
            session['admin'] = 0
            return render_template('index.html',promo=msl.promo())
    else:
        session['admin'] = 0
        return render_template('index.html',promo=msl.promo()) 

@app.route("/produtos")
def produtos():
    return render_template('produtos.html',produtos=msl.gera_produtos())

@app.route("/contato")
def contato():
    return render_template('contatos.html')

@app.route("/galeria")
def galeria():
    galeria = msl.gera_galeria()
    return render_template('galeria.html', galeria=galeria[0], carrossel=galeria[1])

@app.route("/servicos")
def servico():
    serv_all = msl.gera_servicos()
    return render_template('servicos.html',cabelo=serv_all[0],pele=serv_all[1],tratamentos=serv_all[2],promo=msl.promo())

@app.route("/downloads")
def downloads():
    return render_template('downloads.html')

@app.route("/admin", methods=['POST', 'GET'])
def login_admin():
    if request.method == "POST":
        code = request.form.get('code')
        if session.get('admin') == 1:
            page = request.form.get('page')
            if page == "inserir":
                return redirect("/inserir")
            elif page == "galeria":
                return redirect("/inseregaleria")
            elif page == "video":
                return redirect("/videopage")
            elif page == "promo":
                return redirect("/inserepromo")
            else:
                return redirect("/att")
        else:

            if code == "":
                msl.envia_email()
                return render_template('admin.html', enviado='Um código foi gerado e enviado para o administrador, insira o código para acessar')
            else:
                page = request.form.get('page')
                if msl.verification(code) == True:
                    session['admin'] = 1
                    if page == "inserir":
                        return redirect("/inserir")
                    elif page == "galeria":
                        return redirect("/inseregaleria")
                    elif page == "video":
                        return redirect("/videopage")
                    elif page == "promo":
                        return redirect("/inserepromo")
                    else:
                        return redirect("/att")
                else:
                    return render_template('admin.html', enviado='Código errado')
    else:
        return render_template('admin.html', enviado='')


@app.route("/inserir", methods=['POST','GET'])
def inserir():
    if session.get('admin') == 0:
        return redirect("/admin")
    else:
        nome = request.form.get('nome')
        desc = request.form.get('descricao')
        delete = request.form.get('delete')
        marca = request.form.get('marca')
        esgotado = request.form.get('esgotado')
        if esgotado == "N":
            resp_esgotado = "Não"
        else:
            resp_esgotado = "Sim"
        servico = request.form.get('servico')
        classe = request.form.get('classe')
        delete_serv = request.form.get('delete_serv')
        if request.method == 'POST':
            file = request.files['arquivo']
            image_string = base64.b64encode(file.read()).decode('utf-8')
        else:
            image_string = ''


        if servico != None:
            resp = msl.insere_serv(servico,classe,delete_serv)
            return render_template('atualizarbase.html',prod_list=msl.gera_prod_list(),esgotado_template='',resp_serv=resp,nome_serv=servico,nomes=f'', img='',marca='', desc='', categoria='', resp='Insira/Atualize/Delete o produto')
        if nome != None:
            res = msl.insere_prod(nome,image_string,delete,marca,desc,esgotado)
            return render_template('atualizarbase.html',prod_list=msl.gera_prod_list(),esgotado_template=resp_esgotado,nomes=f'{nome}', img=image_string,resp=res,marca=marca,desc=desc, categoria=classe, resp_serv="Insira/Atualize/Delete o serviço",nome_serv="")
        else:
            return render_template('atualizarbase.html',prod_list=msl.gera_prod_list(),esgotado_template='',nomes=f'', img='',marca='',desc='', resp='Insira/Atualize/Delete o produto')

@app.route("/inseregaleria", methods=['POST','GET'])
def insere_gal():
    if session.get('admin') == 0:
        return redirect("/admin")
    else:
        if request.method == 'POST':
            imagem = request.files['imagem']
            imagem_base64 = base64.b64encode(imagem.read()).decode('utf-8')
            carrossel = request.form.get("carrossel")
        else:
            imagem_base64 = ''
        if imagem_base64 != '':
            msl.insere_galeria(imagem_base64, carrossel)
            return render_template('inseregaleria.html',imagem=imagem_base64,listaimg=msl.lista_galeria())
        else:
            return render_template('inseregaleria.html',imagem='',listaimg=msl.lista_galeria())

@app.route("/atualizagaleria", methods=['POST'])
def atualizagaleria():

    data = request.json
    
    img = data.get('img')
    carrossel = data.get('carrossel')
    id = data.get('id')
    msl.atualiza_galeria(img, carrossel, id)
    return 'ok'
    
@app.route("/deleteimg", methods=['POST'])
def deleteimg():
    data = request.json
    id = data.get('id')

    msl.deleteimgfromgalery(id)

    return 'ok'

@app.route("/dicas", methods=['GET'])
def dicas():
    dicas = msl.gera_dicas()
    return render_template('dicas.html', dicas=dicas)

@app.route("/att", methods=['POST','GET'])
def attinsert():
    if session.get('admin') == 0:
        return redirect("/admin")
    else:
        if request.method == 'POST':

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
            if 'fluence_file2' in request.files:
                pdf_file = request.files['fluence_file2']
                if pdf_file.filename != '' and allowed_file(pdf_file.filename):
                    caminho_pdf = os.path.join(app.config['UPLOAD_FOLDER'], 'Fluence2.pdf')
                    pdf_file.save(caminho_pdf)
            if 'Nuance_file' in request.files:
                pdf_file = request.files['Nuance_file']
                if pdf_file.filename != '' and allowed_file(pdf_file.filename):
                    caminho_pdf = os.path.join(app.config['UPLOAD_FOLDER'], 'Nuance.pdf')
                    pdf_file.save(caminho_pdf)
            if 'Burana_file' in request.files:
                pdf_file = request.files['Burana_file']
                if pdf_file.filename != '' and allowed_file(pdf_file.filename):
                    caminho_pdf = os.path.join(app.config['UPLOAD_FOLDER'], 'Burana.pdf')
                    pdf_file.save(caminho_pdf)
        return render_template('atualizatabelas.html')
    
@app.route("/videopage", methods=['GET','POST'])
def video_page():
    if session.get('admin') == 0:
        return redirect("/admin")
    else:
        if request.method == 'POST':
            imagem = request.files['imagem']
            imagem_base64 = base64.b64encode(imagem.read()).decode('utf-8')
            link_video = request.form.get('linkvideo')
            msl.insere_dicas(link_video,imagem_base64)
            return render_template('video.html',imagem=imagem_base64,dicascad=msl.lista_dicas())
        else:
            return render_template('video.html',imagem='',dicascad=msl.lista_dicas())
        
@app.route("/deletevideo", methods=['POST'])
def delete_video():
    result = request.json
    id = result.get('id')
    msl.delete_dicas(id)
    return 'ok'

@app.route("/inserepromo", methods=['POST','GET'])

def inserepromo():
    if request.method == 'POST':
        imagem = request.files['imagem']
        imagem_base64 = base64.b64encode(imagem.read()).decode('utf-8')
        res = msl.insere_promo(imagem_base64)
        return render_template('inserepromo.html',resposta=res,listaimg=msl.lista_promo(), imagem=imagem_base64)
    else:
        return render_template('inserepromo.html',resposta='',listaimg=msl.lista_promo(), imagem='')

@app.route("/deletepromo", methods=['POST','GET'])

def deletepromo():

    import json

    data = request.get_json()

    id = json.loads(data)
    id = str(id)
    file_path = "static/archives/promo.json"

    with open(file_path, 'r') as file:
        data = json.load(file)


    if id in data:
        
        del data[id]


        with open(file_path, 'w') as file:
            json.dump(data, file)
    
    return 'ok'



if __name__ == "__main__":
    app.run(debug=True,port=8000)

