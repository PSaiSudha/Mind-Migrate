# 🧠 Mind Migrate

### Passive Behavioral Telemetry & Real-Time Mental Health Monitoring System

🌐 **Live Demo:** [View Live Streamlit App](https://mind-migrate-saisudha.streamlit.app/)

---

## 🚀 Overview

**Mind Migrate** is a professional Streamlit-based wellness monitoring dashboard designed to analyze behavioral telemetry and identify changes in user mental states in real time.

The system uses behavioral indicators such as typing speed, backspace frequency, typing errors, and application usage patterns to classify possible mental states using a Machine Learning model.

Based on the predicted state, Mind Migrate provides contextual wellness interventions such as breathing exercises, micro-stretches, and personalized guidance to help users manage work-related fatigue and stress.

> **Note:** Mind Migrate is a wellness-support system and is not intended to diagnose or replace professional medical or mental-health care.

---

## ✨ Key Features

### 🧠 Passive Behavioral Telemetry

Tracks behavioral indicators such as:

* Keystrokes per minute
* Backspace frequency
* Typing errors
* Interaction patterns
* Application usage patterns

### 🤖 ML-Powered Mood Classification

Uses a **Scikit-learn Random Forest Classifier** to classify behavioral states into:

* 😰 Stressed
* 😴 Fatigued
* 😌 Calm
* 🎯 Focused

### 🌿 Contextual Wellness Interventions

Provides personalized suggestions based on the predicted state, including:

* Breathing exercises
* Micro-stretches
* Short breaks
* Relaxation techniques
* Focus improvement suggestions

Example:

**4-7-8 Breathing Technique**

* Inhale for 4 seconds
* Hold for 7 seconds
* Exhale for 8 seconds

### 📊 Professional SaaS Dashboard

The application provides a modern dashboard containing:

* Real-time status cards
* Behavioral metrics
* Live charts
* Mood prediction
* Progress indicators
* Wellness recommendations

### 🔐 Privacy & Consent Controls

Mind Migrate includes privacy-focused features such as:

* Anonymous mode
* User consent controls
* Local SQLite data persistence
* On-device processing approach

---

## 🛠️ Tech Stack

| Technology        | Purpose                     |
| ----------------- | --------------------------- |
| **Python 3.8+**   | Core programming language   |
| **Streamlit**     | Dashboard and web interface |
| **Scikit-learn**  | Machine Learning            |
| **Random Forest** | Mood classification         |
| **Joblib**        | Model serialization         |
| **NumPy**         | Numerical computation       |
| **Pandas**        | Data processing             |
| **SQLite**        | Local data persistence      |

---

## 📁 Project Structure

```text
mind-migrate/
│
├── app.py                  # Main Streamlit dashboard and telemetry logic
├── train_model.py          # Machine Learning model training script
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
│
├── model/
│   └── mood_model.pkl      # Trained Random Forest model
│
└── utils/
    ├── __init__.py
    └── tips.py             # Wellness interventions and advice engine
```

---

## ⚙️ Installation & Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/mind-migrate.git
cd mind-migrate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the Machine Learning Model

```bash
python train_model.py
```

This generates the trained model file:

```text
model/mood_model.pkl
```

### 4. Run the Streamlit Dashboard

```bash
streamlit run app.py
```

The application will open in your browser.

---

## ☁️ Deployment on Streamlit Cloud

To deploy Mind Migrate:

### Step 1 — Push the Project to GitHub

Make sure your repository contains:

```text
app.py
train_model.py
requirements.txt
README.md
utils/
model/
```

### Step 2 — Open Streamlit Cloud

Go to **Streamlit Community Cloud** and sign in using your GitHub account.

### Step 3 — Create a New App

Select:

* **Repository:** Your Mind Migrate GitHub repository
* **Branch:** `main`
* **Main file path:** `app.py`

### Step 4 — Deploy

Click **Deploy**.

After deployment, copy the generated Streamlit URL and replace:

```text
YOUR_STREAMLIT_APP_URL
```

at the top of this README.

---

## 🔄 How Mind Migrate Works

```text
User Interaction
       ↓
Behavioral Telemetry
       ↓
Feature Extraction
       ↓
Machine Learning Model
       ↓
Mental State Classification
       ↓
Contextual Wellness Recommendation
       ↓
User Dashboard
```

---

## 🧪 Machine Learning Pipeline

The system follows a basic Machine Learning workflow:

```text
Behavioral Data
      ↓
Data Preprocessing
      ↓
Feature Extraction
      ↓
Random Forest Classifier
      ↓
Mood / State Prediction
      ↓
Wellness Intervention
```

The Random Forest classifier is trained using behavioral features and used to classify the user's current behavioral state.

---

## 🔒 Privacy

Mind Migrate is designed with privacy considerations in mind.

Key principles include:

* User consent before telemetry collection
* Anonymous mode
* Local data persistence
* Minimal collection of behavioral information
* Processing designed to avoid unnecessary external data transmission

Users should understand what information is collected and how it is processed before using the system.

---

## ⚠️ Disclaimer

Mind Migrate is an experimental **wellness and behavioral monitoring project**.

The predicted states such as *Stressed, Fatigued, Calm,* and *Focused* are machine-learning classifications based on behavioral signals. They should **not be interpreted as medical diagnoses or clinical assessments**.

For persistent or serious mental-health concerns, users should consult a qualified healthcare professional.

---

## 🎯 Future Enhancements

Potential future improvements include:

* Real-time notification system
* More behavioral features
* Personalized ML models
* Improved model accuracy
* Advanced analytics dashboard
* Cloud database integration
* Mobile application
* Long-term behavioral trend analysis
* Explainable AI for predictions
* Improved privacy-preserving telemetry

---

## 👩‍💻 Project

**Mind Migrate**

A Machine Learning and Streamlit-based behavioral wellness monitoring system.

Built using **Python, Streamlit, Scikit-learn, Pandas, NumPy, Joblib, and SQLite**.
