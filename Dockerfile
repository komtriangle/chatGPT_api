FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt


# 
RUN pip install -r /code/requirements.txt

# 
COPY . /code

# 
CMD ["uvicorn", "chatGPT:app", "--host", "0.0.0.0", "--port", "8000"]