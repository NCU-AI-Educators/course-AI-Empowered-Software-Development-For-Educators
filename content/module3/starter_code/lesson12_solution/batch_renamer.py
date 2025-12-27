# -*- coding: utf-8 -*-

# =============================================================================
# 《AI赋能软件开发》课程
# 模块三，第12课 最终参考代码
#
# 本文件是第12课“批量文件整理助手”项目的最终参考实现。
# 它严格遵循了我们在课程中设计的“算法蓝图”和使用的“终极指令”。
#
# 特点:
# 1. 导入了os模块用于文件系统操作。
# 2. 核心逻辑被封装在`batch_rename_files`函数中。
# 3. 使用`os.listdir`, `os.path.join`, `os.path.isfile`, `os.rename`来完成任务。
# 4. 包含了对子文件夹和隐藏文件的过滤，增加了代码的健壮性。
# 5. 使用`if __name__ == "__main__:"`结构，这是Python脚本的一个最佳实践。
#
# This file is the final reference implementation for the "Batch File Renamer"
# project from Lesson 12. It strictly follows the "algorithm blueprint" and
# the "final prompt" we designed in the course.
#
# Features:
# 1. Imports the `os` module for filesystem operations.
# 2. The core logic is encapsulated in the `batch_rename_files` function.
# 3. Uses `os.listdir`, `os.path.join`, `os.path.isfile`, and `os.rename`.
# 4. Includes filtering for subdirectories and hidden files to make the code more robust.
# 5. Uses the `if __name__ == "__main__:"` construct, a best practice for Python scripts.
# =============================================================================

import os

def batch_rename_files(folder_path, prefix):
    """
    批量重命名指定文件夹内的所有文件，为其添加统一前缀。
    
    :param folder_path: str, 目标文件夹的路径。
    :param prefix: str, 要添加到每个文件名前的前缀。
    """
    print(f"--- 开始处理文件夹: {folder_path} ---")
    
    try:
        # 获取文件夹中的所有文件名和文件夹名
        items = os.listdir(folder_path)
    except FileNotFoundError:
        print(f"错误：文件夹 '{folder_path}' 不存在。")
        return
    
    renamed_count = 0
    for item_name in items:
        # 构建完整路径
        old_path = os.path.join(folder_path, item_name)
        
        # 判断是否是文件，并且不是隐藏文件（以.开头）
        if os.path.isfile(old_path) and not item_name.startswith('.'):
            # 构建新文件名和新路径
            new_name = f"{prefix}{item_name}"
            new_path = os.path.join(folder_path, new_name)
            
            # 执行重命名
            try:
                os.rename(old_path, new_path)
                print(f"  已重命名: {item_name} -> {new_name}")
                renamed_count += 1
            except OSError as e:
                print(f"  重命名失败: {item_name}。错误: {e}")

    print(f"--- 处理完成。共重命名了 {renamed_count} 个文件。 ---")


# --- 脚本主入口 ---
if __name__ == "__main__:":
    # ===============================================================
    #                        ** 用户配置区 **
    #
    # 在运行脚本前，请修改以下两个变量：
    # 1. TARGET_FOLDER: 你想要整理的文件夹的路径。
    #    - Windows示例: "C:\Users\YourUser\Desktop\课程资料"
    #    - macOS/Linux示例: "/Users/YourUser/Documents/课程资料"
    #    - 使用 "./test_folder" 来测试我们课上创建的沙盒文件夹。
    # 2. PREFIX: 你想要添加的前缀。
    # ===============================================================
    
    TARGET_FOLDER = "./test_folder"  # <--- 修改这里
    PREFIX = "2025秋-软件工程-"      # <--- 修改这里

    # 调用核心函数，执行重命名操作
    batch_rename_files(TARGET_FOLDER, PREFIX)
