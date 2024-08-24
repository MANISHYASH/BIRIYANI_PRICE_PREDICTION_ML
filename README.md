Biryani Price Prediction using Machine Learning & Streamlit

Project Overview 
-----------------
This project is designed to predict the price of biryani based on various input factors using a machine learning model. The goal is to develop a user-friendly application where users can input key ingredients and the chef's experience to receive an accurate price prediction. The application is built using Streamlit and integrates with a deployed machine learning model via an API.

Objective
---------
To develop a machine learning model that predicts the price of biryani based on selected input factors.
To create a Streamlit application that allows users to input ingredient prices and chef experience, and dynamically display the predicted biryani price.
To ensure seamless integration with an API that hosts the machine learning model for real-time predictions.

Data Description The model uses the following input parameters to predict the biryani price:
----------------
Chicken Price: The cost of chicken used in the biryani.
Rice Price: The cost of rice used in the biryani.
Vegetable Price: The cost of vegetables included in the biryani.
Spices Price: The cost of spices added to the biryani.
Chef Experience: The experience level of the chef preparing the biryani, which may influence the quality and price.

Tools and Technologies
----------------------
Machine Learning Model: Deployed using Modelbit for real-time predictions. Linear Regression was used to develop the model.
API Integration: Interaction with the machine learning model through an API.
Web Application: Built using Streamlit to create an interactive user interface.
Programming Language: Python, for both backend and frontend development.

Model Deployment
----------------
Model Training:
The machine learning model was trained using historical data of biryani prices and the associated ingredient costs and chef experience.
Linear Regression was employed as the algorithm to predict biryani prices.

API Deployment:
The trained model was deployed via Modelbit and exposed through an API endpoint for real-time predictions.
Model Training
---------------
The machine learning model was trained using historical data of biryani prices and the associated ingredient costs and chef experience.
Linear Regression was employed as the algorithm to predict biryani prices.
API Deployment:

The trained model was deployed via Modelbit and exposed through an API endpoint for real-time predictions.
Streamlit Application Features:

Input Fields: Users can input the prices of chicken, rice, vegetables, spices, and the chef's experience.
Predict Button: On clicking the button, the app fetches the predicted price via the API and displays it to the user.
User-Friendly Interface: The application provides an intuitive interface for easy interaction.
Conclusion This project successfully demonstrates the integration of machine learning with web applications, providing a practical tool for predicting the price of biryani based on key ingredients and chef experience.

Conclusion 
----------
This project successfully demonstrates the integration of machine learning with web applications, providing a practical tool for predicting the price of biryani based on key ingredients and chef experience.

