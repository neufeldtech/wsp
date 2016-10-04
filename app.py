from StringIO import StringIO
from classify import classify

from flask import *
import re
import requests
import redis

app = Flask(__name__)
# redis_server = redis.StrictRedis(host='localhost', port=6379)

@app.route('/<path:image_url>')
def image(image_url):
    # """Handle image, use redis to cache image."""
    # cached = redis_server.get(image_url)
    # if cached:
    #     buffer_image = StringIO(cached)
    #     buffer_image.seek(0)
    # else:
    #     r = requests.get(image_url)  # you can add UA, referrer, here is an example.
    #     buffer_image = StringIO(r.content)
    #     buffer_image.seek(0)
    #     redis_server.setex(image_url, (60*60*24*7),
    #                        buffer_image.getvalue())
    
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