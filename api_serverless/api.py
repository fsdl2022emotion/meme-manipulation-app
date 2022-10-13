"""AWS Lambda function serving predictions."""
import json

from PIL import ImageStat

from emotion_synthesizer.emotion_synthesis import EmotionSynthesizer
import emotion_synthesizer.util as util


DEFAULT_MODEL_PATH = "emotion_synthesizer/learned_generators/gaus_2d/1800000-G.ckpt"
DEFAULT_MODEL_TYPE = "gaussian"

model = EmotionSynthesizer(DEFAULT_MODEL_PATH, DEFAULT_MODEL_TYPE)


def handler(event, _context):
    """Provide main prediction API."""
    print("INFO loading image")
    image = _load_image(event)
    if image is None:
        return {"statusCode": 400, "message": "neither image_url nor image found in event"}
    print("INFO image loaded")
    print("INFO starting inference")
    pred_image = model.predict(image)
    print("INFO inference complete")
    image_stat = ImageStat.Stat(image)
    pred_image_stat = ImageStat.Stat(pred_image)
    print("METRIC original image_mean_intensity {}".format(image_stat.mean[0]))
    print("METRIC original image_area {}".format(image.size[0] * image.size[1]))
    print("METRIC generated image_mean_intensity {}".format(pred_image_stat.mean[0]))
    print("METRIC generated image_area {}".format(pred_image.size[0] * pred_image.size[1]))
    return {"pred": util.encode_b64_array(pred_image)}


def _load_image(event):
    event = _from_string(event)
    event = _from_string(event.get("body", event))
    image_url = event.get("image_url")
    if image_url is not None:
        print("INFO url {}".format(image_url))
        return util.read_image_pil(image_url, grayscale=True)
    else:
        image = event.get("image")
        if image is not None:
            print("INFO reading image from event")
            return util.read_b64_image(image, grayscale=True)
        else:
            return None


def _from_string(event):
    if isinstance(event, str):
        return json.loads(event)
    else:
        return 