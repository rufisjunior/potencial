FROM python:3.12.2
EXPOSE 5000
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

CMD [ "python3", "web.py" ]