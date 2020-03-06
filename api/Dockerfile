FROM python:3
ENV PYTHONUNBUFFERED 1
EXPOSE 8000
RUN mkdir /api
WORKDIR /api
COPY requirements.txt /api
RUN pip install -r requirements.txt