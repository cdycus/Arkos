class PulseQuorum:
    def __init__(self, peers):
        self.peers = peers

    def is_quorum_met(self, threshold=0.67):
        active = len([p for p in self.peers.values() if p.get("last_seen")])
        return active >= max(3, int(len(self.peers) * threshold))
