FROM python:3.9
WORKDIR funlinks
COPY ./requirements.txt .
COPY ./app ./app
RUN pip install -r ./requirements.txt
EXPOSE 8100
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
