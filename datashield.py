import matplotlib.pyplot as plt
from scipy import stats  
from pandas.plotting import scatter_matrix
import seaborn as sns
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.cluster import KMeans
import streamlit as st
from sklearn.neural_network import MLPRegressor
import hashlib
import json
import os





st.title("Datashield AI")
st.markdown(
        """

        <style>
        .stApp {
           background-color: #00d4ff;
           color: green;

        }
        </style>
        """,

        unsafe_allow_html=True
)




# File to store user data
USER_FILE = "users.json"


# -----------------------------
# Load users from JSON file
# -----------------------------
def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            return json.load(f)
    return {}


# -----------------------------
# Save users to JSON file
# -----------------------------
def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f)


# -----------------------------
# Hash password for security
# -----------------------------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# -----------------------------
# Initialize session state
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""


# -----------------------------
# Load existing users
# -----------------------------
users = load_users()

st.title("🔐 Streamlit Login System")

menu = ["Login", "Register"]
choice = st.sidebar.selectbox("Menu", menu)


# -----------------------------
# REGISTER PAGE
# -----------------------------
if choice == "Register":
    st.subheader("Create New Account")

    new_user = st.text_input("Username")
    new_password = st.text_input("Password", type="password")

    if st.button("Register"):
        if new_user in users:
            st.error("Username already exists!")
        elif new_user == "" or new_password == "":
            st.warning("Please enter username and password.")
        else:
            users[new_user] = hash_password(new_password)
            save_users(users)
            st.success("Account created successfully!")
            st.info("Go to Login menu to sign in.")


# -----------------------------
# LOGIN PAGE
# -----------------------------
elif choice == "Login":
    st.subheader("Login to Your Account")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        hashed_password = hash_password(password)

        if username in users and users[username] == hashed_password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f"Welcome {username}!")
        else:
            st.error("Invalid username or password")


# -----------------------------
# AFTER LOGIN
# -----------------------------
if st.session_state.logged_in:
    st.sidebar.success(f"Logged in as {st.session_state.username}")

    st.header("🏠 Home Page")
    st.write("You are successfully logged in.")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()





































































































        

file = st.file_uploader("Upload your CSV file")

if file is not None:
        try:
                data = pd.read_csv(file, encoding="utf-8")
                st.success("File uploaded successfully")
                st.write(data.head())
                st.write("Rows:", data.shape[0], "Columns:", data.shape[1])
                                                                     

                

        except Exception as e:
                file.seek(0)
                data = pd.read_csv(file, encoding="latin1")
                st.success("File uploaded successfully")
                st.dataframe(data.head())

        columns = data.columns.tolist()
                        

        

        numeric_columns = data.select_dtypes(include=["number"]).columns.tolist()

               
        
                


        chart_type = st.selectbox("Choose Visualization/Model",[
                "Box plot",                 
                "Density plot",
                "Scatter matrix plot",
                "Simple linear regression",
                "Multiple linear regression",
                "Artificial neural network",
                "Histogram",
                "Bar chart",
                "Line chart"
                ])

    


        if chart_type == "Histogram":
                hist_col = st.selectbox("Choose numeric column", numeric_columns, key="hist")

                fig, ax = plt.subplots()
                ax.hist(data[hist_col])
                ax.set_title("Histogram")
               
                st.pyplot(fig)
                plt.savefig("Hist.png")
                
                
               
    


        
     

        elif chart_type == "Box plot":
                box_col = st.selectbox("Choose numeric column", numeric_columns, key="box")

                fig, ax = plt.subplots()
                ax.boxplot(data[box_col].dropna())
                ax.set_title("box plot")
                
                st.pyplot(fig)
                plt.savefig("Box.png")
            




























        elif chart_type == "Line chart":
                line_col = st.selectbox("Choose numeric column", numeric_columns, key="line")
                
                st.line_chart(data[line_col])
                
                plt.savefig("Line.png")
                

















        elif chart_type == "Bar chart":
            bar_col = st.selectbox("Choose numeric column", numeric_columns, key="bar")
            
            st.bar_chart(data[bar_col])

            plt.savefig("Bar.png")
                

                































        elif chart_type == "Scatter matrix plot":
                x_col = st.selectbox("Choose X-axis", numeric_columns)
                y_col = st.selectbox("Choose Y-axis", numeric_columns)

                fig, ax = plt.subplots()
                ax.scatter(data[x_col], data[y_col])
                
                ax.set_title("Scatter box")
                
               
                st.pyplot(fig)
                
                plt.savefig("Scatter.png")
               

        


























        elif chart_type == "Density plot":
                density_col = st.selectbox("Choose numeric column", numeric_columns, key="Density")

                fig, ax = plt.subplots()
                sns.kdeplot(data[density_col].dropna())
                ax.set_title("Density Plot")
               
               
                st.pyplot(fig)
                plt.savefig("Density.png")
               

                














        elif chart_type == "Simple linear regression":
                x_col = st.selectbox("Choose X-axis", numeric_columns)
                y_col = st.selectbox("Choose Y-axis", numeric_columns)

                



        
                X = data[[x_col]]
                y = data[[y_col]]

                model = LinearRegression()
                model.fit(X, y)

                y_pred = model.predict(X)

               
        
               
                fig, ax = plt.subplots()
                ax.scatter(X, y, color='blue')
                ax.plot(X, y_pred, color='red')
               
                ax.set_title("Simple Linear Regression")
                

                st.pyplot(fig)
                plt.savefig("Simple.png")
               
                
               
                 






















                
       

    # -------- Multiple Linear Regression Plot --------
        elif chart_type == "Multiple linear regression":
                x_cols = st.selectbox("Select X-axis ", numeric_columns)
                y_col = st.selectbox("Select Y-axis", numeric_columns)


                if len(x_cols) >0:
                        X = data[[x_cols]]
                        y = data[[y_col]]

                        model = LinearRegression()
                        model.fit(X, y)

                        y_pred = model.predict(X)



                
                
                

                fig, ax = plt.subplots()
                ax.scatter(y, y_pred, color='purple')
               
                

               
                ax.set_title("Actual vs Predicted")
                

                st.pyplot(fig)
                
                plt.savefig("Multiple.png")
               


















                
                       
   
       
               

        elif chart_type == "Artificial neural network":
                x_cols = st.selectbox("Select X-axis", numeric_columns)
                y_col = st.selectbox("Select Y- axis", numeric_columns)

                X = data[[x_cols]]
                y = data[[y_col]]
        

                model = MLPRegressor()
                model.fit(X, y)

                value = st.number_input("Enter value for prediction")

                if st.button("Predict"):
                        prediction = model.predict([[value]])

                        st.write("Prediction:", prediction[0])

                        fig, ax = plt.subplots()
                        ax.scatter(X, y)
                        
                        ax.set_title("ANN")
                        st.pyplot(fig)
                        
                        plt.savefig("ANN.png")

              




