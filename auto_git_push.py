import os
import subprocess

def auto_push():
    print("[🔁] Auto update")

    # 添加所有文件
    subprocess.call(["git", "add", "."])

    # 提交修改
    subprocess.call(["git", "commit", "-m", "Auto update"])

    # 自动推送到当前仓库（不再写死地址）
    subprocess.call(["git", "push"])

if __name__ == "__main__":
    auto_push()
