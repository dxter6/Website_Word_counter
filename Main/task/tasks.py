import requests
import time
def count_words(url):
    
    time.sleep(1)
    response = requests.get(url)
    return len(response.text.split())
