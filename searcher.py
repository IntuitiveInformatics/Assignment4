from collections import defaultdict
import json, re
from nltk.stem import PorterStemmer

# Get User Input
# Tokenize Input
# If exists in Master Dict
# Then display results by doing:stepping into the dictionary and
# find the token class pertaining to the input token
# go to tokenclass.doc_and_freq and use this as dict


max_url_output = 10
max_docs = 200

counter = 0 # only need top ten of them shits, so this keeps track

sample_dict = {} # main dict
output_dict = {} # to hold possible output results, key = doc_id, value = URL
two_ave_tfidf = 0
three_ave_tfidf = 0


def tokenize(text):
    stemmer = PorterStemmer()                       # This is the stemmer
    words = (re.sub('[\W_]', ' ', text).lower())    # This gets rid of any non-alphanumerics
    token_list = words.split()                      # This splits the words at any white-space
    wordlist = []                     # Creating a defaultDictionary
    for token in token_list:                        # For every token in the query
        stemmed = stemmer.stem(token)               # Stem it
        if stemmed not in wordlist:
            wordlist.append(stemmed)                      # add it to the defaultDictionary
    return len(wordlist), wordlist

    """
    words = (re.sub('[\W_]', ' ', text).lower())
    token_list = words.split()
    wordlist = {}
    for token in token_list:
        if token not in wordlist:
            wordlist[token] = 0
        wordlist[token] += 1
    #order(wordlist)
    return wordlist
    """

with open("tokens.json", "r") as a:
    wordList = json.load(a)     # Open the Json
    print(len(wordList))        # Print how many unique words there are in the dictionary
    variable = input("Search for something!: ")        # How we are going to be getting the query until we write a GUI
    query_length, words = tokenize(variable)            # This counts the query length and holds the words that were tokenized/stemmed
    print(words)                                        # This prints the query list
    if (query_length < 1):
        print('No input, cannot process empty input')
    elif (query_length < 2):
        counter = 0
        for k, v in sorted(wordList[words[0]]["doc_and_freq"].items(),
                           key=lambda x: -x[1]):  # NOTE: switch one to first entered token
            if counter > 9:
                break
            counter += 1
            print(str(v) + '\t' + k + '\t' + wordList[words[0]]["doc_and_url"][k])
    elif (query_length <= 2):  # <= 2 key words entered
        counter = 0
        for k, v in sorted(wordList[words[1]]["doc_and_freq"].items(), key=lambda x: -x[1]):
            two_ave_tfidf += v
            counter += 1
            if (counter >= max_docs):
                break
        two_ave_tfidf /= float(counter)  # create ave based on max_docs or less

        counter = 0
        for k, v in sorted(wordList[words[0]]["doc_and_freq"].items(), key=lambda x: -x[1]):
            # going to have to test this if statement, not sure if python works optimal enough to skip
            # the second check if first failed in an and statement
            if (counter >= max_url_output):
                break
            if (k in wordList[words[1]]["doc_and_freq"].keys()):
                if wordList[words[1]]["doc_and_freq"][k] >= two_ave_tfidf:
                    if (k not in output_dict.keys()):  # dont overwrite a previous entry
                        output_dict[k] = wordList[words[0]]["doc_and_url"][k]  # add to output dict
                        counter += 1

        if (counter < max_url_output):  # if we didn't get enough output results, fill with next best results
            for k, v in sorted(wordList[words[0]]["doc_and_freq"].items(), key=lambda x: -x[1]):
                if (counter >= max_url_output):
                    break
                if (k not in output_dict.keys()):
                    output_dict[k] = wordList[words[0]]["doc_and_url"][k]
                    counter += 1

    else:  # > 2 entries
        counter = 0
        for k, v in sorted(wordList[words[0]]["doc_and_freq"].items(), key=lambda x: -x[1]):
            two_ave_tfidf += v
            three_ave_tfidf += v
            counter += 1
            if (counter >= max_docs):
                break
        two_ave_tfidf /= float(counter)  # create ave based on max_docs
        counter = 0
        for k, v in sorted(wordList[words[1]]["doc_and_freq"].items(), key=lambda x: -x[1]):
            two_ave_tfidf += v

            counter += 1
            if (counter >= max_docs):
                break
        three_ave_tfidf /= float(counter)  # create ave based on max_docs
        counter = 0

        for i in words:  # not n^3 ... i,j,k will be < 4 90% of the time, ie. 3^3 = 27 = O(constant), O(27N)
            if (counter >= max_url_output):
                break
            for j in words:
                if (i == j or counter >= max_url_output):
                    break
                for k in words:
                    if (i == k or i == j or j == k or counter >= max_url_output):
                        break
                    for key, value in sorted(wordList[i]["doc_and_freq"].items(), key=lambda x: -x[1]):
                        if (key in wordList[j]["doc_and_freq"].keys() and key in wordList[
                            k]["doc_and_freq"].keys() and counter < max_url_output):
                            if (wordList[j]["doc_and_freq"][key] >= two_ave_tfidf and wordList[k]["doc_and_freq"][
                                key] >= three_ave_tfidf):
                                output_dict[key] = wordList[j]["doc_and_url"][key]
                                counter += 1
        if (counter < max_url_output):  # if this occurs then efficency will decrease by at most n
            for key, value in sorted(wordList[words[0]]["doc_and_freq"].items(), key=lambda x: -x[1]):
                if (key not in output_dict.keys() and counter < max_url_output):
                    output_dict[key] = wordList[words[0]]["doc_and_url"][key]
                    counter += 1

for k, v in output_dict.items():  # Display them dicked items from best to worst
    print(k + ':\t' + v)





