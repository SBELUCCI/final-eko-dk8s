FROM python:3.12-slim


RUN addgroup --system appgroup && adduser --system appuser --ingroup appgroup


WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY app.py .
COPY templates ./templates


USER appuser


EXPOSE 5000
CMD ["python", "app.py"]