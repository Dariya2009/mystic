import streamlit as st
import pandas as pd
import plotly.express as px

# Конфигурация страницы
st.set_page_config(page_title="Finance Statement Checker Pro", layout="wide", page_icon="📈")

# Стилизация: Бордовый + Темный Графит + Контрастный белый текст
st.markdown("""
    <style>
    html { scroll-behavior: smooth; }
    .stApp { background-color: #0e1117; color: #ffffff; }
    
    /* Кнопки входа в углу */
    .header-bar {
        display: flex; justify-content: flex-end; padding: 20px 5%;
        background: #161b22; border-bottom: 2px solid #800020;
    }
    .auth-btn {
        margin-left: 15px; padding: 10px 30px; border-radius: 5px;
        font-weight: 700; cursor: pointer; border: 2px solid #800020;
    }
    .login-btn { color: #ffffff; background: transparent; }
    .signup-btn { background: #800020; color: white; }
    
    /* Секции */
    .hero-section { background: #0e1117; padding: 100px 10%; text-align: center; }
    .knowledge-section { background-color: #ffffff; color: #000000; padding: 80px 10%; border-radius: 50px 50px 0 0; }
    .checker-section { background-color: #161b22; padding: 80px 10%; border-top: 5px solid #800020; }
    .news-section { background-color: #0e1117; padding: 80px 10%; }

    /* Текстовые блоки */
    .white-text { color: #ffffff !important; line-height: 1.6; }
    .black-text { color: #1a1a1a !important; line-height: 1.8; font-size: 1.1rem; }
    .main-title { font-size: 5rem; font-weight: 900; color: #ffffff; letter-spacing: -2px; }
    
    /* Карточки новостей */
    .news-card {
        background: #1c2128; padding: 25px; border-radius: 12px;
        border-left: 6px solid #800020; margin-bottom: 25px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.5);
    }
    .news-title { color: #ffffff; font-weight: 800; font-size: 1.3rem; margin-bottom: 10px; }
    .news-desc { color: #d0d0d0; font-size: 1rem; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
    <div class="header-bar">
        <div class="auth-btn login-btn">LOG IN</div>
        <div class="auth-btn signup-btn">SIGN UP</div>
    </div>
""", unsafe_allow_html=True)

# --- HERO ---
st.markdown("""
    <div class="hero-section">
        <h1 class="main-title">FINANCE STATEMENT CHECKER</h1>
        <p style="font-size: 1.8rem; color: #800020; font-weight: 800;">ELITE DATA VERIFICATION PLATFORM</p>
        <p style="color: #ffffff; font-size: 1.3rem; opacity: 0.9;">System Architecture by: <b>Naikina Dariya & Erik Amira</b></p>
    </div>
""", unsafe_allow_html=True)

# --- KNOWLEDGE BASE (Светлая часть) ---
st.markdown("<div class='knowledge-section'>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #800020; font-size: 3rem; font-weight: 800;'>Professional Financial Education</h2>", unsafe_allow_html=True)
st.markdown("<p class='black-text'>Click on the sections below to expand detailed information about global accounting standards.</p>", unsafe_allow_html=True)

with st.expander("📊 DETAILED ANALYSIS: THE BALANCE SHEET"):
    st.markdown("""
    <p class='black-text'>
    The <b>Balance Sheet</b> is the cornerstone of financial reporting. It reveals the company's financial health by balancing what is owned against what is owed.<br><br>
    <b>Core Equation:</b> Assets = Liabilities + Shareholder's Equity.<br><br>
    - <b>Assets:</b> Resources controlled by the entity (Cash, Inventory, Property).<br>
    - <b>Liabilities:</b> Obligations to outside parties (Loans, Accounts Payable).<br>
    - <b>Equity:</b> The owners' remaining interest in the company after all liabilities are paid.<br>
    This statement is crucial for investors to determine the liquidity and solvency of a business.
    </p>
    """, unsafe_allow_html=True)

with st.expander("📈 DETAILED ANALYSIS: THE INCOME STATEMENT"):
    st.markdown("""
    <p class='black-text'>
    Commonly referred to as the <b>Profit and Loss (P&L)</b> statement, the Income Statement measures a company's financial performance over a specific period.<br><br>
    <b>Core Equation:</b> Net Income = Revenue - Expenses.<br><br>
    It tracks how much revenue is generated from sales and subtracts the costs of doing business (COGS, Operating Expenses, Taxes). 
    A positive bottom line indicates profitability, while a negative one indicates a net loss. It is the primary tool used to evaluate growth and operational efficiency.
    </p>
    """, unsafe_allow_html=True)

with st.expander("💸 DETAILED ANALYSIS: CASH FLOW STATEMENT"):
    st.markdown("""
    <p class='black-text'>
    The <b>Cash Flow Statement</b> provides information about the actual cash inflows and outflows. It is divided into three main categories:<br><br>
    1. <b>Operating Activities:</b> Cash generated from core business products.<br>
    2. <b>Investing Activities:</b> Cash used for buying/selling assets like equipment or land.<br>
    3. <b>Financing Activities:</b> Cash flow from debt, loans, or dividends.<br><br>
    It is vital because profit on an income statement doesn't always equal cash in the bank. High profit with low cash flow can lead to bankruptcy.
    </p>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- AUDIT TERMINAL (Темная часть) ---
st.markdown("<div class='checker-section'>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #ffffff; font-size: 3rem; font-weight: 800;'>Audit & Verification Terminal</h2>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["[ MANUAL ENTRY ]", "[ EXCEL DATABASE ]"])

with tab1:
    report = st.selectbox("Select Report Logic", ["Balance Sheet Audit", "Income Analysis", "Cash Flow Sync"])
    st.markdown("<br>", unsafe_allow_html=True)
    
    if report == "Balance Sheet Audit":
        # Скрываемые подпункты по желанию
        with st.container():
            col_a, col_le = st.columns(2)
            with col_a:
                st.markdown("### Assets Input")
                use_detail = st.toggle("Use Detailed Asset Inputs")
                if use_detail:
                    c1 = st.number_input("Cash & Bank", value=0.0)
                    c2 = st.number_input("Fixed Assets", value=0.0)
                    total_a = c1 + c2
                else:
                    total_a = st.number_input("Total Assets Amount", value=0.0)
            
            with col_le:
                st.markdown("### Liabilities & Equity")
                l1 = st.number_input("Total Liabilities", value=0.0)
                e1 = st.number_input("Shareholder Equity", value=0.0)
                total_le = l1 + e1

        if st.button("RUN SYSTEM AUDIT"):
            if total_a == total_le and total_a > 0:
                st.balloons()
                st.success("AUDIT STATUS: PASSED - STATEMENT IS BALANCED")
            else:
                st.error(f"AUDIT STATUS: FAILED - VARIANCE DETECTED: {abs(total_a - total_le)}")
            
            fig = px.bar(x=['Assets', 'Liab+Eq'], y=[total_a, total_le], range_y=[0, 10000], color_discrete_sequence=['#800020'])
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white")
            st.plotly_chart(fig, use_container_width=True)

    elif report == "Income Analysis":
        rev = st.number_input("Total Revenue", value=0.0)
        exp = st.number_input("Total Expenses", value=0.0)
        ni = st.number_input("Reported Net Income", value=0.0)
        if st.button("VALIDATE PROFIT"):
            if ni == (rev - exp) and rev > 0:
                st.balloons()
                st.success("VERIFIED: Net Income is correct.")
            else:
                st.error("MISMATCH: Please check revenue/expense inputs.")

with tab2:
    st.markdown("### Batch Processing Interface")
    st.file_uploader("Upload .xlsx file for secure analysis")

st.markdown("</div>", unsafe_allow_html=True)

# --- NEWS SECTION ---
st.markdown("<div class='news-section'>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #800020; font-size: 3rem; font-weight: 800;'>Global Financial News Feed</h2>", unsafe_allow_html=True)

col_n1, col_n2 = st.columns(2)
with col_n1:
    st.markdown("""<div class='news-card'><div class='news-title'>Central Banks: Rate Stability</div><div class='news-desc'>The Federal Reserve signals a pause in interest rate hikes as labor markets show signs of rebalancing. Investors pivot to long-term bonds.</div></div>""", unsafe_allow_html=True)
    st.markdown("""<div class='news-card'><div class='news-title'>Tech Giants Revenue Surge</div><div class='news-desc'>Leading AI-driven corporations report a 25% increase in annual net income, exceeding wall street projections for Q1 2026.</div></div>""", unsafe_allow_html=True)
    st.markdown("""<div class='news-card'><div class='news-title'>ESG Reporting Standards</div><div class='news-desc'>New international regulations require companies to provide more transparent cash flow statements regarding green investments.</div></div>""", unsafe_allow_html=True)

with col_n2:
    st.markdown("""<div class='news-card'><div class='news-title'>Emerging Markets Growth</div><div class='news-desc'>Southeast Asian economies project a 5.8% GDP growth as digital trade and fintech adoption reach all-time highs in the region.</div></div>""", unsafe_allow_html=True)
    st.markdown("""<div class='news-card'><div class='news-title'>Oil & Energy Volatility</div><div class='news-desc'>Crude oil prices fluctuate amid geopolitical shifts, causing energy companies to adjust their capital expenditure (CAPEX) forecasts.</div></div>""", unsafe_allow_html=True)
    st.markdown("""<div class='news-card'><div class='news-title'>Global Inflation Trends</div><div class='news-desc'>Consumer price indexes show cooling trends across the EU, leading to speculation of early rate cuts by the European Central Bank.</div></div>""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><p style='text-align: center; color: #555; padding-bottom: 50px;'>Finance Statement Checker v6.0 | Dariya & Amira | Almaty 2026</p>", unsafe_allow_html=True)
