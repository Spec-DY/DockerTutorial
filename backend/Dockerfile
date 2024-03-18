FROM python:3.8-slim

# dependencies
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy code to container
COPY . .

# enable flask
CMD ["python", "app.py"]
