# 🎓 Student Pass Prediction App

This mini project uses **Logistic Regression** to predict whether a student will pass or fail based on their study habits and attendance.

## 🧠 What This Project Includes:
- ✅ Machine Learning model (Logistic Regression)
- ✅ Streamlit web application for easy prediction
- ✅ User input for:
  - Study hours
  - Sleep hours
  - Number of breaks
  - Attendance %
- ✅ Saved model using `joblib`

---

## 📊 Tech Stack Used:
- Python
- pandas, scikit-learn
- Streamlit
- joblib

---

## 🚀 How It Works:
1. The ML model is trained on sample student data.
2. The trained model is saved as a `.pkl` file.
3. Streamlit app loads the model and takes user input.
4. The app predicts whether the student is likely to **pass or fail**.

---

## 📁 Files in This Repo:
| File                  | Description                                |
|-----------------------|--------------------------------------------|
| `train_model.py`      | Trains the logistic regression model       |
| `pass_predictor_model.pkl` | Saved trained model                    |
| `student_pass_app.py` | Streamlit UI for prediction                |
| `student_data.csv`    | Sample dataset used for training           |

---

## 🧪 Example Use Case:
> A student studied 6 hours, slept 7 hours, took 2 breaks, and had 90% attendance?  
🎯 The model says: **PASS!**

---

## 👩‍💻 Author
**Harini Kathirvel**  
Student, AI & Data Science  
🚀 Passionate about ML, UI, and building smart solutions!

---

## 🌐 Future Plans:
- Deploy the app online with Streamlit Cloud
- Add more features like subject-wise scores
- Improve accuracy with a larger dataset

---

⭐ Give this repo a star if you like it!  
💬 Feedback and suggestions are always welcome.

