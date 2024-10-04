"""Cookiecutter hook to execute post project generation."""

import os


def remove_gitkeep_files():
    """Remove .gitkeep files."""
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file == '.gitkeep':
                os.remove(os.path.join(root, file))


if __name__ == "__main__":
    remove_gitkeep_files()
