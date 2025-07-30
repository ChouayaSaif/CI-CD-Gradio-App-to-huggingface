import gradio as gr

def greet(name):
    return f"Hello World, my name's {name}!"

gr.Interface(
    fn=greet,
    inputs="text",  # Changed from 'input' to 'inputs'
    outputs="text"
).launch()
