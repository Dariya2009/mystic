import streamlit as st
import pandas as pd

# Конфигурация страницы
st.set_page_config(page_title="Corporate Finance Terminal", layout="centered")

# Навороченный CSS для стиля "Реальный сайт"
st.markdown("""
    <style>
    .stApp { background-color: #fcf8f9; }
    
    /* Основные кнопки действий */
    .stButton>button {
        width: 100%; border-radius: 8px; background-color: #d16a8c; color: white;
        height: 50px; font-weight: 600; border: none; transition: 0.3s;
        box-shadow: 0 4px 6px rgba(209, 106, 140, 0.2);
    }
    .stButton>button:hover { background-color: #b55474; transform: translateY(-2px); }

    /* Карточки для теории (имитация кнопок) */
    .theory-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #f0e0e5;
        margin-bottom: 15px;
        transition: 0.3s;
        cursor: pointer;
    }
    .theory-card:hover {
        border-color: #d16a8c;
        box-shadow: 0 10px 20px rgba(209, 106, 140, 0.1);
    }
    
    .card-title {
        color: #d16a8c;
        font-weight: 700;
        font-size: 1.1em;
        margin-bottom: 5px;
    }
    
    h1 { color: #4a3b3e; text-align: center; font-weight: 800; letter-spacing: -1px; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>Financial Audit Terminal</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8a7a7d; margin-bottom: 40px;'>Professional Accounting & Data Validation Tool</p>", unsafe_allow_html=True)

# РАБОЧАЯ ЗОНА (ВКЛАДКИ)
tab_manual, tab_excel = st.tabs(["📊 Manual Data Entry", "📂 Excel Data Import"])

with tab_manual:
    report_type = st.selectbox("Select Financial Statement", ["Balance Sheet", "Income Statement", "Cash Flow"])
    
    if report_type == "Balance Sheet":
        col1, col2, col3 = st.columns(3)
        with col1: a = st.number_input("Total Assets", key="ma")
        with col2: l = st.number_input("Total Liabilities", key="ml")
        with col3: e = st.number_input("Total Equity", key="me")
        if st.button("RUN BALANCE AUDIT", key="ba"):
            if a == (l + e) and a != 0:
                st.balloons()
                st.success(f"Verified: Assets ({a}) match Liabilities + Equity.")
            elif a == 0: st.warning("Please enter numerical values.")
            else: 
                st.toast("Discrepancy detected!", icon="⚠️")
                st.error(f"Variance: {abs(a-(l+e))}")

    elif report_type == "Income Statement":
        col1, col2, col3 = st.columns(3)
        with col1: rev = st.number_input("Revenue", key="mr")
        with col2: exp = st.number_input("Operating Expenses", key="mex")
        with col3: ni = st.number_input("Reported Net Income", key="mni")
        if st.button("VALIDATE PROFITABILITY", key="br"):
            if ni == (rev - exp) and rev != 0:
                st.balloons()
                st.success(f"Verified: Net Income confirmed at {ni}.")
            elif rev == 0: st.warning("Please enter numerical values.")
            else: 
                st.toast("Profit mismatch!", icon="❌")
                st.error(f"Calculation Error: {abs(ni-(rev-exp))}")

    elif report_type == "Cash Flow":
        col1, col2 = st.columns(2)
        with col1: sc = st.number_input("Opening Cash", key="msc")
        with col2: ec = st.number_input("Closing Cash", key="mec")
        o, i, f = st.columns(3)
        with o: op = st.number_input("Operating activities", key="mo")
        with i: inv = st.number_input("Investing activities", key="mi")
        with f: fin = st.number_input("Financing activities", key="mf")
        if st.button("VERIFY CASH FLOW", key="bc"):
            if ec == (sc + op + inv + fin) and ec != 0:
                st.balloons()
                st.success("Verified: Cash flow balances are correct.")
            elif ec == 0: st.warning("Please enter numerical values.")
            else: 
                st.toast("Cash mismatch!", icon="💸")
                st.error("Error: Closing balance does not match activities.")

with tab_excel:
    uploaded_file = st.file_uploader("Drop your .xlsx report here", type="xlsx")
    if uploaded_file and st.button("PROCESS EXCEL FILE"):
        try:
            df = pd.read_excel(uploaded_file)
            st.success("File uploaded successfully. Analyzing...")
            st.balloons()
        except: st.toast("Invalid file format", icon="📁")

# --- СЕКЦИЯ: FINANCIAL LIBRARY (В ВИДЕ КАРТОЧЕК-КНОПОК) ---
st.markdown("<br><br><h2 style='text-align: center; color: #4a3b3e;'>Knowledge Base</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #a19194;'>Click to explore financial definitions</p>", unsafe_allow_html=True)

# Используем колонки для "плиточного" дизайна кнопок
col_lib1, col_lib2, col_lib3 = st.columns(3)

with col_lib1:
    with st.expander("📘 Balance Sheet"):
        st.markdown("""
        <div class="theory-card">
            <div class="card-title">Assets = L + E</div>
            <p style='font-size: 0.9em; color: #635155;'>
            Снимок финансового состояния. Показывает, что у компании есть и кому она за это должна.
            </p>
        </div>
        """, unsafe_allow_html=True)

with col_lib2:
    with st.expander("📙 Income Statement"):
        st.markdown("""
        <div class="theory-card">
            <div class="card-title">Rev - Exp = NI</div>
            <p style='font-size: 0.9em; color: #635155;'>
            Отчет о прибылях и убытках. Демонстрирует эффективность бизнеса за период.
            </p>
        </div>
        """, unsafe_allow_html=True)

with col_lib3:
    with st.expander("📗 Cash Flow"):
        st.markdown("""
        <div class="theory-card">
            <div class="card-title">Cash Movement</div>
            <p style='font-size: 0.9em; color: #635155;'>
            Реальное движение денег. Показывает, откуда пришли деньги и куда ушли.
            </p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><br><p style='text-align: center; font-size: 0.75em; color: #a19194;'>Corporate Audit Tool v6.0 | Professional Edition</p>", unsafe_allow_html=True)
