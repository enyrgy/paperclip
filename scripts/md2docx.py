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
        python3 scripts/md2docx.py --check-only --strict <file.md>   # exit 1 on findings
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


# -------------------------------------------------------------- brand style
# Every Enyrgy .docx is built against the brand reference document: Montserrat
# throughout, headings in Sunrise Orange #E64C38, Deep Charcoal body text, and
# the ENYRGY header / Sunlight. Evolved. footer. Without it pandoc emits Aptos
# and no header, which is not the approved standard.
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REFERENCE = os.path.join(REPO, "assets", "enyrgy-reference.docx")

# The reference document's header carries its own title and version, so both
# are rewritten per document at build time.
TITLES = {
    "Enyrgy_GHL_Implementation_Guide_v3_9": "Implementation Guide",
    "Enyrgy_Enterprise_Architecture_v1_0": "Enterprise Architecture",
    "Enyrgy_Paperclip_Knowledge_Base": "Knowledge Base",
    "Enyrgy_Brand_Style_Guide_v2": "Brand Style Guide",
    "Enyrgy_Agent_Email_Templates_v1": "Agent Email Templates",
    "Enyrgy_Funnel_Ownership_Map": "Funnel Ownership Map",
    "Enyrgy_Master_TODO": "Master TODO",
    "Enyrgy_Session_Handoff": "Session Handoff",
    "Enyrgy_Facility_Overview": "Facility Overview",
    "Enyrgy_Story_and_Clinical_Data": "Story and Clinical Data",
    "Enyrgy_Letter_ZENA_Medical": "Letter of Introduction",
}
# Versions are explicit, not sniffed. Auto-detection read the Knowledge Base's
# opening reference to "Implementation Guide v3.9" as the KB's own version.
# UPDATE THESE when a document's version bumps.
VERSIONS = {
    "Enyrgy_GHL_Implementation_Guide_v3_9": "v3.9.7",
    "Enyrgy_Enterprise_Architecture_v1_0": "v1.2",
    "Enyrgy_Paperclip_Knowledge_Base": "v2",
    "Enyrgy_Brand_Style_Guide_v2": "v2.0",
    "Enyrgy_Facility_Overview": "v2.3",
    "Enyrgy_Story_and_Clinical_Data": "v1.1",
}
VERSION_RE = re.compile(r"\bv(\d+\.\d+(?:\.\d+)?)\b|\bVersion (\d+\.\d+)\b")


def doc_title(md):
    """Header title: the mapping, else the filename humanized."""
    stem = os.path.basename(md)[:-3]
    if stem in TITLES:
        return TITLES[stem]
    return stem.replace("Enyrgy_", "").replace("_", " ")


def doc_version(md):
    """The mapped version. Falls back to sniffing only for unmapped files."""
    stem = os.path.basename(md)[:-3]
    if stem in VERSIONS:
        return VERSIONS[stem]
    with open(md, encoding="utf-8") as fh:
        head = "".join(fh.readline() for _ in range(60))
    m = VERSION_RE.search(head)
    return "v" + (m.group(1) or m.group(2)) if m else ""


def brand_header(path, title, version):
    """Rewrite the reference document's header for this document."""
    zin = zipfile.ZipFile(path)
    parts = {n: zin.read(n) for n in zin.namelist()}
    infos = zin.infolist()
    zin.close()
    name = "word/header1.xml"
    if name not in parts:
        return False
    x = parts[name].decode("utf-8")
    x = re.sub(r'(<w:t[^>]*>)ENYRGY \| [^<]*(</w:t>)',
               lambda m: f"{m.group(1)}ENYRGY | {title} {m.group(2)}", x, count=1)
    x = re.sub(r'(<w:t[^>]*>)v[\d.]+\s*(</w:t>)',
               lambda m: f"{m.group(1)}{version}  {m.group(2)}", x, count=1)
    parts[name] = x.encode("utf-8")
    tmp = path + ".tmp"
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for it in infos:
            zi = zipfile.ZipInfo(it.filename, date_time=it.date_time)
            zi.compress_type = it.compress_type
            zi.external_attr = it.external_attr
            zout.writestr(zi, parts[it.filename])
    os.replace(tmp, path)
    return True


# ------------------------------------------------------------------ driver
def build(md):
    docx = md[:-3] + ".docx"
    cmd = ["pandoc", md, "-o", docx]
    if os.path.exists(REFERENCE):
        cmd[1:1] = ["--reference-doc=" + REFERENCE]
    else:
        print(f"    WARNING: {REFERENCE} missing, building unbranded")
    subprocess.run(cmd, check=True)
    n = gridlines(docx)
    title, version = doc_title(md), doc_version(md)
    hdr = brand_header(docx, title, version)
    print(f"  {os.path.basename(docx):42} tables gridlined: {n}"
          f"  header: {title} {version}" if hdr else
          f"  {os.path.basename(docx):42} tables gridlined: {n}")


def main(argv):
    check_only = "--check-only" in argv
    strict = "--strict" in argv
    files = [a for a in argv if not a.startswith("--")]
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
        print(f"\n  {warnings} style finding(s). See Enyrgy_Brand_Style_Guide_v2.md, "
              f"section 05 Mechanics.")
        if strict:
            print("  Wrap a legitimate quotation in style-check ignore/resume comments,")
            print("  or bypass this once with: git commit --no-verify")
            return 1
        print("  Quoted source material may legitimately trip this. Nothing was blocked.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
