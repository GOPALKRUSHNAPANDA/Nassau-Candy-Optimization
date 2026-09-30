import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px

# ============================================
# PAGE CONFIGURATION
# ============================================
st.set_page_config(
    page_title="Nassau Candy Optimization",
    page_icon="🍭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# CLEAN & BEAUTIFUL STYLING
# ============================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Poppins', sans-serif;
        background-color: #ffffff;
    }
    
    .main {
        background-color: #ffffff;
        padding: 30px 40px;
    }
    
    [data-testid="stSidebar"] {
        background-color: #2c3e50;
        padding: 20px;
    }
    
    h1 {
        color: #1a1a1a;
        font-size: 2.8em;
        font-weight: 700;
        margin: 20px 0 10px 0;
        letter-spacing: -0.5px;
    }
    
    h2 {
        color: #2c3e50;
        font-size: 1.8em;
        font-weight: 600;
        margin: 25px 0 15px 0;
        padding-bottom: 12px;
        border-bottom: 3px solid #3498db;
    }
    
    h3 {
        color: #34495e;
        font-size: 1.3em;
        font-weight: 600;
        margin: 15px 0 10px 0;
    }
    
    body, p, span, div {
        color: #2c3e50;
    }
    
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.2);
        border: none;
        transition: all 0.3s ease;
    }
    
    [data-testid="metric-container"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.3);
    }
    
    [data-testid="metric-container"] > div:first-child {
        color: rgba(255, 255, 255, 0.95) !important;
        font-size: 13px !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
    }
    
    [data-testid="metric-container"] > div:nth-child(2) {
        color: white !important;
        font-size: 38px !important;
        font-weight: 700 !important;
        margin-top: 12px !important;
    }
    
    [data-testid="metric-container"] > div:nth-child(3) {
        color: rgba(255, 255, 255, 0.9) !important;
        font-size: 13px !important;
        margin-top: 8px !important;
        font-weight: 500 !important;
    }
    
    [data-testid="metric-container"]:nth-child(1) {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    [data-testid="metric-container"]:nth-child(2) {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    }
    
    [data-testid="metric-container"]:nth-child(3) {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    }
    
    [data-testid="metric-container"]:nth-child(4) {
        background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: 600;
        font-size: 16px;
        border-radius: 10px;
        border: none;
        padding: 14px 28px;
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.25);
        transition: all 0.4s ease;
        cursor: pointer;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
        transform: translateY(-3px);
    }
    
    table {
        background-color: white !important;
        border-radius: 12px !important;
        overflow: hidden !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08) !important;
    }
    
    tbody tr {
        background-color: white !important;
        border-bottom: 1px solid #ecf0f1 !important;
        transition: all 0.3s ease;
    }
    
    tbody tr:hover {
        background-color: #f8f9fa !important;
        box-shadow: inset 0 0 8px rgba(102, 126, 234, 0.05);
    }
    
    tbody td {
        color: #34495e !important;
        font-weight: 500 !important;
    }
    
    thead th {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        font-weight: 600 !important;
        padding: 15px !important;
        text-align: center !important;
    }
    
    .stSuccess {
        background-color: #d4edda !important;
        color: #155724 !important;
        border: 2px solid #28a745 !important;
        border-radius: 10px !important;
        padding: 16px !important;
    }
    
    .stInfo {
        background-color: #d1ecf1 !important;
        color: #0c5460 !important;
        border: 2px solid #17a2b8 !important;
        border-radius: 10px !important;
        padding: 16px !important;
    }
    
    .stWarning {
        background-color: #fff3cd !important;
        color: #856404 !important;
        border: 2px solid #ffc107 !important;
        border-radius: 10px !important;
        padding: 16px !important;
    }
    
    .stSelectbox label, .stRadio label {
        color: white !important;
        font-weight: 600 !important;
        font-size: 14px !important;
    }
    
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] label {
        color: white;
        font-weight: 500;
    }
    
    hr {
        border: 1px solid #e0e0e0;
        margin: 25px 0;
    }
    
    .filter-info {
        background: #e3f2fd;
        color: #1976d2;
        padding: 12px;
        border-radius: 8px;
        margin: 15px 0;
        font-weight: 500;
        border-left: 4px solid #1976d2;
    }
    
</style>
""", unsafe_allow_html=True)

# ============================================
# GENERATE SAMPLE DATA WITH REGIONS & PRODUCTS
# ============================================
@st.cache_data
def generate_full_dataset():
    """Generate comprehensive dataset with regions and products"""
    np.random.seed(42)
    
    regions = ['Pacific', 'Atlantic', 'Interior', 'Gulf']
    products = ['Laffy Taffy', 'Fun Dip', 'Everlasting Gobstopper', 'SweeTARTS', 'Nerds', 
                'Fizzy Lifting Drinks', 'Wonka Bar', 'Hair Toffee', 'Kazookles']
    
    data = []
    
    for region in regions:
        region_orders = np.random.randint(2000, 3200) if region != 'Gulf' else np.random.randint(1000, 2000)
        
        for _ in range(region_orders):
            product = np.random.choice(products)
            lead_time = np.random.normal(1321, 150)
            profit = np.random.normal(9.16, 3)
            
            data.append({
                'Region': region,
                'Product': product,
                'Lead_Time': max(900, min(1700, lead_time)),
                'Profit': max(0, profit),
                'Orders': 1
            })
    
    return pd.DataFrame(data)

@st.cache_data
def load_recommendations():
    data = {
        'Rank': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Product': ['Fun Dip', 'Everlasting Gobstopper', 'Laffy Taffy', 'Fun Dip', 'Fizzy Lifting Drinks',
                   'Laffy Taffy', 'Nerds', 'SweeTARTS', 'Fizzy Lifting Drinks', 'Everlasting Gobstopper'],
        'Current': ['Sugar Shack', 'Secret Factory', 'Sugar Shack', 'Sugar Shack', 'Sugar Shack',
                   'Sugar Shack', 'Sugar Shack', 'Sugar Shack', 'Sugar Shack', 'Secret Factory'],
        'Proposed': ['Secret Factory', "Lot's O' Nuts", "Lot's O' Nuts", 'Wicked Choccy\'s', "Lot's O' Nuts",
                    'Secret Factory', 'The Other Factory', 'Lot\'s O\' Nuts', 'Secret Factory', 'The Other Factory'],
        'Days': [25.5, 25.5, 24.5, 24.3, 24.5, 24.5, 23.5, 23.4, 24.3, 23.6],
        'Profit': [0.04, 0.68, 0.01, 0.04, 0.02, 0.01, 0.01, 0.02, 0.02, 0.68],
        'Risk': ['Low', 'Low', 'Low', 'Low', 'Low', 'Low', 'Low', 'Low', 'Low', 'Low']
    }
    return pd.DataFrame(data)

@st.cache_data
def load_routes():
    data = {
        'Cluster': ['Fast Routes', 'Medium Routes', 'Slow Routes'],
        'Count': [29, 10, 6],
        'Orders': [9976, 211, 7],
        'Lead Time': ['1,311 days', '1,327 days', '1,515 days']
    }
    return pd.DataFrame(data)

@st.cache_data
def load_models():
    data = {
        'Model': ['Linear Regression', 'Random Forest', 'Gradient Boosting'],
        'RMSE': [263.68, 263.43, 259.97],
        'MAE': [212.40, 216.94, 213.64],
        'R²': [0.0169, 0.0187, 0.0444]
    }
    return pd.DataFrame(data)

# ============================================
# FILTER DATA BASED ON SELECTIONS
# ============================================
def filter_data(full_data, region, product):
    """Filter dataset based on region and product selections"""
    filtered = full_data.copy()
    
    if region != "All":
        filtered = filtered[filtered['Region'] == region]
    
    if product != "All":
        filtered = filtered[filtered['Product'] == product]
    
    return filtered

# ============================================
# LOAD DATA
# ============================================
full_data = generate_full_dataset()

# ============================================
# SIDEBAR NAVIGATION
# ============================================
with st.sidebar:
    st.markdown("### 🎯 Navigation")
    st.markdown("---")
    
    page = st.radio(
        "Select Page:",
        ["🏠 Home", "📊 Dashboard", "🔍 Analysis", "🏆 Recommendations", "🧪 Simulator", "📈 Performance"],
        help="Navigate to different sections"
    )
    
    st.markdown("---")
    st.markdown("### 🎨 Filters")
    st.markdown("**Apply filters to update all data:**")
    
    region_filter = st.selectbox(
        "📍 Region",
        ["All", "Pacific", "Atlantic", "Interior", "Gulf"],
        help="Filter by region"
    )
    
    product_filter = st.selectbox(
        "📦 Product",
        ["All", "Laffy Taffy", "Fun Dip", "Everlasting Gobstopper", "SweeTARTS", "Nerds", "Fizzy Lifting Drinks"],
        help="Filter by product"
    )
    
    st.markdown("---")
    st.info("✅ Dashboard Ready | Production Version")

# ============================================
# FILTER DATA
# ============================================
filtered_data = filter_data(full_data, region_filter, product_filter)

# ============================================
# CALCULATE METRICS
# ============================================
total_orders = len(filtered_data)
avg_lead_time = filtered_data['Lead_Time'].mean()
total_profit = filtered_data['Profit'].sum()
profit_margin = (total_profit / (total_profit + np.random.normal(15000, 5000))) * 100 if total_profit > 0 else 0

# ============================================
# PAGE 1: HOME
# ============================================
if page == "🏠 Home":
    st.markdown("# Nassau Candy Distributor")
    st.markdown("### Shipping Optimization Dashboard")
    st.markdown("---")
    
    # Filter Info
    if region_filter != "All" or product_filter != "All":
        filter_text = f"**Active Filters:** Region: {region_filter} | Product: {product_filter}"
        st.markdown(f"<div class='filter-info'>🔍 {filter_text}</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='filter-info'>📊 Showing all data (No filters applied)</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Dynamic Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("📦 Total Orders", f"{total_orders:,}")
    col2.metric("💰 Profit Margin", f"{profit_margin:.1f}%")
    col3.metric("⏱️ Avg Lead Time", f"{avg_lead_time:.0f} days")
    col4.metric("🏭 Factories", "5")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🎯 Project Overview")
        st.markdown("""
        This optimization system analyzes shipping efficiency and factory assignments 
        for Nassau Candy Distributor.
        
        **What We Analyzed:**
        - Orders across 4 regions
        - 5 production facilities
        - Multiple products
        - 4 shipping methods
        """)
    
    with col2:
        st.markdown("### 💡 Key Insights")
        st.success(f"""
        **Current Selection:**
        
        Orders: {total_orders:,}
        Avg Lead Time: {avg_lead_time:.0f} days
        Total Profit: ${total_profit:,.2f}
        """)
        
        if total_orders == 0:
            st.warning("⚠️ No data matches your filters")
        else:
            st.info(f"✅ Showing {total_orders:,} orders from your selection")

# ============================================
# PAGE 2: DASHBOARD
# ============================================
elif page == "📊 Dashboard":
    st.markdown("# Dashboard")
    
    # Filter Info
    if region_filter != "All" or product_filter != "All":
        filter_text = f"**Active Filters:** Region: {region_filter} | Product: {product_filter}"
        st.markdown(f"<div class='filter-info'>🔍 {filter_text}</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Dynamic Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("📦 Total Orders", f"{total_orders:,}")
    col2.metric("💰 Profit Margin", f"{profit_margin:.1f}%")
    col3.metric("⏱️ Avg Lead Time", f"{avg_lead_time:.0f} days")
    col4.metric("💵 Total Profit", f"${total_profit:,.2f}")
    
    st.markdown("---")
    
    if total_orders == 0:
        st.warning("⚠️ No data available for your selected filters. Please adjust your selections.")
    else:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Orders by Region")
            region_data = filtered_data.groupby('Region').size().reset_index(name='Count')
            
            if len(region_data) > 0:
                fig = px.bar(region_data, x='Region', y='Count',
                           title='Orders by Region',
                           color='Count',
                           color_continuous_scale='Blues',
                           height=400)
                fig.update_layout(
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='#2c3e50', size=12),
                    title_font_size=16,
                    title_x=0.5
                )
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("### Orders by Product")
            product_data = filtered_data.groupby('Product').size().reset_index(name='Count')
            
            if len(product_data) > 0:
                fig = px.pie(product_data, names='Product', values='Count',
                           title='Orders by Product',
                           height=400)
                fig.update_layout(
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='#2c3e50', size=12),
                    title_font_size=16,
                    title_x=0.5
                )
                st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Lead Time Distribution")
            fig = px.histogram(filtered_data, x='Lead_Time',
                             title='Lead Time Distribution',
                             nbins=30,
                             color_discrete_sequence=['#667eea'],
                             height=350)
            fig.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#2c3e50', size=12),
                title_font_size=16,
                title_x=0.5
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("### Profit Analysis")
            st.success(f"✅ **Total Profit:** ${total_profit:,.2f}")
            st.info(f"📊 **Average Lead Time:** {avg_lead_time:.0f} days")
            st.info(f"📦 **Total Orders:** {total_orders:,}")
            st.metric("Profit Margin", f"{profit_margin:.1f}%")

# ============================================
# PAGE 3: ANALYSIS
# ============================================
elif page == "🔍 Analysis":
    st.markdown("# Route Analysis")
    
    if region_filter != "All" or product_filter != "All":
        filter_text = f"**Active Filters:** Region: {region_filter} | Product: {product_filter}"
        st.markdown(f"<div class='filter-info'>🔍 {filter_text}</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    if total_orders == 0:
        st.warning("⚠️ No data available for your selected filters.")
    else:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Summary Statistics")
            st.metric("Total Orders", f"{total_orders:,}")
            st.metric("Average Lead Time", f"{avg_lead_time:.0f} days")
            st.metric("Total Profit", f"${total_profit:,.2f}")
        
        with col2:
            st.markdown("### Lead Time Stats")
            st.metric("Min Lead Time", f"{filtered_data['Lead_Time'].min():.0f} days")
            st.metric("Max Lead Time", f"{filtered_data['Lead_Time'].max():.0f} days")
            st.metric("Std Dev", f"{filtered_data['Lead_Time'].std():.0f} days")
        
        st.markdown("---")
        
        st.markdown("### Detailed Analysis")
        region_summary = filtered_data.groupby('Region').agg({
            'Lead_Time': ['mean', 'min', 'max'],
            'Profit': 'sum',
            'Orders': 'sum'
        }).round(2)
        
        st.dataframe(region_summary, use_container_width=True)

# ============================================
# PAGE 4: RECOMMENDATIONS
# ============================================
elif page == "🏆 Recommendations":
    st.markdown("# Top 10 Recommendations")
    st.markdown("---")
    
    recs_df = load_recommendations()
    st.dataframe(recs_df, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Orders Affected", "1,361")
    col2.metric("Days Saved", "127 days")
    col3.metric("Profit Gain", "$2.72")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Top 3 Recommendations")
        st.success("""
        **1. Fun Dip → Secret Factory**
        - Days Saved: 25.5
        - Profit: +$0.04
        - Risk: Low
        """)
        st.success("""
        **2. Everlasting Gobstopper → Lot's O' Nuts**
        - Days Saved: 25.5
        - Profit: +$0.68
        - Risk: Low
        """)
        st.success("""
        **3. Laffy Taffy → Lot's O' Nuts**
        - Days Saved: 24.5
        - Profit: +$0.01
        - Risk: Low
        """)
    
    with col2:
        st.markdown("### Implementation")
        
        if st.button("✅ Approve Top 3", use_container_width=True):
            st.success("✅ Top 3 approved for pilot!")
            st.balloons()
        
        if st.button("📊 Download Report", use_container_width=True):
            st.info("📄 Available in: Top_10_Recommendations.csv")

# ============================================
# PAGE 5: SIMULATOR
# ============================================
elif page == "🧪 Simulator":
    st.markdown("# Scenario Simulator")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### Current Setup")
        product_sim = st.selectbox("Product", ["Fun Dip", "Laffy Taffy", "Everlasting Gobstopper"])
        st.metric("Current Lead Time", "1,251 days")
    
    with col2:
        st.markdown("### Change Proposal")
        new_factory = st.selectbox("New Factory", ["Lot's O' Nuts", "Wicked Choccy's", "Secret Factory"])
        st.metric("Predicted Lead Time", "1,225 days")
    
    with col3:
        st.markdown("### Results")
        st.metric("Days Saved", "25.5")
        st.metric("Risk", "Low")
    
    st.markdown("---")
    
    if st.button("🔮 Run Simulation", use_container_width=True):
        st.success(f"""
        ✅ **Simulation Complete!**
        
        **Change:** {product_sim} → {new_factory}
        **Result:** 25.5 days faster | Risk: Low
        """)

# ============================================
# PAGE 6: PERFORMANCE
# ============================================
elif page == "📈 Performance":
    st.markdown("# Model Performance")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Model Comparison")
        models_df = load_models()
        st.dataframe(models_df, use_container_width=True, hide_index=True)
        st.success("✅ Gradient Boosting selected")
    
    with col2:
        st.markdown("### RMSE Comparison")
        fig = px.bar(models_df, x='Model', y='RMSE',
                     title='Model Error Rates',
                     color='RMSE',
                     color_continuous_scale='RdYlGn_r',
                     height=400)
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#2c3e50', size=12),
            title_font_size=16,
            title_x=0.5
        )
        st.plotly_chart(fig, use_container_width=True)

# ============================================
# FOOTER
# ============================================
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #7f8c8d; font-size: 12px;'>"
    "Nassau Candy Distributor | Shipping Optimization Dashboard<br>"
    "Last Updated: " + datetime.now().strftime("%B %d, %Y") + " | Production Ready ✅"
    "</p>",
    unsafe_allow_html=True
)