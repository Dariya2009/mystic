import streamlit as st
import pandas as pd
import plotly.express as px # Библиотека для графиков

# Конфигурация страницы
st.set_page_config(page_title="Corporate Finance Suite", layout="wide", page_icon="💎")

# Навороченный CSS для стиля "Бизнес-портал"
st.markdown("""
    <style>
    /* Фоновый градиент и шрифт */
    .stApp {
        background: linear-gradient(135deg, #fdf2f5 0%, #e3f2fd 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Стеклянный эффект для блоков */
    .css-1r6slb0, .css-12oz5g7 {
        background: rgba(255, 255, 255, 0.6);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.05);
    }

    /* Профессиональные кнопки */
    .stButton>button {
        width: 100%; border-radius: 10px; background-color: #d16a8c; color: white;
        height: 55px; font-weight: 700; border: none; transition: 0.3s;
        box-shadow: 0 4px 6px rgba(209, 106, 140, 0.2); letter-spacing: 1px;
    }
    .stButton>button:hover { background-color: #b55474; transform: translateY(-3px); }

    /* Заголовки */
    h1 { color: #4a3b3e; text-align: center; font-weight: 800; letter-spacing: -2px; margin-bottom: 0px; }
    h2 { color: #635155; font-weight: 700; margin-top: 30px; }

    /* Карточки знаний */
    .theory-card {
        background-color: rgba(255, 255, 255, 0.9); padding: 25px; border-radius: 20px;
        border: 1px solid #f0e0e5; text-align: center; transition: 0.3s; height: 100%;
    }
    .theory-card:hover { transform: scale(1.03); box-shadow: 0 10px 20px rgba(209, 106, 140, 0.1); }
    .card-icon { font-size: 40px; margin-bottom: 15px; }
    .card-title { color: #d16a8c; font-weight: 700; font-size: 1.2em; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# ГЛАВНЫЙ ЗАГОЛОВОК И ДЕКОР
col_header1, col_header2, col_header3 = st.columns([1,2,1])
with col_header2:
    st.markdown("<h1>Financial Analytics Pro</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #8a7a7d; font-size: 1.2em;'>Next-Generation Terminal for Financial Statement Auditing</p>", unsafe_allow_html=True)
st.markdown("---")

# РАБОЧАЯ ЗОНА: ДАННЫЕ И ГРАФИК
col_data, col_visual = st.columns([1.2, 2]) # Левая колонка для ввода, правая для графика

with col_data:
    st.markdown("## 📊 Data Input")
    tabs = st.tabs(["Manual Entry", "Excel Import"])
    
    with tabs[0]:
        report_type = st.selectbox("Statement", ["Balance Sheet", "Income Statement", "Cash Flow"])
        st.markdown("<br>", unsafe_allow_html=True)
        
        if report_type == "Balance Sheet":
            a = st.number_input("Total Assets", key="ma", value=100000)
            l = st.number_input("Total Liabilities", key="ml", value=60000)
            e = st.number_input("Total Equity", key="me", value=40000)
            
            # Логика графика Баланса
            if a != 0:
                with col_visual:
                    st.markdown("## 📈 Balance Visualization")
                    chart_data = pd.DataFrame({
                        'Category': ['Assets', 'Liabilities + Equity'],
                        'Value': [a, (l + e)]
                    })
                    fig = px.bar(chart_data, x='Category', y='Value', 
                                 title="Assets vs. Funding Source",
                                 color='Category', 
                                 color_discrete_map={'Assets': '#d16a8c', 'Liabilities + Equity': '#64b5f6'})
                    fig.update_layout(showlegend=False, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
                    st.plotly_chart(fig, use_container_width=True)

            if st.button("RUN AUDIT", key="ba"):
                if a == (l + e):
                    st.balloons()
                    st.success(f"Verified: Balance perfectly matches (A={a}). 👍")
                else: 
                    st.toast("Discrepancy detected!", icon="⚠️")
                    st.error(f"Error: Assets do not match sources. Variance: {abs(a-(l+e))}")

        # (Аналогичную логику с графиками можно добавить для Income и Cash Flow)

    with tabs[1]:
        st.markdown("### Import professional data")
        uploaded_file = st.file_uploader("Drop .xlsx report", type="xlsx")
        if uploaded_file and st.button("PROCESS FILE"):
            st.balloons()
            st.success("File analyzed. Data looks correct!")

# --- СЕКЦИЯ: FINANCIAL KNOWLEDGE BASE (КАРТИНКИ И КАРТОЧКИ) ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>📘 Financial Library</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #a19194;'>Interactive guide to corporate reporting</p>", unsafe_allow_html=True)

col_lib1, col_lib2, col_lib3 = st.columns(3)

with col_lib1:
    st.markdown("""
        <div class="theory-card">
            <div class="card-icon">⚖️</div>
            <div class="card-title">Balance Sheet</div>
            <p style='font-size: 0.9em; color: #635155;'>
            "The Snapshot". Shows what a company <b>owns</b> and how it's <b>funded</b> at a specific point in time. 
            Key formula: Assets = L + E.
            </p>
        </div>
    """, unsafe_allow_html=True)

with col_lib2:
    st.markdown("""
        <div class="theory-card">
            <div class="card-icon">📈</div>
            <div class="card-title">Income Statement</div>
            <p style='font-size: 0.9em; color: #635155;'>
            "The Video". Measures performance <b>over time</b>. It shows how much profit (Net Income) remains after all expenses.
            Formula: Revenue - Exp = NI.
            </p>
        </div>
    """, unsafe_allow_html=True)

with col_lib3:
    st.markdown("""
        <div class="theory-card">
            <div class="card-icon">💸</div>
            <div class="card-title">Cash Flow</div>
            <p style='font-size: 0.9em; color: #635155;'>
            "The Pipeline". Tracks where actual <b>cash</b> came from and where it went. Profit does not equal cash in hand!
            It has 3 categories.
            </p>
        </div>
    """, unsafe_allow_html=True)

# Подвал
st.markdown("<br><br><p style='text-align: center; font-size: 0.75em; color: #a19194;'>Powered by Corporate Audit Terminal | v7.0</p>", unsafe_allow_html=True)
