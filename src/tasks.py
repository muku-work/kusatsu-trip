#!/usr/bin/env python3
"""TASKS.md を編集するハーネス。

作業が追加になったら残タスクへ1行追記し、完了したらチェックを付けて
「完了」セクションへ移動する。TASKS.md のフォーマット
（`## 残タスク` / `## 完了` の下に `- [ ]` / `- [x]` が並ぶ）を前提とする。

使い方（プロジェクトルートから実行）:
    python3 src/tasks.py add "公開URLをLINEで共有"     # 残タスクに追記
    python3 src/tasks.py list                           # 残タスクを番号付きで表示
    python3 src/tasks.py done 2                          # 残タスク2番目を完了に移動
"""
import sys
from pathlib import Path

TASKS = Path(__file__).resolve().parent.parent / "TASKS.md"
TODO_H = "## 残タスク"
DONE_H = "## 完了"


def read():
    return TASKS.read_text(encoding="utf-8").splitlines()


def write(lines):
    TASKS.write_text("\n".join(lines) + "\n", encoding="utf-8")


def section_bounds(lines, header):
    """header 直下からセクション末尾（次の `## ` 直前）までの行indexリストを返す。"""
    start = next(i for i, l in enumerate(lines) if l.strip() == header)
    end = len(lines)
    for i in range(start + 1, len(lines)):
        if lines[i].startswith("## "):
            end = i
            break
    return start, end


def todo_items(lines):
    s, e = section_bounds(lines, TODO_H)
    return [(i, lines[i]) for i in range(s + 1, e) if lines[i].lstrip().startswith("- [ ]")]


def cmd_add(text):
    lines = read()
    s, e = section_bounds(lines, TODO_H)
    # セクション内の最後の箇条書きの直後に挿入（無ければ見出し直後）
    insert = s + 1
    for i in range(s + 1, e):
        if lines[i].lstrip().startswith("- ["):
            insert = i + 1
    lines.insert(insert, f"- [ ] {text}")
    write(lines)
    print(f"追加: {text}")


def cmd_list():
    for n, (_, line) in enumerate(todo_items(read()), 1):
        print(f"{n}. {line.split('- [ ]',1)[1].strip()}")


def cmd_done(num):
    lines = read()
    items = todo_items(lines)
    if not (1 <= num <= len(items)):
        sys.exit(f"番号は 1〜{len(items)} で指定してください")
    idx, line = items[num - 1]
    text = line.split("- [ ]", 1)[1].strip()
    del lines[idx]
    ds, _ = section_bounds(lines, DONE_H)
    pos = ds + 1
    if pos < len(lines) and lines[pos].strip() == "":  # 見出し直後の空行を保つ
        pos += 1
    lines.insert(pos, f"- [x] {text}")
    write(lines)
    print(f"完了に移動: {text}")


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    cmd = sys.argv[1]
    if cmd == "add" and len(sys.argv) >= 3:
        cmd_add(" ".join(sys.argv[2:]))
    elif cmd == "list":
        cmd_list()
    elif cmd == "done" and len(sys.argv) == 3 and sys.argv[2].isdigit():
        cmd_done(int(sys.argv[2]))
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
