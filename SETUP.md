# GitHub Pages Setup — Complete System

**One-time setup: 15 minutes**  
**Then:** Auto-updates every time you add a new chapter

---

## Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. **Repository name:** `arjun-study` (or `my-study-materials`, etc.)
3. **Description:** "11th Science study material — Physics, Chemistry, Maths"
4. **Public** (so Arjun can access without login)
5. Create repository

---

## Step 2: Clone & Organize Files

```bash
# Clone the repo locally
git clone https://github.com/YOUR-USERNAME/arjun-study.git
cd arjun-study

# Create folder structure
mkdir -p physics chemistry maths english computer
mkdir -p maths/quadratic maths/trigonometry maths/calculus maths/straight-lines
mkdir -p physics/nlm physics/work-energy physics/collision
mkdir -p chemistry/bonding chemistry/periodicity

# Copy index files (already prepared)
cp /path/to/temp/arjun-study-github/*.html .
cp /path/to/temp/arjun-study-github/*.md .
cp /path/to/temp/arjun-study-github/maths/index.html maths/
```

---

## Step 3: Add Existing Chapters

**From your Drive folder → GitHub folder**

### Mathematics Chapters

```bash
# Quadratic Equations
cp "J:/My Drive/Arjun Study/School - Grade 11/Maths/Chapter Notes/Quadratic Equations.html" arjun-study/maths/quadratic/notes.html
cp "J:/My Drive/Arjun Study/School - Grade 11/Maths/Revision Sheets/Quadratic Equations - Revision Sheet.html" arjun-study/maths/quadratic/revision.html
cp "J:/My Drive/Arjun Study/School - Grade 11/Maths/Practice and Answer Keys/Quadratic Equations PYQ Solutions.html" arjun-study/maths/quadratic/solutions.html

# Trigonometry
cp "J:/My Drive/Arjun Study/School - Grade 11/Maths/Chapter Notes/Trigonometry.html" arjun-study/maths/trigonometry/notes.html
# ... etc
```

### Physics Chapters

```bash
# Copy from Build folder
cp "J:/My Drive/Arjun Study/School - Grade 11/Physics/_build/.../notes.html" arjun-study/physics/nlm/notes.html
cp "J:/My Drive/Arjun Study/School - Grade 11/Physics/_build/.../revision.html" arjun-study/physics/nlm/revision.html
cp "J:/My Drive/Arjun Study/School - Grade 11/Physics/_build/.../solutions.html" arjun-study/physics/nlm/solutions.html
```

---

## Step 4: Update Hub Index Pages

Edit `maths/index.html` — update the chapters list:

```html
<!-- Already has: Quadratic, Trigonometry, Calculus, Straight Lines -->
<!-- For each new chapter, add: -->
<a href="chapter-name/" class="chapter">
    <h2>📖 Chapter Title</h2>
    <div class="chapter-meta">
        <div>X parts • Y questions</div>
        <div class="chapter-docs">
            <a href="chapter-name/notes.html" class="doc-link">📝 Notes</a>
            <a href="chapter-name/revision.html" class="doc-link">⚡ Revision</a>
            <a href="chapter-name/solutions.html" class="doc-link">✅ Solutions</a>
        </div>
    </div>
</a>
```

Similarly update `physics/index.html`, `chemistry/index.html`, etc.

---

## Step 5: Push to GitHub

```bash
cd arjun-study

# First time push
git add .
git commit -m "Initial commit: Add all chapters (Maths, Physics, Chemistry)"
git push -u origin main

# Test that it works (wait ~1-2 minutes)
```

---

## Step 6: Enable GitHub Pages

1. Go to repository Settings (top menu)
2. Scroll to **Pages** section
3. **Source:** Select `main` branch, `/` (root folder)
4. Click Save
5. Wait 1-2 minutes for site to build

**Your site is now live at:**
```
https://YOUR-USERNAME.github.io/arjun-study/
```

---

## Share With Arjun

**Main landing page:**
```
https://your-username.github.io/arjun-study/
```

**Direct to Maths:**
```
https://your-username.github.io/arjun-study/maths/
```

**Direct to Straight Lines solutions:**
```
https://your-username.github.io/arjun-study/maths/straight-lines/solutions.html
```

✅ All internal links work  
✅ No login needed  
✅ Read-only (can't modify unless he has GitHub access)  
✅ Works on mobile, tablet, desktop  

---

## Workflow: Add New Chapter

### Every time you finish a new chapter:

1. **Build locally** (in `_build/chapter-name/`):
   ```bash
   python notes.py "../../Chapter Notes/Chapter Name.html"
   python revision.py "../../Revision Sheets/Chapter Name - Revision.html"
   python make_qb.py "../../Question Banks/Chapter Name - Solutions.html"
   ```

2. **Copy to repo:**
   ```bash
   cp output.html /path/to/arjun-study/subject/chapter/notes.html
   cp output-rev.html /path/to/arjun-study/subject/chapter/revision.html
   cp output-qb.html /path/to/arjun-study/subject/chapter/solutions.html
   ```

3. **Update hub index** (`subject/index.html`):
   - Add new chapter card with parts + questions count

4. **Update main index** (`index.html`):
   - Update "Latest Updates" section
   - Update chapter counts in subject cards

5. **Commit & push:**
   ```bash
   git add -A
   git commit -m "Add: [Subject] - [Chapter Name]"
   git push
   ```

**Site auto-updates in ~1-2 minutes. Arjun sees new chapter immediately.**

---

## Example: Adding "Limits & Continuity" to Maths

**1. Build (local)**
```bash
cd "School - Grade 11/Maths/_build/limits"
python notes.py "../../Chapter Notes/Limits & Continuity.html"
python revision.py "../../Revision Sheets/Limits & Continuity - Revision.html"
python make_qb.py "../../Question Banks/Limits & Continuity - Solutions.html"
```

**2. Copy to repo**
```bash
mkdir arjun-study/maths/limits
cp output.html arjun-study/maths/limits/notes.html
cp output-rev.html arjun-study/maths/limits/revision.html
cp output-qb.html arjun-study/maths/limits/solutions.html
```

**3. Update `arjun-study/maths/index.html`** — add new chapter card

**4. Push**
```bash
git add -A
git commit -m "Add: Maths - Limits & Continuity"
git push
```

**Done!** Arjun sees it at: `https://username.github.io/arjun-study/maths/limits/`

---

## Maintenance

**If you update a chapter:**
```bash
# Rebuild locally
python notes.py output.html

# Copy updated file
cp output.html arjun-study/maths/straight-lines/notes.html

# Commit & push
git add maths/straight-lines/notes.html
git commit -m "Update: Maths - Straight Lines - Add Part 12 diagrams"
git push
```

Site reflects changes in ~1 minute.

---

## Future: Advanced Features

**Once you have 15+ chapters, consider adding:**

1. **Search functionality** — Add a `chapters.json` file
2. **Cross-chapter links** — Reference physics concepts in maths
3. **Progress tracker** — Show which chapters Arjun has studied
4. **Mobile app** — Convert to PWA (Progressive Web App)
5. **Question bank index** — Searchable by topic/difficulty

---

## Troubleshooting

**Links not working?**
- Check file paths are correct (case-sensitive on GitHub)
- Ensure `.html` extensions included
- Wait 2-3 minutes after pushing

**Site not updating after push?**
- Go to Settings > Pages — check Status
- Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)

**Want to add custom domain?**
- See GitHub Pages documentation
- Example: `arjunstudy.com` instead of `username.github.io/arjun-study/`

---

## File Locations (Copy From)

```
J:\My Drive\Arjun Study\
├── School - Grade 11\
│   ├── Maths\
│   │   ├── Chapter Notes\
│   │   ├── Revision Sheets\
│   │   └── Practice and Answer Keys\
│   ├── Physics\
│   └── Chemistry\
```

All files ready to copy into GitHub repo structure.

---

**Setup complete!** 🎉

Questions? See README.md in the repo.
