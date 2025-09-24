
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


@app.get("/behavior", response_class=HTMLResponse)
def behavior_bias_view():
    try:
        from memory.reflection_hook import reflect_on_behavior
        reflection = reflect_on_behavior()
        html = f"""<html><body>
        <h3>Behavioral Reflection State</h3>
        <pre>{json.dumps(reflection, indent=2)}</pre>
        </body></html>"""
    except Exception as e:
        html = f"""<html><body><h3>Error</h3><pre>{e}</pre></body></html>"""
    return html
