import streamlit as st
from views import View
import time

class PerfilUI:
    def Cliente():
        st.header("Meus Dados")
        op = View.cliente_listar_id(st.session_state["usuario_id"])
        nome = st.text_input("Informe o novo nome", op.get_nome(), key="PerfilUI.cliente.nome")
        email = st.text_input("Informe o novo e-mail", op.get_email(), key="PerfilUI.cliente.email")
        fone = st.text_input("Informe o novo fone", op.get_fone(), key="PerfilUI.cliente.fone")
        senha = st.text_input("Informe a nova senha", op.get_senha(), type="password", key="PerfilUI.cliente.senha")
        if st.button("Atualizar", key="perfilUI_cliente_atualizar"):
            if View.email_duplicado_cliente(email):
                st.error("Conta cliente já existente")
                return
            id = op.get_id()
            View.cliente_atualizar(id, nome, email, fone, senha)
            st.success("Cliente atualizado com sucesso")

    def Profissional():
        st.header("Meus Dados")
        op = View.profissional_listar_id(st.session_state["usuario_id"])
        nome = st.text_input("Novo nome", op.get_nome(), key="PerfilUI.profissional.nome")
        especialidade = st.text_input("Nova especialidade", op.get_especialidade(), key="PerfilUI.profissional.especialidade")
        conselho = st.text_input("Novo conselho", op.get_conselho(), key="PerfilUI.profissional.conselho")
        email = st.text_input("Novo e-mail", op.get_email(), key="PerfilUI.profissional.email")
        senha = st.text_input("Nova senha", op.get_senha(), type="password", key="PerfilUI.profissional.senha")
        if st.button("Atualizar", key="perfilUI_profissional_atualizar"):
            if not op.get_email() == email: # se o email foi alterado
                if View.email_duplicado_profissional(email):
                    st.error("Conta profissional já existente")
                    return
            id = op.get_id()
            View.profissional_atualizar(id, nome, especialidade, conselho, email, senha)
            st.success("Profissional atualizado com sucesso")

    def cadastro_horarios_profissional():
        pass