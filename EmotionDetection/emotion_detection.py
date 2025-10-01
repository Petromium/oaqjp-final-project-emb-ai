import requests
import json

def emotion_detector(text_to_analyze):
    """
    Analyzes the input text for emotions using the Watson NLP API.
    Handles blank input by checking the API's response status code.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_payload = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=json_payload, headers=headers)
    
    # New logic: Handle different status codes from the API
    if response.status_code == 200:
        # Successful request
        response_dict = json.loads(response.text)
        emotion_scores = response_dict['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        
        formatted_output = {
            'anger': emotion_scores['anger'],
            'disgust': emotion_scores['disgust'],
            'fear': emotion_scores['fear'],
            'joy': emotion_scores['joy'],
            'sadness': emotion_scores['sadness'],
            'dominant_emotion': dominant_emotion
        }
        return formatted_output
        
    elif response.status_code == 400:
        # This case handles blank entries, as the API returns a 400 error.
        # Return a dictionary with None values as required.
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    else:
        # Handle other potential errors (e.g., 500 Internal Server Error)
        return None