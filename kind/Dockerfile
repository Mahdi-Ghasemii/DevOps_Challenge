FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt script.py ./
COPY templates /app/templates

COPY resolv.conf /etc/resolv.conf

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 4000

CMD [ "python3" , "script.py" ]

