from templates.manterclienteUI import ManterClienteUI
from templates.manterServicosUI import ManterServicosUI
from templates.manterhorarioUI import ManterHorarioUI
from templates.manterProfissionalUI import ManterProfissionalUI
import streamlit as st

class IndexUI:

    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Serviços", "Cadastro de Horários", "Cadastro de Profissionais"])
        if op == "Cadastro de Profissionais": ManterProfissionalUI.main()
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Serviços": ManterServicosUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()

    def sidebar():
        IndexUI.menu_admin()

    def main():
        IndexUI.sidebar()

IndexUI.main()