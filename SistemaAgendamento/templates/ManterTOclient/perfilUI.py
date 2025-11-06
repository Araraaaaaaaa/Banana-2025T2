import streamlit as st
from views import View
import pandas as pd
import time

class ClienteUI:
    def main():
        st.title("Painel Cliente")
        tab1, tab2, tab3, tab4 = st.tabs(["Perfil", "Agendar Serviço", "Ver Serviços", "Ver Receitas"])
        with tab1: ClienteUI.perfil()
        with tab2: ClienteUI.agendar()
        with tab3: ClienteUI.visualizar()
        with tab4: ClienteUI.receitas()

    def perfil():
        op = View.cliente_listar_id(st.session_state["usuario_id"])
        nome = st.text_input("Informe o novo nome", op.get_nome())
        email = st.text_input("Informe o novo e-mail", op.get_email())
        fone = st.text_input("Informe o novo fone", op.get_fone())
        senha = st.text_input("Informe a nova senha", op.get_senha(), type="password")
        if st.button("Atualizar"):
            if not op.get_email() == email: # se o email foi alterado
                if View.email_duplicado_cliente(email):
                    st.error("Conta cliente já existente")
                    return
                if View.usuario_nunca_admin(nome):
                    st.error("Nome inválido")
                    return
            id = op.get_id()
            View.cliente_atualizar(id, nome, email, fone, senha)
            st.success("Cliente atualizado com sucesso")
    
    def agendar():
        profs = View.profissional_listar()
        if len(profs) == 0: st.write("Nenhum profissional cadastrado")
        else:
            profissional = st.selectbox("Informe o profissional", profs)
            horarios = View.horario_agendar_horario(profissional.get_id())
            if len(horarios) == 0: st.write("Nenhum horário disponível")
            else:
                servicos = View.servico_listar()
                if len(servicos) == 0: st.write("Nenhum serviço disponível")
                else:
                    horario = st.selectbox("Informe o horário", horarios)
                    servico = st.selectbox("Informe o serviço", servicos)
                    if st.button("Agendar"):
                        View.horario_atualizar(horario.get_id(), horario.get_data(), False, st.session_state["usuario_id"],servico.get_id(), profissional.get_id())
                        st.success("Horário agendado com sucesso")
                        time.sleep(2)
                        st.rerun()
    
    def visualizar():
        horar = View.horario_listar_id_cliente(st.session_state["usuario_id"]) #tem o id do usuário envolvido
        if len(horar) == 0: st.write("Você não tem nenhum horário cadastrado")
        else:
            dic = []
            for obj in horar:
                servico = View.servico_listar_id(obj.get_id_servico())
                profissio = View.profissional_listar_id(obj.get_id_profissional())
                if servico != None: servico = servico.get_descricao()
                if profissio != None: profissio = profissio.get_nome()
                dic.append({"data" : obj.get_data(),"confirmado" : obj.get_confirmado(), "serviço" : servico, "profissional" : profissio})
            df = pd.DataFrame(dic)
            st.dataframe(df)
            st.rerun()

    def receitas():
        op = View.receita_listar_id_cliente(st.session_state["usuario_id"])
        if len(op) == 0: st.write("Sem receitas válidas")
        else:
            receita = st.selectbox("Escolha a receita", op)
            if st.button("Ver mais"):
                st.write(receita)
                st.write(View.medicamento_listar_id(receita.get_medicamento_id()))
                cliente = View.cliente_listar_id(st.session_state["usuario_id"])
                st.caption(cliente.get_nome())
                st.caption(View.profissional_listar_id(receita.get_profissional_id()))