import streamlit as st
import pandas as pd
import time
from views import View

'''____________________________________________________________________________________________________'''
class ManterProfissionalUI:
    def main():
        st.title("Cadastro de profissional")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProfissionalUI.listar()
        with tab2: ManterProfissionalUI.inserir()
        with tab3: ManterProfissionalUI.atualizar()
        with tab4: ManterProfissionalUI.excluir()

    def listar():
        profissio = View.profissional_listar()
        if len(profissio) == 0: st.write("Nenhum profissional cadastrado")
        else:
            list_dic = []
            for obj in profissio: list_dic.append(obj.to_df())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o nome")
        especialidade = st.text_input("Informe a especialidade")
        conselho = st.text_input("Informe o conselho")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha")
        if st.button("Inserir"):
            if View.email_duplicado_profissional(email):
                st.error("Conta profissional já existente")
                return
            if View.usuario_nunca_admin(nome):
                st.error("Nome inválido")
                return
            if View.usuario_nunca_admin(email):
                st.error("Email inválido")
                return
            View.profissional_inserir(nome, especialidade, conselho, email, senha)
            st.success("Profissional inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        profissio = View.profissional_listar()
        if len(profissio) == 0: st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Atualização de profissionais", profissio)
            nome = st.text_input("Novo nome", op.get_nome())
            especialidade = st.text_input("Nova especialidade", op.get_especialidade())
            conselho = st.text_input("Novo conselho", op.get_conselho())
            email = st.text_input("Novo e-mail", op.get_email())
            senha = st.text_input("Nova senha", op.get_senha(), type="password")
            if st.button("Atualizar"):
                if not op.get_email() == email: # se o email foi alterado
                    if View.email_duplicado_profissional(email):
                        st.error("Conta profissional já existente")
                        return
                    if View.usuario_nunca_admin(email):
                        st.error("Email inválido")
                        return
                if View.usuario_nunca_admin(nome):
                    st.error("Nome inválido")
                    return
                id = op.get_id()
                View.profissional_atualizar(id, nome, especialidade, conselho, email, senha)
                st.success("Profissional atualizado com sucesso")

    def excluir():
        profissio = View.profissional_listar()
        if len(profissio) == 0: st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Exclusão de profissionais", profissio)
            if st.button("Excluir"): 
                if len(View.horario_listar_id_profissional(op.get_id())) != 0:
                    st.error("Profissional com agendamento")
                    return
                id = op.get_id()
                View.profissional_excluir(id)
                st.success("Profissional excluído com sucesso")
