from templates.manterclienteUI import ManterClienteUI
from templates.manterServicosUI import ManterServicosUI
from templates.manterhorarioUI import ManterHorarioUI
from templates.manterProfissionalUI import ManterProfissionalUI
from templates.abrircontaUI import AbrirContaUI
from templates.loginUI import LoginUI
from templates.perfilUI import PerfilUI
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
        op = st.sidebar.selectbox("Menu", ["Meus Dados"]) #verificar no atualizar e inserir se o e-mail é semelhane ao de outro cliente
        if op == "Meus Dados": PerfilUI.Cliente()

    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ["Meus Dados"], ["Cadastrar horário"])
        if op == "Meus Dados": PerfilUI.Profissional()
        if op == "Cadastro de Horários": PerfilUI.cadastro_horarios_profissional()

    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            #profissional = st.session_state["usuario_email"][-4:] == "PFSN"
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
            del st.session_state["usuario_email"]
            del st.session_state["usuario_tipo"]
            st.rerun()

IndexUI.main()