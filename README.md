# Amazon Product Rating Predictions

This project constructs and compares **regression models** to estimate the **average rating of Amazon products** using various product and review features. The goal is to help **Amazon vendors better understand market trends**, identify review-driven insights, and improve marketing strategies.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Dataset](#dataset)
- [Models](#models)
- [Text Representation](#text-representation)
- [Feature Importance](#feature-importance)
- [Results](#results)
- [Conclusions](#conclusions)
- [Benefits](#benefits)

---

## Overview

The project compares **Linear Regression** and **Multi-Class Logistic Regression** models to predict product ratings based on structured and unstructured data from Amazon reviews.  
By analyzing trends in reviews and product metadata, vendors can derive **actionable business insights** about what factors drive positive or negative feedback.

---

## Features

- Linear and Logistic Regression models for rating prediction  
- TF-IDF and Sentence Transformer embeddings for text analysis  
- K-fold cross-validation for robust performance evaluation  
- Feature importance analysis for key review words  
- Data visualization with Matplotlib and Seaborn  
- Model interpretability with LIME  

---

## Dataset

- **1,465 reviews** collected from January 2023  
- **1,351 unique products**  
- **1,194 unique reviewers**  
- Mostly **technical products**  
- **Label:** Average rating  

### Key Features
- Product category  
- Price (discounted and actual)  
- Text content of reviews  

---

## Models

### Linear Regression
- Predicts actual vs. predicted product ratings
- Evaluated model performance using visualization and regression metrics

### Multi-Class Logistic Regression
- Implemented with **Scikit-learn’s Logistic Regression** package  
- **5-fold cross-validation**  
- **Average accuracy score:** 95.28%  
- **Target variable:** Review score (multiclass)  
- Both **TF-IDF** and **Sentence Transformer embeddings** achieved the same accuracy  

---

## Text Representation

Two techniques were used to transform review text into numerical features:

1. **TF-IDF (Term Frequency–Inverse Document Frequency)**  
   - Traditional bag-of-words approach capturing word frequency and importance  

2. **Sentence Transformers (Semantic Embeddings)**  
   - Captures contextual meaning and relationships between words  

Both methods produced **strong, consistent performance** given the small dataset and short review text (e.g., “Good product”, “Poor quality”).

---

## Feature Importance

Words contributing most strongly to **positive** vs. **negative** reviews:

| Sentiment | Key Words |
|------------|------------|
| **Positive** | Easy, Installation, Instagram, Instant |
| **Negative** | Charging, Price, Battery, Power, Weight |

---

## Results

- Both text representation methods achieved **95.28% mean accuracy**
- Logistic regression effectively classified review sentiments
- Linear regression provided reliable average rating predictions

---

## Conclusions

- Users prioritize **easy installation** and **smooth setup experiences**
- Social media (e.g., **Instagram**) influences product discovery
- **Battery life and power issues** are frequent causes of dissatisfaction
- Potential **advertising opportunities** for tech vendors to highlight ease-of-use and reliability

---

## Benefits

- Helps vendors **predict product performance** before launch  
- Identifies **patterns in positive and negative reviews**  
- Turns Amazon reviews into **actionable marketing and product insights**  

---


