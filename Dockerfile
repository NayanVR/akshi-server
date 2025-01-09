FROM --platform=linux/amd64 python:3.11

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 58219

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "58219"]
