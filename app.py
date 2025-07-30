import gradio as gr

def greet(name):
  return f"Hello World, my name's {name}!"

gr.Interface(fn=greet, input="text", outputs="text").launch()
