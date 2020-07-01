import requests

def get_page(url):
    response = requests.get(url)
    print(response.text)

def save_as_html(url, name):
    response = requests.get(url)
    text = response.text
    with open(name, 'w') as f:
        f.write(text)