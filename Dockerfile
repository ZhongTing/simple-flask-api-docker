FROM kennethreitz/pipenv:rewrite-inline-venv-activation
COPY . /app
EXPOSE 5000
ENV PYTHONPATH "${PYTHONPATH}:/app"
WORKDIR my_app
CMD python3 app.py