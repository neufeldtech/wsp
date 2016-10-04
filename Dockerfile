FROM jordanneufeld/caffe:cpu
ENV FLASK_APP=app.py
EXPOSE 5000
ADD . /opt/wsp
WORKDIR /opt/wsp
CMD pip install -r requirements.txt && gunicorn -w 4 --name wsp_gunicorn --bind 0.0.0.0:5000 app:app