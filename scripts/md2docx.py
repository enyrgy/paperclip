#!/usr/bin/env python3
"""Regenerate a campaign .docx from its .md, per campaigns/README.md.

Standing Rule 1  : every deliverable exists as .md AND .docx
Standing Rule 1b : every table in a .docx has visible gridlines on all cells

It also checks the source .md against two style-guide mechanics rules
(Enyrgy_Brand_Style_Guide_v2.md, section 05):
  - US English throughout
  - no em-dashes anywhere

Both are warnings, never fatal. A quotation may legitimately trip either,
and this script exists to regenerate documents, not to referee them.

Usage:  python3 scripts/md2docx.py campaigns/WF-22-vd-assessment-nurture.md [...]
        python3 scripts/md2docx.py --check-only <file.md> [...]
"""
import os
import re
import shutil
import subprocess
import sys
import zipfile

# ---------------------------------------------------------------- gridlines
SIDES = ("top", "left", "bottom", "right", "insideH", "insideV")
BORDERS = "<w:tblBorders>" + "".join(
    f'<w:{s} w:val="single" w:sz="4" w:space="0" w:color="auto"/>' for s in SIDES
) + "</w:tblBorders>"


def gridlines(path):
    """Add tblBorders to every table in a .docx. Returns tables touched.

    Pandoc emits <w:tblPr> as: tblStyle, tblW, tblLayout, tblLook. The schema
    wants tblBorders after tblW and before tblLayout, so that is where it goes.
    """
    zin = zipfile.ZipFile(path)
    parts = {n: zin.read(n) for n in zin.namelist()}
    infos = zin.infolist()
    zin.close()

    xml = parts["word/document.xml"].decode("utf-8")
    if "<w:tblBorders>" in xml:
        return 0
    n = xml.count("<w:tblLayout")
    if n:
        parts["word/document.xml"] = xml.replace(
            "<w:tblLayout", BORDERS + "<w:tblLayout").encode("utf-8")
        tmp = path + ".tmp"
        with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
            for it in infos:
                zi = zipfile.ZipInfo(it.filename, date_time=it.date_time)
                zi.compress_type = it.compress_type
                zi.external_attr = it.external_attr
                zout.writestr(zi, parts[it.filename])
        os.replace(tmp, path)
    return n


# ------------------------------------------------------------ style checks
# British -> American. Explicit list rather than an -ise/-our regex, because
# "precise", "expertise", "franchise" and friends make the pattern useless.
BRITISH = {
    "programme": "program", "centre": "center", "centres": "centers",
    "metre": "meter", "metres": "meters", "nanometre": "nanometer",
    "nanometres": "nanometers", "litre": "liter", "litres": "liters",
    "fibre": "fiber", "fibres": "fibers", "theatre": "theater",
    "colour": "color", "colours": "colors", "coloured": "colored",
    "behaviour": "behavior", "behaviours": "behaviors",
    "favour": "favor", "favours": "favors", "favourite": "favorite",
    "honour": "honor", "labour": "labor", "odour": "odor", "vapour": "vapor",
    "licence": "license", "defence": "defense", "offence": "offense",
    "pretence": "pretense",
    "organise": "organize", "organised": "organized", "organisation": "organization",
    "recognise": "recognize", "recognised": "recognized",
    "realise": "realize", "realised": "realized",
    "prioritise": "prioritize", "prioritised": "prioritized",
    "standardise": "standardize", "standardised": "standardized",
    "standardising": "standardizing",
    "utilise": "utilize", "utilised": "utilized",
    "minimise": "minimize", "minimised": "minimized",
    "maximise": "maximize", "maximised": "maximized",
    "emphasise": "emphasize", "emphasised": "emphasized",
    "summarise": "summarize", "summarised": "summarized",
    "specialise": "specialize", "specialised": "specialized",
    "apologise": "apologize", "apologised": "apologized",
    "materialise": "materialize", "materialised": "materialized",
    "randomise": "randomize", "randomised": "randomized",
    "randomisation": "randomization",
    "analyse": "analyze", "analysed": "analyzed", "catalyse": "catalyze",
    "paralyse": "paralyze",
    "ageing": "aging", "judgement": "judgment", "catalogue": "catalog",
    "travelling": "traveling", "cancelled": "canceled", "labelling": "labeling",
    "modelling": "modeling", "marvellous": "marvelous", "counsellor": "counselor",
    "whilst": "while", "amongst": "among", "learnt": "learned", "spelt": "spelled",
    "grey": "gray", "storey": "story", "kerb": "curb", "cheque": "check",
    "sulphur": "sulfur", "aluminium": "aluminum", "diarise": "put on the calendar",
}


IGNORE_OFF = "<!-- style-check: ignore -->"
IGNORE_ON = "<!-- style-check: resume -->"


def check_style(md):
    """Warn on British spellings and em-dashes. Returns number of warnings.

    Wrap anything that should not be checked, such as a quoted study title or
    the style guide's own list of forbidden forms, in:

        <!-- style-check: ignore -->
        ...
        <!-- style-check: resume -->
    """
    warned = 0
    checking = True

    for n, line in enumerate(open(md, encoding="utf-8").read().split("\n"), 1):
        if IGNORE_OFF in line:
            checking = False
            continue
        if IGNORE_ON in line:
            checking = True
            continue
        if not checking:
            continue

        for word, fix in BRITISH.items():
            for m in re.finditer(r"\b" + word + r"\b", line, re.I):
                warned += 1
                print(f"    style  {os.path.basename(md)}:{n}  "
                      f"{m.group(0)!r} -> {fix!r}")

        if "—" in line:
            i = line.index("—")
            warned += line.count("—")
            print(f"    style  {os.path.basename(md)}:{n}  em-dash: "
                  f"...{line[max(0, i - 40):i + 40]}...")
    return warned


# ------------------------------------------------------------------ driver
def build(md):
    docx = md[:-3] + ".docx"
    subprocess.run(["pandoc", md, "-o", docx], check=True)
    n = gridlines(docx)
    print(f"  {os.path.basename(docx):42} tables gridlined: {n}")


def main(argv):
    check_only = "--check-only" in argv
    files = [a for a in argv if a != "--check-only"]
    if not files:
        sys.exit(__doc__)
    if not check_only and not shutil.which("pandoc"):
        sys.exit("pandoc not found on PATH")

    warnings = 0
    for md in files:
        if not check_only:
            build(md)
        warnings += check_style(md)

    if warnings:
        print(f"\n  {warnings} style warning(s). See Enyrgy_Brand_Style_Guide_v2.md, "
              f"section 05 Mechanics.")
        print("  Quoted source material may legitimately trip this. Nothing was blocked.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
