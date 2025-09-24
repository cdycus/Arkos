def receive_video_input(source="camera"):
    return {
        "type": "video_input",
        "source": source,
        "timestamp": __import__('datetime').datetime.utcnow().isoformat() + "Z",
        "note": "Video input received (stub, no processing)"
    }
