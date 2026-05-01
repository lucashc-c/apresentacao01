import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import sqlite3

tab1, tab2 = st.tabs(["Apresentação", "Comentários"])

def deletar_comentario(id_comentario):
    conn = sqlite3.connect("comentarios.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM comentarios WHERE id = ?", (id_comentario,))
    conn.commit()
    conn.close()

def salvar_comentario(texto):
    conn = sqlite3.connect("comentarios.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO comentarios (texto) VALUES (?)", (texto,))
    conn.commit()
    conn.close()

def buscar_comentarios():
    conn = sqlite3.connect("comentarios.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, texto FROM comentarios ORDER BY id DESC")
    dados = cursor.fetchall()
    conn.close()
    return dados

with tab1:
    st.title("Título slides")

#parte responsável pelos slides que vão aparecer
    with open("slides.pdf", "rb") as f:
        binary_data = f.read()
    pdf_viewer(binary_data)

with tab2:
    st.title("Comentários")
    st.write("deixe sua pergunta ou comentário aqui")
    comentario = st.text_input("Escreva seu comentário")

    if st.button("Enviar"):
        if comentario:
            salvar_comentario(comentario)
            st.rerun()

    st.divider()

    for c in buscar_comentarios():
        col1, col2 = st.columns([4, 1])

        with col1:
            st.write(c[1])

        with col2:
            if st.button("🗑️", key=c[0]):
                deletar_comentario(c[0])
                st.rerun()



