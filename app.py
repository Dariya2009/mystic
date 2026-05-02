import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Настройка страницы
st.set_page_config(page_title="Finance Statement Checker Pro", layout="wide", page_icon="📈")

# 2. Весь CSS (Стили)
st.markdown("""
    <style>
    html { scroll-behavior: smooth; }
    .stApp { background-color: #0e1117; color: #ffffff; }
    
    /* Кнопки входа */
    .header-bar {
        display: flex; justify-content: flex-end; padding: 20px 5%;
        background: #161b22; border-bottom: 2px solid #800020;
    }
    .auth-btn {
        margin-left: 15px; padding: 10px 30px; border-radius: 5px;
        font-weight: 700; cursor: pointer; border: 2px solid #800020;
    }
    .signup-btn { background: #800020; color: white; }
    
    /* Секции */
    .hero-section { background: #0e1117; padding: 80px 10%; text-align: center; }
    .knowledge-section { background-color: #161b22; padding: 80px 10%; border-radius: 50px 50px 0 0; }
    .checker-section { background-color: #0e1117; padding: 80px 10%; border-top: 5px solid #800020; }
    .contact-section { background-color: #161b22; padding: 60px 10%; border-top: 1px solid #333; }

    /* Текст */
    .white-text { color: #ffffff !important; line-height: 1.8; }
    .section-title { color: #800020; font-size: 3rem; font-weight: 800; margin-bottom: 30px; }
    
    /* Ссылки-кнопки */
    .custom-link {
        display: inline-block; margin-top: 15px; padding: 10px 25px;
        background-color: #800020; color: white !important;
        text-decoration: none; border-radius: 5px; font-weight: 600;
    }
    
    .news-card {
        background: #1c2128; padding: 20px; border-radius: 12px;
        border-left: 6px solid #800020; margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. HEADER ---
st.markdown("""
    <div class="header-bar">
        <div class="auth-btn" style="color: white;">LOG IN</div>
        <div class="auth-btn signup-btn">SIGN UP</div>
    </div>
""", unsafe_allow_html=True)

# --- 4. HERO ---
st.markdown("""
    <div class="hero-section">
        <h1 style="font-size: 5rem; font-weight: 900; color: #ffffff;">FINANCE STATEMENT CHECKER</h1>
        <p style="font-size: 1.8rem; color: #800020; font-weight: 800;">ELITE AUDIT PLATFORM</p>
    </div>
""", unsafe_allow_html=True)

# --- 5. EDUCATION ---
st.markdown("<div class='knowledge-section'>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title'>Financial Education</h2>", unsafe_allow_html=True)

with st.expander("📊 BALANCE SHEET DETAILS"):
    st.markdown("""
    <div class='white-text'>
    The Balance Sheet reveals a company's net worth. Formula: <b>Assets = Liabilities + Equity</b>.
    It is used to check liquidity and financial stability.<br>
    <a href="https://www.investopedia.com/terms/b/balancesheet.asp" class="custom-link">Read Full Article</a>
    </div>
    """, unsafe_allow_html=True)

with st.expander("📈 INCOME STATEMENT DETAILS"):
    st.markdown("""
    <div class='white-text'>
    Tracks <b>Revenue</b> and <b>Expenses</b>. The final goal is to calculate Net Income. 
    It shows the operational efficiency of the business.<br>
    <a href="https://www.investopedia.com/terms/i/incomestatement.asp" class="custom-link">Read Full Article</a>
    </div>
    """, unsafe_allow_html=True)

with st.expander("💸 CASH FLOW DETAILS"):
    st.markdown("""
    <div class='white-text'>
    Shows how much <b>physical cash</b> is moving. Important because profit doesn't always equal cash.
    Includes Operating, Investing, and Financing activities.<br>
    <a href="https://www.investopedia.com/terms/c/cashflowstatement.asp" class="custom-link">Read Full Article</a>
    </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- 6. CHECKER ---
st.markdown("<div class='checker-section'>", unsafe_allow_html=True)
st.markdown("<h2 style='color: white;'>Audit Terminal</h2>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Manual Input", "Excel Upload"])
with tab1:
    report = st.selectbox("Choose Report", ["Balance Sheet", "Income Statement"])
    if report == "Balance Sheet":
        col1, col2 = st.columns(2)
        with col1: a = st.number_input("Total Assets", 0.0)
        with col2: le = st.number_input("Liabilities + Equity", 0.0)
        if st.button("RUN CHECK"):
            if a == le and a > 0:
                st.balloons()
                st.success("Balanced!")
            else: st.error("Error in Balance!")
            fig = px.bar(x=['Assets', 'L+E'], y=[a, le], range_y=[0, 10000], color_discrete_sequence=['#800020'])
            st.plotly_chart(fig)
st.markdown("</div>", unsafe_allow_html=True)

# --- 7. NEWS ---
st.markdown("<div style='padding: 60px 10%;'>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title'>Live News Feed</h2>", unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    st.markdown("<div class='news-card'><h4>Market Trends 2026</h4><p class='white-text'>Global markets show 5% growth in fintech sector.</p></div>", unsafe_allow_html=True)
with c2:
    st.markdown("<div class='news-card'><h4>Crypto Regulation</h4><p class='white-text'>New audit standards for digital assets implemented.</p></div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- 8. CONTACTS & REVIEWS ---
st.markdown("<div class='contact-section'>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title'>Contact Information</h2>", unsafe_allow_html=True)
col_c1, col_c2, col_c3 = st.columns(3)

with col_c1:
    st.markdown("### Developers")
    st.markdown("<p class='white-text'>• Naikina Dariya<br>• Erik Amira</p>", unsafe_allow_html=True)

with col_c2:
    st.markdown("### Support")
    st.markdown("<p class='white-text'>Email: support@finchecker.kz<br>Location: Almaty, Kazakhstan</p>", unsafe_allow_html=True)

with col_c3:
    st.markdown("### User Feedback")
    st.markdown("<p class='white-text'>Check our reputation on global platforms:</p>", unsafe_allow_html=True)
    # Ссылка на сайт с отзывами
    st.markdown('<a href="https://www.trustpilot.com" target="_blank" class="custom-link">View Reviews ⭐️</a>', unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; padding: 40px; color: #444;'>©️ 2026 Finance Checker Pro. All rights reserved.</p>", unsafe_allow_html=True)
