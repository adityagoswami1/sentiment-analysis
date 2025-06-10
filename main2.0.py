import string
from collections import Counter

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer

text = open('read.txt', encoding='utf-8').read()

# Convert to lowercase
lower_case = text.lower()

# Create a translation table to remove punctuation
translator = str.maketrans('', '', string.punctuation)

# Remove punctuation using the translation table
cleaned_text = lower_case.translate(translator)

#print(cleaned_text)

tokenized_words=word_tokenize(cleaned_text, "english")
#print(tokenized_words)

final_words=[]
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)
        
#print(final_words)

# NLP Emotion Algorithm
# 1) Check if the word in the final word list is also present in emotion.txt
#  - open the emotion file
#  - Loop through each line and clear it
#  - Extract the word and emotion using split

# 2) If word is present -> Add the emotion to emotion_list
# 3) Finally count each emotion in the emotion list

emotion_list=[]
with open('emotion.txt', 'r') as file:
    for line in file:
        clear_line=line.replace("\n", '').replace(",", '').replace("'",'').strip()
        #print(clear_line)
        word, emotion = clear_line.split(':')
        #print("Word: "+ word + " \t "+"Emotion: "+ emotion)

        if word in final_words:
            emotion_list.append(emotion)
#print(emotion_list)
w = Counter(emotion_list)
print(w)

def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    pos = score['pos']
    print(score)
    if neg>pos:
        print("Negative Sentiment")
    elif pos>neg:
        print("Positive Sentiment")
    else:
        print("Neutral vibe")

sentiment_analyse(cleaned_text)

#Plotting the emotions on the graph
fig, ax1=plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
#plt.bar(w.keys(),w.values())
plt.savefig('graph.png')
plt.show()