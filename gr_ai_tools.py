import gradio as gr

def ai_tool(text, func):
    if func == "文本摘要":
        return f"【摘要】{text[:20]}..."
    elif func == "情感分析":
        return "积极情感" if any(i in text for i in ["好","喜欢","开心"]) else "消极/中性"
    elif func == "关键词提取":
        return "关键词：" + "、".join(text[:10].split())
    elif func == "文案改写":
        return "【改写】" + text + "（优化表达）"
    return "请选择功能"

with gr.Blocks(title="AI文本小助手") as demo:
    gr.Markdown("## 🤖 AI文本处理小助手")
    text = gr.Textbox(label="输入文本", lines=3)
    func = gr.Dropdown(["文本摘要","情感分析","关键词提取","文案改写"], label="选择功能")
    btn = gr.Button("开始处理")
    out = gr.Textbox(label="结果")
    btn.click(ai_tool, inputs=[text, func], outputs=out)

if __name__ == "__main__":
    demo.launch(share=True)
