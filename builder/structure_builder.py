import os

def create_project_structure(structure: dict):
    base_path = structure["project_name"]

    for file in structure["files"]:
        full_path = os.path.join(base_path, file["path"])
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w") as f:
            f.write(file["content"])
