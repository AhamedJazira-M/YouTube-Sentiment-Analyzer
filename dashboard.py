import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
from youtube_comments import get_youtube_comments
from sentiment_analysis import analyze_sentiment

st.set_page_config(page_title="YouTube Sentiment Analyzer", layout="centered")
st.title("📊 YouTube Comment Sentiment Analysis with Selenium")

# Text input and Analyze button
video_url = st.text_input("Paste the YouTube video link")

if st.button("Analyze"):
    with st.spinner("Fetching comments..."):
        comments = get_youtube_comments(video_url)

    if not comments:
        st.error("❌ No comments found or invalid video link!")
        st.session_state.df = None
    else:
        st.success(f"✅ Successfully fetched {len(comments)} comments!")
        df = analyze_sentiment(comments)
        st.session_state.df = df  # Save to session state

# Only display analysis results if we have data
if "df" in st.session_state and st.session_state.df is not None:
    df = st.session_state.df
    sentiment_counts = df["sentiment"].value_counts()

    # 🔥 Interactive bar chart
    st.subheader("📊 Sentiment Distribution (Interactive)")
    fig = px.bar(
        sentiment_counts,
        x=sentiment_counts.index,
        y=sentiment_counts.values,
        color=sentiment_counts.index,
        color_discrete_map={"Positive": "green", "Neutral": "gray", "Negative": "red"},
        labels={"x": "Sentiment", "y": "Count"},
        title="Interactive Sentiment Distribution"
    )
    st.plotly_chart(fig)

    # 🔥 AI-Based Summary
    st.subheader("🧠 AI-Based Sentiment Summary")
    positive = df[df["sentiment"] == "Positive"].shape[0]
    neutral = df[df["sentiment"] == "Neutral"].shape[0]
    negative = df[df["sentiment"] == "Negative"].shape[0]

    st.markdown(f"- ✅ Positive Comments: **{positive}**")
    st.markdown(f"- 😐 Neutral Comments: **{neutral}**")
    st.markdown(f"- ❌ Negative Comments: **{negative}**")

    if positive > negative:
        st.success("😊 The overall sentiment is mostly **positive**.")
    elif negative > positive:
        st.error("😠 The overall sentiment is mostly **negative**.")
    else:
        st.info("😐 The sentiment is quite **balanced**.")

    # 🔥 Filter dropdown outside the button click
    st.subheader("💬 Filter Comments by Sentiment")
    sentiment_filter = st.selectbox("Choose sentiment to display", ["All", "Positive", "Neutral", "Negative"])

    if sentiment_filter != "All":
        filtered_df = df[df["sentiment"] == sentiment_filter]
    else:
        filtered_df = df

    st.dataframe(filtered_df[["comment", "sentiment"]])

    # 🔥 Pie Chart
    st.subheader("📊 Sentiment Pie Chart")
    fig2, ax = plt.subplots()
    ax.pie(
        sentiment_counts,
        labels=sentiment_counts.index,
        autopct="%1.1f%%",
        colors=["green", "gray", "red"]
    )
    ax.axis("equal")
    st.pyplot(fig2)
