# Nassau Candy Distributor - Factory Optimization Project

<div align="center">

## 🍭 Shipping Optimization & Route Analysis System

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)

**An end-to-end data science project analyzing 10,194 orders to optimize factory assignments and shipping efficiency.**

</div>

---

## 📌 Project Overview

This project evaluates shipping efficiency and factory-to-product assignments for Nassau Candy Distributor. Using machine learning and predictive analytics, it identifies optimization opportunities that can reduce lead times and improve profitability.

### 🎯 Objective
- Analyze 10,194 orders across 5 factories
- Build predictive models for shipping lead times
- Identify bottleneck routes through clustering
- Test optimization scenarios
- Provide actionable recommendations for factory reassignment

### 📊 Dataset
- **Records:** 10,194 orders
- **Factories:** 5 production facilities
- **Products:** 15 unique items
- **Regions:** 4 US markets (Pacific, Atlantic, Interior, Gulf)
- **Features:** 18 original columns → 26 engineered features
- **Time Period:** Full year historical data

---

## 📈 Key Findings

### Main Discoveries
- **Sugar products are 204 days slower** than average
- **Day of week impacts lead time** (37% feature importance)
- **Current assignments are near-optimal** (marginal improvements possible)
- **Top opportunity:** 127 days can be saved across 1,361 orders

### Performance Metrics
| Metric | Value |
|--------|-------|
| Total Orders Analyzed | 10,194 |
| Profit Margin | 65.9% |
| Average Lead Time | 1,321 days |
| Total Profit | $93,442.80 |
| Optimization Potential | 127 days (Top 10) |

### Model Performance
| Model | RMSE | MAE | R² |
|-------|------|-----|-----|
| Linear Regression | 263.68 | 212.40 | 0.0169 |
| Random Forest | 263.43 | 216.94 | 0.0187 |
| **Gradient Boosting** ⭐ | **259.97** | **213.64** | **0.0444** |

---

## 🏆 Top 3 Recommendations

### 1️⃣ Fun Dip → Secret Factory
- **Days Saved:** 25.5 days
- **Profit Impact:** +$0.04
- **Risk Level:** Low
- **Implementation:** Immediate

### 2️⃣ Everlasting Gobstopper → Lot's O' Nuts
- **Days Saved:** 25.5 days
- **Profit Impact:** +$0.68 ⭐
- **Risk Level:** Low
- **Implementation:** Immediate

### 3️⃣ Laffy Taffy → Lot's O' Nuts
- **Days Saved:** 24.5 days
- **Profit Impact:** +$0.01
- **Risk Level:** Low
- **Implementation:** 1 week

**Cumulative Impact (Top 10):** 127 days saved + $2.72 profit on 1,361 orders

---

## 🛠️ Technologies Used

### Data & Analysis
- **Python 3.9+** - Programming language
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Scikit-learn** - Machine learning models
- **Matplotlib & Seaborn** - Static visualizations

### Dashboard & Visualization
- **Streamlit** - Interactive web dashboard
- **Plotly** - Dynamic, interactive charts
- **Google Colab** - Development environment

### ML Models
- **Linear Regression** - Baseline model
- **Random Forest** - Ensemble method
- **Gradient Boosting** - Best performing model (RMSE: 259.97)

---

## 📊 Methodology

### STEP 1: Data Exploration
- Loaded 10,194 orders with 18 features
- Analyzed profit margins, regional distribution
- Identified missing values (0 found)
- Created initial visualizations
- Found: Chocolate = 96.5%, Sugar = 2.9%, Other = 0.6%

### STEP 2: Data Preparation
- Converted date formats (DD-MM-YYYY)
- Calculated lead times: Ship Date - Order Date
- Created 11 new features:
  - Profit_Margin (Sales basis)
  - Order_Month, Order_DayOfWeek
  - Units_per_Sale ratio
  - Encoded categories (Region, ShipMode, Division)
- Final dataset: 26 features

### STEP 3: Predictive Modeling
- Split: 80% training (8,155), 20% testing (2,039)
- Built 3 ML models:
  - Linear Regression (RMSE: 263.68)
  - Random Forest (RMSE: 263.43)
  - Gradient Boosting (RMSE: 259.97) ⭐ WINNER
- Evaluated using RMSE, MAE, R²

### STEP 4: Route Clustering
- Identified 45 unique routes
- Applied K-Means clustering (k=3)
- Found 3 clusters:
  - 🟢 Fast Routes: 29 routes, 9,976 orders, 1,311 days avg
  - 🟡 Medium Routes: 10 routes, 211 orders, 1,327 days avg
  - 🔴 Slow Routes: 6 routes, 7 orders, 1,515 days avg (BOTTLENECK)

### STEP 5: Scenario Simulation
- Tested 24 product reassignment scenarios
- Predicted new lead times using best model
- Calculated profit impact for each scenario
- Ranked by: Days saved + Profit gain + Risk score

### STEP 6: Optimization & Recommendations
- Generated top 10 recommendations
- Assessed implementation risk (LOW)
- Calculated cumulative impact: 127 days, $2.72, 1,361 orders
- Provided implementation timeline (2-4 weeks)

---

## 🎯 How to Use

### Option 1: View Interactive Dashboard
```bash
# Install dependencies
pip install streamlit pandas matplotlib numpy plotly

# Run dashboard
python -m streamlit run dashboard/app.py

# Opens in browser at http://localhost:8501
```

### Option 2: View Jupyter Notebook
```bash
# Open Google Colab
# https://colab.research.google.com/

# Upload: Nassau_Candy_Analysis.ipynb
# Run cells in order
```

### Option 3: Analyze CSV Results
- `Prepared_Data.csv` - Cleaned dataset with features
- `Top_10_Recommendations.csv` - Ranked recommendations
- `All_Scenarios.csv` - All 24 scenarios tested
- `Routes_Clustering.csv` - Route cluster analysis

---

## 📊 Dashboard Features

### 6 Interactive Pages

1. **🏠 Home** - Project overview, key metrics
2. **📊 Dashboard** - Factory performance, order distribution
3. **🔍 Analysis** - Route clustering, bottleneck identification
4. **🏆 Recommendations** - Top 10 moves, impact analysis
5. **🧪 Simulator** - What-if scenario testing
6. **📈 Performance** - Model comparison, feature importance

### Live Filters
- Filter by Region (Pacific, Atlantic, Interior, Gulf)
- Filter by Product
- All metrics update in real-time
- Beautiful Plotly visualizations

---

## 💡 Business Impact

### Efficiency Gains
- **Lead Time Reduction:** 127 days (top 10 recommendations)
- **Orders Affected:** 1,361 orders (13.3% of total)
- **Percentage Improvement:** ~1% average reduction

### Financial Impact
- **Profit Improvement:** $2.72 (top 10 combined)
- **Risk Level:** LOW (49.4/100 risk score)
- **Implementation Difficulty:** LOW to MEDIUM

### Implementation Strategy
1. **Phase 1 (Week 1-2):** Pilot with top 3 recommendations
2. **Phase 2 (Week 3-4):** Monitor and validate
3. **Phase 3 (Week 5+):** Roll out remaining recommendations

---

## 🎓 Skills Demonstrated

### Data Science
✅ Exploratory Data Analysis (EDA)
✅ Feature Engineering & Selection
✅ Data Cleaning & Preparation
✅ Statistical Analysis

### Machine Learning
✅ Model Building (3 algorithms)
✅ Model Evaluation & Comparison
✅ Hyperparameter Tuning
✅ Cross-validation

### Clustering & Optimization
✅ K-Means Clustering
✅ Route Performance Analysis
✅ Scenario Simulation
✅ Business Optimization

### Visualization & Communication
✅ Data Visualization (Matplotlib, Seaborn, Plotly)
✅ Interactive Dashboards (Streamlit)
✅ Professional Documentation
✅ Business Recommendations

### Programming
✅ Python (Pandas, NumPy, Scikit-learn)
✅ Google Colab
✅ Jupyter Notebooks
✅ Version Control (Git)

---

## 📁 Project Files