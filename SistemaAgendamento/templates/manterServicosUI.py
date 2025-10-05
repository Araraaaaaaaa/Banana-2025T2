import streamlit as st
import pandas as pd
import time
from views import View
#servico já existente, valor positivo não nulo

class ManterServicosUI:

    def main():
        st.header("Cadastro de Serviços")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterServicosUI.listar()
        with tab2: ManterServicosUI.inserir()
        with tab3: ManterServicosUI.atualizar()
        with tab4: ManterServicosUI.excluir()

    def listar():
        servicos = View.servico_listar()
        if len(servicos) == 0: st.write("Nenhum serviço cadastrado")
        else:
            list_dic = []
            for obj in servicos: list_dic.append(obj.to_df())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        Descricao = st.text_input("Informe a descrição")
        Valor = st.text_input("Informe o valor")
        if st.button("Inserir"):
            View.servico_inserir(Descricao, Valor)
            st.success("Serviço inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        servicos = View.servico_listar()
        if len(servicos) == 0: st.write("Nenhum Serviço cadastrado")
        else:
            op = st.selectbox("Atualização de Serviços", servicos)
            Descricao = st.text_input("Nova descrição", op.get_descricao())
            Valor = st.text_input("Novo e-mail", op.get_valor())
            if st.button("Atualizar"):
                id = op.get_id()
                View.servico_atualizar(id, Descricao, Valor)
                st.success("Serviço atualizado com sucesso")

    def excluir():
        servicos = View.servico_listar()
        if len(servicos) == 0: st.write("Nenhum serviço cadastrado")
        else:
            op = st.selectbox("Exclusão de Serviços", servicos)
            if st.button("Excluir"): 
                id = op.get_id()
                View.servico_excluir(id)
                st.success("Serviço excluído com sucesso")