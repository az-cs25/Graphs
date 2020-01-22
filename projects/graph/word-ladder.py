# https: // leetcode.com/problems/word-ladder/

# Given two words(beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

# Note:

# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.

# words are nodes, one-letter-apart is edges
# do a BFS from start word to end word

from util import Stack, Queue  # These may come in handy
from graph import Graph
import string

f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()

word_set = set()
for word in words:
    word_set.add(word.lower())

# print(len(word_set))


def get_neighbors(word):
    '''
    return all words from word_list that are one letter different
    '''
    neighbors = []
    alphabet = list(string.ascii_lowercase)
    # for each letter in the word,
    for i in range(len(word)):
        # for each letter in the alphabet
        for letter in alphabet:
            # change the word letter to the alphabet letter
            list_word = list(word)
            list_word[i] = letter
            w = "".join(list_word)
            # if the new word is in the word_set:
            if w != word and w in word_set:
                # add it to neighbors
                neighbors.append(w)

    return neighbors


# print(get_neighbors('cat'))


def find_ladders(begin_word, end_word):
    # create a queue
    qq = Queue()

    # Enqueue a path to the starting word
    qq.enqueue([begin_word])
    # Create a visited set
    visited = set()
    # while queue is not empty:
    while qq.size() > 0:
        # dequeue the next path
        path = qq.dequeue()
        # Grab the last word from the path
        vertex = path[-1]
        # check if the word is our end word, if so return path
        if vertex not in visited:
            if vertex == end_word:
                return path
            # if not visited, mark it as visited
            visited.add(vertex)

        # Enqueue a path to each neighbor
            for neighbor in get_neighbors(vertex):
                path_copy = path.copy()
                path_copy.append(neighbor)
                qq.enqueue(path_copy)


print(find_ladders('sail', 'boat'))
