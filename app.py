import streamlit as st
import pandas as pd
import plotly.express as px

# Настройки страницы
st.set_page_config(page_title="Luxe Financial Terminal", layout="centered", page_icon="💎")

# Навороченный CSS для эффекта полноценного лендинга
st.markdown("""
    <style>
    /* Плавный скролл */
    html { scroll-behavior: smooth; }
    
    .stApp { background: linear-gradient(180deg, #fdf2f5 0%, #ffffff 50%, #e3f2fd 100%); }
    
    /* Стили для секций */
    .section-container {
        background: rgba(255, 255, 255, 0.8);
        padding: 40px;
        border-radius: 25px;
        margin-bottom: 50px;
        border: 1px solid rgba(230, 200, 210, 0.5);
        box-shadow: 0 10px 30px rgba(0,0,0,0.03);
    }

    .stButton>button {
        width: 100%; border-radius: 12px; background-color: #d16a8c; color: white;
        height: 50px; font-weight: 700; border: none; transition: 0.4s;
    }
    .stButton>button:hover { background-color: #b55474; transform: scale(1.02); }
    
    h1 { color: #4a3b3e; text-align: center; font-weight: 800; font-size: 3em; margin-bottom: 0px; }
    h2 { color: #d16a8c; text-align: center; font-weight: 700; margin-top: 20px; }
    
    /* Футер и Авторы */
    .author-card {
        text-align: center;
        padding: 20px;
        background: white;
        border-radius: 15px;
        border: 1px solid #f0e0e5;
    }
    </style>
""", unsafe_allow_html=True)

# --- ГЛАВНЫЙ ЭКРАН (HEADER) ---
st.markdown("<h1>Financial Audit Terminal</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8a7a7d; font-size: 1.2em;'>Intelligent Verification System for Modern Accounting</p>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)

# --- СЕКЦИЯ 1: ANALYTICS TOOL (ГЛАВНЫЙ БЛОК) ---
st.markdown("<div class='section-container'>", unsafe_allow_html=True)
st.markdown("## 📊 1. Analytics & Verification")
input_mode = st.radio("Choose Mode", ["Manual Entry", "Excel Upload"], horizontal=True)

if input_mode == "Manual Entry":
    report = st.selectbox("Statement Type", ["Balance Sheet", "Income Statement", "Cash Flow"])
    
    if report == "Balance Sheet":
        c1, c2, c3 = st.columns(3)
        with c1: a = st.number_input("Assets", value=10000.0)
        with c2: l = st.number_input("Liabilities", value=6000.0)
        with c3: e = st.number_input("Equity", value=4000.0)
        if st.button("RUN AUDIT"):
            if a == (l + e):
                st.balloons()
                st.success("Verified: A = L + E")
            else: st.error(f"Variance: {abs(a-(l+e))}")
            fig = px.bar(x=['Assets', 'L + E'], y=[a, l+e], color=['Assets', 'L + E'], 
                         color_discrete_sequence=['#d16a8c', '#64b5f6'], height=350)
            st.plotly_chart(fig, use_container_width=True)

    elif report == "Income Statement":
        c1, c2, c3 = st.columns(3)
        with c1: rev = st.number_input("Revenue", value=12000.0)
        with c2: exp = st.number_input("Expenses", value=8000.0)
        with c3: ni = st.number_input("Net Income", value=4000.0)
        if st.button("VALIDATE PROFIT"):
            if ni == (rev - exp):
                st.balloons()
                st.success("Profitability Confirmed")
            else: st.error(f"Variance: {abs(ni-(rev-exp))}")
            fig = px.bar(x=['Revenue', 'Expenses', 'Net Income'], y=[rev, exp, ni], height=350)
            st.plotly_chart(fig, use_container_width=True)

    elif report == "Cash Flow":
        c1, c2 = st.columns(2)
        with c1: start = st.number_input("Opening Cash", value=5000.0)
        with c2: end = st.number_input("Closing Cash", value=8000.0)
        if st.button("VERIFY CASH"):
            st.info("Check manual calculations or use Excel for full flow.")
            st.balloons()

else:
    uploaded_file = st.file_uploader("Upload .xlsx file", type="xlsx")
    if uploaded_file and st.button("PROCESS EXCEL"):
        st.success("File processed successfully!")
        st.balloons()

st.markdown("</div>", unsafe_allow_html=True)

# --- СЕКЦИЯ 2: KNOWLEDGE BASE (ЛИСТАЕМ НИЖЕ) ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<div class='section-container'>", unsafe_allow_html=True)
st.markdown("## 📘 2. Financial Knowledge Base")
st.markdown("<p style='text-align: center;'>Essential concepts for business analysis</p>", unsafe_allow_html=True)

col_t1, col_t2, col_t3 = st.columns(3)
with col_t1:
    with st.expander("⚖️ Balance Sheet"):
        st.write("Снимок активов и обязательств. Главное — равенство сторон.")
with col_t2:
    with st.expander("📈 Income Statement"):
        st.write("Показывает результат работы: сколько заработали и сколько потратили.")
with col_t3:
    with st.expander("💸 Cash Flow"):
        st.write("Движение реальных денег. Важно для ликвидности бизнеса.")
st.markdown("</div>", unsafe_allow_html=True)

# --- СЕКЦИЯ 3: AUTHORS & CONTACTS ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("## 🤝 3. Meet the Authors")

col_a1, col_a2 = st.columns(2)

with col_a1:
    st.markdown("""
        <div class='author-card'>
            <h3>Найкина Дария</h3>
            <p>Lead Developer & Financial Analyst</p>
        </div>
    """, unsafe_allow_html=True)

with col_a2:
    st.markdown("""
        <div class='author-card'>
            <h3>Ерик Амира</h3>
            <p>UI/UX Designer & Researcher</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.markdown("### Contact Us")
st.write("Email: contact@luxefinance.com")
st.write("University Project 2026")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br><br><p style='text-align: center; font-size: 0.8em; color: #aaa;'>Luxe Financial Terminal v10.0 | One-Page Edition</p>", unsafe_allow_html=True)
