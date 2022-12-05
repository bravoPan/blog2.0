FROM python:3.7-alpine
EXPOSE 8001
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python3" ]
CMD ["manage.py", "runserver", "0.0.0.0:8001"]