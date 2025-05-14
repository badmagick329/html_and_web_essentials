import sys
from pathlib import Path


def main():
    input_file, parent_dir = get_input_and_parent()

    if input("Continue? (y/n) ").strip().lower() != "y":
        sys.exit(0)

    body_and_header = read_body_and_header(file=input_file)
    target_files = [f for f in parent_dir.glob("*.html") if f != input_file]
    print(f"Target files: {[f.name for f in target_files]}")
    replace_body_and_header(
        target_files=target_files,
        body_and_header=body_and_header,
    )


def get_input_and_parent() -> tuple[Path, Path]:
    if len(sys.argv) < 2:
        print("no input file")
        print("py script.py source.html")
        sys.exit(0)

    input_file = Path(sys.argv[1]).resolve().absolute()
    if not input_file.exists():
        print("Input file does not exist. check path")

    parent_dir = input_file.parent
    print(
        f"Copying body starting tag and header from {input_file.name} to all html files in {parent_dir.name}\n"
    )
    return input_file, parent_dir


def read_body_and_header(file: Path) -> str:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    start, end = read_body_and_header_boundaries(content=content)
    assert start != -1 and end != -1, f"body and/or header not found in file {file}"

    return "\n".join(content.splitlines()[start : end + 1])


def read_body_and_header_boundaries(
    file: Path | None = None, content: str | None = None
) -> tuple[int, int]:
    if file is None and content is None:
        raise ValueError("Either file or content must be provided")

    if content is None and file is not None:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

    assert content is not None, "content must be provided"

    start, end = -1, -1
    for i, line in enumerate(content.splitlines()):
        if "<body" in line:
            start = i
        if "</header>" in line:
            end = i
            break
    assert start != -1 and end != -1, f"body and/or header not found in file {file}"
    return start, end


def replace_body_and_header(target_files: list[Path], body_and_header: str):
    for target_file in target_files:
        with open(target_file, "r", encoding="utf-8") as f:
            content = f.read()

        start, end = read_body_and_header_boundaries(content=content)
        assert start != -1 and end != -1, (
            f"body and/or header not found in file {target_file}"
        )

        new_content = (
            "\n".join(content.splitlines()[:start])
            + "\n"
            + body_and_header
            + "\n"
            + "\n".join(content.splitlines()[end + 1 :])
        )
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {target_file.name}")


if __name__ == "__main__":
    main()
