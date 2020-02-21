import json

with open('sentimentTweets.json', 'r') as jf:
    data = json.load(jf)
    score_list = []
    
    count = 0
    for it in data:
        if(len(it) == 2):
            if(len(it['errors']) == 0):
                score_list.append(it['documents'][0]['score'])

    min_score = min(score_list)
    max_score = max(score_list)
    min_index = 0
    max_index = 0
    count = 0
    for score in score_list:
        if(score == min_score):
            min_index = count
        elif(score == max_score):
            max_index = count
        count += 1
    
    print(min_score)
    print(min_index)
    print(max_score)
    print(max_index)

    


    



            