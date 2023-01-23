

FROM python:3.8
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5001
CMD ["python","app.py"]
# docker build -t test_docker .
# docker run -p 5001:5001 test_docker

