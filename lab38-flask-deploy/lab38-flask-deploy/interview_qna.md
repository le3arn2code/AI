# Interview Q&A: Model Deployment with Flask

**Q1: Why use Flask for ML model deployment?**  
A1: Flask is lightweight, easy to use, and provides full control over REST API endpoints.

**Q2: When would you prefer Streamlit over Flask?**  
A2: Streamlit is better for quick prototypes and interactive dashboards, while Flask is for production APIs.

**Q3: How do you secure a Flask API in production?**  
A3: Use HTTPS, authentication tokens, rate limiting, and run behind a production server like Gunicorn/Nginx.

**Q4: Why do we standardize input data before prediction?**  
A4: To ensure the input matches the same distribution as the training data, avoiding incorrect predictions.

**Q5: What is `pickle` used for in ML deployment?**  
A5: Pickle serializes trained models into files (`.pkl`) so they can be loaded later without retraining.

**Q6: What happens if model.pkl is missing?**  
A6: The Flask app will raise `FileNotFoundError`. Always package the model file with the app.

**Q7: How do you handle large ML models in Flask?**  
A7: Use model compression, load balancing, or deploy on dedicated inference servers.

**Q8: What is the difference between `@app.route('/')` and `@app.route('/predict')`?**  
A8: `'/'` serves the homepage, while `/predict` handles POST requests for predictions.

**Q9: How do you handle multiple ML models in one Flask app?**  
A9: Load each model separately and define separate endpoints for them.

**Q10: What’s the difference between `request.form` and `request.json`?**  
A10: `request.form` handles HTML form data (web forms), while `request.json` processes JSON data from API clients.
