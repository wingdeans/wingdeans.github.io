import shutil
import subprocess
from glob import glob
from pathlib import Path

d = Path(__file__).parent.absolute()

def outdated(src, dst):
    try:
        dtime = Path(dst).stat().st_mtime
    except OSError:
        return True
    return dtime < Path(src).stat().st_mtime

if outdated(src := d/"src/index.html", dst := d/"docs/index.html"):
    shutil.copyfile(src, dst)

for src in d.glob("src/*.typ"):
    dst = d / "docs" / Path(src.name).with_suffix(".html")
    html = subprocess.run(
        [
            "typst", "compile",
            "--features=html", "--format=html",
            src, "-"
        ],
        capture_output=True
    ).stdout

    with open(dst, "wb") as f:
        f.write(html[html.index(b"<body>")+6 : html.rindex(b"</body>")])
