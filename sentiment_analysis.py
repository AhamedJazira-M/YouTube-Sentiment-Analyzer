import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import pandas as pd
from youtube_comments import get_youtube_comments

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(comments):
    """Perform sentiment analysis on YouTube comments"""
    data = []

    for comment in comments:
        vader_score = sia.polarity_scores(comment)["compound"]
        textblob_score = TextBlob(comment).sentiment.polarity

        sentiment = "Positive" if vader_score > 0 else "Negative" if vader_score < 0 else "Neutral"

        data.append({"comment": comment, "sentiment": sentiment, "vader_score": vader_score, "textblob_score": textblob_score})

    df = pd.DataFrame(data)
    return df
