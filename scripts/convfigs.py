#!/usr/bin/env python
"""
Convert a list of figures from PDF to PNG.

Requires:
* ImageMagick
* Ghostscript
* Wand (`pip install wand`)

Could use straight ImageMagick:

    convert -density 300 -depth 8 -quality 85 $INPUT_FILE $OUTPUT_FILE
"""

from wand.image import Image
import os


def convert(fpath_in, fpath_out):
    with Image(filename=fpath_in, resolution=300) as img:
        img.save(filename=fpath_out)


if __name__ == "__main__":
    cfd_dir = "../../Papers/CFT wake modeling/figures"
    figs = ["kcont_kOmegaSST.pdf",
            "kcont_SpalartAllmaras.pdf",
            "kcont_exp.pdf",
            "meancontquiv_SpalartAllmaras.pdf",
            "meancontquiv_kOmegaSST.pdf",
            "mom_bar_graph.pdf",
            "perf_bar_chart.pdf",
            "verification.pdf",
            "meancontquiv_exp.pdf"]
    figs = [os.path.join(cfd_dir, f) for f in figs]

    for f in figs:
        fout = "br-cfd-"
        fout += os.path.split(f)[-1].replace(".pdf", ".png")
        fout = os.path.join("figures", fout)
        convert(f, fout)
