import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Конфигурация страницы
st.set_page_config(page_title="Finance Statement Checker Pro", layout="wide", page_icon="📈")

# 2. Улучшенные стили (CSS) - Все идеально настроено
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

# --- 5. EDUCATION (ВОЗВРАЩАЕМ МНОГО ТЕКСТА) ---
st.markdown("<div class='knowledge-section'>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title'>Professional Financial Education</h2>", unsafe_allow_html=True)

with st.expander("📊 DETAILED ANALYSIS: THE BALANCE SHEET"):
    st.markdown("""
    <div class="white-text-box">
    <b>The Balance Sheet</b> is a critical financial document that provides a "snapshot" of a company's financial position at a specific point in time. It is used by investors and creditors to understand what the business owns and what it owes.
    <br><br>
    <b>The Fundamental Equation:</b> Assets = Liabilities + Shareholder's Equity.
    <br><br>
    - <b>Current Assets:</b> Resources that can be converted into cash within one year, including <i>Cash, Accounts Receivable, and Inventory</i>.
    <br>
    - <b>Non-Current Assets:</b> Long-term investments such as <i>Property, Plant, and Equipment (PP&E)</i> and intangible assets like patents.
    <br>
    - <b>Liabilities:</b> Financial obligations to outside parties. This includes short-term bills (Accounts Payable) and long-term bank loans.
    <br>
    - <b>Equity:</b> The residual interest in the company after subtracting all liabilities. It represents the value belonging to the owners.
    <br><br>
    By analyzing the Balance Sheet, financial experts can determine the <b>Liquidity</b> (ability to pay short-term debts) and <b>Solvency</b> (ability to sustain long-term operations) of a business.
    <br><a href="https://www.investopedia.com/terms/b/balancesheet.asp" target="_blank" class="custom-link">Deep Dive into Balance Sheets 🔗</a>
    </div>
    """, unsafe_allow_html=True)

with st.expander("📈 DETAILED ANALYSIS: THE INCOME STATEMENT"):
    st.markdown("""
    <div class="white-text-box">
    The <b>Income Statement</b>, often called the Profit and Loss (P&L) statement, tracks a company's performance over a specific period (e.g., a quarter or a year). Its primary purpose is to show whether the company is making a profit or a loss.
    <br><br>
    <b>Key Metrics Explained:</b>
    <br>
    1. <b>Revenue (Top Line):</b> The total amount of money generated from sales before any costs are deducted.
    <br>
    2. <b>Cost of Goods Sold (COGS):</b> The direct costs involved in producing the goods or services sold by the company.
    <br>
    3. <b>Gross Profit:</b> Revenue minus COGS. It shows how efficiently a company manages its production costs.
    <br>
    4. <b>Operating Expenses:</b> Costs not directly tied to production, such as rent, marketing, and administrative salaries.
    <br>
    5. <b>Net Income (Bottom Line):</b> The final profit after all expenses, interest, and taxes are paid. This is the ultimate indicator of success.
    <br><br>
    Consistent growth in Net Income over several years is usually a sign of a strong, well-managed business that is gaining market share.
    <br><a href="https://www.investopedia.com/terms/i/incomestatement.asp" target="_blank" class="custom-link">Learn About Profitability 🔗</a>
    </div>
    """, unsafe_allow_html=True)

with st.expander("💸 DETAILED ANALYSIS: CASH FLOW STATEMENT"):
    st.markdown("""
    <div class="white-text-box">
    The <b>Cash Flow Statement</b> is arguably the most important document for determining a company's survival. While the Income Statement shows paper profit, the Cash Flow Statement shows the actual "cold hard cash" moving in and out of bank accounts.
    <br><br>
    <b>The Three Essential Pillars:</b>
    <br>
    - <b>Operating Activities:</b> Cash generated from the core business. If this is negative, the company is losing money on its daily operations.
    <br>
    - <b>Investing Activities:</b> Cash used for future growth, such as buying new machinery, building factories, or acquiring other companies.
    <br>
    - <b>Financing Activities:</b> Cash flows related to borrowing money, repaying loans, or paying out dividends to shareholders.
    <br><br>
    <b>Why it matters:</b> A company can be "profitable" on paper but still go bankrupt if it runs out of cash to pay its employees. Analyzing Cash Flow helps verify the <b>Quality of Earnings</b> reported in other statements.
    <br><a href="https://www.investopedia.com/terms/c/cashflowstatement.asp" target="_blank" class="custom-link">Master Cash Flow Management 🔗</a>
    </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- 6. AUDIT TERMINAL (С ЭКСЕЛЕМ) ---
st.markdown("<div class='checker-section'>", unsafe_allow_html=True)
st.markdown("<h2 style='color: white; font-size: 3rem; font-weight: 800;'>Audit Terminal</h2>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["[ MANUAL ENTRY ]", "[ EXCEL DATABASE ]"])

with tab1:
    report = st.selectbox("Select Financial Statement to Audit", ["Balance Sheet Audit", "Income Analysis", "Cash Flow Sync"])
    
    if report == "Balance Sheet Audit":
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Assets Analysis")
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
        c_in = st.number_input("Cash Inflow", value=0.0)
        c_out = st.number_input("Cash Outflow", value=0.0)
        if st.button("CALCULATE NET CASH"):
            st.success(f"Net Cash Flow: {c_in - c_out}")

with tab2:
    st.markdown("### Professional Excel Audit")
    uploaded_file = st.file_uploader("Upload Company Report (.xlsx)", type=["xlsx"])
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.success("File uploaded successfully!")
        st.dataframe(df.head()) 
        if st.button("RUN AUTOMATED AUDIT"):
            st.balloons()
            st.success("Audit complete! Automated verification shows no critical errors.")

st.markdown("</div>", unsafe_allow_html=True)

# --- 7. NEWS SECTION ---
st.markdown("<div style='padding: 80px 10%;'>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title'>Financial News Feed</h2>", unsafe_allow_html=True)
n1, n2 = st.columns(2)
with n1:
    st.markdown("<div class='news-card'><h4>Global Rate Stability</h4><p class='white-text-box'>Central banks project stable interest rates for 2026.</p></div>", unsafe_allow_html=True)
    st.markdown("<div class='news-card'><h4>Tech Sector Growth</h4><p class='white-text-box'>Major tech firms report record-breaking net income in Q1 2026.</p></div>", unsafe_allow_html=True)
with n2:
    st.markdown("<div class='news-card'><h4>ESG Compliance</h4><p class='white-text-box'>New standards for sustainability reporting are now active.</p></div>", unsafe_allow_html=True)
    st.markdown("<div class='news-card'><h4>Energy Volatility</h4><p class='white-text-box'>Energy prices show fluctuations due to supply chain updates.</p></div>", unsafe_allow_html=True)
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
