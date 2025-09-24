
import time
from spine.meta.state_backup import archive_state

INTERVAL_SECONDS = 600  # Every 10 minutes

if __name__ == "__main__":
    while True:
        archive_state()
        time.sleep(INTERVAL_SECONDS)
