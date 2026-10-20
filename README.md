# Student Performance Predictor

This project predicts a student's Performance Index based on study hours, previous scores, sleep hours, extracurricular activities, and practice question papers.

The application uses **Linear Regression** and provides a simple web interface built with **Streamlit**.

## Features

- Predict student performance.
- Enter student details using interactive inputs.
- View the predicted Performance Index.
- See a summary of the entered details.

## Technologies Used

- Python
- Pandas and NumPy
- Scikit-learn
- Streamlit
- Joblib
- Jupyter Notebook

## Project Structure

```text
student-performance-predictor/
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   └── Student_Performance.csv
└── notebooks/
    └── 01_data_exploration.ipynb
```

## Model Evaluation

I compared four machine learning models using test data.

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | 1.600 | 2.018 | 0.989 |
| Ridge Regression | 1.600 | 2.018 | 0.989 |
| Gradient Boosting | 1.654 | 2.083 | 0.989 |
| Random Forest | 1.866 | 2.333 | 0.986 |

Linear Regression was selected because it performed as well as Ridge Regression in this evaluation and is simple to understand.

- **MAE:** Average absolute prediction error; lower is better.
- **RMSE:** Measures prediction errors and penalizes larger errors; lower is better.
- **R²:** Measures how well the model explains the target's variation; higher is generally better.

These results are based on one test split and may vary on new data.

## How to Run the Project

1. Install Python.
2. Download or clone this project.
3. Open a terminal in the project folder.
4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the application:

   ```bash
   python -m streamlit run app.py
   ```

6. Open the local URL shown in the terminal.

## Future Improvements

- Test the model on more data.
- Improve the application's interface.
- Deploy the application online.

## Disclaimer

This project is for learning and demonstration purposes. Predictions are estimates and do not guarantee a student's actual academic performance.
