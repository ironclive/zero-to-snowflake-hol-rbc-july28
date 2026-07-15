import streamlit as st

def setup_page(title, icon="❄️"):
    st.set_page_config(page_title=title, page_icon=icon, layout="wide")
    st.logo("https://upload.wikimedia.org/wikipedia/commons/f/ff/Snowflake_Logo.svg")
    st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #F0F4F8;
        }
        [data-testid="stSidebarNavLink"] span {
            color: #1B2A4A !important;
            font-size: 0.95rem;
        }
        [data-testid="stSidebarNavLink"][aria-current="page"] {
            background-color: #E2E8F0 !important;
            border-radius: 6px;
        }
        [data-testid="stSidebarNavItems"] li:first-child [data-testid="stSidebarNavLink"] span::before {
            content: "🏠 ";
        }
    </style>
    """, unsafe_allow_html=True)
