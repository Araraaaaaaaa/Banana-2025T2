import streamlit as st
import pandas as pd
import time
from datetime import datetime
from views import View

'''____________________________________________________________________________________________________'''
class ManterHorarioUI:
    def main():
        st.title("Cadastro de Horários")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterHorarioUI.listar()
        with tab2: ManterHorarioUI.inserir()
        with tab3: ManterHorarioUI.atualizar()
        with tab4: ManterHorarioUI.excluir()

    def listar():
        horarios = View.horario_listar()
        if len(horarios) == 0: st.write("Nenhum horário cadastrado")

        else:
            dic = []
            for obj in horarios:
                cliente = View.cliente_listar_id(obj.get_id_cliente())
                servico = View.servico_listar_id(obj.get_id_servico())
                profissio = View.profissional_listar_id(obj.get_id_profissional())
                if cliente != None: cliente = cliente.get_nome()
                if servico != None: servico = servico.get_descricao()
                if profissio != None: profissio = profissio.get_nome()
                dic.append({"data" : obj.get_data(),"confirmado" : obj.get_confirmado(), "cliente" : cliente,"serviço" : servico, "profissional" : profissio})
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        clientes= View.cliente_listar()
        servicos= View.servico_listar()
        profissionais= View.profissional_listar()
        data = st.text_input("Informe a data e horário do serviço", datetime.now().strftime("%d/%m/%Y %H:%M"))
        confirmado= st.checkbox("Confirmado")
        cliente = st.selectbox("Informe o cliente", clientes, index=None)
        servico = st.selectbox("Informe o serviço", servicos, index=None)
        profissio = st.selectbox("Informe o profissional", profissionais, index=None)
        if st.button("Inserir"):
            if profissio is None:
                st.error("Você deve selecionar um profissional")
                return 
            if not profissionais:  
                st.error("Nenhum profissional cadastrado")
                return
            id_cliente = cliente.get_id() if cliente else None
            id_servico = servico.get_id() if servico else None
            id_profissio = profissio.get_id()
            View.horario_inserir(
                datetime.strptime(data, "%d/%m/%Y %H:%M"), confirmado, id_cliente, id_servico, id_profissio)
            st.success("Horário inserido com sucesso")

    def atualizar():
        horarios = View.horario_listar()
        if len(horarios) == 0: st.write("Nenhum horário cadastrado")
        else:
            clientes = View.cliente_listar()
            servicos= View.servico_listar()
            profissionais = View.profissional_listar()
            op = st.selectbox("Atualização de Horários", horarios)
            data = st.text_input("Informe a nova data e horário do serviço", op.get_data().strftime("%d/%m/%Y %H:%M"))
            confirmado = st.checkbox("Nova confirmação", op.get_confirmado())
            id_cliente = None if op.get_id_cliente() in [0, None] else op.get_id_cliente()
            id_servico = None if op.get_id_servico() in [0, None] else op.get_id_servico()
            id_profissio = None if op.get_id_profissional() in [0, None] else op.get_id_profissional()
            cliente = st.selectbox("Informe o novo cliente", clientes, next((i for i, c in enumerate(clientes) if c.get_id() == id_cliente), None))
            servico = st.selectbox("Informe o novo serviço", servicos, next((i for i, s in enumerate(servicos) if s.get_id() == id_servico), None))
            profissio = st.selectbox("Informe o novo profissional", profissionais, next((i for i, d in enumerate(profissionais) if d.get_id() == id_profissio), None))
            if st.button("Atualizar"):
                if not profissionais:  # lista vazia
                    st.error("Nenhum profissional cadastrado")
                    return
                if profissio is None:
                    st.error("Você deve selecionar um profissional")
                    return 
                id_cliente = None
                id_servico = None
                id_profissio = None
                if cliente != None: id_cliente = cliente.get_id()
                if servico != None: id_servico = servico.get_id()
                if profissio != None: id_profissio = profissio.get_id()
                View.horario_atualizar(op.get_id(), datetime.strptime(data,"%d/%m/%Y %H:%M"), confirmado, id_cliente, id_servico, id_profissio)
                st.success("Horário atualizado com sucesso")
                st.rerun()

    def excluir():
        horarios = View.horario_listar()
        if len(horarios) == 0: st.write("Nenhum horário cadastrado")
        else:
            op = st.selectbox("Exclusão de Horários", horarios)
            if st.button("Excluir"):
                View.horario_excluir(op.get_id())
                st.success("Horário excluído com sucesso")
                time.sleep(2)
                st.rerun()