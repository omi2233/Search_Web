from googlesearch import search
from bs4 import BeautifulSoup
import requests
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import time
import nltk


# Load cache from file
with open("cache.txt", "r") as f:
    d = f.read()
    cache = eval(d) if d else {}


def perform_search(query):
    try:
        if query in cache:
            return cache[query]
        else:
            print('\nSearching web .........\n\n')
            results = list(search(query, num_results=6))
            cache[query] = (results, time.time())
            return results
    except Exception as e:
        print("An error occurred during the search:", e)
        return []

def summarize_text(text):
    try:
        print("Summarizing and preparing the content to display ...........\n\n")
        sentences = sent_tokenize(text)
        word_frequencies = FreqDist([word for word in text.lower().split() if word not in stopwords.words('english')])
        ranking = {}
        for i, sentence in enumerate(sentences):
            for word in sentence.lower().split():
                if word in word_frequencies:
                    if i in ranking:
                        ranking[i] += word_frequencies[word]
                    else:
                        ranking[i] = word_frequencies[word]

        sorted_sentences = sorted(ranking, key=ranking.get, reverse=True)
        top_sentences = sorted_sentences[:3]
        summary = ' '.join([sentences[i] for i in top_sentences])
        return summary
    except Exception as e:
        print("An error occurred during text summarization:", e)
        return ""

def scrap(li):
    text = ''
    print ('Getting content...........\n\n')
    for i in li[:3]:
        url = i
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all('p')
            for paragraph in paragraphs:
                text += paragraph.text
        except Exception as e:
            print("An error occurred while scraping the web page:", e)
    return text

def main():
    try:
        while True:
            hello = input("\n\n\n\n\nType 'exit' to exit the program.\nEnter search query: ")
            if hello.lower() == "exit":
                with open("cache.txt", "w") as f:
                    f.write(str(cache))
                exit()
            else:
                li = perform_search(hello)
                text = scrap(li)
                summary = summarize_text(text)
                print(summary)
    except Exception as e:
        print("An error occurred during execution:", e)

if __name__ == '__main__':
    main()
