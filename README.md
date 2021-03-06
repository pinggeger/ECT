Event Coreference Resolution On Twitter

Description
===========

This corpus consists of a total of 2994 tweet IDs. All the tweets were obtained from Twitter's streaming API over a 31-day period from October 8, 2016 to November 7, 2016. As we do not have permission to distribute the tweets themselves, we have removed the terms, replacing them with "WORD", to create the dataset you will need to do the following:
* 1) Download the tweets
* 2) Tokenize the tweets using tokenizer.py
* 3) Merge the tweets with the annotations


Statistics of the corpus
===========
 
|               | Total         | 
| ------------- |:-------------:| 
| ctweet        | 2994          |
| event mention | 1111          |
| event instance| 3879          |



How to create our corpus
===========
With U.S. Presidential election receiving high degree of attention among Twitter users, we attempt to focus on the coreferential relationship between events taking place during this period. First, we set the keywords (``trump", ``hillary", ``presidential election") to filter spam and uncorrelated tweets. then, we perform twitter_nlp {https://dev.twitter.com/docs/streaming-api.} to extract all triggers and ranking by frequency after stemming, finally we obtain 1.2 thousand tweets which include one of 20 words we chose from medium frequency triggers. 

Annotators are firstly required to judge if the tweet mentions a event or not. And then for those tweets which mention an event, they need to annotate the event trigger and coreferential index. We selected the consistent 2990 tweets as the golden standard corpus (Event Coreference on Twitter, ECT). 

The following lists our annotation standard:

* We only focus on those were written in English.
* Retweets were not to be taken into account. As we mentioned before, we filter out RT tweets.
* The tweet must explicitly mention a event and the reader can infer what happened without any outside knowledge after reading the tweet.
* We only focus on those which are produced in the declarative way.
* We ignore information indicated by links. Finding information from URLs could be an interesting avenue for future work.
* We did not limit the number of event mentions in a tweet, which means a tweet can include one or more event mentions.
* Event trigger could be nouns, noun phrases, verbs and verb phrases.


20 words are: 

| pay             |       attack        |      defend       |       blame      |
|      ---        |    :-------------:  | :-------------:   |  :-------------:      
| endorse         |       reveal        |      assault      |       build      
| investigate     |       refuse        |       sing        |       impact     
| retire          |       judge         |      discover     |       scream     
| expose          |       explain       |      disappear    |       donate     



The format of our corpus
===========
Our annotator annotated the event trigger and event instance ID of all tweets. corpus.txt contains seven tab separated columns, the format of corpus.txt is:

| # |  Name   | Explanation |
|---| --- | ----
| 1 |event_mention_id        | ID of event mention
| 2 |tweet_id                | id_str of tweet from twitter streaming API
| 3 |event_instance_id       | ID of event
| 4 |event_mention_trigger   | trigger of event mention
| 5 |tweet_timestamp         | timestamp of tweet from twitter streaming API
| 6 |tweet_text              | text of tweet from twitter streaming API




