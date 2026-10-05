# LeetCode Render 数据恢复

更新日期：2026-10-03

## 结论

LeetCode 的运行数据已经单独放在 `leetcode/` 项目里：

- SQLite：`leetcode/backend/leetcode.db`
- 笔记截图：`leetcode/backend/note_images/`

从 Render 拉最新数据时，如果还在 Life OS 仓库里，可以先跑总备份，再只恢复
LeetCode 这一块：

```bash
scripts/backup_render_data.sh
scripts/restore_leetcode_render_data.sh
```

在这个独立 LeetCode 目录里，如果已经有 `~/LifeOS-render-backups/latest.tar.gz`，
直接运行：

```bash
scripts/restore-render-data.sh
```

如果要从某个指定备份恢复：

```bash
scripts/restore-render-data.sh ~/LifeOS-render-backups/lifeos-render-YYYYMMDD-HHMMSS.tar.gz
```

## 冲突规则

Render 是权威来源：

- `leetcode.db` 直接用 Render 备份覆盖本地库。
- 截图文件同名冲突时，用 Render 文件覆盖本地文件。
- 本地独有截图会保留，因为旧笔记里可能还引用这些文件；脚本会先把恢复前的本地
  DB 和截图备份到 `leetcode/backend/render-restore-backups/<timestamp>/`。

## 备份包里的路径

当前 Render 总备份里，LeetCode DB 在：

```text
data/leetcode/leetcode.db
```

截图历史上在 Life OS 共享目录：

```text
data/note_images/
```

新的备份脚本也兼容专属路径：

```text
data/leetcode/note_images/
```
