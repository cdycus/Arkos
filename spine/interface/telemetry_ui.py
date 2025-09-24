
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


@app.get("/cognition", response_class=HTMLResponse)
def cognition_dashboard():
    try:
        with open("spine/meta/meta_skippy_state.json", "r") as f:
            state = json.load(f)
        html = f"""<html><body>
        <h3>🧠 Skippy Cognitive State</h3>
        <pre>{json.dumps(state, indent=2)}</pre>
        </body></html>"""
    except Exception as e:
        html = f"""<html><body><h3>Error loading cognition</h3><pre>{e}</pre></body></html>"""
    return html

@app.get("/api/cognition")
def cognition_api():
    try:
        with open("spine/meta/meta_skippy_state.json", "r") as f:
            return json.load(f)
    except:
        return {"error": "Unable to load state"}
