import requests

def speech_to_text(audio_data):
    url = "https://api.openai.com/v1/whisper/speech"
    headers = {"Authorization": "Bearer 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", "Content-Type": "audio/wav"}
    response = requests.post(url, headers=headers, data=audio_data)
    response.raise_for_status()
    return response.json()["text"]
