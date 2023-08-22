import argparse
from pathlib import Path
from shutil import copyfile
from threading import Thread
import logging

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--source", help="source folder", required=True)
parser.add_argument("-o", "--output", help="output folder", default="dist")
args = vars(parser.parse_args())

source = args.get("source")
output = args.get("output")

folders = []

def grab_folders(path):
    for item in path.iterdir():
        if item.is_dir():
            folders.append(item)
            grab_folders(item)

def copy_file(path):
    for item in path.iterdir():
        if item.is_file():
            ext = item.suffix
            new_path = output_folder / ext
            try:
                new_path.mkdir(exist_ok=True, parents=True)
                copyfile(item, new_path / item.name)
            except OSError as err:
                logging.error(err)

if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR, format="%(threadName)s %(message)s")
    base_folder = Path(source)
    output_folder = Path(output)
    folders.append(base_folder)
    grab_folders(base_folder)

    threads = []
    for folder in folders:
        th = Thread(target=copy_file, args=(folder,))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()

    print("Копіювання завершено.")