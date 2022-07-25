FROM lnlscon/epics-r3.15.8:v1.2 

ADD main.py .

RUN pip install pcaspy

CMD ["python", "./main.py"]