import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Конфигурация страницы
st.set_page_config(page_title="Finance Statement Checker Pro", layout="wide", page_icon="📈")

# 2. Единый стиль CSS (Dark Premium с белым текстом)
st.markdown("""
    <style>
    html { scroll-behavior: smooth; }
    .stApp { background-color: #0e1117; color: #ffffff; }
    
    /* Стиль бокового меню */
    [data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 2px solid #800020;
    }
    
    /* Текстовые блоки */
    /* Принудительно делаем текст белым внутри expander и других блоков */
    .white-text-box, .stExpander p, .stMarkdown p { 
        color: #ffffff !important; 
        line-height: 1.8; 
        font-size: 1.1rem; 
        margin-bottom: 20px; 
    }
    
    .section-title { color: #800020; font-size: 3rem; font-weight: 800; margin-bottom: 30px; }
    
    /* Ссылки-кнопки */
    .custom-link {
        display: inline-block; margin-top: 15px; padding: 10px 25px;
        background-color: #800020; color: white !important;
        text-decoration: none; border-radius: 5px; font-weight: 600;
        transition: 0.3s;
    }
    .custom-link:hover { background-color: #a00028; transform: translateY(-2px); color: white !important; }
    
    /* Карточки новостей */
    .news-card {
        background: #1c2128; padding: 25px; border-radius: 12px;
        border-left: 6px solid #800020; margin-bottom: 25px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.5);
    }
    </style>
""", unsafe_allow_html=True)

# --- БОКОВОЕ МЕНЮ (НАВИГАЦИЯ) ---
st.sidebar.markdown("<h2 style='color: #800020; text-align: center;'>NAVIGATION</h2>", unsafe_allow_html=True)
st.sidebar.markdown("---")
page = st.sidebar.radio("Go to:", ["🏠 Home", "📚 Education Center", "🔬 Audit Lab (Terminal)", "📰 Financial News", "📞 Contacts & Reviews"])

# --- СТРАНИЦА 1: HOME (НЕ МЕНЯЛИ!) ---
if page == "🏠 Home":
    st.markdown("""
        <div style="padding: 100px 10%; text-align: center;">
            <h1 style="font-size: 5rem; font-weight: 900; color: #ffffff; letter-spacing: -2px; margin-bottom: 0;">FINANCE STATEMENT CHECKER</h1>
            <p style="font-size: 1.8rem; color: #800020; font-weight: 800; margin-top: 10px;">ELITE AUDIT & VERIFICATION TERMINAL</p>
            <p style="color: #ffffff; font-size: 1.3rem; opacity: 0.9;">System Architecture by: <b>Naikina Dariya & Erik Amira</b></p>
            <br><br><br>
            <p style="color: #888; font-size: 1rem; text-transform: uppercase; letter-spacing: 2px;">Use the sidebar on the left to explore the system</p>
        </div>
    """, unsafe_allow_html=True)

# --- СТРАНИЦА 2: EDUCATION (ВСЕ ТРИ ОТЧЕТА + ИИ-ВИДЕО + БЕЛЫЙ ТЕКСТ) ---
elif page == "📚 Education Center":
    st.markdown("<h2 class='section-title'>Financial Education Hub</h2>", unsafe_allow_html=True)
    
    # Добавляем ВИДЕО, СОЗДАННОЕ ИИ
    st.markdown("### 🎥 AI Masterclass: Understanding Financial Statements")
    # Это ссылка на видео, где ИИ-аватар объясняет основы
    st.video("https://www.youtube.com/watch?v=N4fXW96_Aas") 
    
    st.markdown("---")
    st.markdown("<p style='color: white; font-size: 1.2rem; margin-bottom: 30px;'>Explore the three cornerstone financial statements. Click to expand for detailed, pro-level analysis.</p>", unsafe_allow_html=True)
    
    # 1. BALANCE SHEET
    with st.expander("📊 DETAILED ANALYSIS: THE BALANCE SHEET"):
        st.markdown("""
        <div class="white-text-box">
        The <b>Balance Sheet</b> is the most critical financial statement for determining the intrinsic value of a company. It provides a detailed report of the financial position at a specific point in time, essentially showing the company’s net worth.<br><br>
        <b>The Fundamental Equilibrium:</b> Assets = Liabilities + Shareholder's Equity.<br><br>
        - <b>Current Assets:</b> Resources expected to be converted into cash within one year, such as <i>Accounts Receivable</i> and <i>Inventory</i>.<br>
        - <b>Non-Current Assets:</b> Long-term investments including <i>Property, Plant, and Equipment (PP&E)http://googleusercontent.com/generated_image_content/0
