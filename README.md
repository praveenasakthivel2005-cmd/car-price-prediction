🚗 Car Price Prediction Using Machine Learning

 📌 Project Overview

This project predicts car prices using features like brand, model, year, engine size, fuel type, transmission, mileage, and condition.  
It involves data preprocessing, EDA, and building an accurate machine learning model.  
A Streamlit app is developed to provide real-time price predictions based on user input.

---

 🎯 Problem Statement

Estimating the correct price of a used car is challenging due to multiple influencing factors.  
This project aims to build a machine learning model to predict car prices based on key features, helping users make informed decisions.

---

 📊 Dataset

The dataset contains the following features:

- Brand  
- Model  
- Year  
- Engine Size  
- Fuel Type  
- Transmission  
- Mileage  
- Condition  

** Target Variable: **
- Price  

---

 📊 Exploratory Data Analysis (EDA)

EDA helps to:

- Understand the structure of the dataset  
- Identify patterns and relationships between features  
- Detect missing values and outliers  
- Prepare the data for machine learning models  

---

 🧹 Data Preprocessing

- Handling missing values  
- Removing duplicates  
- Encoding categorical variables  
- Feature scaling  
- Removing outliers  

---

 🤖 Models Used

The following supervised learning algorithms were trained and evaluated:

- Linear Regression  
- Decision Tree Regressor  
- Random Forest Regressor  

---

 🏆 Model Evaluation

Models were evaluated using:

- Mean Absolute Error (MAE)  
- Mean Squared Error (MSE)  
- R² Score  

👉 Random Forest Regressor performed best with the highest R² score and lowest error values.

---

 💾 Model Saving

After training, the best-performing model was saved for future use without retraining.

- The trained Random Forest Regressor model was saved using `pickle`  
- This allows quick loading and prediction during deployment  

---

 🌐 Web Application (Streamlit)

A simple and interactive web application was built using Streamlit for real-time car price prediction.

 🚀 Features

- User inputs car details  
- Predicts car price instantly  
- Simple UI with sliders and dropdowns  
- Displays the predicted price  

---

 🚀 How to Run the Project

1️⃣ Clone the repository  
```bash
git clone https://github.com/praveena-ml/car-price-prediction.git
cd car-price-prediction
```bash
2️⃣ Install dependencies
pip install -r requirements.txt
```bash
3️⃣ Run the Streamlit app
streamlit run app.py
```bash
---

⚠️ Disclaimer

This project is for educational and demonstration purposes only.
The predicted car prices may not be fully accurate and should not be considered as financial or commercial advice.
Actual car prices may vary based on market conditions and other external factors.

---

🛠️ Tools & Technologies
- Programming Language: Python
- Libraries: Pandas, NumPy, Scikit-learn
- Visualization: Matplotlib, Seaborn
- Web Framework: Streamlit
- Model Saving: joblib

---

👩‍💻 Author

**Praveena**
Aspiring Data Scientist | Machine Learning

📌 Open to internships and entry-level data science opportunities.      
