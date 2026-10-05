# 🎓 Student Performance Predictor

A Machine Learning web application that predicts a student's academic performance based on selected academic and personal factors.

🚀 Live Demo: https://student-performance-predictor-zkbnxrfjpeqbvgnesq8xbj.streamlit.app

## 📌 About the Project

The **Student Performance Predictor** is a Machine Learning project developed using Python and Scikit-learn. The application allows users to enter student-related information and generates a predicted performance score.

The project demonstrates the complete Machine Learning workflow:

* Data collection
* Data preprocessing
* Exploratory Data Analysis (EDA)
* Feature selection
* Model training
* Model evaluation
* Model prediction
* Web application development
* Model deployment

## 📊 Dataset

The project uses a student performance dataset containing **1,000 student records**.

The dataset contains information related to students' academic performance and other relevant factors.

### Main Features

| Feature            | Description                                    |
| ------------------ | ---------------------------------------------- |
| Gender             | Student's gender                               |
| Race/Ethnicity     | Student's race/ethnicity group                 |
| Parental Education | Education level of the student's parents       |
| Lunch              | Type of lunch received by the student          |
| Test Preparation   | Whether the student completed test preparation |
| Math Score         | Student's mathematics score                    |
| Reading Score      | Student's reading score                        |
| Writing Score      | Student's writing score                        |

### 🎯 Target

The model predicts the student's **overall/average performance score**, calculated using the relevant subject scores.

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib
* Streamlit

## 🤖 Machine Learning

The project includes:

* Data preprocessing
* Feature engineering
* Model training
* Model evaluation
* Prediction

The trained model is saved and loaded for making predictions through the Streamlit application.

## 🌐 Deployment

The application is deployed using **Streamlit Community Cloud**.

🚀 **Live Application:** [Student Performance Predictor](YOUR_STREAMLIT_LINK_HERE)

## 📂 Project Structure

```text
student-performance-predictor/
│
├── Home.py
├── models.pkl
├── requirements.txt
├── bg4.jpeg
├── style.css
├── project_sp.ipynb
├── pages/
      ├── 1_Prediction.py
      ├── 2_Analysis.py
      ├── 3_About.py
├── dataset/StudentPerformance.csv
└── README.md
```

## ▶️ Run Locally

Clone the repository:

```bash
git clone https://github.com/Ishika-0309/student-performance-predictor.git
```

Move into the project directory:

```bash
cd student-performance-predictor
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## 👩‍💻 Author

**Ishika Parmar**

BSc(CA & IT) / Integrated MSc(CA & IT)

Gujarat University
