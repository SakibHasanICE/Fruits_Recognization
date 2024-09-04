from fastai.vision.all import *
import gradio as gr

# import pathlib
# temp = pathlib.PosixPath
# pathlib.PosixPath = pathlib.WindowsPath
fruit_labels = (
    'Apples', 'Bael', 'Blackberry', 'Cherry', 'Cucumber', 'Grapes', 'Ice Apple', 'Kiwi', 'Litchi', 'Mangoes', 'Mulberry', 'Muskmelon', 'Oranges', 'Papaya', 'Peaches', 'Pineapples', 'Plums', 'Strawberries', 'Tomato', 'Watermelon'
)

model = load_learner('fruit-recognizer-v4.pkl')

def recognize_image(image):
    pred, idx, probs = model.predict(image)
    return dict(zip(fruit_labels, map(float, probs)))

image = gr.Image()
label = gr.Label()
# examples = [
#     'litchi.jpg',
#     'mango.jpg'
#     ]

iface = gr.Interface(fn=recognize_image, inputs=image, outputs=label)
iface.launch(inline=False)