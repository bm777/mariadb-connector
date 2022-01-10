FROM python:3.8

WORKDIR /usr/src/app

RUN pip3 install Cython
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN bash ./install_mariadb.sh

COPY . .

CMD ["python", "./app.py"]
