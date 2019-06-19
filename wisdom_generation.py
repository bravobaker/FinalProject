import markovify
import json

with open('data/wisdom_model.json', 'r') as f:
    #wisdom_model = json.load(f)
    WISDOM_MODEL = markovify.Text.from_json(json.load(f))

def generate_wisdom(n=3, model=WISDOM_MODEL):
    wisdom = []
    for i in range(n):
        piece = model.make_sentence()
        if piece!=None:
            wisdom.append(piece)
    wisdom = ' '.join(wisdom)
    return wisdom

def is_question(m):
    s = m.text
    return s.endswith('?') or s.lower().startswith(('how ',
                                                    'when ',
                                                    'where ',
                                                    'what ',
                                                    'who ',
                                                    'which ',
                                                    'did ',
                                                    'do ',
                                                    'does ',
                                                    'is ',
                                                    'am ',
                                                    'are ',
                                                    'am ',
                                                    'will ',
                                                    'have ',
                                                    'has ',
                                                    'please ',
                                                    'tell ',
                                                    'share ',
                                                    'o '))
def not_question(m):
    s = m.text
    return not (s.endswith('?') or s.lower().startswith(('how ',
                                                    'when ',
                                                    'where ',
                                                    'what ',
                                                    'who ',
                                                    'which ',
                                                    'did ',
                                                    'do ',
                                                    'does ',
                                                    'is ',
                                                    'am ',
                                                    'are ',
                                                    'am ',
                                                    'will ',
                                                    'have ',
                                                    'has ',
                                                    'please ',
                                                    'tell ',
                                                    'share ',
                                                    'o ')))
