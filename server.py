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
    anger_value=response['anger']
    disgust_value=response['disgust']
    fear_value=response['fear']
    joy_value=response['joy']
    sadness_value=response['sadness']
    dominant_value=response['dominant_emotion']
    
    return 'For the given statement, the system response is anger: {}, disgust: {}, fear: {}, joy: {} and sadness: {}. The dominant emotion is {}.'.format(anger_value, disgust_value, fear_value, joy_value, sadness_value, dominant_value)

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)