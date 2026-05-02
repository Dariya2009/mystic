import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Конфигурация страницы
st.set_page_config(page_title="Finance Checker Pro", layout="wide", page_icon="📈")

# 2. Стили CSS
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #161b22; border-right: 2px solid #800020; }
    .white-text-box { color: #ffffff !important; line-height: 1.6; font-size: 1.1rem; }
    .section-title { color: #800020; font-size: 3rem; font-weight: 800; }
    .custom-link {
        display: inline-block; padding: 10px 20px; background-color: #800020;
        color: white !important; text-decoration: none; border-radius: 5px; font-weight: 600;
    }
    .news-card {
        background: #1c2128; padding: 20px; border-radius: 12px;
        border-left: 6px solid #800020; margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- НАВИГАЦИЯ ---
page = st.sidebar.radio("MENU", ["🏠 Home", "📚 Education", "🔬 Audit Lab", "📰 News", "📞 Contacts"])

# --- PAGE 1: HOME ---
if page == "🏠 Home":
    st.markdown("""
        <div style="padding: 80px 10%; text-align: center;">
            <h1 style="font-size: 4.5rem; font-weight: 900; color: #ffffff;">FINANCE STATEMENT CHECKER</h1>
            <p style="font-size: 1.8rem; color: #800020; font-weight: 800;">ELITE VERIFICATION SYSTEM</p>
            <p style="color: #ffffff; font-size: 1.2rem; opacity: 0.8;">Architects: <b>Naikina Dariya & Erik Amira</b></p>
        </div>
    """, unsafe_allow_html=True)

# --- PAGE 2: EDUCATION (ВИДЕО И ФОТО) ---
elif page == "📚 Education":
    st.markdown("<h2 class='section-title'>Financial Education Hub</h2>", unsafe_allow_html=True)
    
    # Видео с YouTube (Фундаментальный анализ)
    st.video("https://www.youtube.com/watch?v=yWVP6_nAsD4") 
    
    col_t, col_i = st.columns([2, 1])
    with col_t:
        with st.expander("📊 BALANCE SHEET THEORY", expanded=True):
            st.markdown("""<div class='white-text-box'>
            The Balance Sheet is a snapshot of financial health. It follows the rule: <b>Assets = Liabilities + Equity</b>.
            It shows how the company uses its resources.</div>""", unsafe_allow_html=True)
            st.markdown('<a href="https://www.investopedia.com/terms/b/balancesheet.asp" class="custom-link">Read Full Guide</a>', unsafe_allow_html=True)
    with col_i:
        # Надежная ссылка на инфографику
        st.image("https://img.freepik.com/free-vector/gradient-stock-market-concept_23-2149166910.jpg", caption="Financial Analysis")

# --- PAGE 3: AUDIT LAB (ИНСТРУМЕНТЫ + EXCEL) ---
elif page == "🔬 Audit Lab":
    st.markdown("<h2 class='section-title'>Audit Terminal</h2>", unsafe_allow_html=True)
    t1, t2 = st.tabs(["Manual Entry", "Excel Database"])
    
    with t1:
        st.markdown("### Asset & Liability Verification")
        # ВОЗВРАЩАЕМ ТОТ САМЫЙ ИНСТРУМЕНТ
        use_detailed = st.toggle("Enable Detailed Asset Breakdown")
        
        col1, col2 = st.columns(2)
        with col1:
            if use_detailed:
                c = st.number_input("Cash & Bank", 0.0)
                inv = st.number_input("Inventory", 0.0)
                ppe = st.number_input("Fixed Assets", 0.0)
                total_a = c + inv + ppe
                st.info(f"Calculated Total Assets: {total_a}")
            else:
                total_a = st.number_input("Total Assets", 0.0)
        
        with col2:
            liab = st.number_input("Total Liabilities", 0.0)
            equity = st.number_input("Total Equity", 0.0)
            total_le = liab + equity
            
        if st.button("RUN SYSTEM AUDIT"):
            if total_a == total_le and total_a > 0:
                st.balloons()
                st.success("STATUS: BALANCED")
            else:
                st.error("STATUS: DISCREPANCY FOUND")
            st.plotly_chart(px.bar(x=['Assets', 'Liab+Eq'], y=[total_a, total_le], color_discrete_sequence=['#800020']))

    with t2:
        st.markdown("### Professional Excel Audit")
        file = st.file_uploader("Upload .xlsx", type=["xlsx"])
        if file:
            df = pd.read_excel(file)
            st.dataframe(df.head())
            if st.button("BATCH PROCESS"):
                st.balloons()
                st.success("File verified.")

# --- PAGE 4: NEWS ---
elif page == "📰 News":
    st.markdown("<h2 class='section-title'>Market News</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<div class='news-card'><h4>Market Update</h4><p>Global indices show positive trends in 2026.</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='news-card'><h4>AI in Finance</h4><p>Algorithms now handle 40% of corporate audits.</p></div>", unsafe_allow_html=True)

# --- PAGE 5: CONTACTS ---
elif page == "📞 Contacts":
    st.markdown("<h2 class='section-title'>Contacts</h2>", unsafe_allow_html=True)
    st.markdown("### Developers: Naikina Dariya & Erik Amira")
    st.markdown("Email: support@finchecker.pro")
    st.markdown('<a href="https://www.trustpilot.com" class="custom-link">Official Reviews ⭐️</a>', unsafe_allow_html=True)

st.markdown("<br><hr><p style='text-align: center; opacity: 0.5;'>©️ 2026 Finance Checker Pro</p>", unsafe_allow_html=True)
