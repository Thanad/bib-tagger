FROM python:2

WORKDIR /usr/src/app

RUN pip install --no-cache-dir scipy 
RUN pip install --no-cache-dir numpy 
RUN pip install --no-cache-dir pytesseract 
RUN pip install --no-cache-dir pillow

COPY . .

CMD [ "python", "./main.py" ]