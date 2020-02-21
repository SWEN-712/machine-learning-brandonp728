# Attached is all my code for project 2.

## Preface
I had many, many issues trying to get this code to run, mainly due to the tweets I was extracting containing new lines. First, because of the new lines, azure returned some JSON lines with errors because of empty bodies, or tweets would get chopped up because of newlines from one tweet into several. This created problems for the return statement from Azure and made JSON parsing a nightmare. Eventually I had to write the parse_json.py to parse the files as they specifically appeared. This worked, but then pairing them became hard because I had to then determine what were scores for actual tweets and what were scores for empty messages or newlines, or messages cut short by newlines. All in all this was an extremely frustraing experience as databricks was finnicky to work with and I was unable to follow the provided tutorial after a certain point because of the major differences between the tutorial and teh project. 

## Running the code
First run extract_tweets.py to get the tweets

Then run restHandler.scala to send them to Azure

Paste the output of restHandler into a json file named "sentimentTweets.json"

Finally run parse_json.py to fix up the json file and generate score_list.txt  

## Results
I accessed tweets from the @google_access accessibility Twitter account. Scores that were correctly entered ranged between 0.99 and 0.78 sentiment scores. There were occasionally some outliers that scored a 0.5 or 0.12, but when I read the corresponding tweets, they did not seem worthy of that score, which was confusing and hard to reconcile. The account overall was positive and helpful in many of its tweets. I believe this is because a public facing accessibility-related account must be patient and kind as all of the tweets were usually in response to people's accessibility compaints and suggestions. This account must engage in discourse with users regularly, so I imagine it had to stay positive in order to allow for peaceful discussion of what could be done to improve google's accessibility or answer people's concerned tweets. Some scores came in extremely low and I believe that is because they fell victim to issue of newlines splitting up tweets as mentioned above, so sentiment most likely lost in translaation. 
