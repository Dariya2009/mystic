import streamlit as st
import pandas as pd

# Конфигурация страницы
st.set_page_config(page_title="Financial Audit Professional", layout="centered")

# Строгий стиль
st.markdown("""
    <style>
    .stApp { background-color: #fcf8f9; }
    .stButton>button {
        width: 100%; border-radius: 6px; background-color: #d16a8c; color: white;
        height: 48px; font-weight: 500; border: none;
    }
    .upload-box {
        border: 2px dashed #d16a8c; padding: 20px; border-radius: 10px; text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>Financial Analytics Terminal</h1>", unsafe_allow_html=True)

# Выбор способа ввода
input_method = st.radio("Select Input Method", ["Manual Entry", "Excel Upload"])

st.markdown("---")

if input_method == "Excel Upload":
    st.markdown("### Excel Data Import")
    uploaded_file = st.file_uploader("Choose an Excel file (.xlsx)", type="xlsx")

    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            st.write("Preview of your data:")
            st.dataframe(df.head(3)) # Показываем первые 3 строки

            if st.button("Run Audit from File"):
                # Пример логики для Balance Sheet (ищем колонки по названиям)
                # Приводим названия колонок к нижнему регистру для удобства поиска
                df.columns = [c.lower().strip() for c in df.columns]
                
                if 'assets' in df.columns and 'liabilities' in df.columns and 'equity' in df.columns:
                    # Берем первую строку данных
                    row = df.iloc[0]
                    a, l, e = row['assets'], row['liabilities'], row['equity']
                    
                    if a == (l + e):
                        st.success(f"Audit Successful: Assets ({a}) = Liabilities ({l}) + Equity ({e})")
                    else:
                        st.error(f"Audit Failed: Variance detected. Difference: {abs(a-(l+e))}")
                else:
                    st.error("Ошибка: В файле должны быть колонки с заголовками 'Assets', 'Liabilities' и 'Equity'.")
        except Exception as e:
            st.error(f"Ошибка при чтении файла: {e}")

else:
    # Здесь остается ваш старый код для ручного ввода
    report_type = st.selectbox("Select Statement", ["Balance Sheet", "Income Statement", "Cash Flow"])
    # ... (логика ручного ввода из предыдущего сообщения)
    st.info("Используйте ручной ввод или переключитесь на Excel Upload сверху.")

st.markdown("<br><p style='text-align: center; font-size: 0.75em; color: #a19194;'>Corporate Audit Tool v4.0</p>", unsafe_allow_html=True)
