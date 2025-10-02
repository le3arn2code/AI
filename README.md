# AI Labs → le3arn2code / AI

A hands‑on, progressive AI/ML learning repository.  
From basic concepts to real-world mini‑projects, this repo documents a full roadmap of applied Artificial Intelligence labs and experiments.

---

## 🎯 What You’ll Learn

- Core programming and data skills (Python, NumPy, Pandas)  
- Data visualization, cleaning, and preprocessing  
- Fundamental Machine Learning: regression, classification, tree models  
- Ensemble methods, hyperparameter tuning, interpretability  
- Deep learning basics (MLPs, CNNs), NLP fundamentals  
- Mini projects and deployment (Flask, API)  
- Capstone-style project: housing price prediction  

---

## 📂 Repository Structure

```
AI/
├── lab01-introduction-to-ai/             # Introduce AI and basic concepts
├── lab02-setting-up-environment/         # Install Python, libraries
├── lab03-python-basics/                  # Python syntax, data types
├── lab04-intro-to-numpy/                 # Arrays, vectorized ops
├── lab05-intro-to-pandas/                # DataFrames, data manipulation
├── lab06-basic-data-visualization/       # Plots, charts, seaborn/matplotlib
├── lab07-data-preprocessing/             # Cleaning, handling missing, encoding
├── lab08-intro-ml-concepts/              # ML theory: training, loss, etc.
├── lab09-simple-linear-regression/       # Regression lab
├── lab10-simple-logistic-regression/     # Classification with logistic
├── lab11-knn-classification/             # KNN classifier
├── lab12-decision-tree-basics/           # Decision Trees
├── lab13-evaluating-classification/      # Accuracy, precision, recall, F1
├── lab14-train-test-cross-validation/    # Splits, cross-validation
├── lab15-overfitting-vs-underfitting/    # Bias-variance tradeoffs
├── lab16-feature-scaling/                # Normalization, standardization
├── lab17-feature-selection/              # Feature importance, selection
├── lab18-kmeans-clustering/              # Clustering algorithms
├── lab19-model-persistence/              # Saving/loading models
├── lab20-intro-neural-networks/          # Basics of neural nets
├── lab21-mlp-keras/                      # MLP with Keras/TensorFlow
├── lab22-activation-functions/           # ReLU, sigmoid, tanh, etc.
├── lab23-early-stopping-regularization/  # Regularization, early stopping
├── lab24-image-classification/           # CNN & image classification
├── lab25-cnn/                            # Advanced CNN networks
├── lab26-transfer-learning/              # Pretrained models & fine tuning
├── lab27-intro-nlp/                      # Tokenization, embeddings
├── lab28-sentiment/                      # Sentiment classification
├── lab29-text-vectorization/             # Bag‑of‑Words, TF‑IDF
├── lab30-simple-chatbot/                 # Rule-based conversational logic
├── lab31-rl-intro/                       # Reinforcement learning basics
├── lab32-data-augmentation/              # Augment data for robustness
├── lab33-hyperparameter-tuning/          # GridSearch, RandomizedSearch
├── lab34-interpretability/               # LIME, SHAP, feature insights
├── lab35-handling-imbalanced/            # SMOTE, class weighting
├── lab36-timeseries/                     # Forecasting, ARIMA, etc.
├── lab37-pca/                            # Dimensionality reduction
├── lab38-flask-deploy/                   # Deploy model via Flask/app
├── lab39-ensemble-methods/               # Bagging, Boosting, comparison
└── lab40-final-project/                  # Capstone: Housing Price Prediction
```

Each lab folder generally includes:
- `README.md` — objectives, steps, summary  
- `commands.sh` — terminal commands used  
- `troubleshooting.md` — errors encountered & fixes  
- `interview_qna.md` — Q&A for interviews  
- Python or notebook scripts  
- `screenshots/` folder  

---

## 🚀 How to Use It

### 1. Clone the Repo
```bash
git clone https://github.com/le3arn2code/AI.git
cd AI
```

### 2. Setup Python Environment
```bash
python3 -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)
```

### 3. Install Common Dependencies
If there is a `requirements.txt` in the root, run:
```bash
pip install -r requirements.txt
```
Otherwise, each lab contains its own `requirements.txt` or `commands.sh`.

### 4. Run a Lab
Navigate into the lab folder, e.g. `lab40-final-project`, then:
```bash
bash commands.sh   # or `python3 lab40_final_project.py`
```

---

## 🛠 Why This Format Works

- **Modular & Scalable**: Each lab is independent and self-contained  
- **Learner focused**: Step-by-step progression from basics to project  
- **Interview prep**: Q&A files help internalize concepts  
- **Error logs**: `troubleshooting.md` captures real pitfalls and fixes  
- **Verification**: Screenshots confirm that the code runs  

---

## 💡 Best Practices & Tips

- Always commit code **before** making major changes  
- Use Git tags (e.g. `lab40`) to mark stable states  
- Keep `README.md` inside each lab updated with results  
- For long-running labs (DL, training), use checkpoints & logging  
- Try variations: different models, more features, hyperparameter tuning  

---

## 📈 Progress, Metrics & Goals

- Lab completion is tracked by pushing each lab folder  
- Use and compare your results over time  
- Revisit earlier labs and re-run with updated techniques  
- Extend Capstone (Lab 40) by deploying a REST API, adding UI, etc.

---

## 🔗 Links & Acknowledgements

- Datasets used from **Kaggle** & UCI repos  
- Libraries: **NumPy, Pandas, scikit-learn, TensorFlow/Keras, etc.**  
- Inspiration from community tutorials, ML courses, open-source projects  
