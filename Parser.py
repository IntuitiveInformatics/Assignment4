from collections import defaultdict
import re, sys, time, json, nltk
from bs4 import BeautifulSoup
from tester import TokenInfo
from nltk.stem import PorterStemmer

def tokenize(text, stemmer):
    words = (re.sub('[\W_]', ' ', text).lower())
    token_list = words.split()
    wordlist = defaultdict(int)
    for token in token_list:
        stemmed = stemmer.stem(token)
        wordlist[stemmed] += 1
    return len(token_list), wordlist

    # Start of the old code
    # words = (re.sub('[\W_]', ' ', text).lower())
    # token_list = words.split()
    # wordlist = defaultdict(int)
    # for token in token_list:
    #    wordlist[token] += 1
    # return len(token_list), wordlist


def order(defdict):
    ordered = []
    orderednumbers = []
    for k, v in sorted(defdict.items(), key=lambda x: (-x[1], x[0])):
        ordered.append(k)
        orderednumbers.append(v)
        print k + " - " + str(v)


def get_text(temp_file):
    with open(temp_file, "r") as file:
        text = ""
        base = BeautifulSoup(file, "lxml")
        title = ""
        if base.title is not None:
            try:
                title = base.title.contents[0]
            except IndexError:
                title = ""
        tags = []
        tags.append(base.find_all('a'))
        tags.append(base.find_all('p'))
        tags.append(base.find_all('b'))
        tags.append(base.find_all('i'))
        tags.append(base.find_all('h1'))
        tags.append(base.find_all('h2'))
        tags.append(base.find_all('h3'))
        tags.append(base.find_all('h4'))
        tags.append(base.find_all('h5'))
        tags.append(base.find_all('h6'))
        text += " " + title + " "

        for list in tags:
            for tag in list:
                if tag.string is not None:
                    text += " " + tag.string + " "

    file.close()
    return text

def run_parser():
    stemmer = PorterStemmer()
    with open("tokens.json", "r+") as token_list:
        search_dictionary = json.load(token_list)
        with open("WEBPAGES_RAW/bookkeeping.json", "r") as a:
            addresses = json.load(a)
            number = 0
            for k in addresses.keys():
                print("now parsing document: " + k)
                print(str(number) + " Out of " + str(37497))
                page = get_text("WEBPAGES_RAW/" + k)

                length, tokens = tokenize(page, stemmer)


                for key, value in tokens.items():
                    if key not in search_dictionary:
                        search_dictionary[key] = TokenInfo()
                    search_dictionary[key].add_doc(k, value, length, addresses[k])
                number += 1
            for key, token_info in search_dictionary.items():
                search_dictionary[key] = token_info.to_string()
        a.close()
        token_list.close()

        with open("tokens.json", "w") as final_list:
            json.dump(search_dictionary, final_list)
        final_list.close()


run_parser()
