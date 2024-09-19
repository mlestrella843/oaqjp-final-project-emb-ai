import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyze.strip():
        return {
            "error": "No input provided.",
            "emotion": None
        }
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj =  { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=myobj, headers=headers)
        
    # Check for HTTP status code 400
    if response.status_code == 400:
        return {
            "error": "Bad request. Input is likely incorrect or unsupported.",
            "emotion": None
        }
        
    # Check for HTTP status code 500
    if response.status_code == 500:
        return {
            "error": "Server error. Please try again later.",
            "emotion": None
        }

    # Parse the response from the API to variable res
    res = json.loads(response.text)

    # Formatting the output
    formatted_output = res['emotionPredictions'][0]['emotion']

    return formatted_output

    # Find the dominant emotion by finding the key with maximiu value
    #dominant_emotion = max(formatted_output, key=lambda x: formatted_output[x])

    #return the dominant emotion as a string
    #return dominant_emotion
    
