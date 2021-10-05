def generate_response_with_tts(text, tts, music_source, event):
    return {
        'version': event['version'],
        'session': event['session'],
        'response': {
            "text": text,
            "tts": tts + " " + music_source,
            'end_session': 'false',
            "should_listen": 'false',
        }
    }


def generate_response_text(text, event):
    return {
        'version': event['version'],
        'session': event['session'],
        'response': {
            "text": text,
            'end_session': 'false',
            "should_listen": 'false',
        }
    }
