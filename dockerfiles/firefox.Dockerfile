FROM selenium/node-firefox:3.141.59-20200525

USER root

RUN apt-get update
RUN apt-get install python3-pip -y
RUN pip3 install selenium
