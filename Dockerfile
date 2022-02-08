FROM python:3.8

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip

RUN python -m pip install Pillow

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]