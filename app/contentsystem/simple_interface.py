"""
Simple and reliable interface for the viral money content generator.
"""

import gradio as gr
from money_video_generator import MoneyContentGenerator
import os

def generate_content(method, amount, timeframe, duration, platform):
    """Generate viral money-making content."""
    try:
        # Initialize generator
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            return "Error: Please set GROQ_API_KEY environment variable", ""
            
        generator = MoneyContentGenerator(api_key)
        
        # Generate content
        content = generator.generate_money_content(
            method=method,
            amount=amount,
            timeframe=timeframe,
            duration=duration
        )
        
        return content, f"Content generated successfully for {platform}!"
    except Exception as e:
        return f"Error: {str(e)}", "Generation failed"

# Create a simple interface
demo = gr.Interface(
    fn=generate_content,
    inputs=[
        gr.Dropdown(
            choices=["AI Tools", "Freelancing", "Social Media Marketing", "Dropshipping"],
            label="Money-Making Method",
            value="AI Tools"
        ),
        gr.Textbox(label="Earnings Amount", value="$1,000"),
        gr.Dropdown(
            choices=["Day", "Week", "Month"],
            label="Timeframe",
            value="Week"
        ),
        gr.Radio(
            choices=["short", "long"],
            label="Content Duration",
            value="short"
        ),
        gr.Radio(
            choices=["TikTok", "YouTube", "Instagram"],
            label="Platform",
            value="TikTok"
        )
    ],
    outputs=[
        gr.Textbox(label="Generated Content", lines=10),
        gr.Textbox(label="Status")
    ],
    title="💰 Viral Money Content Generator",
    description="Create viral content about making money online",
    theme=gr.themes.Soft(
        primary_hue="blue",
        secondary_hue="orange",
        neutral_hue="slate",
        text_size=gr.themes.sizes.text_lg,
    ),
    allow_flagging="never"
)

if __name__ == "__main__":
    demo.launch(share=True)
