FROM python:3
ADD appf.py /
RUN pip install flask
RUN pip install xmljson
CMD [ "python", "./appf.py" ]
