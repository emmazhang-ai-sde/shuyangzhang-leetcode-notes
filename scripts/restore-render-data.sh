#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BACKUP="${1:-${LIFEOS_RENDER_BACKUP:-$HOME/LifeOS-render-backups/latest.tar.gz}}"
STAMP="$(date +"%Y%m%d-%H%M%S")"
WORK="${TMPDIR:-/tmp}/leetcode-render-restore-$STAMP"

LOCAL_DB="$ROOT/backend/leetcode.db"
LOCAL_IMAGES="$ROOT/backend/note_images"
LOCAL_BACKUP_DIR="$ROOT/backend/render-restore-backups/$STAMP"

if [ ! -f "$BACKUP" ]; then
  echo "Backup not found: $BACKUP" >&2
  exit 1
fi

mkdir -p "$WORK" "$LOCAL_BACKUP_DIR"
tar -xzf "$BACKUP" -C "$WORK" data/leetcode/leetcode.db

if [ -f "$LOCAL_DB" ]; then
  cp -p "$LOCAL_DB" "$LOCAL_BACKUP_DIR/leetcode.db"
fi

if [ -d "$LOCAL_IMAGES" ]; then
  mkdir -p "$LOCAL_BACKUP_DIR/note_images"
  find "$LOCAL_IMAGES" -maxdepth 1 -type f ! -name '._*' -exec cp -p {} "$LOCAL_BACKUP_DIR/note_images/" \;
else
  mkdir -p "$LOCAL_IMAGES"
fi

cp -p "$WORK/data/leetcode/leetcode.db" "$LOCAL_DB"

if tar -tzf "$BACKUP" data/leetcode/note_images >/dev/null 2>&1; then
  tar -xzf "$BACKUP" -C "$WORK" data/leetcode/note_images
  find "$WORK/data/leetcode/note_images" -maxdepth 1 -type f ! -name '._*' -exec cp -p {} "$LOCAL_IMAGES/" \;
elif tar -tzf "$BACKUP" data/note_images >/dev/null 2>&1; then
  tar -xzf "$BACKUP" -C "$WORK" data/note_images
  find "$WORK/data/note_images" -maxdepth 1 -type f ! -name '._*' -exec cp -p {} "$LOCAL_IMAGES/" \;
fi

echo "Restored LeetCode data from: $BACKUP"
echo "Local backup saved at: $LOCAL_BACKUP_DIR"
sqlite3 "$LOCAL_DB" \
  "select 'checkins', count(*) from lc_checkins union all
   select 'cards', count(*) from lc_note_cards union all
   select 'versions', count(*) from lc_solution_versions;"
