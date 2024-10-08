import flet as ft
import pandas as pd
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googledrive import df

TesteCadastroPIB = df
def main(pagina):
    Rc = ft.Text("Recadastramento")
    Usuarios = ["admin"]
    Senhas = ["123"]

    #Opção para menu de preenchimento automático
    # Função para atualizar sugestões
    
    sugestoes = ft.Column()

    def atualizar_sugestoes(evento):
        texto_digitado = lista_nomes.value.strip().lower()  # Captura o texto digitado na caixa de texto correta
        sugestoes.controls.clear()  # Limpa as sugestões anteriores
        
        if texto_digitado:  # Se houver texto digitado
            nomes_filtrados = [nome for nome in nomes_completos if nome.lower().startswith(texto_digitado)]
            for nome in nomes_filtrados:
                sugestao = ft.TextButton(nome, on_click=lambda e, n=nome: selecionar_nome(n))  # Cria um botão para cada nome filtrado
                sugestoes.controls.append(sugestao)  # Adiciona o botão à coluna de sugestões
        
        pagina.update()  # Atualiza a página para refletir as mudanças

    def selecionar_nome(nome):
        lista_nomes.value = nome  # Atualiza o campo de entrada com o nome selecionado
        sugestoes.controls.clear()  # Limpa as sugestões após a seleção
        pagina.update()  # Atualiza a página para refletir as mudanças


    nomes_completos = TesteCadastroPIB["Nome Completo"].tolist()
    lista_nomes = ft.TextField(label="Nome Completo", on_change=atualizar_sugestoes)

    # Tópicos do Cadastro
    link_foto = ft.TextField(label="link")
    link_foto.value = " " # valor padrão
    #-------------------------------------------------------------------
    matricula = ft.TextField(label="Matrícula")
    nomecompleto = ft.TextField(label="Nome")
    cpf = ft.TextField(label="CPF")
    datanascimento = ft.TextField(label="Data de Nascimento")


    sexo = ft.Dropdown(
    label="Sexo",
    options=[
        ft.dropdown.Option("Masculino"),
        ft.dropdown.Option("Feminino")
    ],
    value="",  # Valor padrão
        )
    #--------------------------------------
    pai_membro = ft.Dropdown(
    label="Seu pai é membro da PIB Pavuna?",
    options=[
        ft.dropdown.Option("Sim"),
        ft.dropdown.Option("Não")
    ],
    value="",  # Valor padrão
        )
    #----------------------------------------   
    nome_mae = ft.TextField(label="Nome da Mãe")
    mae_membro = ft.Dropdown(
    label="Sua mãe é membro da PIB Pavuna?",
    options=[
        ft.dropdown.Option("Sim"),
        ft.dropdown.Option("Não")
    ],
    value="",  # Valor padrão
        )
    #--------------------------------------
    nome_conjuge = ft.TextField(label="Nome do Cônjuge")
    datanascimento_conjuge = ft.TextField(label="Data de Nascimento do Cônjuge")

    conjuge_membro = ft.Dropdown(
    label="Seu cônjuge é membro da PIB Pavuna?",
    options = [
        ft.dropdown.Option("Sim"),
        ft.dropdown.Option("Não")
    ],
    value="",  # Valor padrão
        )
    tipo_sanguineo = ft.TextField(label="Tipo Sanguíneo")
    estado_civil = ft.TextField(label="Estado Civil")
    datacasamento = ft.TextField(label="Data do Casamento")
    profissao = ft.TextField(label="Profissão")
    naturalidade = ft.TextField(label="Naturalidade")
    nacionalidade = ft.TextField(label="Nacionalidade")
    rua = ft.TextField(label="Rua")
    complemento = ft.TextField(label="Complemento")
    bairro = ft.TextField(label="Bairro")
    municipio = ft.TextField(label="Município")
    estado = ft.TextField(label="Estado")
    cep = ft.TextField(label="CEP")
    tel_residencial = ft.TextField(label="Telefone Residencial")
    tel_celular = ft.TextField(label="Telefone Celular")
    email = ft.TextField(label="E-mail")
    nome_pai = ft.TextField(label="Nome do Pai")
    cargo_atual = ft.TextField(label = "Cargo Atual")
    databatismo = ft.TextField(label = "Data do Batismo")
    igrejabatismo = ft.TextField(label = "Igreja onde foi bartizado")
    entradaPIB = ft.TextField(label="Quando se Tornou membro PIB?")
    formaentrada = ft.TextField(label = "Como se tornou membro da PIB?")
    #----------------------------------------------------------------------
    #pedir uma foto
    #-------------------------------------------------------------------

    nome_filho1 = (ft.TextField(label="Nome Filho(a) 1"))
    datanascimento_filho1 = (ft.TextField(label="Data de Nascimento do Filho(a) 1"))
    
    filho1_membro = ft.Dropdown(
    label="Seu filho(a) 1 é membro da PIB Pavuna?",
    options=[
        ft.dropdown.Option("Sim"),
        ft.dropdown.Option("Não")
    ],
    value="",  # Valor padrão
    )

    nome_filho2 = (ft.TextField(label="Nome Filho(a) 2"))
    datanascimento_filho2 = (ft.TextField(label="Data de Nascimento do Filho(a) 2"))
    
    filho2_membro = ft.Dropdown(
    label="Seu filho(a) 2 é membro da PIB Pavuna?",
    options=[
        ft.dropdown.Option("Sim"),
        ft.dropdown.Option("Não")
    ],
    value="",  # Valor padrão
    )

    nome_filho3 = (ft.TextField(label="Nome Filho(a) 3"))
    datanascimento_filho3 = (ft.TextField(label="Data de Nascimento do Filho(a) 3"))
    
    filho3_membro = ft.Dropdown(
    label="Seu filho(a) 3 é membro da PIB Pavuna?",
    options=[
        ft.dropdown.Option("Sim"),
        ft.dropdown.Option("Não")
    ],
    value="",  # Valor padrão
    )

    nome_filho4 = (ft.TextField(label="Nome Filho(a) 4"))
    datanascimento_filho4 = (ft.TextField(label="Data de Nascimento do Filho(a) 4"))
    
    filho4_membro = ft.Dropdown(
    label="Seu filho(a) 4 é membro da PIB Pavuna?",
    options=[
        ft.dropdown.Option("Sim"),
        ft.dropdown.Option("Não")
    ],
    value="",  # Valor padrão
    )

    nome_filho5 = (ft.TextField(label="Nome Filho(a) 5"))
    datanascimento_filho5 = (ft.TextField(label="Data de Nascimento do Filho(a) 5"))
    
    filho5_membro = ft.Dropdown(
    label="Seu filho(a) 5 é membro da PIB Pavuna?",
    options=[
        ft.dropdown.Option("Sim"),
        ft.dropdown.Option("Não")
    ],
    value="",  # Valor padrão
    )
    #-------------------------------------------------------------------
    def upload_to_drive(file_path):
        SCOPES = ['https://www.googleapis.com/auth/drive.file']

        # Autenticação via OAuth2
        creds = None
        if os.path.exists("Ftoken.json"):
            creds = Credentials.from_authorized_user_file("Ftoken.json", SCOPES)
        
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
                creds = flow.run_local_server(port=0)
            
            with open("Ftoken.json", 'w') as token:
                token.write(creds.to_json())
        
        service = build('drive', 'v3', credentials=creds)

        # Carregar o arquivo para o Google Drive
        file_metadata = {'name': os.path.basename(file_path)}
        media = MediaIoBaseUpload(io.FileIO(file_path, 'rb'), mimetype='image/jpeg')
        file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

        # Obter o link de compartilhamento
        file_id = file.get('id')
        service.permissions().create(
            fileId=file_id,
            body={'type': 'anyone', 'role': 'reader'}
        ).execute()

        link = f"https://drive.google.com/thumbnail?sz=w500&id={file_id}"
        return link
    file_dialog = ft.FilePicker(on_result=lambda result: on_file_picked(result))
    pagina.overlay.append(file_dialog)
    
    # Função executada após o arquivo ser selecionado
    def on_file_picked(result):
        if result.files:
            file_path = result.files[0].path
            link = upload_to_drive(file_path)
            global link_foto
            link_foto.value = link
            janela_recadastro.open = False
            concluir_janela.open = True
            pagina.update()

    # Função chamada ao clicar no botão
    def on_upload(evento):
        file_dialog.pick_files(allow_multiple=False)


    B_foto = ft.ElevatedButton("Inserir foto", on_click=on_upload)
    #-------------------------------------------------------------------
 
    def confirmando(evento):
        
        #-------------------------------------
        #Definir Campos de preenchimento Obrigatório 
        #-------------------------------------

        SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
        SPREADSHEET_ID = "197dGyWjtAVUVR2K8eODfIxfrEFgeErTcxMhp3OIX8N0"
        RANGE_NAME = "Dados!A1:AY3000"

        creds = None

        if os.path.exists(cod_token):
            creds = Credentials.from_authorized_user_file(cod_token, SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(cod_cred, SCOPES)
                # Use this line instead of run_local_server
                creds = flow.run_console()
        
            with open(cod_token, "w") as token:
                token.write(creds.to_json())

        # Exemplo de chamada para adicionar dados à planilha
        try:
            # Criar um serviço para interagir com a API do Google Sheets
            service = build("sheets", "v4", credentials=creds)
            sheet = service.spreadsheets()
            
            dados = {
                "Foto": [str(link_foto.value)],
                "Nome Completo": [nomecompleto.value],
                "Matrícula": [str(matricula.value)], 
                "CPF": [str(cpf.value)], 
                "Data de Nascimento": [str(datanascimento.value)],  
                "Sexo": [str(sexo.value)],  
                "Tipo Sanguíneo": [str(tipo_sanguineo.value)],  
                "Estado Civil": [str(estado_civil.value)],  
                "Data de Casamento": [str(datacasamento.value)],  
                "Profissão": [str(profissao.value)],  
                "Naturalidade": [str(naturalidade.value)], 
                "Nacionalidade": [str(nacionalidade.value)], 
                "Rua": [str(rua.value)], 
                "Complemento": [str(complemento.value)],  
                "Bairro": [str(bairro.value)], 
                "Município": [str(municipio.value)],  
                "Estado": [str(estado.value)],  
                "CEP": [str(cep.value)],  
                "Tel. Residencial": [str(tel_residencial.value)],  
                "Tel. Celular": [str(tel_celular.value)],  
                "E-mail": [str(email.value)],  
                "Nome do Pai": [str(nome_pai.value)],  
                "Pai Membro": [str(pai_membro.value)],
                "Nome da Mãe": [str(nome_mae.value)], 
                "Mãe Membro": [str(mae_membro.value)],
                "Nome do Conjuge": [str(nome_conjuge.value)],
                "Data de Nascimento Conjuge": [str(datanascimento_conjuge.value)],
                "Conjuge Membro": [str(conjuge_membro.value)],
                "Cargo atual": [str(cargo_atual.value)],
                "Data Batismo": [str(databatismo.value)],
                "Igreja Batismo": [str(igrejabatismo.value)],
                "Data de Entrada PIB": [str(entradaPIB.value)],
                "Forma de entrada": [str(formaentrada.value)],
                "Nome do filho(a) 1": [str(nome_filho1.value)],
                "Data de Nascimento do filho(a) 1": [str(datanascimento_filho1.value)],
                "Seu filho(a) 1 é membro da PIB Pavuna?": [str(filho1_membro.value)],
                "Nome do filho(a) 2": [str(nome_filho2.value)],
                "Data de Nascimento do filho(a) 2": [str(datanascimento_filho2.value)],
                "Seu filho(a) 2 é membro da PIB Pavuna?": [str(filho2_membro.value)],
                "Nome do filho(a) 3": [str(nome_filho3.value)],
                "Data de Nascimento do filho(a) 3": [str(datanascimento_filho3.value)],
                "Seu filho(a) 3 é membro da PIB Pavuna?": [str(filho3_membro.value)],
                "Nome do filho(a) 4": [str(nome_filho4.value)],
                "Data de Nascimento do filho(a) 4": [str(datanascimento_filho4.value)],
                "Seu filho(a) 4 é membro da PIB Pavuna?": [str(filho4_membro.value)],
                "Nome do filho(a) 5": [str(nome_filho5.value)],
                "Data de Nascimento do filho(a) 5": [str(datanascimento_filho5.value)],
                "Seu filho(a) 5 é membro da PIB Pavuna?": [str(filho5_membro.value)]
            }

            # Convertendo para a lista de valores
            valores = [
                [v[0] for v in dados.values()]  # Mantém os valores como strings
            ]


            # Print the values to debug
            print("Valores a serem adicionados:", valores)

            # Append the values to the sheet
            request = sheet.values().append(
                spreadsheetId=SPREADSHEET_ID,
                range=RANGE_NAME,
                valueInputOption="RAW",
                insertDataOption="INSERT_ROWS",
                body={"values": valores},
            )
            response = request.execute()

            print(f"Dados adicionados com sucesso: {response}")

        except HttpError as error:
            print(f"An error occurred: {error}")

 
        #--------------------------------------------------
        link_foto.value = ""
        nomecompleto.value = ""
        matricula.value = ""
        cpf.value = ""
        datanascimento.value = ""
        tipo_sanguineo.value = ""
        estado_civil.value = ""
        datacasamento.value = ""
        profissao.value = ""
        naturalidade.value = ""
        nacionalidade.value = ""
        rua.value = ""
        complemento.value = ""
        bairro.value = ""
        municipio.value = ""
        estado.value = ""
        cep.value = ""
        tel_residencial.value = ""
        tel_celular.value = ""
        email.value = ""
        nome_pai.value = ""
        nome_mae.value = ""
        nome_conjuge.value = ""
        datanascimento_conjuge.value = ""
        cargo_atual.value = ""
        databatismo.value = ""
        igrejabatismo.value = ""
        entradaPIB.value = ""
        formaentrada.value = ""
        sexo.value = ""
        pai_membro.value = ""
        mae_membro.value =  ""
        conjuge_membro.value = ""
        nome_filho1.value = ""
        datanascimento_filho1.value = ""
        filho1_membro.value = ""
        nome_filho2.value = ""
        datanascimento_filho2.value = ""
        filho2_membro.value = ""
        nome_filho3.value = ""
        datanascimento_filho3.value = ""
        filho3_membro.value = ""
        nome_filho4.value = ""
        datanascimento_filho4.value = ""
        filho4_membro.value = ""
        nome_filho5.value = ""
        datanascimento_filho5.value = ""
        filho5_membro.value = ""

        pagina.update()
        janela_recadastro.open = False
        concluir_janela.open = True
        pagina.update()
    Confirmar = ft.ElevatedButton("Confirmar", on_click=confirmando)

    def autopreencher(evento):
        nome_inserido = lista_nomes.value.strip()  # Obter o valor do campo
        if (TesteCadastroPIB["Nome Completo"] == nome_inserido).any():
            indice = TesteCadastroPIB[TesteCadastroPIB["Nome Completo"] == nome_inserido].index[0]  # Obter o primeiro índice correspondente
            
            nomecompleto.value = TesteCadastroPIB["Nome Completo"].iloc[indice]
            matricula.value = TesteCadastroPIB["Matrícula"].iloc[indice]
            cpf.value = TesteCadastroPIB["CPF"].iloc[indice]
            datanascimento.value = TesteCadastroPIB["Data de Nascimento"].iloc[indice]
            tipo_sanguineo.value = TesteCadastroPIB["Tipo Sanguíneo"].iloc[indice]
            estado_civil.value = TesteCadastroPIB["Estado Civil"].iloc[indice]
            datacasamento.value = TesteCadastroPIB["Data de Casamento"].iloc[indice]
            profissao.value = TesteCadastroPIB["Profissão"].iloc[indice]
            naturalidade.value = TesteCadastroPIB["Naturalidade"].iloc[indice]
            nacionalidade.value = TesteCadastroPIB["Nacionalidade"].iloc[indice]
            rua.value = TesteCadastroPIB["Rua"].iloc[indice]
            complemento.value = TesteCadastroPIB["Complemento"].iloc[indice]
            bairro.value = TesteCadastroPIB["Bairro"].iloc[indice]
            municipio.value = TesteCadastroPIB["Cidade"].iloc[indice]
            estado.value = TesteCadastroPIB["Estado"].iloc[indice]
            cep.value = TesteCadastroPIB["CEP"].iloc[indice]
            tel_residencial.value = TesteCadastroPIB["Tel. Residencial"].iloc[indice]
            tel_celular.value = TesteCadastroPIB["Celular"].iloc[indice]
            email.value = TesteCadastroPIB["e-mail"].iloc[indice]
            nome_pai.value = TesteCadastroPIB["Nome do Pai"].iloc[indice]
            nome_mae.value = TesteCadastroPIB["Nome da Mãe"].iloc[indice]
            nome_conjuge.value = TesteCadastroPIB["Nome"].iloc[indice]
            datanascimento_conjuge.value = TesteCadastroPIB["Nascimento"].iloc[indice]
            cargo_atual.value = TesteCadastroPIB["Cargo Atual"].iloc[indice]
            databatismo.value = TesteCadastroPIB["Databatismo"].iloc[indice]
            igrejabatismo.value = TesteCadastroPIB["Igreja"].iloc[indice]
            entradaPIB.value = TesteCadastroPIB["Data Membro"].iloc[indice]
            formaentrada.value = TesteCadastroPIB["Modo"].iloc[indice]
    
            pagina.update()       
    
    # Criação da janela de recadastramento com scroll
    janela_recadastro = ft.AlertDialog(
    title=Rc,
    content=ft.Column(
        controls=[
            ft.Row(controls=[
                ft.Column(controls=[B_foto,
                    matricula, nomecompleto, cpf,
                    datanascimento, sexo, tipo_sanguineo, 
                    estado_civil, datacasamento, profissao, 
                    naturalidade, nacionalidade,rua, complemento,
                    bairro, municipio, estado, cep, tel_residencial,
                    tel_celular, email, nome_pai, pai_membro,
                    nome_mae, mae_membro, nome_conjuge,
                    datanascimento_conjuge, conjuge_membro,
                    cargo_atual, databatismo, igrejabatismo,
                    entradaPIB, formaentrada, 
                    nome_filho1, datanascimento_filho1, filho1_membro, 
                    nome_filho2, datanascimento_filho2, filho2_membro,
                    nome_filho3, datanascimento_filho3, filho3_membro,
                    nome_filho4, datanascimento_filho4, filho4_membro,
                    nome_filho5, datanascimento_filho5, filho5_membro
                ]),
            ]),
            Confirmar
        ],
        scroll=True,
        width=300  # Define uma largura específica, mas ainda assim flexível
    )
    )
    pagina.overlay.append(janela_recadastro)
    # Função para abrir a janela de recadastramento
    def Recadastro(evento):
        pagina.overlay.append(janela_recadastro)  # Atribui a janela à página
        janela_recadastro.open = True  # Abre a janela
        pagina.update()  # Atualiza a página

    Iniciar_cadastro = ft.ElevatedButton("Cadastro", on_click=Recadastro)
    Completar = ft.ElevatedButton("Autopreenchimento", on_click=autopreencher)

    # LOGIN
    def Verificar(evento):
        if Nome_usuario.value in Usuarios:
            if Senha.value in Senhas:
                if Senhas.index(Senha.value) == Usuarios.index(Nome_usuario.value):
                    Nome_usuario.value = ""
                    Senha.value = ""
                    pagina.remove(Rc)
                    pagina.remove(botao_iniciar)
                    janela.open = False
                    pagina.add(lista_nomes)
                    pagina.add(sugestoes)
                    pagina.add(Completar)
                    pagina.add(Iniciar_cadastro)
                    
                    pagina.update()
                else:
                    Senha.value = "Senha Inválida"
                    pagina.update()                 
            else:
                Senha.value = "Senha Inválida"
                pagina.update()
        else:
            Nome_usuario.value = "Usuário Inválido"
            Senha.value = ""
            pagina.update()
#------------------------------------------------------------
#Janela confirmação de cadastro feito

    def fechar_ok(evento):
            concluir_janela.open = False
            pagina.update()

    titulo_concluir = ft.Text("Carregamento concluído")
    ok = ft.ElevatedButton("OK", on_click=fechar_ok)

    concluir_janela = ft.AlertDialog(
        title = titulo_concluir,
        actions=[ok]
    )
    pagina.overlay.append(concluir_janela)

#------------------------------------------------------------
#Janela Login
    titulo_janela = ft.Text("Bem-vindo ao sistema de Recadastramento")
    Nome_usuario = ft.TextField(label="Usuário")
    Senha = ft.TextField(label="Senha")
    botao_entrar = ft.ElevatedButton("Acessar Sistema", on_click=Verificar)

    janela = ft.AlertDialog(
        title=titulo_janela,
        content=ft.Column(controls=[Nome_usuario, Senha]),
        actions=[botao_entrar]
    )
    
    # Função para abrir a janela de login
    def Abrir_popup(evento):
        pagina.overlay.append(janela)
        janela.open = True
        pagina.update()   

    
    botao_iniciar = ft.ElevatedButton("Login", on_click=Abrir_popup)
    pagina.add(Rc)
    pagina.add(botao_iniciar)

    # Função para verificar e modificar os valores vazios, interrompendo o processo

ft.app(main)
