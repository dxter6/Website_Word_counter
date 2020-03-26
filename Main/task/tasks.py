import requests

def count_words(url):
    response = requests.get(url)
    return len(response.text.split())
