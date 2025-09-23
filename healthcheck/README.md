+ ## 🛡️ Health-Check Mesh
+ This release introduces a real-time health-check mesh:
+ - **Service Registry:** Lists all known service health endpoints.
+ - **Checker Module:** Periodically polls services and auto-quarantines failing or offline nodes.
+ - **Quarantine File:** `quarantine.json` records all services that are unhealthy or unreachable.

# 🛠️ Release Notes: Health-Check Mesh Integration

## Features
- Added health-check mesh with live service pings and quarantine logic.
- New files:
  - `Arkos/healthcheck/service_registry.json`
  - `Arkos/healthcheck/checker.py`

## Improvements
- Resilience: Failing services are now isolated automatically.
- Observability: JSON quarantine list allows for external monitoring.
