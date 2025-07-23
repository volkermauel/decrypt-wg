FROM python:3-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir pycryptodome
ENTRYPOINT ["python", "decrypt-wg.py"]
CMD []
