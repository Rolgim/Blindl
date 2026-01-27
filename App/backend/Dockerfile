FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv pip install --system --no-cache -r pyproject.toml --all-extras

RUN pip list

COPY . .

CMD ["python", "-m", "uvicorn", "src.main:app", "--host", "0.0.0.0"]