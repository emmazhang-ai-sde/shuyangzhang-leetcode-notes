# CLAUDE.md

给 Claude Code 用的项目说明。

## 项目概况

刷题相关的一切：题目动画、题解答案、lecture notes、fill-in 练习、
standard-answers 标准答案，加一套长在动画站里的 LC Notes 笔记系统（打卡 + 笔记 +
星标 + 表达库）。2026-08-10 从 `shuyangzhang-life-summary`（Life OS）拆出来，
独立仓库、独立后端、独立数据库。

## 常用命令

```bash
# 首次
python3 -m venv ~/.venvs/leetcode-app
~/.venvs/leetcode-app/bin/pip install -r requirements.txt

./run.sh   # 启动，打开 http://127.0.0.1:8789
```

没有测试/lint/构建步骤，验证方式是启动后在浏览器里实际点。

## 架构

单进程 FastAPI：`backend/main.py` 挂 `/api/leetcode/*` 若干接口 + 把
`leetcode/` 整个目录原样发布在根路径下（`backend/main.py` 的
`app.mount("/", ...)`）。数据存 `backend/leetcode.db`（gitignored），
截图存 `backend/note_images/`（gitignored）。

`leetcode/` 内部结构、共享 CSS 分层、notes.js 四种页面形态等，见
`leetcode/leetcode-all-in-one/ARCHITECTURE.md`——改动画站/笔记系统之前先读。
做新动画页必读 `ANIMATION_GUIDE.md`（硬性规则：紫色行高亮必须逐行走不许跳）。

题目答案的权威是 `leetcode/standard-answers/`（标准答案，保持原样不改动）；
本地私人补充答案可放 `leetcode/user-answers/`（平铺，按题号或题名 slug
命名），但这个目录不属于 template 结构。后端按题号/slug 现扫答案目录
（标准答案优先），不再单独复制一份。`standard-answers` 目录名写死在
`backend/main.py` 顶部的 `STANDARD_ANSWERS_DIR`，改名目录必须同步改常量。
`leetcode/leetcode-all-in-one/catalog.js` 是题目目录的唯一权威（加题/上架
动画都只改它）。`2-leetcode-speak`、`3-leetcode-lecture-notes`、
`4-leetcode-fill-in`、`0-oa-real-problems` 属于本地私人资料，导出的
template 不包含它们。

## 跟 Life OS 的关系

LeetCode 的 API、SQLite 数据库和笔记截图都归这个子项目自己管理。Life OS 只在
sidebar 放一个新标签页入口；本地开发时根目录 `./run.sh` 会把它作为 companion
service 跑在 `8789`，云端部署时 Life OS 会把这个 FastAPI app 挂进同一个 Render
服务。

本地要以 Render 为准恢复 LeetCode 数据时，如果已有
`~/LifeOS-render-backups/latest.tar.gz`，在本目录运行
`scripts/restore-render-data.sh`。恢复规则见 `docs/RENDER_DATA.md`。
