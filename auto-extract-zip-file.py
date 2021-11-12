# Import some library
from zipfile import ZipFile
import os


def get_all_file_paths(directory):

    # initializing empty file paths list
    file_paths = []

    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    # returning all file paths
    return file_paths


def main():
    directory = input("Enter your rar files' path: ")
    file_paths = get_all_file_paths(directory)
    for i in file_paths:
        print(i)
        print("=" * len(i))
        print()
    destination = input(
        "Where do you want extract these files(enter your path): ")

    counter = 0
    for j in file_paths:
        os.mkdir(path=f"{destination}\Part_{counter}")
        with ZipFile(j, 'r') as zip:
            print()
            print("Extracting....")
            zip.extractall(path=f"{destination}\Part_{counter}")
            zip.printdir()
            print("Done !")

        counter += 1


if __name__ == "__main__":
    main()
