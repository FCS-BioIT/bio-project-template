import os


ASSAY_MAP = {
    "1": "mRNA",
    "2": "totRNA",
    "3": "DNA",
    "4": "scRNA10x",
    "5": "snRNA10x",
    "6": "int",
    "7": "px",
    "8": "mox",
    "9": "mgx",
    "10": "mome",
    "11": "chip",
    "12": "atac",
    "13": "wgbs",
    "14": "miRNA",
    "15": "st"
}


def select_assays():
    """Interactively select assays based on numbers."""
    selected_assays = []
    while True:
        print("\nAvailable assays:")
        for number, name in ASSAY_MAP.items():
            print(f"{number}. {name}")
        print("0. Finish selection\n")

        choice = input("Enter the number corresponding to your choice: ")

        if choice == "0":
            break
        elif choice in ASSAY_MAP:
            if ASSAY_MAP[choice] not in selected_assays:
                selected_assays.append(ASSAY_MAP[choice])
                print(f"Added {ASSAY_MAP[choice]}.")
            else:
                print(f"{ASSAY_MAP[choice]} is already selected.")
        else:
            print("Invalid choice. Please try again.")

    return selected_assays


def update_project_slug(selected_assays):
    """Update the project directory name with selected assays."""
    slug_prefix = "{{ cookiecutter.research_group_id.lower() }}-{{ cookiecutter.description.lower().replace(' ', '-') }}"
    assay_slug = "-".join(selected_assays).lower()
    new_slug = f"{slug_prefix}-{assay_slug}"

    # Rename the project directory
    current_dir = os.getcwd()
    new_dir = os.path.join(os.path.dirname(current_dir), new_slug)

    os.rename(current_dir, new_dir)
    print(f"Project directory renamed to: {new_slug}")

    return new_slug


def replace_project_slug_in_files(new_slug):
    """Replace the old project slug with the new one in the generated files."""
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith(('.yaml', '.yml', '.md', '.txt')):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Replace occurrences of old slug
                old_slug = "{{ cookiecutter.project_slug }}"
                updated_content = content.replace(old_slug, new_slug)

                # Write back if changes were made
                if content != updated_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(updated_content)
                    print(f"Updated {file_path} with new slug: {new_slug}")


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
        print("Renamed _gitignore to .gitignore.")

    else:
        raise FileNotFoundError("_gitignore file not found")


if __name__ == "__main__":
    # Select assays before proceeding
    selected_assays = select_assays()

    if not selected_assays:
        print("No assays selected. Exiting.")
        exit(1)

    # Update the project directory name
    new_slug = update_project_slug(selected_assays)

    # Replace old slug in files
    replace_project_slug_in_files(new_slug)

    # Continue with post-generation steps
    remove_gitkeep_files()
    rename_gitignore()

