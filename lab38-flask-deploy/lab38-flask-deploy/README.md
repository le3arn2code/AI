# Lab 38: Deploying a Model Locally with Flask

## Overview
In this lab, we learned how to deploy a machine learning model locally using **Flask**.  
We created a minimal web app, loaded a pre-trained model, and exposed prediction endpoints.  
We also tested predictions via **curl (CLI)** and through a simple HTML form.

## Objectives
- Understand how to deploy ML models using Flask.
- Create a minimal web application.
- Load a pre-trained model (`model.pkl`) for predictions.
- Accept user input and display prediction results.

## Results
- Flask app successfully deployed on `http://127.0.0.1:5000`.
- `/predict-form` route allows user input via HTML form.
- Predictions tested using CLI `curl` and confirmed working (`Prediction: [0]`).
