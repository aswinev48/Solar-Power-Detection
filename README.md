# ☀️ Solar Power Generation Prediction System

An interactive **machine learning web application built with Streamlit** to predict solar power generation based on environmental and weather parameters.

This project demonstrates a **complete machine learning workflow**, including data preprocessing, model training, feature scaling, prediction, and web deployment using Streamlit.

The system allows users to dynamically adjust environmental conditions and instantly predict the expected solar power output.

---

# 🔗 Live Deployment

🚀 **Live Streamlit Application**

After deployment your link will look like:

https://aswinev48-solar-power-detection.streamlit.app

The application runs entirely in the browser and allows users to interact with prediction sliders without installing any software.

---

# 🔍 Project Overview

This project builds a **solar power prediction model** using machine learning techniques and deploys it as a **web application**.

The application allows users to input different atmospheric conditions and predict how much solar power will be generated.

The system includes:

📊 Environmental parameter input  
⚙️ Feature scaling using trained scalers  
🤖 Machine learning prediction using a trained regression model  
📈 Real-time power generation prediction  
🌐 Interactive web interface using Streamlit  

---

# ⚡ Prediction Parameters

The model predicts solar power generation based on the following inputs:

| Parameter | Description |
|-----------|-------------|
| Distance to Solar Noon | Time difference from peak solar position |
| Temperature | Atmospheric temperature (°F) |
| Wind Direction | Direction of wind flow |
| Wind Speed | Wind speed in mph |
| Sky Cover | Cloud cover level |
| Humidity | Atmospheric humidity (%) |
| Average Wind Speed | Average wind speed during the period |
| Average Pressure | Atmospheric pressure during the period |

Users can adjust these parameters using interactive sliders.

---

# 🤖 Machine Learning Model

The prediction system uses a **Gradient Boosting Regression model** trained on historical solar power generation data.

### Model Pipeline

1. Data preprocessing  
2. Feature scaling  
3. Model training using Gradient Boosting  
4. Target scaling for accurate predictions  
5. Model serialization using pickle  

The trained components include:

- gbr_model.pkl  
- scaler_features.pkl  
- scaler_target.pkl  

These files are loaded in the Streamlit app to perform real-time predictions.

---

# 📊 Prediction Workflow

The prediction pipeline follows these steps:

1. User selects environmental conditions using sliders  
2. Input values are converted into a feature vector  
3. Features are scaled using the trained feature scaler  
4. Scaled data is passed to the trained model  
5. Model predicts scaled power output  
6. Target scaler converts prediction back to actual units  

Final output is displayed as:

**Predicted Power Generated (joules)**

---

# 📈 Application Interface

The Streamlit interface provides:

✔ Interactive sliders for environmental parameters  
✔ Real-time prediction button  
✔ Clean and responsive UI layout  
✔ Display of predicted solar power generation  

The UI uses **two-column layout** for better user experience.

---

# 📂 Dataset

The dataset used for training contains historical environmental data and solar power generation values.

### Example Features

- Distance to Solar Noon  
- Temperature  
- Wind Direction  
- Wind Speed  
- Sky Cover  
- Humidity  
- Average Wind Speed  
- Average Pressure  
- Power Generated  

Dataset file:

`solarpowergeneration.csv`

---

# 🛠️ Tech Stack

### Programming Language
Python

### Web Application
Streamlit

### Data Handling
Pandas  
NumPy  

### Machine Learning
Scikit-learn  
Gradient Boosting Regressor  

### Model Serialization
Pickle

---

# 🚀 Deployment

Platform used for deployment:

**Streamlit Community Cloud**

Deployment process:

1. Push project files to GitHub  
2. Add dependency list in `requirements.txt`  
3. Connect GitHub repository to Streamlit Cloud  
4. Deploy using `app.py`  

Streamlit automatically redeploys the app whenever updates are pushed to GitHub.

---

# 📁 Project Structure

```
Solar-Power-Detection
│
├── app.py
├── solarpowergeneration.csv
├── gbr_model.pkl
├── scaler_features.pkl
├── scaler_target.pkl
├── Project_Dep.ipynb
├── requirements.txt
└── README.md
```

---

# 🎯 Project Applications

This project demonstrates concepts useful for:

📊 Data Science projects  
⚡ Renewable energy forecasting  
📚 Academic machine learning projects  
💼 Data science portfolio projects  

---

# 📌 Future Improvements

Possible enhancements include:

📈 Visualization of prediction trends  
📊 Feature importance analysis  
⚡ Integration with real-time weather APIs  
📉 Solar energy production dashboards  
