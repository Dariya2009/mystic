import streamlit as st
import pandas as pd
import plotly.express as px

# Настройки страницы
st.set_page_config(page_title="Financial Analytics Terminal", layout="centered", page_icon="📈")

# Профессиональный дизайн (Строгий розовый + Стекло)
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #fdf2f5 0%, #f7f9fc 100%); }
    .main-block {
        background: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .stButton>button {
        width: 100%; border-radius: 8px; background-color: #d16a8c; color: white;
        height: 50px; font-weight: 700; border: none; transition: 0.3s;
    }
    .stButton>button:hover { background-color: #b55474; transform: translateY(-2px); }
    h1 { color: #4a3b3e; text-align: center; font-weight: 800; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>Financial Audit Terminal</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8a7a7d;'>Professional Statement Verification & Data Visualization</p>", unsafe_allow_html=True)

# Основные вкладки
tab_work, tab_theory = st.tabs(["📊 Analytics Tool", "📘 Knowledge Base"])

with tab_work:
    # Выбор отчета
    report = st.selectbox("Select Report Type", ["Balance Sheet", "Income Statement", "Cash Flow"])
    
    st.markdown("---")
    
    # --- ЛОГИКА ДЛЯ BALANCE SHEET ---
    if report == "Balance Sheet":
        col1, col2, col3 = st.columns(3)
        with col1: a = st.number_input("Total Assets", value=10000.0, step=500.0, key="b1")
        with col2: l = st.number_input("Total Liabilities", value=6000.0, step=500.0, key="b2")
        with col3: e = st.number_input("Total Equity", value=4000.0, step=500.0, key="b3")
        
        if st.button("RUN AUDIT"):
            if a == (l + e):
                st.balloons()
                st.success("Verified: Balance is perfectly aligned.")
            else:
                st.toast("Discrepancy found!", icon="⚠️")
                st.error(f"Variance: {abs(a-(l+e))}")
            
            # График снизу
            df = pd.DataFrame({'Category': ['Assets', 'L + E'], 'Value': [a, (l+e)]})
            fig = px.bar(df, x='Category', y='Value', color='Category', 
                         color_discrete_map={'Assets': '#d16a8c', 'L + E': '#64b5f6'},
                         height=350) # Компактная высота
            st.plotly_chart(fig, use_container_width=True)

    # --- ЛОГИКА ДЛЯ INCOME STATEMENT ---
    elif report == "Income Statement":
        col1, col2, col3 = st.columns(3)
        with col1: rev = st.number_input("Revenue", value=10000.0, step=500.0, key="i1")
        with col2: exp = st.number_input("Expenses", value=7000.0, step=500.0, key="i2")
        with col3: ni = st.number_input("Reported Net Income", value=3000.0, step=500.0, key="i3")
        
        if st.button("VALIDATE PROFIT"):
            calc_ni = rev - exp
            if ni == calc_ni:
                st.balloons()
                st.success(f"Verified: Net Income confirmed at {ni}")
            else:
                st.toast("Calculation error!", icon="❌")
                st.error(f"Variance: {abs(ni-calc_ni)}")
            
            # График снизу
            df = pd.DataFrame({'Component': ['Revenue', 'Expenses', 'Net Income'], 
                               'Amount': [rev, exp, ni]})
            fig = px.bar(df, x='Component', y='Amount', color='Component',
                         color_discrete_sequence=['#ffb3c6', '#fb6f92', '#ff85a2'],
                         height=350)
            st.plotly_chart(fig, use_container_width=True)

    # --- ЛОГИКА ДЛЯ CASH FLOW ---
    elif report == "Cash Flow":
        c1, c2 = st.columns(2)
        with c1: start = st.number_input("Opening Cash", value=5000.0, key="c1")
        with c2: end = st.number_input("Closing Cash", value=8000.0, key="c2")
        
        o, i, f = st.columns(3)
        with o: op = st.number_input("Operating", value=4000.0, key="c3")
        with i: inv = st.number_input("Investing", value=-2000.0, key="c4")
        with f: fin = st.number_input("Financing", value=1000.0, key="c5")
        
        if st.button("VERIFY CASH"):
            calc_end = start + op + inv + fin
            if end == calc_end:
                st.balloons()
                st.success("Verified: Cash movement is correct.")
            else:
                st.error(f"Variance: {abs(end-calc_end)}")
            
            # График снизу
            df = pd.DataFrame({'Stage': ['Start', 'Change', 'End'], 
                               'Cash': [start, (op+inv+fin), end]})
            fig = px.line(df, x='Stage', y='Cash', markers=True, height=350)
            fig.update_traces(line_color='#d16a8c')
            st.plotly_chart(fig, use_container_width=True)

# --- БЛОК ТЕОРИИ (КАРТОЧКИ) ---
with tab_theory:
    st.markdown("<br>", unsafe_allow_html=True)
    c_t1, c_t2, c_t3 = st.columns(3)
    
    with c_t1:
        with st.expander("⚖️ Balance"):
            st.info("Assets = Liabilities + Equity. Shows what the company owns and owes.")
    with c_t2:
        with st.expander("📈 Income"):
            st.info("Revenue - Expenses = Net Income. Shows the profit over a period.")
    with c_t3:
        with st.expander("💸 Cash Flow"):
            st.info("Tracks the actual movement of cash in and out of the business.")

st.markdown("<br><p style='text-align: center; font-size: 0.8em; color: #aaa;'>Luxe Financial Terminal v8.0</p>", unsafe_allow_html=True)
