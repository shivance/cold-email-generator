from config import Config
import gradio as gr

from agent.agent import entrypoint

config = Config.load_config()


interface = gr.Interface(
    fn=entrypoint,
    inputs=gr.Textbox(
        lines=1,
        placeholder="Enter the job posting url here...",
        label="Job Posting URL",
    ),
    outputs=gr.Textbox(lines=15, label="Generated Cold Email"),
)

if __name__ == "__main__":
    interface.queue().launch()
