#Ações do administrador
from templates.ManterTOadmin.ADManter_cliente import ManterClienteUI
from templates.ManterTOadmin.ADManter_profissional import ManterProfissionalUI
from templates.ManterTOadmin.ADManter_horario import ManterHorarioUI
from templates.ManterTOadmin.ADManter_servico import ManterServicosUI
from templates.ManterTOadmin.ADManter_medicamento import ManterMedicamentosUI
#Ações do profissional
from templates.ManterTOpfsn.perfilUI import ProfissionalUI
#Ações do cliente
from templates.ManterTOclient.abrircontaUI import AbrirContaUI
from templates.ManterTOclient.perfilUI import ClienteUI
#Geral
from templates.loginUI import LoginUI
from views import View
import streamlit as st
#bug na hora de agendar um horário - lado cliente
#falta de trys - UI
#horários no passado aparecendo
class IndexUI:

    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        View.cliente_criar_admin()
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()

    def menu_cliente(): ClienteUI.main()

    def menu_profissional(): ProfissionalUI.main()

    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Serviços", "Cadastro de Horários", "Cadastro de Profissionais", "Cadastro de Medicamentos"])
        if op == "Cadastro de Profissionais": ManterProfissionalUI.main()
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Serviços": ManterServicosUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
        if op == "Cadastro de Medicamentos": ManterMedicamentosUI.main()

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
    
    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            del st.session_state["usuario_tipo"]
            st.rerun()

IndexUI.sidebar()