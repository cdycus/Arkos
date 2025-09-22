
import requests

class PulseMeshRouter:
    def __init__(self, peers):
        self.peers = peers

    def broadcast(self, pulse):
        for peer in self.peers:
            try:
                response = requests.post(f"http://{peer}/mesh", json=pulse, timeout=1)
                print(f"Broadcasted to {peer}: {response.status_code}")
            except Exception as e:
                print(f"Mesh broadcast to {peer} failed: {e}")
