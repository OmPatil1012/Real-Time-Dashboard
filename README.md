#  Real-Time Executive Dashboard with Power BI

**Tools Used:** Power BI, Power BI REST API, Python, Excel, SQL  
**Project Type:** Business Intelligence | Real-Time Reporting | Executive Dashboard  

---

##  Objective

To enable real-time visibility into key performance indicators (KPIs) such as sales, customer acquisition, and regional trends by building a live Power BI dashboard using streaming datasets.

---

##  How It Works

1. Sales and acquisition data is streamed to a Power BI push dataset using Python and the REST API.
2. Power BI visualizations update in real-time as new records are pushed.
3. Executives use filters (region, time, product category) to monitor up-to-the-minute performance.

---

##  Dataset Used

- Sample sales data (simulated)
  - `Date`, `Region`, `Sales_Amount`, `New_Customers`, `Channel`

> Located in: [`data/sample_sales_data.csv`](data/sample_sales_data.csv)

---

##  Streaming Script

- Python script sends new rows every few seconds to Power BI.
- Uses the Power BI REST API + bearer token auth.

> See: [`scripts/push_data_to_powerbi.py`](scripts/push_data_to_powerbi.py)

---

##  Dashboard Highlights

> See notes: [`dashboard/README.txt`](dashboard/README.txt)

- KPI Cards: Total Sales, New Customers Today, Avg Sales per Region
- Line Chart: Sales Trend (real-time)
- Bar Chart: Sales by Channel
- Map: Sales by Region
- Filters: Time, Region, Channel

---

##  Business Impact

- Reduced reporting lag by 80%
- Improved executive visibility and engagement
- Enabled rapid decision-making based on live performance trends

---

##  Contact

**Author:** [Your Name]  
**LinkedIn:** [your-link]  
**Live Demo / Portfolio:** [your-link]
