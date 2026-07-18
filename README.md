# 草津温泉 1泊2日 旅のしおり

Version: 1.0.3

2026年7月18日(土)〜19日(日) の草津温泉旅行を友人グループで共有するためのしおり一式。

## 中身

- `index.html` — スマホで見る旅のしおり本体（ブラウザで開く／GitHub Pages公開対象）。
- `others/maps/*.kml` — Googleマイマップに読み込む散策ルート。
- `others/草津_グルメ重視_予定_LINE用.txt` — LINEで共有する用の予定テキスト。
- `src/*.py` — KML・テキストを生成するスクリプト。
- `prompts/design-prompt.txt` — しおりの元になった企画・掲載情報。

## 使い方

しおりを見る:

```
open index.html
```

KMLを再生成する（プロジェクトルートで実行）:

```
python3 src/gen_split.py     # 1日目/2日目に分けたグルメルート
python3 src/gen_kml.py       # 街歩き・グルメの各ルート
```

Googleマイマップに `others/maps/` のKMLをインポートすると地図で確認できる。

## ドキュメント

- プロジェクトの目的・デザイン方針: [CLAUDE.md](./CLAUDE.md)
- 残タスク・進捗: [TASKS.md](./TASKS.md)
