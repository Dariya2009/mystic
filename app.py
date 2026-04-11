import streamlit as st

# Основные настройки страницы
st.set_page_config(page_title="Финансовый Аудитор 3-в-1", page_icon="📊", layout="wide")

# Глобальные стили для всего приложения (шрифты, скругления)
st.markdown("""
    <style>
    /* Общий шрифт и цвет текста */
    html, body, [class*="css"]  {
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        color: #3e2723; /* Темно-коричневый для вежливости */
    }
    /* Заголовки */
    h1, h2, h3 {
        text-align: center;
        font-weight: 700;
    }
    /* Кнопки ввода */
    .stNumberInput div div input {
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Заголовок приложения
st.markdown("# 🛡️ Персональный Финансовый Консультант")
st.markdown("<p style='text-align: center; font-size: 1.2em; color: #6d4c41;'>Автоматическая проверка основных финансовых отчетов</p>", unsafe_allow_html=True)
st.markdown("---")

# СОЗДАНИЕ ВКЛАДОК
tab1, tab2, tab3 = st.tabs(["⚖️ Balance Sheet", "📈 Income Statement", "💸 Cash Flow"])


# --- ВКЛАДКА 1: BALANCE SHEET (Розовая) ---
with tab1:
    # Уникальный стиль для этой вкладки (Розовый фон)
    st.markdown("""
        <style>
        /* Фон только для первой вкладки */
        [data-testid="stAppViewContainer"] {
            background-color: #fdf2f5; /* Очень светлый розовый */
        }
        /* Стиль кнопки на этой вкладке */
        .stButton>button {
            width: 100%; border-radius: 15px; background-color: #d81b60; color: white;
            height: 50px; font-size: 1.1em; font-weight: 500; border: none;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("## Проверка Балансового Уравнения")
    st.markdown("<p style='text-align: center;'>Сверка Активов с Обязательствами и Капиталом 🔍</p>", unsafe_allow_html=True)
    st.markdown("---")

    # Поля ввода с тематическими иконками
    st.markdown("### Введите показатели ⚖️")
    col1, col2, col3 = st.columns(3)

    with col1:
        assets = st.number_input("Total Assets (Активы) 🏦", value=0, key="assets")
    with col2:
        liabilities = st.number_input("Total Liabilities (Обязательства) 💳", value=0, key="liabilities")
    with col3:
        equity = st.number_input("Total Equity (Капитал) 🏢", value=0, key="equity")

    # Логика проверки
    if st.button("Выполнить аудит Баланса ✨", key="btn_balance"):
        if assets == 0 and liabilities == 0 and equity == 0:
            st.info("Пожалуйста, введите значения для проведения анализа. 📝")
        else:
            expected_assets = liabilities + equity
            if assets == expected_assets:
                st.balloons()  # Шарики при успехе!
                st.success(f"""
                *Баланс подтвержден ✅*
                
                Данные указаны верно: Активы ({assets}) равны сумме обязательств ({liabilities}) и капитала ({equity}). 
                Ошибок в расчетах не обнаружено. 👍
                """)
            else:
                difference = abs(assets - expected_assets)
                st.error(f"""
                *Обнаружено расхождение ⚠️*
                
                Разница составляет: *{difference}*. 
                Пожалуйста, проверьте точность данных. Сумма обязательств и капитала должна быть равна активам. 🧐
                """)


# --- ВКЛАДКА 2: INCOME STATEMENT (Желтая) ---
with tab2:
    # Уникальный стиль для этой вкладки (Желтый фон)
    st.markdown("""
        <style>
        /* Смена фона при переключении */
        [data-testid="stAppViewContainer"] {
            background-color: #fffde7; /* Свежий желтый */
        }
        /* Смена цвета кнопки на этой вкладке */
        .stButton>button {
            background-color: #fbc02d; /* Насыщенный желтый */
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("## Проверка Прибылей и Убытков")
    st.markdown("<p style='text-align: center;'>Сверка Выручки, Расходов и Чистой Прибыли 💰</p>", unsafe_allow_html=True)
    st.markdown("---")

    # Поля ввода с тематическими иконками
    st.markdown("### Введите показатели 📊")
    col1, col2, col3 = st.columns(3)

    with col1:
        revenue = st.number_input("Revenue (Выручка) 🛒", value=0, key="revenue")
    with col2:
        expenses = st.number_input("Expenses (Расходы) 📉", value=0, key="expenses")
    with col3:
        net_income_input = st.number_input("Net Income (Чистая прибыль) 💎", value=0, key="net_income")

    # Логика проверки
    if st.button("Проверить Отчет о прибыли ✨", key="btn_income"):
        if revenue == 0 and expenses == 0 and net_income_input == 0:
            st.info("Пожалуйста, введите значения для проверки. 📝")
        else:
            calculated_net_income = revenue - expenses
            if net_income_input == calculated_net_income:
                st.snow()  # Снег при успехе (похоже на конфетти)
                st.success(f"""
                *Расчет прибыли верен ✅*
                
                Данные подтверждены: Выручка ({revenue}) минус Расходы ({expenses}) равны Чистой Прибыли ({net_income_input}). 
                👍 Отличная работа над учетом!
                """)
            else:
                difference = abs(net_income_input - calculated_net_income)
                st.error(f"""
                *Обнаружено несоответствие ⚠️*
                
                Разница составляет: *{difference}*. 
                Рекомендуется перепроверить отчет. Чистая прибыль должна быть равна разнице между выручкой и расходами. 🧐
                """)


# --- ВКЛАДКА 3: CASH FLOW (Голубая) ---
with tab3:
    # Уникальный стиль для этой вкладки (Голубой фон)
    st.markdown("""
        <style>
        /* Смена фона при переключении */
        [data-testid="stAppViewContainer"] {
            background-color: #e3f2fd; /* Светлый голубой */
        }
        /* Смена цвета кнопки на этой вкладке */
        .stButton>button {
            background-color: #1e88e5; /* Яркий голубой */
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("## Мониторинг Движения Средств")
    st.markdown("<p style='text-align: center;'>Сверка остатков денег на начало и конец периода 💸</p>", unsafe_allow_html=True)
    st.markdown("---")

    # Поля ввода с тематическими иконками
    st.markdown("### Введите показатели 🧮")
    col1, col2 = st.columns(2)
    with col1:
        start_cash = st.number_input("Cash at Start (На начало) 🗝️", value=0, key="start_cash")
    with col2:
        end_cash_input = st.number_input("Cash at End (На конец) ✨", value=0, key="end_cash_input")

    st.markdown("### Изменения за период")
    col3, col4, col5 = st.columns(3)
    with col3:
        operating = st.number_input("Operating (От осн. деят.) ⚙️", value=0, key="operating")
    with col4:
        investing = st.number_input("Investing (Инвестиции) 🏗️", value=0, key="investing")
    with col5:
        financing = st.number_input("Financing (Финансирование) 🏦", value=0, key="financing")

    # Логика проверки
    if st.button("Сверить движение средств ✨", key="btn_cash"):
        # Математика Cash Flow: Конец = Начало + (Оп. + Инв. + Фин.)
        total_change = operating + investing + financing
        calculated_end_cash = start_cash + total_change
        
        if total_change == 0 and start_cash == 0 and end_cash_input == 0:
             st.info("Пожалуйста, введите значения для проверки. 📝")
        else:
            if end_cash_input == calculated_end_cash:
                st.balloons() # Шарики при успехе!
                st.success(f"""
                *Движение средств подтверждено ✅*
                
                Конечный остаток ({end_cash_input}) верно рассчитан: Начальный остаток ({start_cash}) плюс сумма всех изменений ({total_change}). 
                👍 Учет денежных средств в полном порядке!
                """)
            else:
                difference = abs(end_cash_input - calculated_end_cash)
                st.error(f"""
                *Обнаружено расхождение денежных средств ⚠️*
                
                Разница составляет: *{difference}*. 
                Пожалуйста, проверьте точность данных. Конечный остаток должен соответствовать начальному остатку плюс сумма всех поступлений и выплат за период. 🧐
                """)


# Футер (подвал) сайта
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 0.8em; color: #888;'>Универсальный финансовый аудитор v2.0 | 2026 📁</p>", unsafe_allow_html=True)
