import gradio as gr
import numpy as np

from emotion_synthesizer.emotion_synthesis import EmotionSynthesizer
from drawer.simple_draw import add_text

DEFAULT_MODEL_PATH = "./emotion_synthesizer/learned_generators/gaus_2d/1800000-G.ckpt"
DEFAULT_MODEL_TYPE = "gaussian"

def make_meme(original_image, new_emotion, text=None):
    model = EmotionSynthesizer(DEFAULT_MODEL_PATH, DEFAULT_MODEL_TYPE)
    try:
        generated_image = model.predict(original_image, new_emotion)
    except:
        raise gr.Error(f"Cannot generate emotion {new_emotion} from the input image.")
    
    if text:
        print(f"Adding text: {text}")
        output_image = add_text(generated_image, text)
        return output_image

    return generated_image


def face_to_face(x):
    return x


if __name__ == "__main__":
    # TODO
    title = "MEME Manipulation Tool"
    description = "MEME Manipulation Tool is an app..."
    article = "example article"
    examples=[["example1"]]

    with gr.Blocks(title=title) as demo:
        with gr.Accordion("README"):
            gr.Markdown("MEME Manipulation Tool")

        with gr.Tab("Change emotion"):
            emtion_image_input = gr.Image()
            emotion_text_input = gr.Radio(["happy", "fear", "sad", "angry", "disgust", "surprise", "neutral"], label="Emotion")
            meme_text_input = gr.Textbox(lines=1, label="Meme text")            
            change_emotion_button = gr.Button("Change emotion")
            emotion_image_output = gr.Image()
            
        with gr.Tab("<other face2face app>"):
            #TODO
            with gr.Row():
                image_input = gr.Image()
                image_output = gr.Image()
            image_button = gr.Button("Convert")


        change_emotion_button.click(make_meme, inputs=[emtion_image_input, emotion_text_input, meme_text_input], outputs=emotion_image_output, )
        image_button.click(face_to_face, inputs=image_input, outputs=image_output)

    demo.launch()