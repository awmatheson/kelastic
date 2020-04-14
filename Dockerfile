FROM python:3-slim

COPY /code /code
ENTRYPOINT ["/code/entrypoint.sh"]