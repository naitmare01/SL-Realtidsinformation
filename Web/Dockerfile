FROM ubuntu:latest
LABEL David Berndtsson
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /main
WORKDIR /main
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]
EXPOSE 80