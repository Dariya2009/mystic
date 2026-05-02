import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Конфигурация страницы
st.set_page_config(page_title="Finance Statement Checker Pro", layout="wide", page_icon="📈")

# 2. Улучшенные стили (CSS)
st.markdown("""
    <style>
    html { scroll-behavior: smooth; }
    .stApp { background-color: #0e1117; color: #ffffff; }
    
    /* Верхняя панель */
    .header-bar {
        display: flex; justify-content: flex-end; padding: 20px 5%;
        background: #161b22; border-bottom: 2px solid #800020;
    }
    .auth-btn {
        margin-left: 15px; padding: 10px 30px; border-radius: 5px;
        font-weight: 700; cursor: pointer; border: 2px solid #800020; color: white;
    }
    .signup-btn { background: #800020; color: white; }
    
    /* Секции */
    .hero-section { background: #0e1117; padding: 80px 10%; text-align: center; }
    .knowledge-section { background-color: #161b22; padding: 80px 10%; border-radius: 50px 50px 0 0; }
    .checker-section { background-color: #0e1117; padding: 80px 10%; border-top: 5px solid #800020; }
    .contact-section { background-color: #161b22; padding: 60px 10%; border-top: 1px solid #333; }

    /* Текст */
    .white-text-box { color: #ffffff !important; line-height: 1.8; font-size: 1.1rem; margin-bottom: 20px; }
    .section-title { color: #800020; font-size: 3rem; font-weight: 800; margin-bottom: 30px; }
    
    /* Ссылки-кнопки */
    .custom-link {
        display: inline-block; margin-top: 15px; padding: 10px 25px;
        background-color: #800020; color: white !important;
        text-decoration: none; border-radius: 5px; font-weight: 600;
        transition: 0.3s;
    }
    .custom-link:hover { background-color: #a00028; transform: translateY(-2px); }
    
    .news-card {
        background: #1c2128; padding: 25px; border-radius: 12px;
        border-left: 6px solid #800020; margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. HEADER ---
st.markdown("""
    <div class="header-bar">
        <div class="auth-btn">LOG IN</div>
        <div class="auth-btn signup-btn">SIGN UP</div>
    </div>
""", unsafe_allow_html=True)

# --- 4. HERO ---
st.markdown("""
    <div class="hero-section">
        <h1 style="font-size: 5rem; font-weight: 900; color: #ffffff; letter-spacing: -2px;">FINANCE STATEMENT CHECKER</h1>
        <p style="font-size: 1.8rem; color: #800020; font-weight: 800;">ELITE AUDIT & VERIFICATION TERMINAL</p>
        <p style="color: #ffffff; font-size: 1.2rem; opacity: 0.8;">System Architecture by: <b>Naikina Dariya & Erik Amira</b></p>
    </div>
""", unsafe_allow_html=True)

# --- 5. EDUCATION (БОЛЬШЕ ТЕКСТА) ---
st.markdown("<div class='knowledge-section'>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title'>Professional Financial Education</h2>", unsafe_allow_html=True)

with st.expander("📊 DETAILED ANALYSIS: THE BALANCE SHEET"):
    st.markdown("""
    <div class="white-text-box">
    <b>The Balance Sheet</b> is a fundamental financial statement that provides a snapshot of a company's financial health at a specific point in time. 
    It is built on the accounting equation: <b>Assets = Liabilities + Equity</b>.<br><br>
    - <b>Assets:</b> What the company owns (Cash, Inventory, PPE). Assets are usually listed in order of liquidity.<br>
    - <b>Liabilities:</b> What the company owes to external parties (Loans, Accounts Payable, Taxes).<br>
    - <b>Equity:</b> The owners' claim on the assets after all debts are paid.<br><br>
    Understanding the Balance Sheet is crucial for assessing a company's <b>Solvency</b> and its ability to pay off long-term obligations.
    <br><a href="https://www.investopedia.com/terms/b/balancesheet.asp" class="custom-link">Deep Dive into Balance Sheets 🔗</a>
    </div>
    """, unsafe_allow_html=True)

with st.expander("📈 DETAILED ANALYSIS: THE INCOME STATEMENT"):
    st.markdown("""
    <div class="white-text-box">
    The <b>Income Statement</b> (P&L) measures a company's financial performance over a specific accounting period. 
    It focuses strictly on the <b>Bottom Line</b>: whether the company is profitable or operating at a loss.<br><br>
    Key components include:<br>
    1. <b>Gross Revenue:</b> Total sales before any deductions.<br>
    2. <b>COGS:</b> Direct costs of producing the goods sold.<br>
    3. <b>Operating Expenses:</b> Rent, salaries, marketing, and utilities.<br>
    4. <b>Net Income:</b> The final profit after all expenses and taxes are subtracted.<br><br>
    Growth in Net Income is the primary indicator of a healthy, expanding business.
    <br><a href="https://www.investopedia.com/terms/i/incomestatement.asp" class="custom-link">Learn About Profitability 🔗</a>
    </div>
    """, unsafe_allow_html=True)

with st.expander("💸 DETAILED ANALYSIS: CASH FLOW STATEMENT"):
    st.markdown("""
    <div class="white-text-box">
    The <b>Cash Flow Statement</b> tracks the actual movement of "hard cash" in and out of the company. 
    Profit on paper (from the Income Statement) does not always mean there is money in the bank.<br><br>
    It is divided into three critical sections:<br>
    - <b>Operating Activities:</b> Cash from day-to-day business sales.<br>
    - <b>Investing Activities:</b> Cash used for buying/selling equipment or assets.<br>
    - <b>Financing Activities:</b> Cash from loans, stock issuance, or dividends.<br><br>
    A positive cash flow ensures the company can pay its employees and suppliers on time.
    <br><a href="https://www.investopedia.com/terms/c/cashflowstatement.asp" class="custom-link">Master Cash Flow Management 🔗</a>
    </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- 6. AUDIT TERMINAL (С КНОПКОЙ ДОП. ДАННЫХ) ---
st.markdown("<div class='checker-section'>", unsafe_allow_html=True)
st.markdown("<h2 style='color: white; font-size: 3rem; font-weight: 800;'>Audit Terminal</h2>", unsafe_allow_html=True)

report = st.selectbox("Select Financial Statement to Audit", ["Balance Sheet Audit", "Income Analysis", "Cash Flow Sync"])

if report == "Balance Sheet Audit":
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Assets Analysis")
        # ТА САМАЯ КНОПКА (TOGGLE)
        use_detailed = st.toggle("Enable Detailed Asset Breakdown", value=False)
        if use_detailed:
            cash = st.number_input("Cash & Bank Balances", value=0.0)
            inv = st.number_input("Inventory Value", value=0.0)
            ppe = st.number_input("Fixed Assets (PPE)", value=0.0)
            total_a = cash + inv + ppe
        else:
            total_a = st.number_input("Enter Total Assets Amount", value=0.0)
            
    with col2:
        st.markdown("### Liabilities & Equity")
        liab = st.number_input("Total Debt Liabilities", value=0.0)
        equity = st.number_input("Total Shareholder Equity", value=0.0)
        total_le = liab + equity

    if st.button("EXECUTE AUDIT"):
        if total_a == total_le and total_a > 0:
            st.balloons()
            st.success("SUCCESS: STATEMENT IS BALANCED")
        else:
            st.error(f"FAILED: DISCREPANCY DETECTED ({abs(total_a - total_le)})")
        fig = px.bar(x=['Assets', 'Liab+Eq'], y=[total_a, total_le], range_y=[0, 10000], color_discrete_sequence=['#800020'])
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white")
        st.plotly_chart(fig, use_container_width=True)

elif report == "Income Analysis":
    rev = st.number_input("Total Revenue", value=0.0)
    exp = st.number_input("Total Expenses", value=0.0)
    ni = st.number_input("Reported Net Income", value=0.0)
    if st.button("VALIDATE PROFIT"):
        if ni == (rev - exp) and rev > 0:
            st.balloons()
            st.success("VERIFIED: Net Income is accurate.")
        else:
            st.error("MISMATCH: Check your entries.")

elif report == "Cash Flow Sync":
    st.info("Cash Flow Module Active")
    cf_in = st.number_input("Total Cash Inflow", value=0.0)
    cf_out = st.number_input("Total Cash Outflow", value=0.0)
    if st.button("CALCULATE NET CASH"):
        st.balloons()
        st.success(f"Net Cash Flow: {cf_in - cf_out}")

st.markdown("</div>", unsafe_allow_html=True)

# --- 7. NEWS SECTION ---
st.markdown("<div style='padding: 80px 10%;'>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title'>Financial News Feed</h2>", unsafe_allow_html=True)
n1, n2 = st.columns(2)
with n1:
    st.markdown("<div class='news-card'><h4>Global Rate Stability</h4><p class='white-text-box'>Central banks project stable interest rates for the upcoming fiscal year.</p></div>", unsafe_allow_html=True)
    st.markdown("<div class='news-card'><h4>Tech Sector Growth</h4><p class='white-text-box'>Major tech firms report record-breaking net income in Q1 2026.</p></div>", unsafe_allow_html=True)
with n2:
    st.markdown("<div class='news-card'><h4>ESG Compliance</h4><p class='white-text-box'>New international standards for sustainability reporting are now active.</p></div>", unsafe_allow_html=True)
    st.markdown("<div class='news-card'><h4>Market Volatility</h4><p class='white-text-box'>Energy prices show slight fluctuations due to supply chain updates.</p></div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- 8. CONTACTS & REVIEWS ---
st.markdown("<div class='contact-section'>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title'>Contact & Information</h2>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("### Developers")
    st.markdown("<p style='color: white;'>• Naikina Dariya<br>• Erik Amira</p>", unsafe_allow_html=True)

with c2:
    st.markdown("### Support")
    st.markdown("<p style='color: white;'>Email: support@finchecker.pro<br>Location: Almaty, Kazakhstan</p>", unsafe_allow_html=True)

with c3:
    st.markdown("### Feedback")
    st.markdown("<p style='color: white;'>Check our official reviews on Trustpilot:</p>", unsafe_allow_html=True)
    st.markdown('<a href="https://www.trustpilot.com" target="_blank" class="custom-link">Read Reviews ⭐️</a>', unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #444; padding: 40px;'>©️ 2026 Finance Checker Pro. All rights reserved.</p>", unsafe_allow_html=True)
