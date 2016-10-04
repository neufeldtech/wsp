FROM jordanneufeld/caffe:cpu
ENV FLASK_APP=app.py
EXPOSE 5000
WORKDIR /opt/nanny-proxy
CMD pip install -r requirements.txt && flask run --host 0.0.0.0 --reload