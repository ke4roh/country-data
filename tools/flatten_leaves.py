import os
from pathlib import Path
import shutil

def flatten_index_dirs(base_path: Path) -> None:
    for root, dirs, files in os.walk(base_path, topdown=False):
        path = Path(root)
        index_file = path / "index.json"

        # If a directory contains only index.json
        if index_file.exists() and len(list(path.iterdir())) == 1:
            new_path = path.with_suffix(".json")
            print(f"Moving {index_file} -> {new_path}")
            shutil.move(str(index_file), str(new_path))
            path.rmdir()

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python flatten_index_dirs.py <base_directory>")
        sys.exit(1)

    base_dir=Path(sys.argv[1])
    if not base_dir.is_dir():
        raise ValueError(f"{str(base_dir)} is not a directory.")

    flatten_index_dirs(base_dir)
