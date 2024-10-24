import gradio as gr
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER lexicon
nltk.download('vader_lexicon', quiet=True)

def perform_sentiment_analysis(text):
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text)

def categorize_sentiment(compound_score):
    # Adjusting thresholds for a more balanced classification
    if compound_score > 0.1:  # Increased positive threshold
        return 'Positive'
    elif compound_score < -0.1:  # Increased negative threshold
        return 'Negative'
    else:
        return 'Neutral'

def analyze_sentiment(input_text):
    scores = perform_sentiment_analysis(input_text)
    sentiment = categorize_sentiment(scores['compound'])
    return {"Sentiment": sentiment, "Scores": scores}

# Example Reddit posts for sentiment analysis
examples = [
    "Just got a new job and I'm so excited! The team seems great and the work looks interesting.",  # Positive
    "I'm really frustrated with how the job market is right now. It's so unfair.",    # Negative
    "Hey John, did you finish your intro to Machine Learning textbook?",  # Neutral
    "I hate Data structures.",  # Negative
    "I really enjoyed the last movie I watched; it was captivating and well-made.",  # Positive
    "Where are you ?",  # Neutral
]

demo = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(label="Enter text for sentiment analysis", placeholder="Type your text here..."),
    outputs="json",
    title="Sentiment Analysis Tool using Reddit Data",
    description=(
        "Enter text to see the sentiment analysis result. You can also use the examples below to test different sentiments."
    ),
    examples=examples  # Add the Reddit examples here
)

demo.launch()