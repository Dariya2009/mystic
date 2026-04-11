import streamlit as st

# Настройки оформления страницы
st.set_page_config(page_title="Финансовый аудитор", page_icon="📉")

st.markdown("""
    <style>
    .stApp { background-color: #fdf2f5; } 
    h1, h2, h3, p, span, label { color: #5d4037 !important; font-family: 'Segoe UI', sans-serif; }
    h1 { text-align: center; font-size: 2.5em !important; }
    .stButton>button {
        width: 100%; border-radius: 12px; background-color: #d81b60; color: white;
        height: 50px; font-size: 1.1em; font-weight: 500; border: none;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("# Проверка финансового баланса 📊")
st.markdown("<p style='text-align: center;'>Автоматизированная сверка активов, обязательств и капитала 🔍</p>", unsafe_allow_html=True)

st.markdown("---")

# Поля ввода данных
st.markdown("### Введите данные отчета 👇")
col1, col2, col3 = st.columns(3)

with col1:
    assets = st.number_input("Активы 💰", value=0)
with col2:
    debts = st.number_input("Обязательства 💳", value=0)
with col3:
    equity = st.number_input("Капитал 🏢", value=0)

if st.button("Выполнить анализ ✨"):
    if assets == 0 and debts == 0 and equity == 0:
        st.info("Пожалуйста, введите значения для проверки. 📝")
    else:
        # Проверка балансового равенства
        expected_assets = debts + equity
        if assets == expected_assets:
            # ВОТ ЗДЕСЬ МЫ ВОЗВРАЩАЕМ ПРАЗДНИК:
            st.balloons()  # Полетят шарики
            
            st.success(f"""
            *Баланс подтвержден ✅*
            
            Расчеты верны: сумма активов ({assets}) соответствует сумме обязательств ({debts}) и капитала ({equity}). 
            Ошибок не обнаружено. 👍
            """)
        else:
            difference = abs(assets - expected_assets)
            st.error(f"""
            *Обнаружено расхождение ⚠️*
            
            Разница составляет: *{difference}*. 
            Рекомендуется проверить точность данных. Сумма обязательств и капитала должна быть равна активам. 🧐
            """)

st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 0.8em; color: #888;'>Система финансовой отчетности | 2026 📁</p>", unsafe_allow_html=True)