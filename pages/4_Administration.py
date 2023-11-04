import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import os
import shutil

if 'review' not in st.session_state:
    st.session_state.review = None

if 'rename' not in st.session_state:
    st.session_state.rename = None
st.set_page_config(page_title = "Administration" ,initial_sidebar_state='collapsed', page_icon="🗃️", layout="wide")
st.markdown("# Administration")

def clear_files(folder_path):
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)


if st.session_state.review and st.session_state.rename is not None:
    st.info('Step 4 : Rename files PDF & Clear ', icon="ℹ️")

    #st.write(f"{st.session_state.rename}")

    folder_path1 = st.session_state.folder_path1.upper()
    folder_path2 = st.session_state.folder_path2.upper()
    folder_path3 = st.session_state.folder_path3.upper()
    #st.write(f"{st.session_state.folder_path1}")

    rename = st.session_state.rename
    columns = st.columns (8)
    clear_file = columns[3].button('Clear files', key='clear_file', help='Clear files in folder', disabled=False)
    rename_pdf = columns[4].button('Rename PDF', key='rename_pdf',help='Rename PDF files')
    st.write(folder_path1)
    if 'rename_pdf' not in st.session_state:
        st.session_state.rename_pdf = False
        st.rerun()

    if rename_pdf:
        st.session_state.initialization = None
        st.session_state.extraction = True
        st.session_state.review = True
        st.session_state.administration = True

        pdf_files = [filename for filename in os.listdir(folder_path1) if filename.endswith('.PDF')]
        if len(pdf_files) != len(rename['drawing no.']):
            st.error("Files PDF in folder not equal.")
        else:
            try:
                for i, filename in enumerate(pdf_files):
                    old_path = os.path.join(folder_path1, filename)
                    new_name = os.path.join(folder_path1, rename['drawing no.'][i] + ".PDF")
                    os.rename(old_path, new_name)
                st.success("PDFs have been renamed!")
            except Exception as e:
                st.error(f"Error : {str(e)}")

    if 'clear_file' not in st.session_state:
        st.session_state.clear_file = False
        st.rerun()

    if clear_file:
        clear_files(folder_path2)
        clear_files(folder_path3)
        st.session_state.drive_letter = None
        st.session_state.folder_name = None
        st.session_state.folder_path1 = None
        st.session_state.folder_path2 = None
        st.session_state.folder_path3 = None
        st.session_state.folder_path4 = None
        st.session_state.initialization = None
        st.session_state.extraction = None
        st.session_state.review = None
        st.session_state.administration = True
        st.session_state.rename = None
        st.session_state.edited_df = None
        switch_page("Initialization")
        st.session_state.clear_file = True
        st.rerun()

else:
    st.error("Please click button 'Next step' on review page", icon="🚨")


