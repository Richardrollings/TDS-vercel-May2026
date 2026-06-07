from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
import numpy as np
import json

app = FastAPI()

# Enable CORS for POST from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.options("/api/latency")
async def options_handler():
    return Response(status_code=200)

TELEMETRY_DATA = json.loads("""
[
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 147.92,
    "uptime_pct": 98.885,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 135.88,
    "uptime_pct": 98.943,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 134.88,
    "uptime_pct": 99.226,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 141.11,
    "uptime_pct": 99.459,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 206.84,
    "uptime_pct": 97.377,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 128.57,
    "uptime_pct": 99.154,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 144.41,
    "uptime_pct": 98.124,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 168.71,
    "uptime_pct": 97.849,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 178.33,
    "uptime_pct": 97.347,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 204.94,
    "uptime_pct": 99.35,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 158.93,
    "uptime_pct": 97.199,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 226.75,
    "uptime_pct": 99.241,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 162.84,
    "uptime_pct": 97.2,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 210.59,
    "uptime_pct": 98.995,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 140.34,
    "uptime_pct": 98.528,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 182.3,
    "uptime_pct": 99.108,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 122.95,
    "uptime_pct": 99.066,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 142.19,
    "uptime_pct": 99.087,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 116.07,
    "uptime_pct": 98.036,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 124.71,
    "uptime_pct": 99.424,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 113.23,
    "uptime_pct": 98.3,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 196.9,
    "uptime_pct": 97.992,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 214.72,
    "uptime_pct": 97.322,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 165.49,
    "uptime_pct": 97.86,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 214.39,
    "uptime_pct": 99.022,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 223.91,
    "uptime_pct": 98.728,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 214.92,
    "uptime_pct": 98.447,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 155.33,
    "uptime_pct": 99.034,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 212.32,
    "uptime_pct": 99.268,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 132.5,
    "uptime_pct": 99.146,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 194.56,
    "uptime_pct": 97.558,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 188.96,
    "uptime_pct": 98.576,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 133.33,
    "uptime_pct": 98.157,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 163.27,
    "uptime_pct": 97.604,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 142.97,
    "uptime_pct": 99.269,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 150.29,
    "uptime_pct": 99.248,
    "timestamp": 20250312
  }
]
""")

@app.post("/api/latency")
async def latency_analytics(request: Request):
    body = await request.json()
    regions = body.get("regions", [])
    threshold_ms = body.get("threshold_ms", 180)

    results = []
    for region in regions:
        records   = [r for r in TELEMETRY_DATA if r["region"] == region]
        latencies = [r["latency_ms"] for r in records]
        uptimes   = [r["uptime_pct"]  for r in records]
        results.append({
            "region":      region,
            "avg_latency": round(float(np.mean(latencies)), 2),
            "p95_latency": round(float(np.percentile(latencies, 95)), 2),
            "avg_uptime":  round(float(np.mean(uptimes)), 3),
            "breaches":    int(sum(1 for l in latencies if l > threshold_ms))
        })

    return {"regions": results}
