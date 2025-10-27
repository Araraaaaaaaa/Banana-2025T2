import streamlit as st
from views import View
import time

class AbrirContaUI:
    def main():
        st.title("Abrir Conta no Sistema")
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
            if View.usuario_nunca_admin(email): #precaução
                st.error("Email inválido")
                return
            View.cliente_inserir(nome, email, fone, senha)
            st.success("Conta criada com sucesso")
            time.sleep(2)
            st.rerun()
