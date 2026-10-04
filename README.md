# LeetCode

A local-first LeetCode study workspace for animated explanations, check-ins, LC Notes, starred problems, struggle markers, expression banks, lecture notes, and OA problem records.

## Run

```bash
python3 -m venv ~/.venvs/leetcode-app
~/.venvs/leetcode-app/bin/pip install -r requirements.txt
./run.sh
```

Open <http://127.0.0.1:8789>.

## Tech Stack

| Layer | Stack | Purpose |
| --- | --- | --- |
| Backend | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python" width="18" /> Python, <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" alt="FastAPI" width="18" /> FastAPI, Uvicorn | Local API, static file serving, and development reloads |
| Database | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" alt="SQLite" width="18" /> SQLite | Check-ins, notes, starred problems, expression banks, and solution versions |
| Frontend | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" alt="HTML5" width="18" /> HTML, <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" alt="CSS3" width="18" /> CSS, <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" alt="JavaScript" width="18" /> JavaScript | Animated problem pages, notes, check-ins, and category views |
| Tooling | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg" alt="Node.js" width="18" /> Node.js, node-html-parser | Index and bundle generation for fill-in practice pages |

## Project Structure

```text
.
├── backend/
│   ├── main.py                 # FastAPI app: API + static file entry points
│   ├── db.py                   # SQLite schema / migration / data access
│   ├── leetcode.db             # Local database
│   └── note_images/            # Note image assets
├── leetcode/
│   ├── 0-oa-real-problems/     # Real OA problem records
│   ├── 3-leetcode-lecture-notes/
│   │                           # Lecture notes, study plans, and chapter notes
│   ├── 4-leetcode-fill-in/     # Fill-in practice project and generation scripts
│   ├── leetcode-all-in-one/    # Animated explanations, LC Notes, and check-ins
│   ├── standard-answers/       # Standard answers
│   └── user-answers/           # Personal answer copies
├── docs/
│   └── RENDER_DATA.md          # Data restore / backup notes
├── render-backups/             # Backup notes
├── requirements.txt            # Python dependencies
└── run.sh                      # Local development startup script
```

For structure details, shared CSS layers, and `notes.js` page patterns, see `leetcode/leetcode-all-in-one/ARCHITECTURE.md`.

## Features

- **Animated explanations:** visual problem pages organized by problem and topic in `leetcode/leetcode-all-in-one/`.
- **LC Notes:** line-linked note cards, custom blocks, chapter/category notes, and image uploads.
- **Check-ins:** problem, timestamp, score, mode, source, review notes, and code snapshots.
- **Problem management:** starred problems, struggle markers, and deletion of a problem with its check-in history.
- **Solution versions:** standard answers plus multiple personal code versions per problem.
- **Expression bank:** scoped phrases, explanation templates, and review wording.
- **Fill-in practice:** chapter index generation and fill-in training materials in `leetcode/4-leetcode-fill-in/`.

## API

| Method | Path | Description |
| --- | --- | --- |
| GET / POST | `/api/leetcode/checkins` | Read / create check-in records |
| PUT | `/api/leetcode/checkins/{cid}` | Update one check-in record |
| DELETE | `/api/leetcode/items/{name}` | Delete a problem and its check-in history |
| GET / PUT | `/api/leetcode/class-links`,<br>`/api/leetcode/class-links/{day}` | Class recording links |
| GET | `/api/leetcode/notes/{name}` | Problem notes, blocks, solutions, and standard answers |
| PUT / DELETE | `/api/leetcode/notes/card`,<br>`/api/leetcode/notes/card/{id}` | Line-linked note cards |
| PUT / DELETE | `/api/leetcode/notes/block`,<br>`/api/leetcode/notes/block/{id}` | Custom note blocks |
| GET / PUT | `/api/leetcode/notes-scope/{scope_key}` | Global / chapter / category notes |
| GET / POST / DELETE | `/api/leetcode/expressions` | Expression bank |
| PUT / DELETE | `/api/leetcode/notes/solution-version`,<br>`/api/leetcode/notes/solution-version/{version_id}` | Solution version copies |
| GET / PUT / DELETE | `/api/leetcode/stars`,<br>`/api/leetcode/stars/{name}` | Starred problem markers |
| GET / PUT / DELETE | `/api/leetcode/struggles`,<br>`/api/leetcode/struggles/{name}` | Struggle markers |
| POST / GET | `/api/leetcode/note-image`,<br>`/api/leetcode/note-image/{fn}` | Upload / read note images |
| GET | `/leetcode-notes/{num}` | Notes page entry for problems without animation pages |

## Attribution

Tech stack icon references are adapted from [Tech Stack Icons - Design Stack Icons (Community)](https://www.figma.com/design/shb7scW12bbgrJSbmnMTq1/Tech-Stack-Icons---Design-Stack-Icons--Community-?node-id=0-1&p=f&t=YPFJ0SuicB8Zy36W-0), a Figma Community file licensed under CC BY 4.0. README icon assets are rendered with [Devicon](https://github.com/devicons/devicon).
