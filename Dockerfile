# ==================================== BASE ====================================
ARG INSTALL_PYTHON_VERSION=${INSTALL_PYTHON_VERSION:-"INSTALL_PYTHON_VERSION NOT SET"}
FROM python:${INSTALL_PYTHON_VERSION}-slim-buster AS base


WORKDIR /app
COPY ["requirements.txt", "requirements-test.txt", "/app/"]

RUN useradd -m duke
RUN chown -R duke:duke /app
USER duke
ENV PATH="/home/duke/.local/bin:${PATH}"

ENTRYPOINT [ "/bin/bash" ]

# ================================= DEVELOPMENT ================================
FROM base AS development

RUN pip install --user -r requirements-test.txt

EXPOSE 8000
