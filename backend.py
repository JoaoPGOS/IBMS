def insere_prod(produto, valor, img, promo,delete,marca,desc):
    import mysql.connector


    host = 'viaduct.proxy.rlwy.net'
    port = 58177
    database = 'railway'
    user = 'root'
    password = 'HhBBh1gGeBegbEAeh-cH45b-1CfG45bc'
    try:
        conn = mysql.connector.connect(
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

        if promo == 'Não':
            promo = 0
        if existing_product:
            if delete == '1':
                cursor.execute(f"DELETE FROM prod_info WHERE name = '{produto}'")
                resposta = 'Produto Deletado'
            else:
                cursor.execute(f"UPDATE prod_info SET value = {valor}, promo = {promo} WHERE name = '{produto}'")
                resposta = 'Produto Atualizado'
        else:

            cursor.execute(f"INSERT INTO prod_info VALUES(0,'{produto}','{valor}','{img}','{promo}','{marca}','{desc}')")
            resposta = 'Produto Inserido'

        conn.commit()

        conn.close()

        return resposta

    except mysql.connector.Error as err:
        print(f"Erro na conexão: {err}")

def gera_produtos():
    import mysql.connector


    host = 'viaduct.proxy.rlwy.net'
    port = 58177
    database = 'railway'
    user = 'root'
    password = 'HhBBh1gGeBegbEAeh-cH45b-1CfG45bc'
    try:
        conn = mysql.connector.connect(
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

        produtos = """"""
        promot = ''
        for row in table_prod:
            if row[4] == '1' or row[4] == 1:
                promot = '<p class="prm">Promoção!</p>'
            else:
                promot = ''
            produtos+=f"""
            <div class='{row[5]}'>
            <div class='searched' id='{row[1]}'>

                <img src="data:image/jpeg;base64,{row[3]}" alt="">
                <p class='prod_name'>{row[1]}</p>
                <p class='prod_value'>R${row[2]}</p>
                <p class='desc'>{row[6]}</p>
                <p class="pointer" id='{row[1]}' onclick='send(this.id,{row[2]})'><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-whatsapp" viewBox="0 0 16 16">
                    <path d="M13.601 2.326A7.854 7.854 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102a7.933 7.933 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.898 7.898 0 0 0 13.6 2.326zM7.994 14.521a6.573 6.573 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.557 6.557 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592zm3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.007-.247-.007-.38-.007a.729.729 0 0 0-.529.247c-.182.198-.691.677-.691 1.654 0 .977.71 1.916.81 2.049.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232z"/>
                </svg> Fazer orçamento</p>
                <p class="pointer2" id='{row[1]}' onclick='inserecarrinho(this.id,{row[2]})'>Adicionar ao carrinho</p>
{promot}
            </div>
            </div>"""
            


        conn.close()
        return produtos
    except mysql.connector.Error as err:
        print(f"Erro na conexão: {err}")
        return 'falha'




def insere_serv(servico,valor_serv,classe,delete_serv):
    import mysql.connector


    host = 'viaduct.proxy.rlwy.net'
    port = 58177
    database = 'railway'
    user = 'root'
    password = 'HhBBh1gGeBegbEAeh-cH45b-1CfG45bc'
    try:
        conn = mysql.connector.connect(
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
                cursor.execute(f"UPDATE Servicos SET valor = {valor_serv} WHERE servico = '{servico}'")
                resposta = 'Serviço Atualizado'
        else:
            cursor.execute(f"INSERT INTO Servicos VALUES(0,'{servico}','{classe}','{valor_serv}')")
            resposta = 'Serviço Inserido'

        conn.commit()

        conn.close()

        return resposta

    except mysql.connector.Error as err:
        print(f"Erro na conexão: {err}")

def gera_servicos():
    import mysql.connector


    host = 'viaduct.proxy.rlwy.net'
    port = 58177
    database = 'railway'
    user = 'root'
    password = 'HhBBh1gGeBegbEAeh-cH45b-1CfG45bc'
    try:
        conn = mysql.connector.connect(
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
            cabelo += f'<p>R${row[3]} - {row[1]}'
        servicos_list.append(cabelo)

        cursor.execute("SELECT * FROM Servicos WHERE classe = 'Pele'")
        servicos_pele = cursor.fetchall()

        for row in servicos_pele:
            pele+= f'<p>R${row[3]} - {row[1]}'
        servicos_list.append(pele)

        cursor.execute("SELECT * FROM Servicos WHERE classe = 'Tratamento'")
        servicos_tratamento = cursor.fetchall()

        for row in servicos_tratamento:
            tratamento+= f'<p>R${row[3]} - {row[1]}'
        servicos_list.append(tratamento)

        



        conn.close()
        return servicos_list
    except mysql.connector.Error as err:
        print(f"Erro na conexão: {err}")
        return 'falha'


def gera_prod_list():
    import mysql.connector


    host = 'viaduct.proxy.rlwy.net'
    port = 58177
    database = 'railway'
    user = 'root'
    password = 'HhBBh1gGeBegbEAeh-cH45b-1CfG45bc'
    try:
        conn = mysql.connector.connect(
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
            produtos_cadastrados+=f"<div class='pesquisa' id='{row[1]}' onclick='insert_to(this.id,{row[2]})'>{row[1]}</div>"

        return produtos_cadastrados
    except mysql.connector.Error as err:
        print(f"Erro na conexão: {err}")