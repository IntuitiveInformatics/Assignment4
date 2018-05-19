from collections import defaultdict
import re, sys, time, json
from bs4 import BeautifulSoup
from tester import TokenInfo

def tokenize(text):
    words = (re.sub('[\W_]', ' ', text).lower())
    token_list = words.split()
    wordlist = defaultdict(int)
    for token in token_list:
        wordlist[token] += 1
    #order(wordlist)
    return len(token_list),wordlist

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
            except IndexError :
                title = ""
        a_tags = base.find_all('a')
        p_tags = base.find_all('p')

        text += " " + title + " "
        for tag in a_tags:
            if tag.string is not None:
                text += " " + tag.string + " "
        for tag in p_tags:
            if tag.string is not None:
                text += " " + tag.string + " "
    file.close()
    return text

def time_mod():
    startTime = time.time()
    with open("tokens.json", "r+") as token_list:
        search_dictionary = json.load(token_list)
        with open("WEBPAGES_RAW/bookkeeping.json", "r") as a:
            addresses = json.load(a)
            number = 0
            for k in addresses.keys():
                print("now parsing document: " + k)
                print(str(number) + " Out of " + str(37497))
                page = get_text("WEBPAGES_RAW/" + k)
                length, tokens = tokenize(page)
                for key, value in tokens.items():
                    if key not in search_dictionary:
                        search_dictionary[key] = TokenInfo()
                    search_dictionary[key].add_doc(k, value, length)
                number += 1
            for key, token_info in search_dictionary.items():
                search_dictionary[key] = token_info.to_string()
        a.close()
        token_list.close()

        with open("tokens.json", "w") as final_list:
            json.dump(search_dictionary, final_list)
        final_list.close()

time_mod()
"""      
filename = "mary.txt"
myFile = open(filename, 'r')
text = myFile.read()
analyzer = MainClass(text)
analyzer.analyze()
analyzer.analyzeFile("hack.txt")
analyzer.analyzeFile("sample1.txt")
myFile.close()
"""
