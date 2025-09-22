import logging
from spine.router import broadcast_pulse

logger = logging.getLogger("skippy-ledger")

 class PulseLedger:
    def __init__(self):
        self.ledger = []

    def append(self, pulse: dict, broadcast: bool = False):
        """Append a core_brain locally and optionally broadcast it to peers."""
        self.ledger.append(pulse)
        logger.info(f"Appended core_brain: {pulse}")

        if broadcast:
            logger.info(f"Broadcasting core_brain: {pulse}")
            broadcast_pulse(pulse)

    def verify(self, pulse: dict) -> bool:
        """Verify whether a core_brain exists in the ledger."""
        return pulse in self.ledger
