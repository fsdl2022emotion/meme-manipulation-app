from functools import partial
import argparse

import gradio as gr
import numpy as np

from emotion_synthesizer.emotion_synthesis import EmotionSynthesizer
from drawer.simple_draw import add_text


DEFAULT_MODEL_PATH = "./emotion_synthesizer/learned_generators/gaus_2d/1800000-G.ckpt"
DEFAULT_MODEL_TYPE = "gaussian"


def make_meme(original_image, new_emotion, secondary_emotion=None, intensity=None, text=None, wandb_artifact=None):
    # workaround for gradio bug (!?)
    secondary_emotion = None if (secondary_emotion == "None" or secondary_emotion == "") else secondary_emotion
    print(f"Secondary emotion: {secondary_emotion}")
    
    if wandb_artifact:
        artifact_dir = artifact.download()
        artifact_path = f"{artifact_dir}/1800000-G.ckpt"
        model_type = artifact.metadata["model_type"]
        model = EmotionSynthesizer(model_path=artifact_path, model_type=model_type)
    else:
        model = EmotionSynthesizer(DEFAULT_MODEL_PATH, DEFAULT_MODEL_TYPE)
    try:
        generated_image = model.predict(original_image, new_emotion, secondary_emotion, intensity)
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


    with gr.Blocks(
        title="MEME Manipulation Tool",
        css ="""
            .gradio-container {background-image: url('file=assets/wallpaper.png');background-repeat: no-repeat; background-size: cover;}
            """
        ) as demo:
        with gr.Accordion("About"):
            gr.Markdown("""
            MEME Emotion Manipulation Tool is an open source project of the [Full Stack Deep Learning](https://fullstackdeeplearning.com) course.<br>
            It is a tool that allows you to manipulate the emotions of a person in a photo. You can also add text on the image to create a meme. We will not save any input from the users. <br>
            This tool used the pretrained model and is modified based on the [GANmut Model](https://github.com/stefanodapolito/GANmut). 
            You can view the source code of this tool in [GitHub](https://github.com/fsdl2022emotion/meme-manipulation-app) and [Gradio Space](https://huggingface.co/spaces/fsdl2022emotion/meme-manipulation-gradio-space) and give it a star if you like it!<br>
            """)
        with gr.Accordion("Valid Mapping"):
            gr.Markdown("""
            You can use purely the primary emotion or combine it with the secondary emotion for image generation. <br>
            Yet only some of the combinations are valid. Please refer to the below mapping: <br>
            ![valid mapping](https://i.ibb.co/5rCXgfB/Screenshot-2022-10-14-at-11-59-28-AM.png)
            """)
        with gr.Tab("Change emotion"):
            with gr.Row():
                with gr.Column():
                    emtion_image_input = gr.Image()
                    emotion_text_input = gr.Radio(["happy", "fear", "sad", "angry", "disgust", "surprise", "neutral"], label="Primary Emotion (Required)")
                    emotion_text_input2 = gr.Radio(["happy", "fear", "sad", "angry", "disgust", "surprise", "neutral"], label="Secondary Emotion (Optional)", value=None)
                    intensity = gr.Slider(0, 1, label="Intensity")
                    meme_text_input = gr.Textbox(lines=1, label="Meme text")            
                    change_emotion_button = gr.Button("Change emotion")
                with gr.Row(scale=1):
                    emotion_image_output = gr.Image()
        change_emotion_button.click(meme_app, inputs=[emtion_image_input, emotion_text_input, emotion_text_input2, intensity, meme_text_input], outputs=emotion_image_output, )
        
        ############################# only show on demo day #############################
        with gr.Tab("original-image"):
            with gr.Row():
                image_input = gr.Image()
                image_output = gr.Image()
            image_button = gr.Button("Convert")
        image_button.click(face_to_face, inputs=image_input, outputs=image_output)
        ##################################################################################

        gr.Examples(examples=[
            ["examples/charles-frye.jpeg", "surprise", "When I got a new idea"], 
            ["examples/sergey.jpg", "neutral", "I did smile"],
            ["examples/josh.jpg", "angry", "nasdaq index"],
            ], 
            inputs=[emtion_image_input, emotion_text_input, meme_text_input],
            fn=meme_app,
            )
        

    demo.launch(favicon_path="./assets/favicon.png")