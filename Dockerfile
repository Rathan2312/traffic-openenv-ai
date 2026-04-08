FROM ghcr.io/meta-pytorch/openenv-base:latest
COPY . /app
WORKDIR /app
RUN pip install fastapi uvicorn
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "7860"]
