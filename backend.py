import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import string
import mysql.connector as mysql


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))



def insere_prod(produto,img,delete,marca,desc,esgotado):
    import mysql


    host = 'viaduct.proxy.rlwy.net'
    port = 58177
    database = 'railway'
    user = 'root'
    password = 'HhBBh1gGeBegbEAeh-cH45b-1CfG45bc'
    try:
        conn = mysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            auth_plugin='caching_sha2_password'
        )
        print("Conexão bem-sucedida!")
        resposta = ''

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM prod_info WHERE name = %s", (produto,))
        existing_product = cursor.fetchall()
        cursor.execute(f"SELECT * FROM prod_info WHERE name = '{produto}'")
        existing_desc = cursor.fetchall()
        for row in existing_desc:
            desc_ = row[4]
            esgotado_ = row[5]


        if existing_product:
            if delete == '1':
                cursor.execute(f"DELETE FROM prod_info WHERE name = '{produto}'")
                resposta = 'Produto Deletado'
            else:
                if img != '' and desc != desc_ and esgotado != esgotado_:
                    cursor.execute(f"UPDATE prod_info SET image = '{img}', descricao='{desc}', esgotado='{esgotado}' WHERE name = '{produto}'")
                    resposta = 'Descrição e Imagem Atualizadas'
                elif img == '' and desc != desc_ and esgotado == esgotado_:
                    cursor.execute(f"UPDATE prod_info SET descricao='{desc}' WHERE name = '{produto}'")
                    resposta = 'Descrição Atualizada'
                elif img != '' and desc == desc_ and esgotado == esgotado_:
                    cursor.execute(f"UPDATE prod_info SET image = '{img}' WHERE name = '{produto}'")
                    resposta = 'Imagem Atualizada'
                elif img == '' and desc == desc_ and esgotado != esgotado_:
                    cursor.execute(f"UPDATE prod_info SET esgotado = '{esgotado}' WHERE name = '{produto}'")
                    resposta = 'Estoque atualizado'
                else:
                    resposta = 'Produto sem alterações feitas'
        else:

            cursor.execute(f"INSERT INTO prod_info VALUES(0,'{produto}','{img}','{marca}','{desc}','{esgotado}')")
            resposta = 'Produto Inserido'

        conn.commit()

        conn.close()

        return resposta

    except mysql.Error as err:
        print(f"Erro na conexão: {err}")

def gera_produtos():
    


    host = 'viaduct.proxy.rlwy.net'
    port = 58177
    database = 'railway'
    user = 'root'
    password = 'HhBBh1gGeBegbEAeh-cH45b-1CfG45bc'
    try:
        conn = mysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            auth_plugin='caching_sha2_password'
        )


        cursor = conn.cursor()

        cursor.execute("SELECT * FROM prod_info ORDER BY name ASC")
        table_prod = cursor.fetchall()

        produtos = """"""
        for row in table_prod:
            name = row[1]
            image = row[2]
            brand = row[3]
            desc = row[4]
            if row[5] == "S":
                esgotado = "<span> Esgotado</span>"
            else:
                esgotado = ''
            produtos+=f"""
            <div class='{brand}' id='{name}' onclick='displaydesc(this.id)'>                

            <div class='searched' id='{name}'>
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-x-lg" viewBox="0 0 16 16" id='{row[1]}' onclick="closeitem(this.id); event.stopPropagation();" >
                    <path d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8z"/>
                  </svg>
                <img src="data:image/jpeg;base64,{image}"   alt="">
                <div class='insidediv'>
                <p class='prod_name'>{name}{esgotado}</p>
                <p class='desc' id='{name}_d'>Descrição:<br>{desc}</p>
                <p class="pointer" id='{name}' onclick='send(this.id)'><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-whatsapp" viewBox="0 0 16 16">
                    <path d="M13.601 2.326A7.854 7.854 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102a7.933 7.933 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.898 7.898 0 0 0 13.6 2.326zM7.994 14.521a6.573 6.573 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.557 6.557 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592zm3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.007-.247-.007-.38-.007a.729.729 0 0 0-.529.247c-.182.198-.691.677-.691 1.654 0 .977.71 1.916.81 2.049.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232z"/>
                </svg> Fazer orçamento</p>
                <p class="pointer2" id='{name}' onclick='inserecarrinho(this.id)'>Adicionar ao orçamento</p>
                <p class='saibamais'>Saiba mais</p>
                </div>
                
            </div>
            </div>"""
            


        conn.close()
        return produtos
    except mysql.Error as err:
        print(f"Erro na conexão: {err}")
        return 'falha'




def insere_serv(servico,classe,delete_serv):
    


    host = 'viaduct.proxy.rlwy.net'
    port = 58177
    database = 'railway'
    user = 'root'
    password = 'HhBBh1gGeBegbEAeh-cH45b-1CfG45bc'
    try:
        conn = mysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            auth_plugin='caching_sha2_password'
        )
        print("Conexão bem-sucedida!")
        resposta = ''

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Servicos WHERE servico = %s", (servico,))
        existing_product = cursor.fetchall()


        if existing_product:
            if delete_serv == '1':
                cursor.execute(f"DELETE FROM Servicos WHERE servico = '{servico}'")
                resposta = 'Serviço Deletado'
            else:
                cursor.execute(f"UPDATE Servicos SET valor = '' WHERE servico = '{servico}'")
                resposta = 'Serviço já existe'
        else:
            cursor.execute(f"INSERT INTO Servicos VALUES(0,'{servico}','{classe}','')")
            resposta = 'Serviço Inserido'

        conn.commit()

        conn.close()

        return resposta

    except mysql.Error as err:
        print(f"Erro na conexão: {err}")

def gera_servicos():
    


    host = 'viaduct.proxy.rlwy.net'
    port = 58177
    database = 'railway'
    user = 'root'
    password = 'HhBBh1gGeBegbEAeh-cH45b-1CfG45bc'
    try:
        conn = mysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            auth_plugin='caching_sha2_password'
        )
        cabelo = ''
        pele = ''
        tratamento = ''
        servicos_list = []

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Servicos WHERE classe = 'Cabelo'")
        servicos_cabelo = cursor.fetchall()

        for row in servicos_cabelo:
            cabelo += f'<p>{row[1]}'
        servicos_list.append(cabelo)

        cursor.execute("SELECT * FROM Servicos WHERE classe = 'Pele'")
        servicos_pele = cursor.fetchall()

        for row in servicos_pele:
            pele+= f'<p>{row[1]}'
        servicos_list.append(pele)

        cursor.execute("SELECT * FROM Servicos WHERE classe = 'Rosto'")
        servicos_tratamento = cursor.fetchall()

        for row in servicos_tratamento:
            tratamento+= f'<p>{row[1]}'
        servicos_list.append(tratamento)

        



        conn.close()
        return servicos_list
    except mysql.Error as err:
        print(f"Erro na conexão: {err}")
        return 'falha'


def gera_prod_list():
    


    host = 'viaduct.proxy.rlwy.net'
    port = 58177
    database = 'railway'
    user = 'root'
    password = 'HhBBh1gGeBegbEAeh-cH45b-1CfG45bc'
    try:
        conn = mysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            auth_plugin='caching_sha2_password'
        )


        cursor = conn.cursor()

        cursor.execute("SELECT * FROM prod_info")
        table_prod = cursor.fetchall()
        produtos_cadastrados = ''
        for row in table_prod:
            nome = row[1]
            desc = row[4]
            esgotado = row[5]
            produtos_cadastrados += f"<div class='pesquisa_{esgotado}' id='{nome}' onclick=\"insert_to('{nome}', '{desc}')\">{nome}</div>"

            

        return produtos_cadastrados
    except mysql.Error as err:
        print(f"Erro na conexão: {err}")

def insere_galeria(imagem, carrossel):
    


    host = 'viaduct.proxy.rlwy.net'
    port = 58177
    database = 'railway'
    user = 'root'
    password = 'HhBBh1gGeBegbEAeh-cH45b-1CfG45bc'
    try:
        conn = mysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            auth_plugin='caching_sha2_password'
        )
        print("Conexão bem-sucedida!")

        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO Galeria VALUES(0,'{carrossel}','{imagem}')")

        conn.commit()

        conn.close()

    except mysql.Error as err:
        print(f"Erro na conexão: {err}")



def gera_galeria():
    


    host = 'viaduct.proxy.rlwy.net'
    port = 58177
    database = 'railway'
    user = 'root'
    password = 'HhBBh1gGeBegbEAeh-cH45b-1CfG45bc'
    try:
        conn = mysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            auth_plugin='caching_sha2_password'
        )

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Galeria")
        table = cursor.fetchall()

        galeria = ''
        carrossel = ''
        galeria_list = []
        for row in table:
            if row[1] == 'carrossel':
                carrossel += f"<img src='data:image/jpeg;base64,{row[2]}'>"
            else:
                galeria+=f"<img src='data:image/jpeg;base64,{row[2]}'>"
        conn.close()

        galeria_list.append(galeria)
        galeria_list.append(carrossel)

        return galeria_list
    except mysql.Error as err:
        print(f"Erro na conexão: {err}")
        return 'falha'

def lista_galeria():
    


    host = 'viaduct.proxy.rlwy.net'
    port = 58177
    database = 'railway'
    user = 'root'
    password = 'HhBBh1gGeBegbEAeh-cH45b-1CfG45bc'
    try:
        conn = mysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            auth_plugin='caching_sha2_password'
        )

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Galeria")
        table = cursor.fetchall()

        lista_galeria = ''

        for row in table:
            if row[1] == "carrossel":
                lista_galeria+=f"<div><img src='data:image/jpeg;base64,{row[2]}'><input type='file' name='imgupdate' id='imgupdate_{row[0]}'><select name='carrossel' id='carrossel_{row[0]}'><option value='carrossel'>Carrossel</option><option value=''>Página</option></select><button type='button' id='{row[0]}' onclick='updateimg(this.id)'>Atualizar</button><button type='button' id='{row[0]}' onclick='deleteimg(this.id)'>Deletar</button></div><br>"
            else:
                lista_galeria+=f"<div><img src='data:image/jpeg;base64,{row[2]}'><input type='file' name='imgupdate' id='imgupdate_{row[0]}'><select name='carrossel' id='carrossel_{row[0]}'><option value=''>Página</option><option value='carrossel'>Carrossel</option></select><button type='button' id='{row[0]}' onclick='updateimg(this.id)'>Atualizar</button><button type='button' id='{row[0]}' onclick='deleteimg(this.id)'>Deletar</button></div><br>"
        conn.close()
        return lista_galeria
    except mysql.Error as err:
        print(f"Erro na conexão: {err}")
        return 'falha'
    
def atualiza_galeria(img, carrossel, id):
    


    host = 'viaduct.proxy.rlwy.net'
    port = 58177
    database = 'railway'
    user = 'root'
    password = 'HhBBh1gGeBegbEAeh-cH45b-1CfG45bc'
    try:
        conn = mysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            auth_plugin='caching_sha2_password'
        )

        cursor = conn.cursor()
        if img != '' and carrossel != 'np':
            cursor.execute("UPDATE Galeria SET imagem = %s, name = %s WHERE id = %s", (img, carrossel, id))
            print('a')
        elif img == '' and carrossel != 'np':
            cursor.execute("UPDATE Galeria SET name = %s WHERE id = %s", (carrossel, id))
            print('b')
        else:
            cursor.execute("UPDATE Galeria SET imagem = %s WHERE id = %s", (img, id))
            print('c')

        # Commitar as mudanças na base de dados
        conn.commit()
        conn.close()
        return 'ok'
    except mysql.Error as err:
        print(f"Erro na conexão: {err}")
        return 'falha'
    
def deleteimgfromgalery(id):
    


    host = 'viaduct.proxy.rlwy.net'
    port = 58177
    database = 'railway'
    user = 'root'
    password = 'HhBBh1gGeBegbEAeh-cH45b-1CfG45bc'
    try:
        conn = mysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            auth_plugin='caching_sha2_password'
        )

        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM Galeria WHERE id = '{id}'")

        conn.commit()
        conn.close()
        return 'ok'
    except mysql.Error as err:
        print(f"Erro na conexão: {err}")
        return 'falha'
    
def insere_dicas(link, imagem):
    

    host = 'viaduct.proxy.rlwy.net'
    port = 58177
    database = 'railway'
    user = 'root'
    password = 'HhBBh1gGeBegbEAeh-cH45b-1CfG45bc'
    
    try:
        conn = mysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            auth_plugin='caching_sha2_password'
        )

        cursor = conn.cursor()
        # Usando parâmetros na consulta SQL para evitar injeção de SQL
        sql = "INSERT INTO Dicas (link, imagem) VALUES (%s, %s)"
        data = (link, imagem)
        cursor.execute(sql, data)

        conn.commit()
        conn.close()
        return 'sucesso'
    except mysql.Error as err:
        print(f"Erro na conexão: {err}")
        return 'falha'


def gera_dicas():
    


    host = 'viaduct.proxy.rlwy.net'
    port = 58177
    database = 'railway'
    user = 'root'
    password = 'HhBBh1gGeBegbEAeh-cH45b-1CfG45bc'
    try:
        conn = mysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            auth_plugin='caching_sha2_password'
        )

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Dicas")
        table = cursor.fetchall()
        dicas = ''

        for row in table:
            dicas+= f"<a href='{row[1]}' target='_blank'><img src='data:image/jpeg;base64,{row[2]}'></a>"

        conn.commit()
        conn.close()
        return dicas
    except mysql.Error as err:
        print(f"Erro na conexão: {err}")
        return 'falha'  


def lista_dicas():
    


    host = 'viaduct.proxy.rlwy.net'
    port = 58177
    database = 'railway'
    user = 'root'
    password = 'HhBBh1gGeBegbEAeh-cH45b-1CfG45bc'
    try:
        conn = mysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            auth_plugin='caching_sha2_password'
        )

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Dicas")
        table = cursor.fetchall()
        lista_dicas = ''

        for row in table:
            lista_dicas+= f"<div><img src='data:image/jpeg;base64,{row[2]}'><button id='{row[0]}' onclick='deletedicas(this.id)'>Apagar</button></div><br>"

        conn.commit()
        conn.close()
        return lista_dicas
    except mysql.Error as err:
        print(f"Erro na conexão: {err}")
        return 'falha'  
    
def delete_dicas(id):
    


    host = 'viaduct.proxy.rlwy.net'
    port = 58177
    database = 'railway'
    user = 'root'
    password = 'HhBBh1gGeBegbEAeh-cH45b-1CfG45bc'
    try:
        conn = mysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            auth_plugin='caching_sha2_password'
        )

        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM Dicas WHERE id = '{id}'")

        conn.commit()
        conn.close()
        return 'ok'
    except mysql.Error as err:
        print(f"Erro na conexão: {err}")
        return 'falha'
    

def verification(user_code):
    with open("code.txt", "r") as file:
        code = file.readline().strip()

    user_code = user_code.replace(" ","")
    if user_code == code:
        with open("code.txt", "w") as file:
            file.write("")
        return True
    else:
        with open("code.txt", "w") as file:
            file.write("")
        return False

def envia_email():
    
    sender_email = "joaopedrogoncalvesdeoliveirasi@gmail.com"
    receiver_emails = ["juniorsouzajp@yahoo.com.br","thecodeofdavinci@gmail.com"]
    password = "pkls eiuo zdzp zdqs"

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = ", ".join(receiver_emails)  # Concatenando os endereços de email separados por vírgula
    message['Subject'] = "Alguém está tentando acessar o painel de admin do site matildesenna.com"
    random_sequence = generate_random_string(22)
    with open("code.txt", "w") as file:
        file.write(random_sequence)
    body = f"""
            Tentativa de acesso identificado no painel de admin, para liberar o acesso insira o código na página: {random_sequence} 
    """

    message.attach(MIMEText(body, 'plain'))

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    server.login(sender_email, password)

    text = message.as_string()
    server.sendmail(sender_email, receiver_emails, text)  # Usando receiver_emails em vez de receiver_email

    server.quit()




def promo():

    import json
    import os

    arquivo_json = "static/archives/promo.json"

    promo = ''

    if os.path.exists(arquivo_json) and os.path.getsize(arquivo_json) > 0:
        with open(arquivo_json, "r") as arquivo:
            dados = json.load(arquivo)

        for chave, valor in dados.items():
            promo+=f"<img src='data:image/jpeg;base64,{valor}'>"

    return promo




def insere_promo(img):

    import json
    import os

    arquivo_json = "static/archives/promo.json"
    
    # Verifica se o arquivo JSON existe e não está vazio
    if os.path.exists(arquivo_json) and os.path.getsize(arquivo_json) > 0:
        with open(arquivo_json, "r") as arquivo:
            dados = json.load(arquivo)
    else:
        dados = {}
    
    # Encontra o maior número de chave presente no dicionário
    if dados:
        ultima_chave = max(map(int, dados.keys()))
        proxima_chave = str(ultima_chave + 1)
    else:
        proxima_chave = "0"
    
    # Adiciona a imagem à próxima chave disponível
    dados[proxima_chave] = img
    
    # Escreve os dados de volta no arquivo JSON
    with open(arquivo_json, "w") as arquivo:
        json.dump(dados, arquivo)
    
    return 'Inserido'

def lista_promo():

    import json
    import os

    arquivo_json = "static/archives/promo.json"

    lista_promo = ''

    if os.path.exists(arquivo_json) and os.path.getsize(arquivo_json) > 0:
        with open(arquivo_json, "r") as arquivo:
            dados = json.load(arquivo)

        for chave, valor in dados.items():
            lista_promo+=f"<div><img src='data:image/jpeg;base64,{valor}'><button id='{chave}' onclick='deletepromo(this.id)'>Apagar</button></div><br>"

    return lista_promo


