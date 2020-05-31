import matplotlib.pyplot as plt
import japanize_matplotlib
import sqlite3
import re

from collections import Counter
import MeCab

import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('../') / '.env'
load_dotenv(dotenv_path=env_path)

def graph_data(counter_list):
    graph = {'x': [], 'y': []}
    for counter in counter_list:
        x, y = counter
        graph['x'].append(x)
        graph['y'].append(y)
    graph['x'].reverse()
    graph['y'].reverse()
    return graph

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

    # fig = plt.figure(figsize=(12, 8))
    # ax1 = fig.add_subplot(2, 2, 1)
    # ax2 = fig.add_subplot(2, 2, 2)
    # ax3 = fig.add_subplot(2, 2, 3)
    # ax4 = fig.add_subplot(2, 2, 4)

    # c1,c2,c3,c4 = "blue","green","red","black"
    # l1,l2,l3,l4 = "名詞","動詞","形容詞","副詞"

    # graph_data_all = graph_data(counters['all'])
    # graph_data_noun = graph_data(counters['noun'])
    # graph_data_verb = graph_data(counters['verb'])
    # graph_data_adjective = graph_data(counters['adjective'])
    # graph_data_adverb = graph_data(counters['adverb'])

    # ax1.barh(graph_data_noun['x'], graph_data_noun['y'], color=c1, label=l1)
    # ax2.barh(graph_data_verb['x'], graph_data_verb['y'], color=c2, label=l2)
    # ax3.barh(graph_data_adjective['x'], graph_data_adjective['y'], color=c3, label=l3)
    # ax4.barh(graph_data_adverb['x'], graph_data_adverb['y'], color=c4, label=l4)
    # ax1.legend(loc = 'lower right')
    # ax2.legend(loc = 'lower right')
    # ax3.legend(loc = 'lower right')
    # ax4.legend(loc = 'lower right')

    # fig.tight_layout()

    # # plt.barh(graph_data_all['x'], graph_data['y'])
    # plt.show()

if __name__ == '__main__':
    print ('====== Enter Tweet Data file =====')
    analyze_tweet_data()