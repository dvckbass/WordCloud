import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

# read file
file = open("text.txt", "r")
words = file.read()


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", \
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                           "been", "being", \
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
                           "where", "how", \
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very",
                           "can", "will", "just"]

    wordDict = {}
    for word in file_contents.split():
        word = word.lower()
        if word not in punctuations and word not in uninteresting_words:
            if word[-1:] in punctuations:
                word = word[:-1]
            if word[:1] in punctuations:
                word = word[1:]
            if word.isalpha():
                if word not in wordDict:
                    wordDict[word] = 1
                else:
                    wordDict[word] += 1

    # wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(wordDict)
    return cloud.to_array()

# Display wordcloud image

myimage = calculate_frequencies(words)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()