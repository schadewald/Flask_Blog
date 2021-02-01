FROM python:3.9
LABEL maintainer = "Chad Schadewald"
WORKDIR /app
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY ./ ./

EXPOSE 8050

CMD ["python", "./app.py"]
