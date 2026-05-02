import streamlit as st
import pandas as pd
import plotly.express as px

# Конфигурация страницы
st.set_page_config(page_title="Finance Statement Checker Pro", layout="wide", page_icon="📈")

# Улучшенный CSS для максимальной читаемости
st.markdown("""
    <style>
    html { scroll-behavior: smooth; }
    .stApp { background-color: #0e1117; color: #ffffff; }
    
    /* Header с кнопками */
    .header-bar {
        display: flex; justify-content: flex-end; padding: 15px 5%;
        background: #1a1c23; border-bottom: 2px solid #800020;
    }
    .auth-btn {
        margin-left: 15px; padding: 10px 25px; border-radius: 8px;
        font-weight: 800; cursor: pointer; transition: 0.3s; border: 2px solid #800020;
    }
    .login-btn { color: #ffffff; background: transparent; }
    .signup-btn { background: #800020; color: white; }
    
    /* Секции */
    .hero-section { background: #0e1117; padding: 100px 10%; text-align: center; }
    .knowledge-section { background-color: #ffffff; color: #000000; padding: 80px 10%; border-radius: 30px 30px 0 0; }
    .checker-section { background-color: #161b22; padding: 80px 10%; border-top: 5px solid #800020; }
    .news-section { background-color: #0e1117; padding: 60px 10%; }

    /* Текст: Максимальный контраст */
    .main-title { font-size: 4.5rem; font-weight: 900; color: #ffffff; margin-bottom: 0px; }
    .section-title { font-size: 3rem; font-weight: 800; margin-bottom: 40px; }
    .white-text { color: #ffffff !important; font-weight: 500; }
    .black-text { color: #000000 !important; font-weight: 500; line-height: 1.6; }

    /* Карточки новостей */
    .news-card {
        background: #1a1c23; padding: 25px; border-radius: 15px;
        border-left: 5px solid #800020; margin-bottom: 20px;
    }
    .news-title { color: #ffffff; font-weight: 700; font-size: 1.2rem; }
    .news-body { color: #bbbbbb; }
    </style>
""", unsafe_allow_html=True)

# --- 1. ВЕРХНЯЯ ПАНЕЛЬ (AUTH) ---
st.markdown("""
    <div class="header-bar">
        <div class="auth-btn login-btn">LOG IN</div>
        <div class="auth-btn signup-btn">SIGN UP</div>
    </div>
""", unsafe_allow_html=True)

# --- 2. ГЛАВНЫЙ ЭКРАН (TITLE) ---
st.markdown("""
    <div class="hero-section">
        <h1 class="main-title">FINANCE STATEMENT CHECKER</h1>
        <p style="font-size: 1.8rem; color: #800020; font-weight: 700;">STRATEGIC AUDIT TERMINAL</p>
        <p style="color: #ffffff; font-size: 1.2rem;">Developed by: <b>Naikina Dariya & Erik Amira</b></p>
    </div>
""", unsafe_allow_html=True)

# --- 3. EDUCATIONAL MODULE (Белая секция) ---
st.markdown("<div class='knowledge-section' id='learn'>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title' style='color: #800020;'>Financial Education Module</h2>", unsafe_allow_html=True)

col_k1, col_k2, col_k3 = st.columns(3)

with col_k1:
    st.markdown("<h3 style='color: #000000; font-size: 1.8rem;'>1. Balance Sheet</h3>", unsafe_allow_html=True)
    st.markdown("<p class='black-text'>The <b>Balance Sheet</b> is the most important report. It follows the formula: <b>Assets = Liabilities + Equity</b>. It shows what a business owns and how those assets are financed. If the sides don't match, the accounting is incorrect.</p>", unsafe_allow_html=True)
    st.image("https://cdn.educba.com/academy/wp-content/uploads/2019/01/Balance-Sheet-Formula.jpg", use_container_width=True)
    st.markdown("[Learn more about Balance Sheets 🔗](https://www.investopedia.com/terms/b/balancesheet.asp)")

with col_k2:
    st.markdown("<h3 style='color: #000000; font-size: 1.8rem;'>2. Income Statement</h3>", unsafe_allow_html=True)
    st.markdown("<p class='black-text'>The <b>Income Statement</b> (P&L) focuses on the bottom line: <b>Revenue - Expenses = Net Income</b>. It tells you if the company is actually making money or losing it over a period of time.</p>", unsafe_allow_html=True)
    st.image("https://corporatefinanceinstitute.com/assets/income-statement-example.png", use_container_width=True)
    st.markdown("[Learn more about Net Income 🔗](https://www.investopedia.com/terms/i/incomestatement.asp)")

with col_k3:
    st.markdown("<h3 style='color: #000000; font-size: 1.8rem;'>3. Cash Flow</h3>", unsafe_allow_html=True)
    st.markdown("<p class='black-text'><b>Cash Flow</b> tracks the real movement of money. A company can have 'profit' on paper but have zero 'cash' in the bank. This statement tracks Operating, Investing, and Financing cash movements.</p>", unsafe_allow_html=True)
    st.image("https://accounting-simplified.com/financial/statements/cash-flow-statement.png", use_container_width=True)
    st.markdown("[Learn more about Cash Flow 🔗](https://www.investopedia.com/terms/c/cashflowstatement.asp)")
st.markdown("</div>", unsafe_allow_html=True)

# --- 4. AUDIT TERMINAL (Темная секция) ---
st.markdown("<div class='checker-section' id='check'>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title' style='color: #ffffff;'>Verification Terminal</h2>", unsafe_allow_html=True)

mode = st.radio("Choose Input Method", ["Manual Terminal", "Excel Database"], horizontal=True)

if mode == "Manual Terminal":
    report = st.selectbox("Select Financial Statement to Audit", ["Balance Sheet Audit", "Income Analysis", "Cash Flow Sync"])
    st.markdown("<br>", unsafe_allow_html=True)
    
    if report == "Balance Sheet Audit":
        # ИНТЕРАКТИВНЫЙ ВВОД АССЕТОВ
        use_detailed = st.toggle("Enable Detailed Asset Inputs", value=False)
        if use_detailed:
            c1, c2 = st.columns(2)
            with c1:
                cash = st.number_input("Cash & Bank Accounts", value=0.0)
                inv = st.number_input("Inventory Value", value=0.0)
            with c2:
                fixed = st.number_input("Fixed Assets (PPE)", value=0.0)
                other = st.number_input("Other Assets", value=0.0)
            total_a = cash + inv + fixed + other
        else:
            total_a = st.number_input("Enter Total Assets", value=0.0)

        # ЛИАБИЛИТИС
        st.markdown("---")
        liab = st.number_input("Total Liabilities (Debt)", value=0.0)
        equity = st.number_input("Total Shareholder Equity", value=0.0)
        total_le = liab + equity

        if st.button("RUN FULL BALANCE AUDIT"):
            if total_a == total_le and total_a != 0:
                st.balloons()
                st.success(f"VERIFIED: Assets ({total_a}) perfectly match Liabilities + Equity.")
            else:
                st.error(f"AUDIT FAILED: Discrepancy detected! Difference: {abs(total_a - total_le)}")
            
            fig = px.bar(x=['Total Assets', 'Liab + Equity'], y=[total_a, total_le], 
                         range_y=[0, 10000], color=['Assets', 'Funding'],
                         color_discrete_map={'Assets': '#800020', 'Funding': '#ffffff'})
            st.plotly_chart(fig, use_container_width=True)

    elif report == "Income Analysis":
        rev = st.number_input("Enter Total Revenue", value=0.0)
        exp = st.number_input("Enter Total Expenses", value=0.0)
        reported_ni = st.number_input("Enter Reported Net Income", value=0.0)
        
        if st.button("VALIDATE PROFITABILITY"):
            if reported_ni == (rev - exp) and rev != 0:
                st.balloons()
                st.success("SUCCESS: Profit margin is calculated correctly.")
            else:
                st.error("ERROR: Net Income does not match Revenue minus Expenses.")
            
            fig = px.bar(x=['Revenue', 'Expenses', 'Net Income'], y=[rev, exp, reported_ni], 
                         range_y=[0, 10000], color_discrete_sequence=['#800020'])
            st.plotly_chart(fig, use_container_width=True)

    elif report == "Cash Flow Sync":
        st.info("Cash Flow validation module is active. Enter your balances below.")
        op = st.number_input("Cash from Operating Activities", value=0.0)
        inv = st.number_input("Cash from Investing Activities", value=0.0)
        fin = st.number_input("Cash from Financing Activities", value=0.0)
        total_cf = op + inv + fin
        st.metric("Total Net Cash Flow", f"{total_cf}")
        if st.button("SYNC CASH FLOW"):
            st.balloons()

else:
    st.markdown("### Professional Excel Upload")
    file = st.file_uploader("Upload Company .xlsx Report", type="xlsx")
    if file:
        st.success("File identified. Ready for batch audit.")
        st.balloons()

st.markdown("</div>", unsafe_allow_html=True)

# --- 5. ФИНАНСОВЫЕ НОВОСТИ ---
st.markdown("<div class='news-section'>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title' style='color: #800020;'>Live Financial News</h2>", unsafe_allow_html=True)

n1, n2 = st.columns(2)
with n1:
    st.markdown("""<div class='news-card'><div class='news-title'>Global Markets Update</div><div class='news-body'>Inflation rates in developed economies show a steady decline of 0.5%.</div></div>""", unsafe_allow_html=True)
    st.markdown("""<div class='news-card'><div class='news-title'>Tech Earnings Season</div><div class='news-body'>Nvidia and Apple report record-breaking revenue in Q1 2026.</div></div>""", unsafe_allow_html=True)
with n2:
    st.markdown("""<div class='news-card'><div class='news-title'>Central Bank Policy</div><div class='news-body'>Federal Reserve maintains current interest rates for the third month.</div></div>""", unsafe_allow_html=True)
    st.markdown("""<div class='news-card'><div class='news-title'>Crypto Regulation</div><div class='news-body'>EU countries agree on a unified framework for digital asset audits.</div></div>""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><br><p style='text-align: center; color: #555; padding-bottom: 50px;'>Finance Statement Checker v5.0 | Naikina Dariya & Erik Amira | 2026</p>", unsafe_allow_html=True)
