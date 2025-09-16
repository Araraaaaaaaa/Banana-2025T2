import streamlit as st
from retangulo import Retangulo


class RetanguloUI:
    def main():
        st.header("Calculos com retângulo")
        base = st.text.input("Informe a base do retângulo")
        altura = st.text.input("Informe a altura do retângulo")
        if st.button("Calcular"):
            b, a = float(base), float(altura)
            r = Retangulo(b, a)
            st.write(r)
            st.write(r.calc_area)
            st.write(r.calc_diagonal)