import string
from collections import Counter
import matplotlib.pyplot as plt
from textblob import TextBlob

example_text = open("example.txt", encoding="utf-8").read()

lower_case_string = example_text.lower()

cleaned_text = lower_case_string.translate(str.maketrans('', '', string.punctuation))

tokenized_words = cleaned_text.split()

stop_words_list = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

analysable_words_list = []
for word in tokenized_words:
    if word not in stop_words_list:
        analysable_words_list.append(word)

emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word,emotion = clear_line.split(':',1)
    
        if word in analysable_words_list:
            emotion_list.append(emotion)

print("Emotion List:", emotion_list)
emotion_count = Counter(emotion_list)
print("Emotion Count:", emotion_count)

# Sentiment Analysis
sentiment_results = TextBlob(example_text)
sentiment_polarity = -sentiment_results.sentiment.polarity

print("Sentiment Polarity:", sentiment_polarity)

if(sentiment_polarity>0):
    print('Sentiment Result= Positive')
elif(sentiment_polarity<0):
    print('Sentiment Result= Negative')
else:
    print('Sentiment Result= Neutral')

fig, ax1 = plt.subplots()
ax1.bar(emotion_count.keys(), emotion_count.values())
fig.autofmt_xdate()
plt.savefig('essay_graph.png')
plt.show()


