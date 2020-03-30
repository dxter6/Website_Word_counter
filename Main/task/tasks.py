import requests
import time
def count_words(url):
    
    time.sleep(1)
    response = requests.get(url)
    return len(response.text.split())
def test(url):
     try:
        r = requests.get(url)
        return r.status_code
     except requests.exceptions.ConnectionError:
         return "connection error"
     return r.status_code

print(test('https://httpbin.org/status/404'))