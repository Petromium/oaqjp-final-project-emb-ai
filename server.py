# File: server.py

"""
This script runs a Flask web server that provides an interface for
the emotion detection application.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """
    Renders the main HTML page which serves as the user interface.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detection_service():
    """
    Analyzes text from a web request and returns the formatted emotion analysis.
    Includes error handling for invalid or blank inputs.
    """
    # Get the text to analyze from the request's query parameters
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the core emotion_detector function from our package
    response = emotion_detector(text_to_analyze)

    # Check for the error condition where dominant_emotion is None.
    # This single check handles blank inputs and other API errors gracefully.
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    # If the response is valid, format the output string as required
    output_string = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return output_string

if __name__ == '__main__':
    # Run the Flask app on localhost, port 5000, accessible from the network
    app.run(host='0.0.0.0', port=5000)
    