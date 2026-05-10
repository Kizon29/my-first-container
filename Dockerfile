FROM python:3.9-slim
WORKDIR /app
# We added psycopg2-binary so Python can talk to Postgres!
RUN pip install flask psycopg2-binary
COPY . .
CMD ["python", "app.py"]