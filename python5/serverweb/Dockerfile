FROM python:3.10-alpine
ADD server.py .
RUN pip install flask

#parti html
RUN mkdir templates
ADD ./templates/index.html ./templates/
ADD ./templates/index2.html ./templates/

#mapping tra le porte da terminale -> docker run -p 8085:8085 NomeServer (myserver)

CMD ["python","./server.py"]
