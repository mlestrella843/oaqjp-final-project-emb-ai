from flask import Flask, render_template, request, Response
import json
from EmotionDetection.emotion_detection import emotion_detector  # Make sure this import is correct

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    ''' This function renders the main application page '''
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_server():
    ''' 
    This function receives the text from the HTML interface and performs emotion analysis 
    using the emotion_detector function. It returns the analysis as plain text.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract emotions and their scores
    emotions = {
        'anger': response['anger'],
        'disgust': response['disgust'],
        'fear': response['fear'],
        'joy': response['joy'],
        'sadness': response['sadness']
    }

    # Determine the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # Create the response text with the scores and dominant emotion
    result_text = (
        f"For the given statement, the system response is "
        f"'anger': {emotions['anger']:.9f}, 'disgust': {emotions['disgust']:.10f}, "
        f"'fear': {emotions['fear']:.9f}, 'joy': {emotions['joy']:.7f} and 'sadness': {emotions['sadness']:.8f}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    # Return the response as plain text
    return Response(result_text, mimetype='text/plain')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5009)

