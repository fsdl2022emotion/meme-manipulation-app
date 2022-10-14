from emotion_synthesizer.models.ganmut import GANmut
# from models.ganmut import GANmut
from emotion_synthesizer.mapping import DEFAULT_NEIGHBORS, DEFAULT_EMOTION_COORDINATES



class EmotionSynthesizer:
    def __init__(self, model_path, model_type, neighbors=DEFAULT_NEIGHBORS):
        self.model_path = model_path
        self.G = GANmut(G_path=model_path, model=model_type)
        self.neighbors = neighbors

    def predict(self, original_image, primary_emotion, secondary_emotion=None, intensity=None):
        coordinates = self._get_coordinate(primary_emotion, secondary_emotion, intensity)
        print(f"Coordinates: {coordinates}")
        generated_image = self.G.emotion_edit(
            imgobj=original_image, 
            x=coordinates[0], 
            y=coordinates[1], 
            save = False)
        return generated_image

    def _get_coordinate(self, primary_emotion, secondary_emotion=None, intensity=None):
        if primary_emotion not in DEFAULT_EMOTION_COORDINATES:
            raise ValueError("Primary emotion must be one of {}".format(DEFAULT_EMOTION_COORDINATES.keys()))
        primary_coordinate = DEFAULT_EMOTION_COORDINATES[primary_emotion]
        if secondary_emotion is None:
            return primary_coordinate
        if secondary_emotion not in self.neighbors:
            raise ValueError("Secondary emotion must be one of {}".format(self.neighbors.keys()))
        secondary_coordinate = self.neighbors[primary_emotion][secondary_emotion]
        print(secondary_coordinate)
        x_dist = abs((primary_coordinate[0] - secondary_coordinate[0]) * intensity)
        y_dist = abs((primary_coordinate[1] - secondary_coordinate[1]) * intensity)
        x_dist = round(x_dist, 2)
        y_dist = round(y_dist, 2)
        if(primary_coordinate[0] > secondary_coordinate[0]):
            x_dist *= -1
        if(primary_coordinate[1] > secondary_coordinate[1]):
            y_dist *= -1
        new_coordinate = (primary_coordinate[0] + x_dist, primary_coordinate[1] + y_dist)
        return new_coordinate