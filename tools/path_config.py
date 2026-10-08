from pathlib import Path

CANDIDATES = [
    Path(r"J:\My Drive\Arjun Study"),   # home laptop
    Path(r"D:\vhd4trd\Arjun Study"),    # office PC
]


def detect_arjun_study_root() -> Path:
    for path in CANDIDATES:
        if path.exists():
            return path
    raise FileNotFoundError(
        "Arjun Study Google Drive root not found. Checked: "
        + ", ".join(str(p) for p in CANDIDATES)
        + ". Add the current machine's synced path instead of hard-coding a guess."
    )


if __name__ == "__main__":
    root = detect_arjun_study_root()
    print(f"ARJUN_STUDY_ROOT={root}")
