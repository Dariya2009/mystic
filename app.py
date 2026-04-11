import streamlit as st

# Основные настройки страницы
st.set_page_config(page_title="Financial Auditor 🎀", page_icon="🌸", layout="wide")

# Выбор типа отчета (вверху страницы)
tabs = ["⚖️ Balance Sheet", "📈 Income Statement", "💸 Cash Flow"]
selected_tab = st.radio("Select Report Type: ✨", tabs, horizontal=True)

# ЛОГИКА СМЕНЫ ЦВЕТОВ
if selected_tab == "⚖️ Balance Sheet":
    bg_color = "#fdf2f5"  # Нежно-розовый 🌷
    btn_color = "#ff85a2" # Розовый лепесток
elif selected_tab == "📈 Income Statement":
    bg_color = "#fffde7"  # Солнечно-желтый ✨
    btn_color = "#ffd54f" # Золотистый
else:
    bg_color = "#e3f2fd"  # Небесно-голубой ☁️
    btn_color = "#64b5f6" # Голубой колокольчик

# Применяем стили динамически
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {bg_color};
    }}
    .stButton>button {{
        width: 100%; border-radius: 20px; background-color: {btn_color}; color: white;
        height: 55px; font-size: 1.2em; font-weight: 500; border: none;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    }}
    h1, h2, h3, p, span, label {{ color: #5d4037 !important; font-family: 'Segoe UI', sans-serif; }}
    </style>
""", unsafe_allow_html=True)

st.markdown(f"# {selected_tab} ✨🎀")
st.markdown("---")

# --- ЛОГИКА ВКЛАДОК ---

if selected_tab == "⚖️ Balance Sheet":
    st.markdown("### Enter Financial Data 👇 🌸")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        assets = st.number_input("Total Assets 🏦 ✨", value=0)
    with col2:
        liabilities = st.number_input("Total Liabilities 💳 🎀", value=0)
    with col3:
        equity = st.number_input("Total Equity 🏢 🕊️", value=0)

    if st.button("Run Audit ✨💖"):
        if assets == 0 and liabilities == 0 and equity == 0:
            st.info("Милая, пожалуйста, введи данные для проверки! 📝🌸")
        elif assets == (liabilities + equity):
            st.balloons()
            st.success(f"*Баланс подтвержден! ✅ ✨* \n\nВсё идеально: Активы ({assets}) равны обязательствам и капиталу. Ты молодец! 🌸🎀")
        else:
            diff = abs(assets - (liabilities + equity))
            st.error(f"*Ой, обнаружено расхождение ⚠️ 🌸* \n\nРазница составляет: {diff}. Пожалуйста, проверь цифры еще раз, солнышко! 🧐✨")

elif selected_tab == "📈 Income Statement":
    st.markdown("### Enter Profit & Loss Data 👇 🌻")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        revenue = st.number_input("Revenue 🛒 ✨", value=0)
    with col2:
        expenses = st.number_input("Expenses 📉 🍃", value=0)
    with col3:
        net_income = st.number_input("Net Income 💎 🍯", value=0)

    if st.button("Analyze Income ✨💛"):
        if revenue == 0 and expenses == 0 and net_income == 0:
            st.info("Пожалуйста, заполни поля для проверки прибыли! 📝✨")
        elif net_income == (revenue - expenses):
            st.snow()
            st.success(f"*Расчет прибыли верен! ✅ 🍯* \n\nВыручка ({revenue}) минус Расходы ({expenses}) в точности равны Чистой Прибыли ({net_income}). Прекрасная работа! 🌻✨")
        else:
            diff = abs(net_income - (revenue - expenses))
            st.error(f"*Кажется, в отчете ошибка ⚠️ ✨* \n\nРазница: {diff}. Давай перепроверим доходы и расходы? 🧐🐝")

elif selected_tab == "💸 Cash Flow":
    st.markdown("### Enter Cash Flow Data 👇 🧊")
    col1, col2 = st.columns(2)
    with col1:
        start_cash = st.number_input("Cash at Beginning 🗝️ ✨", value=0)
    with col2:
        end_cash = st.number_input("Cash at End 🌊 💎", value=0)

    st.markdown("#### Changes during period 🫧")
    c1, c2, c3 = st.columns(3)
    with c1:
        op = st.number_input("Operating ⚙️ ✨", value=0)
    with c2:
        inv = st.number_input("Investing 🏗️ ☁️", value=0)
    with c3:
        fin = st.number_input("Financing 🏦 ❄️", value=0)

    if st.button("Verify Cash ✨💙"):
        total_change = op + inv + fin
        calculated_end = start_cash + total_change
        if start_cash == 0 and end_cash == 0 and total_change == 0:
            st.info("Пожалуйста, введи данные о движении денежных средств! 📝❄️")
        elif end_cash == calculated_end:
            st.balloons()
            st.success(f"*Движение средств подтверждено! ✅ 🌊* \n\nКонечный остаток ({end_cash}) рассчитан абсолютно верно. Твой учет безупречен! 💎✨")
        else:
            diff = abs(end_cash - calculated_end)
            st.error(f"*Найдено расхождение в остатках ⚠️ ❄️* \n\nРазница: {diff}. Нужно проверить движение средств еще раз! 🧐☁️")

st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 0.8em; color: #888;'>Financial Audit System with Love 🌸 | 2026 📁</p>", unsafe_allow_html=True)
