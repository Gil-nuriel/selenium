FROM selenium/node-firefox

USER root

RUN apt-get update
RUN apt-get install python3-pip
RUN pip3 install selenium