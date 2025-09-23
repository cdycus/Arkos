import os
import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class MemoryAbstractionEngine:
    def __init__(self, memory_path="memory/memory_log.json", output_path="memory/abstractions.json"):
        self.memory_path = memory_path
        self.output_path = output_path
        self.embeddings = []
        self.memories = []

    def load_memories(self):
        with open(self.memory_path) as f:
            self.memories = [json.loads(line) for line in f.readlines()]
        self.embeddings = [m["embedding"] for m in self.memories if "embedding" in m]

    def cluster_memories(self, threshold=0.8):
        similarities = cosine_similarity(self.embeddings)
        clustered = []
        used = set()
        for i in range(len(self.embeddings)):
            if i in used:
                continue
            cluster = [i]
            used.add(i)
            for j in range(i + 1, len(self.embeddings)):
                if similarities[i][j] > threshold and j not in used:
                    cluster.append(j)
                    used.add(j)
            clustered.append(cluster)
        return clustered

    def summarize_cluster(self, cluster_indices):
        summary = {
            "pattern": "emerging pattern",
            "source_memories": [self.memories[i]["id"] for i in cluster_indices],
            "confidence": round(len(cluster_indices) / len(self.memories), 2)
        }
        return summary

    def save_abstractions(self, abstractions):
        with open(self.output_path, "w") as f:
            json.dump(abstractions, f, indent=2)

    def run(self):
        self.load_memories()
        clusters = self.cluster_memories()
        abstractions = [self.summarize_cluster(c) for c in clusters if len(c) > 1]
        self.save_abstractions(abstractions)
