
from netfree_unstrict_ssl import unstrict_ssl
unstrict_ssl()
import os

import gradio as gr
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def ask_llm(prompt):
    if not prompt.strip():
        return ""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text


with gr.Blocks() as demo:

    gr.Markdown("# 🤖 CLAI")

    user_input = gr.Textbox(
        label="Request",
        placeholder="Create a folder called test",
    )

    output = gr.Textbox(
        label="Response",
        lines=10,
    )

    btn = gr.Button("Send")

    btn.click(
        fn=ask_llm,
        inputs=user_input,
        outputs=output,
    )

demo.launch()