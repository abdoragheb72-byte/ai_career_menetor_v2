import streamlit as st


def apply_custom_font():
    st.markdown("""
    <style>

    /* الخط العام */
    html, body, [class*="css"]{
        font-family: "Times New Roman", Times, serif;
    }

    /* العناوين */
    h1, h2, h3, h4, h5, h6,
    .stTitle,
    [data-testid="stHeading"]{
        font-family: "Times New Roman", Times, serif !important;
        color:#0E6BA8;
        font-weight:bold;
    }

    /* الأزرار */
    .stButton > button{
        width:100%;
        border-radius:10px;
        height:45px;
        font-size:16px;
        font-weight:bold;
        background:#0E6BA8;
        color:white !important;
        border:none;
    }

    .stButton > button:hover{
        background:#0B5A8A;
        color:white !important;
    }

    /* Text Input */
    .stTextInput input{
        border-radius:8px;
    }

    /* Text Area */
    .stTextArea textarea{
        border-radius:8px;
    }

    /* Alerts */
    .stAlert{
        border-radius:10px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"]{
        background:#F4F6F8;
    }

    /* ==========================
       إصلاح لون الـ Selectbox
       ========================== */

    div[data-baseweb="select"]{
        color:black !important;
    }

    div[data-baseweb="select"] > div{
        background:white !important;
        color:black !important;
    }

    div[data-baseweb="popover"]{
        background:white !important;
    }

    div[data-baseweb="menu"]{
        background:white !important;
    }

    div[data-baseweb="menu"] ul{
        background:white !important;
    }

    div[data-baseweb="menu"] li{
        background:white !important;
        color:black !important;
    }

    div[data-baseweb="menu"] li:hover{
        background:#E6F2FF !important;
        color:black !important;
    }

    div[data-baseweb="menu"] span{
        color:black !important;
    }

    /* Hide Menu & Footer */

    #MainMenu{
        visibility:hidden;
    }

    footer{
        visibility:hidden;
    }

    </style>
    """, unsafe_allow_html=True)