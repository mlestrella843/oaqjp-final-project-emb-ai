import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj =  { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=myobj, headers=headers)

    # Parse the response from the API to variable res
    res = json.loads(response.text)
    
    # Formatting the output
    formatted_output = res['emotionPredictions'][0]['emotion']
    
    # Find the dominant emotion by finding the key with maximiu value
    dominant_emotion = max(formatted_output, key=lambda x: formatted_output[x])

    #return the dominant emotion as a string
    return dominant_emotion

