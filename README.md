# Arjun Study — Complete 11th Science Material

Centralized, searchable study resource for 11th Science (Physics, Chemistry, Mathematics, English, Computer).  
**Physics**: NLM, Work-Energy, Collision, Periodicity  
**Chemistry**: Bonding, Periodicity, Organic, Kinetics  
**Maths**: Quadratic Equations, Trigonometry, Basic Calculus, Straight Lines  
**English & Computer**: Added as chapters complete  

---

## Repository Structure

```
arjun-study/
├── index.html              (Master landing page)
├── README.md              (This file)
├── assets/
│   ├── style.css          (Shared styling)
│   └── logo.png           (Branding)
│
├── physics/
│   ├── index.html         (Physics hub)
│   ├── nlm/
│   │   ├── notes.html
│   │   ├── revision.html
│   │   └── solutions.html
│   └── collision/
│       ├── notes.html
│       ├── revision.html
│       └── solutions.html
│
├── chemistry/
│   ├── index.html
│   └── [chapters...]
│
├── maths/
│   ├── index.html         (Maths hub)
│   ├── quadratic/
│   │   ├── notes.html
│   │   ├── revision.html
│   │   └── solutions.html
│   ├── trigonometry/
│   ├── calculus/
│   └── straight-lines/
│       ├── notes.html
│       ├── revision.html
│       └── solutions.html
│
└── english/
    ├── index.html
    └── [chapters...]
```

---

## File Naming Convention

**All chapters follow same pattern:**

- `{chapter}/notes.html` — Full chapter notes (formulas, diagrams, examples)
- `{chapter}/revision.html` — One-page quick reference  
- `{chapter}/solutions.html` — Question bank with worked solutions

**Linking across chapters:**
```html
<!-- From solutions → notes (automatic, same folder) -->
<a href="notes.html#p05" target="chapterNotes">↗</a>

<!-- From one chapter to another (cross-chapter) -->
<a href="../../physics/nlm/notes.html#p03">Related concept</a>
```

---

## Workflow: Adding New Chapter

### 1. **Build the chapter** (locally in `_build/`)
```bash
cd "School - Grade 11/Maths/_build/new-chapter"
python notes.py "../../Chapter Notes/New Chapter.html"
python revision.py "../../Revision Sheets/New Chapter - Revision.html"
python make_qb.py "../../Question Banks/New Chapter - Solutions.html"
```

### 2. **Copy to repo**
```bash
# From Drive → GitHub folder
cp "Maths/Chapter Notes/New Chapter.html" arjun-study/maths/new-chapter/notes.html
cp "Maths/Revision Sheets/..." arjun-study/maths/new-chapter/revision.html
cp "Maths/Question Banks/..." arjun-study/maths/new-chapter/solutions.html
```

### 3. **Update hub index**
Edit `arjun-study/maths/index.html` to add new chapter card:
```html
<a href="new-chapter/notes.html" class="card">
  <h3>📖 New Chapter</h3>
  <p>Full notes, revision sheet, 107 solutions</p>
</a>
```

### 4. **Commit & push**
```bash
git add .
git commit -m "Add: Maths - New Chapter"
git push origin main
```

**Site updates automatically** (GitHub Pages rebuilds in ~1 min)

---

## Master Index Structure

**Main landing:** `index.html`
- 5 subject cards (Physics, Chemistry, Maths, English, Computer)
- Latest updates feed
- Search/browse by subject

**Subject hub:** `maths/index.html`
- List of all chapters in Maths
- Filter by document type (Notes/Revision/Solutions)
- Quick links to popular chapters

**Chapter:** `maths/straight-lines/notes.html`
- Full content with diagrams
- ↗ links between notes ↔ solutions
- Breadcrumb: Maths > Straight Lines > Chapter Notes

---

## Cross-Chapter Linking

**Problem:** "See also: Similar concept in Trigonometry Part 05"

**Solution (in notes.html):**
```html
<p>See also: <a href="../../trigonometry/notes.html#p05" 
   target="trigNotes">Trigonometry Part 05</a></p>
```

When Arjun clicks → opens Trigonometry in new tab at exact section

---

## GitHub Pages Setup

1. Create repo: `https://github.com/YOUR-USERNAME/arjun-study`
2. Push files (structure above)
3. Settings → Pages → Deploy from `main` branch
4. Live at: `https://YOUR-USERNAME.github.io/arjun-study/`

**Share with Arjun:**
- Main URL: `https://your-username.github.io/arjun-study/`
- Subject URLs: `.../arjun-study/maths/` or `.../arjun-study/physics/`
- Chapter URLs: `.../arjun-study/maths/straight-lines/`

---

## Maintenance

**Updating a chapter:**
```bash
# Edit notes.py in _build/
# Rebuild
python notes.py output.html

# Copy to repo
cp output.html arjun-study/maths/straight-lines/notes.html

# Commit
git add -A
git commit -m "Update: Maths - Straight Lines - Add Part 12"
git push
```

**Site reflects changes in ~1 minute automatically**

---

## Future: Metadata & Search

When you have 20+ chapters, add `chapters.json`:
```json
{
  "maths": [
    {"title": "Straight Lines", "parts": 11, "questions": 107, "updated": "2026-10-07"},
    {"title": "Quadratic Equations", "parts": 8, "questions": 95, "updated": "2026-09-20"}
  ]
}
```

Then update master `index.html` to read JSON and auto-populate chapters.

---

## Current Materials Ready to Push

✅ **Maths:**
- Quadratic Equations (notes, revision, solutions)
- Trigonometry (notes, revision, solutions)
- Basic Calculus (notes, revision, solutions)
- Straight Lines (notes, revision, solutions) — **FULLY REDESIGNED**

✅ **Physics:**
- NLM (notes, solutions)
- Work-Energy (notes, solutions)
- Collision (notes, solutions)

**Next:** Create repo structure, organize & push existing materials, set up hubs.

