# 📘 Universal VL-Driven Knowledge Base Builder 
**(基于视觉大模型的全自动教材/课件解析与知识库重构工具)**

这是一个强大且纯靠**“视觉多模态大模型 (VLM)”**驱动的学术资料逆向工程师。它的核心目的是将任何厚重的教材、练习册 PDF转化为一份**排版精良、具有上下文连贯性**的 Markdown 高清知识库。

无论你的教材中包含了多复杂的**高阶公式**、**学术图表**（如经济学供需曲线、无差异曲线等），它都能够像一个真正的人类学者一样去“看懂”图片，解释图表，并总结知识要点。

---

## ✨ 核心特性 (Key Features)

* **🧠 独创“滑动窗口上下文连读”技术：** 
  传统的单页 OCR/多模态解析往往会在翻页或跨页时打断公式与逻辑。本项目在并发管线中，强制要求大模型在解析**当前页**时，必须参考**上一页刚刚总结过的 2000 字内容**。这使得大纲连贯，有效剪裁废话，彻底消除知识断层。
* **👁️ 降维打击的视觉理解：**
  摒弃传统的基于文本库（如 PyPDF）提取方案。直接将教材页面高清渲染为 PNG 再投喂给强大的视觉模型（默认支持 `Qwen3-VL-235B`），它能无损还原排版、提炼核心概念、深度解读抽象的数据走向与图表变化。
* **⚡ 线程池并发与 API Key 轮替调度：**
  处理一本动辄上千页的教材会遇到高昂的 API Rate limits。项目内建原生 `Queue` 与并发线程池，辅以 API Key 自动抽样轮换机制（以 SiliconFlow 等聚合池为例），直接打满带宽，将解析效率提升数倍。
* **📂 自动探测结构的智能分块 (Universal Parsing)：**
  基于复杂正则矩阵，支持全系学术结构探测（自动匹配 `Chapter X`, `第X章`, `Unit`, `Part`, `Quiz` 等）。对于完全无目录结构的扫描版图书，将自动退化至智能分片（Chunking）模式以确保高稳定运行。

---

## 🛠️ 安装与配置 (Installation)

**1. 克隆仓库与依赖安装**
```bash
git clone https://github.com/YourUsername/your-repo-name.git
cd your-repo-name
pip install pymupdf openai
```

**2. 配置 API Keys**
本工具依赖第三方大模型的 API 接口（默认以 [SiliconFlow (硅基流动)](https://siliconflow.cn/) 为例提供强力廉价的多模态支持）。
打开 `universal_kb_builder.py`（如果需要旧版组件，则查看对应脚本），在头部填入你的 API Key 矩阵：
```python
API_KEYS = [
    "sk-your-key-1.......",
    "sk-your-key-2......."
]
BASE_URL = "https://api.siliconflow.cn/v1"
MODEL_NAME = "Qwen/Qwen3-VL-235B-A22B-Thinking" # 可自行替换为您偏好的纯视觉大模型
```

---

## 🚀 极简用法 (Usage)

我们推荐使用最新整合完毕的终极自动化脚本：

```bash
python universal_kb_builder.py /path/to/您的教科书名称.pdf
```

**运行效果全自动演进：**
1. 自动在同级目录下创建一个名为 `您的教科书名称` 的专属工作区 (Database)。
2. 第一步：探测大纲结构，静默在 `temp_assets/` 高速将全本图书切割为章节切片库。
3. 第二步：唤醒多线程工人，并发解析章节、提炼图表，并存入 `markdown_parts/`。
4. 第三步：全流程完成后，输出一部完美的终极知识库大全集：`您的教科书名称_KnowledgeBase.md`。

---

## 📁 测试用数据

如果您的仓库中看到名为 `微观经济学` 的目录，那是用来测试的，经过一些同学使用后证明知识库效果不错


