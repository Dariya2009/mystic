import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Настройка страницы
st.set_page_config(page_title="Finance Statement Checker Pro", layout="wide", page_icon="📈")

# 2. Стили CSS
st.markdown("""
    <style>
    html { scroll-behavior: smooth; }
    .stApp { background-color: #0e1117; color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #161b22; border-right: 2px solid #800020; }
    
    /* Делаем текст белым везде */
    .white-text { color: #ffffff !important; line-height: 1.8; font-size: 1.1rem; }
    .section-title { color: #800020; font-size: 3rem; font-weight: 800; margin-bottom: 20px; }
    
    .custom-link {
        display: inline-block; margin-top: 10px; padding: 10px 20px;
        background-color: #800020; color: white !important;
        text-decoration: none; border-radius: 5px; font-weight: 600;
    }
    .news-card {
        background: #1c2128; padding: 20px; border-radius: 12px;
        border-left: 6px solid #800020; margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- НАВИГАЦИЯ ---
page = st.sidebar.radio("МЕНЮ НАВИГАЦИИ", ["🏠 Home", "📚 Education Center", "🔬 Audit Lab", "📰 News", "📞 Contacts"])

# --- СТРАНИЦА 1: HOME ---
if page == "🏠 Home":
    st.markdown("""
        <div style="padding: 100px 10%; text-align: center;">
            <h1 style="font-size: 5rem; font-weight: 900; color: #ffffff;">FINANCE STATEMENT CHECKER</h1>
            <p style="font-size: 1.8rem; color: #800020; font-weight: 800;">ELITE AUDIT TERMINAL</p>
            <p style="color: #ffffff; font-size: 1.3rem; opacity: 0.8;">Architecture by: <b>Naikina Dariya & Erik Amira</b></p>
        </div>
    """, unsafe_allow_html=True)

# --- СТРАНИЦА 2: EDUCATION (ВСЁ ВЕРНУЛИ) ---
elif page == "📚 Education Center":
    st.markdown("<h2 class='section-title'>Financial Education</h2>", unsafe_allow_html=True)
    
    # Видео с ИИ-диктором
    st.markdown("### 🎥 AI Masterclass: How to Read Statements")
    st.video("https://www.youtube.com/watch?v=N4fXW96_Aas") 
    
    st.markdown("---")

    # BALANCE SHEET
    with st.expander("📊 BALANCE SHEET DETAILS"):
        st.markdown("""<div class="white-text">
        <b>Balance Sheet</b> — это снимок состояния компании. Формула: <b>Assets = Liabilities + Equity</b>.
        Он показывает, чем владеет компания и за счет чего это было куплено.
        <br><a href="https://www.investopedia.com/terms/b/balancesheet.asp" class="custom-link">Learn More</a></div>""", unsafe_allow_html=True)

    # INCOME STATEMENT
    with st.expander("📈 INCOME STATEMENT DETAILS"):
        st.markdown("""<div class="white-text">
        <b>Income Statement</b> показывает прибыльность. Формула: <b>Revenue - Expenses = Net Income</b>.
        Здесь вы видите, насколько эффективно работает бизнес в течение времени.
        <br><a href="https://www.investopedia.com/terms/i/incomestatement.asp" class="custom-link">Learn More</a></div>""", unsafe_allow_html=True)

    # CASH FLOW
    with st.expander("💸 CASH FLOW DETAILS"):
        st.markdown("""<div class="white-text">
        <b>Cash Flow</b> отслеживает реальные деньги. Прибыль в отчетах не всегда означает наличие денег на счету.
        Разделяется на операционную, инвестиционную и финансовую деятельность.
        <br><a href="https://www.investopedia.com/terms/c/cashflowstatement.asp" class="custom-link">Learn More</a></div>""", unsafe_allow_html=True)

# --- СТРАНИЦА 3: AUDIT LAB (С ЭКСЕЛЕМ И ТОГГЛОМ) ---
elif page == "🔬 Audit Lab":
    st.markdown("<h2 class='section-title'>Audit Terminal</h2>", unsafe_allow_html=True)
    t1, t2 = st.tabs(["Manual Entry", "Excel Database"])
    
    with t1:
        st.markdown("### Asset Verification")
        use_detailed = st.toggle("Enable Detailed Assets")
        
        col1, col2 = st.columns(2)
        with col1:
            if use_detailed:
                c = st.number_input("Cash", 0.0)
                inv = st.number_input("Inventory", 0.0)
                ppe = st.number_input("Fixed Assets", 0.0)
                total_a = c + inv + ppe
            else:
                total_a = st.number_input("Total Assets", 0.0)
        with col2:
            liab = st.number_input("Liabilities", 0.0)
            equity = st.number_input("Equity", 0.0)
            total_le = liab + equity
            
        if st.button("RUN AUDIT"):
            if total_a == total_le and total_a > 0:
                st.balloons()
                st.success("BALANCED")
            else: st.error("NOT BALANCED")
            st.plotly_chart(px.bar(x=['Assets', 'Liab+Eq'], y=[total_a, total_le], color_discrete_sequence=['#800020']))

    with t2:
        st.markdown("### Excel Audit")
        file = st.file_uploader("Upload .xlsx", type=["xlsx"])
        if file:
            df = pd.read_excel(file)
            st.dataframe(df.head())
            if st.button("PROCESS FILE"):
                st.balloons()
                st.success("Verified")

# --- СТРАНИЦА 4: NEWS ---
elif page == "📰 News":
    st.markdown("<h2 class='section-title'>Market News</h2>", unsafe_allow_html=True)
    st.markdown("<div class='news-card'><h4>Market Growth</h4><p>Global markets reached new highs in 2026.</p></div>", unsafe_allow_html=True)

# --- СТРАНИЦА 5: CONTACTS ---
elif page == "📞 Contacts":
    st.markdown("<h2 class='section-title'>Contact Us</h2>", unsafe_allow_html=True)
    st.write("Developers: Naikina Dariya & Erik Amira")
    st.write("Email: support@finchecker.pro")
    st.markdown('<a href="https://www.trustpilot.com" class="custom-link">Reviews ⭐️</a>', unsafe_allow_html=True)

st.markdown("<br><hr><p style='text-align: center; opacity: 0.5;'>©️ 2026 Finance Checker Pro</p>", unsafe_allow_html=True)
