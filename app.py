import streamlit as st
import pandas as pd
import plotly.express as px

# Настройки страницы
st.set_page_config(page_title="Financial Analytics Terminal", layout="centered", page_icon="📈")

# Профессиональный дизайн (Строгий розовый + Стекло)
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #fdf2f5 0%, #f7f9fc 100%); }
    .stButton>button {
        width: 100%; border-radius: 8px; background-color: #d16a8c; color: white;
        height: 50px; font-weight: 700; border: none; transition: 0.3s;
    }
    .stButton>button:hover { background-color: #b55474; transform: translateY(-2px); }
    h1 { color: #4a3b3e; text-align: center; font-weight: 800; }
    .upload-text { text-align: center; color: #8a7a7d; padding: 10px; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>Financial Audit Terminal</h1>", unsafe_allow_html=True)

# ГЛАВНЫЕ ВКЛАДКИ
tab_manual, tab_excel, tab_theory = st.tabs(["📊 Manual Entry", "📂 Excel Upload", "📘 Knowledge Base"])

# --- ВКЛАДКА: РУЧНОЙ ВВОД (С ГРАФИКАМИ) ---
with tab_manual:
    report = st.selectbox("Select Report Type", ["Balance Sheet", "Income Statement", "Cash Flow"], key="main_select")
    st.markdown("---")
    
    if report == "Balance Sheet":
        col1, col2, col3 = st.columns(3)
        with col1: a = st.number_input("Total Assets", value=10000.0, key="b1")
        with col2: l = st.number_input("Total Liabilities", value=6000.0, key="b2")
        with col3: e = st.number_input("Total Equity", value=4000.0, key="b3")
        
        if st.button("RUN BALANCE AUDIT"):
            if a == (l + e) and a != 0:
                st.balloons()
                st.success(f"Verified: Balance perfectly aligned (A = L + E)")
            else:
                st.error(f"Variance: {abs(a-(l+e))}")
            
            # График
            df = pd.DataFrame({'Category': ['Assets', 'L + E'], 'Value': [a, (l+e)]})
            fig = px.bar(df, x='Category', y='Value', color='Category', 
                         color_discrete_map={'Assets': '#d16a8c', 'L + E': '#64b5f6'}, height=350)
            st.plotly_chart(fig, use_container_width=True)

    elif report == "Income Statement":
        col1, col2, col3 = st.columns(3)
        with col1: rev = st.number_input("Revenue", value=12000.0, key="i1")
        with col2: exp = st.number_input("Expenses", value=8000.0, key="i2")
        with col3: ni = st.number_input("Net Income", value=4000.0, key="i3")
        
        if st.button("VALIDATE PROFIT"):
            if ni == (rev - exp):
                st.balloons()
                st.success(f"Verified: Profitability confirmed.")
            else:
                st.error(f"Variance: {abs(ni-(rev-exp))}")
            
            df = pd.DataFrame({'Component': ['Revenue', 'Expenses', 'Net Income'], 'Amount': [rev, exp, ni]})
            fig = px.bar(df, x='Component', y='Amount', color='Component', height=350)
            st.plotly_chart(fig, use_container_width=True)

    elif report == "Cash Flow":
        c1, c2 = st.columns(2)
        with c1: start = st.number_input("Opening Cash", value=5000.0, key="c1")
        with c2: end = st.number_input("Closing Cash", value=8000.0, key="c2")
        o, i, f = st.columns(3)
        with o: op = st.number_input("Operating", value=4000.0, key="c3")
        with i: inv = st.number_input("Investing", value=-2000.0, key="c4")
        with f: fin = st.number_input("Financing", value=1000.0, key="c5")
        
        if st.button("VERIFY CASH"):
            if end == (start + op + inv + fin):
                st.balloons()
                st.success("Verified: Cash flow is correct.")
            else:
                st.error("Error in cash movement.")
            
            df = pd.DataFrame({'Stage': ['Start', 'Change', 'End'], 'Cash': [start, (op+inv+fin), end]})
            fig = px.line(df, x='Stage', y='Cash', markers=True, height=350)
            st.plotly_chart(fig, use_container_width=True)

# --- ВКЛАДКА: EXCEL (ВОЗВРАЩЕНА!) ---
with tab_excel:
    st.markdown("<div class='upload-text'><h3>Drop your Excel report here</h3><p>Ensure columns are named: Assets, Liabilities, Equity</p></div>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload .xlsx file", type="xlsx", label_visibility="collapsed")
    
    if uploaded_file:
        df_xl = pd.read_excel(uploaded_file)
        st.write("Data Preview:")
        st.dataframe(df_xl.head(3))
        
        if st.button("RUN EXCEL AUDIT"):
            df_xl.columns = [c.lower().strip() for c in df_xl.columns]
            if 'assets' in df_xl.columns and 'liabilities' in df_xl.columns:
                row = df_xl.iloc[0]
                if row['assets'] == (row['liabilities'] + row['equity']):
                    st.balloons()
                    st.success("Excel verification successful!")
                else:
                    st.error("Discrepancy in Excel data.")
            else:
                st.warning("Please check column names in your file.")

# --- ВКЛАДКА: ТЕОРИЯ ---
with tab_theory:
    st.markdown("<br>", unsafe_allow_html=True)
    col_t1, col_t2, col_t3 = st.columns(3)
    with col_t1:
        with st.expander("⚖️ Balance"):
            st.write("Assets = Liabilities + Equity. Snapshot of what the company owns.")
    with col_t2:
        with st.expander("📈 Income"):
            st.write("Revenue - Expenses = Net Income. Measures performance over time.")
    with col_t3:
        with st.expander("💸 Cash Flow"):
            st.write("Tracks the actual flow of cash in and out of the entity.")

st.markdown("<br><p style='text-align: center; font-size: 0.8em; color: #aaa;'>Luxe Financial Terminal v9.0</p>", unsafe_allow_html=True)
