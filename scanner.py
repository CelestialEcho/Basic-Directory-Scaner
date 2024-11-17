import os
from colorama import *
from pathlib import Path

init(autoreset=True)

def getItems(directory):
    items = []
    path = Path(directory)
    
    if not path.exists():
        return items
    
    for item in path.iterdir():
        if item.is_dir():
            items.append(f"~{item.name}")
        elif item.is_file():
            name, ext = item.stem, item.suffix
            items.append(f"{name}{ext}")
    
    return items

def exploreDirectory(directory, level=0, is_last=True):
    indent = "    " * level
    items = getItems(directory)
    
    if not items:
        return
    
    for i, item in enumerate(items):
        if item.endswith(".dll") or item.endswith(".sys") or item.endswith(".Msi"):
            print(f"{indent}{'┗' if is_last else '┃'}━ {Fore.RED}{item}")
        elif item[0] == "~":
            print(f"{indent}{'┗' if is_last else '┗'} {Fore.YELLOW}{item}/")
            subdirectory_path = os.path.join(directory, item[1:])
            exploreDirectory(subdirectory_path, level + 1, is_last=(i == len(items) - 1))
        else:
            print(f"{indent}{'┗' if is_last else '┃'}━ {Fore.GREEN}{item}")


start_directory = input(r"input your directory (\\): ") #D:\[C++]Projects
exploreDirectory(start_directory)
