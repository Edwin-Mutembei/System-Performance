import time
import psutil

def display_usage(cpu_usage, mem_usage, bars = 100):
    cpu_percent = (cpu_usage/100.0)
    cpu_bar ='*' * int(cpu_percent * bars) + '_' * (bars - int(cpu_percent * bars))

    mem_percent = (mem_usage/100)
    mem_bar = '!' * int(mem_usage * bars) + '_' * (bars - int(mem_percent * bars))

    print(f"\rcpu Usage: |{cpu_bar}| {cpu_usage:.2f}%  ", end='')
    print(f"MEM Usage: |{mem_bar}| {mem_usage:.2f}%  ", end='\r')


while True:
    display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent, 20)
    time.sleep(0.5)
# https://medium.com/@dipan.saha/managing-git-repositories-with-vscode-setting-up-a-virtual-environment-62980b9e8106#:~:text=Open%20a%20powershell%20terminal%20within,virtual%20environment%20to%20your%20workspace.


# url for virtual environment