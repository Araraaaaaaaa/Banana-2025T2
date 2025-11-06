import streamlit as st
import pandas as pd
import time
from views import View

class ManterMedicamentosUI:
    def main():
        st.title("Cadastro de profissional")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterMedicamentosUI.listar()
        with tab2: ManterMedicamentosUI.inserir()
        with tab3: ManterMedicamentosUI.atualizar()
        with tab4: ManterMedicamentosUI.excluir()
        
    def listar():
        medi = View.medicamento_listar()
        if len(medi) == 0: st.write("Nenhum medicamento cadastrado")
        else:
            list_dic = []
            for obj in medi: list_dic.append(obj.to_df())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o nome-fantasia")
        objetivo = st.text_input("Informe quais os objetivos do remédio")
        aplicacao = st.selectbox("Informe a forma de aplicação", ["oral", "intravenosa", "intramuscular", "subcutânea", "inalatória", "tópica", "mucosa "]) # selecionar itens pré definidos
        if st.button("Inserir"):
            View.medicamento_inserir(nome, objetivo, aplicacao)
            st.success("Medicamento inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        medi = View.medicamento_listar()
        if len(medi) == 0: st.write("Nenhum medicamento cadastrado")
        else:
            op = st.selectbox("Atualização de medicamentos", medi)
            nome = st.text_input("Informe o novo nome-fantasia", op.get_nome())
            objetivo = st.text_input("Informe quais os novos objetivos do remédio", op.get_objetivo)
            aplicacao = st.selectbox("Informe a nova forma de aplicação", ["oral", "intravenosa", "intramuscular", "subcutânea", "inalatória", "tópica", "mucosa "]) # selecionar itens pré definidos
            if st.button("Atualizar"):
                id = op.get_id()
                View.medicamento_atualizar(id, nome, objetivo, aplicacao)
                st.success("Medicamento atualizado com sucesso")

    def excluir():
        medi = View.medicamento_listar()
        if len(medi) == 0: st.write("Nenhum medicamento cadastrado")
        else:
            op = st.selectbox("Exclusão de medicamentos", medi)
            if st.button("Excluir"): 
                id = op.get_id()
                View.medicamento_excluir(id)
                st.success("Medicamento excluído com sucesso")