
# Sentiment Analysis Dataset – Reddit Posts

## 📌 Overview

This project involves cleaning and analyzing a dataset of Reddit posts related to Machine Learning. The dataset includes **post metadata** (title, text, score, comments) and **sentiment analysis features** generated using **VADER** and **TextBlob**.

We clean the dataset, visualize key trends, and prepare it for further **NLP tasks** such as topic modeling and sentiment classification.

---

## 📂 Dataset

* **Original file:** `MachineLearning_sentiment.csv`
* **Cleaned file:** `MachineLearning_sentiment_cleaned.csv`

### Columns:

* `title` → Post title
* `selftext` → Post body text
* `score` → Reddit score (upvotes - downvotes)
* `num_comments` → Number of comments
* `created` → Post creation date (converted from UNIX timestamp)
* `author` → Reddit username
* `vader_compound`, `vader_positive`, `vader_negative`, `vader_neutral` → Sentiment scores from VADER
* `textblob_polarity`, `textblob_subjectivity` → Sentiment metrics from TextBlob

---

## 🧹 Data Cleaning Steps

1. Filled missing `selftext` with an empty string.
2. Converted `created` column from **UNIX timestamp** to human-readable datetime.
3. Removed duplicate posts (based on `title` + `selftext`).
4. Final dataset has **829 rows and 12 columns**.

---

## 📊 Visualizations

The following plots were created:

1. **Distribution of Post Scores**
2. **Distribution of VADER Compound Sentiment**
3. **Scatterplot – VADER Compound vs TextBlob Polarity**
4. **Sentiment Trend Over Time (Weekly)**
5. **Word Cloud** of Titles + Selftext

---

## ⚙️ How to Reproduce

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/sentiment-analysis-reddit.git
   cd sentiment-analysis-reddit
   ```
2. Install required libraries:

   ```bash
   pip install pandas matplotlib wordcloud
   ```
3. Run the Jupyter Notebook or Python script:

   ```python
   import pandas as pd
   import matplotlib.pyplot as plt
   from wordcloud import WordCloud
   ```
4. Load the dataset:

   ```python
   df = pd.read_csv("MachineLearning_sentiment.csv")
   ```
5. Apply cleaning steps, generate visualizations, and save the cleaned file:

   ```python
   df.to_csv("MachineLearning_sentiment_cleaned.csv", index=False)
   ```

