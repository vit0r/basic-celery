from celery import Celery

app = Celery(__name__)
app.config_from_object('celeryconfig')

@app.task
def reverse_string(text):
  return text[::-1]
