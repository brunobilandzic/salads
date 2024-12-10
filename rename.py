import glob
import os
from dotenv import load_dotenv

load_dotenv()

PATH_TO_FOLDER = os.getenv("PATH_TO_FOLDER")
SHEET_FILENAME = os.getenv("SHEET_FILENAME")


def recent():
    list_of_files = glob.glob(f"{PATH_TO_FOLDER}/*")
    latest_file = max(list_of_files, key=os.path.getctime)
    print(f"Most recent file in {PATH_TO_FOLDER} folder is {latest_file}")
    if not "order_export" in latest_file:
        raise FileNotFoundError
    return latest_file


def file_rename(full_name: str):
    file_name = full_name.split("flaying\\")[1]
    new_name = full_name.replace(file_name, SHEET_FILENAME)
    try:
        os.remove(new_name)
    except FileNotFoundError:
        print(f"file {new_name} does not exist")

    except:
        print("Unknown error...")
    os.rename(full_name, new_name)
    print(f"\nRenamed file {file_name} to {new_name}")

    return new_name


if __name__ == "__main__":
    try:
        file_rename(recent())
    except FileNotFoundError:
        print("please make new order_export")
    except:
        print("Unknown error...")
