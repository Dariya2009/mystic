import streamlit as st
import pandas as pd

# Конфигурация страницы
st.set_page_config(page_title="Financial Audit System", layout="centered")

# Строгий дизайн
st.markdown("""
    <style>
    .stApp { background-color: #fcf8f9; }
    .stButton>button {
        width: 100%; border-radius: 6px; background-color: #d16a8c; color: white;
        height: 48px; font-weight: 500; border: none;
    }
    h1 { color: #4a3b3e; text-align: center; font-family: sans-serif; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; font-weight: 600; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>Financial Analytics Terminal</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8a7a7d;'>Professional verification of financial statements</p>", unsafe_allow_html=True)

# Создаем две основные вкладки: Ручной ввод и Excel
tab_manual, tab_excel = st.tabs(["Manual Entry", "Excel Upload"])

# --- ВКЛАДКА: РУЧНОЙ ВВОД ---
with tab_manual:
    report_type = st.selectbox("Select Statement Type", ["Balance Sheet", "Income Statement", "Cash Flow"])
    st.markdown("---")

    if report_type == "Balance Sheet":
        col1, col2, col3 = st.columns(3)
        with col1: a = st.number_input("Total Assets", key="m_a")
        with col2: l = st.number_input("Total Liabilities", key="m_l")
        with col3: e = st.number_input("Total Equity", key="m_e")
        if st.button("Execute Audit", key="btn_a"):
            if a == (l + e) and a != 0:
                st.success(f"Подтверждено: Баланс сошелся ({a} = {l} + {e})")
            else: st.error(f"Ошибка: Расхождение составило {abs(a-(l+e))}")

    elif report_type == "Income Statement":
        col1, col2, col3 = st.columns(3)
        with col1: rev = st.number_input("Revenue", key="m_r")
        with col2: exp = st.number_input("Expenses", key="m_ex")
        with col3: ni = st.number_input("Net Income", key="m_ni")
        if st.button("Validate Profit", key="btn_r"):
            if ni == (rev - exp) and rev != 0:
                st.success(f"Подтверждено: Чистая прибыль верна ({ni})")
            else: st.error(f"Ошибка: Расхождение составило {abs(ni-(rev-exp))}")

    elif report_type == "Cash Flow":
        col1, col2 = st.columns(2)
        with col1: s_c = st.number_input("Opening Cash", key="m_sc")
        with col2: e_c = st.number_input("Closing Cash", key="m_ec")
        o = st.number_input("Operating activities", key="m_o")
        i = st.number_input("Investing activities", key="m_i")
        f = st.number_input("Financing activities", key="m_f")
        if st.button("Verify Movement", key="btn_c"):
            if e_c == (s_c + o + i + f) and e_c != 0:
                st.success("Подтверждено: Движение денежных средств корректно.")
            else: st.error("Ошибка: Остатки не сходятся с движением средств.")

# --- ВКЛАДКА: EXCEL ЗАГРУЗКА ---
with tab_excel:
    st.markdown("### Upload Excel File")
    uploaded_file = st.file_uploader("Choose a file (.xlsx)", type="xlsx")
    
    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        st.write("Data Preview:")
        st.dataframe(df.head(3))
        
        if st.button("Run Audit from Excel"):
            df.columns = [c.lower().strip() for c in df.columns]
            if 'assets' in df.columns and 'liabilities' in df.columns and 'equity' in df.columns:
                row = df.iloc[0]
                a_v, l_v, e_v = row['assets'], row['liabilities'], row['equity']
                if a_v == (l_v + e_v):
                    st.success(f"Excel Audit Success: {a_v} = {l_v} + {e_v}")
                else: st.error(f"Excel Audit Failed: Difference {abs(a_v-(l_v+e_v))}")
            else:
                st.error("Колонки в Excel должны называться: Assets, Liabilities, Equity")

st.markdown("<br><p style='text-align: center; font-size: 0.75em; color: #a19194;'>Corporate Audit Tool v4.1</p>", unsafe_allow_html=True)
