
import streamlit as st
from notebook import Notebook

#crea 5 tab che organizzano l'app in 5 sezioni diverse
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Show Notes", "Create Note",
"Search Notes", "Delete Note", "Modify Note"])

if "book" not in st.session_state:
    st.session_state["book"] = Notebook()

#creaimo nella tab2, una box vuota dove l'utente inserisce la memo
with tab2:
    with st.form('Create Note'):
        memo = st.text_input("Write a memo for your note:", key="memo")
        submitted1 = st.form_submit_button('Add')
    if submitted1:
        st.session_state["book"].new_note(memo)

with tab3:
    with st.form('Search Notes'):
        filter = st.text_input("Search for:", key="filter")
        submitted2 = st.form_submit_button('Search')
    if submitted2:
        notes = st.session_state["book"].search(filter)
        for note in notes:
            st.write("{0}: {1}\n{2}".format(note.id, note.tags, note.memo))

with tab4:
    with st.form('Select Note'):
        id = st.text_input("Note ID:", key="id")
        submitted3 = st.form_submit_button('Delete')
    if submitted3:
        if st.session_state["book"].delete_note(int(id)) != None:
            st.write("CANCELLED NOTE: {0}".format(id))
        else:
            st.write("Note {0} does not exist".format(id))

with tab5:
    with st.form("Update Note"):
        idm = st.text_input("Note ID:", key="idm")
        memou = st.text_input("Write a new memo:", key="memou")
        tags = st.text_input("Write comma-separated tags:", key="tags")
        submitted5 = st.form_submit_button('Update')
    if submitted5:
        st.session_state["book"].modify_memo(int(idm), memou)
        st.session_state["book"].modify_tags(int(idm), tags)

with tab1:
    notes = st.session_state["book"].notes
    for note in notes:
        st.write("{0}: {1}\n{2}".format(note.id, note.tags, note.memo))    