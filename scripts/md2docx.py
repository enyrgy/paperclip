#!/usr/bin/env python3
"""Regenerate a campaign .docx from its .md, per campaigns/README.md.

Standing Rule 1  : every deliverable exists as .md AND .docx
Standing Rule 1b : every table in a .docx has visible gridlines on all cells

Pandoc emits <w:tblPr> as: tblStyle, tblW, tblLayout, tblLook.
The schema requires tblBorders to sit after tblW and before tblLayout,
so the borders block is injected immediately before <w:tblLayout.

Usage:  python3 md2docx.py campaigns/WF-22-vd-assessment-nurture.md [...]
"""
import re, shutil, subprocess, sys, zipfile, os

SIDES = ("top", "left", "bottom", "right", "insideH", "insideV")
BORDERS = "<w:tblBorders>" + "".join(
    f'<w:{s} w:val="single" w:sz="4" w:space="0" w:color="auto"/>' for s in SIDES
) + "</w:tblBorders>"


def gridlines(path):
    """Add tblBorders to every table in a .docx. Returns tables touched."""
    zin = zipfile.ZipFile(path)
    parts = {n: zin.read(n) for n in zin.namelist()}
    infos = zin.infolist()
    zin.close()

    xml = parts["word/document.xml"].decode("utf-8")
    if "<w:tblBorders>" in xml:
        return 0
    n = xml.count("<w:tblLayout")
    if n:
        xml = xml.replace("<w:tblLayout", BORDERS + "<w:tblLayout")
        parts["word/document.xml"] = xml.encode("utf-8")
        tmp = path + ".tmp"
        with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
            for it in infos:
                zi = zipfile.ZipInfo(it.filename, date_time=it.date_time)
                zi.compress_type = it.compress_type
                zi.external_attr = it.external_attr
                zout.writestr(zi, parts[it.filename])
        os.replace(tmp, path)
    return n


def build(md):
    docx = md[:-3] + ".docx"
    subprocess.run(["pandoc", md, "-o", docx], check=True)
    n = gridlines(docx)
    print(f"  {os.path.basename(docx):42} tables gridlined: {n}")


if __name__ == "__main__":
    if not shutil.which("pandoc"):
        sys.exit("pandoc not found on PATH")
    for md in sys.argv[1:]:
        build(md)
