import streamlit as st
import pandas as pd
import plotly.express as px

# Конфигурация страницы
st.set_page_config(page_title="Finance Statement Checker Pro", layout="wide", page_icon="📈")

# Стилизация: Полный Dark Mode с белым текстом
st.markdown("""
    <style>
    html { scroll-behavior: smooth; }
    .stApp { background-color: #0e1117; color: #ffffff; }
    
    /* Кнопки входа в углу */
    .header-bar {
        display: flex; justify-content: flex-end; padding: 20px 5%;
        background: #161b22; border-bottom: 2px solid #800020;
    }
    .auth-btn {
        margin-left: 15px; padding: 10px 30px; border-radius: 5px;
        font-weight: 700; cursor: pointer; border: 2px solid #800020;
    }
    .login-btn { color: #ffffff; background: transparent; }
    .signup-btn { background: #800020; color: white; }
    
    /* Секции */
    .hero-section { background: #0e1117; padding: 80px 10%; text-align: center; }
    
    /* Сделали Education секцию темной с белым текстом */
    .knowledge-section { 
        background-color: #161b22; 
        color: #ffffff !important; 
        padding: 80px 10%; 
        border-radius: 50px 50px 0 0;
        border-top: 1px solid #333;
    }
    
    .checker-section { background-color: #0e1117; padding: 80px 10%; border-top: 5px solid #800020; }
    .news-section { background-color: #161b22; padding: 80px 10%; }

    /* Принудительный белый текст для всех элементов внутри Expander и текста */
    .white-text-box { color: #ffffff !important; line-height: 1.8; font-size: 1.1rem; }
    .stExpander { background-color: #1c2128 !important; border: 1px solid #333 !important; border-radius: 10px !important; }
    .stExpander p { color: #ffffff !important; }
    
    .main-title { font-size: 5rem; font-weight: 900; color: #ffffff; letter-spacing: -2px; }
    
    /* Карточки новостей */
    .news-card {
        background: #0e1117; padding: 25px; border-radius: 12px;
        border-left: 6px solid #800020; margin-bottom: 25px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.5);
    }
    .news-title { color: #ffffff; font-weight: 800; font-size: 1.3rem; margin-bottom: 10px; }
    .news-desc { color: #e0e0e0; font-size: 1rem; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
    <div class="header-bar">
        <div class="auth-btn login-btn">LOG IN</div>
        <div class="auth-btn signup-btn">SIGN UP</div>
    </div>
""", unsafe_allow_html=True)

# --- HERO ---
st.markdown("""
    <div class="hero-section">
        <h1 class="main-title">FINANCE STATEMENT CHECKER</h1>
        <p style="font-size: 1.8rem; color: #800020; font-weight: 800;">ELITE DATA VERIFICATION PLATFORM</p>
        <p style="color: #ffffff; font-size: 1.3rem; opacity: 0.9;">System Architecture by: <b>Naikina Dariya & Erik Amira</b></p>
    </div>
""", unsafe_allow_html=True)

# --- KNOWLEDGE BASE (Теперь темная с белым текстом) ---
st.markdown("<div class='knowledge-section'>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #800020; font-size: 3rem; font-weight: 800;'>Professional Financial Education</h2>", unsafe_allow_html=True)
st.markdown("<p style='color: #ffffff; font-size: 1.2rem; margin-bottom: 30px;'>Explore the core pillars of corporate accounting through our interactive modules.</p>", unsafe_allow_html=True)

with st.expander("📊 DETAILED ANALYSIS: THE BALANCE SHEET"):
    st.markdown("""
    <div class="white-text-box">
    The <b>Balance Sheet</b> is considered the most critical financial statement for determining the intrinsic value of a company. It provides a detailed report of the financial position at a specific point in time, essentially showing the company’s net worth.<br><br>
    <b>The Fundamental Equilibrium:</b> Assets = Liabilities + Shareholder's Equity.<br><br>
    - <b>Current Assets:</b> Resources expected to be converted into cash within one year, such as <i>Accounts Receivable</i> and <i>Inventory</i>.<br>
    - <b>Non-Current Assets:</b> Long-term investments including <i>Property, Plant, and Equipment (PP&E)</i> and <i>Intangible Assets</i> like patents.<br>
    - <b>Liabilities:</b> What the company owes to creditors, including short-term bills and long-term bank loans.<br>
    - <b>Equity:</b> The amount that would be returned to shareholders if all assets were liquidated and all debts paid.<br><br>
    Investors use this statement to calculate key ratios like the <b>Current Ratio</b> to assess liquidity.
    </div>
    """, unsafe_allow_html=True)

with st.expander("📈 DETAILED ANALYSIS: THE INCOME STATEMENT"):
    st.markdown("""
    <div class="white-text-box">
    The <b>Income Statement</b>, or Profit and Loss (P&L) report, focuses strictly on the company’s revenues and expenses during a specific period. It is the primary tool for evaluating the profitability and growth trajectory of a business.<br><br>
    <b>Standard Calculation Path:</b><br>
    1. <b>Gross Revenue:</b> Total income from all sales activities.<br>
    2. <b>Cost of Goods Sold (COGS):</b> The direct costs of producing goods sold by the company.<br>
    3. <b>Operating Expenses:</b> Indirect costs such as marketing, rent, and administrative salaries.<br>
    4. <b>EBITDA:</b> Earnings before interest, taxes, depreciation, and amortization.<br>
    5. <b>Net Income:</b> The final 'Bottom Line' profit after all deductions.<br><br>
    Consistent growth in Net Income over several quarters is usually a strong signal of operational excellence and market demand.
    </div>
    """, unsafe_allow_html=True)

with st.expander("💸 DETAILED ANALYSIS: CASH FLOW STATEMENT"):
    st.markdown("""
    <div class="white-text-box">
    While the Income Statement shows paper profit, the <b>Cash Flow Statement</b> shows the actual cash hitting the bank account. This is vital because a company can be 'profitable' but still go bankrupt if it lacks cash to pay employees.<br><br>
    <b>The Three Pillars of Cash Flow:</b><br>
    1. <b>Operating Cash Flow (OCF):</b> Cash generated by the core business products or services. Healthy companies must have a positive OCF.<br>
    2. <b>Investing Cash Flow:</b> Reflects the company's investment in its future, such as buying new machinery or acquiring other startups.<br>
    3. <b>Financing Cash Flow:</b> Shows how the company manages its capital, including issuing stock, taking on new debt, or paying dividends to shareholders.<br><br>
    Analyzing the interaction between these three pillars reveals whether a company is truly sustainable or merely surviving on borrowed money.
    </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- AUDIT TERMINAL ---
st.markdown("<div class='checker-section'>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #ffffff; font-size: 3rem; font-weight: 800;'>Audit & Verification Terminal</h2>", unsafe_allow_html=True)

# Тюнинг вкладок для темной темы
st.markdown("""<style> .stTabs [data-baseweb="tab-list"] { gap: 24px; } .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; background-color: #1c2128; border-radius: 4px 4px 0px 0px; color: white; } </style>""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["[ MANUAL ENTRY ]", "[ EXCEL DATABASE ]"])

with tab1:
    report = st.selectbox("Select Audit Logic", ["Balance Sheet Audit", "Income Analysis", "Cash Flow Sync"])
    st.markdown("<br>", unsafe_allow_html=True)
    
    if report == "Balance Sheet Audit":
        with st.container():
            col_a, col_le = st.columns(2)
            with col_a:
                st.markdown("### Assets Input")
                use_detail = st.toggle("Use Detailed Asset Inputs")
                if use_detail:
                    c1 = st.number_input("Cash & Bank Balances", value=0.0)
                    c2 = st.number_input("Fixed Property Assets", value=0.0)
                    total_a = c1 + c2
                else:
                    total_a = st.number_input("Input Total Assets", value=0.0)
            
            with col_le:
                st.markdown("### Funding Sources")
                l1 = st.number_input("Total Debt Liabilities", value=0.0)
                e1 = st.number_input("Reported Shareholder Equity", value=0.0)
                total_le = l1 + e1

        if st.button("EXECUTE SYSTEM AUDIT"):
            if total_a == total_le and total_a > 0:
                st.balloons()
                st.success("AUDIT STATUS: VERIFIED - THE STATEMENT IS PERFECTLY BALANCED")
            else:
                st.error(f"AUDIT STATUS: CRITICAL ERROR - VARIANCE DETECTED: {abs(total_a - total_le)}")
            
            fig = px.bar(x=['Assets', 'Liab+Eq'], y=[total_a, total_le], range_y=[0, 10000], color_discrete_sequence=['#800020'])
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white")
            st.plotly_chart(fig, use_container_width=True)

    elif report == "Income Analysis":
        rev = st.number_input("Revenue", value=0.0)
        exp = st.number_input("Expenses", value=0.0)
        ni = st.number_input("Net Income", value=0.0)
        if st.button("VALIDATE PROFIT"):
            if ni == (rev - exp) and rev > 0:
                st.balloons()
                st.success("VERIFIED: Net Income matches the Revenue/Expense ratio.")
            else:
                st.error("MISMATCH: The profit calculation does not align with inputs.")

with tab2:
    st.markdown("### Enterprise Batch Processing")
    st.file_uploader("Upload .xlsx file for secure system-wide analysis")

st.markdown("</div>", unsafe_allow_html=True)

# --- NEWS SECTION ---
st.markdown("<div class='news-section'>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #800020; font-size: 3rem; font-weight: 800;'>Global Financial News Feed</h2>", unsafe_allow_html=True)

col_n1, col_n2 = st.columns(2)
with col_n1:
    st.markdown("""<div class='news-card'><div class='news-title'>Global Monetary Policy</div><div class='news-desc'>The Federal Reserve indicates a potential shift in interest rate strategy for late 2026 as inflationary pressures stabilize across major sectors.</div></div>""", unsafe_allow_html=True)
    st.markdown("""<div class='news-card'><div class='news-title'>Big Tech Fiscal Performance</div><div class='news-desc'>Fortune 500 technology companies report a combined net income increase of 22% due to massive scale-ups in AI-driven automation services.</div></div>""", unsafe_allow_html=True)
    st.markdown("""<div class='news-card'><div class='news-title'>International Audit Standards</div><div class='news-desc'>Regulators propose stricter guidelines for the Cash Flow Statement to improve transparency in cross-border corporate investments.</div></div>""", unsafe_allow_html=True)

with col_n2:
    st.markdown("""<div class='news-card'><div class='news-title'>Fintech Ecosystem Expansion</div><div class='news-desc'>Venture capital flows into emerging fintech hubs reach record levels, specifically targeting blockchain-based settlement systems.</div></div>""", unsafe_allow_html=True)
    st.markdown("""<div class='news-card'><div class='news-title'>Energy Market Volatility</div><div class='news-desc'>Oil futures see sharp fluctuations following supply chain adjustments, prompting global energy firms to re-evaluate their balance sheets.</div></div>""", unsafe_allow_html=True)
    st.markdown("""<div class='news-card'><div class='news-title'>Sustainable Finance Trends</div><div class='news-desc'>Green bonds and ESG-linked equity investments show a 15% increase in demand from institutional investors focused on long-term sustainability.</div></div>""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><p style='text-align: center; color: #555; padding-bottom: 50px;'>Finance Statement Checker v7.0 | Naikina Dariya & Erik Amira | Almaty 2026</p>", unsafe_allow_html=True)
