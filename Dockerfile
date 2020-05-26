FROM python:3.7-alpine
RUN apk add --no-cache autoconf automake g++ make python3-dev
ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
ADD app.py /app.py
RUN chmod +x /app.py
CMD ["/app.py"]
