FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apk update && apk add git && apk add --no-cache rust cargo
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-m", "validateemailapi.api"]
