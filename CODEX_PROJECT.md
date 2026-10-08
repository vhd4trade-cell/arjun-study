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

## Working architecture

### Shared Codex workspace — Google Drive synced
The active Codex project state must live in the synced Google Drive so the same workspace is available from both Office and Home.

Office:
`D:\vhd4trd\Arjun Study\_Codex`

Home:
`J:\My Drive\Arjun Study\_Codex`

This `_Codex` folder stores project instructions, current-state notes, analysis outputs, generated study artifacts and reusable scripts that must follow the user between machines.

### Academic source root
Office:
`D:\vhd4trd\Arjun Study`

Home:
`J:\My Drive\Arjun Study`

Never hard-code one machine path into reusable project logic. Detect the active synced root.

### GitHub repository
`vhd4trade-cell/arjun-study`

GitHub remains the canonical version-controlled source for published chapter HTML and reusable repository tooling.

Do not rely on a C: path for continuity. If a machine-local Git clone is used for publishing/version-control operations, treat it as disposable infrastructure and keep shared Codex state in `_Codex` on Google Drive.

## Current chapter bundles
- `physics/gravitation/`
- `chemistry/states-of-matter/`
- `maths/straight-lines/`

Each chapter normally contains `notes.html`, `revision.html`, and `solutions.html`.

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
