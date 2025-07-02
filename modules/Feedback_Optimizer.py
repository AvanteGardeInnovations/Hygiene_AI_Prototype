def adjust(prediction):
    if prediction["risk"] == "high":
        return {"action": "purify", "status": "harmonized"}
    return {"action": "monitor", "status": "idle"}
