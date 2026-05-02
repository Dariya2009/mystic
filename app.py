import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Конфигурация страницы
st.set_page_config(page_title="Finance Statement Checker Pro", layout="wide", page_icon="📈")

# 2. Улучшенные стили (CSS) - Все идеально настроено
st.markdown("""
    <style>
    html { scroll-behavior: smooth; }
    .stApp { background-color: #0e1117; color: #ffffff; }
    
    /* Верхняя панель */
    .header-bar {
        display: flex; justify-content: flex-end; padding: 20px 5%;
        background: #161b22; border-bottom: 2px solid #800020;
    }
    .auth-btn {
        margin-left: 15px; padding: 10px 30px; border-radius: 5px;
        font-weight: 700; cursor: pointer; border: 2px solid #800020; color: white;
    }
    .signup-btn { background: #800020; color: white; }
    
    /* Секции */
    .hero-section { background: #0e1117; padding: 80px 10%; text-align: center; }
    .knowledge-section { background-color: #161b22; padding: 80px 10%; border-radius: 50px 50px 0 0; }
    .checker-section { background-color: #0e1117; padding: 80px 10%; border-top: 5px solid #800020; }
    .contact-section { background-color: #161b22; padding: 60px 10%; border-top: 1px solid #333; }

    /* Текст */
    .white-text-box { color: #ffffff !important; line-height: 1.8; font-size: 1.1rem; margin-bottom: 20px; }
    .section-title { color: #800020; font-size: 3rem; font-weight: 800; margin-bottom: 30px; }
    
    /* Ссылки-кнопки */
    .custom-link {
        display: inline-block; margin-top: 15px; padding: 10px 25px;
        background-color: #800020; color: white !important;
        text-decoration: none; border-radius: 5px; font-weight: 600;
        transition: 0.3s;
    }
    .custom-link:hover { background-color: #a00028; transform: translateY(-2px); }
    
    .news-card {
        background: #1c2128; padding: 25px; border-radius: 12px;
        border-left: 6px solid #800020; margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. HEADER ---
st.markdown("""
    <div class="header-bar">
        <div class="auth-btn">LOG IN</div>
        <div class="auth-btn signup-btn">SIGN UP</div>
    </div>
""", unsafe_allow_html=True)

# --- 4. HERO ---
st.markdown("""
    <div class="hero-section">
        <h1 style="font-size: 5rem; font-weight: 900; color: #ffffff; letter-spacing: -2px;">FINANCE STATEMENT CHECKER</h1>
        <p style="font-size: 1.8rem; color: #800020; font-weight: 800;">ELITE AUDIT & VERIFICATION TERMINAL</p>
        <p style="color: #ffffff; font-size: 1.2rem; opacity: 0.8;">System Architecture by: <b>Naikina Dariya & Erik Amira</b></p>
    </div>
""", unsafe_allow_html=True)

# --- 5. EDUCATION ---
st.markdown("<div class='knowledge-section'>", unsafe_allow_html
