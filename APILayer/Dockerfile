FROM python:3.12-slim


RUN addgroup --system appgroup && adduser --system appuser --ingroup appgroup


WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY app.py .


USER appuser


EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]