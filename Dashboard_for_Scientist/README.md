## 1. Why (The Problem & Motivation)

- **The Problem:** When data scientists or biologists first encounter a raw CSV dataset, the "shape" and validity of the data are unknown. It is difficult to know the structure and pattern of the data without writing custom code for every file.
- **The Value:** We need a universal "first-look" tool. For a biologist, this might mean quickly checking if a CSV contains valid gene counts or metadata before running a complex pipeline. For a mathematician, it’s about instantly verifying the distribution of a variable (Gaussian vs. Uniform) without writing boilerplate plotting code.
- **The Goal:** Reduce the "Time to Insight" for a raw file from 10 minutes to 10 seconds.

- **Real why:** Jatin have an interest for sciences

## 2. What (Scope & Features)

We will build a Minimum Viable Product (MVP) contained in a single Python file.

- **Inputs:**
  - Drag-and-drop file uploader (supports `.csv` only).
- **Processing:**
  - Automatic parsing of the file into a Pandas DataFrame.
  - Automatic detection of numerical vs. categorical columns.
- **Outputs (The Dashboard):**
  - **Data Preview:** Display the first 5-10 rows (the "Head").
  - **Mathematical Summary:** Display descriptive statistics (Mean, Std Dev, Min, Max) for numerical columns.
  - **Visualizations:**
    - **Univariate:** Histogram to view distributions (crucial for biology/stats).
    - **Bivariate:** Scatter plot to view correlations.

- **Real what:**
  Input CSV file -> processing: showing CSV raw data and basic impouve data count means std ... -> output: GUI interface with info

## 3. How (Technical Implementation)

- **Tech Stack:**
  - **Language:** Python 3.9+
  - **Core Libraries:**
    - `pandas` (Data manipulation)
    - `numpy` (Data manipulation)
    - `streamlit` (UI and server)
    - `matplotlibs` (Interactive plotting)
    - `seaborn` (Interactive plotting)
- **Architecture:**
  - The app will run linearly (top to bottom).
  - `if file is uploaded` -> `load csv` -> `show stats` -> `render plots`.
- **GitHub Workflow:**
  - Initialize repo locally.
  - Create `app.py`.
  - Commit and Push to `main`.

## 4. When (Timeline & Estimation)

- **Deadline:** Tuesday next week
- **Work Period:** Autonomy Section Data Engineering

**Time Estimation Logic:**

- **Total Budget:** 3 Hours
- **Calculation:** 3/2 - (15% Uncertainty)
- **Optimistic Estimate:** 1.2 Hours
- **Pessimistic Estimate:** 3 Hours

## Run Method

- **Requierments:**  
   **Core Libraries:**
  _ `pandas` (Data manipulation)
  _ `numpy` (Data manipulation)
  _ `streamlit` (UI and server)
  _ `matplotlibs` (Interactive plotting)
  _ `seaborn` (Interactive plotting)
  **downloading:**
  _ From 'ENGINEERING-SANDBOX/Dashboard_for_Scientis' Run the 'pip install -r requirements.txt' commande in the terminal
- **Start:**
  - From 'ENGINEERING-SANDBOX/Dashboard_for_Scientis' Run the commande 'streamlit run front_end_streamlit_app.py'
