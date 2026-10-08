# Arjun Study — Codex Working Project

## Current priority
Prepare the current Sunday PABT using only these three chapters until the test-focused pilot is complete:

1. Physics — Gravitation
2. Chemistry — States of Matter
3. Mathematics — Straight Lines

The formula/recall pilot must reduce unnecessary memorisation without reducing exam coverage. Use M/D/R classification:
- M = must memorise as a parent relation/fact
- D = should be derived quickly from a parent relation
- R = recognition/use rule or condition rather than a standalone formula

## Canonical sources

### GitHub repository
`vhd4trade-cell/arjun-study`

Chapter bundles already present:
- `physics/gravitation/`
- `chemistry/states-of-matter/`
- `maths/straight-lines/`

Each chapter normally contains `notes.html`, `revision.html`, and `solutions.html`.

### Google Drive source root
The same Drive folder is synced at different local roots.

Home laptop:
`J:\My Drive\Arjun Study`

Office PC:
`D:\vhd4trd\Arjun Study`

Never hard-code one machine path into project logic. Use `tools/path_config.py` to resolve the active Drive root.

## Recommended local Codex layout
Do not place the Git repository itself inside Google Drive. Keep one local clone on each machine and use GitHub for code/project-state sync.

Recommended clones:

Home:
`C:\Users\Appex\projects\arjun-study`

Office:
`C:\Users\yds_c\projects\arjun-study`

Google Drive is for source books, question banks, exported study artifacts and shared non-Git files. GitHub is for chapter HTML, project instructions and reproducible tooling.

## Start-of-session check
From the repository root run:

```powershell
python tools/path_config.py
```

The command must report the detected Drive root. If neither known root exists, stop and ask for the local synced Drive location rather than inventing a path.

## Current PABT workflow
For each of the three active chapters:

1. Extract every formula/rule currently presented as memorisation-worthy.
2. Group them into formula families.
3. Identify the smallest reliable parent set.
4. Mark each item M, D or R.
5. For every D item, verify that Arjun can derive it correctly in about 20 seconds or less; otherwise promote it to M.
6. Preserve conditions, symbol meanings/pronunciation, units and common traps.
7. Test recall, formula selection and application on chapter questions/PYQs.
8. Record failures and change classification only with evidence.

Do not divert this pilot to Newton's Laws or Trigonometry until the Sunday PABT chapters are complete.
