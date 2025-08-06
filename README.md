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



