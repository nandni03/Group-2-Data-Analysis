# Group-2-Data-Analysis
# 🧠 Customer Segmentation using K-Means Clustering

This project applies machine learning techniques to segment customers based on demographics and behavioral data. Using **K-Means clustering**, we group similar customers to enable targeted marketing strategies.

---

## 📌 Project Objective

To perform **customer segmentation** using unsupervised learning on a marketing dataset. The goal is to:
- Identify customer segments based on purchasing behavior and demographics.
- Understand each segment's characteristics.
- Recommend marketing actions tailored to each segment.

---

## 📊 Dataset

The dataset contains anonymized information about customers, including:
- Demographics (Income, Age, Kids/Teens at Home)
- Spending habits on different product categories
- Campaign response history
- Purchase channel behavior (Web, Store, Deals)

> 📁 File: `marketing_campaign_cleaned.csv`

---

## 🛠️ Tools & Libraries

- **Python 3.12+**
- `pandas`, `numpy` – Data manipulation
- `matplotlib`, `seaborn` – Visualization
- `scikit-learn` – Clustering, scaling, PCA
- `Jupyter Notebook` – Interactive analysis

---

## 📈 Workflow

### 1. Data Preprocessing
- Handling missing values (imputed standardized median for income)
- Standardizing numeric features
- Feature engineering (Age, Total Spend)

### 2. Feature Selection
- Selected meaningful features (Income, Age, Recency, Spending, Campaign Response, etc.)

### 3. Clustering
- Used **K-Means** clustering
- Determined optimal `k` using **Elbow Method** and **Silhouette Score**
- Applied clustering and labeled customers

### 4. Visualization
- **PCA 2D plot** for visual cluster separation
- **Radar plots** to compare cluster profiles
- **Box plots**, **Heatmaps**, and **Pair plots** for in-depth interpretation

### 5. Cluster Profiling
Analyzed each cluster:
- Demographics
- Spending power
- Campaign responsiveness
- Channel preferences

---

## 📊 Key Visualizations

- PCA Scatter Plot of Clusters
- Heatmap of Cluster Centers
- Feature-wise Boxplots per Cluster
- Pie Chart of Customer Distribution

---

## 🔍 Cluster Insights Summary

| Cluster | Traits | Strategy |
|--------|--------|----------|
| 0 | Low-income families, low spend, low campaign response | Target with basic offers & awareness |
| 1 | High-income premium buyers, high spend, active | Personalize premium campaigns |
| 2 | Mid-income, digital-focused, moderate spend | Push online engagement & convenience |
| 3 | Low spend, inactive but responsive to campaigns | Flash sales & promotional hooks |

---

## 📁 Project Structure

├── marketing_campaign_cleaned.csv
├── customer_segmentation.ipynb
├── cluster_visualizations/
│ ├── pca_plot.png
│ ├── radar_chart.png
│ └── cluster_boxplots.png
├── README.md
└── requirements.txt

---
## To install requirements
pip install -r requirements.txt
