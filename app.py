import streamlit as st
import pandas as pd

# Конфигурация страницы
st.set_page_config(page_title="Professional Financial Suite", layout="centered")

# Кастомный строгий дизайн
st.markdown("""
    <style>
    .stApp { background-color: #fcf8f9; }
    .stButton>button {
        width: 100%; border-radius: 6px; background-color: #d16a8c; color: white;
        height: 48px; font-weight: 500; border: none; transition: 0.3s;
    }
    .stButton>button:hover { background-color: #b55474; transform: translateY(-1px); }
    h1 { color: #4a3b3e; text-align: center; font-family: sans-serif; font-weight: 700; }
    .theory-section {
        background-color: white; padding: 25px; border-radius: 12px;
        border-left: 5px solid #d16a8c; margin-top: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.02);
    }
    .theory-title { color: #d16a8c; font-weight: 700; font-size: 1.2em; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>Financial Analytics Terminal</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8a7a7d; margin-bottom: 30px;'>Audit, Validation & Educational Resources</p>", unsafe_allow_html=True)

# Вкладки для работы
tab_manual, tab_excel = st.tabs(["Manual Entry", "Excel Upload"])

# --- РУЧНОЙ ВВОД ---
with tab_manual:
    report_type = st.selectbox("Select Statement Type", ["Balance Sheet", "Income Statement", "Cash Flow"])
    
    if report_type == "Balance Sheet":
        col1, col2, col3 = st.columns(3)
        with col1: a = st.number_input("Total Assets", key="ma")
        with col2: l = st.number_input("Total Liabilities", key="ml")
        with col3: e = st.number_input("Total Equity", key="me")
        if st.button("Execute Audit", key="ba"):
            if a == (l + e) and a != 0:
                st.balloons()
                st.success(f"Подтверждено: {a} = {l} + {e}")
            elif a == 0: st.warning("Введите данные")
            else: 
                st.toast("Ошибка в расчетах!", icon="⚠️")
                st.error(f"Расхождение: {abs(a-(l+e))}")

    elif report_type == "Income Statement":
        col1, col2, col3 = st.columns(3)
        with col1: rev = st.number_input("Revenue", key="mr")
        with col2: exp = st.number_input("Expenses", key="mex")
        with col3: ni = st.number_input("Net Income", key="mni")
        if st.button("Validate Profit", key="br"):
            if ni == (rev - exp) and rev != 0:
                st.balloons()
                st.success(f"Подтверждено: Чистая прибыль {ni}")
            elif rev == 0: st.warning("Введите данные")
            else: 
                st.toast("Прибыль не сходится!", icon="❌")
                st.error(f"Ошибка: {abs(ni-(rev-exp))}")

    elif report_type == "Cash Flow":
        col1, col2 = st.columns(2)
        with col1: sc = st.number_input("Opening Cash", key="msc")
        with col2: ec = st.number_input("Closing Cash", key="mec")
        o, i, f = st.columns(3)
        with o: op = st.number_input("Operating", key="mo")
        with i: inv = st.number_input("Investing", key="mi")
        with f: fin = st.number_input("Financing", key="mf")
        if st.button("Verify Movement", key="bc"):
            if ec == (sc + op + inv + fin) and ec != 0:
                st.balloons()
                st.success("Движение средств корректно")
            elif ec == 0: st.warning("Введите данные")
            else: 
                st.toast("Денежные потоки не верны", icon="💸")
                st.error("Ошибка сверки остатков")

# --- EXCEL ВВОД ---
with tab_excel:
    uploaded_file = st.file_uploader("Upload .xlsx file", type="xlsx")
    if uploaded_file and st.button("Analyze File"):
        df = pd.read_excel(uploaded_file)
        df.columns = [c.lower().strip() for c in df.columns]
        if 'assets' in df.columns and 'liabilities' in df.columns:
            row = df.iloc[0]
            if row['assets'] == (row['liabilities'] + row['equity']):
                st.balloons()
                st.success("Excel данные верны")
            else: st.toast("Ошибка в файле", icon="📁")

# --- СЕКЦИЯ ОБЪЯСНЕНИЙ (Financial Library) ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #4a3b3e;'>Educational Reference</h2>", unsafe_allow_html=True)
st.markdown("---")

with st.expander("📖 1. What is a Balance Sheet?"):
    st.markdown("""
    <div class='theory-section'>
    <p class='theory-title'>Balance Sheet (Бухгалтерский баланс)</p>
    Это «снимок» финансового состояния компании на конкретную дату. Он показывает, чем компания владеет (Assets) и за счет чего это было куплено (Liabilities + Equity).
    <br><br><b>Основная формула:</b> Assets = Liabilities + Equity
    </div>
    """, unsafe_allow_html=True)

with st.expander("📖 2. What is an Income Statement?"):
    st.markdown("""
    <div class='theory-section'>
    <p class='theory-title'>Income Statement (Отчет о прибылях и убытках)</p>
    Показывает финансовый результат деятельности за период времени. Он демонстрирует, способна ли компания генерировать прибыль.
    <br><br><b>Основная формула:</b> Revenue - Expenses = Net Income
    </div>
    """, unsafe_allow_html=True)

with st.expander("📖 3. What is a Cash Flow Statement?"):
    st.markdown("""
    <div class='theory-section'>
    <p class='theory-title'>Cash Flow (Отчет о движении денежных средств)</p>
    Отслеживает реальный приток и отток «живых» денег. Важен потому, что прибыль в отчете (Net Income) не всегда означает наличие денег на счету.
    <br><br><b>Делится на 3 типа:</b> Operating (основная работа), Investing (покупка оборудования), Financing (кредиты и дивиденды).
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><p style='text-align: center; font-size: 0.75em; color: #a19194;'>Corporate Audit Tool v5.0</p>", unsafe_allow_html=True)
