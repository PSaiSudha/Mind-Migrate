def get_wellness_tip(mood: str) -> dict:
    tips = {
        "Stressed": {
            "advice": "High stress levels detected in your behavior patterns.",
            "exercise": "Box Breathing: Inhale for 4s, hold 4s, exhale 4s, hold 4s.",
            "action": "Take a 5-minute break away from your screen."
        },
        "Fatigued": {
            "advice": "Slow typing cadence and long pauses suggest mental fatigue.",
            "exercise": "Eye Palming & Stretching: Rest your eyes and stretch your shoulders.",
            "action": "Hydrate and step outside for some fresh air."
        },
        "Focused": {
            "advice": "You are in a stable, highly focused state!",
            "exercise": "Keep up the great workflow, but remember to blink and adjust posture.",
            "action": "Continue your task or schedule a short break soon."
        },
        "Calm": {
            "advice": "Your behavioral metrics show a relaxed, balanced pattern.",
            "exercise": "Deep diaphragmatic breathing to maintain centeredness.",
            "action": "Maintain your steady pace."
        }
    }
    return tips.get(mood, {
        "advice": "Stay mindful and balanced.",
        "exercise": "Take three deep breaths.",
        "action": "Listen to some light music."
    })