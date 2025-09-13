from Paciente import PPaciente
from datetime import datetime
import streamlit as st

class Paciente:
    #______--__- Estado inicial da página
    def main():
        st.header("Dados do paciente")
        Nome = st.text.input("Nome")
        Cpf = st.text.input("CPF")
        Fone = st.text.input("Fone")
        Nascimento = st.text.input("Nascimento")

        #______--__- Resposta do sistema
        if st.button("Idade"):
            objeto = PPaciente(Nome, Cpf, Fone, datetime.strptime(Nascimento, "d%/m%/Y%"))
            st.write(objeto)
            st.write(objeto.idade())