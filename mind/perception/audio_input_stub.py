def receive_audio_input(source="mic"):
    return {
        "type": "audio_input",
        "source": source,
        "timestamp": __import__('datetime').datetime.utcnow().isoformat() + "Z",
        "note": "Audio input received (stub, no processing)"
    }
