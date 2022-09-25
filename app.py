import gradio as gr
import numpy as np


def mock_ganmut(img):
    return img

def emotion_synthesis(original_img, new_emotion):
    if new_emotion == "happy":
        return mock_ganmut(original_img)
    elif new_emotion == "fear":
        return mock_ganmut(original_img)
    elif new_emotion == "sad":
        return mock_ganmut(original_img)
    elif new_emotion == "angry":
        return mock_ganmut(original_img)
    elif new_emotion == "disgust":
        return mock_ganmut(original_img)
    elif new_emotion == "surprise":
        return mock_ganmut(original_img)
    elif new_emotion == "neutral":
        return mock_ganmut(original_img)

def flip_image(x):
    return np.fliplr(x)


if __name__ == "__main__":

    title = "MEME Manipulation Tool"
    description = "MEME Manipulation Tool is an app..."
    article = "example article"
    examples=[["example1"]]

    with gr.Blocks(title=title) as demo:
        gr.Markdown("Chaning emotion or other-face2face")
        with gr.Tab("Change emotion"):
            emtion_image_input = gr.Image()
            emotion_text_input = gr.Dropdown(["happy", "fear", "sad", "angry", "disgust", "surprise", "neutral"])
            change_emotion_button = gr.Button("Change emotion")
            emotion_image_output = gr.Image()
            
        with gr.Tab("<other face2face app>"):
            with gr.Row():
                image_input = gr.Image()
                image_output = gr.Image()
            image_button = gr.Button("Convert")

        with gr.Accordion("README"):
            gr.Markdown("MEME Manipulation Tool")

        change_emotion_button.click(emotion_synthesis, inputs=[emtion_image_input, emotion_text_input], outputs=emotion_image_output, )
        image_button.click(flip_image, inputs=image_input, outputs=image_output)

    demo.launch()