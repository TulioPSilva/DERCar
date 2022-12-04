import streamlit as st
from streamlit_option_menu import option_menu
import webbrowser
from PIL import Image
from streamlit_modal import Modal
import streamlit.components.v1 as components
import csv

#Definição da liguagem:
lingua = 'português'
if lingua == 'ingles':
    lg = 1
    menu = ["Home", "Real Time",  "Analyzes", 'Contact']
    titulo = 'Virtual platform for operation and planning of electric vehicles in the electrical distribution network'
if lingua == 'português':
    lg = 2
    menu = ["Inicio", "Tempo Real",  "Análises", 'Contato']
    titulo = 'Plataforma virtual para operação e planejamento de veículos elétricos na rede de distribuição elétrica'

if 'sidebar_state' not in st.session_state:
    st.session_state.sidebar_state = 'expanded'

# Set the configs
APP_TITLE = f"DERCar - {titulo}"
st.set_page_config(
    page_title=APP_TITLE,
    page_icon=Image.open("car_ve.jpg"),
    layout="wide",
    initial_sidebar_state=st.session_state.sidebar_state,
)

#Links para baixar:
url_actionnet = 'https://www.dropbox.com/s/3vd8azx9qm0nldm/Action.NET%209.1.25.1_Pt.exe?dl=0'
url_VPN = 'https://www.dropbox.com/s/3t2fvnmkfmwbp6k/openvpn-SPIN_SRV-FW001-UDP4-1196-usr.opendss-install-2.5.2-I601-amd64.exe?dl=0'
url_TRichClient = 'https://www.dropbox.com/s/ryjpmrqyidpe1h6/TRichClient.lnk?dl=0'

#Imagens:
img_arranjo_simu = Image.open("arranjo_simu.png")
img_iee8500 = Image.open("ieee8500.jpg")
img_trend_carregamento = Image.open("trand_c.jpg")
img_trend_injecao = Image.open("trand_j.jpg")
img_trend_legenda = Image.open("trend_legenda.png")
img_screen1 = Image.open("Screen1.jpg")

#Salvar dados de cadastro:
def gravar_cadastro(cad):
    f = open('cadastros.csv', 'a', newline='', encoding='utf-8')
    w = csv.writer(f)
    w.writerow(cad)
    f.close()

image_logo = Image.open("logo__car.png")
st.sidebar.image(image_logo)

with st.sidebar:
    selected = option_menu(None, menu, 
        icons=['house', 'eye', "", ''], 
        menu_icon="cast", default_index=0, orientation="vertical",
        styles={
            "container": {"padding": "0!important", "background-color": "#86f78f"},
            "icon": {"color": "white", "font-size": "25px"}, 
            "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "white"},
            "nav-link-selected": {"background-color": "green"},
        }
    )

st.title(titulo)

## MENU: INICIO (HOME):
if lg == 2:
    text11 = 'A plataforma foi desenvolvida utilizando o software SCADA ActionNET integrado à ferramenta OpenDSS.\n Para utilizar siga os seguintes passos:'
    text12 = '**1. Baixe o software SCADA ActionNET. Siga as instruções apresentadas no processo de instalação.**\
            \n_Pré-requisito: .NET framework 9.6.2 ou superior._'
    textbtn11 = 'Abra o navegador para baixar o software ActionNET'
    text13 = '**2. Baixe a VPN para conectar a nuvem da SPIN Engenharia. Siga as instruções apresentadas no processo de instalação.**'
    textbtn12 = 'Abra o navegador para baixar a VPN'
    text14 = '**3. Baixe o atalho para acesso ao sistema.**\
            \n_O software ActionNET deve ser instalado no diretório C_'
    textbtn13 = 'Abra o navegador para baixar o RichClient'

if(selected == '' or selected == menu[0]):
    st.markdown(text11)
    st.markdown(text12)

    modal = Modal("Por Favor! Realize o cadastro para baixar o software", 1, 10)
    open_modal = st.button(textbtn11)
    if open_modal:
        print(st.session_state.sidebar_state)
        st.session_state.sidebar_state = 'collapsed'
        modal.open()
        st.experimental_rerun()
    
    if modal.is_open():
        with modal.container():
            nome = st.text_input('Nome:', help='campo obrigatorio')
            email = st.text_input('Email:', help='campo obrigatorio')
            empresa = st.text_input('Empresa/Instituição:', help='campo obrigatorio')
            cargo = st.text_input('Cargo:', help='campo obrigatorio')
            cad = nome,email,empresa,cargo

            if nome == "" or email == "" or empresa == "" or cargo == "":
                value = "Verifique o dados inseridos. Todos os campos são obrigatórios"
                ok = 0
            else:
                value = "Cadastro efetuado!"
                ok = 1
            
            col1, col2 = st.columns(2)
            with col1:
                fim = st.button('Finalizar cadastro')
            with col2:
                if fim:
                    st.write(f"{value}")
            
            if ok == 1:
                gravar_cadastro(cad)
                webbrowser.open_new_tab(url_VPN)
                modal.close()

    st.markdown(text13)
    
    if st.button(textbtn12):
        webbrowser.open_new_tab(url_VPN)

    st.markdown(text14)

    if st.button(textbtn13):
        webbrowser.open_new_tab(url_TRichClient)

## MENU: Tempo Real (Real Time):
if lg == 2:
    text20 = 'Avaliação do funcionamento do sistema de distribuição através da integração de VEs nas redes elétricas'
    text21 = '**Premissa**'
    text22 = "Adoção de um modelo de negócio em condomínio, em que os veículos elétricos sejam fornecidos aos usuários por meio de alugueis. No condomínio, as estações de recarga possuem a tecnologia Vehicle-to-Grid (V2G)¹."
    text23 = "O modelo de negócio também abrange uma rede de postos de recarga, que pode ser utilizada tanto pelo usuário do serviço  como também outros motoristas de VEs. As estações dos postos possuem tecnologia G2V²."
    text24 = "_¹  VEs tanto fornecem quanto absorvem energia pela rede elétrica._\
            \n_² VEs absorvem energia pela rede elétrica._"
    text25 = "**Rede IEEE 8500**"
    text26 = "O cenário observado foi aplicado a rede IEEE 8500 barras. Os pontos de conexão podem ser observados na imagem abaixo."
    text27 = "Os dados recebidos dos postos de recarga* geraram as curvas de tendência de carga e descarga abaixo. \
            \nO condominio apresenta um limite de 50 VEs conectados ao mesmo tempo, além de possuir como criterio que o horário das 16h00 às 23h59 os veículos conectados as estações devem injetar energia a rede."
    text28 = "_* Os dados são simulados apenas como critério de apresentação._"
    text29 = "A tela abaixo apresenta a representação da operação deste sistema. As metricas em branco são os dados oriundos das estações de recarga, já as azuis são \
            valores estimados apartir do calculo de fluxo de potência (OpenDSS)."
    text210 = "O operador consegue acompanhar os carregamentos e injeções de potência na rede, e ter a pecepção de seu impacto no sistema de distribuição. \
            \n Em um cenário normativo onde o prosumidor poderá ser penalizado por alguma incontigencia que vir ao causar no sistema, uma plataforma como esta poderá \
            ser de grande valia."
    text211 = "_A tela pode ser acessada seguindo os passos apresentado na aba 'Inicio'_"

if(selected == menu[1]):
    st.markdown(text20)
    st.markdown(text21)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(text22)
        st.markdown(text23)
    with col2:
        st.image(img_arranjo_simu)

    st.markdown(text24)

    st.markdown(text25)
    st.markdown(text26)

    st.image(img_iee8500)

    st.markdown(text27)

    st.image(img_trend_legenda, width=300)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Tendência de Carregamento**")
        st.image(img_trend_carregamento)
    with col2:
        st.markdown("**Tendência de Descarregamento**")
        st.image(img_trend_injecao)

    st.markdown('')
    st.markdown(text28)

    st.markdown('')
    st.markdown(text29)
    st.markdown(text210)

    st.markdown('')
    st.image(img_screen1)

    st.markdown(text211)

## MENU: ANÁLISES:
if lg == 2:
    text30 = "EM BREVE..."


if(selected == menu[2]):
    st.markdown(text30)

 ## MENU: CONTATO:
if lg == 2:
    text40 = "EM BREVE..."

if(selected == menu[3]):
    st.markdown(text40)
