FROM python:3.10.4

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . code
WORKDIR /code

EXPOSE 8000

CMD python3 "todoproject/manage.py" "makemigrations"
CMD python3 "todoproject/manage.py" "migrate"

ENTRYPOINT ["python3", "todoproject/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]