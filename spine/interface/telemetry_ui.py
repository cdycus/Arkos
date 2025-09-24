
from fastapi import FastAPI
import requests
from fastapi.responses import HTMLResponse

app = FastAPI()

SERVICES = {
    'mind': 'http://localhost:8001/pulse',
    'brain': 'http://localhost:8002/pulse',
    'heart': 'http://localhost:8003/pulse'
}

@app.get("/", response_class=HTMLResponse)
def telemetry_dashboard():
    html = """<html><head><title>Skippy Telemetry</title></head><body>
    <h2>Skippy Telemetry Dashboard</h2><ul>"""
    for name, url in SERVICES.items():
        try:
            r = requests.get(url, timeout=2)
            pulse = r.json().get('pulse', 'No pulse')
            html += f"<li><b>{name}</b>: ✅ {pulse}</li>"
        except Exception:
            html += f"<li><b>{name}</b>: ❌ Offline</li>"
    html += """</ul></body></html>"""
    return html
