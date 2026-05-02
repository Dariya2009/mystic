import streamlit as st
import pandas as pd
import plotly.express as px

# Конфигурация страницы
st.set_page_config(page_title="Finance Statement Checker", layout="wide", page_icon="📈")

# Профессиональный дизайн (Серый и Бордовый)
st.markdown("""
    <style>
    /* Основной фон и шрифт */
    .stApp {
        background-color: #1e1e1e;
        color: #e0e0e0;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    
    /* Титульный экран */
    .hero-section {
        height: 80vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        background: linear-gradient(135deg, #1e1e1e 0%, #2d2d2d 100%);
        border-bottom: 3px solid #800020;
    }
    .hero-title { font-size: 5rem; font-weight: 800; color: #ffffff; margin-bottom: 0px; }
    .hero-subtitle { font-size: 1.5rem; color: #800020; font-weight: 500; margin-top: 10px; }
    .developers { font-size: 1rem; color: #aaaaaa; margin-top: 40px; text-transform: uppercase; letter-spacing: 2px; }

    /* Секции */
    .section-container {
        padding: 60px 10%;
        background-color: #262626;
        margin-top: 20px;
        border-radius: 10px;
    }
    h2 { color: #800020; font-weight: 700; border-bottom: 1px solid #333; padding-bottom: 10px; }

    /* Стилизация ввода и кнопок */
    .stNumberInput input { background-color: #333 !important; color: white !important; border: 1px solid #444 !important; }
    .stButton>button {
        background-color: #800020;
        color: white;
        border: none;
        border-radius: 4px;
        height: 50px;
        font-weight: 600;
        transition: all 0.3s;
    }
    .stButton>button:hover { background-color: #a00028; transform: translateY(-2px); border: none; color: white; }

    /* Ссылки */
    a { color: #800020; text-decoration: none; font-weight: bold; }
    a:hover { color: #a00028; }
    </style>
""", unsafe_allow_html=True)

# --- SECTION 1: TITLE SCREEN (HERO) ---
st.markdown(f"""
    <div class="hero-section">
        <div class="hero-title">FINANCE STATEMENT CHECKER</div>
        <div class="hero-subtitle">High-Precision Audit & Data Validation Terminal</div>
        <div class="developers">Developed by: Naikina Dariya & Erik Amira</div>
        <div style="margin-top: 50px; color: #555;">Scroll down to begin</div>
    </div>
""", unsafe_allow_html=True)

# --- SECTION 2: KNOWLEDGE BASE ---
st.markdown("<div class='section-container'>", unsafe_allow_html=True)
st.markdown("## FINANCIAL CONCEPTS & TERMINOLOGY")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Balance Sheet")
    st.write("A financial snapshot that shows a company's assets, liabilities, and equity at a specific point in time.")
    st.markdown("[View Visual Example 🔗](https://www.investopedia.com/terms/b/balancesheet.asp)")

with col2:
    st.markdown("### Income Statement")
    st.write("Reports a company's financial performance over a specific accounting period (Profit/Loss).")
    st.markdown("[View Visual Example 🔗](https://www.investopedia.com/terms/i/incomestatement.asp)")

with col3:
    st.markdown("### Cash Flow")
    st.write("Tracks the net amount of cash and cash equivalents being transferred into and out of a business.")
    st.markdown("[View Visual Example 🔗](https://www.investopedia.com/terms/c/cashflowstatement.asp)")
st.markdown("</div>", unsafe_allow_html=True)

# --- SECTION 3: CHECKER (THE CORE) ---
st.markdown("<div class='section-container' id='checker'>", unsafe_allow_html=True)
st.markdown("## STATEMENT VERIFICATION TERMINAL")

# Интерактивный переход (Переключатель)
input_method = st.segmented_control("Select Input Architecture", ["Manual Terminal", "Excel Database"], default="Manual Terminal")

if input_method == "Manual Terminal":
    st.markdown("### Manual Entry System")
    report_type = st.selectbox("Financial Report Type", ["Balance Sheet Audit", "Income Analysis", "Cash Verification"])
    
    if report_type == "Balance Sheet Audit":
        c1, c2, c3 = st.columns(3)
        with c1: assets = st.number_input("Total Assets", value=0.0, max_value=10000.0)
        with c2: liabilities = st.number_input("Liabilities", value=0.0, max_value=10000.0)
        with c3: equity = st.number_input("Owner's Equity", value=0.0, max_value=10000.0)
        
        if st.button("EXECUTE AUDIT"):
            if assets == (liabilities + equity) and assets != 0:
                st.snow() # Эффект конфетти/снега
                st.success("AUDIT SUCCESS: Statement is balanced.")
            else:
                st.error(f"AUDIT ERROR: Discrepancy of {abs(assets - (liabilities+equity))} detected.")
            
            # График с лимитом 10,000
            df = pd.DataFrame({'Component': ['Assets', 'Liabilities + Equity'], 'Value': [assets, liabilities + equity]})
            fig = px.bar(df, x='Component', y='Value', color='Component', range_y=[0, 10000],
                         color_discrete_map={'Assets': '#800020', 'Liabilities + Equity': '#444444'})
            fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color="white")
            st.plotly_chart(fig, use_container_width=True)

    elif report_type == "Income Analysis":
        c1, c2, c3 = st.columns(3)
        with c1: rev = st.number_input("Total Revenue", value=0.0, max_value=10000.0)
        with c2: exp = st.number_input("Total Expenses", value=0.0, max_value=10000.0)
        with c3: ni = st.number_input("Reported Net Income", value=0.0, max_value=10000.0)
        
        if st.button("VALIDATE PROFITABILITY"):
            if ni == (rev - exp) and rev != 0:
                st.snow()
                st.success("VALIDATION SUCCESS: Profit calculation is accurate.")
            else:
                st.error("VALIDATION ERROR: Net Income does not match Revenue - Expenses.")
            
            df = pd.DataFrame({'Component': ['Revenue', 'Expenses', 'Net Income'], 'Value': [rev, exp, ni]})
            fig = px.bar(df, x='Component', y='Value', color_discrete_sequence=['#800020'], range_y=[0, 10000])
            fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color="white")
            st.plotly_chart(fig, use_container_width=True)

else:
    st.markdown("### Excel Batch Processing")
    file = st.file_uploader("Upload Company Report (.xlsx)", type="xlsx")
    if file:
        st.success("File uploaded. Analyzing secure data...")
        st.snow()

st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<br><p style='text-align: center; color: #555;'>Finance Statement Checker v2.0 | Naikina & Erik | 2026</p>", unsafe_allow_html=True)
