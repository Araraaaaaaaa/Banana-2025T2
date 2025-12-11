from View import views
from TEMPLATE.ManterAdmin import mainAdmin
from TEMPLATE.ManterUsuario import mainUsuario
from TEMPLATE.visita import entrarSistema, abrirConta
import streamlit as st
import pandas as pd
import time as tm

class nav:
    def menu_visitante():
        opassp = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        views.criar_admin()
        if op == "Entrar no Sistema": entrarSistema.main()
        if op == "Abrir Conta": abrirConta.main()

    def menu_usuario():
        op = st.sidebar.selectbox("Menu", ["Perfil", "Pesquisar Livros", "Biblioteca", "Solicitações", "Meus exemplares" ])
        if op == "Perfil": mainUsuario.perfil()
        if op == "Pesquisar Livros": mainUsuario.pesquisar()
        if op == "Biblioteca": mainUsuario.biblioteca()
        if op == "Solicitações": mainUsuario.solicitacoes()

    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Perfil", "Usuarios", "Livros"])
        if op == "Perfil": mainAdmin.perfil()
        if op == "Usuarios": mainAdmin.usuarios()
        if op == "Livros": mainAdmin.livros()

    def sidebar():
        if "usuario_id" not in st.session_state:
            nav.menu_visitante()
        else:
            admin = st.session_state["usuario_username"] == "admin"

            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_username"])

            if admin: nav.menu_admin()
            else: nav.menu_usuario()
            nav.sair_do_sistema()
    
    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_email"]
            del st.session_state["usuario_username"]
            st.rerun()