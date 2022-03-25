FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

ENV PYTHONPATH "${PYTHONPATH}:/"
ENV PORT=8000

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3

COPY ./venv/pyproject.toml  /app/
COPY ./venv/poetry.lock  /app/
ENV PATH=/root/.poetry/bin:${PATH}
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
RUN poetry show

COPY ./app /app
