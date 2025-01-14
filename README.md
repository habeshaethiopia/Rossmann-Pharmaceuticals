# **Rossmann Pharmaceuticals**

## **Project Overview**
 You work at Rossmann Pharmaceuticals as a Machine Learning Engineer. The finance team wants to forecast sales in all their stores across several cities six weeks ahead of time. Managers in individual stores rely on their years of experience as well as their personal judgment to forecast sales.
The data team identified factors such as promotions, competition, school and state holidays, seasonality, and locality as necessary for predicting the sales across the various stores.


---

## **Key Objectives**
1. Perform exploratory data analysis (EDA) to uncover customer behavior patterns.
2. Identify opportunities for growth and profitability improvement.
3. Build an interactive dashboard for data exploration and insight visualization.
4. Develop modular and production-ready Python code to automate workflows and ensure scalability.

---

## **Technologies and Tools**
- **Programming Languages:** Python  
- **Libraries/Modules:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Prophet  
- **Data Visualization:** Plotly, Streamlit  
- **Database:** PostgreSQL  
- **CI/CD:** GitHub Actions  
- **Testing:** Pytest  
- **Web Frameworks:** Flask, Streamlit  

---

## **Folder Structure**
```
📁 TellCo-Data-Analysis/
│
├── .vscode/                # VSCode configuration
│   └── settings.json       # Editor settings
│
├── .github/                # GitHub configuration
│   └── workflows/
│       ├── unittests.yml   # CI/CD for running unit tests
│
├── .gitignore              # Git ignore file
│
├── requirements.txt        # Python dependencies
│
├── README.md               # Project overview and guide
│
├── src/                    # Source code for the application
│   ├── __init__.py         # Module initialization
│
├── notebooks/              # Jupyter notebooks for data analysis
│   ├── __init__.py         # Module initialization
│   └── README.md           # Instructions for using notebooks
│
├── tests/                  # Unit tests for the project
│   ├── __init__.py         # Module initialization
│
└── scripts/                # Utility scripts for automation and pipelines
    ├── __init__.py         # Module initialization
    └── README.md           # Documentation for scripts
```

---

## **Setup and Installation**
1. **Clone the repository:**  
   ```bash
   git clone https://github.com/username/TellCo-Data-Analysis.git
   cd TellCo-Data-Analysis
   ```

2. **Install dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application (e.g., dashboard):**  
   ```bash
   streamlit run src/dashboard.py
   ```

4. **Run unit tests:**  
   ```bash
   pytest tests/
   ```

---

## **Usage**
1. **Notebooks:**  
   The `notebooks/` folder contains detailed Jupyter notebooks for EDA and ML experiments.  

2. **Scripts:**  
   The `scripts/` folder holds reusable scripts for ETL, preprocessing, and automation workflows.  

3. **Testing:**  
   The `tests/` folder includes unit tests to validate the functionality of various modules.  

---

## **Deliverables**
1. **Interactive Dashboard:**  
   A web-based tool for exploring data and insights.  

2. **Business Report:**  
   A detailed document summarizing analysis findings and recommendations.  

3. **Codebase:**  
   Well-organized, modular, and production-ready code.  

---

## **Contributors**
- **[Adane Moges]**  

