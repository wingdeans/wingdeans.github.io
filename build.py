import shutil
import subprocess
from glob import glob
from pathlib import Path

d = Path(__file__).parent.absolute()
template = (d / "src/template.html").read_text()

def outdated(src, dst):
    try:
        dtime = Path(dst).stat().st_mtime
    except OSError:
        return True
    return dtime < Path(src).stat().st_mtime

for src in d.glob("src/*.frag.html"):
    dst = d / "docs" / (src.name.removesuffix(".frag.html") + ".html")
    dst.write_text(template.format(fragment=src.read_text()))

for src in d.glob("src/*.typ"):
    dst = d / "docs" / Path(src.name).with_suffix(".html")
    html = subprocess.run(
        [
            "typst", "compile",
            "--features=html", "--format=html",
            src, "-"
        ],
        stdout=subprocess.PIPE,
        encoding="utf-8"
    ).stdout
    html = html[html.index("<body>")+6 : html.rindex("</body>")]
    dst.write_text(template.format(fragment=html))
