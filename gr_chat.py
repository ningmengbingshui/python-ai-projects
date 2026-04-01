import gradio as gr

def chat(msg, history):
    return f"AI助手：{msg}（已收到你的消息）"

demo = gr.ChatInterface(
    chat,
    title="🤖 AI聊天助手",
    retry_btn="重新生成",
    undo_btn="撤回",
    clear_btn="清空"
)

if __name__ == "__main__":
    demo.launch(share=True)
