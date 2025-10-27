#Ações do administrador
from templates.ManterTOadmin.ADManter_cliente import ManterClienteUI
from templates.ManterTOadmin.ADManter_profissional import ManterProfissionalUI
from templates.ManterTOadmin.ADManter_horario import ManterHorarioUI
from templates.ManterTOadmin.ADManter_servico import ManterServicosUI
#Ações do profissional
from templates.ManterTOpfsn.perfilUI import ProfissionalUI
#Ações do cliente
from templates.ManterTOclient.abrircontaUI import AbrirContaUI
from templates.ManterTOclient.perfilUI import ClienteUI
#Geral
from templates.loginUI import LoginUI
from views import View
import streamlit as st

class IndexUI:

    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Serviços", "Cadastro de Horários", "Cadastro de Profissionais"])
        if op == "Cadastro de Profissionais": ManterProfissionalUI.main()
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Serviços": ManterServicosUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()

    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados"]) 
        if op == "Meus Dados": ClienteUI.main()

    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ["Meus Dados"])
        if op == "Meus Dados": ProfissionalUI.main()

    def sidebar():
        if "usuario_id" not in st.session_state:
            #st.write(st.session_state)
            #print("OK")
            IndexUI.menu_visitante()
        else:
            admin = st.session_state["usuario_nome"] == "admin"
            cliente = st.session_state["usuario_tipo"] == "cliente"
            profi = st.session_state["usuario_tipo"] == "profissional"

            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])

            if admin: IndexUI.menu_admin()
            elif profi: IndexUI.menu_profissional()
            elif cliente: IndexUI.menu_cliente()
            IndexUI.sair_do_sistema()

    def main():
        View.cliente_criar_admin() # verifica se existe o usuário admin
        IndexUI.sidebar() # monta o sidebar
    
    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            del st.session_state["usuario_tipo"]
            st.rerun()

IndexUI.main()