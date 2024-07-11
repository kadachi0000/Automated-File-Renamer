"""a program to rename files"""

import os
from pathlib import Path


def user_input():
    """a function to gather user requirements for name and return the name format"""
    while True:
        series = input("What is the series's name? ")
        season = int(input("What season is it? "))
        season_format = f"S{season:02d}"
        episode = int(input("What number is the first episode? "))
        episode_format = f"E{episode:02d}"
        name_format = f"{series} {season_format}"
        confirmed = input(f"The episodes will be renamed: {name_format}{episode_format}. "
                          f"Is that correct? Type Y or N. ")
        if confirmed.lower() == "y":
            return name_format, episode_format
        else:
            pass


def make_file_list():
    """a function which makes two separate lists: file list which contains all videos in the folder, and deletion_list
    which contains any txt or img files. Program must be placed in the same folder."""
    ignore_ext = ".py"
    banned_ext = ".txt", ".jpg", ".jpeg", ".png"
    file_list = []
    deletion_list = []
    for file in os.listdir("."):
        if file.endswith(banned_ext):
            deletion_list.append(file)
        elif ignore_ext not in file:
            file_list.append(file)
    return file_list, deletion_list


def rename_files(file_list, name_format, episode_format):
    """a function to rename the files"""
    i = 1
    for file in file_list:
        ext = Path(file).suffix
        desired_name = f"{name_format}{episode_format}{ext}"
        os.rename(file, desired_name)
        i += 1
        episode_format = f"E{i:02d}"


def delete_files(deletion_list):
    """a function for deleting txt and img files in the folder"""
    print(f"Deletion List: {deletion_list}")
    confirm = input("Would you like to delete the above files? Type Y or N.")
    if confirm.lower() == "y":
        for file in deletion_list:
            os.remove(file)


def main():
    name_format, episode_format = user_input()
    file_list, deletion_list = make_file_list()
    delete_files(deletion_list)
    rename_files(file_list, name_format, episode_format)


if __name__ == "__main__":
    main()
