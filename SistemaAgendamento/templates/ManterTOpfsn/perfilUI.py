import streamlit as st
from datetime import datetime, timedelta
import pandas as pd
from views import View
import time

class ProfissionalUI:
    def main():
        st.title("Profissional")
        tab1, tab2, tab3, tab4 = st.tabs(["Perfil", "Abrir Agenda", "Ver Serviços", "Confirmar Serviço"])
        with tab1: ProfissionalUI.perfil()
        with tab2: ProfissionalUI.abrir()
        with tab3: ProfissionalUI.visualizar()
        with tab4: ProfissionalUI.confirmar_servico()

    def perfil():
        op = View.profissional_listar_id(st.session_state["usuario_id"])
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
            id = op.get_id()
            View.profissional_atualizar(id, nome, especialidade, conselho, email, senha)
            st.success("Profissional atualizado com sucesso")
            time.sleep(2)
            st.rerun()

    def abrir(): #Visão do profissional
        data = st.text_input("Informe a data no formato dd/mm/aaaa", datetime.now().strftime("%d/%m/%Y"))
        horarioI = st.text_input("Informe o horário inicial no formato HH:MM")
        horarioF = st.text_input("Informe o horário final no formato HH:MM")
        intervalo = st.text_input("Informe o intervalo entre os horários (min)", "30")
        if st.button("Abrir Agenda"):
            horarioI = datetime.strptime(horarioI, "%H:%M")
            horarioF = datetime.strptime(horarioF, "%H:%M")
            data = datetime.strptime(data, "%d/%m/%Y")
            if horarioF < horarioI: #horario final menor que horario inicial
                st.error("Horário final inválido 1")
                return
            if datetime.combine(data.date(), horarioF.time()) < datetime.now():#horario final no passado
                st.error("Horário final inválido 2")
            for i in range(200): #esta criando os vários horários
                variante = horarioI + timedelta(minutes= (i * int(intervalo)))
                if variante >= horarioF: break
                View.horario_inserir(datetime.combine(data.date(), variante.time()), False, None, None, st.session_state["usuario_id"])
            st.success("Horário(s) inserido(s) com sucesso!")
            time.sleep(2)
            st.rerun()

    def visualizar():
        horarios = View.horario_listar_id_profissional(st.session_state["usuario_id"]) #esse id tem acesso a informações do profissional.json
        if len(horarios) == 0: st.write("Nenhum horário cadastrado")
        else:
            list_dic = []
            for obj in horarios: list_dic.append(obj.to_df()) #coloca de um jeito que a senha não seja mostrada no dataframe
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    
    def confirmar_servico(): 
        horarios = View.horario_listar_id_profissional(st.session_state["usuario_id"]) #confirma apenas os horários dele
        if len(horarios) == 0: st.write("Nenhum horário cadastrado")
        else:
            op = st.selectbox("Informe o Horário", horarios) #str(horarios)
            if st.button("Corfirmar"):
                View.horario_atualizar(op.get_id(), op.get_data(), True, op.get_id_cliente(), op.get_id_servico(), op.get_id_profissional())
                st.success("Horário confirmado com sucesso")
                time.sleep(2)
                st.rerun()
           