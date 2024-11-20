FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /backend
RUN pip install poetry

COPY pyproject.toml poetry.lock /backend/
RUN poetry config virtualenvs.create false && poetry install

COPY ./alembic.ini /backend/alembic.ini
COPY ./alembic /backend/alembic
COPY ./api /backend/api/
COPY ./static /backend/static
COPY ./uploads /backend/uploads
COPY .env /backend