import glob
import os
from dotenv import load_dotenv

load_dotenv()


def ff():
    path = os.getenv("PATH_TO_FOLDER")
    print(path)


def recent():
    folder = os.getenv("PATH_TO_FOLDER")
    list_of_files = glob.glob(f"{folder}/*")

    latest_file = max(list_of_files, key=os.path.getctime)
    print(f"Most recent file in {folder} folder is {latest_file}")


if __name__ == "__main__":
    recent()
