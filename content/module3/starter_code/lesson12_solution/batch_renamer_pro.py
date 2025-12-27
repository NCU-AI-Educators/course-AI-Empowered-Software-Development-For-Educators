# -*- coding: utf-8 -*-

# =============================================================================
# 《AI赋能软件开发》课程
# 模块三，第12课 最终参考代码 (专业版)
#
# 这个“专业版”实现了课后练习中的所有挑战，并增加了命令行支持，
# 使其成为一个更强大、更灵活的实用工具。
#
# Pro版特性:
# 1. 命令行接口: 使用`argparse`模块，无需修改代码即可运行。
# 2. 智能学期生成: 能根据当前日期自动推断学期名称 (挑战3)。
# 3. 智能课程名猜测: 能根据文件夹路径猜测课程名称 (挑战4)。
# 4. 灵活的路径/前缀: 支持多种方式定义目标路径和文件前缀 (挑战1, 2)。
# 5. 安全演习模式: 提供`--dry-run`选项，只看不做，确保安全。
# 6. [新]格式转换: 支持`.doc`和`.docx`转PDF (需要`doc2docx`和`docx2pdf`库)。
# 7. [新]健壮性: 自动跳过脚本自身和已包含前缀的文件。
#
# This "Pro" version implements all the challenges from the lesson's exercises
# and adds command-line support, turning it into a more powerful and
# flexible utility.
#
# Pro Features:
# 1. Command-Line Interface: Uses the `argparse` module for configuration without code modification.
# 2. Smart Semester Generation: Automatically determines the semester name based on the current date (Challenge 3).
# 3. Smart Course Name Guessing: Guesses the course name from the folder path (Challenge 4).
# 4. Flexible Path/Prefix: Supports various ways to define the target path and file prefix (Challenges 1, 2).
# 5. Safe Dry-Run Mode: Includes a `--dry-run` option to preview changes without executing them.
# 6. [NEW] Format Conversion: Supports .doc and .docx to PDF (requires `doc2docx` and `docx2pdf` libraries).
# 7. [NEW] Robustness: Automatically skips the script itself and files that already have the prefix.
# =============================================================================

import os
import argparse
import datetime
import re
import sys

# --- 依赖检查 (Dependency Check) ---
# 检查转换功能所需的核心库是否存在
try:
    import docx2pdf
    DOCX2PDF_INSTALLED = True
except ImportError:
    DOCX2PDF_INSTALLED = False

try:
    import doc2docx
    DOC2DOCX_INSTALLED = True
except ImportError:
    DOC2DOCX_INSTALLED = False


def generate_semester_name():
    """
    根据当前日期智能生成学期名称。
    """
    today = datetime.date.today()
    year = today.year
    month = today.month

    if 9 <= month <= 12:
        return f"{year}秋"
    elif month == 1:
        return f"{year - 1}秋"
    elif 3 <= month <= 6:
        return f"{year}春"
    elif 7 <= month <= 8:
        return f"{year}夏"
    elif month == 2:
        while True:
            choice = input(f"当前是2月，请选择学期:\n1: {year - 1}秋\n2: {year}春\n请输入选项 (1或2): ")
            if choice == '1':
                return f"{year - 1}秋"
            elif choice == '2':
                return f"{year}春"
            else:
                print("无效输入，请重新选择。")
    return ""

def guess_course_name(path):
    """
    根据文件夹路径猜测课程名称。
    """
    if not path:
        return ""
    
    course_name = os.path.basename(os.path.abspath(path))
    course_name = re.sub(r'_\d{4}|\d{4}_', '', course_name)
    course_name = re.sub(r'[\d-]', ' ', course_name)
    course_name = course_name.replace('_', ' ')
    course_name = re.sub(r'\b(course|lecture|material)s?\b', '', course_name, flags=re.IGNORECASE)
    
    return course_name.strip().title()

def _convert_docx_to_pdf(docx_path):
    """
    [内部函数] 使用 docx2pdf 将单个 .docx 文件转换为PDF。
    """
    print(f"    > 步骤2: 转换 {os.path.basename(docx_path)} -> PDF...")
    try:
        docx2pdf.convert(docx_path)
        print(f"    > [成功] 已在同目录下生成PDF文件。")
    except Exception as e:
        print(f"    > [失败] PDF转换失败。错误: {e}")
        print(f"    > 请确保您已安装Microsoft Word，并已授予本程序控制Word的权限。")

def convert_word_to_pdf(file_path):
    """
    [转换调度器] 智能处理 .doc 或 .docx 文件到PDF的转换。
    """
    is_doc = file_path.lower().endswith('.doc')
    is_docx = file_path.lower().endswith('.docx')
    
    if is_docx:
        # 如果是.docx文件，直接转换
        _convert_docx_to_pdf(file_path)
        return

    if is_doc:
        # 如果是.doc文件，执行两步转换
        print(f"  检测到 .doc 文件，执行两步转换...")
        temp_docx_path = os.path.splitext(file_path)[0] + ".docx"
        
        # 步骤1: .doc -> .docx
        print(f"    > 步骤1: 转换 {os.path.basename(file_path)} -> .docx ...")
        try:
            doc2docx.convert(file_path, temp_docx_path)
            print(f"    > [成功] 已生成临时的 .docx 文件: {os.path.basename(temp_docx_path)}")
        except Exception as e:
            print(f"    > [失败] .doc -> .docx 转换失败。错误: {e}")
            return # 如果第一步失败，则停止

        # 步骤2: .docx -> .pdf
        _convert_docx_to_pdf(temp_docx_path)

        # 步骤3: 清理临时的.docx文件
        try:
            os.remove(temp_docx_path)
            print(f"    > 步骤3: 清理完成，已删除临时文件。")
        except OSError as e:
            print(f"    > [警告] 删除临时 .docx 文件失败。错误: {e}")

def batch_rename_files(folder_path, prefix, dry_run=False, convert_mode=None):
    """
    批量重命名并根据模式转换文件。
    """
    if dry_run:
        print("\n--- 演习模式（Dry Run）---")
        print("--- 以下操作将不会真实执行 ---\\n")
        
    print(f"--- 开始处理文件夹: {folder_path} ---")
    
    try:
        own_path = os.path.abspath(__file__)
    except NameError:
        own_path = None
    
    try:
        items = os.listdir(folder_path)
    except FileNotFoundError:
        print(f"错误：文件夹 '{folder_path}' 不存在。")
        return
    
    renamed_count = 0
    converted_count = 0
    
    for item_name in items:
        old_path = os.path.join(folder_path, item_name)
        
        if not os.path.isfile(old_path):
            continue

        if item_name.startswith('.'):
            continue

        absolute_old_path = os.path.abspath(old_path)
        if absolute_old_path == own_path:
            print(f"  [跳过] {item_name} (脚本自身)")
            continue

        if prefix and item_name.startswith(prefix):
            print(f"  [跳过] {item_name} (已包含前缀)")
            continue
        
        new_name = f"{prefix}{item_name}"
        new_path = os.path.join(folder_path, new_name)
        
        print(f"  [计划] {item_name} -> {new_name}")
        
        if not dry_run:
            try:
                os.rename(old_path, new_path)
                print(f"  [成功] 已重命名。")
                renamed_count += 1
            except OSError as e:
                print(f"  [失败] 重命名失败: {item_name}。错误: {e}")
                continue
        
        if convert_mode == 'word2pdf' and new_name.lower().endswith(('.docx', '.doc')):
            if dry_run:
                print(f"    > [演习] 计划转换为PDF。")
            else:
                convert_word_to_pdf(new_path)
                converted_count += 1

    print("\n--- 任务报告 ---")
    if dry_run:
        items_to_process = []
        for i in items:
            if not os.path.isfile(os.path.join(folder_path, i)) or i.startswith('.'):
                continue
            if own_path and os.path.abspath(os.path.join(folder_path, i)) == own_path:
                continue
            if prefix and i.startswith(prefix):
                continue
            items_to_process.append(i)
            
        planned_renames = len(items_to_process)
        planned_converts = len([i for i in items_to_process if i.lower().endswith(('.docx', '.doc'))])
        print(f"计划重命名 {planned_renames} 个文件。")
        if convert_mode == 'word2pdf':
            print(f"计划转换 {planned_converts} 个 Word 文件为PDF。")
    else:
        print(f"成功重命名 {renamed_count} 个文件。")
        if convert_mode == 'word2pdf':
            print(f"尝试转换 {converted_count} 个 Word 文件为PDF。")
    print("--- 处理完成 ---")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="批量文件重命名与转换工具 (专业版)",
        formatter_class=argparse.RawTextHelpFormatter # 保持帮助信息格式
    )
    
    parser.add_argument(
        "folder_path", 
        nargs='?', 
        default=".", 
        help="要处理的文件夹路径。\n如果留空，则默认处理当前脚本所在的文件夹。"
    )
    parser.add_argument(
        "-p", "--prefix", 
        help="完整的前缀字符串。\n如果提供此项，将忽略学期和课程名参数。"
    )
    parser.add_argument(
        "-s", "--semester", 
        help="学期名称 (例如 '2025秋')。\n如果留空，将根据当前日期自动生成。"
    )
    parser.add_argument(
        "-c", "--course", 
        help="课程名称 (例如 '软件工程')。\n如果留空，将尝试从文件夹路径中猜测。"
    )
    parser.add_argument(
        "--no-guess-course",
        action="store_true",
        help="禁用从文件夹路径中猜测课程名称的功能。"
    )
    parser.add_argument(
        "--convert",
        choices=['word2pdf'],
        help="在重命名后执行格式转换。\n目前支持: 'word2pdf' (Word转PDF)。"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="演习模式：只显示将要执行的操作，不实际重命名文件。"
    )
    
    args = parser.parse_args()
    
    # --- 依赖检查 ---
    if args.convert == 'word2pdf':
        missing_libs = []
        if not DOCX2PDF_INSTALLED:
            missing_libs.append("docx2pdf")
        if not DOC2DOCX_INSTALLED:
            missing_libs.append("doc2docx")
        
        if missing_libs:
            print("错误：缺少转换所需的库。", file=sys.stderr)
            for lib in missing_libs:
                print(f"请在终端运行以下命令来安装 '{lib}':", file=sys.stderr)
                print(f"    {sys.executable} -m pip install --break-system-packages {lib}", file=sys.stderr)
            print("\n注意：此功能还需要您在电脑上安装 Microsoft Word。", file=sys.stderr)
            sys.exit(1)

    # --- 决定前缀 ---
    print("--- 参数分析 ---")
    final_prefix = ""
    if args.prefix:
        final_prefix = args.prefix
        print(f"模式: 使用用户指定前缀。")
    else:
        print(f"模式: 自动组合前缀。")
        semester_name = args.semester if args.semester else generate_semester_name()
        print(f"  > 学期: '{semester_name}' (来源: {'用户指定' if args.semester else '自动生成'})")
        
        course_name = ""
        if args.course:
            course_name = args.course
            print(f"  > 课程: '{course_name}' (来源: 用户指定)")
        elif not args.no_guess_course:
            course_name = guess_course_name(args.folder_path)
            print(f"  > 课程: '{course_name}' (来源: {'路径猜测' if course_name else '猜测失败'})")
        
        if semester_name and course_name:
            final_prefix = f"{semester_name}-{course_name}-"
        elif semester_name:
            final_prefix = f"{semester_name}-"
        elif course_name:
            final_prefix = f"{course_name}-"
    
    if final_prefix:
        print(f"最终前缀: '{final_prefix}'")
    else:
        print("警告：未能生成有效前缀，将不会执行重命名。")
    print("----------------\n")

    # --- 执行操作 ---
    if final_prefix or args.convert:
        if not final_prefix:
            print("提示：前缀为空，仅执行转换操作（如果适用）。\n")
        batch_rename_files(args.folder_path, final_prefix, args.dry_run, args.convert)
    else:
        print("由于前缀为空且未指定转换任务，没有执行任何操作。")

    # --- 使用示例 ---
    # python batch_renamer_pro.py ./test_folder -s "2025夏" -c "Python编程"
    # python batch_renamer_pro.py ./test_folder --prefix "FINAL-"
    # python batch_renamer_pro.py ./test_folder --dry-run
    # python batch_renamer_pro.py # 处理当前文件夹，并全自动猜测
    # python batch_renamer_pro.py /path/to/my/course --no-guess-course
    # python batch_renamer_pro.py ./test_folder --convert word2pdf