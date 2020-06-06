import matplotlib.pyplot as plt
import japanize_matplotlib
import re

from collections import Counter

def graph_data(counter_list):
    graph = {'x': [], 'y': []}
    for counter in counter_list:
        x, y = counter
        graph['x'].append(x)
        graph['y'].append(y)
    graph['x'].reverse()
    graph['y'].reverse()
    return graph

def graph_tweet(counters):
    fig = plt.figure(figsize=(12, 8))
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)
    ax4 = fig.add_subplot(2, 2, 4)

    c1,c2,c3,c4 = "blue","green","red","black"
    l1,l2,l3,l4 = "名詞","動詞","形容詞","副詞"

    # graph_data_all = graph_data(counters['all'])
    graph_data_noun = graph_data(counters['noun'])
    graph_data_verb = graph_data(counters['verb'])
    graph_data_adjective = graph_data(counters['adjective'])
    graph_data_adverb = graph_data(counters['adverb'])

    ax1.barh(graph_data_noun['x'], graph_data_noun['y'], color=c1, label=l1)
    ax2.barh(graph_data_verb['x'], graph_data_verb['y'], color=c2, label=l2)
    ax3.barh(graph_data_adjective['x'], graph_data_adjective['y'], color=c3, label=l3)
    ax4.barh(graph_data_adverb['x'], graph_data_adverb['y'], color=c4, label=l4)
    ax1.legend(loc = 'lower right')
    ax2.legend(loc = 'lower right')
    ax3.legend(loc = 'lower right')
    ax4.legend(loc = 'lower right')

    fig.tight_layout()

    # plt.barh(graph_data_all['x'], graph_data['y'])
    plt.show()

if __name__ == '__main__':
    graph_tweet(counters)