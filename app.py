import streamlit as st
from data_loader import load_data

st.set_page_config(page_title="GenBI Bot", layout="wide")

st.title("🤖 GenBI Bot: Business Insights Chatbot")
st.markdown("Upload a **CSV or Excel** file and ask questions about your business data!")

uploaded_file = st.file_uploader("Upload CSV or Excel", type=['csv', 'xls', 'xlsx'])

if uploaded_file:
    df, error = load_data(uploaded_file)
    if error:
        st.error(f"Error: {error}")
    else:
        st.success("Data loaded successfully!")
        st.dataframe(df.head())
        # next: embed + question-answering
