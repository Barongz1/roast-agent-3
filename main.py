"""Roast Your Own Agent — entry for make.fun.

Writes one line to /output/entry.txt.
The line is a single roast of our own AI agent, at most 200 characters, and nothing else.
"""
import os

LINE = "Our agent finished the task in record time, then quietly billed us for the three hours it spent congratulating itself."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
