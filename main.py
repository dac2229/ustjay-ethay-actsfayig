import os
import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup


app = Flask(__name__)



def get_fact():
    """ method to get random fact frmo unkno.com"""

    response = requests.get("http://unkno.com")
    soup = BeautifulSoup(response.content, "html.parser")

    facts = soup.find_all("div", id="content")
    return facts[0].getText()

def pig_latinze(fact):

    url_link = "https://hidden-journey-62459.herokuapp.com/piglatinize/"
    data = {"input_text": fact}
    converted_fact = requests.post(url_link, data=data)
    return converted_fact




@app.route('/')
def home():
    fact = get_fact()
    fact_piglatin = pig_latinze(fact)
    return f'<a href="{fact_piglatin.url}">{fact_piglatin.url}</a>'


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 6787))
    host = os.environ.get("HOST", "127.0.0.1")
    app.run(host=host, port=port)
