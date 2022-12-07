# FROM joeblackwaslike/texlive:2016
# WORKDIR /
# RUN tar cfzv lib-tar.tar /lib
# RUN tar cfzv usr-lib-tar.tar /usr/lib
# RUN tar cfzv texmf.tar /etc/texmf
# RUN tar cfzv usr-bin.tar /usr
FROM python:3.9-slim

# COPY --from=0 /usr/bin/xelatex /usr/bin
# COPY --from=0 /lib-tar.tar ./lib-tar.tar
# COPY --from=0 /usr-lib-tar.tar ./usr-lib-tar.tar
# RUN tar -xvf lib-tar.tar -C / --skip-old-files
# RUN tar -xvf usr-lib-tar.tar -C / --skip-old-files

WORKDIR /app
COPY requirements.txt ./

RUN apt-get update

RUN pip install -U pip
RUN pip install -r requirements.txt

RUN python3 -m spacy download en_core_web_sm 


RUN apt-get install -y texlive-fonts-extra \
        texlive-xetex 

WORKDIR /app
COPY . /app


EXPOSE 8080
CMD ["python3", "-u", "main.py"]
