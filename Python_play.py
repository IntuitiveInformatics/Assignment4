import math

#Tokenize two words entered
#Find results from both
#Create two dict with top 10 results from each
#Find if any Doc IDs intersect
#List docs with intersections first + high TF-IDFs
#If < 10 intersections found list first word results

max_url_output = 10
max_docs = 200

class TokenInfo:
   
    def __init__(self):
       self.doc_and_freq = {} # {'Doc_ID', TF(t)}
       self.IDF = 0
       self.num_docs = 0

    def add_doc(self, doc_id, freq_of_word, total_words):
        if doc_id in self.doc_and_freq:
            print('Error doc id already exists')
        else:
            self.doc_and_freq[doc_id] = float(freq_of_word)/total_words
            self.update_num_docs()
            self.generate_IDF()

    def generate_IDF(self):
        self.IDF = math.log10(37497/float(self.num_docs))

    def update_num_docs(self):
        self.num_docs = len(self.doc_and_freq)

    def to_string(self):
        string_doc = "{"
        n = 0
        for doc, tf in self.doc_and_freq.items():
            if n != 0:
                string_doc += ", \"" + doc + "\": " + str(tf)
            else:
                string_doc += "\"" + doc + "\": " + str(tf)
            n += 1
        string_doc += "}"
        return {"doc_and_freq": self.doc_and_freq, "IDF": str(self.IDF), "num_docs": str(self.num_docs)}



one = TokenInfo() # First entered word
two = TokenInfo() # Second word entered
    
# Add some random shiet to them tokens, some in common some not
one.add_doc('1234',10,1000)
one.add_doc('12345',101,1000)
one.add_doc('12342',210,1000)
one.add_doc('12343',110,1000)
one.add_doc('12344',10,1000)
one.add_doc('12346',120,1000)
one.add_doc('12347',10,1000)
one.add_doc('12348',150,1000)
one.add_doc('12349',210,1000)
one.add_doc('12340',610,1000)
one.add_doc('01234',110,1000)

two.add_doc('1234',10,1000)
two.add_doc('123411',150,1000)
two.add_doc('12345',10,1000)
two.add_doc('12348',130,1000)
two.add_doc('12341',10,1000)
two.add_doc('12349',160,1000)
two.add_doc('12340',10,1000)
two.add_doc('12342',510,1000)
two.add_doc('12343',210,1000)
two.add_doc('12344',310,1000)
two.add_doc('12347',10,1000)
    
one.generate_IDF() # Generate the IDF shit
one.update_num_docs() # Count docs of the shit
two.generate_IDF() # Generate the IDF shit
two.update_num_docs() # Count docs of the shit
counter = 0 # only need top ten of them shits, so this keeps track
num_tokens_entered = 2 # put variable instead of 2, but use 2 to test

sample_dict = {} # to hold the two tokens entered by user simulating the real format of our main dict
output_dict = {} # to hold possible output results, key = doc_id, value = URL
sample_dict['one'] = one
sample_dict['two'] = two
two_ave_tfidf = 0

if (num_tokens_entered < 1):
    print('No input, cannot process empty input')
elif (num_tokens_entered < 2):
    for k, v in sorted(a_list.items(), key=lambda x: -x[1]): # NOTE: switch a_list to main dict scoped in to single token entered
        print(str(v) + '\t' + k) 
elif (num_tokens_entered <= 2): # <= 2 key words entered
   counter = 0
   for k, v in sorted(sample_dict['two'].doc_and_freq.items(), key=lambda x: -x[1]):
        two_ave_tfidf += v
        counter += 1
        if(counter >= max_docs):
           break
   two_ave_tfidf /= counter # create ave based on max_docs or less
   
   counter = 0
   for k, v in sorted(sample_dict['one'].doc_and_freq.items(), key=lambda x: -x[1]):
       # going to have to test this if statement, not sure if python works optimal enough to skip 
       # the second check if first failed in an and statement
       if(counter >= max_url_output):
           break
       if(k in sample_dict['one'].doc_and_freq.keys() and sample_dict['two'].doc_and_freq[k] >= two_ave_tfidf):
           if(k not in output_dict.keys()): # dont overwrite a previous entry
               output_dict[k] = sample_dict['one'].doc_and_URL[k] # add to output dict
               counter += 1

   if(counter < max_url_output): # if we didn't get enough output results, fill with next best results
       for k, v in sorted(sample_dict['one'].doc_and_freq.items(), key=lambda x: -x[1]):
           if(counter >= max_url_output):
               break
           if(k not in output_dict.keys()):
               output_dict[k] = sample_dict['one'].doc_and_URL[k]
               counter += 1
               
else: # > 2 entries
   # some code that does some shit

for k, v in sorted(output_dict.items(), key=lambda x: -x[1]): # Display them dicked items from best to worst
    print(str(v) + '\t' + k) 
        
