import gradio as gr
import numpy as np

from emotion_synthesizer.emotion_synthesis import EmotionSynthesizer


def make_meme(original_image, new_emotion, text):
    model = EmotionSynthesizer()
    generated_image = model.predict(original_image, new_emotion)
    output_image = add_text(generated_image, text)
    return output_image

def add_text(image, text):
    #TODO
    return image

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