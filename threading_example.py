import threading
import time
from tqdm import tqdm

def worker(name, delay, progress_bar):
    for _ in tqdm(range(100), desc=f"woker thread {name}", leave=False):
        time.sleep(delay/100)
        progress_bar.update(1)
    print(f"worker thread {name} finished")

def main():
    threads = []
    progress_bars = []

    # 创建3个工作线程
    for i in range(3):
        progress_bar = tqdm(total=100, desc=f"Thread-{i}", position=i)
        progress_bars.append(progress_bar)
        t = threading.Thread(target=worker, args=(f"Thread-{i}", i+1, progress_bar))
        threads.append(t)
        t.start()

    # 等待所有线程完成
    for t in threads:
        t.join()

    # 关闭进度条
    for bar in progress_bars:
        bar.close()

    print("all threads finished")

if __name__ == "__main__":
    main()