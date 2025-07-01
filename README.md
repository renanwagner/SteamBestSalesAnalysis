# 🎮 Steam Best-Selling Games Data Analysis

This project focuses on **data cleaning**, **feature engineering**, and **basic statistical analysis** of best-selling games available on the Steam platform. The goal is to explore, transform, and analyze key variables that may influence a game's success, such as price, downloads, reviews, ratings, and more.

## 📁 Project Structure

### `treatment.py`
This script is responsible for preprocessing and transforming the original dataset (`bestSelling_games.csv`). It includes:

- Parsing and extracting date fields (day, month, year).
- Creating new features (e.g., `generation`, `main_tag`, `main_feature`).
- Applying **MinMax scaling** to numerical variables.
- Encoding categorical features using **LabelEncoder**.
- Calculating total revenue (`price * estimated_downloads`) and converting to millions.
- Renaming and formatting columns to make the data consistent and easier to analyze.
- Saving the cleaned and transformed dataset as `bestSelling_treated.csv`.

### `basic_math_statistics.py`
This script performs basic statistical modeling and analysis using **Linear Regression**. It includes:

- Multiple regression models to estimate relationships between:
  - Price and revenue.
  - Reviews and downloads.
  - Like rate and rating.
  - Year and console generation.
- Evaluation of each model using:
  - **R² Score** (coefficient of determination)
  - **RMSE** (Root Mean Squared Error)
- Analysis of feature correlations using `pandas.corr()`.
- Interpretations of regression results in terms of business and user behavior.

> ⚠️ This script **does not modify the dataset**. It only reads from `bestSelling_treated.csv`.

---

## 📊 Key Technologies

- **Python 3.10+**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Matplotlib & Seaborn** *(in future visualizations)*

---

## 📦 Dataset

The original dataset used is `bestSelling_games.csv`, which must be present in the project directory for the scripts to work correctly. The cleaned dataset is saved as:

- `bestSelling_treated.csv`

---

## 🔧 How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/steam-data-analysis.git
   cd steam-data-analysis
