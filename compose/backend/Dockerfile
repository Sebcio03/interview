ARG PYTHON_VERSION=3.12.2-alpine

FROM python:${PYTHON_VERSION} as python
FROM python as python-build-stage

ARG BUILD_ENVIRONMENT=local

COPY ./backend/requirements .

RUN pip wheel --wheel-dir /usr/src/app/wheels  \
  -r ${BUILD_ENVIRONMENT}.txt

FROM python as python-run-stage

ARG BUILD_ENVIRONMENT=local
ARG APP_HOME=/app/

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

COPY --from=python-build-stage /usr/src/app/wheels  /wheels/

RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
	&& rm -rf /wheels/

COPY ./backend ${APP_HOME}

ENTRYPOINT [ "python","manage.py", "runserver", "0.0.0.0:8000" ]