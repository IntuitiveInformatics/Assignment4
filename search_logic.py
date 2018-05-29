import math

max_url_output = 10
max_docs = 200

counter = 0 # only need top ten of them shits, so this keeps track
num_tokens_entered = 2 # put variable or len(tokens inputted list)

sample_dict = {} # main dict
output_dict = {} # to hold possible output results, key = doc_id, value = URL
two_ave_tfidf = 0
three_ave_tfidf = 0

if (num_tokens_entered < 1):
    print('No input, cannot process empty input')
elif (num_tokens_entered < 2):
    for k, v in sorted(sample_dict['one'].doc_and_freq.items(), key=lambda x: -x[1]): # NOTE: switch one to first entered token
        print(str(v) + '\t' + k) 
elif (num_tokens_entered <= 2): # <= 2 key words entered
   counter = 0
   for k, v in sorted(sample_dict['two'].doc_and_freq.items(), key=lambda x: -x[1]):
        two_ave_tfidf += v
        counter += 1
        if(counter >= max_docs):
           break
   two_ave_tfidf /= float(counter) # create ave based on max_docs or less
   
   counter = 0
   for k, v in sorted(sample_dict['one'].doc_and_freq.items(), key=lambda x: -x[1]):
       # going to have to test this if statement, not sure if python works optimal enough to skip 
       # the second check if first failed in an and statement
       if(counter >= max_url_output):
           break
       if(k in sample_dict['two'].doc_and_freq.keys() and sample_dict['two'].doc_and_freq[k] >= two_ave_tfidf):
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
   counter = 0
    for k, v in sorted(sample_dict[token_list[1]].doc_and_freq.items(), key=lambda x: -x[1]): 
        two_ave_tfidf += v
        counter += 1
        if(counter >= max_docs):
            break
    two_ave_tfidf /= float(counter) # create ave based on max_docs
    counter = 0
    for k, v in sorted(sample_dict[token_list[2]].doc_and_freq.items(), key=lambda x: -x[1]): 
        three_ave_tfidf += v
        counter += 1
        if(counter >= max_docs):
            break
    three_ave_tfidf /= float(counter) # create ave based on max_docs
    counter = 0

    for i in token_list: # not n^3 ... i,j,k will be < 4 90% of the time, ie. 3^3 = 27 = O(constant), O(27N)
        if(counter >= max_url_output):
            break
        for j in token_list:
            if(i == j or counter >= max_url_output):
                break
            for k in token_list:
                if(i == k or i == j or j == k or counter >= max_url_output):
                    break
                for key,value in sorted(main_dict[i].doc_and_freq.items(), key=lambda x: -x[1]):
                    if(key in main_dict[j].doc_and_freq.keys() and key in main_dict[k].doc_and_freq.keys() and counter < max_url_output):
                        if(main_dict[j].doc_and_freq[key] >= two_ave_tfidf and main_dict[k].doc_and_freq[key] >= three_ave_tfidf):
                            output_dict[key] = main_dict[j].doc_and_URL[key]
                            counter += 1
    if(counter < max_url_output): #if this occurs then efficency will decrease by at most n
        for key,value in sorted(main_dict[token_list[0]].doc_and_freq.items(), key=lambda x: -x[1]):
            if(key not in output_dict.keys() and counter < max_url_output):
                output_dict[key] = main_dict[token_list[0]].doc_and_URL[key]
                counter += 1

for k, v in sorted(output_dict.items(), key=lambda x: -x[1]): # Display them dicked items from best to worst
    print(str(v) + '\t' + k) 
        
