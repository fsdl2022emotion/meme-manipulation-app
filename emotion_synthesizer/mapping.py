DEFAULT_EMOTION_COORDINATES = {
    "happy": (0.6, 0.4),
    "sad": (1, -0.7),
    "angry": (0.6, -0.9),
    "fear": (-0.25,-0.9),
    "surprise": (0.9,-0.45),
    "neutral": (0.4, -0.5),
    "disgust": (-0.8,-1)
}

DEFAULT_NEIGHBORS = {
    "happy": {"neutral": (0.4, -0.5), "surprise" : (0.8, -0.4)},
    "sad": {"neutral": (-0.7, -0.3), "disgust" : (-0.8, -1), "fear": (-0.4, -1)},
    "angry": {"surprise": (1, -0.4), "neutral" : (0.4, -0.4), "fear": (-0.3, -0.9), "sad" : (-0.4, -0.6)},
    "fear": {"sad": (-0.4, -0.6), "disgust" : (-0.8, -1), "angry": (0.5,-0.9)},
    "surprise": {"happy": (0.8, -0.1), "neutral" : (0.6, -0.5), "angry": (0.9, -0.8)},
    "disgust": {"sad": (-0.8, -0.75), "fear" : (-0.1, -1)}
}
