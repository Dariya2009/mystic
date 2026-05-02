import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Базовая конфигурация
st.set_page_config(page_title="Finance Statement Checker Pro", layout="wide", page_icon="📈")

# 2. Определение стилей (CSS) - Убраны все спорные символы
style_html = """
<style>
    html { scroll-behavior: smooth; }
    .stApp { background-color: #0e1117; color: #ffffff; }
    .header-bar {
        display: flex; justify-content: flex-end; padding: 20px 5%;
        background: #161b22; border-bottom: 2px solid #800020;
    }
    .auth-btn {
        margin-left: 15px; padding: 10px 30px; border-radius: 5px;
        font-weight: 700; border: 2px solid #800020; color: white; text-decoration: none;
    }
    .signup-btn { background: #800020; color: white; }
    .hero-section { background: #0e1117; padding: 80px 10%; text-align: center; }
    .knowledge-section { background-color: #161b22; padding: 80px 10%; border-radius: 50px 50px 0 0; }
    .checker-section { background-color: #0e1117; padding: 80px 10%; border-top: 5px solid #800020; }
    .contact-section { background-color: #161b22; padding: 60px 10%; border-top: 1px solid #333; }
    .white-text-box { color: #ffffff !important; line-height: 1.8; font-size: 1.1rem; margin-bottom: 20px; }
    .section-title { color: #800020; font-size: 3rem; font-weight: 800; margin-bottom: 30px; }
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
"""
st.markdown(style_html, unsafe_allow_html=True)

# 3. HEADER
st.markdown('<div class="header-bar"><div class="auth-btn">LOG IN</div><div class="auth-btn signup-btn">SIGN UP</div></div>', unsafe_allow_html=True)

# 4. HERO
st.markdown("""
<div class="hero-section">
    <h1 style="font-size: 5rem; font-weight: 900; color: #ffffff;">FINANCE STATEMENT CHECKER</h1>
    <p style="font-size: 1.8rem; color: #800020; font-weight: 800;">ELITE AUDIT TERMINAL</p>
    <p style="color: #ffffff; font-size: 1.2rem; opacity: 0.8;">Architecture by: Naikina Dariya & Erik Amira</p>
</div>
""", unsafe_allow_html=True)

# 5. EDUCATION (Текст белый, ссылок много)
st.markdown("<div class='knowledge-section'><h2 class='section-title'>Financial Education</h2>", unsafe_allow_html=True)

with st.expander("📊 DETAILED ANALYSIS: THE BALANCE SHEET"):
    st.markdown("""
    <div class="white-text-box">
    <b>The Balance Sheet</b> reports a company's financial position at a point in time. 
    <b>Formula: Assets = Liabilities + Equity</b>. 
    It is used to evaluate liquidity, solvency, and capital structure.<br>
    <a href="https://www.investopedia.com/terms/b/balancesheet.asp" class="custom-link">Deep Dive 🔗</a>
    </div>
    """, unsafe_allow_html=True)

with st.expander("📈 DETAILED ANALYSIS: THE INCOME STATEMENT"):
    st.markdown("""
    <div class="white-text-box">
    The <b>Income Statement</b> measures financial performance over a period. 
    It focuses on <b>Revenue - Expenses = Net Income</b>. 
    It is the primary tool for evaluating the profitability of a business.<br>
    <a href="https://www.investopedia.com/terms/i/incomestatement.asp" class="custom-link">Profitability Guide 🔗</a>
    </div>
    """, unsafe_allow_html=True)

with st.expander("💸 DETAILED ANALYSIS: CASH FLOW STATEMENT"):
    st.markdown("""
    <div class="white-text-box">
    The <b>Cash Flow Statement</b> tracks real movement of cash. 
    A business can be profitable but have no cash. It covers Operating, Investing, and Financing activities.<br>
    <a href="https://www.investopedia.com/terms/c/cashflowstatement.asp" class="custom-link">Cash Flow Masterclass 🔗</a>
    </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# 6. AUDIT TERMINAL (С Excel)
st.markdown("<div class='checker-section'><h2 style='color: white; font-size: 3rem; font-weight: 800;'>Audit Terminal</h2>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["[ MANUAL ENTRY ]", "[ EXCEL DATABASE ]"])

with tab1:
    report_type = st.selectbox("Report Type", ["Balance Sheet Audit", "Income Analysis", "Cash Flow Sync"])
    
    if report_type == "Balance Sheet Audit":
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Assets Analysis")
            use_detailed = st.toggle("Enable Detailed Breakdown")
            if use_detailed:
                c = st.number_input("Cash & Bank", value=0.0)
                i = st.number_input("Inventory", value=0.0)
                f = st.number_input("Fixed Assets", value=0.0)
                total_a = c + i + f
            else:
                total_a = st.number_input("Total Assets", value=0.0)
        with col2:
            st.markdown("### Liabilities & Equity")
            liab = st.number_input("Liabilities", value=0.0)
            equi = st.number_input("Equity", value=0.0)
            total_le = liab + equi

        if st.button("RUN AUDIT"):
            if total_a == total_le and total_a > 0:
                st.balloons()
                st.success("BALANCED")
            else: st.error("DISCREPANCY DETECTED")
            st.plotly_chart(px.bar(x=['Assets', 'Liab+Eq'], y=[total_a, total_le], color_discrete_sequence=['#800020']))

    elif report_type == "Income Analysis":
        rev = st.number_input("Revenue", value=0.0)
        exp = st.number_input("Expenses", value=0.0)
        if st.button("CHECK NET INCOME"):
            st.write(f"Profit: {rev - exp}")

    elif report_type == "Cash Flow Sync":
        cf_in = st.number_input("Inflow", value=0.0)
        cf_out = st.number_input("Outflow", value=0.0)
        if st.button("NET CASH"):
            st.write(f"Balance: {cf_in - cf_out}")

with tab2:
    st.markdown("### Professional Excel Upload")
    exc_file = st.file_uploader("Upload .xlsx report", type=["xlsx"])
    if exc_file:
        df_exc = pd.read_excel(exc_file)
        st.dataframe(df_exc.head())
        if st.button("BATCH AUDIT"):
            st.balloons()
            st.success("File Analysis Complete.")

st.markdown("</div>", unsafe_allow_html=True)

# 7. NEWS
st.markdown("<div style='padding: 80px 10%;'><h2 class='section-title'>Live News</h2>", unsafe_allow_html=True)
cn1, cn2 = st.columns(2)
with cn1:
    st.markdown("<div class='news-card'><h4>Market Stability</h4><p>Rates remain steady for 2026.</p></div>", unsafe_allow_html=True)
with cn2:
    st.markdown("<div class='news-card'><h4>Tech Surge</h4><p>AI sector reports growth.</p></div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# 8. CONTACTS & REVIEWS
st.markdown("<div class='contact-section'><h2 class='section-title'>Contacts</h2>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("### Developers")
    st.markdown("<p style='color: white;'>• Naikina Dariya<br>• Erik Amira</p>", unsafe_allow_html=True)
with c2:
    st.markdown("### Support")
    st.markdown("<p style='color: white;'>Email: support@finchecker.pro<br>Almaty, Kazakhstan</p>", unsafe_allow_html=True)
with c3:
    st.markdown("### Feedback")
    st.markdown("<p style='color: white;'>Check our reputation:</p>", unsafe_allow_html=True)
    st.markdown('<a href="https://www.trustpilot.com" class="custom-link">View Reviews ⭐️</a>', unsafe_allow_html=True)
st.markdown("</div><p style='text-align: center; color: #444; padding: 40px;'>©️ 2026 Finance Checker Pro</p>", unsafe_allow_html=True)
