FROM debian:stretch

RUN apt-get update && \
        apt-get install -y \
            wget \
            xzdec \
            cm-super \
            texlive \
            texlive-xetex \
            texlive-fonts-extra \
            texinfo \
            && \
        apt-get clean && \
        rm -rf /var/lib/apt/*

RUN mkdir /root/tetxf
RUN tlmgr init-usertree
RUN tlmgr install ucharcat

VOLUME ["/mnt/system"]

WORKDIR /mnt/system

CMD ["/usr/bin/xelatex"]
