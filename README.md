# Sentiment_Analysis_Hugging_Face_Model

This project is a simple Sentiment Analysis Tool that uses the VADER model from nltk to classify text as Positive, Neutral, or Negative. It provides a user-friendly interface built with Gradio for easy interaction.


## Features
- Simple user interface to input custom text for sentiment analysis.
- Pre-built examples for testing different sentiment categories.
- JSON output displaying sentiment and individual sentiment scores.

## Demo
You can run this demo on Hugging Face Spaces: [https://huggingface.co/spaces/JohnJoelMota/Sentiment_Analysis].

## How It Works
This project is a Sentiment Analysis Tool built using VADER ([VADER sentiment analysis tool](https://github.com/cjhutto/vaderSentiment)) from the nltk library to classify text as **Positive**, **Neutral**, or **Negative**. It features an easy-to-use interface powered by [Gradio](https://gradio.app/).

The text is analyzed, and the sentiment is categorized as:
- **Positive** if the sentiment score > 0.1
- **Negative** if the sentiment score < -0.1
- **Neutral** otherwise

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/sentiment-analysis-reddit.git
    cd sentiment-analysis-reddit
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    python app.py
    ```

4. Access the Gradio interface on your local machine through the provided URL (usually `http://localhost:7860`).

## Project Files

### `app.py`
This file contains the main code to run the sentiment analysis app using Gradio. It includes functions for analyzing text sentiment using the VADER tool and a simple interface to input text and view sentiment results.

### `requirements.txt`
Lists the dependencies required to run the project:
- `pandas`
- `numpy`
- `nltk`

## License

This project is licensed under the Apache-2.0 License - see the [LICENSE](LICENSE) file for details.
