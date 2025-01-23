# Build stage
FROM python:3.9-slim as builder

WORKDIR /app
COPY requirements.txt
RUN pip install --user -r requirements.txt

FROM python:3.9-slim

WORKDIR /app

COPY --from=builder /root/.local/lib/python3.9/site-packages /root/local/lib/python3.9/site-packages
COPY . .

ENV PATH=/root/.local/bin:$PATH
ENV PORT=5000

EXPOSE 5000

CMD ["python", "app.py"]
###############################
