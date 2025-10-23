import streamlit as st
from datetime import datetime, timedelta
import pandas as pd
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
            if not op.get_email() == email: # se o email foi alterado
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
            time.sleep(2)
            st.rerun()

    def abriragenda_profissional(): #não esta criando os vários horários
        st.header("Abrir Minha Agenda")
        data = st.text_input("Informe a data no formato dd/mm/aaaa", datetime.now().strftime("%d/%m/%Y"))
        horarioI = st.text_input("Informe o horário inicial no formato HH:MM")
        horarioF = st.text_input("Informe o horário final no formato HH:MM")
        intervalo = st.text_input("Informe o intervalo entre os horários (min)", "30")
        if st.button("Abrir Agenda", key="perfilUI_profissional_abriragenda"):
            #assegurar que não mostre horários antigos e não pode abrir agenda p/ horarios no passado.
            '''datetime.strptime(horarioF, "%H:%M") == datetime.now() or datetime.strptime(horarioI, "%H:%M") < datetime.now() or'''
            horarioI = datetime.strptime(horarioI, "%H:%M")
            horarioF = datetime.strptime(horarioF, "%H:%M")
            if horarioF < horarioI:
                st.error("Horário inválido")
                return
            data = datetime.strptime(data, "%d/%m/%Y")
            for i in range(200):
                variante = horarioI + timedelta(i * int(intervalo))
                if variante > horarioF: break
                View.horario_inserir(datetime.combine(data.date(), variante.time()), False, None, None, st.session_state["usuario_id"])
            st.success("Horário(s) inserido(s) com sucesso!")
            time.sleep(2)
            st.rerun()

    def visualizaragenda_profissional(): #não está mostrando todos os horários
        st.header("Visualizar Agenda")
        horarios = View.horario_listar_id_profissional(st.session_state["usuario_id"]) #esse id tem acesso a informações do profissional.json
        if horarios == None: st.write("Nenhum horário cadastrado")
        else:
            list_dic = []
            for obj in horarios: list_dic.append(obj.to_df()) #coloca de um jeito que ele não importa a senha ou que ela não seja mostrada no dataframe
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def confirmarservico_profissional(): #mostrando horarios antigos
        st.header("Visualizar Agenda")
        horarios = View.horario_listar()
        if len(horarios) == 0: st.write("Nenhum horário cadastrado")
        else:
            op = st.selectbox("Informe o Horário", horarios) #str(horarios)
            if st.button("Corfirmar"):
                View.horario_atualizar(op.get_id(), op.get_data(), True, op.get_id_cliente(), op.get_id_servico(), op.get_id_profissional())
                st.success("Horário confirmado com sucesso")
                time.sleep(2)
                st.rerun()
                '''Cliente = View.cliente_listar_id (op.get_id_cliente())#lembrando que um profissional n pode ter dois clientes para o mesmo horário
            st.write(f"Cliente")'''