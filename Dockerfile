FROM python:3.12.0
WORKDIR /app
COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && pipenv install --deploy --system
COPY . .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]