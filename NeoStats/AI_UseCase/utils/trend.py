def get_trend(score):
    if score > 0.05:
        return "Bullish 📈"
    elif score < -0.05:
        return "Bearish 📉"
    else:
        return "Neutral ➖"