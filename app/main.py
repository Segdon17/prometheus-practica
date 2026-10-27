from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Endpoint principal con tu nombre y grupo (personalízalo)
@app.get("/")
def read_root():
    return {"message": "Hi, iam Jose Gordillo , group IKBO-66-23"}

# Endpoint de salud (opcional)
@app.get("/health")
def health():
    return {"status": "ok"}

# Instrumentación de Prometheus: expone las métricas en /metrics
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)