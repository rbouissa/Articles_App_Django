FROM python:3.11

WORKDIR /app

RUN pip install django && python -m pip install Pillow

COPY . .

EXPOSE 5000

CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]