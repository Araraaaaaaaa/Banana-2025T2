import streamlit as st
from views import View
import time

class AbrirContaUI:
    def main():
        tab1, tab2 = st.tabs(["Cliente", "Profissional"])
        with tab1: AbrirContaUI.cliente()
        with tab2: AbrirContaUI.profissional()

    def cliente():
        st.header("Abrir Conta Cliente no Sistema")
        nome = st.text_input("Informe o nome", key="abrirUI_cliente_nome")
        email = st.text_input("Informe o e-mail", key="abrirUI_cliente_email")
        fone = st.text_input("Informe o fone", key="abrirUI_cliente_fone")
        senha = st.text_input("Informe a senha", type="password", key="abrirUI_cliente_senha")
        if st.button("Inserir", key="abrircontaUI_cliente_inserir"):
            if View.email_duplicado_cliente(email):
                st.error("Conta cliente já existente")
                return
            if View.usuario_nunca_admin(nome):
                st.error("Nome inválido")
                return
            View.cliente_inserir(nome, email, fone, senha)
            st.success("Conta criada com sucesso")
            time.sleep(2)
            st.rerun()

    def profissional():
        st.header("Abrir Conta Profissional no Sistema")
        nome = st.text_input("Informe o nome", key="abrirUI_profissional_nome")
        especialidade = st.text_input("Informe a especialidade", key="abrirUI_profissional_especialidade")
        conselho = st.text_input("Informe o conselho", key="abrirUI_profissional_conselho")
        email = st.text_input("Informe o e-mail", key="abrirUI_profissional_email")
        senha = st.text_input("Informe a senha", type="password", key="abrirUI_profissional_senha")
        if st.button("Inserir", key="abrircontaUI_profissional_inserir"):
            if View.email_duplicado_profissional(email):
                st.error("Conta profissional já existente")
                return
            if View.usuario_nunca_admin(nome):
                st.error("Nome inválido")
                return
            View.profissional_inserir(nome, especialidade, conselho, email, senha)
            st.success("Conta criada com sucesso")
            time.sleep(2)
            st.rerun()