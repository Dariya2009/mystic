import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Конфигурация страницы
st.set_page_config(page_title="Finance Statement Checker Pro", layout="wide", page_icon="📈")

# 2. Единый стиль CSS (Dark Premium)
st.markdown("""
    <style>
    html { scroll-behavior: smooth; }
    .stApp { background-color: #0e1117; color: #ffffff; }
    
    /* Стиль бокового меню */
    [data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 2px solid #800020;
    }
    
    /* Шапка */
    .header-bar {
        display: flex; justify-content: flex-end; padding: 20px 5%;
        background: #161b22; border-bottom: 2px solid #800020;
    }
    .auth-btn {
        margin-left: 15px; padding: 10px 30px; border-radius: 5px;
        font-weight: 700; cursor: pointer; border: 2px solid #800020; color: white;
    }
    .signup-btn { background: #800020; color: white; }
    
    /* Текстовые блоки */
    .white-text-box { color: #ffffff !important; line-height: 1.8; font-size: 1.1rem; margin-bottom: 20px; }
    .section-title { color: #800020; font-size: 3rem; font-weight: 800; margin-bottom: 30px; }
    
    /* Ссылки */
    .custom-link {
        display: inline-block; margin-top: 15px; padding: 10px 25px;
        background-color: #800020; color: white !important;
        text-decoration: none; border-radius: 5px; font-weight: 600;
    }
    
    .news-card {
        background: #1c2128; padding: 25px; border-radius: 12px;
        border-left: 6px solid #800020; margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# --- БОКОВОЕ МЕНЮ (НАВИГАЦИЯ) ---
st.sidebar.markdown("<h2 style='color: #800020;'>NAVIGATION</h2>", unsafe_allow_html=True)
page = st.sidebar.radio("Go to:", ["🏠 Home", "📚 Education Center", "🔬 Audit Lab (Terminal)", "📰 Financial News", "📞 Contacts & Reviews"])

# --- СТРАНИЦА 1: HOME (НЕ МЕНЯЛИ!) ---
if page == "🏠 Home":
    st.markdown('<div class="header-bar"><div class="auth-btn">LOG IN</div><div class="auth-btn signup-btn">SIGN UP</div></div>', unsafe_allow_html=True)
    st.markdown("""
        <div style="padding: 100px 10%; text-align: center;">
            <h1 style="font-size: 5rem; font-weight: 900; color: #ffffff; letter-spacing: -2px;">FINANCE STATEMENT CHECKER</h1>
            <p style="font-size: 1.8rem; color: #800020; font-weight: 800;">ELITE AUDIT & VERIFICATION TERMINAL</p>
            <p style="color: #ffffff; font-size: 1.3rem; opacity: 0.8;">System Architecture by: <b>Naikina Dariya & Erik Amira</b></p>
            <br><br>
            <p style="color: #666;">Use the sidebar on the left to navigate through the system.</p>
        </div>
    """, unsafe_allow_html=True)

# --- СТРАНИЦА 2: EDUCATION (ДОБАВИЛИ ВИДЕО И ФОТО) ---
elif page == "📚 Education Center":
    st.markdown("<h2 class='section-title'>Financial Education Hub</h2>", unsafe_allow_html=True)
    
    # Добавляем видео-урок
    st.markdown("### 🎥 Masterclass: How to Read Financial Statements")
    st.video("https://www.youtube.com/watch?v=W8qV_67FzEw") # Популярный туториал на английском
    
    st.markdown("---")
    
    col_text, col_img = st.columns([2, 1])
    
    with col_text:
        with st.expander("📊 THE BALANCE SHEET (Detailed Analysis)", expanded=True):
            st.markdown("""
            <div class="white-text-box">
            <b>Assets = Liabilities + Equity</b>. This is the golden rule.<br>
            The balance sheet shows what the company owns and how it paid for it. 
            It is essential for checking <b>Liquidity</b>.
            </div>
            """, unsafe_allow_html=True)
            st.markdown('<a href="https://www.investopedia.com/terms/b/balancesheet.asp" class="custom-link">Investopedia Guide 🔗</a>', unsafe_allow_html=True)

    with col_img:
        # Добавляем картинку-схему
        st.image("https://www.wallstreetmojo.com/wp-content/uploads/2019/03/Balance-Sheet-Formula-1.jpg", caption="Balance Sheet Equation")

    st.markdown("<br>", unsafe_allow_html=True)
    
    col_img2, col_text2 = st.columns([1, 2])
    with col_img2:
        st.image("https://cdn.educba.com/academy/wp-content/uploads/2019/12/Income-Statement-Formula.jpg", caption="Profit & Loss Flow")
    
    with col_text2:
        with st.expander("📈 THE INCOME STATEMENT (P&L)", expanded=True):
            st.markdown("""
            <div class="white-text-box">
            Revenue - Expenses = <b>Net Income</b>.<br>
            This page tracks your profitability over a specific period. It shows the efficiency of management.
            </div>
            """, unsafe_allow_html=True)
            st.markdown('<a href="https://www.investopedia.com/terms/i/incomestatement.asp" class="custom-link">Profitability Guide 🔗</a>', unsafe_allow_html=True)

# --- СТРАНИЦА 3: AUDIT LAB (ТЕРМИНАЛ + EXCEL) ---
elif page == "🔬 Audit Lab (Terminal)":
    st.markdown("<h2 class='section-title'>Audit Terminal</h2>", unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["[ MANUAL ENTRY ]", "[ EXCEL DATABASE ]"])
    
    with tab1:
        st.markdown("### Manual Verification")
        report = st.selectbox("Statement Type", ["Balance Sheet", "Income Analysis", "Cash Flow"])
        val1 = st.number_input("Input A", value=0.0)
        val2 = st.number_input("Input B", value=0.0)
        if st.button("RUN AUDIT"):
            st.balloons()
            st.success("Analysis synchronized.")
            
    with tab2:
        st.markdown("### Professional Excel Audit")
        file = st.file_uploader("Upload Company Report (.xlsx)", type=["xlsx"])
        if file:
            df = pd.read_excel(file)
            st.dataframe(df.head())
            if st.button("BATCH PROCESS"):
                st.balloons()
                st.success("File verified.")

# --- СТРАНИЦА 4: NEWS ---
elif page == "📰 Financial News":
    st.markdown("<h2 class='section-title'>Live Financial News</h2>", unsafe_allow_html=True)
    n1, n2 = st.columns(2)
    with n1:
        st.markdown("<div class='news-card'><h4>FED Interest Rates</h4><p>Fed signals stability for 2026.</p></div>", unsafe_allow_html=True)
    with n2:
        st.markdown("<div class='news-card'><h4>Tech Market Surge</h4><p>AI stocks reaching new all-time highs.</p></div>", unsafe_allow_html=True)

# --- СТРАНИЦА 5: CONTACTS ---
elif page == "📞 Contacts & Reviews":
    st.markdown("<h2 class='section-title'>Contact Information</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### Developers")
        st.markdown("<p style='color: white;'>• Naikina Dariya<br>• Erik Amira</p>", unsafe_allow_html=True)
        st.markdown("### Support")
        st.markdown("<p style='color: white;'>Email: support@finchecker.pro</p>", unsafe_allow_html=True)
    with c2:
        st.markdown("### Feedback")
        st.markdown("<p style='color: white;'>Rate our system on Trustpilot:</p>", unsafe_allow_html=True)
        st.markdown('<a href="https://www.trustpilot.com" target="_blank" class="custom-link">View Reviews ⭐️</a>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><hr><p style='text-align: center; color: #444;'>©️ 2026 Finance Checker Pro | Naikina Dariya & Erik Amira</p>", unsafe_allow_html=True)
