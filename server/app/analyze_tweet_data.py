import sqlite3
import re

from collections import Counter
import MeCab

import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('../') / '.env'
load_dotenv(dotenv_path=env_path)

def get_tweet_data():
    db_path = os.getenv('DB_PATH')
    connect = sqlite3.connect(db_path)
    db = connect.cursor()
    
    try:
        db.execute("SELECT * FROM tweet_data")
        tweet_data = db.fetchall()

    except sqlite3.Error as e:
        print(e)

    connect.close()
    return tweet_data

def analyze_tweet_data():
    print('---- analyze tweet data ----')

    tweet_data = get_tweet_data()
    mecab = MeCab.Tagger(os.getenv('NEOLOGD'))
    # mecab = MeCab.Tagger("-Ochasen")

    words = {
        # 'all': [],
        'noun': [],
        'verb': [],
        'adjective': [],
        'adverb': []
    }

    #ファイルを読込み
    for tweet in tweet_data:
        text_data = tweet[1]
        text_data = text_data.replace('#FF7リメイク', '')

        reject_words = ['#', '@']
        for word in reject_words:
            text_data = text_data.replace(word, '')
        
        # urlを取り除く
        text_data = re.sub(r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+$,%#]+)", "" , text_data)
        node = mecab.parseToNode(text_data)
        while node:
            word_type = node.feature.split(",")[0]

            if word_type in ["名詞", "動詞", "形容詞", "副詞"]:
                if len(node.surface) > 1:
                    # words['all'].append(node.surface)
                    if word_type == '名詞':
                        words['noun'].append(node.surface)
                    elif word_type == '動詞':
                        words['verb'].append(node.surface)
                    elif word_type == '形容詞':
                        words['adjective'].append(node.surface)
                    else:
                        words['adverb'].append(node.surface)
            node = node.next

    counters = {
        'noun': {},
        'verb': {},
        'adjective': {},
        'adverb': {}
    }
    # counters['all'] = Counter(words['all'])
    counters['noun'] = Counter(words['noun'])
    counters['verb'] = Counter(words['verb'])
    counters['adjective'] = Counter(words['adjective'])
    counters['adverb'] = Counter(words['adverb'])
    
    for counter_key in counters:
        counters[counter_key] = counters[counter_key].most_common(30)

    return counters

if __name__ == '__main__':
    print ('====== Enter Tweet Data file =====')
    analyze_tweet_data()