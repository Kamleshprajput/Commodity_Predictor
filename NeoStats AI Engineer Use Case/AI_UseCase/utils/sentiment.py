from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

def get_sentiment(news_list):
    scores = []
    for text in news_list:
        score = analyzer.polarity_scores(text)["compound"]
        scores.append(score)

    return sum(scores) / len(scores)