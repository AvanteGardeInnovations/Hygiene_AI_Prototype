main.py
from modules import Detection_Engine, Feedback_Optimizer, Predictive_Analytics, Coaching_System

def system_cycle(sensor_input):
    detection = Detection_Engine.analyze(sensor_input)
    prediction = Predictive_Analytics.forecast(detection)
    feedback = Feedback_Optimizer.adjust(prediction)
    Coaching_System.coach_user(feedback)

    if feedback["status"] == "harmonized":
        print("✨ Soliri Protocol Activated ✨")

if __name__ == "__main__":
    for cycle in range(3):
        mock_input = {"VOC": 0.85, "traffic": 0.3}
        system_cycle(mock_input)
