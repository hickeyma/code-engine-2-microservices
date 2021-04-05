import urllib.request, json, os 
from flask import Flask

if 'UPSTREAM' in os.environ:
    print("You've set UPSTREAM to:", os.environ['UPSTREAM'])
else:
    print("**** WARNING **** you're UPSTREAM isn't set and is defaulting to localhost ****")
    os.environ['UPSTREAM'] = "http://localhost:8080"

with urllib.request.urlopen(os.environ.get('UPSTREAM')) as url:
    data = json.loads(url.read().decode())
    if str(data['setting']) in ['true','True']:
        with urllib.request.urlopen("https://zenquotes.io/api/random") as quote:
            quote_data = json.loads(quote.read().decode())

    else:
        print("\n\n\n***** Sorry, the upstream service isn't set to true.*******")
        os._exit(1)

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <!DOCTYPE html>
    <body><center>
    {}
    </center></body>
    </html>
    """.format(quote_data[0]['h'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
