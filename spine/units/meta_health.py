from pulse.units.base import PulseUnit
from datetime import datetime

class MetaPulseHealth(PulseUnit):
    def emit(self) -> dict:
        return {
            "type": "pulse_health_check",
            "timestamp": datetime.utcnow().isoformat(),
            "payload": {
                "status": "alive",
                "unit_count": len(self.config.get("active_units", []))
            }
        }
