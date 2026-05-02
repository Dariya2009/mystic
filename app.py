import streamlit as st
import pandas as pd
import plotly.express as px

# Конфигурация страницы
st.set_page_config(page_title="Finance Statement Checker Pro", layout="wide", page_icon="📈")

# Улучшенный CSS
st.markdown("""
    <style>
    html { scroll-behavior: smooth; }
    .stApp { background-color: #121212; color: #ffffff; }
    
    /* Header с кнопками входа */
    .header-bar {
        display: flex; justify-content: flex-end; padding: 10px 5%;
        background: rgba(128, 0, 32, 0.1); border-bottom: 1px solid #800020;
    }
    .auth-btn {
        margin-left: 15px; padding: 8px 20px; border-radius: 5px;
        font-weight: 600; cursor: pointer; transition: 0.3s; border: 1px solid #800020;
    }
    .login-btn { color: #ffffff; background: transparent; }
    .signup-btn { background: #800020; color: white; }
    
    /* Секции с разным фоном */
    .hero-section { background: linear-gradient(180deg, #1e1e1e 0%, #262626 100%); padding: 80px 10%; text-align: center; }
    .knowledge-section { background-color: #f5f5f5; color: #1e1e1e; padding: 60px 10%; }
    .checker-section { background-color: #1e1e1e; padding: 60px 10%; border-top: 5px solid #800020; }
    .news-section { background-color: #121212; padding: 60px 10%; border-top: 1px solid #333; }

    /* Текст */
    .main-title { font-size: 4rem; font-weight: 900; margin-bottom: 10px; color: white; }
    .section-title { font-size: 2.5rem; font-weight: 700; margin-bottom: 30px; }
    .dark-text { color: #2d2d2d; line-height: 1.6; }
    .white-text { color: #ffffff; }

    /* Карточки новостей */
    .news-card {
        background: #262626; padding: 20px; border-radius: 10px;
        border-left: 4px solid #800020; margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 1. ВЕРХНЯЯ ПАНЕЛЬ (AUTH) ---
st.markdown("""
    <div class="header-bar">
        <div class="auth-btn login-btn">Login</div>
        <div class="auth-btn signup-btn">Sign Up</div>
    </div>
""", unsafe_allow_html=True)

# --- 2. ГЛАВНЫЙ ЭКРАН ---
st.markdown("""
    <div class="hero-section">
        <h1 class="main-title">FINANCE STATEMENT CHECKER</h1>
        <p style="font-size: 1.5rem; color: #800020;">Advanced Audit Framework v4.0</p>
        <p style="color: #888;">Designed by Naikina Dariya & Erik Amira</p>
    </div>
""", unsafe_allow_html=True)

# --- 3. БАЗА ЗНАНИЙ (Светлая секция) ---
st.markdown("<div class='knowledge-section'>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title' style='color: #800020;'>Educational Module</h2>", unsafe_allow_html=True)

col_k1, col_k2, col_k3 = st.columns(3)

with col_k1:
    st.markdown("<h3 style='color: #1e1e1e;'>Balance Sheet</h3>", unsafe_allow_html=True)
    st.markdown("<p class='dark-text'>The Balance Sheet is a fundamental financial statement that provides a 'snapshot' of a company’s financial position at a specific point in time. It details assets (what the company owns), liabilities (what it owes), and shareholder's equity (the residual interest).</p>", unsafe_allow_html=True)
    st.image("https://www.investopedia.com/thmb/pX6wR_v7nS8A1vG9jP0uD_E9k5Q=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/BalanceSheet_Final-9426f8b958e0407198114f2e5197825b.png", caption="Balance Sheet Structure")
    st.markdown("[Deep Dive into Balance Sheets 🔗](https://www.investopedia.com/terms/b/balancesheet.asp)")

with col_k2:
    st.markdown("<h3 style='color: #1e1e1e;'>Income Statement</h3>", unsafe_allow_html=True)
    st.markdown("<p class='dark-text'>Also known as the Profit and Loss (P&L) statement, it shows the company’s revenues and expenses during a particular period. It indicates how the revenues are transformed into the net income (the bottom line).</p>", unsafe_allow_html=True)
    st.image("https://www.investopedia.com/thmb/9zG6-X6_O1J7K7Z_7L7_8_8_8_8/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/IncomeStatement_Final-3e7e8e5e5e5e4e4e9e9e9e9e9e9e9e9e.png", caption="Income Statement Flow")
    st.markdown("[Analyze Performance 🔗](https://www.investopedia.com/terms/i/incomestatement.asp)")

with col_k3:
    st.markdown("<h3 style='color: #1e1e1e;'>Cash Flow</h3>", unsafe_allow_html=True)
    st.markdown("<p class='dark-text'>The Cash Flow Statement bridges the gap between the income statement and the balance sheet by showing how much cash is generated and used during a given period across operating, investing, and financing activities.</p>", unsafe_allow_html=True)
    st.image("https://www.investopedia.com/thmb/9zG6-X6_O1J7K7Z_7L7_8_8_8_8/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/CashFlowStatement_Final-3e7e8e5e5e5e4e4e9e9e9e9e9e9e9e9e.png", caption="Cash Flow Categories")
    st.markdown("[Track the Money 🔗](https://www.investopedia.com/terms/c/cashflowstatement.asp)")
st.markdown("</div>", unsafe_allow_html=True)

# --- 4. ЧЕКЕР (Темная секция) ---
st.markdown("<div class='checker-section'>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title'>Audit Terminal</h2>", unsafe_allow_html=True)

mode = st.radio("Select Method", ["Manual Entry", "Excel Upload"], horizontal=True)

if mode == "Manual Entry":
    report = st.selectbox("Report Type", ["Balance Sheet", "Income Statement"])
    
    if report == "Balance Sheet":
        st.markdown("### Assets Analysis")
        # Интерактивная анимация подпунктов
        show_details = st.checkbox("Show Detailed Asset Breakdown")
        
        if show_details:
            c1, c2 = st.columns(2)
            with c1:
                cash = st.number_input("Cash & Equivalents", value=0.0)
                inv = st.number_input("Inventory", value=0.0)
            with c2:
                ppe = st.number_input("Fixed Assets (PPE)", value=0.0)
                other = st.number_input("Other Assets", value=0.0)
            total_a = cash + inv + ppe + other
        else:
            total_a = st.number_input("Total Assets (Simple Entry)", value=0.0)
            
        st.markdown("### Liabilities & Equity")
        l_debt = st.number_input("Total Debt", value=0.0)
        equity = st.number_input("Shareholder Equity", value=0.0)
        total_le = l_debt + equity
        
        if st.button("RUN SYSTEM AUDIT"):
            if total_a == total_le and total_a != 0:
                st.balloons()
                st.success("STATUS: BALANCED")
            else:
                st.error(f"STATUS: DISCREPANCY DETECTED ({abs(total_a-total_le)})")
            
            fig = px.bar(x=['Assets', 'L + E'], y=[total_a, total_le], range_y=[0, 10000], color_discrete_sequence=['#800020'])
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white")
            st.plotly_chart(fig, use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# --- 5. НОВОСТИ ФИНАНСОВ ---
st.markdown("<div class='news-section'>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title'>Global Financial News Feed</h2>", unsafe_allow_html=True)

n_col1, n_col2 = st.columns(2)
with n_col1:
    st.markdown("""<div class='news-card'><h4>FED Interest Rate Decision</h4><p>Markets anticipate a steady rate as inflation shows signs of cooling.</p></div>""", unsafe_allow_html=True)
    st.markdown("""<div class='news-card'><h4>Tech Sector Earnings Report</h4><p>Major AI players report 20% growth in quarterly revenue.</p></div>""", unsafe_allow_html=True)
with n_col2:
    st.markdown("""<div class='news-card'><h4>Emerging Markets Outlook</h4><p>Investment flows increase towards Southeast Asian fintech startups.</p></div>""", unsafe_allow_html=True)
    st.markdown("""<div class='news-card'><h4>Crypto Regulation Update</h4><p>New framework proposed for stablecoin transparency in the EU.</p></div>""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
    <div style='text-align: center; padding: 40px; color: #555;'>
        Finance Statement Checker v4.0 | Created by Naikina Dariya & Erik Amira | 2026
    </div>
""", unsafe_allow_html=True)
