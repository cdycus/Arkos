from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def compute_similarity_matrix(belief_statements):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(belief_statements)
    return (X * X.T).toarray()

def cluster_beliefs(belief_statements, k=3):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(belief_statements)
    km = KMeans(n_clusters=k)
    labels = km.fit_predict(X)
    return list(labels)

def link_beliefs_to_actions(beliefs, actions):
    links = []
    for b in beliefs:
        for a in actions:
            if b["belief_id"] in a.get("belief_ids", []):
                links.append((b["belief_id"], a["pulse_id"]))
    return links
