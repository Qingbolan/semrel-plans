FROM python:3.12-slim
WORKDIR /app
COPY src/server.py src/hosting.py src/eal_reader.py src/eal_strings.py src/plan_store.py ./src/
COPY scripts/serve.py ./scripts/
# Catalog plans ship as build-time snapshots; no EasyNet compiler is needed (EAL import stays disabled).
RUN useradd --uid 10001 --no-create-home atlas
USER 10001:10001
ENV ATLAS_HOST=0.0.0.0 ATLAS_ROOT=/site PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
EXPOSE 8765
HEALTHCHECK --interval=30s --timeout=20s --start-period=30s --retries=3 CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8765/api/health', timeout=18)"
CMD ["python", "scripts/serve.py"]
