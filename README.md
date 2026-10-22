# Airbnb Data Pipeline & Analytics Dashboard

## 📌 Project Overview
This is an end-to-end data project that extracts live listings from Airbnb across 10 major European cities. The goal is to provide actionable insights into pricing strategies, property types, and the impact of host badges (Superhost/Guest Favorite) on market dynamics.

## 🛠️ Tech Stack & Workflow
1. **Web Scraping (Python & Selenium):** Extracted ~500 listings with filters (Entire home/apt, 2 Bedrooms). Handled dynamic loading and cleaned raw strings into structured data.
2. **Data Warehousing (SQL Server):** Cleaned and transformed the data, then modeled it using a **Star Schema** (Fact & Dimension tables) to optimize query performance.
3. **Data Visualization (Power BI):** Built a 4-page interactive dashboard to explore the data.

## 📂 Repository Structure
- `1_Scraper/`: Python script used to extract data from Airbnb.
- `2_SQL_Data_Warehouse/`: T-SQL scripts for table creation, cleaning, and loading.
- `3_Dashboard/`: The Power BI file and a PDF preview of the dashboard.

## 📊 Dashboard Highlights
- **Overview:** High-level KPIs, city price comparisons, and property type distribution.
- **City Deep Dive:** Scatter plots to find "hidden gems" (high rating, low price) and neighborhood analysis.
- **Host Analysis:** Evaluating the pricing premium of Superhosts and Guest Favorites.
- **Data Model:** Visual representation of the SQL Star Schema.

## 💡 Key Insights Discovered
- **The Superhost Premium:** Listings with Superhost or Guest Favorite badges command significantly higher prices in major tourist hubs like Amsterdam and London.
- **Market Economics:** Amsterdam and London are the most expensive markets in this dataset, while Athens and Budapest offer the most budget-friendly options.
- **Hidden Gems:** Price does not always equal quality. The scatter plot revealed several mid-priced properties with 5-star ratings (4.8+).
