"""Module providing a server functionality via flask."""


#import libraries and relevant function
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#initiate Flask app
app = Flask("Emotion Detector")

#define function
@app.route("/emotionDetector")
def emot_detector():
    """Function printing emotion detection."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger_value=response['anger']
    disgust_value=response['disgust']
    fear_value=response['fear']
    joy_value=response['joy']
    sadness_value=response['sadness']
    dominant_value=response['dominant_emotion']
    if dominant_value is None:
        return "Invalid Text! Please try again."
    return f"For the given statement, \
    the system response is anger: {anger_value}, \
    disgust: {disgust_value}, \
    fear: {fear_value}, \
    joy: {joy_value} and sadness: {sadness_value}. \
    The dominant emotion is {dominant_value}."

@app.route("/")
def render_index_page():
    """Function rendering index html page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
