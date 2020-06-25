FROM selenium/node-chrome:3.141.59-20200525


RUN sudo apt-get update
RUN sudo apt-get install python3-pip -y
RUN pip3 install selenium
