# 📊 LIVE YOUTUBE COMMENT SENTIMENT ANALYZER

## 📝 DESCRIPTION
An AI-powered web application that extracts live YouTube comments using Selenium automation and performs real-time sentiment analysis using Natural Language Processing (TextBlob). The system classifies comments into Positive, Neutral, and Negative categories and visualizes results through an interactive Streamlit dashboard with filtering and graphical insights.

---

## 📂 PROJECT STRUCTURE

```
YtSelenium/
│
├── dashboard.py              # Streamlit dashboard (UI + Charts + Filtering)
├── youtube_comments.py       # Selenium logic to scrape YouTube comments
├── sentiment_analysis.py     # Sentiment classification using TextBlob
├── requirements.txt          # Project dependencies
└── README.md                 # Documentation
```

---

## ⚙️ HOW IT WORKS

```
1. User enters YouTube Video URL in Streamlit dashboard
2. Selenium WebDriver launches Chrome browser
3. Script scrolls through YouTube comment section
4. Comments are extracted dynamically
5. Extracted comments are sent to sentiment_analysis.py
6. TextBlob calculates polarity score for each comment

   If polarity > 0  → Positive
   If polarity = 0  → Neutral
   If polarity < 0  → Negative

7. Results are displayed in dashboard:
      - Sentiment Bar Chart
      - Sentiment Pie Chart
      - Filtered Comment Table
```

---

## 🚀 FEATURES

```
✔ Live YouTube Comment Extraction
✔ Automated Scrolling using Selenium
✔ NLP-based Sentiment Classification
✔ Positive / Neutral / Negative Detection
✔ Interactive Bar Chart Visualization
✔ Sentiment Pie Chart
✔ Dropdown Filtering by Sentiment
✔ Real-Time Comment Display
```

---

## 🛠 TECH STACK

```
Language           : Python
Automation Tool    : Selenium
NLP Library        : TextBlob
Web Framework      : Streamlit
Visualization      : Matplotlib
Browser Driver     : ChromeDriver
Data Handling      : Pandas
```


---

## ▶️ INSTALLATION

```
pip install -r requirements.txt
```

---

## ▶️ RUN PROJECT

```
streamlit run dashboard.py
```

---

## 📊 OUTPUT

```
- Total number of comments fetched
- Sentiment distribution (Bar Chart)
- Sentiment percentage breakdown (Pie Chart)
- Filterable comments table
- Real-time sentiment insights
```

---

## 👨‍💻 AUTHOR

Ahamed Jazira M
 ( AI & Data Science Student )
