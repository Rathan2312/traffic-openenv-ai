FROM python:3.10

WORKDIR /app
COPY . .

RUN pip install numpy

CMD ["python", "inference.py"]
