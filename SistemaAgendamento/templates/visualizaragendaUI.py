import streamlit as st
from datetime import datetime, timedelta
import pandas as pd
from views import View
import time

class VisualizarAgendaUI:

    def visualizaragenda_profissional():
        st.header("Visualizar Agenda")
        horarios = View.horario_listar_id_profissional(st.session_state["usuario_id"]) #esse id tem acesso a informações do profissional.json
        if horarios == None: st.write("Nenhum horário cadastrado")
        else:
            list_dic = []
            for obj in horarios: list_dic.append(obj.to_df()) #coloca de um jeito que a senha não seja mostrada no dataframe
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
            View.horario_ministrar() #retira horários antigos
            st.rerun()