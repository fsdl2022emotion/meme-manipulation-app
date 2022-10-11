from functools import partial
import argparse

import gradio as gr
import numpy as np

from emotion_synthesizer.emotion_synthesis import EmotionSynthesizer
from drawer.simple_draw import add_text

DEFAULT_MODEL_PATH = "./emotion_synthesizer/learned_generators/gaus_2d/1800000-G.ckpt"
DEFAULT_MODEL_TYPE = "gaussian"

def make_meme(original_image, new_emotion, text=None, wandb_artifact=None):
    if wandb_artifact:
        artifact_dir = artifact.download()
        artifact_path = f"{artifact_dir}/1800000-G.ckpt"
        model_type = artifact.metadata["model_type"]
        model = EmotionSynthesizer(model_path=artifact_path, model_type=model_type)
    else:
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

    parser = argparse.ArgumentParser()
    parser.add_argument("--use_wandb", action="store_true", help="Use wandb artifact", default=False)
    args = parser.parse_args()
    use_wandb = args.use_wandb

    if use_wandb:
        print(f"Using wandb artifact")
        import wandb
        run = wandb.init(
            project="fsdl2022-emotion", 
            job_type='use-model',
            entity="fsdl22",
            )
        artifact = run.use_artifact("ganmut-model:production")
        meme_app = partial(make_meme, wandb_artifact=artifact)
    else:
        print(f"Using default model: {DEFAULT_MODEL_PATH}")
        meme_app = make_meme

    # TODO
    title = "MEME Manipulation Tool"
    description = "MEME Manipulation Tool is an app..."
    article = "example article"
    examples=[["example1"]]

    with gr.Blocks(
        title=title, 
        css ="""
            .gradio-container {background-image: url('file=wallpaper.jpg');background-repeat: no-repeat; background-size: contain;}
            """
        ) as demo:
        with gr.Accordion("README"):
            gr.Markdown("MEME Manipulation Tool")

        with gr.Tab("Change emotion"):
            with gr.Row():
                with gr.Column():
                    emtion_image_input = gr.Image()
                    emotion_text_input = gr.Radio(["happy", "fear", "sad", "angry", "disgust", "surprise", "neutral"], label="Emotion")
                    meme_text_input = gr.Textbox(lines=1, label="Meme text")            
                    change_emotion_button = gr.Button("Change emotion")
                with gr.Row(scale=1):
                    emotion_image_output = gr.Image()
            
        with gr.Tab("original-image"):
            with gr.Row():
                image_input = gr.Image()
                image_output = gr.Image()
            image_button = gr.Button("Convert")

        change_emotion_button.click(meme_app, inputs=[emtion_image_input, emotion_text_input, meme_text_input], outputs=emotion_image_output, )
        image_button.click(face_to_face, inputs=image_input, outputs=image_output)

    demo.launch()