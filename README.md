
# 💸 Insurance Charge Predictor
A simple and interactive web application built with **Streamlit** and trained using **TensorFlow** to predict **insurance charges** based on user information like age, sex, BMI, number of children, smoking habits, and region.

📂 **Repo:** https://github.com/mohitkumhar/insurance-charge-predictor

---

## 🚀 Features

- 🎯 Predicts insurance charges using a deep neural network
- 📊 Clean and responsive UI built with Streamlit
- 📈 Data preprocessing and Exploratory Data Analysis (EDA)
- 💾 Trained model export (`model.h5`) for quick deployment
- 🧠 Encodes categorical variables using OneHotEncoder

---

## 📌 Input Features

- `age`: Age of the person
- `sex`: Gender (`male`, `female`)
- `bmi`: Body Mass Index
- `children`: Number of dependent children
- `smoker`: Smoking status (`yes`, `no`)
- `region`: Residential region (`southwest`, `southeast`, `northwest`, `northeast`)

---

## 🛠️ Installation

1. **Clone the repo:**
   ```bash
   git clone https://github.com/mohitkumhar/insurance-charge-predictor.git
   cd insurance-charge-predictor
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```bash
   streamlit run app.py
   ```

---

## 🧠 Model Architecture

The neural network consists of:

- Dense layers: [256 → 128 → 64 → 32 → 16 → 8 → 1]
- Activation: ReLU for hidden layers, Linear for output
- Optimizer: Adam
- Loss: Mean Squared Error (MSE)

---

## ⚠️ Troubleshooting

**Error:**  
```
TypeError: Descriptors cannot be created directly...
```

**Fix:**  
Install compatible protobuf version:
```bash
pip install protobuf==3.20.*
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

Made with ❤️ by [Mohit Kumhar](https://github.com/mohitkumhar)
