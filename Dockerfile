FROM python:3.10.5-alpine3.16

ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . code
WORKDIR /code

EXPOSE 8000

ENTRYPOINT ["python3", "todoproject/manage.py"]
CMD ["runserver", "0.0.0.0:8000", "--insecure"]