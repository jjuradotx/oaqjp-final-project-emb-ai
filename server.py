#import libraries and relevant function
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#initiate Flask app
app = Flask("Emotion Detector")

#define function
@app.route("/emotionDetector")
def emot_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    return 'nice'

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)