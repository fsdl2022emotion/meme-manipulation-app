---
title: Meme Manipulation Gradio Space
emoji: 🏃
colorFrom: indigo
colorTo: green
sdk: gradio
sdk_version: 3.4
app_file: app.py
pinned: false
license: mit
---

# MEME Emotion Manipulation Tool

MEME Emotion Manipulation Tool is an app that allows you to manipulate the emotions of a person in a photo. You can also add text on the image to create a meme. 

This tool used the pretrained model and is modified based on the [GANmut Model](https://github.com/stefanodapolito/GANmut). You can view the source code of this tool in [GitHub](https://github.com/fsdl2022emotion/meme-manipulation-app) and [Gradio Space](https://huggingface.co/spaces/fsdl2022emotion/meme-manipulation-gradio-space) and give it a star if you like it!

## Instructions

1. install the libraries `pip install -r requirements.txt`
2. run `python app.py`

## Examples

Original        |  Result
:-------------------------:|:-------------------------:
![charles original](./examples/charles-frye.jpeg)  |  ![charles generated](./examples/charles-generated.png)
![sergey original](./examples/sergey.jpg)  |  ![sergey generated](./examples/sergey-generated.png)
![josh original](./examples/josh.jpg) |  ![josh generated](./examples/josh-generated.png)

## Limitations

As a MVP, the text drawing function does not work well on some images and it only works on relatively short text.
