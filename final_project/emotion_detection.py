import requests
import json

def emotion_detector(text_to_analyze):
  url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
  header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
  myobj= { "raw_document": { "text": text_to_analyze } }
  response = requests.post(url, json = myobj, headers=header)
  json_response = json.loads(response.text)
  
  desired_output = {}

  if response.status_code == 200:
    desired_output = json_response['emotionPredictions'][0]['emotion']
    desired_output['dominant_emotion'] = max(desired_output, key=desired_output.get)

  elif response.status_code == 400:
    desired_output['anger'] = None
    desired_output['disgust'] = None
    desired_output['fear'] = None
    desired_output['joy'] = None
    desired_output['sadness'] = None
    desired_output['dominant_emotion'] = None
    
  return desired_output