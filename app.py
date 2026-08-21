import streamlit as st
import database as db

db.criar_tabela_mecanico()

st.title("Mecânica", text_alignment="center")

with st.form("Cadastro_Mecânico"):
    pega_cpf = st.text_input("Insira um CPF:")
    pega_nome = st.text_input("Insira um Nome:")

    btn_mecanico = st.form_submit_button ("Enviar")

if btn_mecanico:
    msg = db.cadastar_mecanico(pega_cpf , pega_nome)
    st.warning(msg)


with st.form("Deletar_Mecânico"):
    pega_cpf = st.text_input("Insira um CPF:")

    btn_delet = st.form_submit_button("Deletar")

if btn_delet:
    msg = db.deletar_mecanico(pega_cpf)
    st.warning(msg)
