import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score
st.set_page_config( page_title="Microchip Failure Classification",page_icon="🔬")
st.title("🔬 High Precision Microchip Failure Classification")
st.write("SVM based Functional vs Defective Microchip Classification")
st.sidebar.title("⚙️ Model Settings")
kernel = st.sidebar.selectbox( "Select Kernel",["rbf", "linear", "poly"])
C=st.sidebar.slider("C ", 0.1,200.0,100.0)
gamma = st.sidebar.selectbox( "Gamma",0.1,1.0,10.0)
df = pd.read_csv("microchip_data.csv")
st.subheader("Dataset")
st.dataframe(df.head())
X = df[["Voltage_Tolerance","Thermal_Stress"]]
y=df[["Failure"]]
X_train, X_test,y_train, y_test=train_test_split(X,y,test_size=0.2,random_state=42)
scaler = StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)
model=SVC(kernel=kernel,C=C,gamma=gamma)
model.fit(X_train_scaled,y_train)
y_pred =model.predict(X_test_scaled)
accuracy =accuracy_score(y_test,y_pred)
precision = precision_score(  y_test, y_pred, zero_division=0)
col1,col2 = st.columns(2)
col1.metric("Accuracy",f"{accuracy*100:.2f}%")
col2.metric("Precision",f"{precision * 100:.2f}%")
st.subheader(" Microchip Data Plot")
fig, ax = plt.subplots()
ax.scatter(df["Voltage_Tolerance"],df["Thermal_stress"],c=y,cmap='bwr')
ax.set_title("Functional Microchip vs Defective Microchip")
st.pyplot(fig)
st.subheader("🔮 Microchip Prediction")
V_Tolerance = st.number_input("Voltage_Tolerance",value=0.5)
T_Stress = st.number_input("Thermel_Stress",value=0.5)

if st.button("Predict"): 
    new_data = [[V_Tolerance,T_Stress ]]
    new_data_scaled = scaler.transform( new_data)
    
    result = model.predict(new_data_scaled)
    if result[0] == 1:
       st.error("Defective Microchip" )
    else:
        st.success( "Functional Microchip" )
