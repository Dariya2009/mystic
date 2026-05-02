import streamlit as st
import pandas as pd
import plotly.express as px

# Конфигурация страницы
st.set_page_config(page_title="Finance Statement Checker Pro", layout="wide", page_icon="📈")

# Стилизация: Полный Dark Premium Mode
st.markdown("""
    <style>
    html { scroll-behavior: smooth; }
    .stApp { background-color: #0e1117; color: #ffffff; }
    
    /* Header с кнопками */
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
    .hero-section { background: #0e1117; padding: 80px 10%; text-align: center; }
    .knowledge-section { background-color: #161b22; color: #ffffff !important; padding: 80px 10%; border-radius: 50px 50px 0 0; }
    .checker-section { background-color: #0e1117; padding: 80px 10%; border-top: 5px solid #800020; }
    .news-section { background-color: #161b22; padding: 80px 10%; }

    /* Текст и Контейнеры */
    .white-text-box { color: #ffffff !important; line-height: 1.8; font-size: 1.1rem; }
    .stExpander { background-color: #1c2128 !important; border: 1px solid #333 !important; border-radius: 10px !important; }
    
    /* Стилизация ссылок */
    .edu-link {
        display: inline-block;
        margin-top: 15px;
        padding: 8px 20px;
        background-color: #800020;
        color: white !important;
        text-decoration: none;
        border-radius: 5px;
        font-weight: 600;
        transition: 0.3s;
    }
    .edu-link:hover { background-color: #a00028; transform: translateY(-2px); }

    .news-card {
        background: #0e1117; padding: 25px; border-radius: 12px;
        border-left: 6px solid #800020; margin-bottom: 25px;
    }
    .news-title { color: #ffffff; font-weight: 800; font-size: 1.3rem; }
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
        <h1 style="font-size: 5rem; font-weight: 900; color: #ffffff; letter-spacing: -2px;">FINANCE STATEMENT CHECKER</h1>
        <p style="font-size: 1.8rem; color: #800020; font-weight: 800;">ELITE DATA VERIFICATION PLATFORM</p>
        <p style="color: #ffffff; font-size: 1.3rem; opacity: 0.9;">System Architecture by: <b>Naikina Dariya & Erik Amira</b></p>
    </div>
""", unsafe_allow_html=True)

# --- KNOWLEDGE BASE (С ссылками) ---
st.markdown("<div class='knowledge-section'>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #800020; font-size: 3rem; font-weight: 800;'>Professional Financial Education</h2>", unsafe_allow_html=True)

with st.expander("📊 DETAILED ANALYSIS: THE BALANCE SHEET"):
    st.markdown("""
    <div class="white-text-box">
    The <b>Balance Sheet</b> is a financial statement that reports a company's assets, liabilities, and shareholder equity at a specific point in time. It provides a basis for computing rates of return and evaluating its capital structure.<br><br>
    <b>Core Balance:</b> Assets = Liabilities + Equity.<br><br>
    - <b>Liquidity Focus:</b> Shows if the company has enough short-term assets to cover its immediate debts.<br>
    - <b>Solvency Focus:</b> Analyzes long-term debt levels against total equity.<br>
    <a href="https://www.investopedia.com/terms/b/balancesheet.asp" target="_blank" class="edu-link">Explore Detailed Guide 🔗</a>
    </div>
    """, unsafe_allow_html=True)

with st.expander("📈 DETAILED ANALYSIS: THE INCOME STATEMENT"):
    st.markdown("""
    <div class="white-text-box">
    The <b>Income Statement</b> tracks a company’s financial performance over a specific period. It is primarily focused on the company’s revenues and expenses.<br><br>
    - <b>Operating Performance:</b> Evaluates how efficiently a company turns revenue into profit.<br>
    - <b>EPS Analysis:</b> Provides the basis for Earnings Per Share, a key metric for stock market investors.<br><br>
    Understanding the margins (Gross, Operating, and Net) is essential for competitive benchmarking.<br>
    <a href="
