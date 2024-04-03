FROM python:3.12
RUN mkdir -p /opt/termo
COPY . /opt/termo/
RUN pip install termcolor unidecode
WORKDIR /opt/termo
CMD ["python","__main__.py"]