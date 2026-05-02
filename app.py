import streamlit as st
import pandas as pd
import plotly.express as px

# Конфигурация страницы
st.set_page_config(page_title="Finance Statement Checker Pro", layout="wide", page_icon="📈")

# Профессиональный дизайн (Серый, Бордовый, Прозрачность)
st.markdown("""
    <style>
    html { scroll-behavior: smooth; }
    .stApp {
        background: linear-gradient(135deg, #1e1e1e 0%, #2d2d2d 100%);
        color: #e0e0e0;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    .hero-section {
        height: 60vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(5px);
        border-radius: 20px;
        margin: 20px;
        border: 1px solid rgba(128, 0, 32, 0.2);
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    .hero-title { font-size: 4.5rem; font-weight: 800; color: #ffffff; margin-bottom: 0px; letter-spacing: -2px; }
    .hero-subtitle { font-size: 1.4rem; color: #800020; font-weight: 500; margin-top: 10px; }
    .section-container {
        padding: 50px 8%;
        background-color: rgba(38, 38, 38, 0.7);
        backdrop-filter: blur(10px);
        margin: 30px 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.05);
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
    }
    h2 { color: #800020; font-weight: 700; border-bottom: 2px solid rgba(128, 0, 32, 0.3); padding-bottom: 15px; }
    .stNumberInput input { 
        background-color: rgba(51, 51, 51, 0.8) !important; 
        color: white !important; 
        border-radius: 8px !important;
    }
    .stButton>button {
        background-color: #800020;
        color: white;
        border-radius: 8px;
        height: 55px;
        font-weight: 700;
        transition: 0.4s;
    }
    .stButton>button:hover { background-color: #a00028; transform: translateY(-3px); color: white; }
    .author-info {
        display: none;
        position: absolute;
        bottom: 100%;
        left: 50%;
        transform: translateX(-50%);
        background-color: rgba(38, 38, 38, 0.95);
        color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #800020;
        width: 250px;
        z-index: 100;
    }
    .footer-trigger:hover .author-info { display: block; }
    .total-box {
        background-color: rgba(128, 0, 32, 0.1);
        padding: 20px;
        border-radius: 10px;
        border: 1px solid rgba(128, 0, 32, 0.3);
        text-align: center;
        margin-top: 25px;
    }
    .total-value { color: #ffffff; font-size: 2em; font-weight: 800; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
    <div class="hero-section">
        <div class="hero-title">FINANCE STATEMENT CHECKER</div>
        <div class="hero-subtitle">Professional-Grade Audit & Validation Terminal</div>
    </div>
""", unsafe_allow_html=True)

# --- KNOWLEDGE BASE ---
st.markdown("<div class='section-container'>", unsafe_allow_html=True)
st.markdown("## FINANCIAL CONCEPTS")
k1, k2, k3 = st.columns(3)
with k1:
    with st.expander("⚖️ Balance Sheet", expanded=True):
        st.write("A snapshot of assets, liabilities, and equity.")
        st.markdown("[Investopedia Link 🔗](https://www.investopedia.com/terms/b/balancesheet.asp)")
with k2:
    with st.expander("📈 Income Statement"):
        st.write("Reports performance over a period.")
        st.markdown("[Investopedia Link 🔗](https://www.investopedia.com/terms/i/incomestatement.asp)")
with k3:
    with st.expander("💸 Cash Flow"):
        st.write("Tracks movement of cash.")
        st.markdown("[Investopedia Link 🔗](https://www.investopedia.com/terms/c/cashflowstatement.asp)")
st.markdown("</div>", unsafe_allow_html=True)

# --- CHECKER ---
st.markdown("<div class='section-container'>", unsafe_allow_html=True)
st.markdown("## AUDIT TERMINAL")

input_method = st.radio("Input Architecture", ["Manual Entry", "Excel Database"], horizontal=True)

if input_method == "Manual Entry":
    report_type = st.selectbox("Report Type", ["Balance Sheet Audit", "Income Analysis"])
    
    if report_type == "Balance Sheet Audit":
        st.markdown("### Assets")
        ca1, ca2 = st.columns(2)
        with ca1:
            cash = st.number_input("Cash", value=0.0)
            inv = st.number_input("Inventory", value=0.0)
        with ca2:
            ppe = st.number_input("PPE (Fixed Assets)", value=0.0)
            other_a = st.number_input("Other Assets", value=0.0)
        total_a = cash + inv + ppe + other_a
        st.markdown(f"<div class='total-box'>Total Assets: {total_a}</div>", unsafe_allow_html=True)

        st.markdown("### Liabilities & Equity")
        cl1, cl2 = st.columns(2)
        with cl1:
            debt = st.number_input("Total Debt", value=0.0)
            payables = st.number_input("Accounts Payable", value=0.0)
        with cl2:
            equity = st.number_input("Owner's Equity", value=0.0)
        total_le = debt + payables + equity
        st.markdown(f"<div class='total-box'>Total L+E: {total_le}</div>", unsafe_allow_html=True)

        if st.button("RUN AUDIT"):
            if total_a == total_le and total_a != 0:
                st.balloons()
                st.success("Balanced!")
            else:
                st.error("Not Balanced!")
            
            fig = px.bar(x=['Assets', 'L+E'], y=[total_a, total_le], range_y=[0, 10000], color_discrete_sequence=['#800020'])
            st.plotly_chart(fig, use_container_width=True)

    elif report_type == "Income Analysis":
        rev = st.number_input("Total Revenue", value=0.0)
        exp = st.number_input("Total Expenses", value=0.0)
        if st.button("CHECK PROFIT"):
            ni = rev - exp
            st.success(f"Net Income: {ni}")
            st.balloons()
            fig = px.bar(x=['Revenue', 'Expenses', 'Profit'], y=[rev, exp, ni], range_y=[0, 10000], color_discrete_sequence=['#800020'])
            st.plotly_chart(fig, use_container_width=True)

else:
    file = st.file_uploader("Upload .xlsx", type="xlsx")
    if file:
        st.success("File ready for processing.")

st.markdown("</div>", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown(f"""
    <div style='text-align: center; color: #555; position: relative; padding: 50px;' class='footer-trigger'>
        Finance Statement Checker v3.1
        <div style='cursor:pointer; color:#800020;'>[ Created by... ]</div>
        <div class="author-info">
            Naikina Dariya<br> Erik Amira
        </div>
    </div>
""", unsafe_allow_html=True)
