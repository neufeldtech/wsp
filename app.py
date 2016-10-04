from StringIO import StringIO
from classify import classify

from flask import *
import re
import requests

app = Flask(__name__)
@app.route('/')
def index():
    return send_file('index.html')

@app.route('/<path:image_url>')
def image(image_url):
    try:
        r = requests.get(image_url)
        r.raise_for_status()
        if re.match('image', r.headers['Content-Type'] ) is None:
            raise Exception('Client Error. URL is not a valid image')
    except requests.exceptions.HTTPError as e:
        return jsonify({'status': r.status_code, 'message': "There was an error with the request"})
    except Exception as e:
        print e
        return jsonify({'status': 500, 'message': "Something bad happened. Are you supplying a valid Image URL?"})

    buffer_image = StringIO(r.content)
    score = classify(r.content)
    threshold = 0.1
    print "------------"
    print image_url
    print "threshold %s" % threshold
    print "score %s" % float(score)
    print "------------"
    if float(score) > threshold:
        return send_file('nope.jpg')
    else:
        return send_file(buffer_image, mimetype='image/jpeg')