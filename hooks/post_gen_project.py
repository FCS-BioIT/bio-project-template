"""Cookiecutter hook to execute post project generation."""

import os


def remove_gitkeep_files():
    """Remove .gitkeep files."""
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file == '.gitkeep':
                os.remove(os.path.join(root, file))


def rename_gitignore():
    """Rename _gitignore to .gitignore."""
    old_path = os.path.join(os.getcwd(), '_gitignore')
    new_path = os.path.join(os.getcwd(), '.gitignore')

    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print("renaming gitignore")

    else:
        raise FileNotFoundError("_gitignore file not found")


if __name__ == "__main__":
    remove_gitkeep_files()
    rename_gitignore()
