import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score

st.title("High Precision Microchip Failure Classification")
st.write("Using Support  Vector Machine")
df = pd.read_csv("microchip_data.csv",header=None,names=["Voltage_Tolerance","Thermal_Stress","Failure"])
st.subheader("Microchip Dataset")
st.dataframe(df.head())
X = df[["Voltage_Tolerance", "Thermal_Stress"]]
y=df["Failure"]
st.sidebar.header("SVM Settings")
kernel = st.sidebar.selectbox( "Select Kernel",["rbf", "linear", "poly"])
C = st.sidebar.slider("C", 0.1, 10.0, 1.0)
gamma = st.sidebar.slider("Gamma",0.01,1.0,0.1)
X_train, X_test, y_train, y_test =train_test_split(X,y,test_size=0.2,random_state=42)
model=SVC(kernel=kernel,C=C,gamma=gamma)
model.fit(X_train,y_train)
y_pred=model.predict(X_tet)
accuracy = accuracy_score(y_test,y_pred)
precision = precision_score(y_test,y_pred,zero_division=0)
st.subheader("Model Performance")
col1, col2 = st.columns(2)
col1.metric("Accuracy",f"{accuracy*100:.2f}%")
col2.metric("Precision",f"{precision * 100:.2f}%")
st.subheader("Microchip Failure Prediction")
Voltage = st.number_input( "Voltage_Tolerance", value=3.3)
thermal = st.number_input("Thermal_Stress", value=45.0)
if st.button("Predict"):
    prediction = model.predict([[Voltage, Thermal]])
    if prediction[0]==0:
        st.success( "Microchip is Functional.")
    else:
        st.error("Microchip is Defective.")
st.subheader("Microchip Data Plot")
fig, ax = plt.subplots()
ax.scatter(
    df["Voltage_Tolerance"],
    df["Thermal_Stress"],
    c=df["Failure"])
ax.set_xlabel("Voltage_Tolerance")
ax.set_ylabel("Thermal_Stress")
ax.set_title("Functional and Defective Microchip ")
st.pyplot(fig)
