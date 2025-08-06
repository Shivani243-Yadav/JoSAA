# 🏫 JoSAA Seat Allotment EDA & Interactive Dashboard

This repository presents an **Exploratory Data Analysis (EDA)** of JoSAA seat allotment data and a fully **interactive dashboard** built using **Streamlit** for dynamic exploration.

---

## 🚀 Description

The project consists of:

- A **Jupyter Notebook** that performs detailed EDA on JoSAA counselling data.
- A **Streamlit app** that offers interactive visualization and filtering of the dataset.
- Visual insights into branch-wise, institute-wise, category-wise seat allotment trends.
- Tools to help aspirants create optimized preference lists based on historical cutoff data.

---

## 🔍 EDA Contents

Within the notebook, you'll find:

- Data ingestion and cleaning of JoSAA CSV files.
- Summary statistics and count data for all relevant demographics and categories.
- Opening and closing rank trends per branch and institute over rounds.
- Category-wise (GEN, OBC, SC, ST, EWS) and reservation insights.
- Comparative trend analysis across years or institutes.
- Visualizations such as line charts, bar plots, heatmaps, and pivot tables.

---

## 🧩 Streamlit Dashboard Features

Launched via `streamlit run app.py`, the dashboard enables:

- 🌐 **User interactive filters**: Choose institute, branch, category, year, or round.
- 📈 **Dynamic visual charts**: Display cutoff rank trends and comparisons in real time.
- 🔍 **Comparison view**: View side‑by‑side institute and branch analyses.
- 📑 **Detailed round-wise stats**: Opening vs closing ranks, spread, and allocation numbers.

---

## 📁 Repository Structure

├── README.md
├── josaa_eda.ipynb # Exploratory Data Analysis notebook
├── app.py # Streamlit dashboard code
├── data/
│ └── josaa_2022_cutoffs.csv
├── requirements.txt # Python dependencies
└── screenshots/ # Placeholders for dashboard previews


---

## 🛠️ Technologies Used

- **Python**: Pandas, NumPy for data handling  
- **Visualization**: Matplotlib, Seaborn, Plotly  
- **Notebook environment**: Jupyter Notebook  
- **Web app framework**: Streamlit for interactive dashboard deployment

---

## ⚙️ Setup & Run Instructions

1. Clone the repository  
   ```bash
   git clone https://github.com/Shivani243-Yadav/JoSAA.git
   cd JoSAA
Install dependencies

pip install -r requirements.txt
To explore EDA

jupyter notebook josaa_eda.ipynb
To launch the dashboard

streamlit run app.py
📊 Key Insights
Branches like CSE and ECE show the highest competition with tight closing rank ranges.

Top academic institutes such as IIT Bombay and IIT Delhi dominate preference lists among GEN category candidates.

Significant variance in closing ranks across categories illustrates the impact of reservation.

Rival institutes in regional clusters (e.g., NIT Trichy vs NIT Warangal) display contrasting cutoff dynamics.

✅ Future Enhancements
Add predictive modeling (e.g. cutoff rank predictor using ML).

Include multi-year historical JoSAA data for trend forecasting.

Deploy the Streamlit dashboard online (e.g. via Streamlit Cloud) with live, deployable UI.

👥 Contributors
Shivani Yadav – Lead developer & data analyst

📌 Why This Project?
Helps JoSAA aspirants make informed branch and institute preferences.

Demonstrates data science workflow from raw data to interactive insights.

Ready-to-deploy analytics application bridging coding and user experience.

📝 License
This project is licensed under the MIT License – see the LICENSE file for details.

