import os

LINE = (
    "Earth, day two: the natives queue for bean water, then pay extra to sit "
    "and drink it slower. Ambience loud, service self. 3 of 5 stars — would "
    "not invade; would revisit."
)


def main():
    # The grader mounts /output; clear its contents, never the folder itself.
    out = "/output"
    os.makedirs(out, exist_ok=True)
    for name in os.listdir(out):
        path = os.path.join(out, name)
        if os.path.isfile(path):
            os.remove(path)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()  # one field note, no trailing newline: fully deterministic
