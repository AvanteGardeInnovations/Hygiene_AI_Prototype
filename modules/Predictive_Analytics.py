def forecast(detection):
    if detection["contamination"]:
        return {"risk": "high"}
    return {"risk": "low"}
