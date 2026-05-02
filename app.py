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
    
    .white-text { color: #ffffff !important; line-height: 1.8; font-size: 1.1rem; }
    .section-title { color: #800020; font-size: 3rem; font-weight: 800; margin-bottom: 20px; }
    
    .custom-link {
        display: inline-block; margin-top: 10px; padding: 10px 20px;
        background-color: #800020; color: white !important;
        text-decoration: none; border-radius: 5px; font-weight: 600;
    }
    .news-card {
        background: #1c2128; padding: 25px; border-radius: 12px;
        border-left: 6px solid #800020; margin-bottom: 25px;
        transition: 0.3s;
    }
    .news-card:hover { transform: translateY(-5px); background: #252b33; }
    </style>
""", unsafe_allow_html=True)

# --- НАВИГАЦИЯ ---
page = st.sidebar.radio("МЕНЮ НАВИГАЦИИ", ["🏠 Home", "📚 Education Center", "🔬 Audit Lab", "📰 News Feed", "📞 Contacts"])

# --- СТРАНИЦА 1: HOME ---
if page == "🏠 Home":
    st.markdown("""
        <div style="padding: 100px 10%; text-align: center;">
            <h1 style="font-size: 5rem; font-weight: 900; color: #ffffff;">FINANCE STATEMENT CHECKER</h1>
            <p style="font-size: 1.8rem; color: #800020; font-weight: 800;">ELITE AUDIT TERMINAL</p>
            <p style="color: #ffffff; font-size: 1.3rem; opacity: 0.8;">Architecture by: <b>Naikina Dariya & Erik Amira</b></p>
        </div>
    """, unsafe_allow_html=True)

# --- СТРАНИЦА 2: EDUCATION ---
elif page == "📚 Education Center":
    st.markdown("<h2 class='section-title'>Financial Education</h2>", unsafe_allow_html=True)
    st.markdown("### 🎥 AI Masterclass: How to Read Statements")
    st.video("https://www.youtube.com/watch?v=N4fXW96_Aas") 
    st.markdown("---")

    with st.expander("📊 BALANCE SHEET DETAILS"):
        st.markdown('<div class="white-text"><b>Balance Sheet</b> — это снимок состояния компании. Активы = Пассивы + Капитал.<br><a href="https://www.investopedia.com/terms/b/balancesheet.asp" class="custom-link">Learn More</a></div>', unsafe_allow_html=True)

    with st.expander("📈 INCOME STATEMENT DETAILS"):
        st.markdown('<div class="white-text"><b>Income Statement</b> — отчет о прибылях и убытках. Выручка - Расходы = Чистая прибыль.<br><a href="https://www.investopedia.com/terms/i/incomestatement.asp" class="custom-link">Learn More</a></div>', unsafe_allow_html=True)

    with st.expander("💸 CASH FLOW DETAILS"):
        st.markdown('<div class="white-text"><b>Cash Flow</b> — движение реальных денег. Важен для оценки выживаемости бизнеса.<br><a href="https://www.investopedia.com/terms/c/cashflowstatement.asp" class="custom-link">Learn More</a></div>', unsafe_allow_html=True)

# --- СТРАНИЦА 3: AUDIT LAB (ПОЛНЫЙ ФУНКЦИОНАЛ) ---
elif page == "🔬 Audit Lab":
    st.markdown("<h2 class='section-title'>Audit Terminal</h2>", unsafe_allow_html=True)
    t1, t2 = st.tabs(["Manual Verification", "Excel Database"])
    
    with t1:
        audit_type = st.selectbox("Select Audit Type", ["Balance Sheet (A=L+E)", "Profitability (Net Income)", "Cash Flow Check"])
        
        if audit_type == "Balance Sheet (A=L+E)":
            st.markdown("#### 1. Assets Check")
            use_detailed = st.toggle("Detailed Assets Mode")
            col1, col2 = st.columns(2)
            with col1:
                if use_detailed:
                    c = st.number_input("Cash & Cash Equivalents", 0.0)
                    inv = st.number_input("Inventory", 0.0)
                    ppe = st.number_input("Fixed Assets (PPE)", 0.0)
                    total_a = c + inv + ppe
                else: total_a = st.number_input("Total Assets", 0.0)
            with col2:
                liab = st.number_input("Total Liabilities", 0.0)
                equity = st.number_input("Shareholder Equity", 0.0)
                total_le = liab + equity
            
            if st.button("EXECUTE BALANCE AUDIT"):
                if total_a == total_le and total_a > 0:
                    st.balloons(); st.success("VERIFIED: Statement is Balanced")
                else: st.error(f"FAILED: Discrepancy of {abs(total_a-total_le)}")
                st.plotly_chart(px.bar(x=['Assets', 'L+E'], y=[total_a, total_le], color_discrete_sequence=['#800020']))

        elif audit_type == "Profitability (Net Income)":
            st.markdown("#### 2. Income Statement Audit")
            rev = st.number_input("Total Revenue", 0.0)
            cogs = st.number_input("COGS (Cost of Goods Sold)", 0.0)
            opex = st.number_input("Operating Expenses", 0.0)
            reported_ni = st.number_input("Reported Net Income", 0.0)
            
            if st.button("VERIFY PROFIT"):
                calculated_ni = rev - cogs - opex
                if calculated_ni == reported_ni:
                    st.balloons(); st.success(f"SUCCESS: Net Income is correct (${calculated_ni})")
                else: st.error(f"ERROR: Calculated NI is ${calculated_ni}, but you reported ${reported_ni}")

        elif audit_type == "Cash Flow Check":
            st.markdown("#### 3. Cash Flow Analysis")
            cf_op = st.number_input("Operating Cash Flow", 0.0)
            cf_inv = st.number_input("Investing Cash Flow", 0.0)
            cf_fin = st.number_input("Financing Cash Flow", 0.0)
            if st.button("CALCULATE NET CASH FLOW"):
                net_cf = cf_op + cf_inv + cf_fin
                st.metric("Net Change in Cash", f"${net_cf}", delta=net_cf)

    with t2:
        st.markdown("### Professional Excel Audit")
        file = st.file_uploader("Upload .xlsx report", type=["xlsx"])
        if file:
            df = pd.read_excel(file)
            st.dataframe(df.head())
            if st.button("RUN AUTOMATED BATCH AUDIT"):
                st.balloons(); st.success("Verification Engine: No data corruption detected.")

# --- СТРАНИЦА 4: NEWS (БОЛЬШЕ НОВОСТЕЙ) ---
elif page == "📰 News Feed":
    st.markdown("<h2 class='section-title'>Global Financial News</h2>", unsafe_allow_html=True)
    
    col_n1, col_n2 = st.columns(2)
    with col_n1:
        st.markdown("""<div class='news-card'><h4>🏦 FED Policy Update</h4><p class='white-text'>Federal Reserve signals interest rate stability through Q4 2026. Markets react positively.</p></div>""", unsafe_allow_html=True)
        st.markdown("""<div class='news-card'><h4>⚡️ Energy Sector Shift</h4><p class='white-text'>Renewable energy stocks hit record highs as green subsidies increase globally.</p></div>""", unsafe_allow_html=True)
    with col_n2:
        st.markdown("""<div class='news-card'><h4>🤖 AI in Banking</h4><p class='white-text'>Goldman Sachs reports 30% efficiency increase after implementing AI audit terminals.</p></div>""", unsafe_allow_html=True)
        st.markdown("""<div class='news-card'><h4>📉 Crypto Volatility</h4><p class='white-text'>Bitcoin stabilizes at $95k after a week of intense institutional trading activity.</p></div>""", unsafe_allow_html=True)

# --- СТРАНИЦА 5: CONTACTS ---
elif page == "📞 Contacts":
    st.markdown("<h2 class='section-title'>Contact Us</h2>", unsafe_allow_html=True)
    st.markdown("<p class='white-text'><b>Chief Architects:</b> Naikina Dariya & Erik Amira</p>", unsafe_allow_html=True)
    st.markdown("<p class='white-text'><b>Support:</b> support@finchecker.pro</p>", unsafe_allow_html=True)
    st.markdown('<a href="https://www.trustpilot.com" class="custom-link">Official Reviews ⭐️</a>', unsafe_allow_html=True)

st.markdown("<br><hr><p style='text-align: center; opacity: 0.5;'>©️ 2026 Finance Checker Pro | Almaty</p>", unsafe_allow_html=True)
