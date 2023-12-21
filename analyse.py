import os
import re
from collections import Counter
from unidecode import unidecode
from wordcloud import WordCloud
import matplotlib.pyplot as plt

folder_path = "./lyrics"
all_words = []
min_chars = 4


def remove_accents(word):
    return unidecode(word)


for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as file:
            text = file.read()

            words = re.findall(r'\b\w+\b', text)

            words = [remove_accents(word.lower())
                     for word in words if len(word) >= min_chars]

            all_words.extend(words)

word_counter = Counter(all_words)

top_words = word_counter.most_common(250)

wordcloud_data = {word: count for word, count in top_words}

wordcloud = WordCloud(width=1200, height=600, background_color='white', max_words=250,
                      min_font_size=3, font_path="./ARIAL.TTF").generate_from_frequencies(wordcloud_data)

plt.figure(figsize=(20, 10))
plt.imshow(wordcloud)
plt.axis("off")
plt.title(
    f'Most frequent words >= {min_chars} characters', va='bottom')
plt.show()
