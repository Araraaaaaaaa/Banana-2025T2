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
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Inserir"):
            View.cliente_inserir(nome, email, fone, senha)
            st.success("Conta criada com sucesso")
            time.sleep(2)
            st.rerun()

    def profissional():
        st.header("Abrir Conta Profissional no Sistema")
        nome = st.text_input("Informe o nome")
        especialidade = st.text_input("Informe a especialidade")
        conselho = st.text_input("Informe o conselho")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Inserir"):
            if email[-4:] == "PFSN": 
                st.error("Conta profissional inválida")
                return
            View.profissional_inserir(nome, especialidade, conselho email, senha)
            st.success("Conta criada com sucesso")
            time.sleep(2)
            st.rerun()