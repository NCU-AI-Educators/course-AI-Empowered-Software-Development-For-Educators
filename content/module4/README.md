# 模块四实验环境配置指南

为了确保大家能够顺利完成实验，我们准备了一键配置脚本。

## 快速开始 (推荐)

1. **运行配置脚本**：
   打开终端 (Terminal) 或命令行 (CMD)，运行以下命令：
   ```bash
   python3 setup_lab.py
   ```
   *脚本会自动检测您的 Python 版本，创建虚拟环境，并安装所需库。*

2. **激活环境**：
   脚本运行结束后，会提示您如何激活环境。通常是：
   *   **Mac/Linux**: `source .venv_lab/bin/activate`
   *   **Windows**: `.venv_lab\Scripts\activate`

3. **启动实验**：
   ```bash
   jupyter notebook module4_experiment.ipynb
   ```

## 手动配置 (备选)

如果您熟悉 Python 环境管理，也可以手动安装：

```bash
pip install -r requirements.pip
jupyter notebook module4_experiment.ipynb
```

## 常见问题

*   **Q: 为什么要用脚本？**
    A: 它可以自动处理 Python 版本兼容性问题（例如避开不兼容的 Python 3.14），确保实验环境稳定。

*   **Q: 笔记本里不是有安装命令吗？**
    A: 是的，但如果您的基础 Python 环境有问题（如版本过高），笔记本可能根本无法启动。脚本是更保险的启动方式。
