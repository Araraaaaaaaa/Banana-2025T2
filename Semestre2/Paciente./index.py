from Paciente import PPaciente
from datetime import datetime
import streamlit as st

class Paciente:
    #______--__- Estado inicial da página
    def main():
        st.header("Dados do paciente")
        Nome = st.text_input("Nome")
        Cpf = st.text_input("CPF")
        Fone = st.text_input("Fone")
        Nascimento = st.text_input("Nascimento")

        #______--__- Resposta do sistema
        if st.button("Idade"):
            objeto = PPaciente(Nome, Cpf, Fone, datetime.strptime(Nascimento, "d%/m%/Y%"))
            st.write(objeto)
            st.write(objeto.idade())
Paciente.main()