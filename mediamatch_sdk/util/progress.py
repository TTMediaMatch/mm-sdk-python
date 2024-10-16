import time
import sys
from tqdm import tqdm

def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█'):
    return
    """
    打印进度条到控制台，显示 cur/total 信息
    :param iteration: 当前迭代次数
    :param total: 总迭代次数
    :param prefix: 进度条前缀字符串
    :param suffix: 进度条后缀字符串
    :param decimals: 小数位数
    :param length: 进度条长度
    :param fill: 进度条填充字符
    """
    percent = f"{100 * (iteration / float(total)):.{decimals}f}"
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    # 使用 ANSI 代码清除行并打印进度条
    print(f'\033[2K\r{prefix} |{bar}| {percent}% {iteration}/{total} {suffix}', end='\r')
    # 打印100%完成的新行
    if iteration == total:
        print()

def main():
    # 示例用法
    total_items = 100

    # 打印其他东西
    print("Starting the progress...")

    # 初始化进度条
    print_progress_bar(0, total_items, prefix='Progress:', suffix='Complete', length=50)

    for i in range(total_items):
        time.sleep(0.05)  # 模拟任务处理时间
        # 更新进度条
        print_progress_bar(i + 1, total_items, prefix='Progress:', suffix='Complete', length=50)

    # 打印其他东西
    print("Progress complete!")


if __name__ == "__main__":
    main()
