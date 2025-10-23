import streamlit as st
from views import View
import pandas as pd
import time

class AgendarServicoUI:
    def main():
        st.header("Agendar Serviço")
        profs = View.profissional_listar()
        if len(profs) == 0: st.write("Nenhum profissional cadastrado")
        else:
            profissional = st.selectbox("Informe o profissional", profs)
            horarios = View.horario_agendar_horario(profissional.get_id())
            if len(horarios) == 0: st.write("Nenhum horário disponível")
            else:
                View.horario_ministrar()
                horario = st.selectbox("Informe o horário", horarios)
                servicos = View.servico_listar()
                servico = st.selectbox("Informe o serviço", servicos)
                if st.button("Agendar"):
                    View.horario_atualizar(horario.get_id(), horario.get_data(), False, st.session_state["usuario_id"],servico.get_id(), profissional.get_id())
                    View.horario_ministrar()
                    st.success("Horário agendado com sucesso")
                    time.sleep(2)
                    st.rerun()

    def visualizar():
        st.header("Visualizar Serviço")
        horar = View.horario_listar_id_cliente(st.session_state["usuario_id"]) #tem o id do usuário envolvido
        if len(horar) == 0: st.write("Você não tem nenhum horário cadastrado")
        else:
            dic = []
            View.horario_ministrar()
            for obj in horar:
                servico = View.servico_listar_id(obj.get_id_servico())
                profissio = View.profissional_listar_id(obj.get_id_profissional())
                if servico != None: servico = servico.get_descricao()
                if profissio != None: profissio = profissio.get_nome()
                dic.append({"data" : obj.get_data(),"confirmado" : obj.get_confirmado(), "serviço" : servico, "profissional" : profissio})
            df = pd.DataFrame(dic)
            st.dataframe(df)
            st.rerun()