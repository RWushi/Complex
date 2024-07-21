FROM python:3.11

WORKDIR /complex

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app.py

CMD ["python", "app.py"]
