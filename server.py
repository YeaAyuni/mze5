from flask import Flask, request
from zee5 import zee5_scrapper

app = Flask(__name__)
@app.route('/ping')
def hello():
    print('Hello World!')
    return str(request.user_agent)


@app.route("/")
def Zee5_Media_URL():
    params = request.args.to_dict() 

    target_url = params.get("zee5_url")
    timeout = params.get("timeout")

    zee5_media_urls = zee5_scrapper(url=target_url, timeout=timeout)
    
    resp = {
        "data": zee5_media_urls,
    }
    
    return resp

if __name__ == "__main__":
    port = 5050
    app.run(port=port)


    