---
description: TASKS.md の残タスクを追加・一覧・完了させる
---

引数: `$ARGUMENTS`

`src/tasks.py` を使って `TASKS.md` を編集する。プロジェクトルートで実行すること。

- 追加: `python3 src/tasks.py add "<タスク内容>"`
- 一覧: `python3 src/tasks.py list`
- 完了: `python3 src/tasks.py done <番号>`（番号は list の番号）

引数が空なら `list` を実行して残タスクを表示する。
引数の先頭が `done` の場合は完了処理、それ以外はタスク追加として扱う。
編集後は `TASKS.md` の差分を確認し、変更点を1行で報告する。
