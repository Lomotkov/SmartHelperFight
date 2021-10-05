from functions.Answers import *
from functions.GenerateResp import generate_response_text


def handler(event, context):
    text = event['request']['original_utterance'].lower()
    if 'request' in event and \
            'original_utterance' in event['request']:
        if 'дим' in text or 'дмитр' in text or 'ломот' in text:
            return dima(event)
        if 'стрел' in text:
            return shot(event)
        if 'враг' in text:
            return enemy(event)
        if 'бой' in text:
            return fight(text, event)
    return generate_response_text("Будем стоять медитировать, или будем драться", event)
