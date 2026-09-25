#!/usr/bin/env python3
"""
Journal: a private journal that runs on your own computer.

Run it with:   python server.py      (on Windows you can also use:  py server.py)
Then open:     http://127.0.0.1:8765

Entries are saved as ordinary Markdown files in journal/entries, next to
this script, and attached images are copied into journal/images. Zoom frames you save as
pictures also go there, named like "Zoom 2026-09-22 19.48.05.png".
Each time you draw on a picture, the version from before is kept in
journal/original images, so Restore can step back one version at a time.
An entry can link to another: the link is kept in the text as an ordinary
Markdown link to that entry's file, like [Holiday plans](e1ab2c3d4.md).
Archived entries and pictures are moved to journal/archive; "Delete forever"
erases them. Nothing is sent anywhere: the server only listens on this
computer and needs no internet connection. Stop it with Ctrl+C.

Saving pictures from the web: the journal writes a small browser extension into
journal/browser extension (and a zip of it, for Firefox). In Firefox, open
about:debugging, click "This Firefox", then "Load Temporary Add-on..." and pick
manifest.json in that folder (Firefox forgets it when it closes; to keep it for
good, have the zip signed on addons.mozilla.org, "On your own", and install that).
In Chrome, Edge or Brave: open the extensions page, turn on Developer mode, click
"Load unpacked" and pick the folder. Then right-click any picture on a web page
and choose "Save to journal archive"; it lands in the Archive's Images tab.
In that tab, the + beside Close makes a folder (a real folder inside
journal/archive/images, named however you like). Drag pictures and folders onto
a folder to put them in it, or onto a name in the path above the pictures to
move them back out. Pictures saved from the web always arrive loose in
journal/archive/images itself.
In Firefox this works even when the journal isn't running: each time the journal
starts, it tells Firefox about a small helper (journal/browser helper) that
Firefox runs to put the picture in the archive itself. Chrome-type browsers need
the journal running.
The extension can also save writing: select some text on a web page, right-click
it and choose "Add to quote archive". Each quote is kept as its own text file in
journal/quotes (the page each came from is noted in journal/quotes/.sources.json).
The Quotes menu shows them, lets you add and delete them, and any quote can be
dragged into an entry, where it's kept in a box marked "Quote" that can be dragged
to another place in the entry.

The Menu's "Export as PDF" (at its top) saves the open entry as a PDF in journal/exports,
named by its title: its pictures each on their own, full width; its quotes in their boxes;
and each entry it links to named in small raised capitals after the word, like a footnote
mark, with that entry's own text at the end. The entry itself isn't changed. The PDF is set in Spectral,
kept in journal/fonts (downloaded once from Google Fonts; without it, the computer's serif font).

The Log menu keeps what you do each day: activities, listed by day and numbered
in the order they started, kept in journal/log (their pictures in journal/log/images).
Ctrl+Shift+L logs one (just started, or finished) and Ctrl+Alt+S adds a screenshot
to the activity you started last; both can be changed in the Menu. They work anywhere
on the computer, opening a small window (with a screenshot of what you were doing)
that saves straight into journal/log. On Linux the journal puts them in the desktop's
keyboard shortcuts (Hyprland, GNOME, Ubuntu, Budgie, Cinnamon, MATE, Xfce), so they
work even when the journal isn't running; the window needs tkinter (on Arch or CachyOS:
sudo pacman -S tk; on Ubuntu: sudo apt install python3-tk).
On Windows they work while the journal is running. Anywhere else, give your system
keyboard shortcuts that run "server.py --log" and "server.py --screenshot".

PDFs: drop a PDF onto an entry (or pick one with the attach button, or paste it) and it's
kept in journal/pdfs and put in the writing where it was dropped, as its title in a small
box, kept in the file as an ordinary Markdown link like [Receipt](../pdfs/ab12….pdf).
It moves about like a picture or a linked entry: drag it to another place in the writing,
or into the space on the right to keep it open there, where its pages can be read and
scrolled (in the browser's own PDF reader). Click it, or Open on the right, to read it large;
there its title can be changed, "Open in new tab" gives the browser's full reader (to print
or save a copy), and Delete forever takes it out of the entry and erases the file (unless
another entry still has it). Archiving an entry leaves its PDFs in journal/pdfs, so they
still open from the Archive; deleting the entry forever erases those no other entry uses.
Read (on the right, or "Read as a book" when it's open large) opens a PDF as a book: two pages
side by side on their boards, turned by dragging a page's corner (or by clicking a page, or
with the arrow keys; Home and End go to the start and the end). It opens where you last left
it.
Books: drag a PDF from the writing onto a book model on the right and the two become one book:
the model shows "Read", and reading it takes the book up: it floats from where it is to right in
front of you, turning to show its front cover, and the model's own cover swings open, and the pages
are leafed through to where you left off (and it's the model again whenever the book is closed, at the front or the back). The
boards, the insides of the boards and the page edges are those of the model (its photos, or its
colours), and the pages take the shape of its page block. The PDF's first page is left out (the
model is the book's cover now), and pages are numbered as the PDF numbers them. A book with
endpapers opens at them: the endpaper pasted inside the board, and the free endpaper opposite,
whose plain back comes before the first page (and the same at the end). Closing it (Close, or
Escape) shuts the nearer cover (the front one in the first half of the book, the back one past
the middle) and floats the book back to where it was taken from. Turned back past the
first page, or on past the last, the book closes again. How fast pages and covers turn is set in the Menu (Reading books,
Page turning speed); a click or key press while a page is still going over turns the next one once it lands. The model's Open view can take the PDF
out again (the PDF itself stays where it is). The pages are drawn by pdf.js (from Mozilla, the same that draws PDFs in Firefox), which
the journal downloads once from the npm registry into journal/pdfjs and checks against its
known fingerprint; after that it needs no internet connection.

3D models: drop a binary glTF file (.glb) onto an entry (or pick one with the attach
button) and it's kept in journal/models and shown on the right, where it can be turned
by dragging it, zoomed with Ctrl and the scroll wheel (or a pinch), moved sideways with
Shift held while dragging, and put back as it was with a double-click. Its Open button
shows it large. To move it to another place on the right, drag it by its title.
Closing it takes it off the right; the file stays in journal/models. In the large view, Archive
moves it to the Archive's Models tab (folders can be made there, as for images), and Delete
forever erases it.
Book models: right-click a photo of a book's front cover (in the writing or on the right)
and choose "Make book model", or use the button of that name when the picture is open large.
For the front, spine and back, pick a photo from the entry and drag its four corners onto the
book's corners (Turn moves the edge marked Top). Where a side curves, as the head and tail of a
rounded spine do, drag the small + along it to add a point, and as many more as needed; double-
click a point to take it away. The photo follows the curve. A photo of the page edges can be
added too; it goes on the head, fore-edge and tail. The photo is straightened and
put on the model at full sharpness. Spine and back can be left without a photo, and then
take the colour of the cover. The size starts out as the photos suggest; type it in to
change it. Choose plain, gilt, gilt-top or sprinkled page edges and a rounded or flat spine,
watch the preview, and Make model saves it in journal/models, next to the photo on the right.
Scroll over the photo to zoom in on it (drag the photo to move about; Fit shows it whole again).
Endpapers are as a rebound book has them: pasted inside each board over the turned-in edges of
the covering (which show round them), with a free leaf at the start and the end of the book.
Choose plain, marbled, combed or stone (a made-up sheet, its pattern running on across the fold),
none, or a photo of real endpaper on the Endpaper tab. With a photo of the inside of a board
(the Inside tab), the endpaper is pasted over it, its edges showing round it as the turn-ins. Show open, over the preview, swings the front board
open to see the book lying open at its endpapers. Back cover can be the front's photo, mirrored
across the spine or just as it is, and Inside of the back can be the front board's inside (photo
and endpaper) mirrored or just as it is. More photos can go on the outer edges of the boards (one photo of a stretch of
edge, repeated along all six at its true size, which Edge pattern can make larger or smaller),
and on the headcap and tailcap, which then reach a little way in over the pages.
Paper sets what the pages are printed on as the book is read: white, cream, aged, laid or
handmade, or a photo of real paper chosen on the Paper tab (it's stretched over each page, under
the print, which stays as dark as it is).
Raised bands (1 to 5) can be put across the spine. They start evenly spaced and can be moved,
with their sliders or by dragging them on the spine's photo.
Save draft keeps the book as it is so far in journal/book drafts, shown on the right of the
entry as a "Book draft"; Continue opens it again where it was left, and Make model puts the
finished model in its place (Discard draft throws it away).
"""
import base64
import hashlib
import io
import json
import os
import re
import secrets
import shutil
import struct
import tarfile
import zipfile
import sys
import threading
import time
import webbrowser
import zlib
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote

PORT = 8765
HOST = "127.0.0.1"          # this computer only; never reachable from the network
FOLDER = Path(__file__).resolve().parent / "journal"
ENTRIES = FOLDER / "entries"
ARCHIVE = FOLDER / "archive"
ARCHIVE_ENTRIES = ARCHIVE / "entries"
ARCHIVE_TASKS = ARCHIVE / "tasks.json"   # finished tasks archived from the Tasks menu (they stay in their entries)
ARCHIVE_IMAGES = ARCHIVE / "images"
ARCHIVE_ORIGINALS = ARCHIVE / "original images"
ARCHIVE_MODELS = ARCHIVE / "models"   # 3D models archived from the right of an entry, in folders like the images
EXTENSION = FOLDER / "browser extension"   # the right-click "Save to journal archive" extension
EXTENSION_ZIP = FOLDER / "Save to journal archive.zip"   # the same, packed up for signing on addons.mozilla.org
QUOTES = FOLDER / "quotes"   # quotes saved from web pages, one text file each
MAX_QUOTE = 200_000   # characters
QUOTE_SOURCES = QUOTES / ".sources.json"   # quote file name -> {"url", "title"} of the page it came from
HELPER = FOLDER / "browser helper"   # what Firefox runs to save a picture when the journal isn't running
HELPER_NAME = "journal_archive"
EXTENSION_ID = "save-to-journal-archive@journal.local"
OLD_TRASH = FOLDER / ".trash"   # no longer used; removed at startup
IMAGES = FOLDER / "images"
ORIGINALS = FOLDER / "original images"
LINKS = ORIGINALS / "links.json"   # each drawn-on picture -> the version just before it
IMG_RE = re.compile(r"^[a-f0-9]{32}\.(png|jpg|gif|webp|avif)$")
IMG_TYPES = {"png": "image/png", "jpg": "image/jpeg", "gif": "image/gif", "webp": "image/webp", "avif": "image/avif"}
MAX_IMAGE = 40_000_000
PDFS = FOLDER / "pdfs"   # PDFs put in entries, linked from the writing like [Title](../pdfs/<name>.pdf)
PDF_RE = re.compile(r"^[a-f0-9]{32}\.pdf$")
PDF_IN_BODY_RE = re.compile(r"\]\((?:\.\./)?pdfs/([a-f0-9]{32}\.pdf)\)")
MAX_PDF = 200_000_000
# Shown in place of a PDF whose file has gone from journal/pdfs
MISSING_PDF = ("<!doctype html><meta charset=utf-8><style>html{color-scheme:light dark}body{margin:0;height:100vh;display:flex;"
               "align-items:center;justify-content:center;padding:24px;box-sizing:border-box;font:italic 15px/1.5 Georgia,serif;"
               "color:#6b7370;text-align:center}</style><p>This PDF isn't in journal/pdfs any more.</p>")
PDFJS = FOLDER / "pdfjs"   # pdf.js, which draws the pages when a PDF is read as a book (downloaded once)
PDFJS_VERSION = "5.4.624"
PDFJS_URL = f"https://registry.npmjs.org/pdfjs-dist/-/pdfjs-dist-{PDFJS_VERSION}.tgz"
PDFJS_SHA512 = "sm6TxKTtWv1Oh6n3C6J6a8odejb5uO4A4zo/2dgkHuC0iu8ZMAXOezEODkVaoVp8nX1Xzr+0WxFJJmUr45hQzg=="
PDFJS_DIRS = {"cmaps", "standard_fonts", "wasm", "iccs"}   # what some PDFs need: fonts, character maps, decoders
PDFJS_BUILD = {"build/pdf.min.mjs", "build/pdf.worker.min.mjs"}
PDFJS_FILE_RE = re.compile(r"^(build|cmaps|standard_fonts|wasm|iccs)/[A-Za-z0-9._-]{1,80}$")
PDFJS_TYPES = {"mjs": "text/javascript", "js": "text/javascript", "wasm": "application/wasm"}
pdfjs_lock = threading.Lock()
MODELS = FOLDER / "models"   # 3D models shown on the right of entries, as binary glTF (.glb) files
MODEL_RE = re.compile(r"^[a-f0-9]{32}\.glb$")
MAX_MODEL = 200_000_000
BOOK_DRAFTS = FOLDER / "book drafts"   # book models started but not yet made, one small JSON file each
DRAFT_RE = re.compile(r"^[a-f0-9]{16}$")
MAX_DRAFT = 500_000
SETTINGS = FOLDER / "settings.json"
TOPICS = FOLDER / "topics.json"   # the topics made in the Topics menu, in order
HEX_RE = re.compile(r"^#[0-9a-fA-F]{6}$")
KEY_RE = re.compile(r"^(Ctrl\+)?(Alt\+)?(Shift\+)?(Meta\+)?([A-Z0-9]|F([1-9]|1[0-9]|2[0-4])|Space|Enter|Tab|Backspace|Insert|"
                    r"Delete|Home|End|PageUp|PageDown|ArrowUp|ArrowDown|ArrowLeft|ArrowRight)$")
SETTING_KEYS = {"freezeKey", "indentKey", "logKey", "shotKey"}   # keyboard shortcuts, written like "Shift+Z" or "Ctrl+Alt+F"
SETTING_RANGES = {"brandSize": (14, 60), "titleSize": (18, 80), "bodySize": (12, 36), "imgBorder": (0, 8), "zoomLevel": (1.5, 12), "shelfHeight": (150, 800),
                  "subSize": (12, 60), "shelfScale": (25, 100),
                  "topicSize": (10, 48), "listTopicSize": (8, 28), "boldAmount": (1, 8), "underlineThick": (1, 8),
                  "taskScale": (50, 250), "taskMenuScale": (50, 250), "turnSpeed": (25, 200),
                  # the PDF export (sizes in points; the picture as a % of the page's height)
                  "exportBody": (6, 16), "exportMark": (2, 12), "exportNote": (4, 16), "exportNoteName": (4, 24), "exportPicture": (15, 90)}
SETTING_CHOICES = {"listSort": {"recent", "changes", "topic"},   # how the list of entries is shown
                   "tasksSort": {"urgency", "due"}}             # how the Tasks menu lists tasks
SETTING_COLOURS = {"caretColor", "newColor", "titleColor", "imgBorderColor", "subColor"}


def clean_settings(data):
    out = {}
    for key, (lo, hi) in SETTING_RANGES.items():
        v = data.get(key)
        if isinstance(v, (int, float)) and lo <= v <= hi:
            out[key] = v
    for key in SETTING_COLOURS:
        v = data.get(key)
        if isinstance(v, str) and HEX_RE.match(v):
            out[key] = v
    for key in SETTING_KEYS:
        v = data.get(key)
        if isinstance(v, str) and KEY_RE.match(v):
            out[key] = v
    for key, allowed in SETTING_CHOICES.items():
        if data.get(key) in allowed:
            out[key] = data[key]
    v = data.get("listTopics")   # the topics chosen for showing entries "By topic"
    if isinstance(v, list):
        ids = list(dict.fromkeys(x for x in v if isinstance(x, str) and TOPIC_ID_RE.match(x)))[:100]
        if ids:
            out["listTopics"] = ids
    return out
ID_RE = re.compile(r"^[A-Za-z0-9_-]{1,80}$")
TOPIC_ID_RE = re.compile(r"^[a-z0-9]{1,24}$")
ALLOWED_HOSTS = {f"127.0.0.1:{PORT}", f"localhost:{PORT}"}
lock = threading.Lock()


def iso(ms):
    return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).astimezone().isoformat(timespec="seconds")


def ms(text, fallback):
    try:
        return int(datetime.fromisoformat(text.strip()).timestamp() * 1000)
    except (ValueError, AttributeError):
        return fallback


def sniff(data):
    """Work out the image type from the file's contents, not its name."""
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        return "png"
    if data.startswith(b"\xff\xd8\xff"):
        return "jpg"
    if data[:6] in (b"GIF87a", b"GIF89a"):
        return "gif"
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return "webp"
    if data[4:8] == b"ftyp" and data[8:12] in (b"avif", b"avis"):
        return "avif"
    return None


def clean_images(value):
    if isinstance(value, str):
        value = value.split(",")
    if not isinstance(value, list):
        return []
    return [str(n).strip() for n in value if IMG_RE.match(str(n).strip())]


SIDE_ENTRY_RE = re.compile(r"^entry:[A-Za-z0-9_-]{1,80}$")
SIDE_QUOTE_RE = re.compile(r"^quote:[a-z0-9]{1,40}$")
SIDE_MODEL_RE = re.compile(r"^model:[a-f0-9]{32}\.glb$")
SIDE_DRAFT_RE = re.compile(r"^draft:[a-f0-9]{16}$")
SIDE_PDF_RE = re.compile(r"^pdf:[a-f0-9]{32}\.pdf$")


def clean_side(value):
    """What's shown on the right of an entry, in order: picture names, linked entries as "entry:<id>",
    quotes in the entry as "quote:<a short code made from the quote's words>", 3D models as "model:<file name>",
    unfinished book models as "draft:<its code>", and PDFs in the writing as "pdf:<file name>"."""
    if isinstance(value, str):
        value = value.split(",")
    if not isinstance(value, list):
        return []
    out = []
    for n in value:
        n = str(n).strip()
        if IMG_RE.match(n) or SIDE_ENTRY_RE.match(n) or SIDE_QUOTE_RE.match(n) or SIDE_MODEL_RE.match(n) or SIDE_DRAFT_RE.match(n) or SIDE_PDF_RE.match(n):
            out.append(n)
    return out


CSS_VAR_RE = re.compile(r"^--[a-z][a-z0-9-]{0,40}$")
CSS_VAL_RE = re.compile(r"^-?[0-9.]{1,12}(px|em|rem|%)?$")


def clean_ink(v):
    """One linked entry's ink: {"img": pen marks (a see-through picture), "w": the width the entry was laid out
    at when they were drawn, "v": its writing sizes then, "hl": highlights, each the words they cover}."""
    if isinstance(v, str):   # from before highlights were kept as words: just the picture
        v = {"img": v}
    if not isinstance(v, dict):
        return None
    out = {}
    img = str(v.get("img") or "")
    if IMG_RE.match(img):
        out["img"] = img
        w = v.get("w")
        if isinstance(w, (int, float)) and not isinstance(w, bool) and 20 <= w <= 5000:
            out["w"] = round(float(w), 2)
        sizes = v.get("v")
        if isinstance(sizes, dict):
            sizes = {str(k): str(x).strip() for k, x in list(sizes.items())[:40]
                     if CSS_VAR_RE.match(str(k)) and CSS_VAL_RE.match(str(x).strip())}
            if sizes:
                out["v"] = sizes
    marks = []
    for m in v.get("hl") if isinstance(v.get("hl"), list) else []:
        if not isinstance(m, dict):
            continue
        a, b, q, c = m.get("s"), m.get("e"), m.get("q"), m.get("c")
        if (isinstance(a, int) and isinstance(b, int) and not isinstance(a, bool) and not isinstance(b, bool)
                and 0 <= a < b <= 10_000_000 and isinstance(q, str) and 0 < len(q) <= 20_000
                and isinstance(c, str) and HEX_RE.match(c)):
            marks.append({"s": a, "e": b, "q": q, "c": c})
    if marks:
        out["hl"] = marks[:5000]
    return out or None


def clean_inks(value):
    """Ink drawn over linked entries (and quotes) on the right: {linked entry id, or "q-<quote code>": its ink}.
    Kept in the file on one line, as "inks: {...}"."""
    if isinstance(value, str):
        value = value.strip()
        if value.startswith("{"):
            try:
                value = json.loads(value)
            except ValueError:
                return {}
        else:   # the first way it was written: "inks: <id>=<picture>, <id>=<picture>"
            pairs = (part.partition("=") for part in value.split(","))
            value = {k.strip(): v.strip() for k, sep, v in pairs if sep}
    if not isinstance(value, dict):
        return {}
    out = {}
    for k, v in list(value.items())[:1000]:
        ink = clean_ink(v)
        if ID_RE.match(str(k)) and ink:
            out[str(k)] = ink
    return out


def entry_pictures(entry):
    """Every picture that belongs to an entry: those in its writing, and its pen marks over linked entries."""
    names = list(entry.get("images", []))
    return names + [i["img"] for i in entry.get("inks", {}).values() if i.get("img") and i["img"] not in names]


def entry_pdfs(entry):
    """The PDFs an entry has: those linked from its writing, and those made into books with its models."""
    return set(PDF_IN_BODY_RE.findall(entry.get("body", ""))) | set(entry.get("books", {}).values())


def clean_books(value):
    """Book models made into readable books: {model file name: PDF file name}.
    Kept in the entry's file on one line, as "books: <model>=<pdf>, <model>=<pdf>"."""
    if isinstance(value, str):
        pairs = (part.partition("=") for part in value.split(","))
        value = {k.strip(): v.strip() for k, sep, v in pairs if sep}
    if not isinstance(value, dict):
        return {}
    return {str(k): str(v) for k, v in list(value.items())[:500] if MODEL_RE.match(str(k)) and PDF_RE.match(str(v))}


def pdfs_in_use():
    """Every PDF linked from an entry, in the journal or in the archive."""
    used = set()
    for folder in (ENTRIES, ARCHIVE_ENTRIES):
        for p in folder.glob("*.md") if folder.exists() else []:
            try:
                used |= entry_pdfs(read_entry(p))
            except (OSError, UnicodeDecodeError):
                pass
    return used


def erase_unused_pdfs(names):
    """Erases those of these PDFs that no entry links to any more. Returns the ones kept."""
    names = {n for n in names if PDF_RE.match(n)}
    if not names:
        return set()
    used = pdfs_in_use()
    for n in names - used:
        (PDFS / n).unlink(missing_ok=True)
    return names & used


def pdfjs_ready():
    try:
        return ((PDFJS / ".version").read_text(encoding="utf-8").strip() == PDFJS_VERSION
                and all((PDFJS / f).is_file() for f in PDFJS_BUILD))
    except OSError:
        return False


def ensure_pdfjs():
    """Downloads pdf.js into journal/pdfjs the first time a PDF is read as a book. The package is checked
    against its published fingerprint before anything in it is kept. Returns True when it's there."""
    with pdfjs_lock:
        if pdfjs_ready():
            return True
        try:
            import urllib.request
            with urllib.request.urlopen(PDFJS_URL, timeout=60) as r:
                data = r.read(60_000_000)
            if base64.b64encode(hashlib.sha512(data).digest()).decode() != PDFJS_SHA512:
                raise ValueError("pdf.js didn't match its fingerprint")
            tmp = FOLDER / f".pdfjs.{secrets.token_hex(4)}.tmp"
            tmp.mkdir(parents=True)
            with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tar:
                for m in tar.getmembers():
                    rel = m.name[len("package/"):] if m.name.startswith("package/") else ""
                    wanted = rel in PDFJS_BUILD or rel == "LICENSE" or (
                        PDFJS_FILE_RE.match(rel) and rel.split("/")[0] in PDFJS_DIRS)
                    if not (m.isfile() and wanted):
                        continue
                    out = tmp / rel
                    out.parent.mkdir(parents=True, exist_ok=True)
                    out.write_bytes(tar.extractfile(m).read())
            (tmp / ".version").write_text(PDFJS_VERSION, encoding="utf-8")
            if PDFJS.exists():
                shutil.rmtree(PDFJS)
            os.replace(tmp, PDFJS)
            return True
        except Exception as e:
            print(f"Couldn't get pdf.js (for reading PDFs as books): {e}")
            for t in FOLDER.glob(".pdfjs.*.tmp"):
                shutil.rmtree(t, ignore_errors=True)
            return False


def clean_topic(value):
    value = str(value or "").strip()
    return value if TOPIC_ID_RE.match(value) else ""


def clean_topic_ids(value):
    """An entry's topics: a list of topic ids, each once, in the order given."""
    if isinstance(value, str):
        value = value.split(",")
    out = []
    for v in value if isinstance(value, list) else []:
        tid = clean_topic(v)
        if tid and tid not in out:
            out.append(tid)
    return out[:100]


def clean_topics(data):
    """[{id, name}, ...] in the order they're numbered."""
    out, seen = [], set()
    for t in data if isinstance(data, list) else []:
        if not isinstance(t, dict):
            continue
        tid = clean_topic(t.get("id"))
        if tid and tid not in seen:
            seen.add(tid)
            out.append({"id": tid, "name": " ".join(str(t.get("name", "")).split())[:120]})
    return out[:500]


def load_links(path=None):
    try:
        data = json.loads((path or LINKS).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    if not isinstance(data, dict):
        return {}
    return {k: v for k, v in data.items() if isinstance(v, str) and IMG_RE.match(k) and IMG_RE.match(v)}


def save_links(links, folder=None):
    folder = folder or ORIGINALS
    folder.mkdir(parents=True, exist_ok=True)
    tmp = folder / ".links.tmp"
    tmp.write_text(json.dumps(links, indent=2), encoding="utf-8")
    os.replace(tmp, folder / "links.json")


def discard(path, forever, archive_to):
    """Erase a file for good, or move it into the given archive folder."""
    if not path.exists():
        return
    if forever:
        path.unlink()
    else:
        archive_to.mkdir(parents=True, exist_ok=True)
        os.replace(path, archive_to / path.name)
        os.utime(archive_to / path.name)   # the file's date now records when it was archived


def discard_image(name, forever):
    """Archive or erase a picture, together with every earlier version it was drawn from."""
    links = load_links()
    discard(IMAGES / name, forever, ARCHIVE_IMAGES)
    moved, seen = {}, {name}
    while name in links:
        previous = links.pop(name)
        moved[name] = previous
        if previous in seen:
            break
        seen.add(previous)
        discard(ORIGINALS / previous, forever, ARCHIVE_ORIGINALS)
        name = previous
    if moved:
        save_links(links)
        if not forever:
            # Keep a record of which archived picture came from which, as in the main folder.
            archived = load_links(ARCHIVE_ORIGINALS / "links.json")
            archived.update(moved)
            save_links(archived, ARCHIVE_ORIGINALS)


def move_entries_into_folders():
    """Entries used to sit loose in journal/ and journal/archive/; they now live in entries/ folders."""
    for loose, folder in ((FOLDER, ENTRIES), (ARCHIVE, ARCHIVE_ENTRIES)):
        if not loose.exists():
            continue
        for p in loose.glob("*.md"):
            if ID_RE.match(p.stem) and not (folder / p.name).exists():
                folder.mkdir(parents=True, exist_ok=True)
                os.replace(p, folder / p.name)


# ---------- Folders in the archive's Images and Models ----------
# Folders are ordinary folders inside journal/archive/images or journal/archive/models (and inside each other),
# named by you. Pictures and models keep their own file names wherever they are, so the journal finds one by
# its name alone. Each function works on the images unless given the models' root.
FOLDER_NAME_BAD = re.compile(r'[<>:"/\\|?*\x00-\x1f]')
WINDOWS_RESERVED = {"CON", "PRN", "AUX", "NUL", *(f"COM{i}" for i in range(1, 10)), *(f"LPT{i}" for i in range(1, 10))}
MAX_FOLDER_NAME = 80


def clean_folder_name(value):
    """A folder name that's safe on Windows, macOS and Linux, or None."""
    if not isinstance(value, str):
        return None
    name = " ".join(value.split()).rstrip(". ")
    if (not name or len(name) > MAX_FOLDER_NAME or name.startswith(".") or FOLDER_NAME_BAD.search(name)
            or name.split(".")[0].upper() in WINDOWS_RESERVED):
        return None
    return name


def archive_folder(rel, root=ARCHIVE_IMAGES):
    """"Birds/Owls" -> that folder inside archive/images ("" is archive/images itself), or None if not allowed."""
    if rel in ("", None):
        return root
    if not isinstance(rel, str):
        return None
    parts = rel.split("/")
    if len(parts) > 30 or any(clean_folder_name(p) != p for p in parts):
        return None
    return root.joinpath(*parts)


def folder_rel(path, root=ARCHIVE_IMAGES):
    rel = path.relative_to(root).as_posix()
    return "" if rel == "." else rel


def find_archived_image(name, root=ARCHIVE_IMAGES):
    """Where an archived picture (or, with the models' root, model) is: loose in the root, or in one of its folders."""
    p = root / name
    if p.is_file():
        return p
    if root.exists():
        for q in root.rglob(name):
            if q.is_file() and not any(part.startswith(".") for part in q.relative_to(root).parts):
                return q
    return None


def find_archived_model(name):
    return find_archived_image(name, ARCHIVE_MODELS) if MODEL_RE.match(name) else None


def free_folder_name(parent, name, skip=None):
    """name, or "name 2", "name 3"… so it doesn't clash with anything already in parent."""
    taken = {c.name.lower() for c in parent.iterdir() if c != skip} if parent.exists() else set()
    out, n = name, 2
    while out.lower() in taken:
        out, n = f"{name} {n}", n + 1
    return out


def make_archive_folder(parent_rel, name, root=ARCHIVE_IMAGES):
    parent = archive_folder(parent_rel, root)
    name = clean_folder_name(name or "New folder")
    if parent is None or name is None or (parent_rel and not parent.is_dir()):
        return None
    parent.mkdir(parents=True, exist_ok=True)
    name = free_folder_name(parent, name)
    (parent / name).mkdir()
    return folder_rel(parent / name, root)


def rename_archive_folder(rel, name, root=ARCHIVE_IMAGES):
    """Returns the folder's new path, None if not allowed, or False if the name is already used there."""
    src, name = archive_folder(rel, root), clean_folder_name(name)
    if not rel or src is None or name is None or not src.is_dir():
        return None
    if name == src.name:
        return rel
    if name.lower() != src.name.lower() and any(c.name.lower() == name.lower() for c in src.parent.iterdir()):
        return False
    dest = src.parent / name
    os.replace(src, dest)
    return folder_rel(dest, root)


def delete_archive_folder(rel, root=ARCHIVE_IMAGES):
    """Deletes a folder only if there are no pictures (or other files) anywhere inside it."""
    src = archive_folder(rel, root)
    if not rel or src is None or not src.is_dir():
        return None
    if any(p.is_file() for p in src.rglob("*")):
        return False
    shutil.rmtree(src)
    return True


def move_in_archive(images, folders, to_rel, root=ARCHIVE_IMAGES):
    """Puts pictures or models (by name) and folders (by path) into the folder to_rel. Returns how many moved, or None."""
    name_re = MODEL_RE if root == ARCHIVE_MODELS else IMG_RE
    dest = archive_folder(to_rel, root)
    if dest is None or (to_rel and not dest.is_dir()):
        return None
    dest.mkdir(parents=True, exist_ok=True)
    moved = 0
    for name in images:
        if not isinstance(name, str) or not name_re.match(name):
            continue
        src = find_archived_image(name, root)
        if src and src.parent != dest and not (dest / name).exists():
            os.replace(src, dest / name)
            moved += 1
    real_dest = dest.resolve()
    for rel in folders:
        src = archive_folder(rel, root)
        if not rel or src is None or not src.is_dir() or src.parent == dest:
            continue
        real_src = src.resolve()
        if real_dest == real_src or real_src in real_dest.parents:
            continue   # a folder can't go inside itself
        os.replace(src, dest / free_folder_name(dest, src.name))
        moved += 1
    return moved


# ---------- Archived tasks ----------
# A finished task archived from the Tasks menu is copied into archive/tasks.json, with which entry it came
# from and where in it. It stays in its entry (noted there as archived) and only leaves the Tasks menu.
TASK_STAMP_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}$")
TASK_ID_RE = re.compile(r"^[0-9a-f]{16}$")
MAX_TASK_TEXT = 20_000


def load_archived_tasks():
    try:
        data = json.loads(ARCHIVE_TASKS.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return []
    return [t for t in data if isinstance(t, dict) and TASK_ID_RE.match(str(t.get("id", "")))] if isinstance(data, list) else []


def save_archived_tasks(tasks):
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    tmp = ARCHIVE / ".tasks.tmp"
    tmp.write_text(json.dumps(tasks, indent=2, ensure_ascii=False), encoding="utf-8")
    replace_file(tmp, ARCHIVE_TASKS)


def clean_archived_task(t):
    if not isinstance(t, dict) or not isinstance(t.get("item"), dict):
        return None
    item = t["item"]
    state, text = item.get("state"), item.get("text", "")
    if state not in ("x", "-") or not isinstance(text, str) or len(text) > MAX_TASK_TEXT:
        return None
    if not isinstance(t.get("entry"), str) or not ID_RE.match(t["entry"]):
        return None
    clean = {"state": state, "text": text.replace("\n", " ")}
    for k in ("created", "due", "marked"):
        v = item.get(k, "")
        clean[k] = v if isinstance(v, str) and TASK_STAMP_RE.match(v) else ""
    clean["urgency"] = item.get("urgency") if item.get("urgency") in ("high", "medium", "low") else ""
    num = lambda v: v if isinstance(v, int) and not isinstance(v, bool) and 0 <= v <= 100_000 else 0
    title = t.get("entryTitle", "")
    return {"entry": t["entry"], "entryTitle": title[:500] if isinstance(title, str) else "",
            "block": num(t.get("block")), "pos": num(t.get("pos")), "alone": t.get("alone") is True,
            "archived": datetime.now().strftime("%Y-%m-%dT%H:%M"), "item": clean}


def archive_listing():
    entries, used = {}, set()
    for p in ARCHIVE_ENTRIES.glob("*.md") if ARCHIVE_ENTRIES.exists() else []:
        if ID_RE.match(p.stem):
            try:
                e = read_entry(p)
            except (OSError, UnicodeDecodeError):
                continue
            e["archived"] = int(p.stat().st_mtime * 1000)
            entries[p.stem] = e
            used.update(entry_pictures(e))
    images, folders = [], []
    for dirpath, dirnames, filenames in os.walk(ARCHIVE_IMAGES) if ARCHIVE_IMAGES.exists() else []:
        here = Path(dirpath)
        rel = folder_rel(here)
        dirnames[:] = sorted((d for d in dirnames if clean_folder_name(d) == d), key=str.lower)
        for d in dirnames:
            folders.append({"path": f"{rel}/{d}" if rel else d})
        for f in filenames:
            if IMG_RE.match(f) and f not in used:
                images.append({"name": f, "folder": rel, "archived": int((here / f).stat().st_mtime * 1000)})
    models, model_folders = [], []
    for dirpath, dirnames, filenames in os.walk(ARCHIVE_MODELS) if ARCHIVE_MODELS.exists() else []:
        here = Path(dirpath)
        rel = folder_rel(here, ARCHIVE_MODELS)
        dirnames[:] = sorted((d for d in dirnames if clean_folder_name(d) == d), key=str.lower)
        for d in dirnames:
            model_folders.append({"path": f"{rel}/{d}" if rel else d})
        for f in filenames:
            if MODEL_RE.match(f):
                models.append({"name": f, "folder": rel, "archived": int((here / f).stat().st_mtime * 1000)})
    return {"entries": entries, "images": images, "folders": folders, "tasks": load_archived_tasks(),
            "models": models, "modelFolders": model_folders}


def archive_model(name):
    """A model taken off the right of its entry into the archive (loose, at the top of Models)."""
    src = MODELS / name
    if not MODEL_RE.match(name) or not src.is_file():
        return False
    ARCHIVE_MODELS.mkdir(parents=True, exist_ok=True)
    os.replace(src, ARCHIVE_MODELS / name)
    os.utime(ARCHIVE_MODELS / name)   # "archived" is when it went in
    return True


def restore_archived_model(name):
    """Brings an archived model back into journal/models. Returns its name there, or None."""
    src = find_archived_model(name)
    if not src:
        return None
    MODELS.mkdir(exist_ok=True)
    if (MODELS / name).exists():
        name = f"{secrets.token_hex(16)}.glb"
    os.replace(src, MODELS / name)
    return name


def erase_archived_image(name):
    found = find_archived_image(name)
    if found:
        found.unlink(missing_ok=True)
    links = load_links(ARCHIVE_ORIGINALS / "links.json")
    changed, seen = False, {name}
    while name in links:
        name = links.pop(name)
        changed = True
        if name in seen:
            break
        seen.add(name)
        (ARCHIVE_ORIGINALS / name).unlink(missing_ok=True)
    if changed:
        save_links(links, ARCHIVE_ORIGINALS)


def restore_archived_image(name):
    """Brings an archived picture back into the journal, for dragging into an entry. A picture on its own is
    moved back, with its earlier versions; one that belongs to an archived entry is copied, so that entry
    keeps it. Returns (name in the journal, whether it was copied), or None if it isn't in the archive."""
    src = find_archived_image(name)
    if not src:
        return None
    used = set()
    for p in ARCHIVE_ENTRIES.glob("*.md") if ARCHIVE_ENTRIES.exists() else []:
        if ID_RE.match(p.stem):
            try:
                used.update(entry_pictures(read_entry(p)))
            except (OSError, UnicodeDecodeError):
                pass
    IMAGES.mkdir(exist_ok=True)
    if name in used or (IMAGES / name).exists():
        new = f"{secrets.token_hex(16)}.{name.rsplit('.', 1)[1]}"
        shutil.copyfile(src, IMAGES / new)
        return new, True
    os.replace(src, IMAGES / name)
    archived_links = load_links(ARCHIVE_ORIGINALS / "links.json")
    links = load_links()
    current, seen = name, {name}
    while current in archived_links:
        previous = archived_links.pop(current)
        links[current] = previous
        if (ARCHIVE_ORIGINALS / previous).exists():
            ORIGINALS.mkdir(exist_ok=True)
            os.replace(ARCHIVE_ORIGINALS / previous, ORIGINALS / previous)
        if previous in seen:
            break
        seen.add(previous)
        current = previous
    if current != name:
        save_links(links)
        save_links(archived_links, ARCHIVE_ORIGINALS)
    return name, False


def restore_entry(entry_id):
    """Move an archived entry, its pictures and their earlier versions back into the journal."""
    src, dest = ARCHIVE_ENTRIES / f"{entry_id}.md", ENTRIES / f"{entry_id}.md"
    if not src.exists() or dest.exists():
        return False
    entry = read_entry(src)
    archived_links = load_links(ARCHIVE_ORIGINALS / "links.json")
    links = load_links()
    for name in entry_pictures(entry):
        found = find_archived_image(name)
        if found:
            os.replace(found, IMAGES / name)
        current, seen = name, {name}
        while current in archived_links:
            previous = archived_links.pop(current)
            links[current] = previous
            if (ARCHIVE_ORIGINALS / previous).exists():
                ORIGINALS.mkdir(exist_ok=True)
                os.replace(ARCHIVE_ORIGINALS / previous, ORIGINALS / previous)
            if previous in seen:
                break
            seen.add(previous)
            current = previous
    save_links(links)
    if ARCHIVE_ORIGINALS.exists():
        save_links(archived_links, ARCHIVE_ORIGINALS)
    os.replace(src, dest)
    return True


def read_entry(path):
    text = path.read_text(encoding="utf-8")
    mtime = int(path.stat().st_mtime * 1000)
    meta, body = {}, text
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            for line in text[4:end].splitlines():
                key, sep, value = line.partition(":")
                if sep:
                    meta[key.strip()] = value.strip()
            body = text[end + 5:]
            if body.startswith("\n"):
                body = body[1:]
    return {
        "title": meta.get("title", path.stem if not meta else ""),
        "body": body,
        "created": ms(meta.get("created"), mtime),
        "updated": ms(meta.get("updated"), mtime),
        "images": clean_images(meta.get("images", "")),
        "side": clean_side(meta.get("side", "")),
        "inks": clean_inks(meta.get("inks", "")),
        "books": clean_books(meta.get("books", "")),
        "topics": clean_topic_ids(meta.get("topics", meta.get("topic", ""))),   # "topic:" was used when an entry had only one
        "history": [t for t in (ms(x, None) for x in meta.get("history", "").split(",") if x.strip()) if t],
    }


def replace_file(tmp, target):
    """Put tmp in target's place. On Windows a file another program has open for a moment (a sync or backup app,
    antivirus, search indexing) can't be replaced, so try again for up to about two seconds before giving up."""
    for attempt in range(10):
        try:
            os.replace(tmp, target)
            return
        except PermissionError:
            if attempt == 9:
                raise
            time.sleep(0.05 * (attempt + 1))


def write_entry(entry_id, data):
    title = " ".join(str(data.get("title", "")).split())
    body = str(data.get("body", ""))
    now = int(time.time() * 1000)
    created = data.get("created") if isinstance(data.get("created"), (int, float)) else now
    updated = data.get("updated") if isinstance(data.get("updated"), (int, float)) else now
    images = clean_images(data.get("images", []))
    image_line = f"images: {', '.join(images)}\n" if images else ""
    side = clean_side(data.get("side", []))   # pictures and linked entries shown on the right of this entry, in order
    side_line = f"side: {', '.join(side)}\n" if side else ""
    inks = clean_inks(data.get("inks", {}))   # ink drawn over linked entries shown on the right
    ink_line = f"inks: {json.dumps(inks, ensure_ascii=False, separators=(',', ':'))}\n" if inks else ""
    books = clean_books(data.get("books", {}))   # book models made readable with a PDF
    book_line = f"books: {', '.join(f'{k}={v}' for k, v in books.items())}\n" if books else ""
    topic_ids = clean_topic_ids(data.get("topics", []))
    topic_line = f"topics: {', '.join(topic_ids)}\n" if topic_ids else ""
    history = [t for t in data.get("history", []) if isinstance(t, (int, float))][-2000:] if isinstance(data.get("history"), list) else []
    history_line = f"history: {', '.join(iso(t) for t in history)}\n" if history else ""
    content = (f"---\ntitle: {title}\ncreated: {iso(created)}\nupdated: {iso(updated)}\n"
               f"{image_line}{side_line}{ink_line}{book_line}{topic_line}{history_line}---\n\n{body}")
    ENTRIES.mkdir(exist_ok=True)
    target = ENTRIES / f"{entry_id}.md"
    tmp = ENTRIES / f".{entry_id}.tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    replace_file(tmp, target)   # atomic: a crash never leaves a half-written entry


# ---------- Log ----------
# What you did each day: activities kept in journal/log/activities.json, each with a title, a description,
# when it started and/or finished, and pictures (kept in journal/log/images). An activity with a start and
# no finish is ongoing. The Log menu shows them by day, numbered in the order they started.
LOG = FOLDER / "log"
LOG_FILE = LOG / "activities.json"
LOG_IMAGES = LOG / "images"
LOG_ID_RE = re.compile(r"^[0-9a-f]{16}$")
MAX_LOG_TITLE = 500
MAX_LOG_TEXT = 20_000
MAX_LOG_IMAGES = 60


def load_log():
    try:
        data = json.loads(LOG_FILE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return []
    if not isinstance(data, list):
        return []
    return [a for a in data if isinstance(a, dict) and LOG_ID_RE.match(str(a.get("id", "")))]


def save_log(acts):
    LOG.mkdir(parents=True, exist_ok=True)
    tmp = LOG / ".activities.tmp"
    tmp.write_text(json.dumps(acts, indent=2, ensure_ascii=False), encoding="utf-8")
    replace_file(tmp, LOG_FILE)


def log_images_in_use(acts):
    return {n for a in acts for n in a.get("images", [])}


def change_activity(act, data):
    """Takes the fields present in data into act. Returns False if something in data isn't allowed."""
    for key, limit in (("title", MAX_LOG_TITLE), ("description", MAX_LOG_TEXT)):
        if key in data:
            v = data[key]
            if not isinstance(v, str) or len(v) > limit:
                return False
            act[key] = " ".join(v.split()) if key == "title" else v.replace("\r\n", "\n")
    for key in ("start", "end"):
        if key in data:
            v = data[key]
            if v in ("", None):
                act[key] = ""
            elif isinstance(v, str) and TASK_STAMP_RE.match(v):
                act[key] = v
            else:
                return False
    names = None
    if "images" in data:
        names = data["images"]
    elif "addImages" in data:
        names = act.get("images", []) + (data["addImages"] if isinstance(data["addImages"], list) else [None])
    if names is not None:
        if not isinstance(names, list) or not all(isinstance(n, str) and IMG_RE.match(n) and (LOG_IMAGES / n).is_file() for n in names):
            return False
        act["images"] = list(dict.fromkeys(names))[:MAX_LOG_IMAGES]
    return bool(act.get("start") or act.get("end"))   # it has to have happened at some time


def erase_unused_log_images(names, acts):
    used = log_images_in_use(acts)
    for n in names:
        if n not in used and IMG_RE.match(n):
            (LOG_IMAGES / n).unlink(missing_ok=True)


class log_file_lock:
    """Only one program changes the log at a time: the journal, or the logging window when the journal isn't open."""
    def __enter__(self):
        LOG.mkdir(parents=True, exist_ok=True)
        self.f = open(LOG / ".lock", "a+b")
        if os.name == "nt":
            import msvcrt
            for _ in range(400):
                try:
                    self.f.seek(0)
                    msvcrt.locking(self.f.fileno(), msvcrt.LK_NBLCK, 1)
                    break
                except OSError:
                    time.sleep(0.025)
        else:
            import fcntl
            fcntl.flock(self.f, fcntl.LOCK_EX)
        return self

    def __exit__(self, *exc):
        try:
            if os.name == "nt":
                import msvcrt
                self.f.seek(0)
                msvcrt.locking(self.f.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                import fcntl
                fcntl.flock(self.f, fcntl.LOCK_UN)
        except OSError:
            pass
        self.f.close()


def store_log_image(data):
    """Keeps a picture for the Log. Returns its name, or None if it isn't a picture the journal keeps."""
    ext = sniff(data)
    if not ext or len(data) > MAX_IMAGE:
        return None
    name = f"{secrets.token_hex(16)}.{ext}"
    LOG_IMAGES.mkdir(parents=True, exist_ok=True)
    tmp = LOG_IMAGES / f".{name}.tmp"
    tmp.write_bytes(data)
    os.replace(tmp, LOG_IMAGES / name)   # appears only once it's complete
    return name


def create_activity(data):
    """A new activity in the Log. Returns it, or None if data isn't allowed. Raises OSError if it can't be saved."""
    with log_file_lock():
        acts = load_log()
        act = {"id": secrets.token_hex(8), "title": "", "description": "", "start": "", "end": "", "images": [],
               "logged": datetime.now().strftime("%Y-%m-%dT%H:%M")}
        while any(a["id"] == act["id"] for a in acts):
            act["id"] = secrets.token_hex(8)
        if not change_activity(act, data):
            return None
        save_log(acts + [act])
        return act


def update_activity(act_id, data):
    """Changes an activity. Returns it, "missing" if there's no such activity, or None if data isn't allowed."""
    with log_file_lock():
        acts = load_log()
        act = next((a for a in acts if a["id"] == act_id), None)
        if not act:
            return "missing"
        before = list(act.get("images", []))
        changed = dict(act)
        if not change_activity(changed, data):
            return None
        acts = [changed if a is act else a for a in acts]
        save_log(acts)
        erase_unused_log_images(before, acts)   # pictures taken off it are erased
        return changed


def delete_activity(act_id):
    with log_file_lock():
        acts = load_log()
        gone = next((a for a in acts if a["id"] == act_id), None)
        if not gone:
            return False
        acts = [a for a in acts if a is not gone]
        save_log(acts)
        erase_unused_log_images(gone.get("images", []), acts)
        return True


# ---------- Logging from anywhere ----------
# A keyboard shortcut (Ctrl+Shift+L unless changed in the Menu) opens a small window over whatever you're doing,
# for logging an activity; another (Ctrl+Alt+S) takes a screenshot and adds it to the activity you started last.
# The window saves straight into journal/log, so the journal needn't be open.
# On Linux the journal gives the shortcuts to the desktop (Hyprland, GNOME, Ubuntu, Budgie, Cinnamon, MATE or Xfce), so they
# work all the time, even when the journal isn't running. On Windows the journal listens for them itself while it runs.
LOG_KEY_DEFAULT = "Ctrl+Shift+L"
SHOT_KEY_DEFAULT = "Ctrl+Alt+S"
hotkeys = {"thread": None, "state": {}}


def saved_setting(key, default):
    try:
        return clean_settings(json.loads(SETTINGS.read_text(encoding="utf-8"))).get(key, default)
    except (OSError, ValueError):
        return default


def helper_command(flag):
    script = Path(__file__).resolve()
    if os.name == "nt":
        w = Path(sys.executable).with_name("pythonw.exe")
        return f'"{w if w.exists() else sys.executable}" "{script}" {flag}'
    return f'"{sys.executable}" "{script}" {flag}'


def launch_helper(flag):
    """Runs this script again as a small separate program: the logging window (--log) or a screenshot (--screenshot)."""
    exe, flags = sys.executable, 0
    if os.name == "nt":
        w = Path(sys.executable).with_name("pythonw.exe")
        if w.exists():
            exe = str(w)
        else:
            flags = 0x08000000   # CREATE_NO_WINDOW: no black window flashing up
        try:
            import ctypes
            ctypes.windll.user32.AllowSetForegroundWindow(ctypes.c_uint32(0xFFFFFFFF).value)   # let the window come to the front
        except Exception:
            pass
    try:
        import subprocess
        subprocess.Popen([exe, str(Path(__file__).resolve()), flag], creationflags=flags, close_fds=True,
                         stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except OSError as e:
        print(f"Couldn't open the logging window: {e}")


VK_NAMED = {"Space": 0x20, "Enter": 0x0D, "Tab": 0x09, "Backspace": 0x08, "Insert": 0x2D, "Delete": 0x2E, "Home": 0x24,
            "End": 0x23, "PageUp": 0x21, "PageDown": 0x22, "ArrowUp": 0x26, "ArrowDown": 0x28, "ArrowLeft": 0x25, "ArrowRight": 0x27}


def parse_hotkey(combo):
    """"Ctrl+Shift+L" -> (modifiers, virtual key) for Windows, or a string saying why it can't be used all over the computer."""
    if not isinstance(combo, str) or not KEY_RE.match(combo):
        return "isn't a shortcut the journal understands"
    *mods, key = combo.split("+")
    if not ({"Ctrl", "Alt", "Meta"} & set(mods)):
        return "needs Ctrl or Alt in it to work all over the computer (on its own it would catch that key every time you type it)"
    m = 0x4000   # MOD_NOREPEAT: holding the keys down doesn't open it again and again
    m |= 2 if "Ctrl" in mods else 0
    m |= 1 if "Alt" in mods else 0
    m |= 4 if "Shift" in mods else 0
    m |= 8 if "Meta" in mods else 0
    if len(key) == 1:
        vk = ord(key)
    elif key in VK_NAMED:
        vk = VK_NAMED[key]
    else:
        vk = 0x70 + int(key[1:]) - 1   # F1 to F24
    return m, vk


def start_hotkeys():
    if os.name == "nt":
        threading.Thread(target=_hotkey_loop, name="log shortcuts", daemon=True).start()
    elif sys.platform.startswith("linux"):
        linux_shortcuts(announce=True)
    else:
        hotkeys["state"] = {"global": False}


def hotkeys_changed():
    """The shortcuts were changed in the Menu: have them taken up."""
    if sys.platform.startswith("linux"):
        threading.Thread(target=linux_shortcuts, daemon=True).start()
        return
    tid = hotkeys["thread"]
    if tid:
        try:
            import ctypes
            ctypes.windll.user32.PostThreadMessageW(tid, 0x8001, 0, 0)
        except Exception:
            pass


def _hotkey_loop():
    import ctypes
    from ctypes import wintypes
    user32, kernel32 = ctypes.windll.user32, ctypes.windll.kernel32
    user32.RegisterHotKey.argtypes = [wintypes.HWND, ctypes.c_int, wintypes.UINT, wintypes.UINT]
    user32.UnregisterHotKey.argtypes = [wintypes.HWND, ctypes.c_int]
    user32.GetMessageW.argtypes = [ctypes.POINTER(wintypes.MSG), wintypes.HWND, wintypes.UINT, wintypes.UINT]
    user32.PeekMessageW.argtypes = [ctypes.POINTER(wintypes.MSG), wintypes.HWND, wintypes.UINT, wintypes.UINT, wintypes.UINT]
    user32.PostThreadMessageW.argtypes = [wintypes.DWORD, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM]
    msg = wintypes.MSG()
    user32.PeekMessageW(ctypes.byref(msg), None, 0, 0, 0)   # gives this thread a message queue
    hotkeys["thread"] = kernel32.GetCurrentThreadId()
    jobs = {1: ("logKey", LOG_KEY_DEFAULT, "--log", "Log shortcut"), 2: ("shotKey", SHOT_KEY_DEFAULT, "--screenshot", "Screenshot shortcut")}

    def register():
        state = {"global": True}
        for n, (key, default, _, label) in jobs.items():
            user32.UnregisterHotKey(None, n)
            combo = saved_setting(key, default)
            parsed = parse_hotkey(combo)
            if isinstance(parsed, str):
                state[key] = f"{combo} {parsed}."
            elif not user32.RegisterHotKey(None, n, parsed[0], parsed[1]):
                state[key] = f"{combo} is already taken by another program, so it only works inside the journal. Choose another in the Menu."
            else:
                state[key] = ""
            if state[key]:
                print(f"{label}: {state[key]}")
        hotkeys["state"] = state

    register()
    while user32.GetMessageW(ctypes.byref(msg), None, 0, 0) > 0:
        if msg.message == 0x0312 and msg.wParam in jobs:   # WM_HOTKEY
            launch_helper(jobs[msg.wParam][2])
        elif msg.message == 0x8001:   # the Menu changed a shortcut
            register()


# ---------- Shortcuts on the Linux desktop ----------
# The desktop's own custom keyboard shortcuts run "server.py --log" and "server.py --screenshot". They're set each
# time the journal starts (so they follow the journal if its folder moves) and whenever they're changed in the Menu.
GNOME_KEYS = "org.gnome.settings-daemon.plugins.media-keys"
GNOME_PATH = "/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/"
CINNAMON_KEYS = "org.cinnamon.desktop.keybindings"
CINNAMON_PATH = "/org/cinnamon/desktop/keybindings/custom-keybindings/"
MATE_PATH = "/org/mate/desktop/keybindings/"
XFCE_KEYS = "xfce4-keyboard-shortcuts"
DESKTOP_KEY_NAMES = {"Space": "space", "Enter": "Return", "Tab": "Tab", "Backspace": "BackSpace", "Insert": "Insert",
                     "Delete": "Delete", "Home": "Home", "End": "End", "PageUp": "Page_Up", "PageDown": "Page_Down",
                     "ArrowUp": "Up", "ArrowDown": "Down", "ArrowLeft": "Left", "ArrowRight": "Right"}


def desktop_accel(combo, ctrl="<Control>"):
    """"Ctrl+Shift+L" -> "<Control><Shift>l", the way Linux desktops write shortcuts."""
    *mods, key = combo.split("+")
    names = {"Ctrl": ctrl, "Alt": "<Alt>", "Shift": "<Shift>", "Meta": "<Super>"}
    return "".join(names[m] for m in mods) + DESKTOP_KEY_NAMES.get(key, key.lower() if len(key) == 1 else key)


def gvariant(text):
    return "'" + text.replace("\\", "\\\\").replace("'", "\\'") + "'"


def _run(*cmd):
    import subprocess
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
    if r.returncode != 0:
        raise OSError((r.stderr or r.stdout or "failed").strip()[:300])
    return r.stdout


def which_desktop():
    if os.environ.get("HYPRLAND_INSTANCE_SIGNATURE"):
        return "Hyprland"
    names = [d.strip().lower() for d in (os.environ.get("XDG_CURRENT_DESKTOP", "") + ":" + os.environ.get("DESKTOP_SESSION", "")).split(":") if d.strip()]
    for want, family in (("hyprland", "Hyprland"), ("cinnamon", "Cinnamon"), ("mate", "MATE"), ("xfce", "Xfce"), ("kde", "KDE Plasma"), ("plasma", "KDE Plasma"),
                         ("gnome", "GNOME"), ("ubuntu", "GNOME"), ("unity", "GNOME"), ("budgie", "GNOME"), ("pop", "GNOME")):
        if any(want in n for n in names):
            return family
    return ""


def _gnome_like(schema_list, list_key, relocatable, base, slugs_as_paths, jobs, ctrl, binding_as_list=False, command_key="command"):
    have = re.findall(r"'([^']*)'", _run("gsettings", "get", schema_list, list_key)) if schema_list else []
    for slug, name, command, combo in jobs:
        path = f"{base}{slug}/"
        where = f"{relocatable}:{path}"
        accel = desktop_accel(combo, ctrl) if combo else ""
        _run("gsettings", "set", where, "name", gvariant(name))
        _run("gsettings", "set", where, command_key, gvariant(command))
        _run("gsettings", "set", where, "binding", ("[" + gvariant(accel) + "]" if accel else "@as []") if binding_as_list else gvariant(accel))
        entry = path if slugs_as_paths else slug
        if schema_list and entry not in have:
            have.append(entry)
    if schema_list:
        _run("gsettings", "set", schema_list, list_key, "[" + ", ".join(gvariant(x) for x in have) + "]")


def _xfce(jobs):
    listing = _run("xfconf-query", "-c", XFCE_KEYS, "-l", "-v")
    script = str(Path(__file__).resolve())
    ours, taken = [], {}
    for line in listing.splitlines():
        prop, _, value = line.partition(" ")
        value = value.strip()
        if prop.startswith("/commands/custom/"):
            if script in value and (value.endswith("--log") or value.endswith("--screenshot")):
                ours.append(prop)
            else:
                taken[prop] = value
    for prop in ours:   # the journal's old shortcuts, in case the keys have changed
        _run("xfconf-query", "-c", XFCE_KEYS, "-p", prop, "-r")
    problems = {}
    for slug, name, command, combo in jobs:
        prop = "/commands/custom/" + desktop_accel(combo, "<Primary>")
        if prop in taken:
            problems[slug] = f"{combo} is already a shortcut in Xfce (for {taken[prop]}). Choose other keys in the Menu."
            continue
        _run("xfconf-query", "-c", XFCE_KEYS, "-p", prop, "-n", "-t", "string", "-s", command)
    return problems


HYPR_KEY_NAMES = {"Space": "space", "Enter": "Return", "Tab": "Tab", "Backspace": "BackSpace", "Insert": "Insert", "Delete": "Delete",
                  "Home": "Home", "End": "End", "PageUp": "Page_Up", "PageDown": "Page_Down",
                  "ArrowUp": "Up", "ArrowDown": "Down", "ArrowLeft": "Left", "ArrowRight": "Right"}


def _hyprland(jobs):
    """Hyprland: the shortcuts go in their own file, hypr/journal.conf, which hyprland.conf is told to read
    (one "source =" line added at its end, once). Hyprland takes up the change by itself."""
    conf_dir = Path(os.environ.get("XDG_CONFIG_HOME") or Path.home() / ".config") / "hypr"
    main = conf_dir / "hyprland.conf"
    if not main.exists():
        raise OSError(f"there's no {main}")
    ours = conf_dir / "journal.conf"
    lines = ["# The journal's Log shortcuts, written by server.py each time it starts.",
             "# Change the keys in the journal's Menu (under Log) rather than here: this file is rewritten."]
    for slug, name, command, combo in jobs:
        if not combo:
            continue
        *mods, key = combo.split("+")
        hmods = " ".join({"Ctrl": "CTRL", "Alt": "ALT", "Shift": "SHIFT", "Meta": "SUPER"}[m] for m in mods)
        lines += [f"# {name}", f"bind = {hmods}, {HYPR_KEY_NAMES.get(key, key)}, exec, {command}"]
    text = "\n".join(lines) + "\n"
    if not ours.exists() or ours.read_text(encoding="utf-8") != text:
        ours.write_text(text, encoding="utf-8")
    source = f"source = {ours}"
    current = main.read_text(encoding="utf-8")
    if not any(l.strip() == source for l in current.splitlines()):
        with open(main, "a", encoding="utf-8") as f:
            f.write(("" if current.endswith("\n") or not current else "\n")
                    + "\n# The journal's Log shortcuts (Ctrl+Shift+L and so on), kept in their own file\n" + source + "\n")
    if shutil.which("hyprctl"):
        try:
            _run("hyprctl", "reload")
        except (OSError, ValueError):
            pass   # Hyprland reloads its settings by itself when the file changes


def linux_shortcuts(announce=False):
    """Gives the Log shortcuts to the desktop. Records what happened for the Menu."""
    desktop = which_desktop()
    keys = {"logKey": saved_setting("logKey", LOG_KEY_DEFAULT), "shotKey": saved_setting("shotKey", SHOT_KEY_DEFAULT)}
    state = {"global": False, "desktop": desktop}
    jobs, slug_of = [], {"logKey": "journal-log", "shotKey": "journal-screenshot"}
    for key, flag, name in (("logKey", "--log", "Journal: log an activity"), ("shotKey", "--screenshot", "Journal: add a screenshot")):
        parsed = parse_hotkey(keys[key])
        if isinstance(parsed, str):
            state[key] = f"{keys[key]} {parsed}."
            jobs.append((slug_of[key], name, helper_command(flag), ""))   # no keys: the shortcut is switched off
        else:
            state[key] = ""
            jobs.append((slug_of[key], name, helper_command(flag), keys[key]))
    try:
        if desktop == "Hyprland":
            _hyprland(jobs)
        elif desktop == "GNOME":
            _gnome_like(GNOME_KEYS, "custom-keybindings", GNOME_KEYS + ".custom-keybinding", GNOME_PATH, True, jobs, "<Control>")
        elif desktop == "Cinnamon":
            _gnome_like(CINNAMON_KEYS, "custom-list", CINNAMON_KEYS + ".custom-keybinding", CINNAMON_PATH, False, jobs, "<Primary>", binding_as_list=True)
        elif desktop == "MATE":
            _gnome_like(None, None, "org.mate.control-center.keybinding", MATE_PATH, False, jobs, "<Control>", command_key="action")
        elif desktop == "Xfce":
            for slug, problem in _xfce([j for j in jobs if j[3]]).items():
                state["logKey" if slug == "journal-log" else "shotKey"] = problem
        else:
            state["note"] = (f"The journal can't set shortcuts in {desktop} by itself." if desktop
                             else "The journal couldn't tell which desktop this is, so it can't set the shortcuts by itself.")
            hotkeys["state"] = state
            if announce:
                print(state["note"] + " Give these commands keyboard shortcuts in your system's keyboard settings:")
                print(f"  log an activity:   {helper_command('--log')}")
                print(f"  add a screenshot:  {helper_command('--screenshot')}")
            return
    except (OSError, ValueError) as e:
        state["note"] = f"Couldn't set the shortcuts in {desktop}: {e}"
        hotkeys["state"] = state
        if announce:
            print(state["note"])
        return
    state["global"] = True
    hotkeys["state"] = state
    if announce:
        print(f"Log shortcuts, anywhere on the computer (set in {desktop}, so they work even when the journal isn't running): "
              f"{keys['logKey']} to log an activity, {keys['shotKey']} to add a screenshot to the one you started last.")
        for key in ("logKey", "shotKey"):
            if state.get(key):
                print("  " + state[key])


# ---------- Screenshots ----------
def png_from_rgb(w, h, rgb):
    stride = w * 3
    rows = b"".join(b"\x00" + bytes(rgb[y * stride:(y + 1) * stride]) for y in range(h))
    def chunk(kind, data):
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(rows, 6)) + chunk(b"IEND", b""))


def dpi_aware():
    """On Windows, work in real screen pixels (so screenshots are sharp and whole, and the window isn't blurry)."""
    if os.name != "nt":
        return
    import ctypes
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
    except Exception:
        try:
            ctypes.windll.user32.SetProcessDPIAware()
        except Exception:
            pass


def _capture_windows():
    import ctypes
    from ctypes import wintypes
    user32, gdi32 = ctypes.windll.user32, ctypes.windll.gdi32
    user32.GetDC.restype, user32.GetDC.argtypes = wintypes.HDC, [wintypes.HWND]
    user32.ReleaseDC.argtypes = [wintypes.HWND, wintypes.HDC]
    gdi32.CreateCompatibleDC.restype, gdi32.CreateCompatibleDC.argtypes = wintypes.HDC, [wintypes.HDC]
    gdi32.CreateCompatibleBitmap.restype = wintypes.HBITMAP
    gdi32.CreateCompatibleBitmap.argtypes = [wintypes.HDC, ctypes.c_int, ctypes.c_int]
    gdi32.SelectObject.restype, gdi32.SelectObject.argtypes = wintypes.HGDIOBJ, [wintypes.HDC, wintypes.HGDIOBJ]
    gdi32.BitBlt.argtypes = [wintypes.HDC, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
                             wintypes.HDC, ctypes.c_int, ctypes.c_int, wintypes.DWORD]
    gdi32.GetDIBits.argtypes = [wintypes.HDC, wintypes.HBITMAP, wintypes.UINT, wintypes.UINT, ctypes.c_void_p, ctypes.c_void_p, wintypes.UINT]
    gdi32.DeleteObject.argtypes = [wintypes.HGDIOBJ]
    gdi32.DeleteDC.argtypes = [wintypes.HDC]

    class BITMAPINFOHEADER(ctypes.Structure):
        _fields_ = [("biSize", wintypes.DWORD), ("biWidth", wintypes.LONG), ("biHeight", wintypes.LONG),
                    ("biPlanes", wintypes.WORD), ("biBitCount", wintypes.WORD), ("biCompression", wintypes.DWORD),
                    ("biSizeImage", wintypes.DWORD), ("biXPelsPerMeter", wintypes.LONG), ("biYPelsPerMeter", wintypes.LONG),
                    ("biClrUsed", wintypes.DWORD), ("biClrImportant", wintypes.DWORD)]

    x, y, w, h = (user32.GetSystemMetrics(i) for i in (76, 77, 78, 79))   # every monitor together
    if w <= 0 or h <= 0:
        return None
    screen = user32.GetDC(None)
    mem = gdi32.CreateCompatibleDC(screen)
    bmp = gdi32.CreateCompatibleBitmap(screen, w, h)
    old = gdi32.SelectObject(mem, bmp)
    try:
        if not gdi32.BitBlt(mem, 0, 0, w, h, screen, x, y, 0x00CC0020 | 0x40000000):   # SRCCOPY | CAPTUREBLT
            return None
        info = BITMAPINFOHEADER(40, w, -h, 1, 32, 0, 0, 0, 0, 0, 0)   # negative height: top row first
        buf = ctypes.create_string_buffer(w * h * 4 + 64)
        if gdi32.GetDIBits(mem, bmp, 0, h, buf, ctypes.byref(info), 0) != h:
            return None
    finally:
        gdi32.SelectObject(mem, old)
        gdi32.DeleteObject(bmp)
        gdi32.DeleteDC(mem)
        user32.ReleaseDC(None, screen)
    bgra = buf.raw[:w * h * 4]
    rgb = bytearray(w * h * 3)
    rgb[0::3], rgb[1::3], rgb[2::3] = bgra[2::4], bgra[1::4], bgra[0::4]
    return png_from_rgb(w, h, rgb)


def _capture_x11():
    """The whole X11 screen, read straight from the X server."""
    import ctypes
    import ctypes.util
    lib = ctypes.util.find_library("X11") or "libX11.so.6"
    x = ctypes.cdll.LoadLibrary(lib)

    class XImage(ctypes.Structure):
        _fields_ = [("width", ctypes.c_int), ("height", ctypes.c_int), ("xoffset", ctypes.c_int), ("format", ctypes.c_int),
                    ("data", ctypes.c_void_p), ("byte_order", ctypes.c_int), ("bitmap_unit", ctypes.c_int),
                    ("bitmap_bit_order", ctypes.c_int), ("bitmap_pad", ctypes.c_int), ("depth", ctypes.c_int),
                    ("bytes_per_line", ctypes.c_int), ("bits_per_pixel", ctypes.c_int),
                    ("red_mask", ctypes.c_ulong), ("green_mask", ctypes.c_ulong), ("blue_mask", ctypes.c_ulong)]
    x.XOpenDisplay.restype, x.XOpenDisplay.argtypes = ctypes.c_void_p, [ctypes.c_char_p]
    x.XDefaultRootWindow.restype, x.XDefaultRootWindow.argtypes = ctypes.c_ulong, [ctypes.c_void_p]
    x.XGetGeometry.argtypes = [ctypes.c_void_p, ctypes.c_ulong, ctypes.POINTER(ctypes.c_ulong)] + [ctypes.POINTER(ctypes.c_int)] * 2 + [ctypes.POINTER(ctypes.c_uint)] * 4
    x.XGetImage.restype = ctypes.POINTER(XImage)
    x.XGetImage.argtypes = [ctypes.c_void_p, ctypes.c_ulong, ctypes.c_int, ctypes.c_int, ctypes.c_uint, ctypes.c_uint, ctypes.c_ulong, ctypes.c_int]
    x.XCloseDisplay.argtypes = [ctypes.c_void_p]
    dpy = x.XOpenDisplay(None)
    if not dpy:
        return None
    try:
        root = x.XDefaultRootWindow(dpy)
        r, gx, gy = ctypes.c_ulong(), ctypes.c_int(), ctypes.c_int()
        w, h, bw, depth = ctypes.c_uint(), ctypes.c_uint(), ctypes.c_uint(), ctypes.c_uint()
        if not x.XGetGeometry(dpy, root, ctypes.byref(r), ctypes.byref(gx), ctypes.byref(gy), ctypes.byref(w), ctypes.byref(h), ctypes.byref(bw), ctypes.byref(depth)):
            return None
        w, h = w.value, h.value
        img = x.XGetImage(dpy, root, 0, 0, w, h, 0xFFFFFFFF, 2)   # ZPixmap
        if not img:
            return None
        im = img.contents
        if im.bits_per_pixel != 32 or im.byte_order != 0:
            return None
        raw = ctypes.string_at(im.data, im.bytes_per_line * h)
        stride = im.bytes_per_line
        packed = raw if stride == w * 4 else b"".join(raw[y * stride:y * stride + w * 4] for y in range(h))
        rgb = bytearray(w * h * 3)
        shift = {0xFF0000: 2, 0xFF00: 1, 0xFF: 0}   # where each colour sits in the 4 bytes of a pixel
        ri, gi, bi = shift.get(im.red_mask, 2), shift.get(im.green_mask, 1), shift.get(im.blue_mask, 0)
        rgb[0::3], rgb[1::3], rgb[2::3] = packed[ri::4], packed[gi::4], packed[bi::4]
        return png_from_rgb(w, h, rgb)
    finally:
        x.XCloseDisplay(dpy)


def capture_screen():
    """The whole screen as PNG bytes, or None if it can't be taken here."""
    if os.name == "nt":
        try:
            return _capture_windows()
        except Exception as e:
            print(f"Couldn't take a screenshot: {e}")
            return None
    if sys.platform.startswith("linux") and os.environ.get("DISPLAY") and os.environ.get("XDG_SESSION_TYPE") != "wayland" \
            and not os.environ.get("WAYLAND_DISPLAY"):
        try:
            shot = _capture_x11()
            if shot:
                return shot
        except Exception:
            pass
    import subprocess
    import tempfile
    fd, tmp = tempfile.mkstemp(suffix=".png")
    os.close(fd)
    try:
        if sys.platform == "darwin":
            tries = [["screencapture", "-x", "-t", "png", tmp]]
        else:
            tries = [["gnome-screenshot", "-f", tmp], ["grim", tmp], ["spectacle", "-b", "-n", "-o", tmp],
                     ["xfce4-screenshooter", "-f", "-s", tmp], ["mate-screenshot", "-f", tmp], ["maim", tmp],
                     ["scrot", "-o", tmp], ["import", "-window", "root", tmp]]
        for cmd in tries:
            if not shutil.which(cmd[0]):
                continue
            try:
                subprocess.run(cmd, timeout=15, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                data = Path(tmp).read_bytes()
                if sniff(data) == "png":
                    return data
            except (OSError, subprocess.SubprocessError):
                pass
        return None
    finally:
        try:
            os.unlink(tmp)
        except OSError:
            pass


# ---------- The logging window (server.py --log) and screenshots (server.py --screenshot) ----------
# Both save straight into journal/log, so they work whether or not the journal is running.

def ongoing_activities(acts):
    return sorted((a for a in acts if a.get("start") and not a.get("end")), key=lambda a: a["start"], reverse=True)


def stamp_label(stamp):
    """"2026-09-23T14:05" -> "14:05" today, or "Tue 22 Sep 14:05" another day."""
    try:
        d = datetime.strptime(stamp, "%Y-%m-%dT%H:%M")
    except (TypeError, ValueError):
        return ""
    return d.strftime("%H:%M") if d.date() == datetime.now().date() else d.strftime("%a %d %b %H:%M")


def screenshot_to_log():
    """server.py --screenshot: a screenshot added to the activity started most recently; with none going, the logging window opens with it."""
    dpi_aware()
    shot = capture_screen()
    if not shot:
        return show_note("Couldn't take a screenshot", SHOT_HELP)
    going = ongoing_activities(load_log())
    if not going:
        return quick_log_window(shot, taken=True)
    try:
        name = store_log_image(shot)
        if not name or not isinstance(update_activity(going[0]["id"], {"addImages": [name]}), dict):
            raise OSError
    except OSError:
        return show_note("Couldn't add the screenshot", f"Check that the journal's folder can be written to: {LOG}")
    show_note("Screenshot added", f"to \u201c{going[0].get('title') or 'Untitled'}\u201d", toast=True)


SHOT_HELP = ("This computer didn't let the journal take one. On Linux with Wayland, installing grim (Hyprland, Sway), "
             "gnome-screenshot (GNOME) or spectacle (KDE) lets it.")
TK_HELP = ("The logging window needs tkinter. On Arch or CachyOS: sudo pacman -S tk. On Ubuntu, Mint or Debian: "
           "sudo apt install python3-tk (Fedora: sudo dnf install python3-tkinter).")


def float_window(root):
    """Marks the window as a dialog, so tiling window managers (Hyprland, Sway, i3) float it over what you're
    doing instead of squeezing it in beside your other windows."""
    if sys.platform.startswith("linux"):
        try:
            root.attributes("-type", "dialog")
        except Exception:
            pass


def show_note(title, text, toast=False):
    try:
        import tkinter as tk
    except ImportError:
        print(f"{title}: {text}")
        desktop_notice(title, text)
        return
    root = tk.Tk()
    root.title(title)
    float_window(root)
    root.configure(bg="#1E2723")
    if toast:
        root.overrideredirect(True)
    root.attributes("-topmost", True)
    tk.Label(root, text=title, bg="#1E2723", fg="#F8F9F5", font=("Segoe UI", 11, "bold"), padx=18, pady=(0)).pack(anchor="w", pady=(12, 0))
    tk.Label(root, text=text, bg="#1E2723", fg="#C9CFC9", font=("Segoe UI", 10), padx=18, wraplength=320, justify="left").pack(anchor="w", pady=(2, 12))
    root.update_idletasks()
    w, h = root.winfo_reqwidth(), root.winfo_reqheight()
    if toast:
        root.geometry(f"+{root.winfo_screenwidth() - w - 24}+{root.winfo_screenheight() - h - 72}")
        root.after(1800, root.destroy)
    else:
        root.geometry(f"+{(root.winfo_screenwidth() - w) // 2}+{(root.winfo_screenheight() - h) // 3}")
        root.bind("<Key>", lambda e: root.destroy())
        root.after(6000, root.destroy)
    root.mainloop()


def desktop_notice(title, text):
    """A notification from the desktop, for when there's no tkinter to show a window with."""
    if shutil.which("notify-send"):
        import subprocess
        try:
            subprocess.run(["notify-send", "-a", "Journal", title, text], timeout=10)
        except (OSError, subprocess.SubprocessError):
            pass


def quick_log_window(shot=None, taken=False):
    """server.py --log: a small window over whatever you're doing, for logging an activity.
    A screenshot is taken first, before the window appears, so it shows what you were doing."""
    dpi_aware()
    try:
        import tkinter as tk
        from tkinter import ttk, filedialog
    except ImportError:
        print(TK_HELP)
        desktop_notice("The journal's logging window can't open", TK_HELP)
        return
    if not taken:
        shot = capture_screen()
    acts = load_log()
    import base64
    going = ongoing_activities(acts)
    ink, paper, sheet, muted, accent, rule = "#1E2723", "#F8F9F5", "#FFFFFF", "#6B746F", "#7A2E3A", "#D9DDD6"
    root = tk.Tk()
    root.title("Log an activity")
    float_window(root)
    root.configure(bg=paper)
    root.resizable(False, False)
    style = ttk.Style(root)
    try:
        style.theme_use("clam")
    except tk.TclError:
        pass
    font = ("Segoe UI", 10) if os.name == "nt" else ("Helvetica", 11)
    bold = (font[0], font[1] + 2, "bold")
    for s in ("TFrame", "TLabel", "TRadiobutton", "TCheckbutton"):
        style.configure(s, background=paper, foreground=ink, font=font)
    style.configure("Muted.TLabel", foreground=muted)
    style.configure("Err.TLabel", foreground=accent)
    style.configure("Head.TLabel", font=bold)
    style.configure("TButton", font=font, padding=(10, 3))
    style.configure("Save.TButton", foreground=paper, background=ink)
    style.map("Save.TButton", background=[("active", "#34403A")])
    f = ttk.Frame(root, padding=(18, 14, 18, 14))
    f.pack(fill="both", expand=True)
    f.columnconfigure(1, weight=1)
    ttk.Label(f, text="Log an activity", style="Head.TLabel").grid(row=0, column=0, columnspan=3, sticky="w", pady=(0, 10))

    mode = tk.StringVar(value="start")
    modes = ttk.Frame(f)
    modes.grid(row=1, column=0, columnspan=3, sticky="w", pady=(0, 8))
    ttk.Radiobutton(modes, text="Just started", value="start", variable=mode).pack(side="left", padx=(0, 16))
    ttk.Radiobutton(modes, text="Finished", value="finish", variable=mode).pack(side="left")

    which_label = ttk.Label(f, text="Which")
    NEW = "Something not logged yet"
    which = ttk.Combobox(f, state="readonly", width=44,
                         values=[NEW] + [f"{a.get('title') or 'Untitled'}  (started {stamp_label(a['start'])})" for a in going])
    which.current(0)

    ttk.Label(f, text="Title").grid(row=3, column=0, sticky="w", padx=(0, 10), pady=3)
    title = ttk.Entry(f, width=46, font=font)
    title.grid(row=3, column=1, columnspan=2, sticky="we", pady=3)
    ttk.Label(f, text="Description").grid(row=4, column=0, sticky="nw", padx=(0, 10), pady=3)
    desc = tk.Text(f, width=46, height=4, wrap="word", font=font, relief="solid", bd=1, highlightthickness=0,
                   bg=sheet, fg=ink, insertbackground=ink, padx=6, pady=4)
    desc.grid(row=4, column=1, columnspan=2, sticky="we", pady=3)

    now = lambda: datetime.now().strftime("%Y-%m-%d %H:%M")
    time_label = ttk.Label(f, text="Started at")
    time_label.grid(row=5, column=0, sticky="w", padx=(0, 10), pady=3)
    when = ttk.Entry(f, width=18, font=font)
    when.insert(0, now())
    when.grid(row=5, column=1, sticky="w", pady=3)
    ttk.Button(f, text="Now", command=lambda: (when.delete(0, "end"), when.insert(0, now()))).grid(row=5, column=2, sticky="e", pady=3)
    began_label = ttk.Label(f, text="Started at")
    began = ttk.Entry(f, width=18, font=font)
    began_hint = ttk.Label(f, text="if you know (optional)", style="Muted.TLabel")

    ttk.Label(f, text="Pictures").grid(row=7, column=0, sticky="nw", padx=(0, 10), pady=3)
    pics_box = ttk.Frame(f)
    pics_box.grid(row=7, column=1, columnspan=2, sticky="we", pady=3)
    pics = []
    pics_list = tk.Listbox(pics_box, height=3, font=font, relief="solid", bd=1, highlightthickness=0, bg=sheet, fg=ink, activestyle="none")
    pics_list.pack(side="left", fill="x", expand=True)
    pic_btns = ttk.Frame(pics_box)
    pic_btns.pack(side="left", padx=(8, 0), anchor="n")

    def add_pics():
        root.attributes("-topmost", False)
        names = filedialog.askopenfilenames(parent=root, title="Add pictures",
                                            filetypes=[("Pictures", "*.png *.jpg *.jpeg *.gif *.webp *.avif"), ("All files", "*.*")])
        root.attributes("-topmost", True)
        for n in names:
            if n not in pics:
                pics.append(n)
                pics_list.insert("end", Path(n).name)

    def remove_pic():
        for i in reversed(pics_list.curselection()):
            pics_list.delete(i)
            del pics[i]
    ttk.Button(pic_btns, text="Add\u2026", command=add_pics).pack(fill="x")
    ttk.Button(pic_btns, text="Remove", command=remove_pic).pack(fill="x", pady=(4, 0))

    use_shot = tk.BooleanVar(value=bool(shot))
    shot_touched = [False]
    shot_row = ttk.Frame(f)
    shot_row.grid(row=8, column=0, columnspan=3, sticky="we", pady=(8, 0))
    thumb = None
    if shot:
        ttk.Checkbutton(shot_row, text="Attach a screenshot of what was on the screen",
                        variable=use_shot, command=lambda: shot_touched.__setitem__(0, True)).pack(anchor="w")
        try:
            img = tk.PhotoImage(data=base64.b64encode(shot).decode("ascii"))
            k = max(1, -(-img.width() // 300))
            thumb = img.subsample(k, k)
            tk.Label(shot_row, image=thumb, bd=1, relief="solid", bg=sheet).pack(anchor="w", pady=(6, 0))
        except tk.TclError:
            pass
    else:
        ttk.Label(shot_row, text="No screenshot: " + SHOT_HELP[0].lower() + SHOT_HELP[1:], style="Muted.TLabel", wraplength=420).pack(anchor="w")

    note = ttk.Label(f, text="", style="Err.TLabel", wraplength=420)
    note.grid(row=9, column=0, columnspan=3, sticky="w", pady=(8, 0))
    btns = ttk.Frame(f)
    btns.grid(row=10, column=0, columnspan=3, sticky="e", pady=(10, 0))

    chose = [False]

    def layout(*_):
        finishing = mode.get() == "finish"
        existing = finishing and which.current() > 0
        if finishing:
            which_label.grid(row=2, column=0, sticky="w", padx=(0, 10), pady=3)
            which.grid(row=2, column=1, columnspan=2, sticky="we", pady=3)
        else:
            which_label.grid_remove(); which.grid_remove()
        time_label.configure(text="Finished at" if finishing else "Started at")
        if finishing and not existing:
            began_label.grid(row=6, column=0, sticky="w", padx=(0, 10), pady=3)
            began.grid(row=6, column=1, sticky="w", pady=3)
            began_hint.grid(row=6, column=1, columnspan=2, sticky="e", pady=3)
        else:
            began_label.grid_remove(); began.grid_remove(); began_hint.grid_remove()
        if finishing and going and not chose[0]:
            chose[0] = True   # finishing: offer the activity started most recently
            which.current(1)
            picked()
            return
        if shot and not shot_touched[0]:
            use_shot.set(not finishing)   # a screenshot goes with an activity that's starting; tick it to add one when finishing
    mode.trace_add("write", layout)

    def picked(_=None):
        i = which.current()
        if i > 0:
            a = going[i - 1]
            title.delete(0, "end"); title.insert(0, a.get("title", ""))
            desc.delete("1.0", "end"); desc.insert("1.0", a.get("description", ""))
        layout()
    which.bind("<<ComboboxSelected>>", picked)

    def read_stamp(text, needed):
        text = text.strip()
        if not text:
            return None if needed else ""
        for fmt in ("%Y-%m-%d %H:%M", "%Y-%m-%dT%H:%M", "%H:%M"):
            try:
                d = datetime.strptime(text, fmt)
            except ValueError:
                continue
            if fmt == "%H:%M":
                d = datetime.combine(datetime.now().date(), d.time())
            return d.strftime("%Y-%m-%dT%H:%M")
        return None

    def save(_=None):
        finishing = mode.get() == "finish"
        existing = going[which.current() - 1] if finishing and which.current() > 0 else None
        name = " ".join(title.get().split())
        if not name:
            note.configure(text="Give it a title.")
            title.focus_set()
            return "break"
        t = read_stamp(when.get(), True)
        if not t:
            note.configure(text="Write the time like 2026-09-23 14:05 (or just 14:05 for today).")
            when.focus_set()
            return "break"
        t0 = read_stamp(began.get(), False) if finishing and not existing else ""
        if t0 is None:
            note.configure(text="Write the start time like 2026-09-23 14:05, or leave it empty.")
            return "break"
        note.configure(text="Saving\u2026")
        root.update_idletasks()
        try:
            datas = []
            for p in pics:
                data = Path(p).read_bytes()
                if not sniff(data) or len(data) > MAX_IMAGE:
                    note.configure(text=f"{Path(p).name} isn't a picture the journal can keep (PNG, JPEG, GIF, WebP or AVIF).")
                    return "break"
                datas.append(data)
            if shot and use_shot.get():
                datas.append(shot)
            names = [store_log_image(d) for d in datas]
            text = desc.get("1.0", "end").rstrip()
            if existing:
                done = update_activity(existing["id"], {"title": name, "description": text, "end": t, "addImages": names})
            else:
                done = create_activity({"title": name, "description": text, "images": names,
                                        "start": t0 if finishing else t, "end": t if finishing else ""})
            if not isinstance(done, dict):
                erase_unused_log_images(names, load_log())
                note.configure(text="That activity isn't in the log any more." if done == "missing" else "The journal didn't accept that.")
                return "break"
        except OSError as e:
            note.configure(text=f"Couldn't save it: {e}")
            return "break"
        root.destroy()
        return "break"

    ttk.Button(btns, text="Cancel", command=root.destroy).pack(side="left", padx=(0, 8))
    ttk.Button(btns, text="Save", style="Save.TButton", command=save).pack(side="left")
    title.bind("<Return>", save)
    when.bind("<Return>", save)
    began.bind("<Return>", save)
    desc.bind("<Control-Return>", save)
    root.bind("<Escape>", lambda e: root.destroy())
    layout()

    root.update_idletasks()
    w, h = root.winfo_reqwidth(), root.winfo_reqheight()
    root.geometry(f"+{(root.winfo_screenwidth() - w) // 2}+{max(20, (root.winfo_screenheight() - h) // 3)}")
    root.attributes("-topmost", True)
    root.lift()
    root.after(80, lambda: (root.focus_force(), title.focus_set()))
    root.mainloop()


class Handler(BaseHTTPRequestHandler):
    server_version = "Journal"

    def log_message(self, *args):
        pass  # keep the terminal quiet

    def refuse(self, code=403):
        self.send_response(code)
        self.send_header("Content-Length", "0")
        self.end_headers()

    def safe(self, write=False):
        # Only accept requests addressed to this computer, and require a custom
        # header on API calls so other websites open in your browser can't use it.
        if self.headers.get("Host") not in ALLOWED_HOSTS:
            return False
        if write or self.path.startswith("/api/"):
            return self.headers.get("X-Journal") == "1"
        return True

    def send(self, code, body, ctype, cache="no-store", frame="DENY"):
        data = body.encode("utf-8") if isinstance(body, str) else body
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", cache)
        self.send_header("Cross-Origin-Resource-Policy", "same-origin")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", frame)   # PDFs may be shown in a frame on the journal's own page
        self.end_headers()
        self.wfile.write(data)

    def read_json(self, limit):
        """The request's JSON object, or None if it's missing, too big or not an object."""
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length > limit:
                return None
            data = json.loads(self.rfile.read(length).decode("utf-8"))
        except (ValueError, UnicodeDecodeError):
            return None
        return data if isinstance(data, dict) else None

    def item(self, kind, pattern):
        parts = self.path.split("?")[0].split("/")
        if len(parts) == 4 and parts[1] == "api" and parts[2] == kind and pattern.match(parts[3]):
            return parts[3]
        return None

    def entry_id(self):
        return self.item("entries", ID_RE)

    def do_GET(self):
        if not self.safe():
            return self.refuse()
        path = self.path.split("?")[0]
        if path in ("/", "/index.html"):
            return self.send(200, PAGE, "text/html; charset=utf-8")
        if path == "/api/settings":
            try:
                data = clean_settings(json.loads(SETTINGS.read_text(encoding="utf-8")))
            except (OSError, ValueError):
                data = {}
            return self.send(200, json.dumps(data), "application/json")
        if path == "/api/topics":
            try:
                data = clean_topics(json.loads(TOPICS.read_text(encoding="utf-8")))
            except (OSError, ValueError):
                data = []
            return self.send(200, json.dumps(data), "application/json")
        if path == "/api/changed":
            with lock:
                return self.send(200, json.dumps(sorted(load_links())), "application/json")
        if path == "/api/entries":
            out = {}
            with lock:
                for p in ENTRIES.glob("*.md"):
                    if ID_RE.match(p.stem):
                        try:
                            out[p.stem] = read_entry(p)
                        except (OSError, UnicodeDecodeError):
                            pass
            return self.send(200, json.dumps(out), "application/json")
        if path == "/api/quotes":
            with lock:
                return self.send(200, json.dumps(quote_listing()), "application/json")
        if path == "/api/archive":
            with lock:
                return self.send(200, json.dumps(archive_listing()), "application/json")
        if path == "/api/log":
            with lock:
                acts = load_log()
            shortcuts = dict(hotkeys["state"], log=helper_command("--log"), screenshot=helper_command("--screenshot"))
            return self.send(200, json.dumps({"activities": acts, "shortcuts": shortcuts}, ensure_ascii=False), "application/json")
        if path.startswith("/log/images/"):
            name = path.rsplit("/", 1)[1]
            if IMG_RE.match(name) and (LOG_IMAGES / name).is_file():
                return self.send(200, (LOG_IMAGES / name).read_bytes(), IMG_TYPES[name.rsplit(".", 1)[1]], "private, max-age=31536000, immutable")
        # /api/book-drafts/<code>: a book model saved as a draft, to carry on with
        if path.startswith("/api/book-drafts/"):
            code = path.rsplit("/", 1)[1]
            if DRAFT_RE.match(code) and (BOOK_DRAFTS / f"{code}.json").is_file():
                return self.send(200, (BOOK_DRAFTS / f"{code}.json").read_bytes(), "application/json")
            return self.refuse(404)
        # /api/pdfjs: pdf.js made ready (downloaded the first time), for reading a PDF as a book
        if path == "/api/pdfjs":
            ok = ensure_pdfjs()
            return self.send(200 if ok else 503, json.dumps({"ok": ok}), "application/json")
        # /pdfjs/<folder>/<file>: pdf.js itself, and the fonts, character maps and decoders it uses
        if path.startswith("/pdfjs/"):
            rel = path[len("/pdfjs/"):]
            if PDFJS_FILE_RE.match(rel) and (rel in PDFJS_BUILD or rel.split("/")[0] in PDFJS_DIRS) and (PDFJS / rel).is_file():
                ctype = PDFJS_TYPES.get(rel.rsplit(".", 1)[-1], "application/octet-stream")
                return self.send(200, (PDFJS / rel).read_bytes(), ctype, "private, max-age=86400")
            return self.refuse(404)
        # /pdfs/<name>: a PDF from an entry, shown in the browser's own PDF reader (in a frame on the page, or a tab)
        if path.startswith("/pdfs/"):
            name = path.rsplit("/", 1)[1]
            if PDF_RE.match(name) and (PDFS / name).is_file():
                return self.send(200, (PDFS / name).read_bytes(), "application/pdf", "private, max-age=31536000, immutable", "SAMEORIGIN")
            return self.send(404, MISSING_PDF, "text/html; charset=utf-8", "no-store", "SAMEORIGIN")
        if path.startswith("/models/"):
            name = path.rsplit("/", 1)[1]
            if MODEL_RE.match(name) and (MODELS / name).is_file():
                return self.send(200, (MODELS / name).read_bytes(), "model/gltf-binary", "private, max-age=31536000, immutable")
        if path.startswith("/archive/models/"):
            name = path.rsplit("/", 1)[1]
            with lock:
                file = find_archived_model(name)
            if file:
                return self.send(200, file.read_bytes(), "model/gltf-binary", "no-store")
        if path.startswith("/images/") or path.startswith("/archive/images/"):
            name = path.rsplit("/", 1)[1]
            if path.startswith("/images/"):
                file = IMAGES / name
            else:
                with lock:
                    file = find_archived_image(name) if IMG_RE.match(name) else None
            if IMG_RE.match(name) and file and file.is_file():
                ctype = IMG_TYPES[name.rsplit(".", 1)[1]]
                return self.send(200, file.read_bytes(), ctype, "private, max-age=31536000, immutable")
        self.refuse(404)

    def do_POST(self):
        if not self.safe(write=True):
            return self.refuse()
        parts = self.path.split("?")[0].split("/")
        # /api/images/<new>/replaces/<old>: a drawing now stands in for <old>
        if len(parts) == 6 and parts[1:3] == ["api", "images"] and parts[4] == "replaces" \
                and IMG_RE.match(parts[3]) and IMG_RE.match(parts[5]):
            new, old = parts[3], parts[5]
            with lock:
                links = load_links()
                # Every earlier version is kept, each linked to the one before it.
                ORIGINALS.mkdir(exist_ok=True)
                if (IMAGES / old).exists():
                    os.replace(IMAGES / old, ORIGINALS / old)
                links[new] = old
                save_links(links)
            return self.send(200, "{}", "application/json")
        # /api/archive/entries/<id>/restore: bring an archived entry back into the journal
        if len(parts) == 6 and parts[1:4] == ["api", "archive", "entries"] and parts[5] == "restore" and ID_RE.match(parts[4]):
            with lock:
                ok = restore_entry(parts[4])
            return self.send(200, "{}", "application/json") if ok else self.refuse(409)
        # /api/archive/images/<name>/restore: an archived picture dragged into an entry comes back into the journal
        if len(parts) == 6 and parts[1:4] == ["api", "archive", "images"] and parts[5] == "restore" and IMG_RE.match(parts[4]):
            with lock:
                done = restore_archived_image(parts[4])
            if not done:
                return self.refuse(404)
            return self.send(200, json.dumps({"name": done[0], "copied": done[1]}), "application/json")
        # /api/images/<name>/restore: go back one version, erasing the current one
        if len(parts) == 5 and parts[1:3] == ["api", "images"] and parts[4] == "restore" and IMG_RE.match(parts[3]):
            name = parts[3]
            with lock:
                links = load_links()
                original = links.get(name)
                if not original or not (ORIGINALS / original).exists():
                    return self.refuse(404)
                os.replace(ORIGINALS / original, IMAGES / original)
                (IMAGES / name).unlink(missing_ok=True)   # the drawn-on version is erased for good
                del links[name]
                save_links(links)
            return self.send(200, json.dumps({"name": original, "changed": original in links}), "application/json")
        # /api/log/images: a picture for an activity in the Log
        if self.path.split("?")[0] == "/api/log/images":
            try:
                length = int(self.headers.get("Content-Length", "0"))
            except ValueError:
                return self.refuse(400)
            if length > MAX_IMAGE:
                return self.refuse(413)
            name = store_log_image(self.rfile.read(length))
            if not name:
                return self.refuse(415)
            return self.send(200, json.dumps({"name": name}), "application/json")
        # /api/log/activities: a new activity in the Log
        if self.path.split("?")[0] == "/api/log/activities":
            data = self.read_json(200_000)
            if data is None:
                return self.refuse(400)
            with lock:
                try:
                    act = create_activity(data)
                except OSError as e:
                    print(f"Couldn't save the log: {e}")
                    return self.refuse(500)
            if not act:
                return self.refuse(400)
            return self.send(200, json.dumps(act, ensure_ascii=False), "application/json")
        # /api/zooms: a frozen zoom frame saved as a picture, under a plain dated name
        if self.path.split("?")[0] == "/api/zooms":
            try:
                length = int(self.headers.get("Content-Length", "0"))
            except ValueError:
                return self.refuse(400)
            if length > MAX_IMAGE:
                return self.refuse(413)
            data = self.rfile.read(length)
            if sniff(data) != "png":
                return self.refuse(415)
            stamp = datetime.now().strftime("%Y-%m-%d %H.%M.%S")
            with lock:
                IMAGES.mkdir(exist_ok=True)
                name, n = f"Zoom {stamp}.png", 2
                while (IMAGES / name).exists():
                    name, n = f"Zoom {stamp} ({n}).png", n + 1
                with open(IMAGES / name, "wb") as f:
                    f.write(data)
            return self.send(200, json.dumps({"name": name}), "application/json")
        # /api/export: the open entry, sent as blocks, written as journal/exports/<title>.pdf
        if self.path.split("?")[0] == "/api/export":
            data = self.read_json(MAX_EXPORT)
            if data is None:
                return self.refuse(400)
            try:
                path = export_pdf(data)
            except RuntimeError:
                return self.send(500, json.dumps({"error": "font"}), "application/json")
            except (OSError, ValueError, TypeError, KeyError, struct.error) as err:
                print("Export failed:", err, file=sys.stderr)
                return self.send(500, json.dumps({"error": "write"}), "application/json")
            return self.send(200, json.dumps({"file": path.name, "folder": str(path.parent)}), "application/json")
        # /api/quotes: writing saved from a web page with the browser extension ("Add to quote archive")
        if self.path.split("?")[0] == "/api/quotes":
            try:
                length = int(self.headers.get("Content-Length", "0"))
                if length > MAX_QUOTE * 4 + 1000:
                    return self.refuse(413)
                data = json.loads(self.rfile.read(length).decode("utf-8"))
            except (ValueError, UnicodeDecodeError):
                return self.refuse(400)
            text = clean_quote_text(data.get("text") if isinstance(data, dict) else None)
            if text is None:
                return self.refuse(400)
            with lock:
                name = save_quote(text, data.get("source"))
            return self.send(200, json.dumps({"name": name}), "application/json")
        # Folders in the archive's Images: make, rename, delete (when empty), and move things into them
        if parts[1:4] == ["api", "archive", "folders"] or self.path.split("?")[0] == "/api/archive/move":
            try:
                length = int(self.headers.get("Content-Length", "0"))
                if length > 200_000:
                    return self.refuse(413)
                data = json.loads(self.rfile.read(length).decode("utf-8") or "{}")
                if not isinstance(data, dict):
                    raise ValueError
            except (ValueError, UnicodeDecodeError):
                return self.refuse(400)
            action = parts[4] if len(parts) == 5 else ("move" if parts[3] == "move" else "make" if len(parts) == 4 else None)
            root = ARCHIVE_MODELS if data.get("kind") == "models" else ARCHIVE_IMAGES   # the Models tab has its own folders
            try:
                with lock:
                    if action == "make":
                        done = make_archive_folder(data.get("parent", ""), data.get("name"), root)
                        return self.send(200, json.dumps({"path": done}), "application/json") if done else self.refuse(400)
                    if action == "rename":
                        done = rename_archive_folder(data.get("path"), data.get("name"), root)
                        if done is False:
                            return self.refuse(409)
                        return self.send(200, json.dumps({"path": done}), "application/json") if done else self.refuse(400)
                    if action == "delete":
                        done = delete_archive_folder(data.get("path"), root)
                        if done is False:
                            return self.refuse(409)
                        return self.send(200, "{}", "application/json") if done else self.refuse(400)
                    if action == "move":
                        imgs, dirs = data.get("models" if root == ARCHIVE_MODELS else "images", []), data.get("folders", [])
                        if not isinstance(imgs, list) or not isinstance(dirs, list):
                            return self.refuse(400)
                        done = move_in_archive(imgs[:1000], dirs[:1000], data.get("to", ""), root)
                        return self.send(200, json.dumps({"moved": done}), "application/json") if done is not None else self.refuse(400)
            except OSError as e:
                print(f"Couldn't change the archive's folders: {e}")
                return self.refuse(500)
            return self.refuse(404)
        # /api/archive/tasks: finished tasks archived from the Tasks menu
        if self.path.split("?")[0] == "/api/archive/tasks":
            try:
                length = int(self.headers.get("Content-Length", "0"))
                if length > 5_000_000:
                    return self.refuse(413)
                data = json.loads(self.rfile.read(length).decode("utf-8"))
                incoming = data.get("tasks") if isinstance(data, dict) else None
                if not isinstance(incoming, list) or not incoming or len(incoming) > 5000:
                    raise ValueError
            except (ValueError, UnicodeDecodeError):
                return self.refuse(400)
            cleaned = [clean_archived_task(t) for t in incoming]
            if any(c is None for c in cleaned):
                return self.refuse(400)
            with lock:
                tasks = load_archived_tasks()
                taken = {t["id"] for t in tasks}
                for c in cleaned:
                    c["id"] = secrets.token_hex(8)
                    while c["id"] in taken:
                        c["id"] = secrets.token_hex(8)
                    taken.add(c["id"])
                try:
                    save_archived_tasks(tasks + cleaned)
                except OSError as e:
                    print(f"Couldn't archive tasks: {e}")
                    return self.refuse(500)
            return self.send(200, json.dumps({"tasks": cleaned}, ensure_ascii=False), "application/json")
        # /api/archive/images: a picture saved from a web page with the browser extension goes straight into the archive
        if self.path.split("?")[0] == "/api/archive/images":
            try:
                length = int(self.headers.get("Content-Length", "0"))
            except ValueError:
                return self.refuse(400)
            if length > MAX_IMAGE:
                return self.refuse(413)
            data = self.rfile.read(length)
            ext = sniff(data)
            if not ext:
                return self.refuse(415)
            name = f"{secrets.token_hex(16)}.{ext}"
            with lock:
                ARCHIVE_IMAGES.mkdir(parents=True, exist_ok=True)
                with open(ARCHIVE_IMAGES / name, "wb") as f:
                    f.write(data)
            return self.send(200, json.dumps({"name": name}), "application/json")
        # /api/models/<n>/archive: a model taken off the right of its entry, into the archive's Models
        if len(parts) == 5 and parts[1:3] == ["api", "models"] and parts[4] == "archive" and MODEL_RE.match(parts[3]):
            with lock:
                done = archive_model(parts[3])
            return self.send(200, "{}", "application/json") if done else self.refuse(404)
        # /api/archive/models/<n>/restore: an archived model back into journal/models, for the open entry
        if len(parts) == 6 and parts[1:4] == ["api", "archive", "models"] and parts[5] == "restore" and MODEL_RE.match(parts[4]):
            with lock:
                done = restore_archived_model(parts[4])
            return self.send(200, json.dumps({"name": done}), "application/json") if done else self.refuse(404)
        # /api/pdfs: a PDF to put in an entry
        if self.path.split("?")[0] == "/api/pdfs":
            try:
                length = int(self.headers.get("Content-Length", "0"))
            except ValueError:
                return self.refuse(400)
            if length > MAX_PDF:
                return self.refuse(413)
            data = self.rfile.read(length)
            if b"%PDF-" not in data[:1024]:
                return self.refuse(415)
            name = f"{secrets.token_hex(16)}.pdf"
            PDFS.mkdir(exist_ok=True)
            tmp = PDFS / f".{name}.tmp"
            with open(tmp, "wb") as f:
                f.write(data)
            os.replace(tmp, PDFS / name)
            return self.send(200, json.dumps({"name": name}), "application/json")
        # /api/models: a 3D model (a binary glTF file) to show on the right of an entry
        if self.path.split("?")[0] == "/api/models":
            try:
                length = int(self.headers.get("Content-Length", "0"))
            except ValueError:
                return self.refuse(400)
            if length > MAX_MODEL:
                return self.refuse(413)
            data = self.rfile.read(length)
            if len(data) < 20 or data[:4] != b"glTF" or struct.unpack_from("<I", data, 4)[0] != 2:
                return self.refuse(415)
            name = f"{secrets.token_hex(16)}.glb"
            MODELS.mkdir(exist_ok=True)
            tmp = MODELS / f".{name}.tmp"
            with open(tmp, "wb") as f:
                f.write(data)
            os.replace(tmp, MODELS / name)
            return self.send(200, json.dumps({"name": name}), "application/json")
        if self.path.split("?")[0] != "/api/images":
            return self.refuse(404)
        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            return self.refuse(400)
        if length > MAX_IMAGE:
            return self.refuse(413)
        data = self.rfile.read(length)
        ext = sniff(data)
        if not ext:
            return self.refuse(415)
        name = f"{secrets.token_hex(16)}.{ext}"
        IMAGES.mkdir(exist_ok=True)
        with open(IMAGES / name, "wb") as f:
            f.write(data)
        self.send(200, json.dumps({"name": name}), "application/json")

    def do_PUT(self):
        if not self.safe(write=True):
            return self.refuse()
        # /api/book-drafts/<code>: a book model saved as a draft (the photos it uses stay in the entry)
        code = self.item("book-drafts", DRAFT_RE)
        if code:
            data = self.read_json(MAX_DRAFT)
            if data is None:
                return self.refuse(400)
            with lock:
                BOOK_DRAFTS.mkdir(parents=True, exist_ok=True)
                tmp = BOOK_DRAFTS / f".{code}.tmp"
                tmp.write_text(json.dumps(data), encoding="utf-8")
                replace_file(tmp, BOOK_DRAFTS / f"{code}.json")
            return self.send(200, "{}", "application/json")
        if self.path.split("?")[0] == "/api/settings":
            try:
                length = int(self.headers.get("Content-Length", "0"))
                if length > 20_000:
                    return self.refuse(413)
                data = json.loads(self.rfile.read(length).decode("utf-8"))
                if not isinstance(data, dict):
                    raise ValueError
            except (ValueError, UnicodeDecodeError):
                return self.refuse(400)
            with lock:
                tmp = FOLDER / ".settings.tmp"
                tmp.write_text(json.dumps(clean_settings(data), indent=2), encoding="utf-8")
                replace_file(tmp, SETTINGS)
            hotkeys_changed()   # the Log shortcuts may have changed
            return self.send(200, "{}", "application/json")
        if self.path.split("?")[0] == "/api/topics":
            try:
                length = int(self.headers.get("Content-Length", "0"))
                if length > 200_000:
                    return self.refuse(413)
                data = json.loads(self.rfile.read(length).decode("utf-8"))
            except (ValueError, UnicodeDecodeError):
                return self.refuse(400)
            with lock:
                FOLDER.mkdir(exist_ok=True)
                tmp = FOLDER / ".topics.tmp"
                tmp.write_text(json.dumps(clean_topics(data), indent=2, ensure_ascii=False), encoding="utf-8")
                replace_file(tmp, TOPICS)
            return self.send(200, "{}", "application/json")
        # /api/log/activities/<id>: an activity in the Log changed (finished, edited, a picture added)
        parts = self.path.split("?")[0].split("/")
        if len(parts) == 5 and parts[1:4] == ["api", "log", "activities"]:
            if not LOG_ID_RE.match(parts[4]):
                return self.refuse(404)
            data = self.read_json(200_000)
            if data is None:
                return self.refuse(400)
            with lock:
                try:
                    changed = update_activity(parts[4], data)
                except OSError as e:
                    print(f"Couldn't save the log: {e}")
                    return self.refuse(500)
            if changed == "missing":
                return self.refuse(404)
            if not changed:
                return self.refuse(400)
            return self.send(200, json.dumps(changed, ensure_ascii=False), "application/json")
        entry_id = self.entry_id()
        if not entry_id:
            return self.refuse(404)
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length > 5_000_000:
                return self.refuse(413)
            data = json.loads(self.rfile.read(length).decode("utf-8"))
            if not isinstance(data, dict):
                raise ValueError
        except (ValueError, UnicodeDecodeError):
            return self.refuse(400)
        with lock:
            try:
                write_entry(entry_id, data)
            except OSError as e:
                print(f"Couldn't save an entry ({entry_id}.md): {e}")
                return self.refuse(500)
        self.send(200, "{}", "application/json")

    def do_DELETE(self):
        if not self.safe(write=True):
            return self.refuse()
        parts = self.path.split("?")[0].split("/")
        # /api/book-drafts/<code>: a draft thrown away, or made into a model
        code = self.item("book-drafts", DRAFT_RE)
        if code:
            with lock:
                (BOOK_DRAFTS / f"{code}.json").unlink(missing_ok=True)
            return self.send(200, "{}", "application/json")
        # /api/pdfs/<n>: a PDF deleted for good, once it's been taken out of the entry (kept if another entry has it)
        if len(parts) == 4 and parts[1:3] == ["api", "pdfs"] and PDF_RE.match(parts[3]):
            with lock:
                kept = bool(erase_unused_pdfs({parts[3]}))
            return self.send(200, json.dumps({"kept": kept}), "application/json")
        # /api/models/<n>: a model deleted for good from the right of an entry
        if len(parts) == 4 and parts[1:3] == ["api", "models"] and MODEL_RE.match(parts[3]):
            with lock:
                (MODELS / parts[3]).unlink(missing_ok=True)
            return self.send(200, "{}", "application/json")
        # /api/archive/models/<n>: an archived model deleted for good
        if len(parts) == 5 and parts[1:4] == ["api", "archive", "models"] and MODEL_RE.match(parts[4]):
            with lock:
                found = find_archived_model(parts[4])
                if found:
                    found.unlink(missing_ok=True)
            return self.send(200, "{}", "application/json")
        if len(parts) == 5 and parts[1:4] == ["api", "archive", "images"] and IMG_RE.match(parts[4]):
            with lock:
                erase_archived_image(parts[4])
            return self.send(200, "{}", "application/json")
        # /api/log/activities/<id>: an activity taken out of the Log, with its pictures
        if len(parts) == 5 and parts[1:4] == ["api", "log", "activities"] and LOG_ID_RE.match(parts[4]):
            with lock:
                try:
                    done = delete_activity(parts[4])
                except OSError as e:
                    print(f"Couldn't save the log: {e}")
                    return self.refuse(500)
            return self.send(200, "{}", "application/json") if done else self.refuse(404)
        # /api/log/images/<name>: a picture added to the logging form and then taken off before saving
        if len(parts) == 5 and parts[1:4] == ["api", "log", "images"] and IMG_RE.match(parts[4]):
            with lock, log_file_lock():
                erase_unused_log_images([parts[4]], load_log())
            return self.send(200, "{}", "application/json")
        # /api/archive/tasks/<id>: an archived task is taken out of the archive (to put it back, or for good)
        if len(parts) == 5 and parts[1:4] == ["api", "archive", "tasks"] and TASK_ID_RE.match(parts[4]):
            with lock:
                tasks = load_archived_tasks()
                gone = next((t for t in tasks if t["id"] == parts[4]), None)
                if not gone:
                    return self.refuse(404)
                try:
                    save_archived_tasks([t for t in tasks if t is not gone])
                except OSError as e:
                    print(f"Couldn't change the archived tasks: {e}")
                    return self.refuse(500)
            return self.send(200, json.dumps(gone, ensure_ascii=False), "application/json")
        if len(parts) == 5 and parts[1:4] == ["api", "archive", "entries"] and ID_RE.match(parts[4]):
            with lock:
                src = ARCHIVE_ENTRIES / f"{parts[4]}.md"
                if src.exists():
                    pdfs = set()
                    try:
                        entry = read_entry(src)
                        pdfs = entry_pdfs(entry)
                        for name in entry_pictures(entry):
                            erase_archived_image(name)
                    except (OSError, UnicodeDecodeError):
                        pass
                    src.unlink()
                    erase_unused_pdfs(pdfs)
            return self.send(200, "{}", "application/json")
        # /api/quotes/<file name>: delete a quote (entries that have it keep their own copy)
        if len(parts) == 4 and parts[1:3] == ["api", "quotes"]:
            with lock:
                done = delete_quote(unquote(parts[3]))
            return self.send(200, "{}", "application/json") if done else self.refuse(404)
        forever = "forever=1" in self.path.partition("?")[2].split("&")
        image = self.item("images", IMG_RE)
        if image:
            with lock:
                discard_image(image, forever)
            return self.send(200, "{}", "application/json")
        entry_id = self.entry_id()
        if not entry_id:
            return self.refuse(404)
        with lock:
            src = ENTRIES / f"{entry_id}.md"
            if src.exists():
                pdfs = set()
                try:
                    entry = read_entry(src)
                    pdfs = entry_pdfs(entry)
                    for name in entry_pictures(entry):
                        discard_image(name, forever)
                except (OSError, UnicodeDecodeError):
                    pass
                discard(src, forever, ARCHIVE_ENTRIES)
                if forever:
                    erase_unused_pdfs(pdfs)   # archived, an entry's PDFs stay in journal/pdfs
        self.send(200, "{}", "application/json")


# ---------- Exporting an entry as a PDF ----------
# The Menu's "Export as PDF" sends the open entry, laid out as blocks (writing, pictures, quotes, task lists, the
# days parts were written on), and the text of every entry it links to. This writes it as a PDF in journal/exports,
# named by the entry's title. The entry itself isn't touched. It's all done here, with nothing but Python:
# the writing is set in Spectral (the journal's own typeface), kept in journal/fonts; if it isn't there, it's
# downloaded once from Google Fonts, and failing that the computer's own serif font is used.
EXPORTS = FOLDER / "exports"
FONTS = FOLDER / "fonts"
MAX_EXPORT = 800_000_000   # bytes in the request (pictures included)
SPECTRAL_URL = "https://raw.githubusercontent.com/google/fonts/main/ofl/spectral/Spectral-{}.ttf"
PDF_W, PDF_H = 595.28, 841.89   # A4, in points
PDF_MARGIN_X, PDF_MARGIN_TOP, PDF_MARGIN_BOTTOM = 70.0, 72.0, 76.0
PDF_BODY = 10.0   # the size of the writing
PDF_LEAD = 1.62   # line height, as a multiple of the size
INK = (0.118, 0.153, 0.137)
MUTED = (0.42, 0.45, 0.44)
ACCENT = (0.478, 0.180, 0.227)
FAINT = (0.66, 0.68, 0.67)   # "Tasks" over a list of tasks: the ink, as if faded
PDF_PICTURE = 33   # every picture is made this tall, as a % of the page (less only if it'd be wider than the page)
PDF_MARK = 3.3   # a linked entry's name, raised after a word
PDF_NOTE = 7.2   # the linked entries at the end are set this small…
PDF_NOTE_BLANK = 0.2   # …with an empty line between paragraphs only this fraction of a line
PDF_NOTE_NAME = 9.4   # and each one's name, in front of it
# The sizes the Menu can change (in points, the picture as a % of the page): the setting, its default and range.
PDF_SIZES = {"body": ("exportBody", PDF_BODY, 6, 16), "mark": ("exportMark", PDF_MARK, 2, 12),
             "note": ("exportNote", PDF_NOTE, 4, 16), "note_name": ("exportNoteName", PDF_NOTE_NAME, 4, 24),
             "picture_size": ("exportPicture", PDF_PICTURE, 15, 90)}


class TTFont:
    """What the PDF needs from a TrueType font file: its glyphs for each character, their widths, and its size lines."""

    def __init__(self, path):
        data = Path(path).read_bytes()
        if data[:4] not in (b"\x00\x01\x00\x00", b"true"):
            raise ValueError("not a TrueType font")
        tables = {}
        for i in range(struct.unpack(">H", data[4:6])[0]):
            tag, _, off, length = struct.unpack(">4sIII", data[12 + 16 * i:28 + 16 * i])
            tables[tag.decode("latin-1")] = data[off:off + length]
        if "glyf" not in tables:
            raise ValueError("no TrueType outlines")
        self.path, self.data = str(path), data
        head, hhea = tables["head"], tables["hhea"]
        self.upem = struct.unpack(">H", head[18:20])[0] or 1000
        self.bbox = [v * 1000 / self.upem for v in struct.unpack(">hhhh", head[36:44])]
        asc, desc = struct.unpack(">hh", hhea[4:8])
        self.ascent, self.descent = asc * 1000 / self.upem, desc * 1000 / self.upem
        count = struct.unpack(">H", tables["maxp"][4:6])[0]
        nhm = max(1, struct.unpack(">H", hhea[34:36])[0])
        hmtx = tables["hmtx"]
        adv = [struct.unpack(">H", hmtx[4 * i:4 * i + 2])[0] for i in range(min(nhm, len(hmtx) // 4))] or [self.upem // 2]
        self.adv = adv + [adv[-1]] * max(0, count - len(adv))
        os2 = tables.get("OS/2", b"")
        self.cap = struct.unpack(">h", os2[88:90])[0] * 1000 / self.upem if len(os2) >= 90 else self.ascent * 0.7
        post = tables.get("post", b"")
        self.italic = struct.unpack(">i", post[4:8])[0] / 65536 if len(post) >= 8 else 0
        self.name = self._name(tables.get("name", b"")) or Path(path).stem
        self.cmap = self._cmap(tables["cmap"])

    @staticmethod
    def _name(t):
        if len(t) < 6:
            return None
        count, strings = struct.unpack(">HH", t[2:6])
        for i in range(count):
            pid, eid, lid, nid, length, off = struct.unpack(">HHHHHH", t[6 + 12 * i:18 + 12 * i])
            if nid == 6:
                raw = t[strings + off:strings + off + length]
                s = raw.decode("utf-16-be", "ignore") if pid in (0, 3) else raw.decode("latin-1")
                s = re.sub(r"[^A-Za-z0-9_+-]", "", s)
                if s:
                    return s[:60]
        return None

    @staticmethod
    def _cmap(t):
        subs = {}
        for i in range(struct.unpack(">H", t[2:4])[0]):
            pid, eid, off = struct.unpack(">HHI", t[4 + 8 * i:12 + 8 * i])
            subs[(pid, eid)] = off
        out = {}
        for key in ((3, 10), (0, 6), (0, 4), (3, 1), (0, 3), (0, 2), (0, 1), (0, 0)):
            if key not in subs:
                continue
            off = subs[key]
            fmt = struct.unpack(">H", t[off:off + 2])[0]
            if fmt == 12:
                for g in range(struct.unpack(">I", t[off + 12:off + 16])[0]):
                    start, end, gid = struct.unpack(">III", t[off + 16 + 12 * g:off + 28 + 12 * g])
                    for c in range(start, min(end, 0x10FFFF) + 1):
                        out.setdefault(c, gid + c - start)
                return out
            if fmt == 4:
                seg = struct.unpack(">H", t[off + 6:off + 8])[0]
                ends, starts = off + 14, off + 16 + seg
                deltas, ranges = starts + seg, starts + 2 * seg
                for s in range(seg // 2):
                    end = struct.unpack(">H", t[ends + 2 * s:ends + 2 * s + 2])[0]
                    start = struct.unpack(">H", t[starts + 2 * s:starts + 2 * s + 2])[0]
                    delta = struct.unpack(">h", t[deltas + 2 * s:deltas + 2 * s + 2])[0]
                    ro = struct.unpack(">H", t[ranges + 2 * s:ranges + 2 * s + 2])[0]
                    for c in range(start, end + 1):
                        if c == 0xFFFF:
                            continue
                        if ro:
                            at = ranges + 2 * s + ro + 2 * (c - start)
                            g = struct.unpack(">H", t[at:at + 2])[0] if at + 2 <= len(t) else 0
                            g = (g + delta) & 0xFFFF if g else 0
                        else:
                            g = (c + delta) & 0xFFFF
                        if g:
                            out.setdefault(c, g)
                return out
        return out


_font_cache = {}
_font_download_failed = [0.0]


def _load_font(path):
    path = str(path)
    if path not in _font_cache:
        try:
            _font_cache[path] = TTFont(path)
        except (OSError, ValueError, struct.error, IndexError):
            _font_cache[path] = None
    return _font_cache[path]


def _spectral(style):
    """Spectral in journal/fonts, downloading it there first if it isn't (tried again at most every 10 minutes)."""
    p = FONTS / f"Spectral-{style}.ttf"
    if not p.exists() and time.time() - _font_download_failed[0] > 600:
        try:
            import urllib.request
            with urllib.request.urlopen(SPECTRAL_URL.format(style), timeout=10) as r:
                data = r.read(5_000_000)
            if data[:4] != b"\x00\x01\x00\x00":
                raise ValueError("not a font")
            FONTS.mkdir(parents=True, exist_ok=True)
            tmp = FONTS / f".{p.name}.{secrets.token_hex(4)}.tmp"
            tmp.write_bytes(data)
            os.replace(tmp, p)
        except Exception:
            _font_download_failed[0] = time.time()
    return _load_font(p) if p.exists() else None


def _system_fonts(pattern):
    """TrueType fonts on this computer matching a fontconfig pattern like "serif:bold", best first."""
    found = []
    try:
        import subprocess
        out = subprocess.run(["fc-match", "-s", "-f", "%{file}\n", pattern], capture_output=True, text=True, timeout=10).stdout
        found = [line for line in out.splitlines()[:12] if line.lower().endswith(".ttf")]
    except (OSError, ValueError, Exception):
        pass
    bold, italic = ":bold" in pattern, ":italic" in pattern
    name = "georgia" + ("z" if bold and italic else "b" if bold else "i" if italic else "")
    for d in (Path(os.environ.get("WINDIR", "C:/Windows")) / "Fonts", Path("/System/Library/Fonts/Supplemental"), Path("/Library/Fonts")):
        found += [str(d / f"{name}.ttf"), str(d / ("Georgia" + (" Bold" if bold else "") + (" Italic" if italic else "") + ".ttf"))]
    for p in ("/usr/share/fonts/TTF/DejaVuSerif" + ("-Bold" if bold else "-Italic" if italic else "") + ".ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSerif" + ("-Bold" if bold else "-Italic" if italic else "") + ".ttf"):
        found.append(p)
    return [f for f in (_load_font(p) for p in found if Path(p).exists()) if f]


def export_fonts():
    """For each style (r regular, b bold, i italic): the fonts to try, in order, for each character."""
    out = {}
    for key, style, pattern in (("r", "Regular", "serif"), ("b", "Bold", "serif:bold"), ("i", "Italic", "serif:italic")):
        chain = [f for f in [_spectral(style)] if f] + _system_fonts(pattern)
        seen, uniq = set(), []
        for f in chain:
            if f.path not in seen:
                seen.add(f.path); uniq.append(f)
        out[key] = uniq
    if not out["r"]:
        raise RuntimeError("no font")
    return out


def jpeg_info(data):
    """Width, height, colour channels, whether it's an Adobe CMYK one, and its EXIF orientation (1 to 8)."""
    if data[:2] != b"\xff\xd8":
        return None
    i, size, adobe, orient = 2, None, False, 1
    while i + 4 <= len(data):
        if data[i] != 0xFF:
            i += 1; continue
        m = data[i + 1]
        if m in (0xD8, 0x01) or 0xD0 <= m <= 0xD7 or m == 0xFF:
            i += 1 if m == 0xFF else 2; continue
        length = struct.unpack(">H", data[i + 2:i + 4])[0]
        seg = data[i + 4:i + 2 + length]
        if m == 0xEE and seg[:5] == b"Adobe":
            adobe = True
        elif m == 0xE1 and seg[:6] == b"Exif\x00\x00":
            orient = _exif_orientation(seg[6:]) or 1
        elif 0xC0 <= m <= 0xCF and m not in (0xC4, 0xC8, 0xCC):
            h, w, n = struct.unpack(">HHB", seg[1:6])
            size = (w, h, n)
            break
        i += 2 + length
    if not size or size[2] not in (1, 3, 4) or not size[0] or not size[1]:
        return None
    return size[0], size[1], size[2], adobe, orient


def _exif_orientation(t):
    try:
        e = "<" if t[:2] == b"II" else ">"
        ifd = struct.unpack(e + "I", t[4:8])[0]
        for k in range(struct.unpack(e + "H", t[ifd:ifd + 2])[0]):
            at = ifd + 2 + 12 * k
            if struct.unpack(e + "H", t[at:at + 2])[0] == 0x0112:
                v = struct.unpack(e + "H", t[at + 8:at + 10])[0]
                return v if 1 <= v <= 8 else 1
    except struct.error:
        pass
    return 1


def pdf_str(s):
    """A PDF text string that keeps any character: UTF-16 with its byte-order mark, as hex."""
    return "<FEFF" + s.encode("utf-16-be").hex().upper() + ">"


class PdfExport:
    def __init__(self, fonts, sizes=None):
        self.fonts = fonts
        sizes = sizes if isinstance(sizes, dict) else {}
        for attr, (key, default, lo, hi) in PDF_SIZES.items():
            v = sizes.get(key)
            setattr(self, attr, min(hi, max(lo, float(v))) if isinstance(v, (int, float)) and not isinstance(v, bool) else default)
        self.fake_bold = not fonts["b"]
        self.used = {}   # font path -> {glyph id: the characters it stands for}
        self.font_ids = {}   # font path -> its name in the pages ("F1"…)
        self.pages = []   # each: list of drawing operations
        self.images = []   # [(name "Im1", object bytes, stream bytes)]
        self.page_images = []   # each page: set of the image names on it
        self.width = PDF_W - 2 * PDF_MARGIN_X
        self.bottom = PDF_H - PDF_MARGIN_BOTTOM
        self._pick_cache = {}
        self.blank = 1.0   # how much of a line an empty line takes
        self.new_page()

    # ---- characters and fonts ----
    def pick(self, ch, kind):
        key = (ch, kind)
        hit = self._pick_cache.get(key)
        if hit is None:
            chain = self.fonts[kind] or self.fonts["r"]
            cp = ord(ch)
            hit = next(((f, f.cmap[cp]) for f in chain if cp in f.cmap), None)
            if hit is None:
                hit = next(((f, f.cmap[cp]) for f in self.fonts["r"] if cp in f.cmap), (chain[0], 0))
            self._pick_cache[key] = hit
        return hit

    def char_width(self, ch, st):
        f, g = self.pick(ch, st["f"])
        return f.adv[g] * st["size"] / f.upem if g < len(f.adv) else st["size"] * 0.5

    def text_width(self, s, st):
        return sum(self.char_width(c, st) for c in s)

    # ---- pages ----
    def new_page(self):
        self.ops = []
        self.pages.append(self.ops)
        self.page_images.append(set())
        self.y = PDF_MARGIN_TOP

    def ensure(self, h):
        if self.y + h > self.bottom and self.y > PDF_MARGIN_TOP + 0.5:
            self.new_page()

    def draw_text(self, x, baseline, s, st):
        """Writing in one style, starting at x, with its baseline this far down the page."""
        runs, cur, font = [], [], None
        for ch in s:
            f, g = self.pick(ch, st["f"])
            if f is not font and cur:
                runs.append((font, cur)); cur = []
            font = f
            cur.append((g, ch))
        if cur:
            runs.append((font, cur))
        r, g_, b = st.get("color", INK)
        for f, glyphs in runs:
            fid = self.font_ids.setdefault(f.path, "F%d" % (len(self.font_ids) + 1))
            used = self.used.setdefault(f.path, {})
            for gid, ch in glyphs:
                used.setdefault(gid, ch)
            hexs = "".join("%04X" % gid for gid, _ in glyphs)
            y = PDF_H - baseline + st.get("rise", 0)
            bold = "2 Tr %.3f w %.3f %.3f %.3f RG " % (st["size"] * 0.03, r, g_, b) if st["f"] == "b" and (self.fake_bold or f not in self.fonts["b"]) else "0 Tr "
            self.ops.append("BT /%s %.2f Tf %.3f %.3f %.3f rg %s%.2f %.2f Td <%s> Tj ET" % (fid, st["size"], r, g_, b, bold, x, y, hexs))
            x += sum(f.adv[gid] * st["size"] / f.upem for gid, _ in glyphs if gid < len(f.adv))
        return x

    def line(self, x0, y0, x1, y1, width, color):
        self.ops.append("%.3f %.3f %.3f RG %.2f w %.2f %.2f m %.2f %.2f l S" % (color + (width, x0, PDF_H - y0, x1, PDF_H - y1)))

    def rect_fill(self, x, y, w, h, color):
        self.ops.append("%.3f %.3f %.3f rg %.2f %.2f %.2f %.2f re f" % (color + (x, PDF_H - y - h, w, h)))

    # ---- laying out writing ----
    def style(self, size=None, f="r", **kw):
        st = {"size": self.body if size is None else size, "f": f}
        st.update(kw)
        return st

    def chars_for(self, runs, base):
        """A line's runs as characters, each [character, style, width]. A None character is a gap: space that
        isn't a place to break the line and has nothing drawn in it."""
        out = []
        for r in runs:
            if "mark" in r:   # a linked entry's name, in bold capitals, raised after the word like a footnote mark
                size = r["size"] if isinstance(r.get("size"), (int, float)) else self.mark
                st = self.style(size, "b", nb=True, **({"rise": base["size"] * 0.5} if r.get("up", True) else {}))
                out += [[c, st, self.char_width(c, st)] for c in " ".join(str(r["mark"]).split()).upper()[:200]]
            elif "sub" in r:
                st = self.style(base["size"] * 1.02, "b", color=ACCENT)
                out += [[c, st, self.char_width(c, st)] for c in str(r["sub"])[:20]]
                out.append([None, st, base["size"] * 0.4])
            elif "indent" in r:
                st = self.style(base["size"] * 1.02, "b")
                out.append([None, st, self.text_width(str(r["indent"])[:20], st) + base["size"] * 0.4])
            else:
                st = dict(base)
                if r.get("b"):
                    st["f"] = "b"
                elif r.get("i"):
                    st["f"] = "i"
                if r.get("u"):
                    st["u"] = True
                for c in str(r.get("s", "")):
                    if c == "\t":
                        out += [[" ", st, self.char_width(" ", st)] for _ in range(4)]
                    elif c == "\u00a0":
                        out.append([" ", st, self.char_width(" ", st)])
                    elif c >= " " and not ("\u200b" <= c <= "\u200f") and c != "\ufeff":
                        out.append([c, st, self.char_width(c, st)])
        return out

    @staticmethod
    def wrap(chars, width):
        """Breaks a line of characters into lines no wider than width, between words where it can."""
        tokens, cur = [], []
        for c in chars:
            space = c[0] == " " and not c[1].get("nb")   # the spaces in a raised name don't break the line
            if cur and (cur[0][0] == " " and not cur[0][1].get("nb")) != space:
                tokens.append(cur); cur = []
            cur.append(c)
        if cur:
            tokens.append(cur)
        lines, line, w, pending = [], [], 0.0, []
        for tok in tokens:
            tw = sum(c[2] for c in tok)
            if tok[0][0] == " " and not tok[0][1].get("nb"):
                if line or not lines:
                    pending = tok
                continue
            pw = sum(c[2] for c in pending)
            if line and w + pw + tw > width:
                lines.append(line); line, w, pending, pw = [], 0.0, [], 0.0
            if not line and tw > width:   # a word too long for a line: broken where it has to be
                if pending and not lines:
                    line, w = list(pending), pw
                for c in tok:
                    if line and w + c[2] > width:
                        lines.append(line); line, w = [], 0.0
                    line.append(c); w += c[2]
                pending = []
                continue
            line += pending + tok
            w += pw + tw
            pending = []
        if line or not lines:
            lines.append(line + ([] if line else pending))
        return lines

    def draw_line(self, chars, x, top, lead):
        """One laid-out line, its top this far down the page."""
        size = max([c[1]["size"] for c in chars if c[0] is not None and "rise" not in c[1]] or [self.body])
        baseline = top + (lead + size * 0.68) / 2
        i = 0
        while i < len(chars):
            st = chars[i][1]
            j = i
            while j < len(chars) and chars[j][1] is st and chars[j][0] is not None:
                j += 1
            if j == i:   # a gap
                x += chars[i][2]; i += 1; continue
            s = "".join(c[0] for c in chars[i:j])
            w = sum(c[2] for c in chars[i:j])
            if s.strip():
                self.draw_text(x, baseline, s, st)
            if st.get("u"):
                uw = sum(c[2] for c in chars[i:j][:len(s.rstrip())]) if j == len(chars) else w   # not under spaces ending the line
                self.line(x, baseline + st["size"] * 0.13, x + uw, baseline + st["size"] * 0.13, st["size"] * 0.055, st.get("color", INK))
            x += w
            i = j

    def paragraph(self, runs, base=None, x=None, width=None, first_indent=0.0):
        """Writing: its runs split into lines where it has line breaks, and each of those wrapped to the width."""
        base = base or self.style()
        x = PDF_MARGIN_X if x is None else x
        width = self.width if width is None else width
        lead = base["size"] * PDF_LEAD
        for hard in self.split_lines(runs):
            chars = self.chars_for(hard, base)
            for line in self.wrap(chars, width):
                if not line:   # an empty line, between paragraphs
                    self.y += lead * self.blank; continue
                self.ensure(lead)
                self.draw_line(line, x, self.y, lead)
                self.y += lead

    @staticmethod
    def split_lines(runs):
        """Runs split at their line breaks: a list of lines, each a list of runs."""
        lines = [[]]
        for r in runs:
            if not isinstance(r, dict):
                continue
            if "s" in r and not ("mark" in r or "sub" in r or "indent" in r):
                parts = str(r["s"]).replace("\r\n", "\n").replace("\r", "\n").split("\n")
                for k, part in enumerate(parts):
                    if k:
                        lines.append([])
                    if part:
                        lines[-1].append(dict(r, s=part))
            else:
                lines[-1].append(r)
        return lines

    # ---- blocks ----
    def blocks(self, blocks, pics, size=None):
        size = self.body if size is None else size
        for b in blocks if isinstance(blocks, list) else []:
            if not isinstance(b, dict):
                continue
            t = b.get("t")
            if t == "text":
                self.paragraph(b.get("runs") or [], self.style(size))
            elif t == "img":
                self.picture(b, pics)
            elif t == "quote":
                self.quote(str(b.get("s", "")), size)
            elif t == "day":
                self.day(str(b.get("s", "")), size)
            elif t == "tasks":
                self.tasks(b.get("items") or [], size)

    def day(self, s, size):
        st = self.style(size * 0.8, "i", color=MUTED)
        self.y += size * 0.9
        self.paragraph([{"s": s}], st)
        self.y += size * 0.3

    def quote(self, text, size):
        """A quote: in italics, between quotation marks."""
        text = text.strip("\n")
        self.y += size * 0.9
        self.paragraph([{"s": "\u201c" + text + "\u201d"}], self.style(size, "i"))
        self.y += size * 0.9

    def tasks(self, items, size):
        base = self.style(size)
        lead = size * PDF_LEAD
        box, indent = size * 0.78, size * 1.7
        self.y += size * 0.5
        if len([it for it in items if isinstance(it, dict)]) > 1:
            label = self.style(size * 0.85, "r", color=FAINT)
            self.ensure(size * 0.85 * PDF_LEAD + lead)
            self.paragraph([{"s": "Tasks"}], label)
        for it in items if isinstance(items, list) else []:
            if not isinstance(it, dict):
                continue
            state = it.get("state")
            st = dict(base, color=MUTED) if state in ("x", "-") else base
            lines = []
            for hard in self.split_lines(it.get("runs") or []):
                lines += self.wrap(self.chars_for(hard, st), self.width - indent)
            self.ensure(lead)
            top = self.y + (lead - box) / 2 + size * 0.06
            x0 = PDF_MARGIN_X + 1
            self.ops.append("%.3f %.3f %.3f RG 0.9 w %.2f %.2f %.2f %.2f re S" % (MUTED + (x0, PDF_H - top - box, box, box)))
            if state == "x":
                self.ops.append("%.3f %.3f %.3f RG 1.3 w 1 J 1 j %.2f %.2f m %.2f %.2f l %.2f %.2f l S 0 J 0 j" % (
                    INK + (x0 + box * 0.2, PDF_H - top - box * 0.52, x0 + box * 0.42, PDF_H - top - box * 0.76, x0 + box * 0.82, PDF_H - top - box * 0.24)))
            elif state == "-":
                self.line(x0 + box * 0.22, top + box / 2, x0 + box * 0.78, top + box / 2, 1.2, MUTED)
            for k, line in enumerate(lines or [[]]):
                if k:
                    self.ensure(lead)
                if line:
                    self.draw_line(line, PDF_MARGIN_X + indent, self.y, lead)
                self.y += lead
            self.y += size * 0.25
        self.y += size * 0.4

    def picture(self, b, pics):
        """A picture on its own, as big as the page allows (never more than 3 times its own size)."""
        img = self.image(b, pics)
        if not img:
            return
        name, w, h, orient = img
        dw, dh = (h, w) if orient >= 5 else (w, h)
        cap = str(b.get("cap") or "").strip()
        cap_st = self.style(self.body * 0.8, "i", color=MUTED)
        cap_h = self.body * 0.8 * PDF_LEAD * 2 + 4 if cap else 0
        scale = min(PDF_H * self.picture_size / 100 / dh, self.width / dw, (self.bottom - PDF_MARGIN_TOP - cap_h - 30) / dh)
        W, H = dw * scale, dh * scale
        self.y += 10
        self.ensure(H + cap_h)
        x, y = PDF_MARGIN_X + (self.width - W) / 2, PDF_H - self.y - H
        m = {1: (W, 0, 0, H, x, y), 2: (-W, 0, 0, H, x + W, y), 3: (-W, 0, 0, -H, x + W, y + H), 4: (W, 0, 0, -H, x, y + H),
             5: (0, -H, -W, 0, x + W, y + H), 6: (0, -H, W, 0, x, y + H), 7: (0, H, W, 0, x, y), 8: (0, H, -W, 0, x + W, y)}[orient]
        self.ops.append("q %.3f %.3f %.3f %.3f %.3f %.3f cm /%s Do Q" % (m + (name,)))
        self.page_images[-1].add(name)
        self.y += H
        if cap:
            self.y += 4
            for line in self.wrap(self.chars_for([{"s": cap.replace("\n", " ")}], cap_st), self.width)[:2]:
                lw = sum(c[2] for c in line)
                self.draw_line(line, PDF_MARGIN_X + (self.width - lw) / 2, self.y, cap_st["size"] * PDF_LEAD)
                self.y += cap_st["size"] * PDF_LEAD
        self.y += 12

    def image(self, b, pics):
        """The picture's image in the PDF (added the first time it's used): (its name, width, height, orientation)."""
        key = str(b.get("name", ""))
        if not hasattr(self, "_imgs"):
            self._imgs = {}
        if key in self._imgs:
            return self._imgs[key]
        found = None
        if key.endswith(".jpg") and IMG_RE.match(key) and (IMAGES / key).is_file():
            data = (IMAGES / key).read_bytes()
            info = jpeg_info(data)
            if info:
                w, h, n, adobe, orient = info
                space = {1: "/DeviceGray", 3: "/DeviceRGB", 4: "/DeviceCMYK"}[n]
                decode = " /Decode [1 0 1 0 1 0 1 0]" if n == 4 and adobe else ""
                found = (w, h, orient, "/Width %d /Height %d /ColorSpace %s /BitsPerComponent 8 /Filter /DCTDecode%s" % (w, h, space, decode), data)
        if not found:
            p = pics.get(key) if isinstance(pics, dict) else None
            try:
                w, h = int(p["w"]), int(p["h"])
                data = base64.b64decode(p["data"], validate=True)
                if not (0 < w <= 20000 and 0 < h <= 20000) or len(zlib.decompress(data, bufsize=w * h * 3)) != w * h * 3:
                    raise ValueError
                found = (w, h, 1, "/Width %d /Height %d /ColorSpace /DeviceRGB /BitsPerComponent 8 /Filter /FlateDecode" % (w, h), data)
            except (TypeError, KeyError, ValueError, zlib.error, base64.binascii.Error):
                found = None
        if not found:
            self._imgs[key] = None
            return None
        w, h, orient, dict_, data = found
        name = "Im%d" % (len(self.images) + 1)
        self.images.append((name, dict_, data))
        self._imgs[key] = (name, w, h, orient)
        return self._imgs[key]

    def heading(self, runs, size, gap_after):
        self.paragraph(runs, self.style(size))
        self.y += gap_after

    def page_numbers(self):
        st = self.style(PDF_BODY * 0.75, color=MUTED)   # the page numbers stay the same size
        if len(self.pages) < 2:
            return
        for n, ops in enumerate(self.pages, 1):
            self.ops = ops
            s = str(n)
            self.draw_text((PDF_W - self.text_width(s, st)) / 2, PDF_H - PDF_MARGIN_BOTTOM / 2 + 4, s, st)

    # ---- the file ----
    def build(self, title):
        objs = []   # object number - 1 -> bytes

        def add(body):
            objs.append(body)
            return len(objs)

        def stream(dict_, data, compress=True):
            if compress:
                data = zlib.compress(data, 6)
                dict_ += " /Filter /FlateDecode"
            return b"<< " + dict_.encode("latin-1") + b" /Length %d >>\nstream\n" % len(data) + data + b"\nendstream"

        catalog, pages_id = add(b""), add(b"")
        font_objs = {}
        by_path = {f.path: f for chain in self.fonts.values() for f in chain}
        for path, fid in self.font_ids.items():
            f, used = by_path[path], self.used.get(path, {})
            ff = add(stream("/Length1 %d" % len(f.data), f.data))
            flags = 32 | 2 | (64 if f.italic else 0)
            desc = add(("<< /Type /FontDescriptor /FontName /%s /Flags %d /FontBBox [%d %d %d %d] /ItalicAngle %.2f /Ascent %d /Descent %d "
                        "/CapHeight %d /StemV 80 /FontFile2 %d 0 R >>" % ((f.name, flags) + tuple(int(v) for v in f.bbox) +
                                                                       (f.italic, f.ascent, f.descent, f.cap, ff))).encode("latin-1"))
            widths = " ".join("%d [%d]" % (g, round(f.adv[g] * 1000 / f.upem)) for g in sorted(used) if g < len(f.adv))
            cid = add(("<< /Type /Font /Subtype /CIDFontType2 /BaseFont /%s /CIDSystemInfo << /Registry (Adobe) /Ordering (Identity) /Supplement 0 >> "
                       "/FontDescriptor %d 0 R /CIDToGIDMap /Identity /DW 500 /W [%s] >>" % (f.name, desc, widths)).encode("latin-1"))
            maps = ["<%04X> <%s>" % (g, ch.encode("utf-16-be").hex().upper()) for g, ch in sorted(used.items())]
            cmap = ("/CIDInit /ProcSet findresource begin 12 dict begin begincmap /CIDSystemInfo << /Registry (Adobe) /Ordering (UCS) /Supplement 0 >> def "
                    "/CMapName /Adobe-Identity-UCS def /CMapType 2 def 1 begincodespacerange <0000> <FFFF> endcodespacerange\n")
            for k in range(0, len(maps), 100):
                chunk = maps[k:k + 100]
                cmap += "%d beginbfchar\n%s\nendbfchar\n" % (len(chunk), "\n".join(chunk))
            cmap += "endcmap CMapName currentdict /CMap defineresource pop end end"
            tu = add(stream("", cmap.encode("latin-1")))
            font_objs[fid] = add(("<< /Type /Font /Subtype /Type0 /BaseFont /%s /Encoding /Identity-H /DescendantFonts [%d 0 R] /ToUnicode %d 0 R >>"
                                  % (f.name, cid, tu)).encode("latin-1"))
        img_objs = {name: add(stream("/Type /XObject /Subtype /Image " + d, data, compress=False)) for name, d, data in self.images}
        fonts = " ".join("/%s %d 0 R" % (k, v) for k, v in font_objs.items())
        kids = []
        for ops, imgs in zip(self.pages, self.page_images):
            content = add(stream("", "\n".join(ops).encode("latin-1")))
            xo = " ".join("/%s %d 0 R" % (n, img_objs[n]) for n in sorted(imgs))
            res = "<< /Font << %s >>%s >>" % (fonts, " /XObject << %s >>" % xo if xo else "")
            kids.append(add(("<< /Type /Page /Parent %d 0 R /MediaBox [0 0 %.2f %.2f] /Resources %s /Contents %d 0 R >>"
                             % (pages_id, PDF_W, PDF_H, res, content)).encode("latin-1")))
        objs[pages_id - 1] = ("<< /Type /Pages /Kids [%s] /Count %d >>" % (" ".join("%d 0 R" % k for k in kids), len(kids))).encode("latin-1")
        objs[catalog - 1] = ("<< /Type /Catalog /Pages %d 0 R /ViewerPreferences << /DisplayDocTitle true >> >>" % pages_id).encode("latin-1")
        now = datetime.now().strftime("D:%Y%m%d%H%M%S")
        info = add(("<< /Title %s /Producer (Journal) /CreationDate (%s) >>" % (pdf_str(title), now)).encode("latin-1"))
        out = bytearray(b"%PDF-1.7\n%\xe2\xe3\xcf\xd3\n")
        offsets = []
        for n, body in enumerate(objs, 1):
            offsets.append(len(out))
            out += b"%d 0 obj\n" % n + body + b"\nendobj\n"
        xref = len(out)
        out += b"xref\n0 %d\n0000000000 65535 f \n" % (len(objs) + 1)
        out += b"".join(b"%010d 00000 n \n" % o for o in offsets)
        out += b"trailer\n<< /Size %d /Root %d 0 R /Info %d 0 R >>\nstartxref\n%d\n%%%%EOF\n" % (len(objs) + 1, catalog, info, xref)
        return bytes(out)


def export_file_name(title):
    """A file name made from the entry's title: characters no system allows in a name are swapped for dashes."""
    name = re.sub(r'[\x00-\x1f\x7f/\\:*?"<>|]', "-", str(title or "")).strip().strip(".").strip()
    name = re.sub(r"\s+", " ", name)[:150].rstrip(". ") or "Untitled"
    if name.split(".")[0].upper() in {"CON", "PRN", "AUX", "NUL"} | {f"COM{i}" for i in range(1, 10)} | {f"LPT{i}" for i in range(1, 10)}:
        name += " (entry)"
    return name + ".pdf"


def export_pdf(data):
    """Writes the entry sent from the page as journal/exports/<title>.pdf. Returns the file's path."""
    doc = PdfExport(export_fonts(), data.get("sizes"))
    pics = data.get("pics") if isinstance(data.get("pics"), dict) else {}
    title = str(data.get("title") or "").strip() or "Untitled"
    doc.paragraph([{"s": title}], doc.style(24, "r"))
    created = str(data.get("created") or "").strip()
    if created:
        doc.y += 2
        doc.paragraph([{"s": created}], doc.style(doc.body * 0.8, "i", color=MUTED))
    doc.y += 22
    doc.blocks(data.get("main"), pics)
    notes = [n for n in data.get("notes") or [] if isinstance(n, dict)]
    for k, n in enumerate(notes):
        if k == 0:
            doc.new_page()
        else:
            doc.y += doc.note * 1.2
        # The linked entry's name, as it's shown in the writing, starts the entry's first line: "NAME The entry…"
        name = " ".join((str(n.get("title") or "").strip() or "Untitled").split())
        lead_in = [{"mark": name, "up": False, "size": doc.note_name}, {"s": " "}]
        blocks = [b for b in (n.get("blocks") if isinstance(n.get("blocks"), list) else []) if isinstance(b, dict)]
        if n.get("missing"):
            blocks = [{"t": "text", "runs": [{"s": "This entry is no longer in the journal.", "i": True}]}]
        if blocks and blocks[0].get("t") == "text" and isinstance(blocks[0].get("runs"), list):
            blocks[0] = dict(blocks[0], runs=lead_in + blocks[0]["runs"])
        else:
            blocks.insert(0, {"t": "text", "runs": lead_in[:1]})
        doc.blank = PDF_NOTE_BLANK
        doc.blocks(blocks, pics, doc.note)
        doc.blank = 1.0
    doc.page_numbers()
    pdf = doc.build(title)
    EXPORTS.mkdir(parents=True, exist_ok=True)
    path = EXPORTS / export_file_name(title)
    tmp = EXPORTS / f".{secrets.token_hex(6)}.tmp"
    tmp.write_bytes(pdf)
    os.replace(tmp, path)
    return path


# ---------- Quotes ----------
def clean_source(value):
    """The page a quote came from: its web address (http or https only) and title."""
    if not isinstance(value, dict):
        return None
    url = value.get("url") if isinstance(value.get("url"), str) else ""
    title = value.get("title") if isinstance(value.get("title"), str) else ""
    url, title = url.strip()[:2000], " ".join(title.split())[:300]
    if not re.match(r"^https?://", url, re.I):
        url = ""
    return {"url": url, "title": title} if url or title else None


def load_sources():
    try:
        data = json.loads(QUOTE_SOURCES.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except (OSError, ValueError):
        return {}


def save_sources(data):
    QUOTES.mkdir(parents=True, exist_ok=True)
    tmp = QUOTES / f".sources.{secrets.token_hex(4)}.tmp"
    tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    os.replace(tmp, QUOTE_SOURCES)


def quote_file(name):
    """The quote file with this name, if it's really one in journal/quotes."""
    if not isinstance(name, str) or not name.endswith(".txt") or name.startswith(".") or "/" in name or "\\" in name or "\x00" in name:
        return None
    p = QUOTES / name
    return p if p.parent == QUOTES and p.is_file() else None


def delete_quote(name):
    p = quote_file(name)
    if not p:
        return False
    p.unlink()
    sources = load_sources()
    if sources.pop(name, None) is not None:
        save_sources(sources)
    return True


def save_quote(text, source=None):
    """Keeps a quote as its own text file in journal/quotes, named by when it was saved. Returns the name."""
    text = text.replace("\r\n", "\n").replace("\r", "\n").strip("\n")
    stamp = datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    QUOTES.mkdir(parents=True, exist_ok=True)
    name, n = f"{stamp}.txt", 2
    while (QUOTES / name).exists():
        name, n = f"{stamp} ({n}).txt", n + 1
    tmp = QUOTES / f".{name}.tmp"
    tmp.write_text(text + "\n", encoding="utf-8", newline="\n")
    os.replace(tmp, QUOTES / name)   # shows up only once it's complete
    source = clean_source(source)
    if source:
        sources = load_sources()
        sources[name] = source
        save_sources(sources)
    return name


def quote_listing():
    """Every quote in journal/quotes, newest first. Any .txt file put in that folder by hand counts too."""
    out, sources = [], load_sources()
    for p in QUOTES.glob("*.txt") if QUOTES.exists() else []:
        if p.name.startswith(".") or not p.is_file():
            continue
        try:
            if p.stat().st_size > 2_000_000:
                continue
            text = p.read_text(encoding="utf-8-sig", errors="replace").replace("\r\n", "\n").replace("\r", "\n").strip("\n")
        except OSError:
            continue
        if text.strip():
            item = {"name": p.name, "text": text, "saved": int(p.stat().st_mtime * 1000)}
            source = clean_source(sources.get(p.name))
            if source:
                item["source"] = source
            out.append(item)
    out.sort(key=lambda q: (-q["saved"], q["name"]))
    return out


def clean_quote_text(value):
    if not isinstance(value, str):
        return None
    value = value.replace("\x00", "")
    return value if value.strip() and len(value) <= MAX_QUOTE else None


# ---------- The browser extension for saving pictures from web pages ----------
# It adds "Save to journal archive" to the menu you get by right-clicking a picture, and sends the picture
# to this server, which puts it in the archive. The files are written out each time the journal starts.
EXT_MANIFEST = {
    "manifest_version": 3,
    "name": "Save to journal archive",
    "version": "1.4",
    "description": "Right-click a picture, or some selected writing, and save it straight into your journal.",
    "permissions": ["contextMenus", "notifications", "scripting", "nativeMessaging"],
    "host_permissions": ["<all_urls>"],
    # Firefox runs "scripts"; Chrome, Edge and Brave run "service_worker". Each ignores the other.
    "background": {"scripts": ["background.js"], "service_worker": "background.js"},
    # Firefox needs a fixed name for the extension, to keep it and to sign it.
    "browser_specific_settings": {"gecko": {
        "id": EXTENSION_ID,
        "strict_min_version": "142.0",
        "data_collection_permissions": {"required": ["none"]},
    }},
    "icons": {"48": "icon48.png", "128": "icon128.png"},
}
EXT_BACKGROUND = r"""
const JOURNAL = 'http://127.0.0.1:__PORT__';
const MENU_ID = 'save-to-journal-archive';
const QUOTE_ID = 'add-to-quote-archive';
const FIREFOX = typeof browser !== 'undefined';
const api = FIREFOX ? browser : chrome;

async function makeMenu(){
  await api.contextMenus.removeAll();
  api.contextMenus.create({id: MENU_ID, title: 'Save to journal archive', contexts: ['image']});
  api.contextMenus.create({id: QUOTE_ID, title: 'Add to quote archive', contexts: ['selection']});
}
api.runtime.onInstalled.addListener(makeMenu);
api.runtime.onStartup.addListener(makeMenu);

function tell(title, message){
  api.notifications.create({type: 'basic', iconUrl: api.runtime.getURL('icon128.png'), title, message});
}

// The kinds of picture the journal keeps, worked out from the file's first bytes.
function kindOf(bytes){
  const b = new Uint8Array(bytes.slice(0, 16)), s = (i, n) => String.fromCharCode(...b.slice(i, i + n));
  if (b[0] === 0x89 && s(1, 3) === 'PNG') return 'png';
  if (b[0] === 0xff && b[1] === 0xd8 && b[2] === 0xff) return 'jpg';
  if (s(0, 6) === 'GIF87a' || s(0, 6) === 'GIF89a') return 'gif';
  if (s(0, 4) === 'RIFF' && s(8, 4) === 'WEBP') return 'webp';
  if (s(4, 4) === 'ftyp' && (s(8, 4) === 'avif' || s(8, 4) === 'avis')) return 'avif';
  return null;
}

// A picture made on the page itself (a "blob:" address) can only be read from inside that page.
async function readFromPage(tabId, frameId, url){
  const [res] = await api.scripting.executeScript({
    target: {tabId, frameIds: [frameId || 0]},
    args: [url],
    func: async src => {
      const blob = await (await fetch(src)).blob();
      return await new Promise((ok, fail) => {
        const r = new FileReader(); r.onload = () => ok(r.result); r.onerror = fail; r.readAsDataURL(blob);
      });
    },
  });
  return await (await fetch(res.result)).arrayBuffer();
}

async function getPicture(info, tab){
  const url = info.srcUrl;
  if (url.startsWith('blob:')) return readFromPage(tab.id, info.frameId, url);
  const r = await fetch(url, {credentials: 'include'});
  if (!r.ok) throw new Error('fetch');
  return await r.arrayBuffer();
}

async function toBase64(bytes){
  const url = await new Promise((ok, fail) => {
    const r = new FileReader(); r.onload = () => ok(r.result); r.onerror = fail; r.readAsDataURL(new Blob([bytes]));
  });
  return url.slice(url.indexOf(',') + 1);
}

// Pictures in other formats (like BMP or ICO) are turned into PNG so the journal can keep them.
async function asPng(bytes){
  const bmp = await createImageBitmap(new Blob([bytes]));
  const canvas = new OffscreenCanvas(bmp.width, bmp.height);
  canvas.getContext('2d').drawImage(bmp, 0, 0);
  return await (await canvas.convertToBlob({type: 'image/png'})).arrayBuffer();
}

api.contextMenus.onClicked.addListener((info, tab) => {
  const run = info.menuItemId === QUOTE_ID ? saveQuote : info.menuItemId === MENU_ID && info.srcUrl ? save : null;
  if (!run) return;
  if (!FIREFOX) return run(info, tab);
  // Firefox may not yet have let the extension read web pages (or reach the journal):
  // ask once, right away while it still counts as your click. Once allowed, it doesn't ask again.
  api.permissions.request({origins: ['<all_urls>']}).then(ok => {
    if (ok || run === saveQuote) run(info, tab);   // a quote can still be saved from what the menu was given
    else tell("Couldn't save the picture", 'The extension needs permission to fetch pictures from websites. Allow it in Add-ons and themes, under this extension\u2019s Permissions.');
  }, () => run(info, tab));
});

/* ---------- Quotes: selected writing, kept as it's laid out on the page (line breaks included) ---------- */
async function selectedWriting(info, tab){
  try {
    const [res] = await api.scripting.executeScript({
      target: {tabId: tab.id, frameIds: [info.frameId || 0]},
      func: () => {
        const el = document.activeElement;   // writing selected inside a text box
        if (el && (el.tagName === 'TEXTAREA' || (el.tagName === 'INPUT' && /^(text|search|url|email)$/i.test(el.type)))
            && el.selectionStart !== el.selectionEnd) return el.value.slice(el.selectionStart, el.selectionEnd);
        return String(window.getSelection());
      },
    });
    if (res && typeof res.result === 'string' && res.result.trim()) return res.result;
  } catch (e) { /* some pages (like the browser's own) can't be read: use what the menu was given */ }
  return info.selectionText || '';
}

async function saveQuote(info, tab){
  const source = {url: info.pageUrl || (tab && tab.url) || '', title: (tab && tab.title) || ''};
  const text = (await selectedWriting(info, tab)).replace(/\r\n?/g, '\n').replace(/\u00a0/g, ' ').replace(/[ \t]+\n/g, '\n').replace(/^\n+|\s+$/g, '');
  if (!text) return tell("Couldn't save the quote", 'No writing was selected.');
  if (text.length > 200000) return tell("Couldn't save the quote", 'That selection is too long for one quote.');
  try {
    const reply = await api.runtime.sendNativeMessage('__HELPER__', {kind: 'quote', text, source});
    if (reply && reply.ok) return tell('Added to quote archive', 'It\u2019s in the journal, under Quotes.');
  } catch (e) { /* no helper: try the running journal instead */ }
  try {
    const r = await fetch(JOURNAL + '/api/quotes', {method: 'POST', headers: {'X-Journal': '1', 'Content-Type': 'application/json'}, body: JSON.stringify({text, source})});
    if (!r.ok) throw new Error('server');
    tell('Added to quote archive', 'It\u2019s in the journal, under Quotes.');
  } catch (e) {
    tell("Couldn't save the quote", FIREFOX
      ? 'Firefox couldn\u2019t reach the journal. Start server.py once (it sets up saving without the journal open), then try again.'
      : 'The journal isn\u2019t running. Start server.py, then try again.');
  }
}

async function save(info, tab){
  let bytes;
  try {
    bytes = await getPicture(info, tab);
  } catch (e) {
    return tell("Couldn't save the picture", "The website wouldn't hand over this picture. Try opening it in its own tab and saving it from there.");
  }
  if (!kindOf(bytes)) {
    try { bytes = await asPng(bytes); }
    catch (e) { return tell("Couldn't save the picture", "The journal can't keep this kind of picture (for example SVG drawings)."); }
  }
  // First the helper Firefox runs by itself, so the journal doesn't need to be open; then the journal, if it's running.
  try {
    const reply = await api.runtime.sendNativeMessage('__HELPER__', {data: await toBase64(bytes)});
    if (reply && reply.ok) return tell('Saved to journal archive', "It's in the Archive, under Images.");
    if (reply && reply.error === 'size') return tell("Couldn't save the picture", 'The picture is too large for the journal (over 40 MB).');
    if (reply && reply.error === 'type') return tell("Couldn't save the picture", "The journal can't keep this kind of picture.");
  } catch (e) { /* no helper yet (or not Firefox): try the running journal instead */ }
  try {
    const r = await fetch(JOURNAL + '/api/archive/images', {method: 'POST', headers: {'X-Journal': '1'}, body: bytes});
    if (r.status === 413) return tell("Couldn't save the picture", 'The picture is too large for the journal (over 40 MB).');
    if (!r.ok) throw new Error('server');
    tell('Saved to journal archive', "It's in the Archive, under Images.");
  } catch (e) {
    tell("Couldn't save the picture", FIREFOX
      ? 'Firefox couldn\u2019t reach the journal. Start server.py once (it sets up saving without the journal open), then try again.'
      : 'The journal isn\u2019t running. Start server.py, then try again.');
  }
}
"""


def _png(size, pixel):
    """A small PNG, drawn one pixel at a time by pixel(x, y) -> (r, g, b, a)."""
    rows = b"".join(b"\x00" + bytes(c for x in range(size) for c in pixel(x, y)) for y in range(size))
    def chunk(kind, data):
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", size, size, 8, 6, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(rows, 9)) + chunk(b"IEND", b""))


def _icon(size):
    # A dark rounded square with a pale page on it, in the journal's colours.
    ink, paper, accent = (0x1E, 0x27, 0x23, 255), (0xF8, 0xF9, 0xF5, 255), (0x7A, 0x2E, 0x3A, 255)
    r = size * 0.2
    def pixel(x, y):
        cx, cy = x + 0.5, y + 0.5
        dx, dy = max(r - cx, 0, cx - (size - r)), max(r - cy, 0, cy - (size - r))
        if dx * dx + dy * dy > r * r:
            return (0, 0, 0, 0)
        if size * .28 <= cx <= size * .72 and size * .2 <= cy <= size * .8:
            if size * .6 <= cx <= size * .66 and cy <= size * .5:
                return accent   # a ribbon bookmark
            return paper
        return ink
    return _png(size, pixel)


def write_extension():
    files = {
        "manifest.json": json.dumps(EXT_MANIFEST, indent=2).encode("utf-8"),
        "background.js": EXT_BACKGROUND.replace("__PORT__", str(PORT)).replace("__HELPER__", HELPER_NAME).lstrip().encode("utf-8"),
        "icon48.png": _icon(48),
        "icon128.png": _icon(128),
    }
    try:
        EXTENSION.mkdir(parents=True, exist_ok=True)
        changed = not EXTENSION_ZIP.exists()
        for name, data in files.items():
            target = EXTENSION / name
            if not target.exists() or target.read_bytes() != data:
                target.write_bytes(data)
                changed = True
        if changed:   # the zip to upload to addons.mozilla.org, to get a signed copy that Firefox keeps
            with zipfile.ZipFile(EXTENSION_ZIP, "w", zipfile.ZIP_DEFLATED) as z:
                for name, data in files.items():
                    z.writestr(zipfile.ZipInfo(name, (2026, 1, 1, 0, 0, 0)), data, zipfile.ZIP_DEFLATED)
    except OSError as e:
        print(f"Couldn't write the browser extension ({EXTENSION}): {e}")



# ---------- The helper Firefox runs to save a picture when the journal isn't running ----------
# Firefox starts "python server.py --save-picture", hands it the picture, and it's put straight in the archive.
def save_picture_for_browser():
    import base64
    def reply(msg):
        data = json.dumps(msg).encode("utf-8")
        sys.stdout.buffer.write(struct.pack("@I", len(data)) + data)
        sys.stdout.buffer.flush()
    try:
        raw = sys.stdin.buffer.read(4)
        if len(raw) < 4:
            return
        length = struct.unpack("@I", raw)[0]
        if length > MAX_IMAGE * 2:
            return reply({"ok": False, "error": "size"})
        msg = json.loads(sys.stdin.buffer.read(length).decode("utf-8"))
        if msg.get("kind") == "quote":
            text = clean_quote_text(msg.get("text"))
            if text is None:
                return reply({"ok": False, "error": "size" if isinstance(msg.get("text"), str) and msg["text"].strip() else "empty"})
            return reply({"ok": True, "name": save_quote(text, msg.get("source"))})
        data = base64.b64decode(msg.get("data", ""), validate=True)
        if len(data) > MAX_IMAGE:
            return reply({"ok": False, "error": "size"})
        ext = sniff(data)
        if not ext:
            return reply({"ok": False, "error": "type"})
        name = f"{secrets.token_hex(16)}.{ext}"
        ARCHIVE_IMAGES.mkdir(parents=True, exist_ok=True)
        tmp = ARCHIVE_IMAGES / f".{name}.tmp"
        tmp.write_bytes(data)
        os.replace(tmp, ARCHIVE_IMAGES / name)   # appears in the archive only once it's complete
        reply({"ok": True, "name": name})
    except Exception as e:   # anything else: say so, rather than leave Firefox waiting
        reply({"ok": False, "error": "failed", "detail": str(e)[:200]})


def register_helper():
    """Tell Firefox where the helper is, so the extension can save pictures without the journal running.
    Done each time the journal starts, so it follows the journal if its folder is moved."""
    script = Path(__file__).resolve()
    try:
        HELPER.mkdir(parents=True, exist_ok=True)
        if os.name == "nt":
            launcher = HELPER / f"{HELPER_NAME}.bat"
            text = f'@echo off\r\n"{sys.executable}" "{script}" --save-picture %*\r\n'
        else:
            launcher = HELPER / HELPER_NAME
            text = f'#!/bin/sh\nexec "{sys.executable}" "{script}" --save-picture "$@"\n'
        if not launcher.exists() or launcher.read_text(encoding="utf-8") != text:
            launcher.write_text(text, encoding="utf-8", newline="")
        if os.name != "nt":
            launcher.chmod(0o755)
        manifest = json.dumps({"name": HELPER_NAME, "description": "Saves pictures from Firefox into the journal's archive",
                               "path": str(launcher), "type": "stdio", "allowed_extensions": [EXTENSION_ID]}, indent=2)
        if os.name == "nt":
            where = HELPER / f"{HELPER_NAME}.json"
        elif sys.platform == "darwin":
            where = Path.home() / "Library" / "Application Support" / "Mozilla" / "NativeMessagingHosts" / f"{HELPER_NAME}.json"
        else:
            where = Path.home() / ".mozilla" / "native-messaging-hosts" / f"{HELPER_NAME}.json"
        where.parent.mkdir(parents=True, exist_ok=True)
        if not where.exists() or where.read_text(encoding="utf-8") != manifest:
            where.write_text(manifest, encoding="utf-8")
        if os.name == "nt":
            import winreg
            with winreg.CreateKey(winreg.HKEY_CURRENT_USER, rf"Software\Mozilla\NativeMessagingHosts\{HELPER_NAME}") as key:
                winreg.SetValueEx(key, "", 0, winreg.REG_SZ, str(where))
    except OSError as e:
        print(f"Couldn't set up saving pictures from Firefox while the journal is closed: {e}")


def main():
    FOLDER.mkdir(exist_ok=True)
    IMAGES.mkdir(exist_ok=True)
    ENTRIES.mkdir(exist_ok=True)
    move_entries_into_folders()
    write_extension()
    register_helper()
    start_hotkeys()
    if OLD_TRASH.exists():
        shutil.rmtree(OLD_TRASH, ignore_errors=True)
        print("Removed the old .trash folder (archiving has replaced it).")
    try:
        httpd = ThreadingHTTPServer((HOST, PORT), Handler)
    except OSError:
        sys.exit(f"Port {PORT} is already in use. Is the journal already running?")
    url = f"http://127.0.0.1:{PORT}"
    print(f"Your journal is running at {url}")
    print(f"Entries are saved in: {FOLDER}")
    print(f"To save pictures from web pages by right-clicking them, load this folder as a browser extension: {EXTENSION}")
    print("  (in Firefox: about:debugging > This Firefox > Load Temporary Add-on..., then pick manifest.json in it)")
    if os.name == "nt":
        print(f"Log shortcuts, anywhere on the computer: {saved_setting('logKey', LOG_KEY_DEFAULT)} to log an activity, "
              f"{saved_setting('shotKey', SHOT_KEY_DEFAULT)} to add a screenshot to the one you started last.")
    elif not sys.platform.startswith("linux"):
        print("To log from anywhere on the computer, give these commands keyboard shortcuts in your system's keyboard settings:")
        print(f"  log an activity:   {helper_command('--log')}")
        print(f"  add a screenshot:  {helper_command('--screenshot')}")
    if sys.platform.startswith("linux"):
        try:
            import tkinter   # noqa: F401  (the logging window is drawn with it)
        except ImportError:
            print(TK_HELP)
    print("Leave this window open while you write. Press Ctrl+C to stop.")
    threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nJournal stopped.")


PAGE = r'''
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Journal</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,500;1,600;1,700;1,800&display=swap" rel="stylesheet">
<style>
:root{
  --paper:#E9ECE6; --sheet:#F8F9F5; --ink:#1E2723; --muted:#5E6963; --rule:#C8CEC5;
  --accent:#7A2E3A; --sel:#DCE1D8;
  color-scheme:light;
  box-sizing:border-box;
  padding-top:env(safe-area-inset-top,0px);
  padding-bottom:env(safe-area-inset-bottom,0px);
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --paper:#131715; --sheet:#1A1F1C; --ink:#E4E6DF; --muted:#9BA49E; --rule:#2E3531;
    --accent:#D6939D; --sel:#262C29; color-scheme:dark;
  }
}
:root[data-theme="dark"]{
  --paper:#131715; --sheet:#1A1F1C; --ink:#E4E6DF; --muted:#9BA49E; --rule:#2E3531;
  --accent:#D6939D; --sel:#262C29; color-scheme:dark;
}
/* Values the Menu can change; unset means the defaults below */
:root{--brand-size:1.6rem;--title-size:clamp(1.9rem,4.2vw,2.7rem);--body-size:1.16rem;
  --caret:var(--accent);--new-bg:var(--ink);--new-fg:var(--paper);--title-color:var(--ink);
  --img-border:1px;--img-border-color:var(--muted);--shelf-h:320px;--shelf-scale:1;--topic-size:16px;--list-topic-size:13px;--bold-amount:3;--u-thick:1.5px;
  --sub-size:20px;--sub-color:var(--ink);--task-scale:1;--task-menu-scale:1}
*,*::before,*::after{box-sizing:inherit}
html{height:100%;scroll-padding-top:env(safe-area-inset-top,0px)}
body{height:100%;margin:0;background:var(--paper);color:var(--ink);
  font-family:"Spectral",Georgia,"Times New Roman",serif;-webkit-font-smoothing:antialiased}
button{font:inherit;color:inherit;cursor:pointer}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px}

.app{display:grid;grid-template-columns:minmax(250px,320px) 1fr;height:100%}

/* Sidebar */
aside{border-right:1px solid var(--rule);display:flex;flex-direction:column;min-height:0}
.side-head{padding:22px 20px 14px;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:10px 12px}
.brand{min-width:0;overflow-wrap:anywhere}
.brand{font-size:var(--brand-size);font-style:italic;font-weight:500;margin:0;letter-spacing:-.01em}
.new{white-space:nowrap;background:var(--new-bg);color:var(--new-fg);border:0;border-radius:999px;padding:6px 16px;font-size:.95rem}
.new:hover{filter:brightness(1.18)}
.search{margin:0 20px 10px;padding:8px 12px;border:1px solid var(--rule);border-radius:6px;
  background:var(--sheet);font:inherit;font-size:.95rem;color:var(--ink)}
.search::placeholder{color:var(--muted)}
/* Which entries the list shows, and in what order */
.list-view{margin:0 20px 8px}
.view-tabs{display:flex;flex-wrap:wrap;gap:4px}
.view-tab{flex:1 1 auto;background:none;border:1px solid var(--rule);border-radius:999px;padding:2px 8px;font-size:.8rem;color:var(--ink);white-space:nowrap}
.view-tab:hover{border-color:var(--ink)}
.view-tab[aria-checked="true"]{background:var(--ink);color:var(--paper);border-color:var(--ink)}
.view-topics{display:flex;flex-wrap:wrap;align-items:center;gap:5px;margin-top:8px;max-height:9.5em;overflow-y:auto;padding:1px}
.view-topics[hidden]{display:none}
.view-chip{background:none;border:1px dashed var(--rule);border-radius:999px;padding:1px 10px;font-size:.82rem;color:var(--muted);max-width:100%;
  overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.view-chip:hover{border-color:var(--ink);color:var(--ink)}
.view-chip[aria-pressed="true"]{border:1px solid var(--accent);color:var(--accent);background:color-mix(in srgb, var(--accent) 8%, transparent)}
.view-chip.clear{border-style:solid;color:var(--ink)}
.view-hint{flex-basis:100%;margin:0;font-size:.8rem;font-style:italic;color:var(--muted)}
.list{overflow-y:auto;flex:1;min-height:0;padding:4px 10px 16px;margin:0;list-style:none}
.list li + li{border-top:1px solid var(--rule)}
.entry-btn{display:block;width:100%;text-align:left;background:none;border:0;border-radius:6px;padding:12px 10px}
.entry-btn:hover{background:var(--sel)}
.entry-btn[aria-current="true"]{background:var(--sel)}
.entry-btn .trow{display:flex;align-items:center;gap:8px}
.entry-btn .t{flex:0 1 auto;min-width:0;font-weight:500;font-size:1.02rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.minis{display:flex;align-items:center;gap:4px;flex:none;margin-left:auto}
.entry-btn .tp{flex:1 1 0;min-width:2.5em;font-size:var(--list-topic-size);color:var(--muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.minis img{display:block;width:28px;height:28px;object-fit:cover;border-radius:3px;border:1px solid var(--rule);background:var(--paper)}
.minis .more{font-size:.8rem;color:var(--muted);white-space:nowrap;margin-left:3px}
.entry-btn .t.untitled{font-style:italic;color:var(--muted);font-weight:400}
.entry-btn .d{display:block;font-style:italic;color:var(--muted);font-size:.85rem;margin-top:2px}
.entry-btn .s{display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;
  color:var(--muted);font-size:.92rem;line-height:1.45;margin-top:4px}
.list-note{color:var(--muted);font-style:italic;padding:12px 10px;margin:0}
.foot{display:flex;flex-wrap:wrap;align-items:center;gap:8px;padding:12px 20px 16px;border-top:1px solid var(--rule)}
.where{font-size:.82rem;color:var(--accent);margin:0 0 4px;flex:1 0 100%}
.where:empty{display:none}
.menu-btn{background:none;border:1px solid var(--rule);border-radius:999px;padding:3px 12px;color:var(--ink);font-size:.9rem;flex:none}
.menu-btn:hover{border-color:var(--ink)}

/* Writing page */
main{min-height:0;overflow-y:auto;background:var(--sheet)}
.page{margin:0;padding:40px 40px 0;height:100%;display:flex;flex-direction:column}
.page[hidden]{display:none}
.page > *{flex:none}
/* The writing scrolls on its own, under the title and buttons, with its scrollbar just to the right of the text
   (between the text and the pictures), while the pictures on the right scroll separately */
.page > .scroll{flex:1;min-height:0;width:100%;max-width:calc(42rem + 28px);overflow-y:auto;overscroll-behavior:contain;
  padding:0 28px 96px 0}
.title,.body{max-width:42rem}
.back{display:none;background:none;border:1px solid var(--rule);border-radius:999px;padding:3px 12px;margin-bottom:20px;color:var(--ink);font-size:.9rem}
.back:hover{border-color:var(--ink)}
.title{display:block;font:inherit;font-size:var(--title-size);caret-color:var(--caret);font-style:italic;font-weight:500;
  line-height:1.15;border:0;background:none;color:var(--title-color);width:100%;padding:0;outline:none;letter-spacing:-.01em}
.title::placeholder{color:var(--muted);opacity:.7}
.body:empty::before{content:attr(data-placeholder);color:var(--muted);opacity:.7;pointer-events:none}
.meta{color:var(--muted);font-size:.9rem;margin:12px 0 30px;display:flex;flex-wrap:wrap;gap:6px 18px;align-items:center}
.actions{display:flex;align-items:center;gap:8px;flex-wrap:nowrap}
.status{font-style:italic}
.status.err{color:var(--accent);font-style:normal}
.export-row{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin-bottom:4px}
#exportBtn:disabled{opacity:.5;cursor:default}
.hist{position:relative}
.hist-btn{background:none;border:1px solid var(--rule);border-radius:999px;padding:3px 12px;color:var(--ink);font-size:.9rem;cursor:default}
.hist-pop{display:none;position:absolute;top:100%;left:0;z-index:20;padding-top:6px}
.hist-pop ul{margin:0;padding:10px 14px;list-style:none;background:var(--sheet);border:1px solid var(--rule);border-radius:6px;
  box-shadow:0 6px 20px rgba(0,0,0,.14);white-space:nowrap;font-size:.92rem;color:var(--ink);max-height:50vh;overflow-y:auto}
.hist-pop li{padding:2px 0}
.hist-pop li.begun{color:var(--muted);font-style:italic;border-bottom:1px solid var(--rule);padding-bottom:6px;margin-bottom:4px}
.hist:hover .hist-pop,.hist:focus-within .hist-pop{display:block}
.draw{position:fixed;z-index:40;display:flex;flex-direction:column;
  background:color-mix(in srgb, var(--sheet) 86%, transparent)}
.draw[hidden]{display:none}
.draw-bar{display:flex;flex-wrap:wrap;align-items:center;gap:8px 14px;padding:12px 20px;border-bottom:1px solid var(--rule);
  background:color-mix(in srgb, var(--sheet) 94%, transparent)}
.draw-group{display:flex;align-items:center;gap:6px}
.swatch{width:24px;height:24px;border-radius:50%;border:1px solid var(--rule);padding:0}
.swatch[aria-pressed="true"],.size[aria-pressed="true"],.tool[aria-pressed="true"]{outline:2px solid var(--ink);outline-offset:2px}
.size{width:28px;height:28px;border-radius:50%;border:1px solid var(--rule);background:none;display:grid;place-items:center;padding:0}
.size span{display:block;border-radius:50%;background:var(--ink)}
.tool{background:none;border:1px solid var(--rule);border-radius:999px;padding:3px 12px;color:var(--ink);font-size:.9rem}
.tool:hover{border-color:var(--ink)}
.draw-bar .spacer{flex:1}
.swatch[hidden]{display:none}
.swatch.hl{border-radius:5px}
#hlSwatches,.side-draw [aria-label="Highlighter colour"]{padding-left:8px;border-left:1px solid var(--rule)}
.draw-done{background:var(--ink);color:var(--paper);border:0;border-radius:999px;padding:5px 18px;font-size:.95rem}
.draw-done:hover{background:var(--accent)}
.tool.arm{color:var(--accent);border-color:var(--accent)}
#canvas{flex:1;min-height:0;width:100%;display:block;touch-action:none;cursor:crosshair}
#settings{border:1px solid var(--rule);border-radius:10px;background:var(--sheet);color:var(--ink);padding:0;
  width:min(480px,92vw);max-height:90vh;overflow:auto;box-shadow:0 18px 50px rgba(0,0,0,.25)}
#settings::backdrop{background:rgba(10,12,11,.35)}
.set-head{display:flex;align-items:center;justify-content:space-between;padding:18px 24px 6px}
.set-head h2{margin:0;font-size:1.5rem;font-style:italic;font-weight:500}
#settings section{padding:8px 24px 6px}
#settings h3{font-size:1.02rem;font-weight:600;margin:14px 0 8px}
.set-row{display:grid;grid-template-columns:1fr auto 3.2em auto;align-items:center;gap:10px;padding:7px 0;border-top:1px solid var(--rule)}
.set-row label{font-size:.98rem}
.set-row input[type=range]{width:150px;accent-color:var(--accent)}
.set-row input[type=color]{width:44px;height:28px;padding:0;border:1px solid var(--rule);border-radius:6px;background:none;cursor:pointer}
.set-row output{font-size:.88rem;color:var(--muted);text-align:right}
.set-reset{background:none;border:1px solid var(--rule);border-radius:999px;padding:1px 10px;color:var(--ink);font-size:.84rem}
.set-reset:hover{border-color:var(--ink)}
.set-reset:disabled{visibility:hidden}
.set-foot{display:flex;justify-content:space-between;align-items:center;padding:14px 24px 20px}
.set-foot .tool{font-size:.9rem}
#archive,#tasksDialog,#logDialog,#topicsDialog,#quotesDialog{border:1px solid var(--rule);border-radius:10px;background:var(--sheet);color:var(--ink);padding:0;
  width:min(680px,94vw);height:min(80vh,760px);box-shadow:0 18px 50px rgba(0,0,0,.25);overflow:hidden}
#archive[open],#tasksDialog[open],#logDialog[open],#topicsDialog[open],#quotesDialog[open]{display:flex;flex-direction:column}
#archive::backdrop,#tasksDialog::backdrop,#logDialog::backdrop,#topicsDialog::backdrop,#quotesDialog::backdrop,#logPic::backdrop{background:rgba(10,12,11,.35)}
/* The Log: days that open to show their activities, numbered in the order they started */
.log-day{border-top:1px solid var(--rule)}
.log-day:first-child{border-top:0}
.log-day summary{display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 12px;padding:11px 10px;cursor:pointer;list-style:none;border-radius:6px}
.log-day summary::-webkit-details-marker{display:none}
.log-day summary::before{content:"";flex:none;align-self:center;width:0;height:0;border-left:6px solid var(--muted);border-top:4.5px solid transparent;border-bottom:4.5px solid transparent;transition:transform .15s}
.log-day[open] summary::before{transform:rotate(90deg)}
.log-day summary:hover{background:var(--paper)}
.log-date{font-weight:500;font-size:1.02rem}
.log-count{color:var(--muted);font-size:.86rem}
.log-going{color:var(--accent);font-size:.8rem;border:1px solid currentColor;border-radius:999px;padding:0 8px}
.log-acts{list-style:none;margin:2px 0 14px;padding:0 6px 0 24px;display:flex;flex-direction:column;gap:8px}
.log-act{display:grid;grid-template-columns:1.8em 1fr;gap:0 8px;padding:9px 12px 10px;border:1px solid var(--rule);border-radius:8px}
.log-act.going{border-color:color-mix(in srgb, var(--accent) 45%, var(--rule))}
.log-num{color:var(--muted);text-align:right;font-variant-numeric:tabular-nums;line-height:1.6}
.log-main{min-width:0}
.log-head{display:flex;flex-wrap:wrap;align-items:baseline;gap:2px 12px;line-height:1.6}
.log-title{font-weight:500;overflow-wrap:anywhere}
.log-when{color:var(--muted);font-size:.84rem;font-variant-numeric:tabular-nums}
.log-act.going .log-when{color:var(--accent)}
.log-desc{white-space:pre-wrap;overflow-wrap:anywhere;margin:3px 0 0;font-size:.95rem;line-height:1.5}
.log-pics{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px}
.log-pics img{height:72px;max-width:140px;object-fit:cover;border:1px solid var(--rule);border-radius:4px;cursor:zoom-in;background:var(--paper)}
.log-btns{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px}
.log-btns .tool{font-size:.8rem;padding:1px 10px}
.log-btns .log-del{color:var(--accent)}
.log-btns .log-del.arm{border-color:var(--accent)}
.log-form{border-bottom:1px solid var(--rule);padding-bottom:14px}
.log-form-title{margin:0;font-size:1rem;font-weight:500}
.log-row{display:flex;flex-wrap:wrap;align-items:center;gap:8px 10px}
.log-row[hidden]{display:none}
.log-row > label:not(.log-radio){min-width:6.5em;color:var(--muted);font-size:.9rem}
.log-form .log-row input[type="datetime-local"],.log-form .log-row select{width:auto;padding:4px 8px;color-scheme:light dark}
.log-form select{font:inherit;font-size:.95rem;color:var(--ink);background:var(--paper);border:1px solid var(--rule);border-radius:6px;max-width:100%}
.log-radio{display:inline-flex;align-items:center;gap:6px;font-size:.95rem;cursor:pointer}
.log-form .log-radio input{width:auto;margin:0;accent-color:var(--ink)}
.log-hint{color:var(--muted);font-size:.84rem;font-style:italic}
.log-form-pics{display:flex;flex-wrap:wrap;gap:8px}
.log-form-pics:empty{display:none}
.log-form-pic{position:relative}
.log-form-pic img{height:60px;max-width:120px;object-fit:cover;border:1px solid var(--rule);border-radius:4px;display:block}
.log-form-pic button{position:absolute;top:-7px;right:-7px;width:20px;height:20px;border-radius:50%;border:1px solid var(--rule);background:var(--sheet);color:var(--ink);font-size:.8rem;line-height:1;padding:0}
.log-form-pic button:hover{border-color:var(--accent);color:var(--accent)}
.log-keys-note{margin:6px 0 0;color:var(--muted);font-size:.86rem;line-height:1.5}
.log-keys-note.err{color:var(--accent)}
.log-keys-note.log-cmd{font-family:ui-monospace,Consolas,monospace;font-size:.78rem;color:var(--ink);overflow-wrap:anywhere;user-select:all}
#logPic{border:0;padding:0;background:none;max-width:94vw;max-height:92vh;cursor:zoom-out}
#logPic img{display:block;max-width:94vw;max-height:92vh;border-radius:6px}
/* Topics: made in the Topics menu, numbered from 1; each entry can have one, shown under its title */
#topicsDialog,#quotesDialog{height:fit-content;max-height:min(80vh,760px)}
#quotesDialog .arch-panel{flex:0 1 auto}
#topicsDialog .arch-panel{flex:0 1 auto}
.topic-list{list-style:none;margin:0;padding:0}
.topic-list li,.topic-add{display:flex;align-items:center;gap:10px;padding:9px 10px}
.topic-list li + li{border-top:1px solid var(--rule)}
.topic-add{border-top:1px solid var(--rule);margin-top:4px}
.topic-num{flex:none;min-width:1.6em;text-align:right;color:var(--muted);font-variant-numeric:tabular-nums}
.topic-input{flex:1;min-width:0;font:inherit;font-size:1rem;color:var(--ink);background:none;border:1px solid transparent;border-radius:6px;padding:4px 8px}
.topic-input:hover{border-color:var(--rule)}
.topic-input:focus{outline:none;border-color:var(--accent);background:var(--paper)}
.topic-add .topic-input{border-color:var(--rule)}
.topic-uses{flex:none;font-size:.84rem;font-style:italic;color:var(--muted);white-space:nowrap}
.topic-list .tool{flex:none;font-size:.84rem;padding:2px 11px}
/* Pulled up into the space the title's line leaves below its letters, so the topics sit just under it */
.topic-row{position:relative;display:flex;flex-wrap:wrap;align-items:center;gap:4px 10px;margin-top:calc(var(--title-size) * -.13);max-width:42rem}
.topic-name{font-size:var(--topic-size);line-height:1.05;font-style:italic;color:var(--ink)}
.topic-btn{flex:none;width:22px;height:22px;display:grid;place-items:center;background:none;border:1px solid var(--rule);border-radius:50%;padding:0 0 1px;
  color:var(--muted);font-size:1.05rem;line-height:1}
.topic-btn:hover,.topic-btn[aria-expanded="true"]{border-color:var(--ink);color:var(--ink)}
.topic-pop{position:absolute;left:0;top:100%;z-index:22;margin-top:6px;min-width:220px;max-width:min(360px,90vw);max-height:50vh;overflow-y:auto;
  padding:6px;background:var(--sheet);border:1px solid var(--rule);border-radius:8px;box-shadow:0 6px 20px rgba(0,0,0,.14)}
.topic-pop[hidden]{display:none}
.topic-pop button{display:flex;align-items:baseline;gap:10px;width:100%;text-align:left;background:none;border:0;border-radius:5px;padding:6px 10px;font-size:.95rem;color:var(--ink)}
.topic-pop button:hover,.topic-pop button:focus-visible{background:var(--sel)}
.topic-pop button[aria-pressed="true"]{color:var(--accent)}
.topic-pop button[aria-pressed="true"]::after{content:"\2713";margin-left:auto}
.topic-pop .topic-num{min-width:1.4em}
.topic-pop .topic-none{color:var(--muted);font-style:italic;border-top:1px solid var(--rule);border-radius:0 0 5px 5px;margin-top:4px}
.topic-pop p{margin:4px 10px 8px;color:var(--muted);font-style:italic;font-size:.92rem}
.tabs{display:flex;gap:6px;padding:6px 24px 12px;border-bottom:1px solid var(--rule)}
.tab{background:none;border:1px solid var(--rule);border-radius:999px;padding:4px 14px;color:var(--ink);font-size:.95rem}
.tab[aria-selected="true"]{background:var(--ink);color:var(--paper);border-color:var(--ink)}
.arch-panel{flex:1;min-height:0;overflow-y:auto;padding:8px 14px 20px}
.arch-note{color:var(--muted);font-style:italic;padding:14px 10px;margin:0}
.arch-list{list-style:none;margin:0;padding:0}
.arch-list li + li{border-top:1px solid var(--rule)}
.arch-item{padding:12px 10px}
.arch-item .trow{display:flex;align-items:center;gap:8px}
.arch-item .t{flex:1;min-width:0;font-weight:500;font-size:1.02rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;
  background:none;border:0;padding:0;text-align:left;color:var(--ink)}
.arch-item .t.untitled{font-style:italic;color:var(--muted);font-weight:400}
.arch-item .d{display:block;font-style:italic;color:var(--muted);font-size:.85rem;margin-top:2px}
.arch-item .s{color:var(--muted);font-size:.92rem;line-height:1.45;margin-top:4px;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;cursor:pointer}
.arch-item.open .s{display:none}
.arch-body{display:none;white-space:pre-wrap;overflow-wrap:break-word;font-size:1.02rem;line-height:1.7;margin-top:8px;padding:10px 12px;
  background:var(--paper);border-radius:6px}
.arch-item.open .arch-body{display:block}
.arch-body .fig,.arch-grid .fig{cursor:zoom-in}
.add-back{flex:none;background:none;border:1px solid var(--rule);border-radius:999px;padding:2px 12px;color:var(--ink);font-size:.86rem;white-space:nowrap}
.add-back:hover{border-color:var(--ink)}
.erase-entry{flex:none;background:none;border:1px solid var(--rule);border-radius:999px;padding:2px 12px;color:var(--accent);font-size:.86rem;white-space:nowrap}
.erase-entry:hover,.erase-entry.arm{border-color:var(--accent)}
.arch-grid{list-style:none;margin:0;padding:6px 6px;display:grid;grid-template-columns:repeat(auto-fill,minmax(120px,1fr));gap:14px}
.arch-grid button{display:block;width:100%;padding:0;border:1px solid var(--rule);border-radius:6px;background:var(--paper);overflow:hidden;cursor:zoom-in}
.arch-grid img{display:block;width:100%;aspect-ratio:1;object-fit:cover}
/* With an entry open, archived pictures can be dragged into it */
body.can-bring-back .arch-grid button,body.can-bring-back .arch-body .fig{cursor:grab}
.arch-hint{margin:0 0 10px;color:var(--muted);font-size:.86rem;font-style:italic}
.arch-grid span{display:block;font-size:.82rem;font-style:italic;color:var(--muted);margin-top:4px}
.arch-grid .erase{width:auto;margin-top:6px;border:1px solid var(--rule);border-radius:999px;background:none;padding:2px 12px;
  color:var(--accent);font-size:.84rem;cursor:pointer}
.arch-grid .erase:hover,.arch-grid .erase.arm{border-color:var(--accent)}
/* Folders in the archive's Images */
.arch-crumbs{display:flex;flex-wrap:wrap;align-items:center;gap:2px 4px;margin:0 6px 10px;font-size:.95rem}
.arch-crumb{background:none;border:1px solid transparent;border-radius:999px;padding:2px 10px;color:var(--accent);max-width:18em;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.arch-crumb:hover{border-color:var(--rule)}
.arch-crumb[aria-current="page"]{color:var(--ink);font-weight:500;cursor:default}
.arch-crumb[aria-current="page"]:hover{border-color:transparent}
.arch-crumbs .sep{color:var(--muted)}
.arch-grid .folder-tile{aspect-ratio:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;padding:8px;cursor:pointer;color:var(--ink)}
body.can-bring-back .arch-grid .folder-tile,.arch-grid .folder-tile{cursor:pointer}
.arch-grid .folder-tile svg{width:46%;height:auto;color:var(--muted)}
.arch-grid .folder-tile .folder-name{font-style:normal;color:var(--ink);font-size:.9rem;margin:0;max-width:100%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.arch-grid .folder-tile .folder-count{margin:0}
.arch-grid .folder-rename{display:block;width:100%;margin-top:4px;font:inherit;font-size:.9rem;color:var(--ink);background:var(--paper);border:1px solid var(--ink);border-radius:6px;padding:2px 6px}
.arch-grid .folder-btns{display:flex;flex-wrap:wrap;gap:6px}
.arch-grid .folder-btns button{width:auto;margin-top:6px;border:1px solid var(--rule);border-radius:999px;background:none;padding:2px 12px;color:var(--ink);font-size:.84rem;cursor:pointer}
.arch-grid .folder-btns button:hover{border-color:var(--ink)}
.arch-grid .folder-btns .erase{color:var(--accent)}
.arch-grid .folder-btns .erase:hover{border-color:var(--accent)}
.arch-folder-note{margin:6px 6px 0;color:var(--accent);font-size:.86rem}
.drop-folder{outline:2px dashed var(--accent);outline-offset:2px;border-radius:6px}
.ghost.ghost-folder{display:grid;place-items:center;background:var(--sheet);border:1px solid var(--rule);color:var(--muted)}
.ghost.ghost-folder svg{width:30px;height:30px}
#viewer.readonly .viewer-bar button:not(#viewerClose){display:none}
.del{background:none;border:1px solid var(--rule);border-radius:999px;padding:3px 12px;color:var(--ink);font-size:.9rem}
.del:hover{border-color:var(--ink)}
.del.arm{color:var(--accent);border-color:var(--accent)}
.del.forever{color:var(--accent)}
.del.forever:hover{border-color:var(--accent)}
.viewer-bar .forever{background:none;color:#F0B8C0;border:1px solid rgba(240,184,192,.5)}
.viewer-bar .arm{background:#9B2F3F;color:#fff;border-color:#9B2F3F}
.body{display:block;font-size:var(--body-size);line-height:1.78;color:var(--ink);white-space:pre-wrap;overflow-wrap:break-word;
  outline:none;min-height:55vh;padding-bottom:4em;caret-color:var(--caret)}
/* Bold and underlined writing. Bold strength 1 to 4 steps through the font's weights (medium to extra bold);
   above 4 the letters are thickened further with an outline. Both are set in the Menu. */
.body b,.link-body b{font-weight:calc(400 + min(var(--bold-amount), 4) * 100);-webkit-text-stroke:calc(max(var(--bold-amount) - 4, 0) * .014em) currentColor}
.body u,.link-body u{text-decoration-line:underline;text-decoration-thickness:var(--u-thick);text-underline-offset:calc(var(--u-thick) / 2 + .14em);
  text-decoration-skip-ink:auto}
#boldBtn{font-weight:700}
#underlineBtn{text-decoration:underline;text-underline-offset:.18em}
#boldBtn[aria-pressed="true"],#underlineBtn[aria-pressed="true"]{background:var(--ink);color:var(--paper);border-color:var(--ink)}
/* Sub-entry: a roman numeral where the topic changes, with the writing carrying on right beside it */
.sub{display:inline-block;margin-right:.4em;line-height:1;user-select:none;-webkit-user-select:none;
  color:var(--sub-color);font-size:var(--sub-size);font-style:normal;font-weight:600;letter-spacing:.04em;font-variant-numeric:lining-nums}
/* Indent: an invisible copy of the sub-entry's numeral, so the line's words start where the words beside the numeral do.
   It takes up no height, so a large numeral doesn't open up the line. */
.indent{display:inline-block;height:0;overflow:hidden;visibility:hidden;vertical-align:baseline;margin-right:.4em;
  font-size:var(--sub-size);font-style:normal;font-weight:600;letter-spacing:.04em;font-variant-numeric:lining-nums;
  user-select:none;-webkit-user-select:none}
.indent::before{content:attr(data-n)}
/* Task size is set in the Menu, separately for tasks in the entry (--task-scale) and in the Tasks menu (--task-menu-scale) */
.tasks{--ts:var(--task-scale);display:block;margin:10px 0 16px;max-width:calc(42rem * var(--ts));white-space:normal;line-height:1.5;font-size:calc(100% * var(--ts));
  user-select:none;-webkit-user-select:none}
#tasksPanel .tasks{--ts:var(--task-menu-scale)}
.tasks ol{list-style:none;margin:0;padding:0;counter-reset:task;display:flex;flex-direction:column;gap:calc(6px * var(--ts))}
.task{counter-increment:task;display:flex;flex-wrap:wrap;align-items:center;gap:calc(6px * var(--ts)) calc(12px * var(--ts));padding:calc(8px * var(--ts)) calc(12px * var(--ts));border:1px solid var(--rule);border-radius:calc(8px * var(--ts));
  background:var(--sheet);transition:transform .14s ease, box-shadow .14s ease;transform-origin:center left}
.task::before{content:counter(task) ".";color:var(--muted);min-width:1.5em;text-align:right;font-variant-numeric:tabular-nums;flex:none}
.task:hover{transform:scale(1.02);box-shadow:0 3px 12px rgba(0,0,0,.08)}
.task-text{flex:0 1 auto;min-width:0;outline:none;white-space:pre-wrap;overflow-wrap:anywhere;caret-color:var(--caret);user-select:text;-webkit-user-select:text}
.task-text:empty::before{content:"New task";color:var(--muted);opacity:.7}
.task-box{flex:none;width:calc(26px * var(--ts));height:calc(26px * var(--ts));border:1.5px solid var(--muted);border-radius:calc(6px * var(--ts));background:none;display:grid;place-items:center;padding:0;color:var(--muted)}
.task-box:hover{border-color:var(--ink)}
.task-box svg{width:calc(16px * var(--ts));height:calc(16px * var(--ts))}
.task[data-state="done"] .task-box{border-color:#2F8A4C;color:#2F8A4C;background:rgba(47,138,76,.10)}
.task[data-state="fail"] .task-box{border-color:#C23B3B;color:#C23B3B;background:rgba(194,59,59,.10)}
.task-del{display:none;flex:none;background:none;border:1px solid var(--rule);border-radius:999px;padding:1px 10px;color:var(--accent);font-size:calc(.84rem * var(--ts));line-height:1.5}
.task-del:hover{border-color:var(--accent)}
.task.asking .task-del{display:inline-block}
.task-grip{order:-1;flex:none;margin-left:-4px;color:var(--muted);opacity:0;cursor:grab;font-size:calc(.95rem * var(--ts));line-height:1;
  user-select:none;-webkit-user-select:none;touch-action:none;transition:opacity .12s}
.task:hover .task-grip,.task.asking .task-grip{opacity:.55}
.task.task-dragging{position:relative;z-index:2;transform:scale(1.02);box-shadow:0 8px 24px rgba(0,0,0,.16);cursor:grabbing}
.task.task-dragging .task-grip{opacity:.9}
.task.drop-into{outline:2px dashed var(--accent);outline-offset:2px}
.task-meta{display:inline-flex;flex-wrap:wrap;align-items:baseline;gap:2px 10px;margin-right:auto;font-size:calc(.76rem * var(--ts));line-height:1.3;white-space:nowrap}
.task-when{color:var(--muted);opacity:.6;font-variant-numeric:tabular-nums}
.task-due{color:var(--muted);opacity:.85;font-variant-numeric:tabular-nums}
.task-marked{opacity:.85;font-variant-numeric:tabular-nums}
.task-marked.done{color:#2F8A4C}
.task-marked.fail{color:#C23B3B}
.task-due.late{color:var(--accent);opacity:1}
/* Archiving finished tasks (Tasks menu, Done) and the Archive's Tasks tab */
.task-arch-btn{flex:none;background:none;border:1px solid var(--rule);border-radius:999px;padding:1px 10px;color:var(--ink);font-size:calc(.84rem * var(--ts));line-height:1.5;cursor:pointer}
.task-arch-btn:hover{border-color:var(--ink)}
.task-arch-btn:disabled{cursor:default;color:var(--muted);border-color:var(--rule)}
.task-arch-btn.erase-task{color:var(--accent)}
.task-arch-btn.erase-task:hover,.task-arch-btn.erase-task.arm{border-color:var(--accent)}
.tl-actions{display:flex;justify-content:flex-end;align-items:center;gap:10px;margin:0 0 6px}
.tl-actions .status{margin-right:auto;font-size:.86rem}
.task-archived{color:var(--muted);font-style:italic;font-variant-numeric:tabular-nums}
#archTasks .task:hover{transform:none;box-shadow:none}
#archTasks .tl-entry.gone{color:var(--muted);cursor:default}
/* The Archive's Tasks tab, a day at a time: the day's heading, then that day's tasks under their entries. */
.arch-task-day + .arch-task-day{margin-top:18px}
.arch-task-day-head{margin:0;padding:6px 10px 7px;border-bottom:1px solid var(--rule);font-size:.9rem;font-weight:600;letter-spacing:.02em;color:var(--muted)}
.arch-task-day .tl-group + .tl-group{border-top:1px dashed var(--rule)}
.task-due-btn{display:none;flex:none;background:none;border:1px solid var(--rule);border-radius:999px;padding:1px 10px;color:var(--ink);font-size:calc(.84rem * var(--ts));line-height:1.5}
.task-due-btn:hover{border-color:var(--ink)}
.task.asking .task-due-btn:not([hidden]){display:inline-block}
.task-due-edit{display:none;flex:none;align-items:center;gap:6px}
.task.asking .task-due-edit:not([hidden]){display:inline-flex}
.task-due-edit input{font:inherit;color:var(--ink);background:var(--sheet);border:1px solid var(--rule);border-radius:6px;padding:1px 6px;color-scheme:light dark;font-size:calc(.84rem * var(--ts))}
.task-due-edit button{background:none;border:1px solid var(--rule);border-radius:999px;padding:1px 10px;color:var(--muted);font-size:calc(.84rem * var(--ts));line-height:1.5}
.task-due-edit button:hover{border-color:var(--ink);color:var(--ink)}
/* Urgency: a coloured label at the right of the task, just before its box */
:root{--urg-high:#C23B3B;--urg-high-text:#B03030;--urg-medium:#D9A800;--urg-medium-text:#8A6A00;--urg-low:#2F8A4C;--urg-low-text:#2F8A4C}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--urg-high-text:#F07A7A;--urg-medium-text:#F0C63C;--urg-low-text:#6CCB8C}}
.task-urg{flex:none;display:inline-flex;align-items:center;gap:5px;border:1px solid var(--u);border-radius:999px;padding:1px 9px;
  color:var(--ut);background:color-mix(in srgb, var(--u) 12%, transparent);font:inherit;font-size:calc(.76rem * var(--ts));line-height:1.5;white-space:nowrap}
.task-urg::before,.urg-dot{content:"";display:inline-block;width:.6em;height:.6em;border-radius:50%;background:var(--u);flex:none}
.task-urg[hidden]{display:none}
button.task-urg{cursor:pointer}
button.task-urg:hover{background:color-mix(in srgb, var(--u) 22%, transparent)}
[data-u="high"]{--u:var(--urg-high);--ut:var(--urg-high-text)}
[data-u="medium"]{--u:var(--urg-medium);--ut:var(--urg-medium-text)}
[data-u="low"]{--u:var(--urg-low);--ut:var(--urg-low-text)}
.task-urg-btn{display:none;flex:none;background:none;border:1px solid var(--rule);border-radius:999px;padding:1px 10px;color:var(--ink);font-size:calc(.84rem * var(--ts));line-height:1.5}
.task-urg-btn:hover{border-color:var(--ink)}
.task.asking .task-urg-btn{display:inline-block}
.urg-menu button{color:var(--ut, var(--ink))}
/* The Tasks menu listed by urgency or by finish time: one list across all entries, each task saying which entry it's in */
#tasksDialog .tabs{flex-wrap:wrap;align-items:center}
.task-sort{margin-left:auto;display:flex;align-items:center;gap:4px;flex-wrap:wrap}
.task-sort .lbl{font-size:.82rem;color:var(--muted);font-style:italic;margin-right:2px}
.tl-head{display:block;font-weight:500;font-size:1.02rem;color:var(--ink)}
.tl-group .tasks.flat .task::before{content:none}
.task-from{color:var(--accent);opacity:.85;font-style:italic;max-width:16em;overflow:hidden;text-overflow:ellipsis}
.tl-group{padding:12px 10px 4px}
.tl-group + .tl-group{border-top:1px solid var(--rule)}
.tl-entry{display:block;background:none;border:0;padding:0;font:inherit;font-weight:500;font-size:1.02rem;color:var(--ink);text-align:left;cursor:pointer;
  max-width:100%;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.tl-entry:hover{text-decoration:underline}
.tl-entry.untitled{font-style:italic;color:var(--muted);font-weight:400}
.tl-group .tasks{margin:8px 0 10px}
/* In the Ongoing and Done tabs each task keeps the number it has in its entry */
.tl-group .task[data-n]::before{content:attr(data-n) "."}
.tab .tab-n{margin-left:6px;font-size:.84em;opacity:.7;font-variant-numeric:tabular-nums}
/* Task lists that are apart in the entry are shown apart here too, each numbered from 1 */
.tl-group .tasks + .tasks{margin-top:calc(26px * var(--ts));position:relative}
.tl-group .tasks + .tasks::before{content:"";position:absolute;left:12px;right:12px;top:calc(-13px * var(--ts));border-top:1px dashed var(--rule)}
.tl-group .task{cursor:pointer}
.tl-group .task-text{cursor:pointer;user-select:none;-webkit-user-select:none}
.tasks.readonly .task:hover{transform:none;box-shadow:none}
.task-menu{position:fixed;z-index:70;display:flex;flex-direction:column;gap:2px;padding:6px;background:var(--sheet);border:1px solid var(--rule);
  border-radius:8px;box-shadow:0 8px 24px rgba(0,0,0,.16)}
.task-menu[hidden]{display:none}
.task-menu button{display:flex;align-items:center;gap:8px;background:none;border:1px solid transparent;border-radius:6px;padding:5px 12px 5px 8px;
  color:var(--ink);font-size:.92rem;text-align:left}
.task-menu button:hover,.task-menu button:focus-visible{border-color:var(--rule);background:var(--paper)}
.task-menu .tm-done svg{color:#2F8A4C}
.task-menu .tm-fail svg{color:#C23B3B}
.task-menu .tm-clear{padding-left:32px;color:var(--muted)}
.task-menu [hidden]{display:none}
@media (prefers-reduced-motion: reduce){.task{transition:none}.task:hover{transform:none}}
.fig{display:inline-block;vertical-align:-.2em;line-height:0;cursor:grab;user-select:none;-webkit-user-select:none;touch-action:none}
.fig img{display:block;width:1.1em;height:1.1em;object-fit:cover;border-radius:2px;pointer-events:none;
  outline:var(--img-border) solid var(--img-border-color)}
.fig.dragging{opacity:.3}
.quote.dragging{opacity:.3}
/* A link to another entry: its name in capitals inside a border, about the height of a picture in the writing */
.fig.elink{line-height:1;vertical-align:.12em;font-size:.6em;font-weight:600;font-style:normal;letter-spacing:.06em;text-transform:uppercase;
  padding:.22em .55em .2em;border:1.5px solid var(--ink);border-radius:3px;color:var(--ink);background:var(--sheet);white-space:nowrap;
  max-width:24em;overflow:hidden;text-overflow:ellipsis}
button.fig.elink{font-family:inherit;margin:0;cursor:pointer}
.fig.elink:hover{border-color:var(--accent)}
.fig.elink.missing{border-style:dashed;border-color:var(--muted);color:var(--muted)}
.ghost.elink{width:auto;height:auto;font-size:calc(var(--body-size) * .6);box-shadow:0 8px 24px rgba(0,0,0,.2)}
.ghost.elink.nodrop{opacity:.45}
/* A PDF in the writing: its title beside a small page with a turned corner, in a box like a linked entry's
   but in ordinary letters, so the two are told apart at a glance */
.fig.epdf{line-height:1;vertical-align:.1em;font-size:.72em;font-style:italic;font-weight:500;
  padding:.2em .6em .2em .42em;border:1.5px solid var(--ink);border-radius:3px;color:var(--ink);background:var(--sheet);white-space:nowrap;
  max-width:24em;overflow:hidden;text-overflow:ellipsis}
.fig.epdf svg,.ghost.epdf svg{width:.95em;height:1.1em;margin-right:.35em;vertical-align:-.18em;color:var(--accent)}
button.fig.epdf{font-family:inherit;margin:0;cursor:pointer}
.fig.epdf:hover{border-color:var(--accent)}
.ghost.epdf{width:auto;height:auto;padding:.2em .6em .2em .42em;border:1.5px solid var(--ink);border-radius:3px;background:var(--sheet);color:var(--ink);
  font-size:calc(var(--body-size) * .72);font-style:italic;line-height:1;white-space:nowrap;box-shadow:0 8px 24px rgba(0,0,0,.2)}
.ghost.epdf.nodrop{opacity:.45}
/* A PDF on the right: its pages in the browser's own reader, under the title and buttons */
.shelf-pdf .pdf-frame{position:absolute;left:0;right:0;bottom:0;top:38px;width:100%;height:calc(100% - 38px);border:0;border-top:1px solid var(--rule);background:var(--paper)}
.shelf-pdf .zoom-tag{cursor:grab}
/* A model a PDF is held over, ready to become a book */
.shelf-item.bind-target{box-shadow:inset 0 0 0 3px var(--accent)}
.shelf-item.bind-target .zoom-tag::after{content:" (let go to make it a book)"}
/* A frame takes the pointer for itself, so while anything is being moved the PDFs let it pass */
body.moving iframe,body.holding iframe{pointer-events:none}
/* Reading a PDF large */
#pdfView{border:1px solid var(--rule);border-radius:10px;background:var(--sheet);color:var(--ink);padding:0;
  width:min(1100px,96vw);height:94vh;max-height:94vh;box-shadow:0 18px 50px rgba(0,0,0,.25);overflow:hidden}
#pdfView[open]{display:flex;flex-direction:column}
#pdfView::backdrop{background:rgba(10,12,11,.55)}
#pdfView .set-head{gap:12px}
#pdfView .set-head span{flex:none;display:flex;gap:8px;align-items:center}
#pdfView .set-head [hidden]{display:none}
#pdfView a.tool{text-decoration:none;color:var(--ink)}
.pdf-view-title{flex:1;min-width:0;font:inherit;font-size:1.15rem;font-style:italic;color:var(--ink);background:none;border:1px solid transparent;border-radius:6px;padding:4px 8px}
.pdf-view-title:hover:not([readonly]){border-color:var(--rule)}
.pdf-view-title:focus{outline:none;border-color:var(--ink)}
#pdfView .pdf-frame{flex:1;width:100%;border:0;border-top:1px solid var(--rule);background:var(--paper)}
/* Reading a PDF as a book: the open book on its boards, filling the screen */
#bookReader{border:0;padding:0;margin:0;background:transparent;width:100vw;height:100vh;max-width:none;max-height:none;overflow:hidden}
#bookReader[open]{display:flex;flex-direction:column}
#bookReader::backdrop{background:rgba(10,12,11,.92)}
/* Taking a book up to read it: the model floats in front of you, and fades away over the reader's book as it lands */
.reader-flight{position:fixed;inset:0;width:100%;height:100%;pointer-events:none;z-index:2;transition:opacity .3s ease}
.reader-flight[hidden]{display:none}
.reader-flight.landing{opacity:0}
.reader-flight.entering{animation:readerIn .18s ease}
@keyframes readerIn{from{opacity:0}}
#bookReader.flying #readerCanvas{opacity:0;pointer-events:none}
#bookReader.flying .reader-note{align-items:flex-end;padding-bottom:10px}
#bookReader.flying::backdrop{animation:readerDim .8s ease both}
#bookReader.flying .reader-bar{animation:readerBarIn .5s ease .45s both}
@keyframes readerDim{from{background:rgba(10,12,11,0)}}
#bookReader.leaving::backdrop{animation:readerUndim .7s ease both}
#bookReader.leaving .reader-bar{transition:opacity .3s ease;opacity:0}
#bookReader.leaving #readerCanvas{opacity:0;pointer-events:none}
#bookReader.leaving .reader-note{display:none}
@keyframes readerUndim{to{background:rgba(10,12,11,0)}}
@keyframes readerBarIn{from{opacity:0}}
.reader-stage{position:relative;flex:1;min-height:0}
#readerCanvas{position:absolute;inset:0;width:100%;height:100%;touch-action:none;outline:none}
.reader-note{position:absolute;inset:0;margin:0;display:flex;align-items:center;justify-content:center;padding:24px;text-align:center;
  color:rgba(243,241,236,.72);font-style:italic;pointer-events:none}
.reader-note[hidden]{display:none}
.reader-bar{align-items:center;padding:10px 24px 18px}
.reader-title{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;color:rgba(243,241,236,.85);font-style:italic;font-size:1.05rem}
.reader-help{flex:none}
.reader-pages{flex:none;color:rgba(243,241,236,.62);font-size:.9rem;font-variant-numeric:tabular-nums}
.reader-go{flex:none;display:flex;align-items:center;gap:6px;color:rgba(243,241,236,.62);font-size:.9rem}
.reader-go input{width:4.8em;font:inherit;color:#F3F1EC;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.3);border-radius:999px;padding:3px 10px}
.reader-go input:focus{outline:none;border-color:rgba(255,255,255,.7)}
@media (max-width:900px){.reader-help{display:none}}
/* Previewing a linked entry: everything in it, read-only, scrolling in its own window */
#linkView{border:1px solid var(--rule);border-radius:10px;background:var(--sheet);color:var(--ink);padding:0;
  width:min(760px,94vw);height:min(86vh,900px);box-shadow:0 18px 50px rgba(0,0,0,.25);overflow:hidden}
#linkView[open]{display:flex;flex-direction:column}
#linkView::backdrop{background:rgba(10,12,11,.35)}
#linkView .set-head{gap:12px}
#linkView .set-head h2{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
#linkView .set-head span{flex:none;display:flex;gap:8px}
#linkView .set-head [hidden]{display:none}
.link-meta{margin:0 0 8px;color:var(--muted);font-size:.86rem;font-style:italic}
#linkViewPanel .link-meta{padding:4px 10px 0}
#linkViewPanel > .quote{max-width:none;margin:22px 10px 20px;font-size:var(--body-size)}
.arch-body.link-body{display:block;margin:0;font-size:var(--body-size);line-height:1.7;background:none;padding:4px 10px 20px}
/* A linked entry shown on the right: it scrolls within its box, and moves about like the pictures there */
.shelf-entry-view{position:absolute;inset:0;overflow-y:auto;padding:42px 16px 16px}
.shelf-entry-view .arch-body.link-body{font-size:calc(var(--body-size) * .82);padding:0}
.shelf-quote .quote{margin:10px 0 4px;max-width:none;font-size:calc(var(--body-size) * .82);--qbg:var(--sheet)}
.shelf-entry .fig img{width:1.1em;height:1.1em;object-fit:cover}
.shelf-entry .tasks img{width:1.1em;height:1.1em}
/* A quote in an entry: a light box with "Quote" set into its top edge, near the left */
.quote{--qline:color-mix(in srgb, var(--ink) 28%, transparent);position:relative;display:block;max-width:42rem;margin:20px 0 16px;
  padding:16px 18px 12px;border:1.5px solid var(--qline);border-radius:3px;white-space:normal;cursor:default}
/* The day a later part of an entry was written on, when it's not the day the entry was begun. */
.written-day{display:block;margin:1.5em 0 .45em;font-size:.8em;font-style:italic;letter-spacing:.03em;line-height:1.3;white-space:normal;
  color:color-mix(in srgb, var(--ink) 42%, transparent);user-select:none;-webkit-user-select:none;cursor:default}
.written-day:first-child{margin-top:.3em}
.quote::before{content:"Quote";position:absolute;left:14px;top:0;transform:translateY(-55%);padding:0 7px;background:var(--qbg, var(--sheet));
  color:color-mix(in srgb, var(--ink) 55%, transparent);font-size:.72em;font-style:italic;letter-spacing:.02em;line-height:1.2}
.quote-text{white-space:pre-wrap;overflow-wrap:break-word;line-height:1.7}
.quote-btns{position:absolute;right:12px;top:0;transform:translateY(-55%);display:flex;gap:6px}
.quote-del,.quote-fold{display:none;background:var(--qbg, var(--sheet));border:1px solid var(--rule);
  border-radius:999px;padding:0 9px;color:var(--accent);font-size:.72rem;line-height:1.5}
.quote-fold{color:var(--ink)}
.quote-del:hover{border-color:var(--accent)}
.quote-fold:hover{border-color:var(--ink)}
.quote:hover .quote-del,.quote:focus-within .quote-del,.quote:hover .quote-fold:not([hidden]),.quote:focus-within .quote-fold:not([hidden]){display:inline-block}
@media (hover:none){.quote-del,.quote-fold:not([hidden]){display:inline-block}}
/* A long quote folded to its first 5 lines, fading out at the bottom */
.quote.folded .quote-text{max-height:calc(1.7em * 5);overflow:hidden;
  -webkit-mask-image:linear-gradient(to bottom, #000 calc(100% - 1.7em), transparent);mask-image:linear-gradient(to bottom, #000 calc(100% - 1.7em), transparent)}
.arch-body{--qbg:var(--paper)}
.arch-body.link-body{--qbg:var(--sheet)}
.arch-body .quote{margin:14px 0 10px}
/* The Quotes menu: each quote in its own box, like a linked entry on the right */
.quote-list{list-style:none;margin:0;padding:6px 0 0;display:flex;flex-direction:column;gap:12px}
.quote-card{position:relative;border:1px solid var(--accent);border-radius:10px;background:var(--sheet);padding:38px 16px 14px;touch-action:none}
.quote-card-bar{position:absolute;left:8px;right:8px;top:8px;display:flex;align-items:center;gap:6px}
.quote-card-bar .zoom-tag{max-width:none;flex:none}
.quote-card-bar .zoom-space{flex:1}
.quote-card .quote-card-del{font-size:.76rem;line-height:1.4;padding:2px 9px;flex:none;cursor:pointer}
/* "Source": pointing at it shows the page the quote came from */
.quote-src{position:relative;flex:none;cursor:default}
.quote-src > .zoom-tag{display:inline-block;color:var(--ink);border:1px solid var(--rule)}
.quote-src-pop{display:none;position:absolute;left:0;top:100%;z-index:5;padding-top:6px;width:max-content;max-width:min(420px,70vw)}
.quote-src:hover .quote-src-pop,.quote-src:focus-within .quote-src-pop{display:block}
.quote-src-box{display:block;padding:10px 14px;background:var(--sheet);border:1px solid var(--rule);border-radius:6px;
  box-shadow:0 6px 20px rgba(0,0,0,.14);font-size:.9rem;line-height:1.45;color:var(--ink);white-space:normal;cursor:auto}
.quote-src-title{display:block;font-weight:600;overflow-wrap:anywhere}
/* A long address is cut to two lines; the whole of it shows when you point at it, and the link still opens it */
.quote-src-url{display:-webkit-box;-webkit-box-orient:vertical;-webkit-line-clamp:2;line-clamp:2;overflow:hidden;margin-top:3px;color:var(--accent);overflow-wrap:anywhere;font-size:.85rem}
.quotes-head-btns{display:flex;gap:8px;align-items:center}
.quote-add-btn{font-size:1.15rem;line-height:1;padding:3px 12px 5px}
.quote-add-btn[aria-expanded="true"]{border-color:var(--ink)}
.quote-form{display:flex;flex-direction:column;gap:8px;padding:6px 24px 10px}
.quote-form[hidden]{display:none}
.quote-form textarea,.quote-form input{font:inherit;font-size:1rem;color:var(--ink);background:var(--paper);border:1px solid var(--rule);border-radius:6px;padding:8px 10px;width:100%}
.quote-form textarea{resize:vertical;min-height:5em;line-height:1.55}
.quote-form textarea:focus,.quote-form input:focus{outline:2px solid var(--ink);outline-offset:1px}
.quote-form-btns{display:flex;align-items:center;justify-content:flex-end;gap:8px}
.quote-form-btns .status{margin-right:auto}
.quote-card-text{white-space:pre-wrap;overflow-wrap:break-word;font-size:calc(var(--body-size) * .82);line-height:1.65;max-height:18em;overflow-y:auto}
body.can-bring-back .quote-card{cursor:grab}
.body .quote{cursor:grab}
.quote.quote-ghost{position:fixed;left:0;top:0;z-index:60;margin:0;max-width:280px;padding:14px 12px 8px;pointer-events:none;background:var(--sheet);
  font-size:.85rem;box-shadow:0 8px 24px rgba(0,0,0,.2);transform:translate(14px,14px) rotate(-1.5deg)}
.quote.quote-ghost .quote-text{display:-webkit-box;-webkit-line-clamp:4;-webkit-box-orient:vertical;overflow:hidden}
body.moving, body.moving *{cursor:grabbing !important;user-select:none;-webkit-user-select:none}
.ghost{position:fixed;left:0;top:0;z-index:60;pointer-events:none;width:44px;height:44px;object-fit:cover;border-radius:3px;opacity:.9;
  box-shadow:0 8px 24px rgba(0,0,0,.25);transform:translate(14px,14px) rotate(-2deg)}
/* The magnified view stays at the top of the right-hand side while the pictures and entries scroll beneath it */
.zoom-view{position:sticky;top:0;z-index:3;flex:none;height:var(--shelf-h);overflow:hidden;background:var(--sheet);border:1px solid var(--rule);border-radius:10px;}
.zoom-view[hidden],.zoom-lens[hidden]{display:none}
.zoom-view.frozen{border-color:var(--accent)}
.zoom-bar{position:absolute;left:8px;right:8px;top:8px;z-index:1;display:flex;align-items:center;gap:6px}
.zoom-bar .zoom-space{flex:1}
.zoom-tag,.zoom-bar button{font-size:.76rem;line-height:1.4;padding:2px 9px;border-radius:999px;background:var(--sheet);white-space:nowrap}
.zoom-tag{max-width:70%;overflow:hidden;text-overflow:ellipsis;color:var(--accent);border:1px solid color-mix(in srgb, var(--accent) 40%, transparent)}
.zoom-bar button{color:var(--ink);border:1px solid var(--rule)}
.zoom-bar button:hover:not(:disabled){border-color:var(--ink)}
.zoom-bar button:disabled{cursor:default;color:var(--muted)}
.zoom-bar [hidden]{display:none}
.zoom-pic{display:block;width:100%;height:100%;object-fit:contain;background:var(--sheet)}
.zoom-drop{position:fixed;z-index:31;pointer-events:none;border:2px dashed var(--accent);border-radius:10px;
  background:color-mix(in srgb, var(--accent) 6%, transparent)}
.zoom-drop[hidden]{display:none}
.shelf{position:fixed;z-index:25;display:flex;flex-direction:column;gap:12px;overflow-y:auto;overscroll-behavior:contain;padding-right:2px}
.shelf[hidden]{display:none}
.shelf-item{position:relative;flex:none;height:var(--shelf-h);border:1px solid var(--accent);border-radius:10px;background:var(--sheet);overflow:hidden}
.shelf-item img{display:block;width:100%;height:100%;object-fit:contain}
/* A 3D model: turned by dragging it, moved to another place by its title */
.model-canvas{display:block;width:100%;height:100%;touch-action:none;cursor:grab;outline:none}
.model-canvas.turning{cursor:grabbing}
.model-canvas:focus-visible{outline:2px solid var(--accent);outline-offset:-3px;border-radius:9px}
.shelf-model .zoom-tag{cursor:grab}
.model-note{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;padding:44px 20px 20px;text-align:center;
  color:var(--muted);font-style:italic;font-size:.95rem;pointer-events:none}
.model-note[hidden]{display:none}
#modelViewer{border:0;padding:0;background:transparent;max-width:96vw;max-height:96vh;overflow:visible}
#modelViewer::backdrop{background:rgba(10,12,11,.88)}
.model-big{position:relative;width:min(1200px,94vw);height:calc(94vh - 64px);background:var(--sheet);border-radius:10px;overflow:hidden}
.model-help{flex:1;align-self:center;color:rgba(243,241,236,.62);font-size:.85rem;font-style:italic}
/* Making a book model */
#bookDialog{border:1px solid var(--rule);border-radius:10px;background:var(--sheet);color:var(--ink);padding:0;
  width:min(1240px,96vw);height:min(860px,94vh);box-shadow:0 18px 50px rgba(0,0,0,.25);overflow:hidden}
#bookDialog[open]{display:flex;flex-direction:column}
#bookDialog::backdrop{background:rgba(10,12,11,.35)}
.book-head-btns{display:flex;gap:8px}
.book-go{background:var(--ink);color:var(--paper);border-color:var(--ink)}
.book-go:hover:not(:disabled){background:var(--accent);border-color:var(--accent)}
.book-go:disabled{opacity:.4}
.book-main{flex:1;min-height:0;display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,1fr);gap:18px;padding:0 24px 20px}
.book-left,.book-right{min-height:0;display:flex;flex-direction:column;gap:10px}
#bookDialog .tabs{padding:6px 0 10px;flex-wrap:wrap}
#bookTabs .tab.has::after{content:"";display:inline-block;width:6px;height:6px;margin-left:6px;vertical-align:middle;border-radius:50%;background:var(--accent)}
#bookTabs .tab.has[aria-selected="true"]::after{background:var(--paper)}
.book-discard{color:var(--accent)}
.book-bands{display:flex;flex-wrap:wrap;gap:6px 16px}
.book-bands[hidden]{display:none}
.book-bands label{display:flex;align-items:center;gap:6px;font-size:.88rem;color:var(--muted)}
.book-bands input{width:110px;accent-color:var(--accent)}
.book-discard.arm{background:#9B2F3F;color:#fff;border-color:#9B2F3F}
.book-head-btns [hidden]{display:none}
.shelf-draft > img{display:block;width:100%;height:100%;object-fit:contain;opacity:.55}
.shelf-draft .zoom-tag{cursor:grab}
.book-crop{position:relative;flex:1;min-height:200px;background:var(--paper);border:1px solid var(--rule);border-radius:10px;overflow:hidden}
.book-crop canvas{position:absolute;inset:0;width:100%;height:100%;touch-action:none}
.book-note{position:absolute;inset:0;margin:0;display:flex;align-items:center;justify-content:center;padding:24px;text-align:center;color:var(--muted);font-style:italic}
.book-note[hidden]{display:none}
.book-tools{display:flex;flex-wrap:wrap;align-items:center;gap:8px}
.book-tools .book-hint{flex:1 1 220px}
.book-tools [hidden]{display:none}
.tool:disabled{opacity:.4}
.book-hint{margin:0;color:var(--muted);font-size:.86rem;font-style:italic}
.book-pics{flex:none;display:flex;gap:8px;overflow-x:auto;padding:2px 2px 6px}
.book-pic{flex:none;width:78px;height:78px;padding:0;border:1px solid var(--rule);border-radius:8px;background:var(--paper);overflow:hidden}
.book-pic img{display:block;width:100%;height:100%;object-fit:cover}
.book-pic:hover{border-color:var(--ink)}
.book-pic.on{border:2px solid var(--accent);box-shadow:0 0 0 2px color-mix(in srgb, var(--accent) 25%, transparent)}
.book-empty{margin:0;color:var(--muted);font-style:italic}
.book-preview{position:relative;flex:1;min-height:200px;border:1px solid var(--rule);border-radius:10px;overflow:hidden;background:var(--paper)}
.book-open-btn{position:absolute;top:10px;right:10px;background:var(--sheet)}
.book-opts{flex:none;display:flex;flex-direction:column;gap:8px}
.book-size{display:flex;flex-wrap:wrap;align-items:center;gap:8px 14px}
.book-size label{display:flex;align-items:center;gap:6px;font-size:.92rem}
.book-size input{width:5.2em;padding:3px 6px;border:1px solid var(--rule);border-radius:6px;background:var(--sheet);color:var(--ink);font:inherit}
.book-size select{padding:3px 6px;border:1px solid var(--rule);border-radius:6px;background:var(--sheet);color:var(--ink);font:inherit}
.book-size [hidden]{display:none}
@media (max-width:820px){.book-main{grid-template-columns:1fr;overflow-y:auto}.book-crop,.book-preview{flex:none;height:44vh}}
.arch-models{grid-template-columns:repeat(auto-fill,minmax(180px,1fr))}
.arch-model-view{position:relative;aspect-ratio:1;border:1px solid var(--rule);border-radius:6px;background:var(--paper);overflow:hidden}
.arch-model-view .model-note{padding:12px;font-size:.82rem}
.arch-grid .arch-model-cap{display:block;margin-top:4px;padding:2px 0;cursor:grab;user-select:none;font-size:.82rem;font-style:italic;color:var(--muted)}
.arch-model-btns{display:flex;flex-wrap:wrap;gap:6px;margin-top:4px}
.arch-grid .arch-model-btns button{width:auto;border:1px solid var(--rule);border-radius:999px;background:none;padding:2px 11px;color:var(--ink);font-size:.82rem;cursor:pointer}
.arch-grid .arch-model-btns button:hover,.arch-grid .arch-model-btns .erase.arm{border-color:var(--accent)}
.arch-grid .arch-model-btns .erase{color:var(--accent);margin-top:0}
body:not(.can-bring-back) .arch-model-add{display:none}
.ghost-model svg{color:var(--accent)}
.pic-menu{position:fixed;z-index:70;display:flex;flex-direction:column;min-width:170px;padding:5px;background:var(--sheet);
  border:1px solid var(--rule);border-radius:10px;box-shadow:0 10px 28px rgba(0,0,0,.18)}
.pic-menu[hidden]{display:none}
.pic-menu button{background:none;border:0;border-radius:6px;padding:6px 12px;text-align:left;color:var(--ink);font:inherit;font-size:.92rem}
.pic-menu button:hover,.pic-menu button:focus-visible{background:var(--sel);outline:none}
.shelf-item{transition:box-shadow .18s ease}
/* Hovering a picture, link or quote in the writing makes its copy on the right light up: a glassy sheen over
   the inside (brightest at the top-left, a soft accent glow gathered at the edges) and only a faint glow outside. */
.shelf-item::after{content:"";position:absolute;inset:0;z-index:2;border-radius:inherit;pointer-events:none;opacity:0;transition:opacity .18s ease;
  background:linear-gradient(155deg, rgba(255,255,255,.26) 0%, rgba(255,255,255,.07) 35%, transparent 55%, color-mix(in srgb, var(--accent) 10%, transparent) 100%);
  box-shadow:inset 0 1px 0 rgba(255,255,255,.45),inset 0 0 0 1px color-mix(in srgb, var(--accent) 55%, transparent),inset 0 0 24px color-mix(in srgb, var(--accent) 22%, transparent)}
.shelf-item.echo::after{opacity:1}
.shelf-item.echo{box-shadow:0 0 5px color-mix(in srgb, var(--accent) 30%, transparent)}
@media (prefers-reduced-motion: reduce){.shelf-item,.shelf-item::after{transition:none}}
/* Pictures on the right can be shrunk in the Menu: at a quarter of full size, four sit side by side in a row.
   Width and height shrink together, and the widths are worked out so a row of them exactly fills the space. */
.shelf-pics{flex:none;display:flex;flex-wrap:wrap;align-content:flex-start;gap:12px}
.shelf-pics > .shelf-item{width:calc(var(--shelf-scale) * (100% + 12px) - 12px - .1px);height:calc(var(--shelf-h) * var(--shelf-scale));
  container-type:inline-size}
/* A picture being drawn on opens out to full size while you draw, and goes back when the drawing is saved */
.shelf-pics > .shelf-item.inked{width:100%;height:var(--shelf-h)}
/* On small pictures the title makes way, and the buttons show when the pointer is over the picture */
@container (max-width:240px){
  .shelf-item .zoom-bar{flex-wrap:wrap;justify-content:flex-end;left:5px;right:5px;top:5px;gap:4px}
  .shelf-item .zoom-bar .zoom-tag,.shelf-item .zoom-bar .zoom-space{display:none}
  .shelf-item .zoom-bar button{padding:1px 7px}
}
@media (hover:hover){
  @container (max-width:240px){
    .shelf-item .zoom-bar{opacity:0;transition:opacity .12s}
    .shelf-item:hover .zoom-bar,.shelf-item:focus-within .zoom-bar{opacity:1}
  }
}
/* Moving a picture to another place on the right: drag it by the picture */
.shelf-pics > .shelf-item{cursor:grab}
.shelf-pics > .shelf-item.drawing,.shelf-pics > .shelf-item.inked{cursor:auto}
.shelf-item.shifting{transition:transform .18s cubic-bezier(.2,.7,.2,1)}
.shelf-item.lifted{z-index:2;box-shadow:0 10px 28px rgba(0,0,0,.22)}
@media (prefers-reduced-motion: reduce){.shelf-item.shifting{transition:none}}
/* Drawing on a picture on the right: its Draw button opens out into the pen tools */
.side-canvas{position:absolute;inset:0;width:100%;height:100%;display:block;touch-action:none;cursor:crosshair}
.side-canvas.done{pointer-events:none}
.shelf-item.drawing > img{visibility:hidden}
.shelf-item.drawing .zoom-bar > :not(.side-draw){visibility:hidden}
.side-draw{position:absolute;left:0;right:0;top:0;display:flex;align-items:center;gap:6px;padding:3px 4px 3px 6px;
  background:var(--sheet);border:1px solid var(--ink);border-radius:16px;box-shadow:0 4px 14px rgba(0,0,0,.14)}
/* All the tools stay in view: when they don't fit on one row they carry on onto the next */
.side-draw-tools{flex:1;min-width:0;display:flex;flex-wrap:wrap;align-items:center;gap:6px 10px;padding:4px 5px;
  scrollbar-width:none;overscroll-behavior-x:contain}
.side-draw-tools::-webkit-scrollbar{display:none}
.side-draw-tools.more-left{-webkit-mask-image:linear-gradient(to right,transparent,#000 18px);mask-image:linear-gradient(to right,transparent,#000 18px)}
.side-draw-tools.more-right{-webkit-mask-image:linear-gradient(to left,transparent,#000 18px);mask-image:linear-gradient(to left,transparent,#000 18px)}
.side-draw-tools.more-left.more-right{-webkit-mask-image:linear-gradient(to right,transparent,#000 18px,#000 calc(100% - 18px),transparent);
  mask-image:linear-gradient(to right,transparent,#000 18px,#000 calc(100% - 18px),transparent)}
.side-draw .draw-group{flex:none;gap:5px}
.side-draw .swatch{flex:none;width:18px;height:18px;padding:0;border-radius:50%}
.side-draw .size{flex:none;width:20px;height:20px;padding:0;border-radius:50%;background:none}
.side-draw .tool{flex:none}
.side-draw-end{flex:none;display:flex;align-items:center;gap:6px}
.side-draw .draw-done{flex:none;font-size:.76rem;line-height:1.4;padding:2px 11px;border:1px solid var(--ink);background:var(--ink);color:var(--paper)}
.side-draw .draw-done:hover{background:var(--accent);border-color:var(--accent)}
.side-draw .swatch.hl{border-radius:4px}
/* Ink and highlighting over a linked entry on the right: it lies over the writing and scrolls with it */
.shelf-entry-page{position:relative}
/* An entry with pen marks on it keeps the layout it had when they were drawn, scaled to fit its box */
.shelf-entry-view.frozen{scrollbar-gutter:stable}
/* Highlights lie on the words themselves, so they move with them */
.shelf-entry mark.ink-hl{background:color-mix(in srgb, var(--hl) 42%, transparent);color:inherit;border-radius:2px;
  padding:.06em 0;-webkit-box-decoration-break:clone;box-decoration-break:clone;mix-blend-mode:multiply}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]) .shelf-entry mark.ink-hl{mix-blend-mode:screen}}
:root[data-theme="dark"] .shelf-entry mark.ink-hl{mix-blend-mode:screen}
.shelf-entry .shelf-ink{position:absolute;left:0;top:0;width:100%;height:auto;object-fit:fill;pointer-events:none}
.shelf-entry .side-canvas{bottom:auto;height:auto}
.shelf-entry.drawing .shelf-ink{visibility:hidden}
/* Like a real highlighter, the colour tints the writing beneath without covering it */
.shelf-entry .shelf-ink,.shelf-entry .side-canvas{mix-blend-mode:multiply}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]) .shelf-entry .shelf-ink,:root:not([data-theme="light"]) .shelf-entry .side-canvas{mix-blend-mode:screen}}
:root[data-theme="dark"] .shelf-entry .shelf-ink,:root[data-theme="dark"] .shelf-entry .side-canvas{mix-blend-mode:screen}
.zoom-hint{position:absolute;inset:0;display:grid;place-items:center;padding:16px;text-align:center;color:var(--muted);font-style:italic;font-size:.92rem}
.set-key{min-width:120px;background:none;border:1px solid var(--rule);border-radius:6px;padding:3px 10px;color:var(--ink);font-size:.9rem}
.set-key:hover{border-color:var(--ink)}
.set-key.listening{border-color:var(--accent);color:var(--accent);font-style:italic}
.zoom-copy{position:absolute;left:0;top:0;margin:0;transform-origin:0 0;min-height:0 !important;padding-bottom:0 !important}
.zoom-lens{position:fixed;z-index:30;pointer-events:none;border:1px solid color-mix(in srgb, var(--accent) 55%, transparent);border-radius:4px;
  background:color-mix(in srgb, var(--accent) 5%, transparent)}
#zoomBtn[aria-pressed="true"]{background:var(--ink);color:var(--paper);border-color:var(--ink)}
.drop-mark{position:fixed;z-index:59;pointer-events:none;background:var(--accent);border-radius:2px;display:none;width:3px}

.attach{background:none;border:1px solid var(--rule);border-radius:999px;padding:3px 12px;color:var(--ink);font-size:.9rem}
.attach:hover{border-color:var(--ink)}
#viewer{border:0;padding:0;background:transparent;max-width:96vw;max-height:96vh;overflow:visible}
#viewer::backdrop{background:rgba(10,12,11,.88)}
#viewerImg{display:block;max-width:96vw;max-height:calc(96vh - 112px);object-fit:contain;margin:0 auto}
.viewer-title{display:block;width:min(560px,90vw);margin:12px auto 0;padding:4px 8px;background:transparent;border:0;border-bottom:1px solid rgba(255,255,255,.28);
  color:#F3F1EC;font:inherit;font-size:1.08rem;font-style:italic;text-align:center;outline:none}
.viewer-title::placeholder{color:rgba(243,241,236,.5)}
.viewer-title:hover{border-bottom-color:rgba(255,255,255,.5)}
.viewer-title:focus{border-bottom-color:#F3F1EC}
.viewer-title[readonly]{border-bottom-color:transparent;cursor:default}
.viewer-title[hidden]{display:none}
.viewer-bar{display:flex;justify-content:flex-end;gap:10px;padding-top:12px}
.viewer-bar button{background:var(--sheet);color:var(--ink);border:1px solid rgba(255,255,255,.35);border-radius:999px;padding:6px 16px}
.viewer-bar .rm{background:none;color:#E9D9DB;border:1px solid rgba(255,255,255,.35)}

.empty{max-width:34ch;margin:18vh auto 0;text-align:center;color:var(--muted);padding:0 24px}
.empty p{font-size:1.35rem;font-style:italic;line-height:1.5;color:var(--ink);margin:0 0 20px}
.empty .new{font-size:1rem;padding:8px 20px}

@media (max-width:720px){
  .app{grid-template-columns:1fr}
  aside{border-right:0}
  body.editing aside{display:none}
  body:not(.editing) main{display:none}
  .back{display:inline-block}
  .page{padding:24px 20px 0}
  .page > .scroll{max-width:none;padding:0 8px 80px 0}
}
</style>
</head>
<body>
<div class="app">
  <aside>
    <div class="side-head">
      <h1 class="brand">Journal</h1>
      <button class="new" id="newBtn" type="button">New entry</button>
    </div>
    <input class="search" id="search" type="search" placeholder="Search entries" aria-label="Search entries">
    <div class="list-view">
      <div class="view-tabs" role="radiogroup" aria-label="Show entries">
        <button class="view-tab" type="button" role="radio" data-view="recent" title="Newest changes first">Most recent</button>
        <button class="view-tab" type="button" role="radio" data-view="changes" title="Entries written in on the most days first">Most changes</button>
        <button class="view-tab" type="button" role="radio" data-view="topic" title="Only entries with the topics you choose">By topic</button>
      </div>
      <div class="view-topics" id="viewTopics" hidden></div>
    </div>
    <ul class="list" id="list" aria-label="Entries"></ul>
    <div class="foot">
      <p class="where" id="where" aria-live="polite"></p>
      <button class="menu-btn" id="menuBtn" type="button">Menu</button>
      <button class="menu-btn" id="archiveBtn" type="button">Archive</button>
      <button class="menu-btn" id="tasksMenuBtn" type="button">Tasks</button>
      <button class="menu-btn" id="logMenuBtn" type="button">Log</button>
      <button class="menu-btn" id="topicsMenuBtn" type="button">Topics</button>
      <button class="menu-btn" id="quotesMenuBtn" type="button">Quotes</button>
    </div>
  </aside>
  <main id="main">
    <div class="empty" id="empty">
      <p>Somewhere to put the ideas before they wander off.</p>
      <button class="new" id="newBtn2" type="button">New entry</button>
    </div>
    <div class="page" id="page" hidden>
      <button class="back" id="back" type="button">All entries</button>
      <input class="title" id="title" placeholder="Untitled" aria-label="Title" autocomplete="off">
      <div class="topic-row" id="topicRow">
        <span class="topic-name" id="topicName" hidden></span>
        <button class="topic-btn" id="topicBtn" type="button" aria-haspopup="true" aria-expanded="false" aria-controls="topicPop"
          title="Choose topics for this entry" aria-label="Choose topics for this entry">+</button>
        <div class="topic-pop" id="topicPop" hidden></div>
      </div>
      <div class="meta">
        <span id="created"></span>
        <span id="words"></span>
        <span class="status" id="status" aria-live="polite"></span>
        <span class="actions">
        <button class="attach" id="attach" type="button" title="Add pictures, PDFs or 3D models">Add files</button>
        <input id="file" type="file" accept="image/png,image/jpeg,image/gif,image/webp,image/avif,.pdf,application/pdf,.glb,.gltf,model/gltf-binary" multiple hidden>
        <span class="hist" id="hist" hidden>
          <button class="hist-btn" type="button" aria-describedby="histPop">History</button>
          <span class="hist-pop" id="histPop" role="tooltip"><ul id="histList"></ul></span>
        </span>
        <button class="attach" id="drawBtn" type="button">Draw</button>
        <button class="attach" id="tasksBtn" type="button">Task</button>
        <button class="attach" id="subBtn" type="button" title="Start a new sub-entry here: a numbered break where the topic changes">Entry</button>
        <button class="attach" id="subSubBtn" type="button" title="Start a sub-entry within the current one: I.I, I.II and so on">Sub entry</button>
        <button class="attach" id="boldBtn" type="button" aria-pressed="false" title="Make the selected writing bold (click again to take it off)">Bold</button>
        <button class="attach" id="underlineBtn" type="button" aria-pressed="false" title="Underline the selected writing (click again to take it off)">Underline</button>
        <button class="attach" id="zoomBtn" type="button" aria-pressed="false" >Zoom</button>
        <button class="del" id="del" type="button">Archive</button>
        <button class="del forever" id="delForever" type="button">Delete forever</button>
        </span>
      </div>
      <div class="scroll" id="scroll">
        <div class="body" id="body" role="textbox" aria-multiline="true" aria-label="Entry" data-placeholder="Write it down…" spellcheck="true"></div>
      </div>
    </div>
  </main>
</div>
<div class="drop-mark" id="dropMark"></div>
<div class="zoom-lens" id="zoomLens" hidden></div>
<div class="shelf" id="shelf" hidden aria-label="Pictures and linked entries beside the entry">
  <div class="zoom-view" id="zoomView" hidden aria-hidden="true"></div>
  <div class="shelf-pics" id="shelfPics"></div>
</div>
<dialog id="archive" aria-labelledby="archiveTitle">
  <div class="set-head">
    <h2 id="archiveTitle">Archive</h2>
    <span class="quotes-head-btns">
      <button class="tool quote-add-btn" id="archNewFolder" type="button" title="New folder" aria-label="New folder" hidden>+</button>
      <button class="tool" id="archiveClose" type="button">Close</button>
    </span>
  </div>
  <div class="tabs" role="tablist" aria-label="Archive">
    <button class="tab" id="tabEntries" role="tab" type="button" aria-selected="true" aria-controls="archEntries">Entries</button>
    <button class="tab" id="tabImages" role="tab" type="button" aria-selected="false" aria-controls="archImages">Images</button>
    <button class="tab" id="tabArchModels" role="tab" type="button" aria-selected="false" aria-controls="archModels">Models</button>
    <button class="tab" id="tabArchTasks" role="tab" type="button" aria-selected="false" aria-controls="archTasks">Tasks</button>
  </div>
  <div class="arch-panel" id="archEntries" role="tabpanel" aria-labelledby="tabEntries"></div>
  <div class="arch-panel" id="archImages" role="tabpanel" aria-labelledby="tabImages" hidden></div>
  <div class="arch-panel" id="archModels" role="tabpanel" aria-labelledby="tabArchModels" hidden></div>
  <div class="arch-panel" id="archTasks" role="tabpanel" aria-labelledby="tabArchTasks" hidden></div>
</dialog>
<dialog id="linkView" aria-labelledby="linkViewTitle">
  <div class="set-head">
    <h2 id="linkViewTitle"></h2>
    <span><button class="tool" id="linkViewOpen" type="button">Open entry</button><button class="tool" id="linkViewClose" type="button">Close</button></span>
  </div>
  <div class="arch-panel" id="linkViewPanel"></div>
</dialog>
<dialog id="tasksDialog" aria-labelledby="tasksTitle">
  <div class="set-head">
    <h2 id="tasksTitle">Tasks</h2>
    <button class="tool" id="tasksClose" type="button">Close</button>
  </div>
  <div class="tabs" role="tablist" aria-label="Tasks">
    <button class="tab" id="tabOngoing" role="tab" type="button" aria-selected="true" aria-controls="tasksPanel">Ongoing</button>
    <button class="tab" id="tabDone" role="tab" type="button" aria-selected="false" aria-controls="tasksPanel">Done</button>
    <span class="task-sort" role="radiogroup" aria-label="List tasks by">
      <span class="lbl">List by</span>
      <button class="view-tab" type="button" role="radio" data-sort="entries" title="Under the entry each task is in">Entry</button>
      <button class="view-tab" type="button" role="radio" data-sort="urgency" title="High, then Medium, then Low">Urgency</button>
      <button class="view-tab" type="button" role="radio" data-sort="due" title="Tasks with a finish time first, the soonest at the top">Ending soonest</button>
    </span>
  </div>
  <div class="arch-panel" id="tasksPanel"></div>
</dialog>
<dialog id="logDialog" aria-labelledby="logTitleHead">
  <div class="set-head">
    <h2 id="logTitleHead">Log</h2>
    <span class="quotes-head-btns">
      <button class="tool quote-add-btn" id="logAddBtn" type="button" title="Log an activity" aria-label="Log an activity" aria-expanded="false">+</button>
      <button class="tool" id="logClose" type="button">Close</button>
    </span>
  </div>
  <div class="quote-form log-form" id="logForm" hidden>
    <h3 class="log-form-title" id="logFormTitle">Log an activity</h3>
    <div class="log-row" id="logModeRow" role="radiogroup" aria-label="The activity has">
      <label class="log-radio"><input type="radio" name="logMode" value="start" checked> Just started</label>
      <label class="log-radio"><input type="radio" name="logMode" value="finish"> Finished</label>
    </div>
    <div class="log-row" id="logWhichRow" hidden>
      <label for="logWhich">Which</label>
      <select id="logWhich"></select>
    </div>
    <input id="logTitle" type="text" placeholder="Title" aria-label="Title" autocomplete="off" maxlength="500">
    <textarea id="logDesc" rows="3" placeholder="Description (optional)" aria-label="Description"></textarea>
    <div class="log-row">
      <label for="logWhen" id="logWhenLabel">Started at</label>
      <input id="logWhen" type="datetime-local">
      <button class="tool" id="logNow" type="button">Now</button>
    </div>
    <div class="log-row" id="logBeganRow" hidden>
      <label for="logBegan">Started at</label>
      <input id="logBegan" type="datetime-local">
      <span class="log-hint">if you know</span>
    </div>
    <div class="log-row" id="logEndRow" hidden>
      <label for="logEnd">Finished at</label>
      <input id="logEnd" type="datetime-local">
      <span class="log-hint">empty while it's ongoing</span>
    </div>
    <div class="log-row log-pic-row">
      <button class="tool" id="logPicBtn" type="button">Add pictures</button>
      <input id="logFile" type="file" accept="image/png,image/jpeg,image/gif,image/webp,image/avif" multiple hidden>
      <span class="log-hint">or paste or drop them here</span>
    </div>
    <div class="log-form-pics" id="logPics"></div>
    <div class="quote-form-btns">
      <span class="status" id="logFormNote" aria-live="polite"></span>
      <button class="tool" id="logCancel" type="button">Cancel</button>
      <button class="draw-done" id="logSave" type="button">Save</button>
    </div>
  </div>
  <div class="arch-panel" id="logPanel"></div>
</dialog>
<dialog id="logPic" aria-label="Picture"><img id="logPicImg" alt="Picture"></dialog>
<dialog id="quotesDialog" aria-labelledby="quotesTitle">
  <div class="set-head">
    <h2 id="quotesTitle">Quotes</h2>
    <span class="quotes-head-btns">
      <button class="tool quote-add-btn" id="quoteAddBtn" type="button" title="Add a quote" aria-label="Add a quote" aria-expanded="false">+</button>
      <button class="tool" id="quotesClose" type="button">Close</button>
    </span>
  </div>
  <div class="quote-form" id="quoteForm" hidden>
    <textarea id="quoteText" rows="4" placeholder="The words of the quote" aria-label="The words of the quote"></textarea>
    <input id="quoteSource" type="url" placeholder="Where it's from: a web address (optional)" aria-label="Where it's from (optional)" autocomplete="off">
    <div class="quote-form-btns">
      <span class="status" id="quoteFormNote" aria-live="polite"></span>
      <button class="tool" id="quoteCancel" type="button">Cancel</button>
      <button class="draw-done" id="quoteSave" type="button">Add quote</button>
    </div>
  </div>
  <div class="arch-panel" id="quotesPanel"></div>
</dialog>
<dialog id="topicsDialog" aria-labelledby="topicsTitle">
  <div class="set-head">
    <h2 id="topicsTitle">Topics</h2>
    <button class="tool" id="topicsClose" type="button">Close</button>
  </div>
  <div class="arch-panel" id="topicsPanel">
    <ol class="topic-list" id="topicList"></ol>
    <p class="arch-note" id="topicsEmpty">No topics yet. Name your first one below.</p>
    <div class="topic-add">
      <span class="topic-num" id="topicNextNum">1</span>
      <input class="topic-input" id="topicNew" type="text" placeholder="New topic" aria-label="Name of the new topic" autocomplete="off" maxlength="120">
      <button class="tool" id="topicAdd" type="button">Add topic</button>
    </div>
  </div>
</dialog>
<dialog id="settings" aria-labelledby="settingsTitle">
  <div class="set-head">
    <h2 id="settingsTitle">Menu</h2>
    <button class="tool" id="settingsClose" type="button">Close</button>
  </div>
  <section aria-labelledby="exportTitle">
    <h3 id="exportTitle">Export</h3>
    <div class="export-row">
      <button class="tool" id="exportBtn" type="button" title="Save the open entry as a PDF in journal/exports, named by its title">Export as PDF</button>
      <span class="status" id="exportNote" aria-live="polite"></span>
    </div>
    <div id="exportRows"></div>
  </section>
  <section aria-labelledby="sizesTitle">
    <h3 id="sizesTitle">Text size</h3>
    <div id="sizeRows"></div>
  </section>
  <section aria-labelledby="coloursTitle">
    <h3 id="coloursTitle">Colours</h3>
    <div id="colourRows"></div>
  </section>
  <section aria-labelledby="imagesTitle">
    <h3 id="imagesTitle">Images in entries</h3>
    <div id="imageRows"></div>
  </section>
  <section aria-labelledby="fmtSetTitle">
    <h3 id="fmtSetTitle">Bold and underline</h3>
    <div id="fmtRows"></div>
  </section>
  <section aria-labelledby="taskSetTitle">
    <h3 id="taskSetTitle">Tasks</h3>
    <div id="taskRows"></div>
  </section>
  <section aria-labelledby="subSetTitle">
    <h3 id="subSetTitle">Sub-entries</h3>
    <div id="subRows"></div>
  </section>
  <section aria-labelledby="zoomSetTitle">
    <h3 id="zoomSetTitle">Zoom and pictures on the right</h3>
    <div id="zoomRows"></div>
  </section>
  <section aria-labelledby="readSetTitle">
    <h3 id="readSetTitle">Reading books</h3>
    <div id="readRows"></div>
  </section>
  <section aria-labelledby="logSetTitle">
    <h3 id="logSetTitle">Log</h3>
    <div id="logRows"></div>
    <div id="logKeysNote"></div>
  </section>
  <div class="set-foot">
    <button class="tool" id="resetAll" type="button">Reset everything</button>
    <span class="status" id="settingsStatus" aria-live="polite"></span>
  </div>
</dialog>
<div class="draw" id="draw" hidden role="dialog" aria-label="Drawing">
  <div class="draw-bar">
    <div class="draw-group" id="swatches" aria-label="Pen colour"></div>
    <div class="draw-group" id="hlSwatches" aria-label="Highlighter colour"></div>
    <div class="draw-group" id="sizes" aria-label="Pen size"></div>
    <div class="draw-group">
      <button class="tool pen-btn" id="pen" type="button" aria-pressed="true">Pen</button>
      <button class="tool hl-btn" id="highlighter" type="button" aria-pressed="false">Highlighter</button>
      <button class="tool eraser-btn" id="eraser" type="button" aria-pressed="false">Eraser</button>
      <button class="tool" id="undo" type="button">Undo</button>
      <button class="tool" id="clear" type="button">Clear</button>
    </div>
    <span class="spacer"></span>
    <button class="tool" id="discard" type="button">Discard</button>
    <button class="draw-done" id="drawDone" type="button">Done</button>
  </div>
  <canvas id="canvas"></canvas>
</div>
<dialog id="bookDialog" aria-labelledby="bookTitle">
  <div class="set-head">
    <h2 id="bookTitle">Book model</h2>
    <span class="book-head-btns"><button class="tool book-discard" id="bookDiscard" type="button" title="Throw this draft away (the photos stay in the entry)" hidden>Discard draft</button><button class="tool" id="bookCancel" type="button">Cancel</button><button class="tool" id="bookDraft" type="button" title="Keep the model as it is so far, to carry on with later from the right of the entry">Save draft</button><button class="tool book-go" id="bookMake" type="button">Make model</button></span>
  </div>
  <div class="book-main">
    <div class="book-left">
      <div class="tabs" id="bookTabs" role="tablist" aria-label="Side of the book">
        <button class="tab" type="button" role="tab" data-face="front">Front</button>
        <button class="tab" type="button" role="tab" data-face="spine">Spine</button>
        <button class="tab" type="button" role="tab" data-face="back">Back</button>
        <button class="tab" type="button" role="tab" data-face="pages">Page edges</button>
        <button class="tab" type="button" role="tab" data-face="inside">Inside</button>
        <button class="tab" type="button" role="tab" data-face="endsheet">Endpaper</button>
        <button class="tab" type="button" role="tab" data-face="leaf">Paper</button>
        <button class="tab" type="button" role="tab" data-face="boardEdges">Board edges</button>
        <button class="tab" type="button" role="tab" data-face="headcap">Headcap</button>
        <button class="tab" type="button" role="tab" data-face="tailcap">Tailcap</button>
      </div>
      <div class="book-crop"><canvas id="bookCrop" aria-label="The photo, with four corners to drag onto the corners of the book. Scroll to zoom in, drag the photo to move it"></canvas><p class="book-note" id="bookCropNote"></p></div>
      <div class="book-tools">
        <span class="book-hint" id="bookFaceHint"></span>
        <button class="tool" id="bookTurn" type="button" title="Turn a quarter turn, to put Top on the right edge">Turn</button>
        <button class="tool" id="bookWhole" type="button" title="Use the whole photo, for one already cropped to the book">Whole photo</button>
        <button class="tool" id="bookStraight" type="button" title="Take away the points added along the sides" disabled>Straight sides</button>
        <button class="tool" id="bookNone" type="button">No photo</button>
        <button class="tool" id="bookFit" type="button" title="Zoom back out to the whole photo (or double-click beside the outline)" disabled>Fit</button>
      </div>
      <div class="book-pics" id="bookPics" aria-label="The entry's pictures"></div>
    </div>
    <div class="book-right">
      <div class="book-preview"><canvas id="bookPreview" class="model-canvas" aria-label="The book model. Drag to turn it, scroll to zoom"></canvas><div class="model-note" id="bookPreviewNote" hidden></div><button class="tool book-open-btn" id="bookOpen" type="button" aria-pressed="false" title="See the book lying open, at its endpapers">Show open</button></div>
      <div class="book-opts">
        <div class="book-size">
          <label>Height <input id="bookH" type="number" min="0.1" step="0.1" inputmode="decimal"></label>
          <label>Width <input id="bookW" type="number" min="0.1" step="0.1" inputmode="decimal"></label>
          <label>Thickness <input id="bookT" type="number" min="0.1" step="0.1" inputmode="decimal"></label>
          <button class="tool" id="bookFromPhotos" type="button" hidden>From the photos</button>
        </div>
        <p class="book-hint">Any units: only the proportions matter. They start out as the photos suggest.</p>
        <div class="book-size">
          <label>Page edges <select id="bookEdges"><option value="plain">Plain</option><option value="gilt">Gilt</option><option value="giltTop">Gilt top</option><option value="red">Sprinkled red</option><option value="photo" id="bookEdgesPhoto" disabled>From the photo</option></select></label>
          <label title="The paper the pages are printed on, seen as the book is read">Paper <select id="bookLeaf"><option value="white">White</option><option value="cream">Cream</option><option value="aged">Aged</option><option value="laid">Laid</option><option value="rough">Handmade</option><option value="photo" id="bookLeafPhoto" disabled>From the photo</option></select></label>
          <label title="The endpapers: pasted inside the boards, over the turned-in edges of the covering, and a free leaf at the start and the end of the book">Endpapers <select id="bookEnds"><option value="plain">Plain</option><option value="marbled">Marbled</option><option value="combed">Combed</option><option value="stone">Stone</option><option value="none">None</option><option value="photo" id="bookEndsPhoto" disabled>From the photo</option></select></label>
          <label title="The headbands: little rolls of silk worked over in two colours, at the head and the tail of the spine, where the pages meet it">Headbands <select id="bookHeadband"><option value="red">Red and white</option><option value="green">Green and white</option><option value="blue">Blue and white</option><option value="black">Black and white</option><option value="brown">Brown and white</option><option value="redgold">Red and gold</option><option value="greengold">Green and gold</option><option value="bluegold">Blue and gold</option><option value="none">None</option></select></label>
          <label>Spine <select id="bookSpine"><option value="round">Rounded</option><option value="flat">Flat</option></select></label>
          <label>Bands <select id="bookBands"><option value="0">None</option><option value="1">1</option><option value="2">2</option><option value="3">3</option><option value="4">4</option><option value="5">5</option></select></label>
        </div>
        <div class="book-size">
          <label title="What the back cover shows: its own photo (or the cover's colour), or the front's photo, flipped across the spine or just as it is">Back cover <select id="bookBackFrom"><option value="own">Its own photo</option><option value="mirror">The front, mirrored</option><option value="same">The front, as it is</option></select></label>
          <label title="What the inside of the back board shows: the inside of the front board (its photo and endpaper), flipped across the spine or just as it is">Inside of the back <select id="bookInsideBack"><option value="mirror">The front's, mirrored</option><option value="same">The front's, as it is</option></select></label>
        </div>
        <div class="book-bands" id="bookBandPos" hidden></div>
        <div class="book-bands" id="bookRimBox" hidden><label title="How large the board edges’ photo is along the edges: 100% is its true size">Edge pattern <input id="bookRim" type="range" min="25" max="400" step="5" value="100"> <span id="bookRimPct">100%</span></label></div>
      </div>
    </div>
  </div>
</dialog>
<dialog id="modelViewer" aria-label="3D model">
  <div class="model-big">
    <canvas id="modelCanvas" class="model-canvas" aria-label="3D model. Drag to turn it, scroll to zoom, Shift and drag to move it sideways, double-click to put it back as it was"></canvas>
    <div class="model-note" id="modelNote" hidden></div>
  </div>
  <div class="viewer-bar">
    <span class="model-help">Drag to turn, scroll to zoom, Shift+drag to move, double-click to reset</span>
    <button id="modelRead" type="button" hidden>Read</button>
    <button class="rm" id="modelUnbind" type="button" hidden title="It goes back to being a model; the PDF stays in the entry">Take out the PDF</button>
    <button id="modelReset" type="button">Reset</button>
    <button class="rm" id="modelArchive" type="button">Archive</button>
    <button class="forever" id="modelForever" type="button">Delete forever</button>
    <button id="modelClose" type="button">Close</button>
  </div>
</dialog>
<dialog id="pdfView" aria-label="PDF">
  <div class="set-head">
    <input class="pdf-view-title" id="pdfViewTitle" type="text" placeholder="Untitled PDF" aria-label="PDF title" autocomplete="off" spellcheck="true">
    <span>
      <button class="tool" id="pdfViewRead" type="button" title="Open it as a book and turn its pages">Read as a book</button>
      <a class="tool" id="pdfViewTab" href="#" target="_blank" rel="noopener" title="The browser's full PDF reader, to print it or save a copy">Open in new tab</a>
      <button class="tool forever" id="pdfViewForever" type="button" title="Take it out of this entry and erase the file (kept if another entry still has it)">Delete forever</button>
      <button class="tool" id="pdfViewClose" type="button">Close</button>
    </span>
  </div>
  <iframe class="pdf-frame" id="pdfViewFrame" title="PDF"></iframe>
</dialog>
<dialog id="bookReader" aria-label="Reading a PDF as a book">
  <div class="reader-stage" id="readerStage">
    <canvas id="readerCanvas" tabindex="0" aria-label="The open book. Drag a page's corner to turn it, click a page, or use the arrow keys"></canvas>
    <p class="reader-note" id="readerNote" hidden></p>
  </div>
  <canvas class="reader-flight" id="readerFlight" aria-hidden="true" hidden></canvas>
  <div class="viewer-bar reader-bar">
    <span class="reader-title" id="readerTitle"></span>
    <span class="model-help reader-help">Drag a corner, click a page, or use the arrow keys</span>
    <span class="reader-pages" id="readerPages" aria-live="polite"></span>
    <label class="reader-go">Page <input id="readerGo" type="number" min="1" inputmode="numeric" disabled></label>
    <button id="reader3d" type="button" aria-pressed="true" title="Show a book made with one of the journal's book models lying open in 3D, seen from a little below, or flat, from straight above">3D</button>
    <button id="readerClose" type="button">Close</button>
  </div>
</dialog>
<dialog id="viewer" aria-label="Image">
  <img id="viewerImg" alt="">
  <input class="viewer-title" id="viewerTitle" type="text" placeholder="Untitled picture" aria-label="Picture title" autocomplete="off" spellcheck="true">
  <div class="viewer-bar">
    <button id="viewerBook" type="button" title="Make a 3D model of a book, with this picture as its front cover">Make book model</button>
    <button id="viewerDraw" type="button">Draw</button>
    <button id="viewerRestore" type="button" hidden>Restore</button>
    <button class="rm" id="viewerRemove" type="button">Archive</button>
    <button class="forever" id="viewerForever" type="button">Delete forever</button>
    <button id="viewerClose" type="button">Close</button>
  </div>
</dialog>

<script>
const $ = id => document.getElementById(id);
const els = {list:$('list'), search:$('search'), where:$('where'), empty:$('empty'), page:$('page'), main:$('main'), scroll:$('scroll'),
  title:$('title'), body:$('body'), created:$('created'), words:$('words'), status:$('status'), del:$('del'),
  file:$('file'), hist:$('hist'), histList:$('histList'), viewer:$('viewer'), viewerImg:$('viewerImg'), mark:$('dropMark')};

const entries = new Map();   // id -> {title, body, created, updated, images}
const dirty = new Set();     // ids with edits not yet confirmed saved
const unsaved = new Set();   // ids that have never been written
const timers = new Map();
const writes = new Map();
let currentId = null, store = null, loaded = false, query = '';

/* Images live inside the entry text as Markdown image links, e.g. ![Beach at dusk.jpg](../images/ab12….jpg).
   The words in the brackets are the picture's title (at first, the name of the file it was added from).
   The "../" points from the entries folder to the images folder; older entries without it still work. */
const TOKEN_SRC = '!\\[([^\\]\\n]*)\\]\\((?:\\.\\.\\/)?images\\/([a-f0-9]{32}\\.(?:png|jpg|gif|webp|avif))\\)';
const cleanTitle = t => String(t || '').replace(/[\[\]\r\n]+/g, ' ').replace(/\s+/g, ' ').trim().slice(0, 200);
const token = (name, title) => '![' + cleanTitle(title) + '](../images/' + name + ')';
const swapImage = (body, oldName, newName) =>
  body.replace(new RegExp(TOKEN_SRC, 'g'), (m, title, n) => n === oldName ? token(newName, title) : m);
const plainText = body => body.replace(/(^|\n)<!-- day \d{4}-\d{2}-\d{2}(?: \d{2}:\d{2})? -->(?:\n|$)/g, '$1').replace(/(^|\n)<!-- quote -->\n/g, '$1').replace(/^> ?/gm, '').replace(/<\/?[bu]>/g, '').replace(new RegExp(TOKEN_SRC, 'g'), ' ').replace(new RegExp(LINK_SRC, 'g'), '$1').replace(new RegExp(PDF_SRC, 'g'), '$1').replace(/## [IVXLCDM]+ <!-- sub-entry -->|### [IVXLCDM]+\.[IVXLCDM]+ <!-- sub-sub-entry -->/g, ' ').replace(/\s*<!--\s*(?:created|due|marked|urgency) [^\n]*?-->/g, '');
const imagesIn = body => [...body.matchAll(new RegExp(TOKEN_SRC, 'g'))].map(m => m[2]);
// A link to another entry is an ordinary Markdown link to that entry's file, e.g. [Holiday plans](e1ab2c3d4.md).
// The words in the brackets are the entry's title when it was linked; the link always shows the title it has now.
const LINK_SRC = '\\[([^\\]\\n]*)\\]\\(([A-Za-z0-9_-]{1,80})\\.md\\)';
const linkToken = (id, title) => '[' + cleanTitle(title) + '](' + id + '.md)';
const linksIn = body => [...body.matchAll(new RegExp(LINK_SRC, 'g'))].map(m => m[2]);
// A PDF is an ordinary Markdown link to its file in journal/pdfs, e.g. [Receipt](../pdfs/ab12….pdf).
// The words in the brackets are its title (at first, the name of the file it was added from).
const PDF_SRC = '\\[([^\\]\\n]*)\\]\\((?:\\.\\.\\/)?pdfs\\/([a-f0-9]{32}\\.pdf)\\)';
const pdfToken = (name, title) => '[' + cleanTitle(title) + '](../pdfs/' + name + ')';
const pdfsIn = body => [...body.matchAll(new RegExp(PDF_SRC, 'g'))].map(m => m[2]);
function pdfTitleIn(body, name){
  for (const m of body.matchAll(new RegExp(PDF_SRC, 'g'))) if (m[2] === name) return m[1].trim();
  return '';
}
// The title given to a picture in an entry (its first appearance), or '' if it has none.
function titleIn(body, name){
  for (const m of body.matchAll(new RegExp(TOKEN_SRC, 'g'))) if (m[2] === name) return m[1].trim();
  return '';
}

const fmtDate = new Intl.DateTimeFormat(undefined,{day:'numeric',month:'long',year:'numeric'});
const fmtTime = new Intl.DateTimeFormat(undefined,{hour:'numeric',minute:'2-digit'});
function when(ts){
  const d = new Date(ts), now = new Date();
  return d.toDateString() === now.toDateString() ? 'Today, ' + fmtTime.format(d) : fmtDate.format(d);
}
function sameDay(a, b){ return new Date(a).toDateString() === new Date(b).toDateString(); }
function newId(){ return 'e' + Date.now().toString(36) + Math.random().toString(36).slice(2,8); }
function isEmpty(e){ return !e.title.trim() && !e.body.trim(); }

/* ---------- Text <-> parts ---------- */
// Each picture is written into the text exactly where it sits, as ![](images/…).
// Task lists are written as numbered Markdown lines on their own:
//   1. [ ] not marked    2. [x] success    3. [-] failure
// A task can end with a note of when it was made and when it should be finished by:
//   1. [ ] Ring the bank <!-- created 2026-09-22 14:05; due 2026-09-25 17:00; urgency high -->
// (urgency is high, medium or low)
// A marked task also notes when it was marked:  2. [x] Post the letter <!-- created 2026-09-22 14:05; marked 2026-09-23 09:12 -->
// An archived task stays in its entry and notes when it was archived (it's then left out of the Tasks menu):
//   2. [x] Post the letter <!-- created 2026-09-22 14:05; marked 2026-09-23 09:12; archived 2026-09-24 10:00 -->
// (An HTML comment, so it stays out of sight if the file is opened in another Markdown app.)
const TASK_BLOCK = '(^|\\n)((?:\\d+\\. \\[[ xX-]\\] [^\\n]*(?:\\n|$))+)';
const TASK_LINE = /^\d+\. \[([ xX-])\] (.*)$/;
// A sub-entry is kept in the file as "## II <!-- sub-entry -->", followed by a space and the words written beside it.
// The numeral is only there to read the file by: numbers always follow the order of the sub-entries, starting from I.
const SUB_SRC = '## [IVXLCDM]+ <!-- sub-entry -->';
// A sub-entry within a sub-entry: "### I.II <!-- sub-sub-entry -->", numbered from I again under each sub-entry.
const SUB2_SRC = '### [IVXLCDM]+\\.[IVXLCDM]+ <!-- sub-sub-entry -->';
// An indented line starts with a tab in the file.
// A quote dragged in from the Quotes menu is kept as a Markdown quote under a marker, each line starting "> ":
//   <!-- quote -->
//   > The words of the quote
const QUOTE_BLOCK = '(^|\\n)<!-- quote -->\\n((?:>(?: [^\\n]*)?(?:\\n|$))+)';
// Writing done on a later day than the entry was begun starts under that day, kept on a line of its own:
//   <!-- day 2026-09-24 14:05 -->
const DAY_BLOCK = '(^|\\n)<!-- day (\\d{4}-\\d{2}-\\d{2}(?: \\d{2}:\\d{2})?) -->(?:\\n|$)';
const BLOCKS = '(?:' + TASK_BLOCK + ')|(' + SUB_SRC + ') ?|(?<=^|\\n)(\\t)|(' + SUB2_SRC + ') ?|(?:' + QUOTE_BLOCK + ')|(?:' + DAY_BLOCK + ')';
function roman(n){
  let out = '';
  for (const [v, r] of [[1000,'M'],[900,'CM'],[500,'D'],[400,'CD'],[100,'C'],[90,'XC'],[50,'L'],[40,'XL'],[10,'X'],[9,'IX'],[5,'V'],[4,'IV'],[1,'I']])
    while (n >= v) { out += r; n -= v; }
  return out;
}
// Task times are kept as local "YYYY-MM-DDTHH:MM", the same form a date-and-time input uses.
const pad2 = n => String(n).padStart(2, '0');
function stampNow(){
  const d = new Date();
  return d.getFullYear() + '-' + pad2(d.getMonth() + 1) + '-' + pad2(d.getDate()) + 'T' + pad2(d.getHours()) + ':' + pad2(d.getMinutes());
}
const STAMP_RE = /^(\d{4})-(\d{2})-(\d{2})[T ](\d{2}):(\d{2})$/;
function stampDate(s){
  const m = s && s.match(STAMP_RE);
  return m ? new Date(+m[1], m[2] - 1, +m[3], +m[4], +m[5]) : null;
}
const fmtStamp = new Intl.DateTimeFormat(undefined,{day:'numeric',month:'short',year:'numeric',hour:'numeric',minute:'2-digit'});
function splitTaskText(raw){
  const item = {text:raw, created:'', due:'', marked:'', urgency:'', archived:''};
  const m = raw.match(/^(.*?)\s*<!--\s*(.*?)\s*-->\s*$/);
  if (!m) return item;
  let found = false;
  for (const f of m[2].split(';')) {
    const k = f.trim().match(/^(created|due|marked|archived)\s+(.+)$/);
    if (k && STAMP_RE.test(k[2].trim())) { item[k[1]] = k[2].trim().replace(' ', 'T'); found = true; }
    const u = f.trim().match(/^urgency\s+(high|medium|low)$/i);
    if (u) { item.urgency = u[1].toLowerCase(); found = true; }
  }
  if (found) item.text = m[1];
  return item;
}
function taskLine(it){
  const meta = [];
  if (it.created) meta.push('created ' + it.created.replace('T', ' '));
  if (it.due) meta.push('due ' + it.due.replace('T', ' '));
  if (it.marked && it.state !== ' ') meta.push('marked ' + it.marked.replace('T', ' '));
  if (URGENCY[it.urgency]) meta.push('urgency ' + it.urgency);
  if (it.archived && it.state !== ' ') meta.push('archived ' + it.archived.replace('T', ' '));
  return (it.text || '').replace(/\n/g, ' ') + (meta.length ? ' <!-- ' + meta.join('; ') + ' -->' : '');
}
function parseText(text, parts){
  const re = new RegExp(TOKEN_SRC + '|' + LINK_SRC + '|' + PDF_SRC, 'g');
  let last = 0, m;
  while ((m = re.exec(text))) {
    if (m.index > last) parts.push({type:'text', text:text.slice(last, m.index)});
    if (m[6] !== undefined) parts.push({type:'pdf', name:m[6], title:m[5]});
    else if (m[4] !== undefined) parts.push({type:'link', id:m[4], title:m[3]});
    else parts.push({type:'img', name:m[2], title:m[1]});
    last = m.index + m[0].length;
  }
  if (last < text.length) parts.push({type:'text', text:text.slice(last)});
}
function parseBody(body){
  const parts = [], re = new RegExp(BLOCKS, 'g');
  let last = 0, m;
  while ((m = re.exec(body))) {
    parseText(body.slice(last, m.index), parts);
    last = m.index + m[0].length;
    if (m[9] !== undefined) { parts.push({type:'day', day:m[9]}); continue; }
    if (m[7] !== undefined) { parts.push({type:'quote', text:m[7].replace(/\n$/, '').split('\n').map(l => l.replace(/^> ?/, '')).join('\n')}); continue; }
    if (m[5] !== undefined) { parts.push({type:'sub', level:2}); continue; }
    if (m[4] !== undefined) { parts.push({type:'indent'}); continue; }
    if (m[2] === undefined) { parts.push({type:'sub', level:1}); continue; }
    const items = m[2].replace(/\n$/, '').split('\n').map(line => {
      const t = line.match(TASK_LINE);
      const mark = t[1].toLowerCase();
      return {state: mark === 'x' ? 'x' : mark === '-' ? '-' : ' ', ...splitTaskText(t[2])};
    });
    parts.push({type:'tasks', items});
  }
  parseText(body.slice(last), parts);
  return parts;
}
function serializeParts(parts){
  let out = '', subs = 0, subs2 = 0, afterSub = false;
  for (const p of parts) {
    // One space between a numeral and whatever follows it on its line (it's taken off again when reading).
    if (afterSub && p.type !== 'tasks' && p.type !== 'quote' && p.type !== 'day' && !(p.type === 'text' && p.text.startsWith('\n'))) out += ' ';
    afterSub = false;
    if (p.type === 'text') out += p.text;
    else if (p.type === 'img') out += token(p.name, p.title);
    else if (p.type === 'link') out += linkToken(p.id, p.title);
    else if (p.type === 'pdf') out += pdfToken(p.name, p.title);
    else if (p.type === 'sub' && p.level === 2) { out += '### ' + roman(Math.max(subs, 1)) + '.' + roman(++subs2) + ' <!-- sub-sub-entry -->'; afterSub = true; }
    else if (p.type === 'sub') { out += '## ' + roman(++subs) + ' <!-- sub-entry -->'; subs2 = 0; afterSub = true; }
    else if (p.type === 'indent') out += '\t';
    else if (p.type === 'day') { if (out) out += '\n'; out += '<!-- day ' + p.day + ' -->\n'; }
    else if (p.type === 'quote') {
      if (out) out += '\n';
      out += '<!-- quote -->\n' + p.text.split('\n').map(l => l ? '> ' + l : '>').join('\n') + '\n';
    }
    else {
      if (out) out += '\n';
      out += p.items.map((it, i) => (i + 1) + '. [' + it.state + '] ' + taskLine(it)).join('\n') + '\n';
    }
  }
  return out;
}
function withLegacyImages(body, images){
  // Entries from before pictures could be placed keep them at the top.
  const inBody = imagesIn(body);
  const missing = (images || []).filter(n => !inBody.includes(n));
  if (!missing.length) return body;
  return missing.map(n => token(n)).join(' ') + '\n' + body;
}

/* ---------- Storage: the server on this computer ---------- */
const H = {'Content-Type':'application/json','X-Journal':'1'};
const KEEPALIVE_MAX = 60000;
const byteSize = text => new TextEncoder().encode(text).length;
function serverStore(){
  return {
    async load(){
      const r = await fetch('/api/entries', {headers:{'X-Journal':'1'}, cache:'no-store'});
      if (!r.ok) throw new Error('load');
      return r.json();
    },
    // A save is sent so that it still finishes if the page closes. Browsers only allow that for requests of
    // up to 64 KB (shared with any other save still on its way), so a longer entry is sent the ordinary way,
    // and so is one the browser turns away.
    async save(id, data){
      const body = JSON.stringify(data), url = '/api/entries/' + id;
      let r;
      if (byteSize(body) <= KEEPALIVE_MAX) {
        try { r = await fetch(url, {method:'PUT', headers:H, body, keepalive:true}); } catch (err) { r = null; }
      }
      if (!r) r = await fetch(url, {method:'PUT', headers:H, body});
      if (!r.ok) throw new Error('save');
    },
    async remove(id){
      const r = await fetch('/api/entries/' + id, {method:'DELETE', headers:H});
      if (!r.ok) throw new Error('delete');
    },
    async uploadImage(file){
      const r = await fetch('/api/images', {method:'POST', headers:{'X-Journal':'1','Content-Type':file.type||'application/octet-stream'}, body:file});
      if (r.status === 415) throw new Error('type');
      if (r.status === 413) throw new Error('size');
      if (!r.ok) throw new Error('upload');
      return (await r.json()).name;
    },
    async uploadPdf(file){
      const r = await fetch('/api/pdfs', {method:'POST', headers:{'X-Journal':'1','Content-Type':'application/pdf'}, body:file});
      if (r.status === 415) throw new Error('type');
      if (r.status === 413) throw new Error('size');
      if (!r.ok) throw new Error('upload');
      return (await r.json()).name;
    },
    async uploadModel(file){
      const r = await fetch('/api/models', {method:'POST', headers:{'X-Journal':'1','Content-Type':'model/gltf-binary'}, body:file});
      if (r.status === 415) throw new Error('type');
      if (r.status === 413) throw new Error('size');
      if (!r.ok) throw new Error('upload');
      return (await r.json()).name;
    },
    async removeImage(name, forever){
      await fetch('/api/images/' + name + (forever ? '?forever=1' : ''), {method:'DELETE', headers:H});
    },
    async removeEntry(id, forever){
      const r = await fetch('/api/entries/' + id + (forever ? '?forever=1' : ''), {method:'DELETE', headers:H});
      if (!r.ok) throw new Error('delete');
    },
    async changedImages(){
      const r = await fetch('/api/changed', {headers:{'X-Journal':'1'}, cache:'no-store'});
      return r.ok ? r.json() : [];
    },
    async linkDrawing(name, old){
      const r = await fetch('/api/images/' + name + '/replaces/' + old, {method:'POST', headers:H});
      if (!r.ok) throw new Error('link');
    },
    async restoreImage(name){
      const r = await fetch('/api/images/' + name + '/restore', {method:'POST', headers:H});
      if (!r.ok) throw new Error('restore');
      return r.json();
    }
  };
}

async function init(){
  renderList();
  loadSettings();
  loadTopics();
  store = serverStore();
  try {
    store.changedImages().then(list => { changed = new Set(list); }).catch(() => {});
    applyIncoming(await store.load());
    els.where.textContent = '';
  } catch (e) {
    loaded = true; renderList();
    els.where.textContent = "Can't reach the journal server. Check that it's still running, then reload.";
  }
}

function applyIncoming(obj){
  loaded = true;
  for (const [id, data] of Object.entries(obj)) {
    if (dirty.has(id)) continue;
    const body = withLegacyImages(data.body || '', data.images);
    const created = data.created || Date.now(), updated = data.updated || created;
    let history = Array.isArray(data.history) ? data.history.slice() : [];
    // Entries from before history was kept: count their last change if it was on a later day.
    if (!Array.isArray(data.history) || (!history.length && !sameDay(created, updated))) history = sameDay(created, updated) ? [] : [updated];
    entries.set(id, {title:data.title||'', body, created, updated, images:imagesIn(body), history,
      side:Array.isArray(data.side) ? data.side.slice() : [], topics:Array.isArray(data.topics) ? data.topics.slice() : [],
      inks:data.inks && typeof data.inks === 'object' ? Object.assign({}, data.inks) : {},
      books:data.books && typeof data.books === 'object' ? Object.assign({}, data.books) : {}});
  }
  for (const id of [...entries.keys()]) {
    if (!(id in obj) && !dirty.has(id) && !unsaved.has(id)) entries.delete(id);
  }
  if (currentId && !entries.has(currentId)) { currentId = null; showEditor(); }
  else if (currentId && !dirty.has(currentId)) fillEditor(false);
  renderList();
}

/* ---------- Saving ---------- */
function scheduleSave(id){
  clearTimeout(timers.get(id));
  timers.set(id, setTimeout(() => flush(id), 900));
}
function flush(id){
  clearTimeout(timers.get(id)); timers.delete(id);
  if (!store) return Promise.resolve();
  const prev = writes.get(id) || Promise.resolve();
  const p = prev.then(async () => {
    const e = entries.get(id);
    if (!e || !dirty.has(id)) return;
    if (unsaved.has(id) && isEmpty(e)) { dirty.delete(id); return; }
    const snap = {title:e.title, body:e.body, created:e.created, updated:e.updated, images:e.images.slice(), history:e.history.slice(),
      side:shelfNames(e), topics:(e.topics || []).slice(), inks:Object.assign({}, e.inks), books:Object.assign({}, e.books)};
    if (id === currentId) setStatus('Saving…');
    try {
      await store.save(id, snap);
      unsaved.delete(id);
      const now = entries.get(id);
      if (now && now.updated === snap.updated) dirty.delete(id);
      if (id === currentId && !dirty.has(id)) setStatus('Saved');
    } catch (err) {
      if (id === currentId) setStatus("Couldn't save. Your words are still here; keep typing to try again.", true);
    }
  });
  writes.set(id, p);
  return p;
}
function flushAll(){ for (const id of [...timers.keys()]) flush(id); }
document.addEventListener('visibilitychange', () => { if (document.visibilityState === 'hidden') flushAll(); });
window.addEventListener('pagehide', flushAll);
// A long entry can't be saved on the way out, so if one has unsaved changes the browser asks before leaving.
window.addEventListener('beforeunload', ev => {
  const long = [...dirty].some(id => { const e = entries.get(id); return e && byteSize(e.body) > KEEPALIVE_MAX - 4000; });
  if (long) { flushAll(); ev.preventDefault(); ev.returnValue = ''; }
});

/* ---------- Entry list ---------- */
function snippet(e){
  return plainText(e.body).replace(/^\d+\. \[[ xX-]\] /gm, '').split('\n').map(s => s.trim()).filter(Boolean).join(' ').slice(0, 160);
}
function renderList(){
  els.list.replaceChildren();
  if (!loaded) {
    const li = document.createElement('li'); li.className = 'list-note'; li.textContent = 'Opening your journal…';
    els.list.append(li); return;
  }
  const q = query.toLowerCase();
  const view = listView(), chosen = view === 'topic' ? listTopics() : [];
  const items = [...entries.entries()]
    .filter(([id, e]) => !(unsaved.has(id) && isEmpty(e) && id !== currentId))
    .filter(([, e]) => !q || e.title.toLowerCase().includes(q) || plainText(e.body).toLowerCase().includes(q)
      || topicLabel(e).toLowerCase().includes(q))
    .filter(([, e]) => !chosen.length || chosen.every(tid => (e.topics || []).includes(tid)))
    .sort((a, b) => (view === 'changes' ? changeDays(b[1]) - changeDays(a[1]) : 0) || b[1].updated - a[1].updated);
  if (!items.length) {
    const li = document.createElement('li'); li.className = 'list-note';
    li.textContent = q ? 'No entries match that search.'
      : chosen.length ? (chosen.length > 1 ? 'No entries have all of these topics.' : 'No entries have this topic.') : 'No entries yet.';
    els.list.append(li); return;
  }
  for (const [id, e] of items) {
    const li = document.createElement('li');
    const b = document.createElement('button');
    b.type = 'button'; b.className = 'entry-btn';
    b.setAttribute('aria-current', id === currentId ? 'true' : 'false');
    const row = document.createElement('span'); row.className = 'trow';
    const t = document.createElement('span'); t.className = 't' + (e.title.trim() ? '' : ' untitled');
    t.textContent = e.title.trim() || 'Untitled';
    row.append(t);
    const topic = topicLabel(e);
    if (topic) {
      const tp = document.createElement('span'); tp.className = 'tp';
      tp.textContent = '(' + topic + ')'; tp.title = (entryTopics(e).length > 1 ? 'Topics: ' : 'Topic: ') + topic;
      row.append(tp);
    }
    if (e.images.length) {
      const minis = document.createElement('span'); minis.className = 'minis';
      for (const name of e.images.slice(0, 3)) {
        const img = document.createElement('img');
        img.src = '/images/' + name; img.alt = ''; img.loading = 'lazy'; img.decoding = 'async';
        minis.append(img);
      }
      const extra = e.images.length - 3;
      if (extra > 0) {
        const more = document.createElement('span'); more.className = 'more';
        more.textContent = '+' + extra + (extra === 1 ? ' image' : ' images');
        minis.append(more);
      }
      minis.title = e.images.length === 1 ? '1 image' : e.images.length + ' images';
      row.append(minis);
    }
    const d = document.createElement('span'); d.className = 'd'; d.textContent = when(e.updated);
    if (view === 'changes') { const n = changeDays(e); d.textContent += ' \u00b7 changed on ' + n + (n === 1 ? ' day' : ' days'); }
    b.append(row, d);
    const s = snippet(e);
    if (s) { const sp = document.createElement('span'); sp.className = 's'; sp.textContent = s; b.append(sp); }
    b.addEventListener('click', () => { if (Date.now() - listDragEnded < 400) return; open(id); });
    b.addEventListener('pointerdown', ev => startListDrag(ev, id));
    li.append(b); els.list.append(li);
  }
}

/* ---------- Editor ---------- */
try { els.body.contentEditable = 'plaintext-only'; } catch (e) { els.body.contentEditable = 'true'; }
const richFallback = els.body.contentEditable !== 'plaintext-only';

function setFigTitle(fig, title){
  fig.dataset.title = cleanTitle(title);
  fig.title = (fig.dataset.title ? fig.dataset.title + '\n' : '') + 'Click to enlarge, drag to move';
  const img = fig.querySelector('img'); if (img) img.alt = fig.dataset.title || 'Attached image';
}
function makeFigure(name, title){
  const fig = document.createElement('span');
  fig.className = 'fig'; fig.contentEditable = 'false'; fig.dataset.name = name;
  const img = document.createElement('img');
  img.src = '/images/' + name; img.draggable = false;
  fig.append(img);
  setFigTitle(fig, title);
  fig.addEventListener('pointerdown', startDrag);
  fig.addEventListener('dragstart', ev => ev.preventDefault());
  return fig;
}
function renderEditor(body){
  const frag = document.createDocumentFragment();
  for (const p of parseBody(body)) {
    frag.append(p.type === 'text' ? formattedText(p.text) : p.type === 'img' ? makeFigure(p.name, p.title) : p.type === 'link' ? makeLink(p.id, p.title)
      : p.type === 'pdf' ? makePdf(p.name, p.title) : p.type === 'sub' ? makeSub(p.level) : p.type === 'indent' ? makeIndent() : p.type === 'quote' ? makeQuote(p.text) : p.type === 'day' ? makeWrittenDay(p.day) : makeTasks(p.items));
  }
  els.body.replaceChildren(frag);
  numberSubs(els.body);
}
// Writing with <b>…</b> (bold) and <u>…</u> (underline) in it, as it's shown in the editor.
function formattedText(text){
  const frag = document.createDocumentFragment(), re = /<(\/?)([bu])>/g;
  let last = 0, m, b = false, u = false;
  const add = str => {
    if (!str) return;
    let node = document.createTextNode(str);
    if (u) { const el = document.createElement('u'); el.append(node); node = el; }
    if (b) { const el = document.createElement('b'); el.append(node); node = el; }
    frag.append(node);
  };
  while ((m = re.exec(text))) {
    add(text.slice(last, m.index)); last = re.lastIndex;
    if (m[2] === 'b') b = !m[1]; else u = !m[1];
  }
  add(text.slice(last));
  return frag;
}
// When a part of an entry was written, if not on the day the entry was begun: a faint date and time on a
// line of its own, above that writing. Kept as "YYYY-MM-DD HH:MM" (dates put in before times were added have no time).
const dayKey = d => d.getFullYear() + '-' + pad2(d.getMonth() + 1) + '-' + pad2(d.getDate());
const dayStamp = d => dayKey(d) + ' ' + pad2(d.getHours()) + ':' + pad2(d.getMinutes());
function makeWrittenDay(stamp){
  const el = document.createElement('div'); el.className = 'written-day'; el.contentEditable = 'false';
  el.dataset.day = stamp;
  const m = stamp.match(/^(\d{4})-(\d{2})-(\d{2})(?: (\d{2}):(\d{2}))?$/);
  const d = new Date(+m[1], m[2] - 1, +m[3], +(m[4] || 0), +(m[5] || 0));
  el.textContent = fmtDate.format(d) + (m[4] !== undefined ? ', ' + fmtTime.format(d) : '');
  el.setAttribute('role', 'separator'); el.setAttribute('aria-label', 'Written ' + el.textContent);
  return el;
}
// A piece of the entry flattened to plain characters, just enough to tell where lines begin and end:
// blocks (task lists, quotes, dates) count as line breaks, pictures, links and numerals as something written.
function lineChars(node){
  let out = '';
  for (const n of node.childNodes) {
    if (n.nodeType === 3) out += n.data;
    else if (n.nodeType !== 1) continue;
    else if (n.matches('.tasks, .quote, .written-day') || n.tagName === 'BR') out += '\n';
    else if (n.matches('.fig, .sub, .indent')) out += 'x';
    else if (n.tagName === 'DIV' || n.tagName === 'P') out += '\n' + lineChars(n);
    else out += lineChars(n);
  }
  return out;
}
// Before writing goes in on a later day than the part of the entry it's going into was written (the day the
// entry was begun, or the last date above it), that day's date and time go in first. This happens when the
// writing is added at the end of the entry, or on an empty line of its own among the older writing; changing
// words inside a line that's already there doesn't get a date. Among older writing, the older date is put
// back after the new piece, so the writing below it keeps its own date.
// Returns an empty bit of text just after the new date, with the cursor in it, for the writing to go into
// (or null when no date was needed).
function dayBeforeWriting(){
  const e = currentId ? entries.get(currentId) : null, sel = document.getSelection();
  if (!e || !sel.rangeCount || !sel.isCollapsed) return null;
  const r = sel.getRangeAt(0), at = r.startContainer;
  if (!els.body.contains(at)) return null;
  const host = at.nodeType === 1 ? at : at.parentElement;
  if (host !== els.body && host.closest('.fig, .tasks, .quote, .sub, .indent, .written-day')) return null;
  const before = document.createRange(), rest = document.createRange();
  before.setStart(els.body, 0); before.setEnd(at, r.startOffset);
  rest.setStart(at, r.startOffset); rest.setEnd(els.body, els.body.childNodes.length);
  // The date of the part of the entry the cursor is in.
  const above = [...els.body.querySelectorAll('.written-day')].filter(d => before.intersectsNode(d));
  const since = above.length ? above[above.length - 1].dataset.day : dayStamp(new Date(e.created));
  const now = new Date();
  if (since.slice(0, 10) >= dayKey(now)) return null;
  const after = rest.cloneContents();
  const atEnd = !after.textContent.trim() && !after.querySelector('.fig, .tasks, .quote, .sub, .indent, .written-day');
  if (!atEnd) {
    const b = lineChars(before.cloneContents()), a = lineChars(after);
    if ((b && !b.endsWith('\n')) || (a && !a.startsWith('\n'))) return null;   // in the middle of a line
  }
  const mark = makeWrittenDay(dayStamp(now));
  r.insertNode(mark);
  // Each date stands in for the line break beside it, as a quote does.
  let p = mark.previousSibling;
  while (p && p.nodeType === 3 && p.data === '') p = p.previousSibling;
  if (p && p.nodeType === 3 && p.data.endsWith('\n')) p.data = p.data.slice(0, -1);
  const t = document.createTextNode('');
  mark.after(t);
  if (!atEnd) {
    let n = t.nextSibling;
    while (n && n.nodeType === 3 && /^\n*$/.test(n.data) && n.nextSibling) n = n.nextSibling;
    const nextIsDate = n && n.nodeType === 1 && n.classList.contains('written-day');
    if (!nextIsDate) {
      const back = makeWrittenDay(since);
      t.after(back);
      const q = back.nextSibling;
      if (q && q.nodeType === 3 && q.data.startsWith('\n')) q.data = q.data.slice(1);
    }
  }
  sel.collapse(t, 0);
  return t;
}
// Puts writing into the bit of text dayBeforeWriting made, with the cursor after it.
function writeAfterDay(t, text){
  t.data = text;
  document.getSelection().collapse(t, t.data.length);
  onBodyChange();
}
// A quote in an entry: its words in a box marked "Quote". It can't be typed in; Remove takes it out of the
// entry (it stays in the Quotes menu).
function makeQuote(text, readonly){
  const q = document.createElement('div'); q.className = 'quote'; q.contentEditable = 'false';
  q.setAttribute('role', 'figure'); q.setAttribute('aria-label', 'Quote');
  const words = document.createElement('div'); words.className = 'quote-text'; words.textContent = text;
  q.append(words);
  if (!readonly) {
    // Expand / Collapse: only offered for quotes longer than 5 lines, which start out collapsed.
    const fold = document.createElement('button'); fold.type = 'button'; fold.className = 'quote-fold'; fold.hidden = true;
    fold.addEventListener('mousedown', ev => ev.preventDefault());
    fold.addEventListener('click', ev => {
      ev.preventDefault(); ev.stopPropagation();
      q.classList.toggle('folded'); showQuoteFold(q);
    });
    const del = document.createElement('button'); del.type = 'button'; del.className = 'quote-del'; del.textContent = 'Remove';
    del.title = 'Take this quote out of the entry (it stays in Quotes)';
    del.addEventListener('mousedown', ev => ev.preventDefault());
    del.addEventListener('click', ev => { ev.preventDefault(); ev.stopPropagation(); removeTasks(q); onBodyChange(); });
    const btns = document.createElement('span'); btns.className = 'quote-btns';
    btns.append(fold, del);
    q.append(btns);
    q.addEventListener('pointerdown', ev => startBodyQuoteDrag(ev, q));
    quoteSizes.observe(words);
  }
  return q;
}
// Works out, once a quote is on the page (and again whenever its width changes), whether it's over 5 lines.
const QUOTE_LINES = 5;
const quoteSizes = new ResizeObserver(list => {
  for (const en of list) {
    const words = en.target, q = words.parentElement;
    if (!q || !words.isConnected || !words.scrollHeight) continue;
    const line = parseFloat(getComputedStyle(words).lineHeight) || 20;
    const long = words.scrollHeight > line * QUOTE_LINES + 2;
    if (!long) { q.classList.remove('folded'); delete q.dataset.foldSeen; }
    else if (!q.dataset.foldSeen) { q.classList.add('folded'); q.dataset.foldSeen = '1'; }   // collapsed the first time it's seen to be long
    q.dataset.long = long ? '1' : '';
    showQuoteFold(q);
  }
});
function showQuoteFold(q){
  const fold = q.querySelector(':scope > .quote-btns > .quote-fold'); if (!fold) return;
  fold.hidden = !q.dataset.long;
  const folded = q.classList.contains('folded');
  fold.textContent = folded ? 'Expand' : 'Collapse';
  fold.title = folded ? 'Show the whole quote' : 'Show only the first ' + QUOTE_LINES + ' lines';
  fold.setAttribute('aria-expanded', String(!folded));
}
function makeSub(level){
  const sub = document.createElement('span'); sub.className = level === 2 ? 'sub sub2' : 'sub'; sub.contentEditable = 'false';
  return sub;
}
// Numbers the sub-entries I, II, III… in the order they come.
// Also gives each indented line the numeral of the sub-entry it's under (I, before the first one).
// Sub-entries within one are numbered after it (I.I, I.II…), starting again under each; before any, under I.
// Indented lines line up with whichever numeral comes last above them.
function numberSubs(root){
  let i = 0, j = 0, last = 'I';
  for (const el of root.querySelectorAll('.sub, .indent')) {
    if (el.classList.contains('indent')) { if (el.dataset.n !== last) el.dataset.n = last; continue; }
    if (el.classList.contains('sub2')) last = roman(Math.max(i, 1)) + '.' + roman(++j);
    else { last = roman(++i); j = 0; }
    if (el.textContent !== last) el.textContent = last;
    el.setAttribute('aria-label', 'Sub-entry ' + last);
  }
}
function makeIndent(){
  const ind = document.createElement('span'); ind.className = 'indent'; ind.contentEditable = 'false'; ind.dataset.n = 'I';
  return ind;
}
// Bold and underlined writing is saved as <b>…</b> and <u>…</u>, always bold outside underline, and never
// running across the end of a line (or past a picture, numeral or task list), so those stay where they belong.
const PLAIN = {b:false, u:false};
function domParts(){
  const parts = []; let buf = '', cur = PLAIN;
  const setState = want => {
    if (want.b === cur.b && want.u === cur.u) return;
    if (want.b !== cur.b) {
      if (cur.u) buf += '</u>';
      buf += want.b ? '<b>' : '</b>';
      if (want.u) buf += '<u>';
    } else buf += want.u ? '<u>' : '</u>';
    cur = want;
  };
  const addText = (str, want) => str.split('\n').forEach((line, i) => {
    if (i) { setState(PLAIN); buf += '\n'; }
    if (line) { setState(want); buf += line; }
  });
  const push = () => { setState(PLAIN); if (buf) { parts.push({type:'text', text:buf}); buf = ''; } };
  const walk = (node, top, want = PLAIN) => {
    for (const n of node.childNodes) {
      if (n.nodeType === 3) addText(n.data, want);
      else if (n.nodeType === 1) {
        if (n.classList.contains('elink')) { push(); parts.push({type:'link', id:n.dataset.link, title:n.dataset.title || ''}); }
        else if (n.classList.contains('epdf')) { push(); parts.push({type:'pdf', name:n.dataset.pdf, title:n.dataset.title || ''}); }
        else if (n.classList.contains('fig')) { push(); parts.push({type:'img', name:n.dataset.name, title:n.dataset.title || ''}); }
        else if (n.classList.contains('sub')) { push(); parts.push({type:'sub', level:n.classList.contains('sub2') ? 2 : 1}); }
        else if (n.classList.contains('indent')) { push(); parts.push({type:'indent'}); }
        else if (n.classList.contains('written-day')) { push(); parts.push({type:'day', day:n.dataset.day}); }
        else if (n.classList.contains('quote')) { push(); parts.push({type:'quote', text:n.querySelector('.quote-text').textContent}); }
        else if (n.classList.contains('tasks')) {
          push();
          parts.push({type:'tasks', items:[...n.querySelectorAll('.task')].map(li => ({
            state: STATE_MARK[li.dataset.state] || ' ', text: taskTextOf(li.querySelector('.task-text')),
            created: li.dataset.created || '', due: li.dataset.due || '', marked: li.dataset.marked || '', urgency: li.dataset.urgency || '', archived: li.dataset.archived || ''}))});
        }
        else if (n.tagName === 'BR') { if (!(top && n === node.lastChild)) addText('\n', want); }
        else if (n.tagName === 'DIV' || n.tagName === 'P') { if (buf && !buf.endsWith('\n')) addText('\n', want); walk(n, false, want); }
        else if (n.tagName === 'B' || n.tagName === 'STRONG') walk(n, false, {...want, b:true});
        else if (n.tagName === 'U') walk(n, false, {...want, u:true});
        else walk(n, false, want);
      }
    }
  };
  walk(els.body, true); push();
  return parts;
}
function countWords(s){ const m = plainText(s).replace(/^\d+\. \[[ xX-]\] /gm, '').trim().match(/\S+/g); return m ? m.length : 0; }
function updateMeta(){
  const e = entries.get(currentId); if (!e) return;
  els.created.textContent = 'Begun ' + fmtDate.format(new Date(e.created));
  const n = countWords(e.body);
  els.words.textContent = n === 1 ? '1 word' : n + ' words';
}
function fillEditor(resetStatus){
  const e = entries.get(currentId); if (!e) return;
  if (els.title.value !== e.title) els.title.value = e.title;
  if (serializeParts(domParts()) !== e.body) renderEditor(e.body);
  updateMeta(); renderHistory(); renderShelf(); renderTopic();
  if (resetStatus) setStatus(unsaved.has(currentId) ? '' : 'Saved');
}
function showEditor(){
  const has = !!currentId;
  els.page.hidden = !has; els.empty.hidden = has;
  document.body.classList.toggle('editing', has);
  disarmDelete();
  renderShelf();
}
function setStatus(text, err){
  els.status.textContent = text;
  els.status.classList.toggle('err', !!err);
}
// One history line per day after the entry was begun, holding the time of that day's latest change.
function recordHistory(e, now){
  if (sameDay(now, e.created)) return;
  const h = e.history;
  if (h.length && sameDay(h[h.length - 1], now)) h[h.length - 1] = now;
  else h.push(now);
}
function renderHistory(){
  const e = entries.get(currentId);
  if (!e || !e.history.length) { els.hist.hidden = true; return; }
  const line = (ts, cls) => {
    const li = document.createElement('li');
    if (cls) li.className = cls;
    li.textContent = (cls ? 'Begun ' : '') + fmtDate.format(new Date(ts)) + ', ' + fmtTime.format(new Date(ts));
    return li;
  };
  els.histList.replaceChildren(line(e.created, 'begun'), ...e.history.map(t => line(t)));
  els.hist.hidden = false;
}
function markChanged(id){
  const e = entries.get(id); if (!e) return;
  e.updated = Date.now();
  recordHistory(e, e.updated);
  dirty.add(id);
  scheduleSave(id);
  if (id === currentId) { setStatus('Editing'); updateMeta(); renderHistory(); }
  renderList();
}
function onBodyChange(){
  if (!currentId) return;
  const e = entries.get(currentId); if (!e) return;
  liftBlocks();
  e.body = serializeParts(domParts());
  e.images = imagesIn(e.body);
  numberSubs(els.body);
  markChanged(currentId);
  renderShelf();
}
function onTitleChange(){
  if (!currentId) return;
  const e = entries.get(currentId); if (!e) return;
  e.title = els.title.value;
  markChanged(currentId);
}

/* ---------- Task lists ---------- */
const STATE_MARK = {none:' ', done:'x', fail:'-'};
const MARK_STATE = {' ':'none', x:'done', '-':'fail'};
const STATE_LABEL = {none:'Not marked', done:'Marked as success', fail:'Marked as failure'};
const ICONS = {
  done:'<svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true"><path d="M4 10.5l4 4 8-9" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
  fail:'<svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true"><path d="M5 5l10 10M15 5L5 15" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/></svg>',
  none:''
};
function setTaskState(li, state){
  li.dataset.state = state;
  const box = li.querySelector('.task-box');
  box.innerHTML = ICONS[state];
  box.setAttribute('aria-label', STATE_LABEL[state] + '. Click to change');
  refreshTaskMeta(li);
}
// The small dates beside a task's name: when it was made, and when it should be finished by.
function taskMeta(created, due, state, marked, archived){
  const m = document.createElement('span'); m.className = 'task-meta';
  const c = stampDate(created), d = stampDate(due), k = state !== 'none' ? stampDate(marked) : null;
  if (c) {
    const s = document.createElement('span'); s.className = 'task-when';
    s.textContent = fmtStamp.format(c); s.title = 'Created ' + fmtStamp.format(c);
    m.append(s);
  }
  // When it was ticked (or marked as a failure), just after the date it was made.
  if (k) {
    const s = document.createElement('span'); s.className = 'task-marked ' + state;
    s.textContent = (state === 'done' ? '✓ ' : '✗ ') + fmtStamp.format(k);
    s.title = (state === 'done' ? 'Ticked ' : 'Marked as failure ') + fmtStamp.format(k);
    m.append(s);
  }
  if (d) {
    const s = document.createElement('span');
    s.className = 'task-due' + (state === 'none' && d < new Date() ? ' late' : '');
    s.textContent = 'Finish by ' + fmtStamp.format(d);
    m.append(s);
  }
  // An archived task stays in its entry, with a note that it's in the Archive (and so not in the Tasks menu).
  const a = state !== 'none' ? stampDate(archived) : null;
  if (a) {
    const s = document.createElement('span'); s.className = 'task-archived';
    s.textContent = 'Archived ' + fmtStamp.format(a); s.title = 'Archived ' + fmtStamp.format(a) + ', so it isn\u2019t in the Tasks menu';
    m.append(s);
  }
  return m;
}
function refreshTaskMeta(li){
  const old = li.querySelector('.task-meta');
  if (old) old.replaceWith(taskMeta(li.dataset.created, li.dataset.due, li.dataset.state, li.dataset.marked, li.dataset.archived));
  const b = li.querySelector('.task-due-btn');
  if (b) b.textContent = li.dataset.due ? 'Change finish time' : 'Set finish time';
}
function makeTask(item){
  const li = document.createElement('li'); li.className = 'task';
  li.dataset.created = item.created || ''; li.dataset.due = item.due || ''; li.dataset.marked = item.marked || ''; li.dataset.urgency = URGENCY[item.urgency] ? item.urgency : '';
  li.dataset.archived = item.archived || '';
  const text = document.createElement('span'); text.className = 'task-text';
  try { text.contentEditable = 'plaintext-only'; } catch (e) { text.contentEditable = 'true'; }
  text.spellcheck = true;
  fillTaskText(text, item.text || '', makeFigure, makeLink, makePdf);
  const box = document.createElement('button'); box.type = 'button'; box.className = 'task-box';
  box.addEventListener('click', ev => { ev.preventDefault(); openTaskMenu(li, box); });
  const del = document.createElement('button'); del.type = 'button'; del.className = 'task-del'; del.textContent = 'Delete task';
  del.addEventListener('mousedown', ev => ev.preventDefault());
  del.addEventListener('click', () => deleteTask(li));

  // Finish time: a button beside "Delete task" that opens a date-and-time field.
  const dueBtn = document.createElement('button'); dueBtn.type = 'button'; dueBtn.className = 'task-due-btn';
  const dueEdit = document.createElement('span'); dueEdit.className = 'task-due-edit'; dueEdit.hidden = true;
  const dueInput = document.createElement('input'); dueInput.type = 'datetime-local'; dueInput.setAttribute('aria-label', 'Finish by');
  const dueClear = document.createElement('button'); dueClear.type = 'button'; dueClear.textContent = 'No finish time';
  dueEdit.append(dueInput, dueClear);
  const closeDue = () => { dueEdit.hidden = true; dueBtn.hidden = false; };
  dueBtn.addEventListener('mousedown', ev => ev.preventDefault());
  dueBtn.addEventListener('click', () => {
    dueInput.value = li.dataset.due || '';
    dueClear.hidden = !li.dataset.due;
    dueBtn.hidden = true; dueEdit.hidden = false;
    dueInput.focus();
    try { dueInput.showPicker(); } catch (e) {}
  });
  dueInput.addEventListener('change', () => {
    if (!STAMP_RE.test(dueInput.value) || dueInput.value === li.dataset.due) return;
    li.dataset.due = dueInput.value; dueClear.hidden = false;
    refreshTaskMeta(li); onBodyChange();
  });
  dueClear.addEventListener('mousedown', ev => ev.preventDefault());
  dueClear.addEventListener('click', () => {
    li.dataset.due = ''; dueInput.value = '';
    refreshTaskMeta(li); onBodyChange();
    closeDue(); focusTask(li);
  });
  // Keep the field's typing to itself, so it isn't taken as writing in the entry.
  for (const type of ['input', 'paste', 'keydown']) dueEdit.addEventListener(type, ev => ev.stopPropagation());
  dueInput.addEventListener('keydown', ev => {
    if (ev.key === 'Enter' || ev.key === 'Escape') { ev.preventDefault(); closeDue(); focusTask(li); }
  });

  // The buttons show while you're in the task's text or its finish-time field.
  const inside = n => !!n && (n === text || dueEdit.contains(n) || urgMenu.contains(n));   // the urgency choices count as in the task
  li.addEventListener('focusin', ev => { if (inside(ev.target)) li.classList.add('asking'); });
  li.addEventListener('focusout', ev => { if (!inside(ev.relatedTarget)) { li.classList.remove('asking'); closeDue(); } });
  // Pressing on the grip or the empty part of the row (or its dates) drags the task;
  // a plain click there goes into the task's text.
  const grip = document.createElement('span'); grip.className = 'task-grip'; grip.textContent = '⠿';
  grip.title = 'Drag to move this task';
  li.addEventListener('pointerdown', ev => {
    const t = ev.target;
    if (ev.button === 0 && (t === li || t === grip || t.closest('.task-meta'))) startTaskDrag(ev, li);
  });

  // Urgency: a button beside the others that offers High, Medium and Low; the chosen one shows as a
  // coloured label just before the box (click it to change it too).
  const urgBtn = document.createElement('button'); urgBtn.type = 'button'; urgBtn.className = 'task-urg-btn'; urgBtn.textContent = 'Urgency';
  urgBtn.addEventListener('mousedown', ev => ev.preventDefault());
  urgBtn.addEventListener('click', ev => { ev.preventDefault(); openUrgencyMenu(li, urgBtn); });
  const urg = document.createElement('button'); urg.type = 'button'; urg.className = 'task-urg';
  urg.addEventListener('click', ev => { ev.preventDefault(); openUrgencyMenu(li, urg); });

  li.append(grip, text, taskMeta('', '', 'none'), dueBtn, dueEdit, urgBtn, del, urg, box);
  setTaskState(li, MARK_STATE[item.state] || 'none');
  showUrgency(li);
  return li;
}
// A task shown for reading only (in the archive and the Tasks menu).
function staticTask(it, src){
  src = src || (n => '/images/' + n);
  const li = document.createElement('li'); li.className = 'task';
  const state = MARK_STATE[it.state] || 'none'; li.dataset.state = state;
  const t = document.createElement('span'); t.className = 'task-text';
  fillTaskText(t, it.text || '', (name, title) => {
    const fig = document.createElement('span'); fig.className = 'fig'; if (title) fig.title = title;
    const img = document.createElement('img'); img.src = src(name); img.alt = title || 'Picture';
    fig.append(img); return fig;
  });
  const b = document.createElement('span'); b.className = 'task-box'; b.innerHTML = ICONS[state];
  b.setAttribute('aria-label', STATE_LABEL[state]);
  const u = document.createElement('span'); u.className = 'task-urg';
  if (URGENCY[it.urgency]) { u.dataset.u = it.urgency; u.textContent = URGENCY[it.urgency]; } else u.hidden = true;
  li.append(t, taskMeta(it.created, it.due, state, it.marked, it.archived), u, b);
  return li;
}
// A task's words can have pictures among them, written in the file the same way as in the entry.
function fillTaskText(span, text, figure, link = staticLink, pdf = staticPdf){
  const parts = []; parseText(text, parts);
  for (const p of parts) span.append(p.type === 'text' ? document.createTextNode(p.text) : p.type === 'link' ? link(p.id, p.title)
    : p.type === 'pdf' ? pdf(p.name, p.title) : figure(p.name, p.title));
}
function taskTextOf(span){
  let out = '';
  for (const n of span.childNodes) {
    if (n.nodeType === 3) out += n.data;
    else if (n.nodeType === 1 && n.classList.contains('elink')) out += linkToken(n.dataset.link, n.dataset.title);
    else if (n.nodeType === 1 && n.classList.contains('epdf')) out += pdfToken(n.dataset.pdf, n.dataset.title);
    else if (n.nodeType === 1 && n.classList.contains('fig')) out += token(n.dataset.name, n.dataset.title);
    else out += n.textContent;
  }
  return out.replace(/\n/g, ' ');
}
const taskBlank = span => !span.textContent.trim() && !span.querySelector('.fig');
function makeTasks(items){
  const block = document.createElement('div'); block.className = 'tasks'; block.contentEditable = 'false';
  const ol = document.createElement('ol');
  for (const it of items) ol.append(makeTask(it));
  block.append(ol);
  return block;
}
function focusTask(li, atStart){
  const span = li.querySelector('.task-text');
  span.focus();
  const sel = document.getSelection(); sel.selectAllChildren(span);
  if (atStart) sel.collapseToStart(); else sel.collapseToEnd();
}
// Where the cursor goes in the ordinary text next to a task list.
function caretBeside(block, before){
  const sib = before ? block.previousSibling : block.nextSibling;
  els.body.focus({preventScroll:true});
  const sel = document.getSelection();
  if (sib && sib.nodeType === 3) { sel.collapse(sib, before ? sib.data.length : 0); return; }
  const line = document.createTextNode('\n');
  if (before) block.before(line); else block.after(line);
  sel.collapse(line, 0);
}
// Clicking in the space just below a task list (or between its tasks) puts the cursor there ourselves:
// left to the browser, a click on that empty space can land the cursor at the very start of the entry
// and jump the view up to the top.
els.body.addEventListener('mousedown', ev => {
  if (ev.button !== 0 || ev.detail > 1 || ev.shiftKey) return;
  const t = ev.target;
  if (!t.closest || t.closest('.task, button, input, .fig, .quote, .sub, .indent, .written-day')) return;
  const y = ev.clientY;
  for (const block of els.body.querySelectorAll('.tasks')) {
    const tasks = block.querySelectorAll('.task'); if (!tasks.length) continue;
    const r = block.getBoundingClientRect(), last = tasks[tasks.length - 1].getBoundingClientRect();
    const below = r.bottom + (parseFloat(getComputedStyle(block).marginBottom) || 0);
    if (y > last.bottom && y <= below) { ev.preventDefault(); caretBeside(block, false); return; }
    if (t.closest('.tasks') === block && y >= r.top && y <= r.bottom) {
      // Between two tasks: into whichever is nearer.
      let best = null, dist = Infinity;
      for (const li of tasks) { const q = li.getBoundingClientRect(), d = y < q.top ? q.top - y : y > q.bottom ? y - q.bottom : 0; if (d < dist) { dist = d; best = li; } }
      if (best) { ev.preventDefault(); focusTask(best); }
      return;
    }
  }
});
function removeTasks(block){
  const prev = block.previousSibling, next = block.nextSibling;
  block.remove();
  if (prev && next && prev.nodeType === 3 && next.nodeType === 3 && !prev.data.endsWith('\n') && !next.data.startsWith('\n')) prev.data += '\n';
  els.body.focus({preventScroll:true});
  const sel = document.getSelection();
  if (prev && prev.nodeType === 3) sel.collapse(prev, prev.data.length);
  else if (next && next.nodeType === 3) sel.collapse(next, 0);
  els.body.normalize();
}
// Puts a task list at the end of the line the cursor is on (or between other blocks).
function placeBlock(block, t){
  if (t.text && t.text.parentNode) {
    const end = lineEndAt(t.text, t.offset), node = end.text;
    const after = node.splitText(end.offset);
    node.parentNode.insertBefore(block, after);
  } else {
    const parent = t.parent && els.body.contains(t.parent) && !t.parent.closest('.tasks, .quote, .sub, .indent, .written-day') ? t.parent : els.body;
    parent.insertBefore(block, t.ref && t.ref.parentNode === parent ? t.ref : null);
  }
  const p = block.previousSibling, n = block.nextSibling;
  if (n && n.nodeType === 3 && n.data.startsWith('\n')) n.data = n.data.slice(1);
  else if (p && p.nodeType === 3 && p.data.endsWith('\n')) p.data = p.data.slice(0, -1);
  els.body.normalize();
}
// Task lists that end up side by side become one list, so the numbering carries on.
function mergeTaskLists(){
  const skipEmpty = n => { while (n && n.nodeType === 3 && n.data === '') { const x = n.nextSibling; n.remove(); n = x; } return n; };
  for (const block of [...els.body.children].filter(el => el.classList.contains('tasks'))) {
    if (!block.isConnected) continue;
    let n = skipEmpty(block.nextSibling);
    while (n && n.nodeType === 1 && n.classList.contains('tasks')) {
      block.querySelector('ol').append(...n.querySelectorAll('.task'));
      const x = n.nextSibling; n.remove(); n = skipEmpty(x);
    }
  }
}
// Adds a single task: right after the task you're in, or else at the end of the current line.
function insertTask(){
  if (!currentId) return;
  const li = makeTask({state:' ', text:'', created:stampNow()});
  const sel = document.getSelection();
  const here = sel.rangeCount && els.body.contains(sel.anchorNode)
    ? (sel.anchorNode.nodeType === 1 ? sel.anchorNode : sel.anchorNode.parentElement).closest('.task') : null;
  if (here) here.after(li);
  else {
    const block = makeTasks([]);
    block.querySelector('ol').append(li);
    placeBlock(block, caretTarget());
    mergeTaskLists();
  }
  onBodyChange();
  focusTask(li);
}
/* ---------- Bold and underline ----------
   Select some writing and click Bold or Underline (or press Ctrl+B / Ctrl+U, ⌘ on a Mac). If all of it already
   has that, clicking takes it off again. Pictures, numerals and task lists are left as they are. */
const FMT_TAG = {bold:'B', underline:'U'};
const isFmt = n => n && n.nodeType === 1 && (n.tagName === 'B' || n.tagName === 'U');
const BLOCK_SEL = '.fig, .sub, .indent, .tasks, .quote, .written-day';
// The pieces of writing the selection covers: [text node, start, end].
function selectedText(){
  const sel = document.getSelection();
  if (!sel.rangeCount || sel.isCollapsed) return [];
  const range = sel.getRangeAt(0);
  if (!els.body.contains(range.commonAncestorContainer)) return [];
  const out = [], walker = document.createTreeWalker(els.body, NodeFilter.SHOW_TEXT);
  for (let n = walker.nextNode(); n; n = walker.nextNode()) {
    if (!range.intersectsNode(n) || n.parentElement.closest(BLOCK_SEL)) continue;
    const a = n === range.startContainer ? range.startOffset : 0, z = n === range.endContainer ? range.endOffset : n.length;
    if (a < z) out.push([n, a, z]);
  }
  return out;
}
const fmtAround = (t, tag) => { const a = t.parentElement.closest(tag); return a && els.body.contains(a) ? a : null; };
// Takes the formatting element a off the text t only, leaving the rest of a as it was.
function unwrapAround(t, a){
  const keep = frag => frag.textContent !== '' || frag.querySelector(BLOCK_SEL);
  const r = document.createRange();
  r.setStart(a, 0); r.setEndBefore(t);
  const before = r.extractContents();
  if (keep(before)) { const c = a.cloneNode(false); c.append(before); a.before(c); }
  r.setStartAfter(t); r.setEnd(a, a.childNodes.length);
  const after = r.extractContents();
  if (keep(after)) { const c = a.cloneNode(false); c.append(after); a.after(c); }
  a.replaceWith(...a.childNodes);
}
// Tidies up afterwards: no empty or doubled-up formatting, and side-by-side pieces joined together.
function tidyFormatting(){
  for (const el of [...els.body.querySelectorAll('b, u')].reverse()) {
    if (!el.isConnected) continue;
    if (!el.textContent && !el.querySelector(BLOCK_SEL)) { el.remove(); continue; }
    const outer = el.parentElement.closest(el.tagName);
    if (outer && els.body.contains(outer)) el.replaceWith(...el.childNodes);
  }
  for (const el of els.body.querySelectorAll('b, u')) {
    let next = el.nextSibling;
    while (next && next.nodeType === 3 && next.data === '') { const x = next.nextSibling; next.remove(); next = x; }
    while (next && next.nodeType === 1 && next.tagName === el.tagName) {
      el.append(...next.childNodes); next.remove(); next = el.nextSibling;
    }
  }
}
function formatSelection(kind){
  if (!currentId) return;
  const tag = FMT_TAG[kind], pieces = selectedText();
  if (!pieces.length) { els.body.focus({preventScroll:true}); return; }
  // Split off the selected parts, and split them again at line ends so formatting stays within lines.
  const segs = [];
  for (let [n, a, z] of pieces) {
    if (z < n.length) n.splitText(z);
    if (a > 0) n = n.splitText(a);
    let i;
    while ((i = n.data.indexOf('\n')) !== -1) {
      if (i > 0) { const rest = n.splitText(i); segs.push(n); n = rest; }
      n = n.data.length > 1 ? n.splitText(1) : null;   // the line end itself stays unformatted
      if (!n) break;
    }
    if (n && n.data) segs.push(n);
  }
  if (!segs.length) return;
  const remove = segs.every(t => fmtAround(t, tag));
  for (const t of segs) {
    if (remove) { let a; while ((a = fmtAround(t, tag))) unwrapAround(t, a); }
    else if (!fmtAround(t, tag)) { const el = document.createElement(tag); t.before(el); el.append(t); }
  }
  tidyFormatting();
  els.body.focus({preventScroll:true});
  const last = segs[segs.length - 1];
  document.getSelection().setBaseAndExtent(segs[0], 0, last, last.length);
  onBodyChange();
  syncFormatButtons();
}
// Where the line that has this bit of text in it really ends, when bold or underlined pieces continue it:
// {text, offset} of the line end (or of the end of the line's last bit of text).
function lineEndAt(node, off){
  const i = node.data.indexOf('\n', off);
  if (i !== -1) return {text:node, offset:i};
  let last = {text:node, offset:node.data.length};
  const w = document.createTreeWalker(els.body, NodeFilter.SHOW_TEXT | NodeFilter.SHOW_ELEMENT);
  w.currentNode = node;
  for (let x = w.nextNode(); x; x = w.nextNode()) {
    if (x.nodeType === 1) { if (x.matches('.tasks, .quote, .sub, .written-day')) break; continue; }
    if (x.parentElement.closest(BLOCK_SEL)) continue;
    const j = x.data.indexOf('\n');
    if (j !== -1) return {text:x, offset:j};
    last = {text:x, offset:x.data.length};
  }
  return last;
}
// A picture, numeral or task list that ends up inside bold or underlined writing is moved just outside it.
function liftBlocks(){
  const stuck = els.body.querySelectorAll(':is(b, u) :is(' + BLOCK_SEL + ')');
  if (!stuck.length) return;
  const sel = document.getSelection(), s = sel.rangeCount ? [sel.anchorNode, sel.anchorOffset, sel.focusNode, sel.focusOffset] : null;
  for (const block of stuck) {
    if (block.parentElement.closest(BLOCK_SEL)) continue;   // inside another block: it moves with that one
    let p;
    while (isFmt(p = block.parentElement) && p !== els.body) {
      const after = p.cloneNode(false);
      while (block.nextSibling) after.append(block.nextSibling);
      p.after(block);
      if (after.firstChild) block.after(after);
      if (!p.firstChild) p.remove();
    }
  }
  if (s && s[0] && s[0].nodeType === 3 && els.body.contains(s[0]) && els.body.contains(s[2])) {
    try { sel.setBaseAndExtent(s[0], s[1], s[2], s[3]); } catch (e) {}
  }
}
// The buttons show when all of the selected writing is bold or underlined.
function syncFormatButtons(){
  const pieces = selectedText();
  for (const [kind, id] of [['bold', 'boldBtn'], ['underline', 'underlineBtn']]) {
    const on = pieces.length > 0 && pieces.every(([n]) => fmtAround(n, FMT_TAG[kind]));
    $(id).setAttribute('aria-pressed', String(on));
  }
}
document.addEventListener('selectionchange', syncFormatButtons);
for (const [kind, id] of [['bold', 'boldBtn'], ['underline', 'underlineBtn']]) {
  $(id).addEventListener('mousedown', ev => ev.preventDefault());   // keep the selection
  $(id).addEventListener('click', () => formatSelection(kind));
}
els.body.addEventListener('keydown', ev => {
  if (!(ev.ctrlKey || ev.metaKey) || ev.altKey || ev.shiftKey || ev.isComposing) return;
  const k = ev.key.toLowerCase();
  if (k !== 'b' && k !== 'u') return;
  ev.preventDefault();
  formatSelection(k === 'b' ? 'bold' : 'underline');
});

// Entry and Sub entry buttons: start a sub-entry at the beginning of a new line under the one the cursor is on
// (or on the cursor's line, if that line is empty), and puts the cursor right beside the numeral.
function insertSub(level){
  if (!currentId) return;
  const sub = makeSub(level === 2 ? 2 : 1), t = caretTarget();
  let after;   // the text the cursor goes into
  if (t.text && t.text.parentNode) {
    let node = t.text, d = node.data, off = t.offset;
    // The line may carry on past this bit of text in bold or underlined writing: go to its real end.
    const real = lineEndAt(node, off);
    if (real.text !== node) { node = real.text; d = node.data; off = real.offset; }
    const start = off > 0 ? d.lastIndexOf('\n', off - 1) + 1 : 0, nl = d.indexOf('\n', off), end = nl === -1 ? d.length : nl;
    const prev = node.previousSibling;
    const emptyLine = real.text === t.text && !d.slice(start, end).trim()
      && (start > 0 || !prev || (prev.nodeType === 1 && prev.classList.contains('tasks')));
    if (emptyLine) {
      after = node.splitText(start);
      after.deleteData(0, end - start);   // the line's stray spaces
    } else {
      after = node.splitText(end);
      node.appendData('\n');
    }
    node.after(sub);
  } else {
    const parent = t.parent && els.body.contains(t.parent) && !t.parent.closest('.fig, .tasks, .quote, .sub, .indent, .written-day') ? t.parent : els.body;
    const ref = t.ref && t.ref.parentNode === parent ? t.ref : null;
    const prev = ref ? ref.previousSibling : parent.lastChild;
    parent.insertBefore(sub, ref);
    if (prev && !(prev.nodeType === 1 && prev.classList.contains('tasks'))) {
      if (prev.nodeType === 3) { if (!prev.data.endsWith('\n')) prev.appendData('\n'); }
      else sub.before(document.createTextNode('\n'));
    }
    after = sub.nextSibling && sub.nextSibling.nodeType === 3 ? sub.nextSibling : null;
    if (!after) { after = document.createTextNode(''); sub.after(after); }
  }
  onBodyChange();
  els.body.focus({preventScroll:true});
  document.getSelection().collapse(after, 0);
}
// Backspace just after a sub-entry's numeral or an indent, or Delete just before it, removes it.
function subBeside(backwards){
  const sel = document.getSelection();
  if (!sel.rangeCount || !sel.isCollapsed || !els.body.contains(sel.anchorNode)) return null;
  const n = sel.anchorNode, o = sel.anchorOffset;
  let sib = null;
  if (n.nodeType === 3) {
    if (backwards ? o === 0 : o === n.data.length) sib = backwards ? n.previousSibling : n.nextSibling;
  } else if (n.nodeType === 1) sib = backwards ? n.childNodes[o - 1] : n.childNodes[o];
  return sib && sib.nodeType === 1 && (sib.classList.contains('sub') || sib.classList.contains('indent')) ? sib : null;
}
function removeSub(sub){
  const parent = sub.parentNode, prev = sub.previousSibling, next = sub.nextSibling;
  sub.remove();
  const sel = document.getSelection();
  if (prev && prev.nodeType === 3 && prev.data) { const at = prev.data.length; parent.normalize(); sel.collapse(prev, at); }
  else if (next && next.nodeType === 3) sel.collapse(next, 0);
  else sel.collapse(parent, next ? [...parent.childNodes].indexOf(next) : parent.childNodes.length);
  onBodyChange();
}
/* Indenting: the shortcut (Tab unless changed in the Menu) lines the cursor's line up with the words beside
   the sub-entry numeral above it; Shift with the shortcut takes the indent away again. */
function indentCombo(){ return settings.indentKey || 'Tab'; }
// Where the cursor's line begins: {text, offset} inside a piece of text, or {parent, ref} between pieces.
function lineStart(){
  const sel = document.getSelection();
  if (!sel.rangeCount || !els.body.contains(sel.anchorNode)) return null;
  let n = sel.anchorNode, o = sel.anchorOffset;
  if (n.nodeType === 3) {
    const i = o > 0 ? n.data.lastIndexOf('\n', o - 1) : -1;
    if (i >= 0) return {text:n, offset:i + 1};
  } else { n = n.childNodes[o] || null; if (!n) { const p = sel.anchorNode; return scanBack(p, p.lastChild); } }
  return scanBack(n.parentNode, n.previousSibling);
}
function scanBack(parent, n){
  for (;;) {
    for (; n; n = n.previousSibling) {
      if (n.nodeType === 3) { const i = n.data.lastIndexOf('\n'); if (i >= 0) return {text:n, offset:i + 1}; }
      else if (n.classList.contains('tasks') || n.classList.contains('quote') || n.classList.contains('written-day')) return {parent, ref:n.nextSibling};
      else if (isFmt(n)) {   // bold or underlined writing: the line may begin inside it
        const texts = [], w = document.createTreeWalker(n, NodeFilter.SHOW_TEXT);
        for (let x = w.nextNode(); x; x = w.nextNode()) texts.push(x);
        for (const x of texts.reverse()) { const i = x.data.lastIndexOf('\n'); if (i >= 0) return {text:x, offset:i + 1}; }
      }
    }
    if (!isFmt(parent) || parent === els.body) return {parent, ref:parent.firstChild};
    n = parent.previousSibling; parent = parent.parentNode;   // carry on before the bold or underlined piece
  }
}
// What the line starts with, if it's a numeral or an indent.
function lineMarker(at){
  let next = at.text ? (at.offset < at.text.data.length ? null : at.text.nextSibling) : at.ref;
  if (!next && !(at.text && at.offset < at.text.data.length)) {   // at the end of a bold or underlined piece: look after it
    for (let p = at.text ? at.text.parentNode : at.parent; !next && isFmt(p) && p !== els.body; p = p.parentNode) next = p.nextSibling;
  }
  while (next && next.nodeType === 3 && !next.data) next = next.nextSibling;   // empty bits of text don't count
  return next && next.nodeType === 1 && (next.classList.contains('sub') || next.classList.contains('indent')) ? next : null;
}
function indentLine(){
  const at = lineStart(); if (!at) return;
  if (lineMarker(at)) return;   // already indented, or a sub-entry's own line
  const sel = document.getSelection(), atStart = sel.isCollapsed
    && (at.text ? sel.anchorNode === at.text && sel.anchorOffset === at.offset : sel.anchorNode === at.parent && at.parent.childNodes[sel.anchorOffset] === at.ref);
  const ind = makeIndent();
  if (at.text) {
    if (at.offset < at.text.data.length) at.text.splitText(at.offset);
    at.text.after(ind);
  } else at.parent.insertBefore(ind, at.ref);
  if (atStart) {
    let after = ind.nextSibling;
    if (!after || after.nodeType !== 3) { after = document.createTextNode(''); ind.after(after); }
    sel.collapse(after, 0);
  }
  onBodyChange();
}
function outdentLine(){
  const at = lineStart(); if (!at) return;
  const ind = lineMarker(at);
  if (ind && ind.classList.contains('indent')) removeSub(ind);
}
els.body.addEventListener('keydown', ev => {
  if (ev.isComposing || !ev.target.closest || ev.target.closest('.tasks')) return;
  const combo = comboOf(ev), key = indentCombo();
  if (!combo) return;
  if (combo === key) { ev.preventDefault(); indentLine(); }
  else if (ev.shiftKey && !key.includes('Shift') && combo.replace('Shift+', '') === key) { ev.preventDefault(); outdentLine(); }
});
/* Backspace right after a task list doesn't delete it: the cursor jumps to just before the list instead
   (above the first task, however many tasks are strung together). */
// (A quote counts the same way: Backspace just after one jumps above it rather than deleting it.)
const isTasks = n => n && n.nodeType === 1 && (n.classList.contains('tasks') || n.classList.contains('quote') || n.classList.contains('written-day'));
function tasksBefore(){
  const sel = document.getSelection();
  if (!sel.rangeCount || !sel.isCollapsed || !els.body.contains(sel.anchorNode)) return null;
  let n = sel.anchorNode, o = sel.anchorOffset, prev;
  if (n.nodeType === 3) { if (o > 0) return null; prev = n.previousSibling; }
  else prev = n.childNodes[o - 1] || null;
  for (;;) {
    while (prev && prev.nodeType === 3 && prev.data === '') prev = prev.previousSibling;   // empty bits of text don't count
    if (prev || !isFmt(n.nodeType === 3 ? n.parentNode : n)) break;
    n = n.nodeType === 3 ? n.parentNode : n;   // at the very start of bold or underlined writing: look before it
    prev = n.previousSibling;
  }
  return isTasks(prev) ? prev : null;
}
function jumpAboveTasks(block){
  // Lists separated only by empty bits of text count as one run of tasks: go above the first of them.
  for (let p = block.previousSibling; ; p = p.previousSibling) {
    if (p && p.nodeType === 3 && p.data === '') continue;
    if (isTasks(p)) { block = p; continue; }
    break;
  }
  let prev = block.previousSibling;
  while (prev && prev.nodeType === 3 && prev.data === '') prev = prev.previousSibling;
  const sel = document.getSelection();
  if (prev && prev.nodeType === 3) { els.body.focus({preventScroll:true}); sel.collapse(prev, prev.data.length); }
  else if (isFmt(prev)) { els.body.focus({preventScroll:true}); sel.selectAllChildren(prev); sel.collapseToEnd(); }
  else { const first = block.querySelector('.task'); if (first) focusTask(first, true); else caretBeside(block, true); }
}
els.body.addEventListener('keydown', ev => {
  if (ev.key !== 'Backspace' || ev.ctrlKey || ev.metaKey || ev.altKey || ev.isComposing) return;
  if (ev.target.closest && ev.target.closest('.tasks')) return;
  const block = tasksBefore();
  if (block) { ev.preventDefault(); jumpAboveTasks(block); }
});
els.body.addEventListener('keydown', ev => {
  if ((ev.key !== 'Backspace' && ev.key !== 'Delete') || ev.ctrlKey || ev.metaKey || ev.altKey) return;
  const block = subBeside(ev.key === 'Backspace');
  if (block) { ev.preventDefault(); removeSub(block); }
});
function deleteTask(li){
  const block = li.closest('.tasks');
  li.remove();
  if (!block.querySelector('.task')) removeTasks(block);
  else caretBeside(block, false);
  onBodyChange();
}
/* Dragging a task to a new place, in its own list or another list in the entry */
let taskDrag = null;
function startTaskDrag(ev, li){
  ev.preventDefault();
  taskDrag = {li, x0:ev.clientX, y0:ev.clientY, x:ev.clientX, y:ev.clientY, started:false, from:li.closest('.tasks'), before:'', raf:0};
  // Listen on the window: moving the task within the page would lose a pointer capture on it.
  window.addEventListener('pointermove', moveTaskDrag);
  window.addEventListener('pointerup', endTaskDrag);
  window.addEventListener('pointercancel', endTaskDrag);
}
function moveTaskDrag(ev){
  const d = taskDrag; if (!d) return;
  d.x = ev.clientX; d.y = ev.clientY;
  if (d.started || Math.hypot(d.x - d.x0, d.y - d.y0) < 4) return;
  d.started = true; d.before = serializeParts(domParts());
  if (!taskMenu.hidden) closeTaskMenu();
  d.li.classList.add('task-dragging'); document.body.classList.add('moving');
  d.raf = requestAnimationFrame(taskDragFrame);
}
function taskDragFrame(){
  const d = taskDrag; if (!d || !d.started) return;
  const mr = els.scroll.getBoundingClientRect(), edge = 60;
  if (d.y < mr.top + edge) els.scroll.scrollTop -= Math.ceil((mr.top + edge - d.y) / 4);
  else if (d.y > mr.bottom - edge) els.scroll.scrollTop += Math.ceil((d.y - (mr.bottom - edge)) / 4);
  // Put the task before or after whichever task the pointer is over.
  for (const other of els.body.querySelectorAll('.task')) {
    if (other === d.li) continue;
    const r = other.getBoundingClientRect();
    if (d.y < r.top || d.y > r.bottom) continue;
    if (d.y > r.top + r.height / 2) { if (other.nextElementSibling !== d.li) other.after(d.li); }
    else if (other.previousElementSibling !== d.li) other.before(d.li);
    break;
  }
  d.raf = requestAnimationFrame(taskDragFrame);
}
function endTaskDrag(){
  const d = taskDrag; if (!d) return;
  taskDrag = null;
  cancelAnimationFrame(d.raf);
  window.removeEventListener('pointermove', moveTaskDrag);
  window.removeEventListener('pointerup', endTaskDrag);
  window.removeEventListener('pointercancel', endTaskDrag);
  d.li.classList.remove('task-dragging'); document.body.classList.remove('moving');
  if (!d.started) { focusTask(d.li); return; }
  if (d.from.isConnected && !d.from.querySelector('.task')) removeTasks(d.from);   // its old list is now empty
  if (serializeParts(domParts()) !== d.before) onBodyChange();
}

els.body.addEventListener('keydown', ev => {
  const span = ev.target.closest ? ev.target.closest('.task-text') : null;
  if (!span) return;
  const li = span.closest('.task'), block = li.closest('.tasks');
  const sel = document.getSelection();
  const atStart = sel.isCollapsed && (span.textContent === '' || (sel.anchorOffset === 0 && (sel.anchorNode === span || sel.anchorNode === span.firstChild)));
  if (ev.key === 'Enter') {
    // Enter finishes the task and carries on writing underneath the list.
    ev.preventDefault();
    if (taskBlank(span)) {
      li.remove();
      if (!block.querySelector('.task')) { removeTasks(block); onBodyChange(); return; }
    }
    caretBeside(block, false);
    onBodyChange();
  } else if (ev.key === 'Backspace' && span.textContent === '' && !span.querySelector('.fig')) {
    ev.preventDefault();
    const prev = li.previousElementSibling, next = li.nextElementSibling;
    li.remove();
    if (prev) focusTask(prev); else if (next) focusTask(next, true); else removeTasks(block);
    onBodyChange();
  } else if (ev.key === 'ArrowUp') {
    ev.preventDefault();
    if (li.previousElementSibling) focusTask(li.previousElementSibling); else caretBeside(block, true);
  } else if (ev.key === 'ArrowDown') {
    ev.preventDefault();
    if (li.nextElementSibling) focusTask(li.nextElementSibling); else caretBeside(block, false);
  }
  void atStart;
});

/* The little menu for marking a task */
/* Urgency */
const URGENCY = {high:'High', medium:'Medium', low:'Low'};
const URGENCY_RANK = {high:0, medium:1, low:2};
function showUrgency(li){
  const u = li.dataset.urgency, tag = li.querySelector('.task-urg');
  if (URGENCY[u]) { tag.dataset.u = u; tag.textContent = URGENCY[u]; tag.hidden = false; tag.title = 'Urgency: ' + URGENCY[u] + '. Click to change'; }
  else { delete tag.dataset.u; tag.textContent = ''; tag.hidden = true; }
  const b = li.querySelector('.task-urg-btn'); if (b) b.title = URGENCY[u] ? 'Urgency: ' + URGENCY[u] : 'Set how urgent this task is';
}
const urgMenu = document.createElement('div');
urgMenu.className = 'task-menu urg-menu'; urgMenu.hidden = true; urgMenu.setAttribute('role', 'menu');
urgMenu.innerHTML = Object.entries(URGENCY).map(([k, v]) =>
  '<button type="button" role="menuitem" data-u="' + k + '"><span class="urg-dot"></span><span>' + v + '</span></button>').join('')
  + '<button type="button" role="menuitem" class="tm-clear" data-clear="1">No urgency</button>';
document.body.append(urgMenu);
let urgTask = null;
function openUrgencyMenu(li, anchor){
  urgTask = li;
  urgMenu.querySelector('.tm-clear').hidden = !li.dataset.urgency;
  urgMenu.hidden = false;
  const r = anchor.getBoundingClientRect(), w = urgMenu.offsetWidth;
  urgMenu.style.left = Math.max(8, Math.min(window.innerWidth - w - 8, r.right - w)) + 'px';
  urgMenu.style.top = (r.bottom + 6) + 'px';
  (urgMenu.querySelector('[data-u="' + li.dataset.urgency + '"]') || urgMenu.querySelector('button')).focus();
}
function closeUrgencyMenu(){
  const li = urgTask;
  urgMenu.hidden = true; urgTask = null;
  // Its buttons stay showing only if the focus went back into the task.
  if (li) setTimeout(() => { if (!li.contains(document.activeElement)) li.classList.remove('asking'); }, 0);
}
urgMenu.addEventListener('click', ev => {
  const b = ev.target.closest('button'), li = urgTask; if (!b || !li) return;
  const u = b.dataset.clear ? '' : b.dataset.u;
  closeUrgencyMenu();
  if (u !== li.dataset.urgency) { li.dataset.urgency = u; showUrgency(li); onBodyChange(); }
  focusTask(li);
});
urgMenu.addEventListener('keydown', ev => {
  if (ev.key !== 'ArrowDown' && ev.key !== 'ArrowUp') return;
  const list = [...urgMenu.querySelectorAll('button:not([hidden])')], i = list.indexOf(document.activeElement);
  ev.preventDefault(); list[(i + (ev.key === 'ArrowDown' ? 1 : -1) + list.length) % list.length].focus();
});
document.addEventListener('pointerdown', ev => { if (!urgMenu.hidden && !urgMenu.contains(ev.target) && !ev.target.closest('.task-urg-btn, .task-urg')) closeUrgencyMenu(); });
document.addEventListener('keydown', ev => { if (ev.key === 'Escape' && !urgMenu.hidden) { const li = urgTask; closeUrgencyMenu(); if (li) focusTask(li); } });
els.scroll.addEventListener('scroll', () => { if (!urgMenu.hidden) closeUrgencyMenu(); });

const taskMenu = document.createElement('div');
taskMenu.className = 'task-menu'; taskMenu.hidden = true; taskMenu.setAttribute('role', 'menu');
taskMenu.innerHTML = '<button type="button" role="menuitem" data-state="done" class="tm-done">' + ICONS.done + '<span>Success</span></button>'
  + '<button type="button" role="menuitem" data-state="fail" class="tm-fail">' + ICONS.fail + '<span>Failure</span></button>'
  + '<button type="button" role="menuitem" data-state="none" class="tm-clear"><span>Clear</span></button>';
document.body.append(taskMenu);
let menuTask = null;
function openTaskMenu(li, box){
  menuTask = li;
  taskMenu.querySelector('.tm-clear').hidden = li.dataset.state === 'none';
  taskMenu.hidden = false;
  const r = box.getBoundingClientRect(), w = taskMenu.offsetWidth;
  taskMenu.style.left = Math.max(8, Math.min(window.innerWidth - w - 8, r.right - w)) + 'px';
  taskMenu.style.top = (r.bottom + 6) + 'px';
  taskMenu.querySelector('button').focus();
}
function closeTaskMenu(){ taskMenu.hidden = true; menuTask = null; }
taskMenu.addEventListener('click', ev => {
  const b = ev.target.closest('button'); if (!b || !menuTask) return;
  // Note the time whenever the mark changes; clearing the mark clears the time too.
  if (b.dataset.state !== menuTask.dataset.state) menuTask.dataset.marked = b.dataset.state === 'none' ? '' : stampNow();
  // An archived task set back to not marked is ongoing again, so it shows in the Tasks menu once more.
  if (b.dataset.state === 'none') menuTask.dataset.archived = '';
  setTaskState(menuTask, b.dataset.state);
  const box = menuTask.querySelector('.task-box');
  closeTaskMenu(); onBodyChange(); box.focus();
});
document.addEventListener('pointerdown', ev => { if (!taskMenu.hidden && !taskMenu.contains(ev.target) && !ev.target.closest('.task-box')) closeTaskMenu(); });
document.addEventListener('keydown', ev => { if (ev.key === 'Escape' && !taskMenu.hidden) closeTaskMenu(); });
els.scroll.addEventListener('scroll', () => { if (!taskMenu.hidden) closeTaskMenu(); });

/* ---------- Placing images in the text ---------- */
// A drop target is either {text, offset}: a spot inside a run of text,
// or {parent, ref}: next to another picture (before `ref`, or at the end if ref is null).
function caretAt(x, y){
  if (document.caretPositionFromPoint) {
    const p = document.caretPositionFromPoint(x, y);
    return p && {node:p.offsetNode, offset:p.offset};
  }
  if (document.caretRangeFromPoint) {
    const r = document.caretRangeFromPoint(x, y);
    return r && {node:r.startContainer, offset:r.startOffset};
  }
  return null;
}
// Pictures go between words, never inside one.
function snapToWord(node, offset){
  const text = node.data, stops = [0, text.length];
  const ws = c => /\s/.test(c);
  for (let i = 1; i < text.length; i++) {
    if (ws(text[i - 1]) !== ws(text[i])) stops.push(i);
  }
  let best = 0, dist = Infinity;
  for (const s of stops) { const d = Math.abs(s - offset); if (d < dist) { dist = d; best = s; } }
  return best;
}
function dropTarget(x, y){
  const ed = els.body, r = ed.getBoundingClientRect();
  if (y < r.top) return {text:null, parent:ed, ref:ed.firstChild};
  const hit = document.elementFromPoint(x, y);
  const task = hit && hit.closest ? hit.closest('.task') : null;
  if (task && ed.contains(task)) return taskDropTarget(task, x, y, hit);
  const list = hit && hit.closest ? hit.closest('.tasks, .quote') : null;
  if (list && ed.contains(list)) {
    const lr = list.getBoundingClientRect();
    return {parent:list.parentNode, ref: y < lr.top + lr.height / 2 ? list : list.nextSibling};
  }
  const fig = hit && hit.closest ? hit.closest('.fig, .sub, .indent') : null;
  if (fig && ed.contains(fig)) {
    const fr = fig.getBoundingClientRect();
    return {parent:fig.parentNode, ref: x < fr.left + fr.width / 2 ? fig : fig.nextSibling};
  }
  const cx = Math.min(Math.max(x, r.left + 1), r.right - 1);
  const c = caretAt(cx, Math.min(y, r.bottom - 2));
  if (!c || !ed.contains(c.node)) return {parent:ed, ref:null};
  const inList = (c.node.nodeType === 1 ? c.node : c.node.parentElement).closest('.tasks, .quote, .sub, .indent, .written-day');
  if (inList) return {parent:inList.parentNode, ref:inList.nextSibling};
  if (c.node.nodeType === 3) return {text:c.node, offset:snapToWord(c.node, c.offset)};
  if (c.node.nodeType === 1 && !c.node.closest('.fig')) return {parent:c.node, ref:c.node.childNodes[c.offset] || null};
  return null;
}
// A picture dropped on a task goes into the task's words: between the words it's over, or at the end.
function taskDropTarget(li, x, y, hit){
  const span = li.querySelector('.task-text');
  const fig = hit.closest('.fig');
  if (fig && span.contains(fig)) {
    const fr = fig.getBoundingClientRect();
    return {task:li, parent:span, ref: x < fr.left + fr.width / 2 ? fig : fig.nextSibling};
  }
  const c = span.contains(hit) ? caretAt(x, y) : null;
  if (c && c.node.nodeType === 3 && span.contains(c.node)) return {task:li, text:c.node, offset:snapToWord(c.node, c.offset)};
  const last = span.lastChild;
  if (last && last.nodeType === 3) return {task:li, text:last, offset:last.data.length};
  return {task:li, parent:span, ref:null};
}
let markedTask = null;
function markTask(li){
  if (markedTask && markedTask !== li) markedTask.classList.remove('drop-into');
  markedTask = li || null;
  if (li) li.classList.add('drop-into');
}
function edgeY(node, top){
  if (!node) return null;
  if (node.nodeType === 1) { const b = node.getBoundingClientRect(); return top ? b.top : b.bottom; }
  const range = document.createRange(); range.selectNodeContents(node);
  const rects = range.getClientRects(); if (!rects.length) return null;
  return top ? rects[0].top : rects[rects.length - 1].bottom;
}
function targetRect(t){
  const range = document.createRange();
  if (t.text) { range.setStart(t.text, t.offset); range.collapse(true); }
  else {
    const kids = [...t.parent.childNodes], i = t.ref ? kids.indexOf(t.ref) : kids.length;
    range.setStart(t.parent, Math.max(0, i)); range.collapse(true);
    const near = t.ref || t.parent.lastChild;
    if (near && near.nodeType === 1 && near.classList.contains('tasks')) {
      const b = near.getBoundingClientRect();
      return {left:b.left, top: t.ref ? b.top - 5 : b.bottom + 2, height:3, width:b.width};
    }
    if (near && near.nodeType === 1) {
      const b = near.getBoundingClientRect();
      return {left: t.ref ? b.left - 2 : b.right + 1, top:b.top - 3, height:b.height + 6};
    }
  }
  const rc = range.getClientRects()[0] || range.getBoundingClientRect();
  if (rc && rc.height) return {left:rc.left - 1, top:rc.top, height:rc.height};
  const er = els.body.getBoundingClientRect();
  return {left:er.left, top:er.top, height:24};
}
function showMark(t){
  const m = els.mark;
  markTask(t && t.task);
  if (!t || (t.task && !t.task.querySelector('.task-text').childNodes.length)) { m.style.display = 'none'; return; }
  const r = targetRect(t);
  Object.assign(m.style, {display:'block', left:r.left + 'px', top:r.top + 'px', height:r.height + 'px', width: r.width ? r.width + 'px' : ''});
}
const isSpace = c => c === ' ' || c === '\u00a0';
// Keep one space between a picture and the words either side of it.
function tidyAround(fig){
  const prev = fig.previousSibling, next = fig.nextSibling;
  const before = prev ? (prev.nodeType === 3 ? prev.data.slice(-1) : 'x') : '';
  const after = next ? (next.nodeType === 3 ? next.data.charAt(0) : 'x') : '';
  if (before && !isSpace(before) && before !== '\n') fig.before(' ');
  if (!after || (!isSpace(after) && after !== '\n')) fig.after(' ');
}
function detachFigure(fig){
  const prev = fig.previousSibling, next = fig.nextSibling;
  fig.remove();
  const pEnd = prev && prev.nodeType === 3 ? prev.data.slice(-1) : '';
  const nStart = next && next.nodeType === 3 ? next.data.charAt(0) : '';
  // Returns which character was taken out, so a pending drop position can be adjusted.
  if (isSpace(nStart) && (!prev || isSpace(pEnd) || pEnd === '\n')) { next.data = next.data.slice(1); return {node:next, at:0}; }
  if (isSpace(pEnd) && (!next || nStart === '\n')) { prev.data = prev.data.slice(0, -1); return {node:prev, at:prev.data.length}; }
  return null;
}
function placeFigure(fig, t){
  if (t.text && t.text.parentNode) {
    const before = t.text, after = before.splitText(Math.min(t.offset, before.data.length));
    before.parentNode.insertBefore(fig, after);
  } else {
    const parent = t.parent && els.body.contains(t.parent) ? t.parent : els.body;
    const ref = t.ref && t.ref.parentNode === parent ? t.ref : null;
    parent.insertBefore(fig, ref);
  }
  tidyAround(fig);
  els.body.normalize();
}

/* Dragging an image within the entry */
let drag = null;
function startDrag(ev){
  if (ev.button !== 0) return;
  ev.preventDefault();
  const fig = ev.currentTarget;
  drag = {fig, x0:ev.clientX, y0:ev.clientY, x:ev.clientX, y:ev.clientY, started:false, target:null, ghost:null, raf:0};
  fig.setPointerCapture(ev.pointerId);
  fig.addEventListener('pointermove', moveDrag);
  fig.addEventListener('pointerup', endDrag);
  fig.addEventListener('pointercancel', cancelDrag);
}
function moveDrag(ev){
  if (!drag) return;
  drag.x = ev.clientX; drag.y = ev.clientY;
  if (!drag.started) {
    if (Math.hypot(drag.x - drag.x0, drag.y - drag.y0) < 4) return;
    drag.started = true;
    drag.fig.classList.add('dragging');
    document.body.classList.add('moving');
    let g;
    if (drag.fig.classList.contains('elink')) { g = document.createElement('span'); g.className = 'ghost fig elink'; g.textContent = drag.fig.textContent; }
    else if (drag.fig.classList.contains('epdf')) { g = document.createElement('span'); g.className = 'ghost epdf'; g.innerHTML = PDF_ICON; g.append(drag.fig.textContent); }
    else { g = document.createElement('img'); g.className = 'ghost'; g.src = drag.fig.querySelector('img').src; g.alt = ''; }
    document.body.append(g); drag.ghost = g;
    drag.raf = requestAnimationFrame(dragFrame);
  }
  drag.ghost.style.left = drag.x + 'px'; drag.ghost.style.top = drag.y + 'px';
}
function dragFrame(){
  if (!drag || !drag.started) return;
  const mr = els.scroll.getBoundingClientRect(), edge = 60;
  if (drag.y < mr.top + edge) els.scroll.scrollTop -= Math.ceil((mr.top + edge - drag.y) / 4);
  else if (drag.y > mr.bottom - edge) els.scroll.scrollTop += Math.ceil((drag.y - (mr.bottom - edge)) / 4);
  // A PDF held over a 3D model on the right makes the model into a book when it's let go.
  const bindTo = drag.fig.classList.contains('epdf') ? modelUnder(drag.x, drag.y) : null;
  markBindTarget(bindTo);
  const side = bindTo ? null : sideDrop(drag.x, drag.y);
  showSideDrop(side);
  if (bindTo) { drag.target = {bind:bindTo.dataset.name.slice(6)}; showMark(null); }
  else if (side) { drag.target = {side:true}; showMark(null); }
  else {
    drag.ghost.style.visibility = 'hidden';
    drag.target = dropTarget(drag.x, drag.y);
    drag.ghost.style.visibility = '';
    showMark(drag.target);
  }
  drag.raf = requestAnimationFrame(dragFrame);
}
function finishDrag(){
  const d = drag; drag = null;
  cancelAnimationFrame(d.raf);
  d.fig.removeEventListener('pointermove', moveDrag);
  d.fig.removeEventListener('pointerup', endDrag);
  d.fig.removeEventListener('pointercancel', cancelDrag);
  d.fig.classList.remove('dragging');
  document.body.classList.remove('moving');
  if (d.ghost) d.ghost.remove();
  showMark(null); showSideDrop(null); markBindTarget(null);
  return d;
}
function endDrag(){
  if (!drag) return;
  const d = finishDrag();
  const isLink = d.fig.classList.contains('elink'), isPdf = d.fig.classList.contains('epdf');
  if (!d.started) { if (isLink) openLinkView(d.fig.dataset.link, d.fig.dataset.title); else if (isPdf) openPdfView(d.fig.dataset.pdf, d.fig.dataset.title, true); else openViewer(d.fig); return; }
  if (d.target && d.target.bind) { bindBook(d.target.bind, d.fig.dataset.pdf); return; }
  // Dropped in the space right of the text: add it to what's shown there; it stays in the entry too.
  if (d.target && d.target.side) { addToShelf(isLink ? 'entry:' + d.fig.dataset.link : isPdf ? 'pdf:' + d.fig.dataset.pdf : d.fig.dataset.name); return; }
  if (!d.target || (d.target.parent && (d.target.ref === d.fig || d.target.ref === d.fig.nextSibling))) return;
  const beforeMove = serializeParts(domParts());
  const cut = detachFigure(d.fig);
  if (cut && d.target.text === cut.node && d.target.offset > cut.at) d.target.offset--;
  placeFigure(d.fig, d.target);
  if (serializeParts(domParts()) !== beforeMove) onBodyChange();
}
function cancelDrag(){ if (drag) finishDrag(); }

/* Remember where the text cursor was, so new images go there */
let lastCaret = null;
document.addEventListener('selectionchange', () => {
  const sel = document.getSelection();
  if (sel.rangeCount && els.body.contains(sel.anchorNode)) {
    const n = sel.anchorNode, o = sel.anchorOffset;
    const list = (n.nodeType === 1 ? n : n.parentElement).closest('.tasks, .quote, .sub, .indent, .written-day');
    if (list) lastCaret = {parent:list.parentNode, ref:list.nextSibling};
    else lastCaret = n.nodeType === 3 ? {text:n, offset:o} : {parent:n, ref:n.childNodes[o] || null};
  }
});
function caretTarget(){
  const t = lastCaret;
  if (!t) return {parent:els.body, ref:null};
  if (t.text && els.body.contains(t.text)) return {text:t.text, offset:Math.min(t.offset, t.text.data.length)};
  if (t.parent && els.body.contains(t.parent) && !t.parent.closest('.fig, .tasks, .quote, .sub, .indent, .written-day')) return t;
  return {parent:els.body, ref:null};
}

/* ---------- Adding and removing images ---------- */
async function addFiles(fileList, target){
  const all = [...fileList], models = all.filter(isModelFile), pdfs = all.filter(isPdfFile);
  const files = all.filter(f => !isModelFile(f) && !isPdfFile(f) && (!f.type || f.type.startsWith('image/')));
  if (!files.length && !models.length && !pdfs.length) return;
  if (!currentId) { newEntry(); target = null; }
  if (models.length) await addModels(models);   // 3D models go on the right, not into the writing
  let t = target || caretTarget();
  if (pdfs.length) t = await addPdfs(pdfs, t);   // PDFs go into the writing, where they were dropped
  if (!files.length) return;
  const id = currentId;
  let problem = '', added = 0;
  setStatus(files.length === 1 ? 'Adding image…' : 'Adding ' + files.length + ' images…');
  for (const f of files) {
    try {
      const name = await store.uploadImage(f);
      if (id !== currentId) {
        // The entry was closed mid-upload: add the picture at the end of its text.
        const e = entries.get(id);
        if (e) { e.body = serializeParts([...parseBody(e.body), {type:'img', name, title:f.name || ''}]); e.images = imagesIn(e.body); markChanged(id); }
        continue;
      }
      const fig = makeFigure(name, f.name || '');
      placeFigure(fig, t);
      t = {parent:fig.parentNode, ref:fig.nextSibling};
      added++;
      onBodyChange();
    } catch (err) {
      problem = err.message === 'type'
        ? f.name + " isn't a supported image. Use JPEG, PNG, GIF, WebP or AVIF."
        : err.message === 'size' ? f.name + ' is too large (the limit is 40 MB).'
        : "Couldn't add " + f.name + '. Check that the journal server is still running.';
    }
  }
  if (id === currentId && problem) setStatus(problem, true);
}
let viewingFig = null;
let changed = new Set();   // pictures that have been drawn on and can be restored
function openViewer(fig){
  els.viewer.classList.remove('readonly');
  viewingFig = fig;
  els.viewerImg.src = '/images/' + fig.dataset.name;
  showViewerTitle(fig.dataset.title || '', false);
  $('viewerRestore').hidden = !changed.has(fig.dataset.name);
  disarm($('viewerForever'), 'Delete forever');
  els.viewer.showModal();
}
function showViewerTitle(title, readOnly){
  const t = $('viewerTitle');
  t.value = title; t.readOnly = readOnly; t.hidden = readOnly && !title;
  t.title = readOnly ? '' : 'The picture\'s title. Click to change it';
}
// Changing the title changes it in the entry (and on the right, if the picture is there).
$('viewerTitle').addEventListener('input', () => {
  const fig = viewingFig;
  if (!fig || !els.body.contains(fig) || $('viewerTitle').readOnly) return;
  setFigTitle(fig, $('viewerTitle').value);
  onBodyChange();
});
$('viewerTitle').addEventListener('keydown', ev => { if (ev.key === 'Enter') { ev.preventDefault(); $('viewerTitle').blur(); } });
// Buttons that need a second click to confirm.
const armTimers = new WeakMap();
function disarm(btn, label){ clearTimeout(armTimers.get(btn)); btn.classList.remove('arm'); btn.textContent = label; }
function armed(btn, label, confirmLabel){
  if (btn.classList.contains('arm')) { disarm(btn, label); return true; }
  btn.classList.add('arm'); btn.textContent = confirmLabel;
  armTimers.set(btn, setTimeout(() => disarm(btn, label), 4000));
  return false;
}
async function restoreViewing(){
  const fig = viewingFig, id = currentId;
  if (!fig || !els.body.contains(fig)) { els.viewer.close(); return; }
  const name = fig.dataset.name;
  try {
    const {name:original, changed:stillChanged} = await store.restoreImage(name);
    changed.delete(name);
    if (stillChanged) changed.add(original);
    renameSide(id, name, original);
    fig.dataset.name = original; fig.querySelector('img').src = '/images/' + original;
    els.viewer.close();
    onBodyChange();
    await flush(id);
  } catch (e) {
    setStatus("Couldn't restore the original picture.", true);
    els.viewer.close();
  }
}
async function foreverViewing(){
  const btn = $('viewerForever');
  if (!armed(btn, 'Delete forever', 'Delete forever? This can\'t be undone')) return;
  const fig = viewingFig, id = currentId;
  els.viewer.close();
  if (!fig || !els.body.contains(fig)) return;
  const name = fig.dataset.name;
  detachFigure(fig);
  els.body.normalize();
  onBodyChange();
  await flush(id);
  const e = entries.get(id);
  if (e && !e.images.includes(name)) { changed.delete(name); store.removeImage(name, true).catch(() => {}); }
}
async function removeViewing(){
  const fig = viewingFig, id = currentId;
  els.viewer.close();
  if (!fig || !els.body.contains(fig)) return;
  const name = fig.dataset.name;
  detachFigure(fig);
  els.body.normalize();
  onBodyChange();
  await flush(id);
  const e = entries.get(id);
  if (e && !e.images.includes(name)) store.removeImage(name).catch(() => {});
}

/* ---------- Drawing ---------- */
const drawing = {el:$('draw'), canvas:$('canvas'), ctx:$('canvas').getContext('2d'), strokes:[], current:null,
  color:'ink', hlColor:'#FFE14D', size:4, tool:'pen', lastTool:'pen', dpr:1, id:null, raf:0, base:null, fig:null};
const COLORS = [['ink','Ink'], ['#9B2F3F','Red'], ['#2D5DA8','Blue'], ['#3F7D4E','Green'], ['#C7892B','Ochre']];
// The highlighter: bright colours laid on see-through, so the writing or picture beneath still shows.
const HL_COLORS = [['#FFE14D','Yellow'], ['#FF8FB8','Pink'], ['#7EE08A','Green'], ['#7CC6FF','Blue'], ['#FFB35C','Orange']];
const HL_ALPHA = 0.42;
// How wide a stroke is for the pen size chosen: the highlighter is broad, the eraser broader still.
const strokeWidth = (tool, size) => tool === 'eraser' ? size * 3 + 8 : tool === 'highlighter' ? size * 2 + 12 : size;
const SIZES = [[2,'Fine'], [5,'Medium'], [11,'Thick']];
const cssVar = name => getComputedStyle(document.documentElement).getPropertyValue(name).trim();
// Colour and pen-size buttons. The same pen is used on the drawing sheet and on the pictures on the right.
function buildDrawBar(sw = $('swatches'), sz = $('sizes'), hw = $('hlSwatches')){
  for (const [c, label] of COLORS) {
    const b = document.createElement('button');
    b.type = 'button'; b.className = 'swatch'; b.dataset.color = c; b.setAttribute('aria-label', label); b.title = label;
    b.style.background = c === 'ink' ? 'var(--ink)' : c;
    b.addEventListener('click', () => { drawing.color = c; setTool('pen'); });
    sw.append(b);
  }
  // The highlighter's colours sit beside the pen's: choosing one picks up the highlighter.
  for (const [c, label] of HL_COLORS) {
    const b = document.createElement('button');
    b.type = 'button'; b.className = 'swatch hl'; b.dataset.hl = c; b.setAttribute('aria-label', label + ' highlighter'); b.title = label + ' highlighter';
    b.style.background = c;
    b.addEventListener('click', () => { drawing.hlColor = c; setTool('highlighter'); });
    hw.append(b);
  }
  for (const [n, label] of SIZES) {
    const b = document.createElement('button');
    b.type = 'button'; b.className = 'size'; b.dataset.size = n; b.setAttribute('aria-label', label); b.title = label;
    const dot = document.createElement('span'); const d = Math.min(n + 2, 16) + 'px'; dot.style.width = d; dot.style.height = d;
    b.append(dot);
    b.addEventListener('click', () => { drawing.size = n; syncDrawBar(); });
    sz.append(b);
  }
}
function syncDrawBar(){
  const t = drawing.tool;
  // Only the colour of the tool in hand shows as chosen.
  document.querySelectorAll('.swatch').forEach(b => b.setAttribute('aria-pressed',
    String(b.dataset.hl ? t === 'highlighter' && b.dataset.hl === drawing.hlColor : t === 'pen' && b.dataset.color === drawing.color)));
  document.querySelectorAll('.pen-btn').forEach(b => b.setAttribute('aria-pressed', String(t === 'pen')));
  document.querySelectorAll('.size').forEach(b => b.setAttribute('aria-pressed', String(+b.dataset.size === drawing.size)));
  document.querySelectorAll('.hl-btn').forEach(b => b.setAttribute('aria-pressed', String(t === 'highlighter')));
  document.querySelectorAll('.eraser-btn').forEach(b => b.setAttribute('aria-pressed', String(t === 'eraser')));
}
// Pen, highlighter or eraser. Putting the eraser down goes back to whichever of the other two was in hand.
function setTool(t){
  if (t !== 'eraser') drawing.lastTool = t;
  drawing.tool = t; syncDrawBar();
}
const toggleEraser = () => setTool(drawing.tool === 'eraser' ? drawing.lastTool : 'eraser');
function placeOverlay(){
  const r = els.main.getBoundingClientRect();
  Object.assign(drawing.el.style, {left:r.left + 'px', top:r.top + 'px', width:r.width + 'px', height:r.height + 'px'});
}
function sizeCanvas(d = drawing){
  const c = d.canvas, r = c.getBoundingClientRect();
  d.dpr = window.devicePixelRatio || 1;
  c.width = Math.max(1, Math.round(r.width * d.dpr));
  c.height = Math.max(1, Math.round(r.height * d.dpr));
  redrawCanvas(d);
}
function strokeColor(s){ return s.color === 'ink' ? cssVar('--ink') : s.color; }
function paintStroke(ctx, s){
  const p = s.pts;
  // The highlighter is laid on see-through and multiplied into what's beneath, as real highlighter ink is:
  // a stroke is one even wash (going back over it within one stroke doesn't darken it), and dark
  // writing or lines under it stay dark. A second stroke over the first deepens the colour, as it would on paper.
  ctx.globalCompositeOperation = s.eraser ? 'destination-out' : s.hl ? 'multiply' : 'source-over';
  ctx.globalAlpha = s.hl ? HL_ALPHA : 1;
  ctx.strokeStyle = ctx.fillStyle = s.eraser ? '#000' : strokeColor(s);
  ctx.lineWidth = s.width; ctx.lineCap = s.hl ? 'butt' : 'round'; ctx.lineJoin = 'round';
  if (p.length === 1) {
    ctx.beginPath();
    if (s.hl) ctx.rect(p[0][0] - s.width / 4, p[0][1] - s.width / 2, s.width / 2, s.width);   // a dab of the flat tip
    else ctx.arc(p[0][0], p[0][1], s.width / 2, 0, Math.PI * 2);
    ctx.fill();
  } else {
    ctx.beginPath(); ctx.moveTo(p[0][0], p[0][1]);
    for (let i = 1; i < p.length - 1; i++) {
      ctx.quadraticCurveTo(p[i][0], p[i][1], (p[i][0] + p[i + 1][0]) / 2, (p[i][1] + p[i + 1][1]) / 2);
    }
    ctx.lineTo(p[p.length - 1][0], p[p.length - 1][1]);
    ctx.stroke();
  }
  ctx.globalAlpha = 1;
}
// Paints the picture being drawn on (if any) and every stroke, in canvas coordinates.
function paintScene(ctx, d = drawing){
  const b = d.base;
  ctx.globalCompositeOperation = 'source-over';
  if (b) ctx.drawImage(b.img, b.x, b.y, b.w, b.h);
  for (const s of d.strokes) paintStroke(ctx, s);
  ctx.globalCompositeOperation = 'source-over';
}
function redrawCanvas(d = drawing){
  const {ctx, canvas, dpr} = d;
  ctx.setTransform(1, 0, 0, 1, 0, 0);
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  paintScene(ctx, d);
}
// Centres the picture in the canvas, inside the margins. On the sheet it's only ever shrunk;
// on the right it fills the space the way the picture itself does.
function fitBase(d = drawing){
  const b = d.base; if (!b) return;
  const r = d.canvas.getBoundingClientRect(), p = d.pad ? d.pad() : {t:32, r:32, b:32, l:32};
  const aw = Math.max(1, r.width - p.l - p.r), ah = Math.max(1, r.height - p.t - p.b);
  const scale = Math.min(aw / b.img.naturalWidth, ah / b.img.naturalHeight, d.upscale ? Infinity : 1);
  const w = b.img.naturalWidth * scale, h = b.img.naturalHeight * scale;
  const nx = p.l + (aw - w) / 2, ny = p.t + (ah - h) / 2;
  if (b.w) {
    // Keep existing strokes lined up with the picture when the space changes size.
    const k = w / b.w;
    for (const s of d.strokes) { s.pts = s.pts.map(([x, y]) => [nx + (x - b.x) * k, ny + (y - b.y) * k]); s.width *= k; }
  }
  Object.assign(b, {x:nx, y:ny, w, h, scale});
}
function scheduleRedraw(d = drawing){
  if (d.raf) return;
  d.raf = requestAnimationFrame(() => { d.raf = 0; redrawCanvas(d); });
}
// Where the pointer is on the canvas. A canvas inside a scaled linked entry (cssW set) works in the entry's own sizes.
function canvasPoint(ev, d = drawing){
  const r = d.canvas.getBoundingClientRect(), k = d.cssW ? d.cssW / r.width : 1;
  return [(ev.clientX - r.left) * k, (ev.clientY - r.top) * k];
}
// Lets you draw on d.canvas with the current pen; onStroke runs as each stroke begins.
function attachPen(d, onStroke, onEnd){
  d.canvas.addEventListener('pointerdown', ev => {
    if (ev.button !== 0) return;
    ev.preventDefault();
    d.canvas.setPointerCapture(ev.pointerId);
    const t = drawing.tool;
    d.current = {color: t === 'highlighter' ? drawing.hlColor : drawing.color, width:strokeWidth(t, drawing.size),
      eraser: t === 'eraser', hl: t === 'highlighter', pts:[canvasPoint(ev, d)]};
    d.strokes.push(d.current);
    if (onStroke) onStroke();
    scheduleRedraw(d);
  });
  d.canvas.addEventListener('pointermove', ev => {
    if (!d.current) return;
    const evs = ev.getCoalescedEvents ? ev.getCoalescedEvents() : [ev];
    for (const e of (evs.length ? evs : [ev])) d.current.pts.push(canvasPoint(e, d));
    scheduleRedraw(d);
  });
  const endStroke = () => { const s = d.current; d.current = null; if (s && onEnd) onEnd(s); };
  d.canvas.addEventListener('pointerup', endStroke);
  d.canvas.addEventListener('pointercancel', endStroke);
}
attachPen(drawing, () => disarmDiscard());

// Opens the drawing sheet. With `fig`, that picture is loaded so you can draw on it.
async function openDrawing(fig){
  if (!currentId || !drawing.el.hidden) return;
  if (side.active) finishSideDraw();   // one drawing at a time
  drawing.id = currentId; drawing.strokes = []; drawing.current = null; drawing.base = null;
  drawing.fig = fig instanceof Element ? fig : null;
  if (drawing.fig) {
    const img = new Image();
    img.src = '/images/' + drawing.fig.dataset.name;
    try { await img.decode(); } catch (e) { setStatus("Couldn't open that picture for drawing.", true); return; }
    drawing.base = {img, name:drawing.fig.dataset.name, x:0, y:0, w:0, h:0, scale:1};
  }
  drawing.el.hidden = false;
  setTool('pen');   // each drawing starts with the pen in hand
  placeOverlay();
  const r = drawing.canvas.getBoundingClientRect();
  drawing.dpr = window.devicePixelRatio || 1;
  drawing.canvas.width = Math.max(1, Math.round(r.width * drawing.dpr));
  drawing.canvas.height = Math.max(1, Math.round(r.height * drawing.dpr));
  fitBase(); redrawCanvas(); syncDrawBar(); disarmDiscard();
  $('drawDone').focus();
}
function closeOverlay(){ drawing.el.hidden = true; drawing.current = null; drawing.base = null; drawing.fig = null; disarmDiscard(); }
// The part of the canvas that has pen marks on it, with a little margin.
function drawnBounds(d = drawing){
  const pen = d.strokes.filter(s => !s.eraser), b = d.base;
  if (b) {
    // Drawing on a picture: keep the whole picture, plus anything drawn beyond its edges.
    let x0 = b.x, y0 = b.y, x1 = b.x + b.w, y1 = b.y + b.h;
    for (const s of pen) for (const [x, y] of s.pts) {
      x0 = Math.min(x0, x - s.width - 12); y0 = Math.min(y0, y - s.width - 12);
      x1 = Math.max(x1, x + s.width + 12); y1 = Math.max(y1, y + s.width + 12);
    }
    const r = d.canvas.getBoundingClientRect();
    x0 = Math.max(0, x0); y0 = Math.max(0, y0); x1 = Math.min(r.width, x1); y1 = Math.min(r.height, y1);
    return {x:x0, y:y0, w:x1 - x0, h:y1 - y0};
  }
  if (!pen.length) return null;
  let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
  for (const s of pen) for (const [x, y] of s.pts) {
    x0 = Math.min(x0, x - s.width); y0 = Math.min(y0, y - s.width);
    x1 = Math.max(x1, x + s.width); y1 = Math.max(y1, y + s.width);
  }
  const r = d.canvas.getBoundingClientRect(), pad = 18;
  x0 -= pad; y0 -= pad; x1 += pad; y1 += pad;
  x0 = Math.max(0, x0); y0 = Math.max(0, y0);
  x1 = Math.min(r.width, x1 + pad); y1 = Math.min(r.height, y1 + pad);
  return x1 > x0 && y1 > y0 ? {x:x0, y:y0, w:x1 - x0, h:y1 - y0} : null;
}
function endOfLastWord(){
  const kids = els.body.childNodes;
  for (let i = kids.length - 1; i >= 0; i--) {
    const n = kids[i];
    if (n.nodeType === 1 && n.classList.contains('fig')) return {parent:els.body, ref:n.nextSibling};
    if (n.nodeType === 3 && /\S/.test(n.data)) {
      let k = n.data.length; while (k > 0 && /\s/.test(n.data[k - 1])) k--;
      return {text:n, offset:k};
    }
  }
  return {parent:els.body, ref:null};
}
// Renders the picture and strokes inside bounds b, at the picture's own resolution (or the screen's).
function renderDrawing(d, b){
  const base = d.base;
  const k = Math.min(base ? Math.max(d.dpr, 1 / base.scale) : d.dpr, 4000 / Math.max(b.w, b.h));
  const W = Math.max(1, Math.round(b.w * k)), Hh = Math.max(1, Math.round(b.h * k));
  const layer = document.createElement('canvas'); layer.width = W; layer.height = Hh;
  const l = layer.getContext('2d');
  l.setTransform(k, 0, 0, k, -b.x * k, -b.y * k);
  paintScene(l, d);
  const out = document.createElement('canvas'); out.width = W; out.height = Hh;
  const o = out.getContext('2d');
  o.fillStyle = cssVar('--sheet') || '#ffffff';
  o.fillRect(0, 0, W, Hh);
  o.drawImage(layer, 0, 0);
  return out;
}
// Photos stay JPEG so they don't balloon in size; drawings are saved as PNG for crisp lines.
function drawnBlob(base, out){
  const photo = base && /\.(jpg|webp|avif)$/.test(base.name);
  return new Promise(res => photo ? out.toBlob(res, 'image/jpeg', 0.92) : out.toBlob(res, 'image/png'));
}
async function finishDrawing(){
  if (drawing.el.hidden) return;
  const id = drawing.id, fig = drawing.fig, base = drawing.base, b = drawnBounds();
  if (!b || (base && !drawing.strokes.length)) { closeOverlay(); return; }
  const out = renderDrawing(drawing, b);
  closeOverlay();
  await saveDrawing(id, base, fig, await drawnBlob(base, out));
}
// Saves a finished drawing. On a picture (base), it replaces that picture wherever it sits in the entry:
// just `fig` if given, otherwise every place the picture appears.
async function saveDrawing(id, base, fig, blob){
  if (id === currentId) setStatus('Saving drawing…');
  try {
    const name = await store.uploadImage(blob);
    if (base) {
      // Drawing on an existing picture replaces it where it sits; the old one is kept in "original images".
      const old = base.name;
      renameSide(id, old, name);
      const figs = id !== currentId ? []
        : (fig ? [fig] : [...els.body.querySelectorAll('.fig')].filter(f => f.dataset.name === old)).filter(f => els.body.contains(f));
      if (figs.length) {
        for (const f of figs) { f.dataset.name = name; f.querySelector('img').src = '/images/' + name; }
        onBodyChange();
      } else {
        const e = entries.get(id);
        if (e) { e.body = swapImage(e.body, old, name); e.images = imagesIn(e.body); markChanged(id); }
      }
      await flush(id);
      // The old version is kept in "original images" so it can be restored.
      try { await store.linkDrawing(name, old); changed.delete(old); changed.add(name); }
      catch (err) { if (id === currentId) setStatus("The drawing was saved, but the original picture couldn't be set aside.", true); }
    } else if (id === currentId) {
      const fig = makeFigure(name, 'Drawing');
      placeFigure(fig, endOfLastWord());
      onBodyChange();
    } else {
      const e = entries.get(id);
      if (e) { e.body = e.body.replace(/\s*$/, '') + ' ' + token(name, 'Drawing') + ' '; e.images = imagesIn(e.body); markChanged(id); }
    }
    return name;
  } catch (err) {
    if (id === currentId) setStatus("Couldn't save the drawing. Check that the journal server is still running.", true);
    return null;
  }
}
let discardTimer;
function disarmDiscard(){ clearTimeout(discardTimer); const d = $('discard'); d.classList.remove('arm'); d.textContent = 'Discard'; }
$('discard').addEventListener('click', () => {
  const d = $('discard');
  if (!drawing.strokes.length || d.classList.contains('arm')) { closeOverlay(); return; }
  d.classList.add('arm'); d.textContent = 'Discard drawing?';
  discardTimer = setTimeout(disarmDiscard, 4000);
});
$('drawBtn').addEventListener('click', () => openDrawing());
$('tasksBtn').addEventListener('mousedown', ev => ev.preventDefault());   // keep the cursor where it is
$('tasksBtn').addEventListener('click', insertTask);
$('subBtn').addEventListener('mousedown', ev => ev.preventDefault());   // keep the cursor where it is
$('subBtn').addEventListener('click', () => insertSub(1));
$('subSubBtn').addEventListener('mousedown', ev => ev.preventDefault());
$('subSubBtn').addEventListener('click', () => insertSub(2));
$('drawDone').addEventListener('click', finishDrawing);
$('eraser').addEventListener('click', toggleEraser);
$('highlighter').addEventListener('click', () => setTool('highlighter'));
$('pen').addEventListener('click', () => setTool('pen'));
$('undo').addEventListener('click', () => { drawing.strokes.pop(); redrawCanvas(); });
$('clear').addEventListener('click', () => { drawing.strokes = []; redrawCanvas(); });
document.addEventListener('keydown', ev => {
  if (drawing.el.hidden) return;
  if (ev.key === 'Escape') { ev.preventDefault(); finishDrawing(); }
  else if ((ev.ctrlKey || ev.metaKey) && ev.key.toLowerCase() === 'z') { ev.preventDefault(); drawing.strokes.pop(); redrawCanvas(); }
});
window.addEventListener('resize', () => { if (!drawing.el.hidden) { placeOverlay(); sizeCanvas(); fitBase(); redrawCanvas(); } });
buildDrawBar();

/* ---------- Drawing on a picture on the right ----------
   Each picture's Draw button opens out sideways into the same pen tools as the drawing sheet,
   and folds back into the button when you're done. The drawing then takes the picture's place in
   the entry, just as drawing on it from the viewer does, so Restore brings back the one before. */
// kind is 'picture' or 'entry' (a linked entry, drawn over with a layer of ink that scrolls with its writing);
// key is the name the item goes by on the right: the picture's name, or "entry:<id>".
const side = {active:false, kind:'picture', key:null, item:null, menu:null, canvas:null, ctx:null, strokes:[], current:null, dpr:1, raf:0,
  base:null, id:null, upscale:true, resize:null, saving:new Set(), page:null, inkW:0, cleared:false,
  // Keep the whole picture clear of the tools along the top.
  pad(){
    const it = side.item.getBoundingClientRect(), mb = side.menu.el.getBoundingClientRect().bottom;
    return {t:Math.max(10, mb - it.top + 8), r:10, b:10, l:10};
  }};
const calm = () => matchMedia('(prefers-reduced-motion: reduce)').matches;
function makeSideMenu(){
  const el = document.createElement('div'); el.className = 'side-draw';
  el.setAttribute('role', 'toolbar'); el.setAttribute('aria-label', 'Drawing on this picture');
  const tools = document.createElement('div'); tools.className = 'side-draw-tools';
  const group = label => { const g = document.createElement('span'); g.className = 'draw-group'; g.setAttribute('aria-label', label); return g; };
  const btn = (cls, text) => { const b = document.createElement('button'); b.type = 'button'; b.className = cls; b.textContent = text; return b; };
  const sw = group('Pen colour'), hw = group('Highlighter colour'), sz = group('Pen size');
  const pen = btn('tool pen-btn', 'Pen'), hl = btn('tool hl-btn', 'Highlighter'), eraser = btn('tool eraser-btn', 'Eraser'), undo = btn('tool', 'Undo'), clear = btn('tool', 'Clear');
  const discard = btn('tool', 'Discard'), done = btn('draw-done', 'Done');
  pen.setAttribute('aria-pressed', 'true'); hl.setAttribute('aria-pressed', 'false'); eraser.setAttribute('aria-pressed', 'false');
  buildDrawBar(sw, sz, hw);
  // Discard and Done come straight after the other tools, kept together so they're never split across rows.
  const end = document.createElement('span'); end.className = 'side-draw-end';
  end.append(discard, done);
  tools.append(sw, hw, sz, pen, hl, eraser, undo, clear, end);
  el.append(tools);
  pen.addEventListener('click', () => setTool('pen'));
  hl.addEventListener('click', () => setTool('highlighter'));
  eraser.addEventListener('click', toggleEraser);
  undo.addEventListener('click', sideUndo);
  clear.addEventListener('click', sideClear);
  discard.addEventListener('click', () => {
    if ((!side.strokes.length && !side.cleared && !side.marksChanged) || armed(discard, 'Discard', 'Discard drawing?')) closeSide();
  });
  done.addEventListener('click', finishSideDraw);
  // When the tools don't all fit, they scroll sideways (the mouse wheel works too) and fade at the edge that has more.
  const fades = () => {
    tools.classList.toggle('more-left', tools.scrollLeft > 1);
    tools.classList.toggle('more-right', tools.scrollLeft + tools.clientWidth < tools.scrollWidth - 1);
  };
  tools.addEventListener('scroll', fades);
  tools.addEventListener('wheel', ev => {
    if (tools.scrollWidth <= tools.clientWidth || Math.abs(ev.deltaX) >= Math.abs(ev.deltaY)) return;
    ev.preventDefault(); tools.scrollLeft += ev.deltaY;
  }, {passive:false});
  tools.addEventListener('focusin', ev => ev.target.scrollIntoView({block:'nearest', inline:'nearest'}));
  return {el, tools, discard, done, fades};
}
// A clip that makes the open menu look like just the Draw button: it opens out of it and folds back into it.
function buttonClip(menu, btn){
  const m = menu.getBoundingClientRect(), b = btn.getBoundingClientRect();
  const c = v => Math.max(0, v).toFixed(1) + 'px';
  return 'inset(' + c(b.top - m.top) + ' ' + c(m.right - b.right) + ' ' + c(m.bottom - b.bottom) + ' ' + c(b.left - m.left) + ' round 999px)';
}
// Sizes the canvas to its picture's space and lays the picture out in it.
function sideFit(){
  if (side.kind === 'entry') { inkFit(); return; }
  const r = side.canvas.getBoundingClientRect();
  if (r.width < 20 || r.height < 20) return;   // hidden for now (window too narrow): keep things as they are
  side.dpr = window.devicePixelRatio || 1;
  side.canvas.width = Math.max(1, Math.round(r.width * side.dpr));
  side.canvas.height = Math.max(1, Math.round(r.height * side.dpr));
  fitBase(side); redrawCanvas(side); side.menu.fades();
}
/* ---------- Drawing over a linked entry on the right ----------
   Highlights over writing are kept as the words they cover (with the words themselves, so they're found
   again if the linked entry is edited), and are shown on those words wherever they fall.
   Pen marks are kept as a see-through picture. So that they stay on what they were drawn over, an entry
   with pen marks keeps the layout it had when they were drawn (its width and writing sizes), and is
   scaled as a whole to fit its box, as a picture would be. */
const FROZEN_SKIP = new Set(['--shelf-h', '--shelf-scale', '--brand-size', '--title-size', '--list-topic-size', '--task-menu-scale']);
function inkRec(e, linked){
  const r = e && e.inks ? e.inks[linked] : null;
  return !r ? null : typeof r === 'string' ? {img:r} : r;
}
// The sizes the writing is laid out with now, to be kept with pen marks.
function layoutVars(){
  const cs = getComputedStyle(document.documentElement), v = {};
  for (const s of SIZE_SETTINGS) {
    if (!s.cssVar || FROZEN_SKIP.has(s.cssVar)) continue;
    const x = cs.getPropertyValue(s.cssVar).trim();
    if (/^-?[0-9.]{1,12}(px|em|rem|%)?$/.test(x)) v[s.cssVar] = x;
  }
  return v;
}
const frozenViews = new ResizeObserver(list => { for (const en of list) fitFrozen(en.target); });
function freezePage(page, w, vars){
  page.classList.add('frozen'); page.dataset.w = w; page.style.width = w + 'px';
  for (const [k, x] of Object.entries(vars || {})) page.style.setProperty(k, x);
  const view = page.closest('.shelf-entry-view'); view.classList.add('frozen');
  frozenViews.observe(view); fitFrozen(view);
}
// Scales a frozen entry to fill its box.
function fitFrozen(view){
  const page = view.querySelector(':scope > .shelf-entry-page.frozen'); if (!page || !view.isConnected) return;
  const cs = getComputedStyle(view), avail = view.clientWidth - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
  if (avail < 20) return;
  page.style.zoom = String(avail / +page.dataset.w);
  if (side.active && side.page === page) inkFit();
}
// The canvas covers the whole of the entry's writing (not just the part in view), and scrolls with it.
function inkFit(){
  clearOfMenu();
  const page = side.page, W = side.inkW, z = parseFloat(page.style.zoom) || 1, pr = page.getBoundingClientRect();
  if (pr.width < 20) return;   // hidden for now (window too narrow): keep things as they are
  const b = side.base;
  if (b) Object.assign(b, {x:0, y:0, w:W, h:W * b.img.naturalHeight / b.img.naturalWidth});
  const H = Math.max(pr.height / z, b ? b.h : 0, (page.parentElement.clientHeight - page.offsetTop - 16) / z, 20);
  side.canvas.style.height = H + 'px';
  // Very long entries: keep the canvas within what browsers can draw on.
  side.dpr = Math.min((window.devicePixelRatio || 1) * z, 16000 / Math.max(W, H));
  side.canvas.width = Math.max(1, Math.round(W * side.dpr));
  side.canvas.height = Math.max(1, Math.round(H * side.dpr));
  redrawCanvas(side); side.menu.fades();
}
// The text of an entry's writing, piece by piece, with the place each piece starts.
function textPieces(box){
  const out = []; if (!box) return out;
  const w = document.createTreeWalker(box, NodeFilter.SHOW_TEXT); let off = 0, n;
  while ((n = w.nextNode())) { out.push({node:n, off}); off += n.data.length; }
  return out;
}
// Finds each highlight's words in the writing as it is now: where they were if they're still there,
// otherwise the nearest place they appear. A highlight whose words have gone is kept, but not shown.
function resolveMarks(T, marks){
  return marks.map(m => {
    if (!m.q) return {...m, lost:true};
    if (T.slice(m.s, m.e) === m.q) return {...m, lost:false};
    let best = -1;
    for (let i = T.indexOf(m.q); i !== -1; i = T.indexOf(m.q, i + 1)) if (best < 0 || Math.abs(i - m.s) < Math.abs(best - m.s)) best = i;
    return best < 0 ? {...m, lost:true} : {...m, s:best, e:best + m.q.length, lost:false};
  });
}
function wrapRange(box, s, e, colour){
  for (const {node, off} of textPieces(box)) {
    const a = Math.max(s, off), b = Math.min(e, off + node.data.length);
    if (a >= b) continue;
    let n = node;
    if (b - off < n.data.length) n.splitText(b - off);
    if (a > off) n = n.splitText(a - off);
    const m = document.createElement('mark'); m.className = 'ink-hl'; m.style.setProperty('--hl', colour);
    n.replaceWith(m); m.append(n);
  }
}
// Shows the highlights on the writing, and returns them with their places brought up to date.
function renderMarks(box, marks){
  if (!box) return [];
  for (const m of box.querySelectorAll('mark.ink-hl')) m.replaceWith(...m.childNodes);
  box.normalize();
  const out = resolveMarks(box.textContent, marks || []);
  for (const m of out) if (!m.lost) wrapRange(box, m.s, m.e, m.c);
  return out;
}
// How far a point is from a stroke's centre line. With flat ends (the highlighter's tip), a point beyond
// either end of the stroke isn't on it at all.
function distToLine(px, py, pts, flat){
  if (pts.length === 1) return Math.hypot(px - pts[0][0], py - pts[0][1]);
  let best = Infinity;
  for (let i = 1; i < pts.length; i++) {
    const [x1, y1] = pts[i - 1], [x2, y2] = pts[i], dx = x2 - x1, dy = y2 - y1, L = dx * dx + dy * dy;
    const raw = L ? ((px - x1) * dx + (py - y1) * dy) / L : 0;
    if (flat && L && ((i === 1 && raw < 0) || (i === pts.length - 1 && raw > 1))) continue;
    const t = Math.max(0, Math.min(1, raw));
    best = Math.min(best, Math.hypot(px - (x1 + t * dx), py - (y1 + t * dy)));
  }
  return best;
}
// The words a stroke passes over, as [start, end) places in the writing. A word counts when the stroke
// covers at least half its letters; words next to each other are joined, with the space between them.
function wordsUnder(box, stroke){
  if (!box) return [];
  const cr = side.canvas.getBoundingClientRect(), k = side.inkW / cr.width, half = stroke.width / 2;
  const pts = stroke.pts.filter((p, i, a) => !i || p[0] !== a[i - 1][0] || p[1] !== a[i - 1][1]);   // no repeated points
  let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
  for (const [x, y] of stroke.pts) { x0 = Math.min(x0, x); y0 = Math.min(y0, y); x1 = Math.max(x1, x); y1 = Math.max(y1, y); }
  x0 -= half; y0 -= half; x1 += half; y1 += half;
  const toInk = r => ({x:(r.left - cr.left) * k, y:(r.top - cr.top) * k, w:r.width * k, h:r.height * k});
  const near = r => r.x < x1 && r.x + r.w > x0 && r.y < y1 && r.y + r.h > y0;
  const covered = new Set(), range = document.createRange();
  for (const {node, off} of textPieces(box)) {
    range.selectNodeContents(node);
    if (![...range.getClientRects()].some(r => near(toInk(r)))) continue;
    for (let i = 0; i < node.data.length; i++) {
      if (/\s/.test(node.data[i])) continue;
      range.setStart(node, i); range.setEnd(node, i + 1);
      const r = toInk(range.getBoundingClientRect());
      if ((r.w || r.h) && near(r) && distToLine(r.x + r.w / 2, r.y + r.h / 2, pts, stroke.hl) <= half) covered.add(off + i);
    }
  }
  if (!covered.size) return [];
  const T = box.textContent, out = [], re = /\S+/g;
  let m, prev = false;
  while ((m = re.exec(T))) {
    let n = 0;
    for (let i = m.index; i < m.index + m[0].length; i++) if (covered.has(i)) n++;
    const on = n > 0 && n * 2 >= m[0].length;
    if (on && prev) out[out.length - 1][1] = m.index + m[0].length;
    else if (on) out.push([m.index, m.index + m[0].length]);
    prev = on;
  }
  return out;
}
// Highlights tidied: no spaces at their ends, and those of one colour that touch or overlap made one.
function tidyMarks(T, marks){
  const lost = marks.filter(m => m.lost), out = [];
  const live = marks.filter(m => !m.lost).map(m => {
    let s = m.s, e = m.e;
    while (s < e && /\s/.test(T[s])) s++;
    while (e > s && /\s/.test(T[e - 1])) e--;
    return {s, e, c:m.c};
  }).filter(m => m.e > m.s).sort((a, b) => a.c < b.c ? -1 : a.c > b.c ? 1 : a.s - b.s);
  for (const m of live) {
    const last = out[out.length - 1];
    if (last && last.c === m.c && (m.s <= last.e || !/\S/.test(T.slice(last.e, m.s)))) last.e = Math.max(last.e, m.e);
    else out.push({...m});
  }
  for (const m of out) m.q = T.slice(m.s, m.e);
  return out.sort((a, b) => a.s - b.s).concat(lost);
}
function eraseMarks(T, marks, ranges){
  let out = marks;
  for (const [a, b] of ranges) {
    out = out.flatMap(m => m.lost || m.e <= a || m.s >= b ? [m] : [{...m, e:a}, {...m, s:b}].filter(x => x.e > x.s));
  }
  return tidyMarks(T, out);
}
// As each stroke on a linked entry ends: a highlighter stroke over writing goes onto the words it covers
// (a stroke in the margin stays as drawn), and the eraser takes highlights off the words it passes over.
function inkStrokeDone(s){
  if (side.kind !== 'entry') return;
  const box = side.box, before = side.marks, T = box ? box.textContent : '';
  const words = (s.hl || s.eraser) ? wordsUnder(box, s) : [];
  if (s.hl && words.length) {
    side.strokes.splice(side.strokes.indexOf(s), 1);
    side.marks = renderMarks(box, tidyMarks(T, before.concat(words.map(([a, b]) => ({s:a, e:b, c:s.color})))));
    side.hist.push({marks:before}); side.marksChanged = true;
    redrawCanvas(side); return;
  }
  if (s.eraser && words.length) {
    const after = eraseMarks(T, before, words);
    if (JSON.stringify(after) !== JSON.stringify(tidyMarks(T, before))) {
      side.marks = renderMarks(box, after); side.marksChanged = true;
      side.hist.push({stroke:true, marks:before}); return;
    }
  }
  side.hist.push({stroke:true});
}
function sideUndo(){
  if (!side.active) return;
  if (side.kind !== 'entry') { side.strokes.pop(); redrawCanvas(side); return; }
  const h = side.hist.pop(); if (!h) return;
  if (h.stroke) side.strokes.pop();
  if (h.marks) { side.marks = renderMarks(side.box, h.marks); side.marksChanged = true; }
  redrawCanvas(side);
}
// On a linked entry, Clear takes off everything, the ink and highlights from before included (Discard brings them back).
function sideClear(){
  side.strokes = []; side.hist = [];
  if (side.kind === 'entry') {
    if (side.base) { side.base = null; side.cleared = true; }
    if (side.marks.length) { side.marks = renderMarks(side.box, []); side.marksChanged = true; }
  }
  redrawCanvas(side);
}
function clearOfMenu(){
  const view = side.page && side.page.parentElement;
  if (view) view.style.paddingTop = Math.max(42, side.menu.el.offsetHeight + 16) + 'px';
}
function refreshShelf(){ if (currentId) { $('shelf').dataset.key = currentId + '|refresh'; renderShelf(); } }
const loadImage = async src => { const img = new Image(); img.src = src; await img.decode(); return img; };
async function openSideDraw(item){
  const key = item.dataset.name, kind = isReadRef(key) ? 'entry' : 'picture';
  if (!currentId || !drawing.el.hidden || side.saving.has(key)) return;
  if (side.active) { if (side.item === item) return; finishSideDraw(); }
  const id = currentId, e = entries.get(id);
  // A picture is drawn on directly; a linked entry has its ink from before (if any) brought back to add to.
  const rec = kind === 'entry' ? inkRec(e, inkKey(key)) : null, inkName = rec ? rec.img : null;
  let img = null;
  try { if (kind === 'picture') img = await loadImage('/images/' + key); else if (inkName) img = await loadImage('/images/' + inkName); }
  catch (err) { setStatus(kind === 'picture' ? "Couldn't open that picture for drawing." : "Couldn't open the ink on that entry.", true); return; }
  if (!item.isConnected || id !== currentId || side.active || !drawing.el.hidden) return;
  const bar = item.querySelector('.zoom-bar'), btn = item.querySelector('.side-draw-btn');
  const canvas = document.createElement('canvas'); canvas.className = 'side-canvas';
  const page = kind === 'entry' ? item.querySelector('.shelf-entry-page') : null;
  if (page) page.append(canvas); else item.insertBefore(canvas, bar);
  // A linked entry is held to the layout it has now while it's drawn on (before it opens out to full size).
  const vars = rec && rec.w ? rec.v || {} : layoutVars();
  if (page && !page.classList.contains('frozen')) freezePage(page, Math.round(page.getBoundingClientRect().width * 100) / 100, vars);
  const menu = makeSideMenu();
  Object.assign(side, {active:true, kind, key, item, menu, canvas, ctx:canvas.getContext('2d'), strokes:[], current:null, id,
    page, inkW: page ? +page.dataset.w : 0, cssW: page ? +page.dataset.w : 0, vars, cleared:false,
    box: page ? page.querySelector('.link-body') : null, marks: item.inkMarks || [], marksChanged:false, hist:[],
    base: img ? {img, name: kind === 'picture' ? key : inkName, x:0, y:0, w:0, h:0, scale:1} : null});
  attachPen(side, () => disarm(menu.discard, 'Discard'), inkStrokeDone);
  setTool('pen');   // each drawing starts with the pen in hand
  bar.append(menu.el);
  item.classList.add('drawing', 'inked');
  item.scrollIntoView({block:'nearest'});
  sideFit(); syncDrawBar();
  side.resize = new ResizeObserver(() => { if (side.active && side.canvas === canvas) sideFit(); });
  side.resize.observe(page || canvas); side.resize.observe(menu.el);   // the tools may take more rows or fewer
  if (!calm()) {
    menu.el.animate([{clipPath:buttonClip(menu.el, btn)}, {clipPath:'inset(0px 0px 0px 0px round 16px)'}],
      {duration:240, easing:'cubic-bezier(.2,.7,.2,1)'});
    for (const n of [menu.tools]) n.animate([{opacity:0}, {opacity:1}], {duration:160, delay:100, easing:'ease-out', fill:'backwards'});
  }
  menu.done.focus({preventScroll:true});
}
// Folds the tools back into the Draw button. With keepCanvas, the drawing stays showing until it's replaced.
function closeSide(keepCanvas){
  if (!side.active) return;
  const {item, canvas, menu} = side, btn = item.querySelector('.side-draw-btn');
  const hadFocus = menu.el.contains(document.activeElement);
  side.active = false; side.current = null;
  // A linked entry closed without saving goes back to just as it was: its highlights, pen marks and layout.
  if (side.kind === 'entry' && !keepCanvas) queueMicrotask(refreshShelf);
  if (side.resize) { side.resize.disconnect(); side.resize = null; }
  if (keepCanvas) canvas.classList.add('done');
  else { canvas.remove(); item.classList.remove('inked'); }
  const folded = () => {
    menu.el.remove(); item.classList.remove('drawing');
    if (hadFocus && btn.isConnected) btn.focus({preventScroll:true});
  };
  if (calm() || !item.isConnected) { folded(); return; }
  menu.el.style.pointerEvents = 'none';
  for (const n of [menu.tools]) n.animate([{opacity:1}, {opacity:0}], {duration:90, fill:'forwards'});
  menu.el.animate([{clipPath:'inset(0px 0px 0px 0px round 16px)'}, {clipPath:buttonClip(menu.el, btn)}],
    {duration:200, easing:'cubic-bezier(.4,0,.6,1)', fill:'forwards'}).finished.then(folded, folded);
}
// Done: the drawing replaces the picture, in the entry and here on the right.
function finishSideDraw(){
  if (!side.active) return;
  if (side.kind === 'entry') { finishInk(); return; }
  const {id, base, item, canvas} = side, e = entries.get(id);
  // Nothing drawn, or the picture has gone from the entry meanwhile: nothing to save.
  if (!side.strokes.length || !e || !e.images.includes(base.name)) { closeSide(); return; }
  const out = renderDrawing(side, drawnBounds(side));
  closeSide(true);
  side.saving.add(base.name);
  (async () => {
    const blob = await drawnBlob(base, out);
    const img = item.querySelector(':scope > img');
    let url = null;
    if (blob && item.isConnected) {   // show the result straight away, while it's saved
      url = URL.createObjectURL(blob); img.src = url;
      try { await img.decode(); } catch (err) {}
    }
    canvas.remove(); item.classList.remove('inked');
    const saved = blob ? await saveDrawing(id, base, null, blob) : null;
    if (!blob && id === currentId) setStatus("Couldn't save the drawing.", true);
    if (!saved && item.isConnected) img.src = '/images/' + base.name;
    if (url) URL.revokeObjectURL(url);
    side.saving.delete(base.name);
  })();
}
// Done on a linked entry. Its ink is kept with this entry (its "inks:" line), for that linked entry:
// the highlights as words, and the pen marks as a see-through picture with the layout they were drawn on.
function finishInk(){
  const {id, key, base, canvas, cleared, strokes, vars} = side, e = entries.get(id), linked = inkKey(key);
  const W = side.inkW, H = parseFloat(canvas.style.height) || 0;
  if ((!strokes.length && !cleared && !side.marksChanged) || !e || !shelfNames(e).includes(key) || !W || !H) { closeSide(); return; }
  const old = inkRec(e, linked) || {}, repaint = strokes.length > 0 || cleared;
  let out = null;
  if (repaint && (strokes.some(s => !s.eraser) || (base && !cleared))) {
    const k = Math.min(Math.max(window.devicePixelRatio || 1, 1), 12000 / Math.max(W, H));
    out = document.createElement('canvas');
    out.width = Math.max(1, Math.round(W * k)); out.height = Math.max(1, Math.round(H * k));
    const o = out.getContext('2d'); o.setTransform(k, 0, 0, k, 0, 0);
    paintScene(o, side);   // left see-through: the entry's writing shows beneath it
  }
  const marks = side.marks.map(({s, e, q, c}) => ({s, e, q, c}));
  closeSide(true);
  side.saving.add(key);
  (async () => {
    let img = repaint ? null : old.img || null;
    try {
      if (out) {
        const blob = await new Promise(res => out.toBlob(res, 'image/png'));
        if (!blob) throw new Error('render');
        img = await store.uploadImage(blob);
        try { await loadImage('/images/' + img); } catch (err) {}   // ready to show straight away
      }
      const now = entries.get(id);
      if (now) {
        const rec = {};
        if (img) Object.assign(rec, {img, w:W, v:vars});
        if (marks.length) rec.hl = marks;
        now.inks = Object.assign({}, now.inks);
        if (rec.img || rec.hl) now.inks[linked] = rec; else delete now.inks[linked];
        markChanged(id);
        await flush(id);
      }
      if (old.img && old.img !== img) store.removeImage(old.img, true).catch(() => {});
    } catch (err) {
      if (id === currentId) setStatus("Couldn't save the ink on that entry. Check that the journal server is still running.", true);
    }
    side.saving.delete(key);
    if (id === currentId) refreshShelf();
  })();
}
function shelfInk(name){
  const ink = document.createElement('img'); ink.className = 'shelf-ink'; ink.alt = ''; ink.draggable = false;
  if (name) ink.src = '/images/' + name;
  return ink;
}
document.addEventListener('keydown', ev => {
  if (!side.active || document.querySelector('dialog[open]')) return;
  const t = ev.target;
  if (t && (t.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName))) return;   // writing in the entry
  if (ev.key === 'Escape') { ev.preventDefault(); finishSideDraw(); }
  else if ((ev.ctrlKey || ev.metaKey) && !ev.shiftKey && ev.key.toLowerCase() === 'z') { ev.preventDefault(); sideUndo(); }
});

/* ---------- Menu: settings ---------- */
let settings = {};
const SIZE_SETTINGS = [
  {key:'brandSize', label:'Journal name', cssVar:'--brand-size', min:14, max:60, def:26},
  {key:'titleSize', label:'Entry title', cssVar:'--title-size', min:18, max:80, def:43},
  {key:'bodySize', label:'Writing', cssVar:'--body-size', min:12, max:36, def:19},
  {key:'topicSize', label:'Topic under the title', cssVar:'--topic-size', min:10, max:48, def:16},
  {key:'listTopicSize', label:'Topic in the list', cssVar:'--list-topic-size', min:8, max:28, def:13},
  {key:'imgBorder', label:'Border thickness', cssVar:'--img-border', min:0, max:8, def:1, box:'imageRows'},
  {key:'zoomLevel', label:'Magnification', min:1.5, max:12, step:0.5, def:2, unit:'×', box:'zoomRows'},
  {key:'shelfHeight', label:'Height of each picture', cssVar:'--shelf-h', min:150, max:800, step:10, def:320, box:'zoomRows'},
  {key:'shelfScale', label:'Size of each picture', cssVar:'--shelf-scale', css:v => v / 100, min:25, max:100, step:5, def:100, unit:'%', box:'zoomRows',
   title:'Smaller pictures sit side by side: at 50% two fit in a row, at 25% four'},
  {key:'boldAmount', label:'Bold strength', cssVar:'--bold-amount', css:v => v, min:1, max:8, def:3, unit:'', box:'fmtRows',
   title:'1 is a little heavier than ordinary writing, 8 is very heavy'},
  {key:'underlineThick', label:'Underline thickness', cssVar:'--u-thick', min:1, max:8, step:0.5, def:1.5, box:'fmtRows'},
  {key:'subSize', label:'Numeral size', cssVar:'--sub-size', min:12, max:60, def:20, box:'subRows'},
  {key:'taskScale', label:'Task size in entries', cssVar:'--task-scale', css:v => v / 100, min:50, max:250, step:5, def:100, unit:'%', box:'taskRows',
   title:'The size of tasks as you write them in an entry (and in the Archive)'},
  {key:'exportBody', label:'Writing', min:6, max:16, step:0.5, def:10, unit:' pt', box:'exportRows',
   title:'The size of the entry\u2019s writing in the PDF'},
  {key:'exportMark', label:'Linked entry name in the writing', min:2, max:12, step:0.1, def:3.3, unit:' pt', box:'exportRows',
   title:'The linked entry\u2019s name, raised after the word where the link is'},
  {key:'exportNote', label:'Linked entries at the end', min:4, max:16, step:0.1, def:7.2, unit:' pt', box:'exportRows',
   title:'The size of the linked entries\u2019 writing at the end of the PDF'},
  {key:'exportNoteName', label:'Linked entry name at the end', min:4, max:24, step:0.1, def:9.4, unit:' pt', box:'exportRows',
   title:'The linked entry\u2019s name, in front of its writing at the end of the PDF'},
  {key:'exportPicture', label:'Picture height', min:15, max:90, def:33, unit:'% of a page', box:'exportRows',
   title:'How tall each picture is in the PDF (a very wide one is made narrower to fit the page, so it comes out a little shorter)'},
  {key:'turnSpeed', label:'Page turning speed', min:25, max:200, step:5, def:100, unit:'%', box:'readRows',
   title:'How fast pages and covers turn when you read a book: lower is slower, 100% as it was made'},
  {key:'taskMenuScale', label:'Task size in the Tasks menu', cssVar:'--task-menu-scale', css:v => v / 100, min:50, max:250, step:5, def:100, unit:'%', box:'taskRows',
   title:'The size of tasks as they appear in the Tasks menu'},
];
const COLOUR_SETTINGS = [
  {key:'caretColor', label:'Text cursor', cssVar:'--caret', from:'--accent'},
  {key:'newColor', label:'New entry button', cssVar:'--new-bg', from:'--ink'},
  {key:'titleColor', label:'Entry title', cssVar:'--title-color', from:'--ink'},
  {key:'imgBorderColor', label:'Border colour', cssVar:'--img-border-color', from:'--muted', box:'imageRows'},
  {key:'subColor', label:'Numeral colour', cssVar:'--sub-color', from:'--ink', box:'subRows'},
];
function readableOn(hex){
  const n = parseInt(hex.slice(1), 16), r = n >> 16 & 255, g = n >> 8 & 255, b = n & 255;
  return (0.299 * r + 0.587 * g + 0.114 * b) > 150 ? '#1E2723' : '#F8F9F5';
}
function toHex(colour){
  const c = document.createElement('canvas').getContext('2d');
  c.fillStyle = '#000'; c.fillStyle = colour.trim();
  return c.fillStyle.startsWith('#') ? c.fillStyle : '#000000';
}
function applySettings(){
  const root = document.documentElement.style;
  for (const s of SIZE_SETTINGS) {
    if (!s.cssVar) continue;
    if (settings[s.key] !== undefined) root.setProperty(s.cssVar, s.css ? s.css(settings[s.key]) : settings[s.key] + 'px');
    else root.removeProperty(s.cssVar);
  }
  for (const s of COLOUR_SETTINGS) {
    if (settings[s.key]) root.setProperty(s.cssVar, settings[s.key]);
    else root.removeProperty(s.cssVar);
  }
  if (settings.newColor) root.setProperty('--new-fg', readableOn(settings.newColor));
  else root.removeProperty('--new-fg');
  showFreezeCombo();
  renderListView(); renderList();
}
let settingsTimer;
function saveSettings(){
  clearTimeout(settingsTimer);
  settingsTimer = setTimeout(async () => {
    try {
      const r = await fetch('/api/settings', {method:'PUT', headers:H, body:JSON.stringify(settings)});
      if (!r.ok) throw new Error();
      $('settingsStatus').textContent = 'Saved';
      $('settingsStatus').classList.remove('err');
    } catch (e) {
      $('settingsStatus').textContent = "Couldn't save settings";
      $('settingsStatus').classList.add('err');
    }
  }, 400);
}
function changeSetting(key, value){
  if (value === undefined) delete settings[key]; else settings[key] = value;
  applySettings(); syncSettingsForm(); saveSettings();
  if (key === 'shelfScale' || key === 'shelfHeight') layoutShelf();
  if (key === 'logKey' || key === 'shotKey') { showLogShortcuts(); setTimeout(loadLog, 1200); }   // on Windows, whether the new keys could be taken
}
function buildSettingsForm(){
  const sizeRows = $('sizeRows'), colourRows = $('colourRows');
  for (const s of SIZE_SETTINGS) {
    const row = document.createElement('div'); row.className = 'set-row';
    const id = 'set-' + s.key;
    row.innerHTML = '<label for="' + id + '"></label><input type="range" id="' + id + '" min="' + s.min + '" max="' + s.max + '" step="' + (s.step || 1) + '"><output for="' + id + '"></output><button class="set-reset" type="button">Reset</button>';
    row.querySelector('label').textContent = s.label;
    if (s.title) row.title = s.title;
    row.querySelector('input').addEventListener('input', ev => changeSetting(s.key, +ev.target.value));
    row.querySelector('.set-reset').addEventListener('click', () => changeSetting(s.key, undefined));
    (s.box ? $(s.box) : sizeRows).append(row);
  }
  for (const s of COLOUR_SETTINGS) {
    const row = document.createElement('div'); row.className = 'set-row';
    const id = 'set-' + s.key;
    row.innerHTML = '<label for="' + id + '"></label><input type="color" id="' + id + '"><output></output><button class="set-reset" type="button">Reset</button>';
    row.querySelector('label').textContent = s.label;
    row.querySelector('input').addEventListener('input', ev => changeSetting(s.key, ev.target.value));
    row.querySelector('.set-reset').addEventListener('click', () => changeSetting(s.key, undefined));
    (s.box ? $(s.box) : colourRows).append(row);
  }
  for (const k of KEY_SETTINGS) buildKeyRow(k);
}
const KEY_SETTINGS = [
  {key:'freezeKey', label:'Freeze shortcut', def:'Shift+Z', box:'zoomRows'},
  {key:'indentKey', label:'Indent shortcut', def:'Tab', box:'subRows',
   title:'Lines up the line with the words beside the sub-entry numeral. With Shift, takes the indent away'},
  {key:'logKey', label:'Log an activity', def:'Ctrl+Shift+L', box:'logRows', title:'Opens the form for logging what you\u2019re doing'},
  {key:'shotKey', label:'Add a screenshot', def:'Ctrl+Alt+S', box:'logRows', title:'Adds a screenshot to the activity you started last'},
];
function buildKeyRow(k){
  const row = document.createElement('div'); row.className = 'set-row';
  row.innerHTML = '<label for="set-' + k.key + '">' + k.label + '</label><button class="set-key" id="set-' + k.key + '" type="button"></button>'
    + '<output></output><button class="set-reset" type="button">Reset</button>';
  const btn = row.querySelector('.set-key');
  btn.title = (k.title ? k.title + '. ' : '') + 'Click, then press the key or keys to use';
  btn.addEventListener('click', () => listenForKeys(btn, k));
  row.querySelector('.set-reset').addEventListener('click', () => changeSetting(k.key, undefined));
  $(k.box).append(row);
}
// Waits for the next key press (with any Ctrl / Alt / Shift / Meta held) and uses it as the shortcut.
let keyListener = null;
function listenForKeys(btn, k){
  if (keyListener) return;
  btn.textContent = 'Press the keys…'; btn.classList.add('listening');
  const stop = () => { window.removeEventListener('keydown', keyListener, true); keyListener = null; btn.classList.remove('listening'); };
  keyListener = ev => {
    ev.preventDefault(); ev.stopPropagation();
    if (['Shift', 'Control', 'Alt', 'Meta', 'AltGraph', 'CapsLock'].includes(ev.key)) return;   // wait for the main key
    stop();
    if (ev.key === 'Escape') { syncSettingsForm(); return; }
    const combo = comboOf(ev);
    if (!combo) { btn.textContent = "That key can't be used"; setTimeout(syncSettingsForm, 1500); return; }
    changeSetting(k.key, combo === k.def ? undefined : combo);
  };
  window.addEventListener('keydown', keyListener, true);
  btn.addEventListener('blur', () => { if (keyListener) { stop(); syncSettingsForm(); } }, {once:true});
}
function syncSettingsForm(){
  for (const k of KEY_SETTINGS) {
    const kb = $('set-' + k.key);
    if (!kb || keyListener) continue;
    kb.textContent = settings[k.key] || k.def;
    kb.parentElement.querySelector('.set-reset').disabled = !settings[k.key];
  }
  for (const s of SIZE_SETTINGS) {
    const input = $('set-' + s.key), row = input.parentElement;
    const v = settings[s.key] !== undefined ? settings[s.key] : s.def;
    input.value = v;
    row.querySelector('output').textContent = v + (s.unit !== undefined ? s.unit : ' px');
    row.querySelector('.set-reset').disabled = settings[s.key] === undefined;
  }
  for (const s of COLOUR_SETTINGS) {
    const input = $('set-' + s.key), row = input.parentElement;
    input.value = settings[s.key] || toHex(cssVar(s.from));
    row.querySelector('.set-reset').disabled = !settings[s.key];
  }
}
async function loadSettings(){
  try {
    const r = await fetch('/api/settings', {headers:{'X-Journal':'1'}, cache:'no-store'});
    if (r.ok) settings = await r.json();
  } catch (e) { settings = {}; }
  applySettings();
}
buildSettingsForm();
$('menuBtn').addEventListener('click', () => { syncSettingsForm(); $('settingsStatus').textContent = ''; $('settings').showModal(); });
$('settingsClose').addEventListener('click', () => $('settings').close());
$('settings').addEventListener('click', ev => { if (ev.target === $('settings')) $('settings').close(); });
$('resetAll').addEventListener('click', () => {
  // The way the list of entries is shown isn't one of the Menu's settings, so it stays as it is.
  settings = {listSort:settings.listSort, listTopics:settings.listTopics, tasksSort:settings.tasksSort}; applySettings(); syncSettingsForm(); saveSettings(); });

/* ---------- Quotes ----------
   Writing saved from web pages with the browser extension ("Add to quote archive") is kept in journal/quotes,
   one text file per quote. The Quotes menu shows them; drag one into the open entry to put it there. Like a
   picture from the Archive, the menu steps aside while you drag, and comes back if you let go elsewhere. */
function quotesNote(text){ const p = document.createElement('p'); p.className = 'arch-note'; p.textContent = text; return p; }
async function openQuotes(){
  const note = quotesNote('Opening quotes…');
  $('quotesPanel').replaceChildren(note);
  $('quotesDialog').showModal();
  document.body.classList.toggle('can-bring-back', canBringBack());
  try {
    const r = await fetch('/api/quotes', {headers:{'X-Journal':'1'}, cache:'no-store'});
    if (!r.ok) throw new Error();
    renderQuotes(await r.json());
  } catch (e) {
    note.textContent = "Couldn't open the quotes. Check that the journal server is still running.";
  }
}
function renderQuotes(list){
  const panel = $('quotesPanel');
  if (!list.length) {
    panel.replaceChildren(quotesNote('No quotes yet. Select some writing on a web page, right-click it and choose Add to quote archive.'));
    return;
  }
  const ul = document.createElement('ul'); ul.className = 'quote-list';
  for (const q of list) {
    const li = document.createElement('li'); li.className = 'quote-card';
    const bar = document.createElement('div'); bar.className = 'quote-card-bar';
    const tag = document.createElement('span'); tag.className = 'zoom-tag';
    tag.textContent = q.saved ? fmtStamp.format(new Date(q.saved)) : q.name;
    tag.title = q.name;
    bar.append(tag);
    if (q.source) bar.append(quoteSource(q.source));
    const space = document.createElement('span'); space.className = 'zoom-space';
    const del = document.createElement('button'); del.type = 'button'; del.className = 'tool quote-card-del'; del.textContent = 'Delete';
    del.title = 'Delete this quote from the Quotes (entries that have it keep it)';
    del.addEventListener('click', () => deleteQuote(q.name, del, li));
    bar.append(space, del);
    const words = document.createElement('div'); words.className = 'quote-card-text'; words.textContent = q.text;
    li.append(bar, words);
    li.addEventListener('pointerdown', ev => startQuoteDrag(ev, q.text));
    ul.append(li);
  }
  panel.replaceChildren(quotesNote(canBringBack() ? 'Drag a quote into the entry to add it.' : 'Open an entry to drag quotes into it.'), ul);
}
// "Source" beside the date: pointing at it (or tabbing to it) shows the page's title and address.
function quoteSource(src){
  const wrap = document.createElement('span'); wrap.className = 'quote-src';
  const tag = document.createElement('span'); tag.className = 'zoom-tag'; tag.textContent = 'Source'; tag.tabIndex = 0;
  tag.setAttribute('aria-label', 'Source: ' + (src.title || src.url));
  const pop = document.createElement('span'); pop.className = 'quote-src-pop';
  const box = document.createElement('span'); box.className = 'quote-src-box';
  if (src.title) { const t = document.createElement('span'); t.className = 'quote-src-title'; t.textContent = src.title; box.append(t); }
  if (src.url) {
    const a = document.createElement('a'); a.className = 'quote-src-url'; a.href = src.url; a.target = '_blank'; a.rel = 'noopener noreferrer';
    a.textContent = src.url; a.title = src.url;
    box.append(a);
  }
  pop.append(box); wrap.append(tag, pop);
  return wrap;
}
async function deleteQuote(name, btn, li){
  if (!armed(btn, 'Delete', 'Delete for good?')) return;
  btn.disabled = true; btn.textContent = 'Deleting…';
  try {
    const r = await fetch('/api/quotes/' + encodeURIComponent(name), {method:'DELETE', headers:H});
    if (!r.ok && r.status !== 404) throw new Error();
    const ul = li.parentElement; li.remove();
    if (ul && !ul.children.length) renderQuotes([]);
  } catch (e) {
    btn.disabled = false; btn.textContent = "Couldn't delete. Try again";
  }
}
// The + in the Quotes menu: type or paste a quote, with where it's from if you like.
function showQuoteForm(show){
  $('quoteForm').hidden = !show;
  $('quoteAddBtn').setAttribute('aria-expanded', String(show));
  $('quoteFormNote').textContent = ''; $('quoteFormNote').classList.remove('err');
  if (show) $('quoteText').focus();
  else { $('quoteText').value = ''; $('quoteSource').value = ''; }
}
async function addQuote(){
  const text = $('quoteText').value.replace(/\r\n?/g, '\n').replace(/^\n+|\s+$/g, '');
  const note = $('quoteFormNote');
  if (!text) { note.textContent = 'Write or paste the quote first.'; note.classList.add('err'); $('quoteText').focus(); return; }
  let url = $('quoteSource').value.trim();
  if (url && !/^https?:\/\//i.test(url)) url = 'https://' + url;
  const btn = $('quoteSave'); btn.disabled = true;
  note.classList.remove('err'); note.textContent = 'Adding…';
  try {
    const body = {text};
    if (url) body.source = {url, title:''};
    const r = await fetch('/api/quotes', {method:'POST', headers:H, body:JSON.stringify(body)});
    if (!r.ok) throw new Error();
    showQuoteForm(false);
    const l = await fetch('/api/quotes', {headers:{'X-Journal':'1'}, cache:'no-store'});
    if (l.ok) renderQuotes(await l.json());
  } catch (e) {
    note.textContent = "Couldn't add the quote. Check that the journal server is still running."; note.classList.add('err');
  } finally { btn.disabled = false; }
}
$('quoteAddBtn').addEventListener('click', () => showQuoteForm($('quoteForm').hidden));
$('quoteCancel').addEventListener('click', () => showQuoteForm(false));
$('quoteSave').addEventListener('click', addQuote);
$('quoteText').addEventListener('keydown', ev => { if (ev.key === 'Enter' && (ev.ctrlKey || ev.metaKey)) { ev.preventDefault(); addQuote(); } });
$('quotesDialog').addEventListener('close', () => { if (!quoteDrag) showQuoteForm(false); });
let quoteDrag = null;
function startQuoteDrag(ev, text){
  if (ev.button !== 0 || !canBringBack() || quoteDrag) return;
  const t = ev.target;
  if (t.closest && t.closest('button, a, .quote-src')) return;   // Delete, Source and its link work as usual
  if (t.classList && t.classList.contains('quote-card-text') && ev.offsetX > t.clientWidth) return;   // on its scrollbar
  ev.preventDefault();
  quoteDrag = {text, x0:ev.clientX, y0:ev.clientY, x:ev.clientX, y:ev.clientY, started:false, target:null, ghost:null, raf:0};
  window.addEventListener('pointermove', moveQuoteDrag);
  window.addEventListener('pointerup', endQuoteDrag);
  window.addEventListener('pointercancel', cancelQuoteDrag);
}
function moveQuoteDrag(ev){
  const d = quoteDrag; if (!d) return;
  d.x = ev.clientX; d.y = ev.clientY;
  if (!d.started) {
    if (Math.hypot(d.x - d.x0, d.y - d.y0) < 4) return;
    d.started = true;
    $('quotesDialog').close();   // step aside
    document.body.classList.add('moving');
    const g = makeQuote(d.text, true); g.classList.add('quote-ghost'); g.setAttribute('aria-hidden', 'true');
    document.body.append(g); d.ghost = g;
    d.raf = requestAnimationFrame(quoteDragFrame);
  }
  d.ghost.style.left = d.x + 'px'; d.ghost.style.top = d.y + 'px';
}
// Where a quote goes: it takes a line of its own. Let go at the start of a line, it goes above that line;
// anywhere else in a line, it goes below it. On a task list, it goes below the list.
function quoteTarget(t){
  if (!t) return null;
  if (t.task) { const list = t.task.closest('.tasks'); return {parent:list.parentNode, ref:list.nextSibling}; }
  if (t.text) {
    const prev = t.text.previousSibling;
    const atStart = t.offset === 0 ? !prev || (prev.nodeType === 1 && prev.matches('.tasks, .quote')) : t.text.data[t.offset - 1] === '\n';
    return atStart ? {text:t.text, offset:t.offset} : lineEndAt(t.text, t.offset);
  }
  return t;
}
function quoteDragFrame(){
  const d = quoteDrag; if (!d || !d.started) return;
  const mr = els.scroll.getBoundingClientRect(), edge = 60;
  if (d.y < mr.top + edge) els.scroll.scrollTop -= Math.ceil((mr.top + edge - d.y) / 4);
  else if (d.y > mr.bottom - edge) els.scroll.scrollTop += Math.ceil((d.y - (mr.bottom - edge)) / 4);
  const br = els.body.getBoundingClientRect();
  if (d.x < br.left - 40 || d.x > br.right + 40 || d.y < mr.top || d.y > mr.bottom) { d.target = null; showMark(null); }   // not over the entry
  else {
    d.ghost.style.visibility = 'hidden';
    d.target = quoteTarget(dropTarget(d.x, d.y));
    d.ghost.style.visibility = '';
    showMark(d.target);
  }
  d.raf = requestAnimationFrame(quoteDragFrame);
}
function finishQuoteDrag(){
  const d = quoteDrag; quoteDrag = null;
  cancelAnimationFrame(d.raf);
  window.removeEventListener('pointermove', moveQuoteDrag);
  window.removeEventListener('pointerup', endQuoteDrag);
  window.removeEventListener('pointercancel', cancelQuoteDrag);
  document.body.classList.remove('moving');
  if (d.ghost) d.ghost.remove();
  showMark(null);
  return d;
}
function endQuoteDrag(){
  if (!quoteDrag) return;
  const d = finishQuoteDrag();
  if (!d.started) return;
  const t = d.target, inBody = n => n && els.body.contains(n);
  if (!t || !canBringBack() || !(t.text ? inBody(t.text) : inBody(t.parent))) { $('quotesDialog').showModal(); return; }   // let go elsewhere
  placeQuote(makeQuote(d.text), t);
  onBodyChange();
}
// A quote in the entry can be dragged to another place in the entry to move it there, or into the space on
// the right to show it there too (it stays in the entry).
let bodyQuoteDrag = null;
function startBodyQuoteDrag(ev, q){
  if (ev.button !== 0 || ev.pointerType === 'touch' || bodyQuoteDrag || !currentId || !els.body.contains(q)) return;
  if (ev.target.closest && ev.target.closest('button')) return;   // Expand / Collapse and Remove work as usual
  ev.preventDefault();
  bodyQuoteDrag = {q, text:q.querySelector('.quote-text').textContent, x0:ev.clientX, y0:ev.clientY, x:ev.clientX, y:ev.clientY,
                   started:false, ghost:null, box:null, target:null, raf:0};
  window.addEventListener('pointermove', moveBodyQuoteDrag);
  window.addEventListener('pointerup', endBodyQuoteDrag);
  window.addEventListener('pointercancel', endBodyQuoteDrag);
}
function moveBodyQuoteDrag(ev){
  const d = bodyQuoteDrag; if (!d) return;
  d.x = ev.clientX; d.y = ev.clientY;
  if (!d.started) {
    if (Math.hypot(d.x - d.x0, d.y - d.y0) < 4) return;
    d.started = true;
    document.body.classList.add('moving');
    d.q.classList.add('dragging');
    const g = makeQuote(d.text, true); g.classList.add('quote-ghost'); g.setAttribute('aria-hidden', 'true');
    document.body.append(g); d.ghost = g;
    d.raf = requestAnimationFrame(bodyQuoteDragFrame);
  }
  d.ghost.style.left = d.x + 'px'; d.ghost.style.top = d.y + 'px';
}
// Each frame: over the space on the right, it'll be shown there; over the entry, the mark shows where it'll
// move to (scrolling the entry when near its top or bottom edge).
function bodyQuoteDragFrame(){
  const d = bodyQuoteDrag; if (!d || !d.started) return;
  d.box = sideDrop(d.x, d.y);
  showSideDrop(d.box);
  d.target = null;
  if (!d.box) {
    const mr = els.scroll.getBoundingClientRect(), edge = 60;
    if (d.y < mr.top + edge) els.scroll.scrollTop -= Math.ceil((mr.top + edge - d.y) / 4);
    else if (d.y > mr.bottom - edge) els.scroll.scrollTop += Math.ceil((d.y - (mr.bottom - edge)) / 4);
    const br = els.body.getBoundingClientRect();
    if (d.x >= br.left - 40 && d.x <= br.right + 40 && d.y >= mr.top && d.y <= mr.bottom) {
      d.ghost.style.visibility = 'hidden';
      const t = quoteTarget(dropTarget(d.x, d.y));
      d.ghost.style.visibility = '';
      if (t && !quoteStaysPut(d.q, t)) d.target = t;
    }
  }
  showMark(d.target);
  d.raf = requestAnimationFrame(bodyQuoteDragFrame);
}
function endBodyQuoteDrag(ev){
  const d = bodyQuoteDrag; if (!d) return;
  bodyQuoteDrag = null;
  cancelAnimationFrame(d.raf);
  window.removeEventListener('pointermove', moveBodyQuoteDrag);
  window.removeEventListener('pointerup', endBodyQuoteDrag);
  window.removeEventListener('pointercancel', endBodyQuoteDrag);
  document.body.classList.remove('moving');
  d.q.classList.remove('dragging');
  if (d.ghost) d.ghost.remove();
  showSideDrop(null); showMark(null);
  if (!d.started || ev.type !== 'pointerup' || !d.q.isConnected) return;
  if (d.box) addToShelf('quote:' + quoteCode(d.text));
  else if (d.target && moveQuote(d.q, d.target)) onBodyChange();
}
// Whether letting go here would leave the quote just where it is (right before or after itself).
function quoteStaysPut(q, t){
  const blank = n => n && n.nodeType === 3 && !n.data;
  if (t.text) {
    if (!els.body.contains(t.text)) return true;
    let n = t.text;
    if (t.offset >= t.text.data.length) { n = n.nextSibling; while (blank(n)) n = n.nextSibling; if (n === q) return true; }
    n = t.text;
    if (t.offset === 0) { n = n.previousSibling; while (blank(n)) n = n.previousSibling; if (n === q) return true; }
    return false;
  }
  return !t.parent || !els.body.contains(t.parent) || q.contains(t.parent) || t.ref === q || (t.ref === q.nextSibling && t.parent === q.parentNode);
}
// Moves a quote already in the entry to a new place in it. The place is marked first, as taking the quote out
// joins the writing either side of it back up with a line break.
function moveQuote(q, t){
  const mark = document.createComment('');
  if (t.text) {
    const after = t.text.splitText(Math.min(t.offset, t.text.data.length));
    after.parentNode.insertBefore(mark, after);
  } else {
    const parent = t.parent && els.body.contains(t.parent) && !t.parent.closest('.fig, .tasks, .quote, .sub, .indent, .written-day') ? t.parent : els.body;
    parent.insertBefore(mark, t.ref && t.ref.parentNode === parent ? t.ref : null);
  }
  const blank = n => n && n.nodeType === 3 && !n.data;
  let a = mark.previousSibling; while (blank(a)) a = a.previousSibling;
  let b = mark.nextSibling; while (blank(b)) b = b.nextSibling;
  if (a === q || b === q) { mark.remove(); els.body.normalize(); return false; }   // it would end up where it was
  // Take it out, putting back the line break it stood in for (as Remove does).
  const prev = q.previousSibling, next = q.nextSibling;
  q.remove();
  if (prev && next && prev.nodeType === 3 && next.nodeType === 3 && !prev.data.endsWith('\n') && !next.data.startsWith('\n')) prev.data += '\n';
  mark.replaceWith(q);
  takeLineBreak(q);
  els.body.normalize();
  return true;
}
function cancelQuoteDrag(){ if (quoteDrag && finishQuoteDrag().started) $('quotesDialog').showModal(); }
function placeQuote(block, t){
  if (t.text) {
    const after = t.text.splitText(Math.min(t.offset, t.text.data.length));
    after.parentNode.insertBefore(block, after);
  } else {
    const parent = t.parent && els.body.contains(t.parent) && !t.parent.closest('.fig, .tasks, .quote, .sub, .indent, .written-day') ? t.parent : els.body;
    parent.insertBefore(block, t.ref && t.ref.parentNode === parent ? t.ref : null);
  }
  takeLineBreak(block);
  els.body.normalize();
}
// A quote stands in for the line break next to it, as a task list does.
function takeLineBreak(block){
  const blank = x => x && x.nodeType === 3 && !x.data;
  let p = block.previousSibling, n = block.nextSibling;
  while (blank(p)) p = p.previousSibling;
  while (blank(n)) n = n.nextSibling;
  if (n && n.nodeType === 3 && n.data.startsWith('\n')) n.data = n.data.slice(1);
  else if (p && p.nodeType === 3 && p.data.endsWith('\n')) p.data = p.data.slice(0, -1);
}

/* ---------- Archive ---------- */
// Shows a picture full-size with only a Close button (used for archived pictures).
function viewOnly(src, title){
  viewingFig = null;
  els.viewer.classList.add('readonly');
  els.viewerImg.src = src;
  showViewerTitle(title || '', true);
  els.viewer.showModal();
}
const archiveSrc = name => '/archive/images/' + name;
// Everything in an entry, for reading only: in the Archive (where pictures are in the archive's folder),
// and in the preview of a linked entry (formatted, with pictures from the journal).
function readOnlyBody(body, src = archiveSrc, formatted = false){
  const box = document.createElement('div'); box.className = 'arch-body';
  for (const p of parseBody(body)) {
    if (p.type === 'text') { box.append(formatted ? formattedText(p.text) : document.createTextNode(p.text)); continue; }
    if (p.type === 'link') { box.append(staticLink(p.id, p.title)); continue; }
    if (p.type === 'pdf') { box.append(staticPdf(p.name, p.title)); continue; }
    if (p.type === 'sub') { box.append(makeSub(p.level)); continue; }
    if (p.type === 'indent') { box.append(makeIndent()); continue; }
    if (p.type === 'quote') { box.append(makeQuote(p.text, true)); continue; }
    if (p.type === 'day') { box.append(makeWrittenDay(p.day)); continue; }
    if (p.type === 'tasks') {
      const block = document.createElement('div'); block.className = 'tasks readonly';
      const ol = document.createElement('ol');
      for (const it of p.items) ol.append(staticTask(it, src));
      block.append(ol); box.append(block); continue;
    }
    const fig = document.createElement('button'); fig.type = 'button'; fig.className = 'fig';
    fig.style.cssText = 'border:0;padding:0;background:none;font:inherit';
    const img = document.createElement('img'); img.src = src(p.name); img.alt = p.title || 'Picture';
    if (p.title) fig.title = p.title;
    fig.append(img);
    fig.addEventListener('click', ev => { ev.stopPropagation(); viewOnly(src(p.name), p.title); });
    if (src === archiveSrc) { img.draggable = false; fig.addEventListener('pointerdown', ev => startArchiveDrag(ev, p.name, p.title, null)); }
    box.append(fig);
  }
  numberSubs(box);
  return box;
}
function archiveEntryItem(id, e){
  const li = document.createElement('li');
  const item = document.createElement('div'); item.className = 'arch-item';
  const row = document.createElement('div'); row.className = 'trow';
  const t = document.createElement('button'); t.type = 'button';
  t.className = 't' + (e.title.trim() ? '' : ' untitled');
  t.textContent = e.title.trim() || 'Untitled';
  t.setAttribute('aria-expanded', 'false');
  row.append(t);
  const imgs = imagesIn(e.body);
  if (imgs.length) {
    const minis = document.createElement('span'); minis.className = 'minis';
    for (const name of imgs.slice(0, 3)) {
      const img = document.createElement('img'); img.src = archiveSrc(name); img.alt = ''; img.loading = 'lazy';
      minis.append(img);
    }
    const extra = imgs.length - 3;
    if (extra > 0) { const more = document.createElement('span'); more.className = 'more'; more.textContent = '+' + extra + (extra === 1 ? ' image' : ' images'); minis.append(more); }
    row.append(minis);
  }
  const add = document.createElement('button'); add.type = 'button'; add.className = 'add-back'; add.textContent = 'Add to journal';
  add.addEventListener('click', () => addBack(id, add, li));
  const erase = document.createElement('button'); erase.type = 'button'; erase.className = 'erase-entry'; erase.textContent = 'Delete forever';
  erase.addEventListener('click', () => eraseArchivedEntry(id, erase, li));
  row.append(add, erase);
  const d = document.createElement('span'); d.className = 'd';
  d.textContent = 'Archived ' + fmtDate.format(new Date(e.archived)) + ', last changed ' + when(e.updated);
  item.append(row, d);
  const sn = snippet(e);
  if (sn) { const s = document.createElement('span'); s.className = 's'; s.textContent = sn; item.append(s); s.addEventListener('click', toggle); }
  item.append(readOnlyBody(e.body));
  function toggle(){ const open = item.classList.toggle('open'); t.setAttribute('aria-expanded', String(open)); }
  t.addEventListener('click', toggle);
  li.append(item);
  return li;
}
function renderArchive(data){
  const ep = $('archEntries'), ip = $('archImages');
  const list = Object.entries(data.entries).sort((a, b) => b[1].archived - a[1].archived);
  if (!list.length) {
    const p = document.createElement('p'); p.className = 'arch-note'; p.textContent = 'No archived entries. Entries you archive will appear here.';
    ep.replaceChildren(p);
  } else {
    const ul = document.createElement('ul'); ul.className = 'arch-list';
    for (const [id, e] of list) ul.append(archiveEntryItem(id, e));
    ep.replaceChildren(ul);
  }
  archData = {images:data.images || [], folders:data.folders || []};
  archModels = {models:data.models || [], folders:data.modelFolders || []};
  renderArchImages(); renderArchModels();
  archTasks = Array.isArray(data.tasks) ? data.tasks : [];
  renderArchTasks();
}
/* ---------- Archived tasks ----------
   Finished tasks archived from the Tasks menu, by the day they were archived (the latest day first), and
   within each day under the entry each came from.
   They can't be marked or changed here. An archived task also stays in its entry; De-archive takes away its
   archived note there, and so puts it back in the Tasks menu. (Tasks archived before they stayed in their
   entries are put back in their old list if it's still there, otherwise in a new list at the end of the entry.)
   Delete forever takes one out of the Archive only: it stays in its entry, still out of the Tasks menu. */
let archTasks = [];
function renderArchTasks(){
  const panel = $('archTasks');
  if (!archTasks.length) {
    const p = document.createElement('p'); p.className = 'arch-note';
    p.textContent = 'No archived tasks. Finished tasks you archive from the Tasks menu will appear here.';
    return panel.replaceChildren(p);
  }
  // By the day each was archived, the latest day first; within a day, under the entry each came from.
  const days = new Map();
  for (const t of archTasks.slice().sort((a, b) => (b.archived || '').localeCompare(a.archived || ''))) {
    const day = stampDate(t.archived) ? t.archived.slice(0, 10) : '';
    if (!days.has(day)) days.set(day, new Map());
    const groups = days.get(day);
    if (!groups.has(t.entry)) groups.set(t.entry, []);
    groups.get(t.entry).push(t);
  }
  const fmtDay = new Intl.DateTimeFormat(undefined, {weekday:'long', day:'numeric', month:'long', year:'numeric'});
  const frag = document.createDocumentFragment();
  for (const [day, groups] of days) {
    const box = document.createElement('section'); box.className = 'arch-task-day';
    const dh = document.createElement('h3'); dh.className = 'arch-task-day-head';
    dh.textContent = day ? fmtDay.format(stampDate(day + 'T00:00')) : 'Day not known';
    box.append(dh);
    for (const [id, list] of groups) {
      const e = entries.get(id);
      const g = document.createElement('section'); g.className = 'tl-group';
      const head = document.createElement('button'); head.type = 'button';
      const title = (e ? e.title : list[0].entryTitle || '').trim();
      head.className = 'tl-entry' + (title ? '' : ' untitled') + (e ? '' : ' gone');
      head.textContent = (title || 'Untitled') + (e ? '' : ' (not in the journal now)');
      if (e) { head.title = 'Open this entry'; head.addEventListener('click', () => { $('archive').close(); open(id); }); }
      else { head.disabled = true; head.title = 'This entry has been archived or deleted'; }
      const div = document.createElement('div'); div.className = 'tasks readonly flat';
      const ol = document.createElement('ol');
      for (const t of list) {
        const li = staticTask(t.item);
        const when = document.createElement('span'); when.className = 'task-archived';
        const d = stampDate(t.archived); when.textContent = d ? 'Archived at ' + fmtTime.format(d) : 'Archived';   // the day is the heading above
        li.querySelector('.task-meta').append(when);
        const back = document.createElement('button'); back.type = 'button'; back.className = 'task-arch-btn'; back.textContent = 'De-archive';
        back.title = e ? 'Put this task back in its entry, and so in the Tasks menu' : 'Its entry isn\u2019t in the journal now';
        back.disabled = !e;
        back.addEventListener('click', () => dearchiveTask(t, back));
        const erase = document.createElement('button'); erase.type = 'button'; erase.className = 'task-arch-btn erase-task'; erase.textContent = 'Delete forever';
        erase.title = 'Take it out of the Archive for good. It stays in its entry, but not in the Tasks menu';
        erase.addEventListener('click', () => eraseArchivedTask(t, erase));
        li.insertBefore(back, li.querySelector('.task-box'));
        li.insertBefore(erase, li.querySelector('.task-box'));
        ol.append(li);
      }
      div.append(ol); g.append(head, div); box.append(g);
    }
    frag.append(box);
  }
  panel.replaceChildren(frag);
}
async function dearchiveTask(t, btn){
  if (!entries.has(t.entry)) return;
  btn.disabled = true; btn.textContent = 'Putting back\u2026';
  try {
    const r = await fetch('/api/archive/tasks/' + t.id, {method:'DELETE', headers:H});
    if (!r.ok) throw new Error();
    const ok = changeEntryBody(t.entry, parts => { if (!unmarkTaskArchivedInParts(parts, taskKey(t.item))) insertTaskInParts(parts, t); });
    archTasks = archTasks.filter(x => x.id !== t.id);
    renderArchTasks();
    if (!ok) throw new Error('lost');
  } catch (e) {
    btn.disabled = false; btn.textContent = e.message === 'lost' ? 'Its entry is gone' : "Couldn't. Try again";
  }
}
async function eraseArchivedTask(t, btn){
  if (!armed(btn, 'Delete forever', "Delete forever? Can't be undone")) return;
  btn.disabled = true;
  try {
    const r = await fetch('/api/archive/tasks/' + t.id, {method:'DELETE', headers:H});
    if (!r.ok && r.status !== 404) throw new Error();
    archTasks = archTasks.filter(x => x.id !== t.id);
    renderArchTasks();
  } catch (e) {
    btn.disabled = false; btn.textContent = "Couldn't delete. Try again";
  }
}
/* ---------- Folders in the archive's Images ----------
   Folders are real folders inside journal/archive/images, named by you. The + beside Close makes one in the
   folder you're looking at. Drag a picture or folder onto a folder to put it there, or onto a name in the
   path at the top to move it back up. Pictures saved from the web always arrive loose, at the top. */
let archData = {images:[], folders:[]}, archFolder = '';
// The Models tab has folders of its own, in journal/archive/models, which work just the same way.
let archModels = {models:[], folders:[]}, archModelFolder = '', archKind = 'images';
// The folders being worked on: those of the Images tab, or of the Models tab when it's open.
function archK(kind = archKind){
  return kind === 'models'
    ? {kind, panel:$('archModels'), items:archModels.models, folders:archModels.folders, root:'Models', one:'model', many:'models',
       get folder(){ return archModelFolder; }, set folder(v){ archModelFolder = v; }, render:renderArchModels}
    : {kind, panel:$('archImages'), items:archData.images, folders:archData.folders, root:'Images', one:'picture', many:'pictures',
       get folder(){ return archFolder; }, set folder(v){ archFolder = v; }, render:renderArchImages};
}
// The path at the top: Images › Birds › Owls. Each name opens that folder, and takes things dropped on it.
function archCrumbs(K){
  const crumbs = document.createElement('nav'); crumbs.className = 'arch-crumbs'; crumbs.setAttribute('aria-label', 'Folder');
  const trail = [''].concat(K.folder ? K.folder.split('/').map((_, i, a) => a.slice(0, i + 1).join('/')) : []);
  trail.forEach((path, i) => {
    if (i) { const sep = document.createElement('span'); sep.className = 'sep'; sep.textContent = '\u203a'; sep.setAttribute('aria-hidden', 'true'); crumbs.append(sep); }
    const b = document.createElement('button'); b.type = 'button'; b.className = 'arch-crumb'; b.dataset.folder = path;
    b.textContent = path ? baseName(path) : K.root; b.title = b.textContent;
    if (i === trail.length - 1) b.setAttribute('aria-current', 'page');
    else b.addEventListener('click', () => openArchFolder(path));
    crumbs.append(b);
  });
  return crumbs;
}
const FOLDER_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6.5A1.5 1.5 0 0 1 4.5 5h4.6l2 2.2h8.4A1.5 1.5 0 0 1 21 8.7v9.8a1.5 1.5 0 0 1-1.5 1.5h-15A1.5 1.5 0 0 1 3 18.5z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>';
const parentOf = path => path.includes('/') ? path.slice(0, path.lastIndexOf('/')) : '';
const baseName = path => path.slice(path.lastIndexOf('/') + 1);
const inFolder = (folder, path) => folder === path || folder.startsWith(path + '/');
function archImagesNote(text){
  const p = document.createElement('p'); p.className = 'arch-note'; p.textContent = text; return p;
}
function renderArchImages(){
  const ip = $('archImages');
  if (archFolder && !archData.folders.some(f => f.path === archFolder)) archFolder = '';
  const crumbs = archCrumbs(archK('images'));
  const folders = archData.folders.filter(f => parentOf(f.path) === archFolder)
    .sort((a, b) => baseName(a.path).localeCompare(baseName(b.path), undefined, {numeric:true, sensitivity:'base'}));
  const imgs = archData.images.filter(im => (im.folder || '') === archFolder).sort((a, b) => b.archived - a.archived);
  if (!folders.length && !imgs.length) {
    ip.replaceChildren(crumbs, archImagesNote(archFolder
      ? 'Nothing in this folder yet. Drag pictures onto its name in the folder above to put them here.'
      : 'No archived images. Pictures you archive on their own, or save from the web, will appear here.'));
    return;
  }
  const ul = document.createElement('ul'); ul.className = 'arch-grid';
  for (const f of folders) ul.append(archFolderItem(f.path, 'images'));
  for (const im of imgs) {
    const li = document.createElement('li');
    const b = document.createElement('button'); b.type = 'button'; b.setAttribute('aria-label', 'Enlarge archived image');
    const img = document.createElement('img'); img.src = archiveSrc(im.name); img.alt = ''; img.loading = 'lazy'; img.draggable = false;
    b.append(img); b.addEventListener('click', () => viewOnly(archiveSrc(im.name)));
    b.addEventListener('pointerdown', ev => startArchiveDrag(ev, im.name, '', li));
    const d = document.createElement('span'); d.textContent = 'Archived ' + fmtDate.format(new Date(im.archived));
    const erase = document.createElement('button'); erase.type = 'button'; erase.className = 'erase'; erase.textContent = 'Delete forever';
    erase.addEventListener('click', () => eraseArchived(im.name, erase, li));
    li.append(b, d, erase); ul.append(li);
  }
  const hint = document.createElement('p'); hint.className = 'arch-hint';
  hint.textContent = 'Drag a picture onto a folder to put it there, or onto the open entry to use it again.';
  ip.replaceChildren(crumbs, hint, ul);
}
function archFolderItem(path, kind){
  const K = archK(kind);
  const li = document.createElement('li'); li.className = 'arch-folder'; li.dataset.folder = path;
  const inside = K.items.filter(im => inFolder(im.folder || '', path)).length;
  const subs = K.folders.filter(f => parentOf(f.path) === path).length;
  const tile = document.createElement('button'); tile.type = 'button'; tile.className = 'folder-tile';
  tile.setAttribute('aria-label', 'Open folder ' + baseName(path));
  tile.innerHTML = FOLDER_ICON;
  const name = document.createElement('span'); name.className = 'folder-name'; name.textContent = baseName(path); name.title = baseName(path);
  const count = document.createElement('span'); count.className = 'folder-count';
  count.textContent = [subs ? subs + (subs === 1 ? ' folder' : ' folders') : '', inside || !subs ? inside + ' ' + (inside === 1 ? K.one : K.many) : ''].filter(Boolean).join(', ');
  tile.append(name, count);
  tile.addEventListener('click', () => openArchFolder(path));
  tile.addEventListener('pointerdown', ev => startArchiveDrag(ev, null, '', li, path));
  const btns = document.createElement('span'); btns.className = 'folder-btns';
  const rename = document.createElement('button'); rename.type = 'button'; rename.textContent = 'Rename';
  rename.addEventListener('click', () => startFolderRename(path));
  btns.append(rename);
  if (!inside) {   // only an empty folder can be deleted, so nothing is ever lost with one
    const del = document.createElement('button'); del.type = 'button'; del.className = 'erase'; del.textContent = 'Delete';
    del.addEventListener('click', () => deleteArchFolder(path, del));
    btns.append(del);
  }
  li.append(tile, btns);
  return li;
}
function openArchFolder(path){
  const K = archK(); K.folder = path; K.render();
  K.panel.scrollTop = 0;
}
function archFolderMessage(text){
  const ip = archK().panel;
  let n = ip.querySelector('.arch-folder-note');
  if (!n) { n = document.createElement('p'); n.className = 'arch-folder-note'; n.setAttribute('role', 'status'); const c = ip.querySelector('.arch-crumbs'); if (c) c.after(n); else ip.prepend(n); }
  n.textContent = text;
}
async function reloadArchImages(){
  const r = await fetch('/api/archive', {headers:{'X-Journal':'1'}, cache:'no-store'});
  if (!r.ok) throw new Error();
  const data = await r.json();
  archData = {folders:data.folders || [], images:data.images || []};
  archModels = {models:data.models || [], folders:data.modelFolders || []};
  renderArchImages(); renderArchModels();
}
const archPost = (url, body) => fetch(url, {method:'POST', headers:H, body:JSON.stringify(body)});
async function newArchFolder(){
  const btn = $('archNewFolder'); btn.disabled = true;
  try {
    const r = await archPost('/api/archive/folders', {parent:archK().folder, name:'New folder', kind:archKind});
    if (!r.ok) throw new Error();
    const {path} = await r.json();
    await reloadArchImages();
    startFolderRename(path);
  } catch (e) {
    archFolderMessage("Couldn't make a folder. Check that the journal server is still running.");
  } finally { btn.disabled = false; }
}
// Naming a folder: its name turns into a box to type in. Enter (or clicking away) keeps it; Escape leaves it as it was.
function startFolderRename(path){
  const K = archK(), li = [...K.panel.querySelectorAll('.arch-folder')].find(x => x.dataset.folder === path);
  if (!li) return;
  const tile = li.querySelector('.folder-tile'), btns = li.querySelector('.folder-btns');
  const input = document.createElement('input'); input.type = 'text'; input.className = 'folder-rename';
  input.value = baseName(path); input.maxLength = 80; input.setAttribute('aria-label', 'Folder name'); input.spellcheck = false;
  btns.hidden = true; tile.after(input);
  input.focus(); input.select();
  li.scrollIntoView({block:'nearest'});
  let done = false;
  const finish = async keep => {
    if (done) return;
    const name = input.value.trim();
    if (!keep || !name || name === baseName(path)) { done = true; K.render(); return; }
    done = true;
    try {
      const r = await archPost('/api/archive/folders/rename', {path, name, kind:K.kind});
      if (r.status === 409 || r.status === 400) {
        done = false;
        archFolderMessage(r.status === 409 ? 'There\u2019s already something called \u201c' + name + '\u201d in this folder.'
          : 'A folder can\u2019t be called that. Leave out / \\ : * ? " < > | and don\u2019t start it with a full stop.');
        input.focus(); input.select(); return;
      }
      if (!r.ok) throw new Error();
      await reloadArchImages();
    } catch (e) {
      K.render(); archFolderMessage("Couldn't rename that folder. Check that the journal server is still running.");
    }
  };
  input.addEventListener('keydown', ev => {
    ev.stopPropagation();
    if (ev.key === 'Enter') { ev.preventDefault(); finish(true); }
    else if (ev.key === 'Escape') { ev.preventDefault(); finish(false); }   // not closing the Archive
  });
  input.addEventListener('blur', () => finish(true));
}
async function deleteArchFolder(path, btn){
  btn.disabled = true;
  try {
    const r = await archPost('/api/archive/folders/delete', {path, kind:archKind});
    if (r.status === 409) { btn.disabled = false; archFolderMessage('That folder still has files in it, so it was left alone.'); return; }
    if (!r.ok) throw new Error();
    await reloadArchImages();
  } catch (e) {
    btn.disabled = false; archFolderMessage("Couldn't delete that folder. Check that the journal server is still running.");
  }
}
async function moveIntoArchFolder(d, to){
  try {
    const names = d.name ? [d.name] : [];
    const r = await archPost('/api/archive/move', {kind:archKind, [archKind === 'models' ? 'models' : 'images']:names, folders:d.folder ? [d.folder] : [], to});
    if (!r.ok) throw new Error();
    await reloadArchImages();
  } catch (e) {
    archFolderMessage("Couldn't move that. Check that the journal server is still running.");
  }
}
// Whether what's being dragged can go into the folder at `to`.
function canDropInFolder(d, to){
  if (d.folder) return !inFolder(to, d.folder) && to !== parentOf(d.folder);   // not into itself, nor where it already is
  return to !== d.from;
}
async function openArchive(){
  const p = document.createElement('p'); p.className = 'arch-note'; p.textContent = 'Opening the archive…';
  $('archEntries').replaceChildren(p);
  $('archImages').replaceChildren(p.cloneNode(true));
  $('archModels').replaceChildren(p.cloneNode(true));
  $('archTasks').replaceChildren(p.cloneNode(true));
  $('archive').showModal();
  document.body.classList.toggle('can-bring-back', canBringBack());
  try {
    const r = await fetch('/api/archive', {headers:{'X-Journal':'1'}, cache:'no-store'});
    if (!r.ok) throw new Error();
    renderArchive(await r.json());
  } catch (e) {
    p.textContent = "Couldn't open the archive. Check that the journal server is still running.";
  }
}
async function addBack(id, btn, li){
  btn.disabled = true; btn.textContent = 'Adding…';
  try {
    const r = await fetch('/api/archive/entries/' + id + '/restore', {method:'POST', headers:H});
    if (!r.ok) throw new Error();
    li.remove();
    if (!$('archEntries').querySelector('li')) {
      const p = document.createElement('p'); p.className = 'arch-note'; p.textContent = 'No archived entries. Entries you archive will appear here.';
      $('archEntries').replaceChildren(p);
    }
    applyIncoming(await store.load());
    store.changedImages().then(list => { changed = new Set(list); }).catch(() => {});
  } catch (e) {
    btn.disabled = false; btn.textContent = 'Add to journal';
    const note = document.createElement('p'); note.className = 'arch-note'; note.textContent = "Couldn't add that entry back. Try again.";
    li.append(note);
  }
}
async function eraseArchived(name, btn, li){
  if (!armed(btn, 'Delete forever', "Delete forever? Can't be undone")) return;
  btn.disabled = true;
  try {
    const r = await fetch('/api/archive/images/' + name, {method:'DELETE', headers:H});
    if (!r.ok) throw new Error();
    archData.images = archData.images.filter(im => im.name !== name);
    renderArchImages();
  } catch (e) {
    btn.disabled = false; btn.textContent = "Couldn't delete. Try again";
  }
}
async function eraseArchivedEntry(id, btn, li){
  if (!armed(btn, 'Delete forever', "Delete forever? Can't be undone")) return;
  btn.disabled = true;
  try {
    const r = await fetch('/api/archive/entries/' + id, {method:'DELETE', headers:H});
    if (!r.ok) throw new Error();
    li.remove();
    if (!$('archEntries').querySelector('li')) {
      const p = document.createElement('p'); p.className = 'arch-note'; p.textContent = 'No archived entries. Entries you archive will appear here.';
      $('archEntries').replaceChildren(p);
    }
  } catch (e) {
    btn.disabled = false; btn.textContent = "Couldn't delete. Try again";
  }
}
/* Dragging a picture out of the Archive into the open entry. As soon as it's picked up, the Archive steps
   aside so the entry can be seen; it comes back if the picture is let go anywhere else. The picture can go
   anywhere in the writing, just like one being moved within it, or onto the right-hand side (it goes at the
   end of the writing and is shown on the right). A picture on its own in the archive comes back into the
   journal; one from an archived entry is copied, so that entry still has it. */
let archDrag = null;
const canBringBack = () => !!currentId && !els.page.hidden;
// Pictures and folders in the Images tab (li given) can also be dragged onto folders there. The Archive only
// steps aside once a picture is dragged out past its edge; a folder never leaves it.
function startArchiveDrag(ev, name, title, li, folder){
  if (ev.button !== 0 || archDrag || (!li && !canBringBack())) return;
  const naming = document.activeElement;
  if (naming && naming.classList && naming.classList.contains('folder-rename')) naming.blur();   // keeps the name being typed
  ev.preventDefault();
  archDrag = {name, folder:folder || null, from:archK().folder, model:archKind === 'models' && !!name, title:title || '', li, x0:ev.clientX, y0:ev.clientY, x:ev.clientX, y:ev.clientY,
    started:false, target:null, folderTarget:null, inArchive:!!li, ghost:null, raf:0};
  window.addEventListener('pointermove', moveArchiveDrag);
  window.addEventListener('pointerup', endArchiveDrag);
  window.addEventListener('pointercancel', cancelArchiveDrag);
}
function moveArchiveDrag(ev){
  const d = archDrag; if (!d) return;
  d.x = ev.clientX; d.y = ev.clientY;
  if (!d.started) {
    if (Math.hypot(d.x - d.x0, d.y - d.y0) < 4) return;
    d.started = true;
    if (d.inArchive && !$('archive').open) d.inArchive = false;
    if (!d.inArchive) for (const dlg of document.querySelectorAll('dialog[open]')) dlg.close();   // step aside (the enlarged view too)
    document.body.classList.add('moving');
    let g;
    if (d.folder) { g = document.createElement('div'); g.className = 'ghost ghost-folder'; g.innerHTML = FOLDER_ICON; }
    else if (d.model) { g = document.createElement('div'); g.className = 'ghost ghost-folder ghost-model'; g.innerHTML = MODEL_ICON; }
    else { g = document.createElement('img'); g.className = 'ghost'; g.src = archiveSrc(d.name); g.alt = ''; }
    (d.inArchive ? $('archive') : document.body).append(g); d.ghost = g;   // inside the Archive, so it shows above it
    d.raf = requestAnimationFrame(archiveDragFrame);
  }
  d.ghost.style.left = d.x + 'px'; d.ghost.style.top = d.y + 'px';
}
function markArchDrop(el){
  for (const x of document.querySelectorAll('.drop-folder')) if (x !== el) x.classList.remove('drop-folder');
  if (el) el.classList.add('drop-folder');
}
function archiveDragFrame(){
  const d = archDrag; if (!d || !d.started) return;
  if (d.inArchive) {
    const dlg = $('archive'), r = dlg.getBoundingClientRect();
    if (d.x >= r.left && d.x <= r.right && d.y >= r.top && d.y <= r.bottom) {
      // Over the Archive: is it over a folder, or a name in the path at the top?
      const hit = document.elementFromPoint(d.x, d.y), el = hit && hit.closest ? hit.closest('[data-folder]') : null;
      const ok = el && dlg.contains(el) && canDropInFolder(d, el.dataset.folder);
      markArchDrop(ok ? el : null); d.folderTarget = ok ? el.dataset.folder : null;
      d.raf = requestAnimationFrame(archiveDragFrame); return;
    }
    markArchDrop(null); d.folderTarget = null;
    if (d.folder || !canBringBack()) { d.raf = requestAnimationFrame(archiveDragFrame); return; }
    // A picture taken out past the Archive's edge: the Archive steps aside so it can go into the entry.
    d.inArchive = false;
    for (const x of document.querySelectorAll('dialog[open]')) x.close();
    document.body.append(d.ghost);
  }
  const mr = els.scroll.getBoundingClientRect(), edge = 60;
  if (d.y < mr.top + edge) els.scroll.scrollTop -= Math.ceil((mr.top + edge - d.y) / 4);
  else if (d.y > mr.bottom - edge) els.scroll.scrollTop += Math.ceil((d.y - (mr.bottom - edge)) / 4);
  const box = sideDrop(d.x, d.y);
  showSideDrop(box);
  const br = els.body.getBoundingClientRect();
  if (box) { d.target = {side:true}; showMark(null); }
  else if (d.x < br.left - 40 || d.x > br.right + 40 || d.y < mr.top || d.y > mr.bottom) { d.target = null; showMark(null); }   // not over the entry
  else {
    d.ghost.style.visibility = 'hidden';
    d.target = dropTarget(d.x, d.y);
    d.ghost.style.visibility = '';
    showMark(d.target);
  }
  d.raf = requestAnimationFrame(archiveDragFrame);
}
function finishArchiveDrag(){
  const d = archDrag; archDrag = null;
  cancelAnimationFrame(d.raf);
  window.removeEventListener('pointermove', moveArchiveDrag);
  window.removeEventListener('pointerup', endArchiveDrag);
  window.removeEventListener('pointercancel', cancelArchiveDrag);
  document.body.classList.remove('moving');
  if (d.ghost) d.ghost.remove();
  showMark(null); showSideDrop(null); markArchDrop(null);
  return d;
}
// After a drag, the click that follows letting go isn't taken as a click on whatever is under the pointer.
function swallowClick(){
  const stop = ev => { ev.stopPropagation(); ev.preventDefault(); };
  window.addEventListener('click', stop, {capture:true, once:true});
  setTimeout(() => window.removeEventListener('click', stop, {capture:true}), 0);
}
function endArchiveDrag(){
  if (!archDrag) return;
  const d = finishArchiveDrag();
  if (!d.started) return;   // just a click: it enlarges (or opens the folder), as before
  swallowClick();
  if (d.inArchive) { if (typeof d.folderTarget === 'string') moveIntoArchFolder(d, d.folderTarget); return; }
  if (!d.target || !canBringBack()) { if (!$('archive').open) $('archive').showModal(); return; }   // let go elsewhere: the Archive comes back as it was
  if (d.model) bringBackModel(d); else bringBack(d);
}
function cancelArchiveDrag(){
  if (!archDrag) return;
  const d = finishArchiveDrag();
  if (d.started && !d.inArchive && !$('archive').open) $('archive').showModal();
}
async function bringBack(d){
  const id = currentId;
  setStatus('Adding image…');
  try {
    const r = await fetch('/api/archive/images/' + d.name + '/restore', {method:'POST', headers:H});
    if (!r.ok) throw new Error();
    const {name, copied} = await r.json();
    if (!copied) {
      store.changedImages().then(list => { changed = new Set(list); }).catch(() => {});   // its earlier versions came back too
      if (d.li) {   // no longer in the archive
        archData.images = archData.images.filter(im => im.name !== d.name);
        renderArchImages();
      }
    }
    if (id !== currentId) {
      // The entry was closed meanwhile: the picture goes at the end of its writing.
      const e = entries.get(id);
      if (e) { e.body = serializeParts([...parseBody(e.body), {type:'img', name, title:d.title}]); e.images = imagesIn(e.body); markChanged(id); }
      return;
    }
    let t = d.target.side ? endOfLastWord() : d.target;
    const inBody = n => n && els.body.contains(n);
    if (!(t.text ? inBody(t.text) : inBody(t.parent))) t = endOfLastWord();   // the writing changed under it meanwhile
    const fig = makeFigure(name, d.title);
    placeFigure(fig, t);
    onBodyChange();
    if (d.target.side) addToShelf(name);
  } catch (err) {
    if (id === currentId) setStatus("Couldn't bring that picture back from the archive. Check that the journal server is still running.", true);
  }
}

/* ---------- Models in the Archive ----------
   Models archived from the right of an entry, each shown turnable in a small box. Drag one by its caption
   onto a folder to put it there, or out onto the open entry to put it back on its right; or use Add to entry.
   The boxes are only filled in as they scroll into view, so a large archive opens quickly. */
const MODEL_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3 20 7.5v9L12 21l-8-4.5v-9zM4 7.5 12 12l8-4.5M12 12v9" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>';
const archModelSeen = new IntersectionObserver(list => {
  for (const x of list) if (x.isIntersecting && !x.target.dataset.shown) {
    x.target.dataset.shown = '1'; archModelSeen.unobserve(x.target);
    m3View(x.target.querySelector('canvas'), 'archive/' + x.target.dataset.model, x.target.querySelector('.model-note'), false);
  }
}, {rootMargin:'200px'});
function renderArchModels(){
  const panel = $('archModels'), K = archK('models');
  if (archModelFolder && !archModels.folders.some(f => f.path === archModelFolder)) archModelFolder = '';
  const crumbs = archCrumbs(K);
  const folders = archModels.folders.filter(f => parentOf(f.path) === archModelFolder)
    .sort((a, b) => baseName(a.path).localeCompare(baseName(b.path), undefined, {numeric:true, sensitivity:'base'}));
  const models = archModels.models.filter(m => (m.folder || '') === archModelFolder).sort((a, b) => b.archived - a.archived);
  if (!folders.length && !models.length) {
    panel.replaceChildren(crumbs, archImagesNote(archModelFolder
      ? 'Nothing in this folder yet. Drag models onto its name in the folder above to put them here.'
      : 'No archived models. Models you archive from the right of an entry will appear here.'));
    return;
  }
  const ul = document.createElement('ul'); ul.className = 'arch-grid arch-models';
  for (const f of folders) ul.append(archFolderItem(f.path, 'models'));
  for (const m of models) ul.append(archModelItem(m));
  const hint = document.createElement('p'); hint.className = 'arch-hint';
  hint.textContent = 'Drag a model by its caption onto a folder to put it there, or onto the open entry to use it again. Drag the model itself to turn it.';
  panel.replaceChildren(crumbs, hint, ul);
  for (const li of ul.querySelectorAll('.arch-model')) archModelSeen.observe(li);
}
function archModelItem(m){
  const li = document.createElement('li'); li.className = 'arch-model'; li.dataset.model = m.name;
  const view = document.createElement('div'); view.className = 'arch-model-view';
  const canvas = document.createElement('canvas'); canvas.className = 'model-canvas';
  canvas.setAttribute('aria-label', 'Archived 3D model. Drag to turn it');
  const note = document.createElement('div'); note.className = 'model-note'; note.hidden = true;
  view.append(canvas, note);
  const cap = document.createElement('div'); cap.className = 'arch-model-cap'; cap.title = 'Drag here to move it';
  cap.textContent = 'Archived ' + fmtDate.format(new Date(m.archived));
  cap.addEventListener('pointerdown', ev => startArchiveDrag(ev, m.name, '', li));
  const btns = document.createElement('div'); btns.className = 'arch-model-btns';
  const open = document.createElement('button'); open.type = 'button'; open.textContent = 'Open';
  open.addEventListener('click', () => openModelView('archive/' + m.name));
  const add = document.createElement('button'); add.type = 'button'; add.className = 'arch-model-add'; add.textContent = 'Add to entry';
  add.title = 'Put it back on the right of the open entry';
  add.addEventListener('click', () => bringBackModel({name:m.name, li, button:add}));
  const erase = document.createElement('button'); erase.type = 'button'; erase.className = 'erase'; erase.textContent = 'Delete forever';
  erase.addEventListener('click', () => eraseArchivedModel(m.name, erase));
  btns.append(open, add, erase);
  li.append(view, cap, btns);
  return li;
}
// An archived model back into the journal, on the right of the open entry.
async function bringBackModel(d){
  const id = currentId, e = id ? entries.get(id) : null;
  if (!e || els.page.hidden) { archFolderMessage('Open an entry first, to put the model on its right.'); return; }
  if (d.button) { d.button.disabled = true; d.button.textContent = 'Adding\u2026'; }
  try {
    const r = await fetch('/api/archive/models/' + d.name + '/restore', {method:'POST', headers:H});
    if (!r.ok) throw new Error();
    const {name} = await r.json();
    archModels.models = archModels.models.filter(m => m.name !== d.name);
    M3.cache.delete('archive/' + d.name);
    renderArchModels();
    if (id === currentId) addToShelf('model:' + name);
    else { e.side = shelfNames(e).concat('model:' + name); markChanged(id); }
  } catch (err) {
    if (d.button) { d.button.disabled = false; d.button.textContent = 'Add to entry'; }
    setStatus("Couldn't bring that model back from the archive. Check that the journal server is still running.", true);
  }
}
async function eraseArchivedModel(name, btn){
  if (!armed(btn, 'Delete forever', "Delete forever? Can't be undone")) return;
  btn.disabled = true;
  try {
    const r = await fetch('/api/archive/models/' + name, {method:'DELETE', headers:H});
    if (!r.ok) throw new Error();
    archModels.models = archModels.models.filter(m => m.name !== name);
    M3.cache.delete('archive/' + name);
    renderArchModels();
  } catch (e) {
    btn.disabled = false; btn.textContent = "Couldn't delete. Try again";
  }
}
/* Archiving or deleting a model from the right of an entry (or from its large view). It's taken off the
   right of every entry that shows it. Archived, it goes to the Archive's Models; deleted, it's gone for good. */
function dropModelEverywhere(name, forever){
  const ref = 'model:' + name;
  if (forever) for (const [id, e] of entries) if (e.books && e.books[name]) { e.books = Object.assign({}, e.books); delete e.books[name]; markChanged(id); }
  for (const [id, e] of entries) if (e.side && e.side.includes(ref)) { e.side = e.side.filter(n => n !== ref); markChanged(id); }
  M3.cache.delete(name);
  renderShelf();
}
async function archiveModel(name){
  try {
    const r = await fetch('/api/models/' + name + '/archive', {method:'POST', headers:H});
    if (!r.ok && r.status !== 404) throw new Error();
    dropModelEverywhere(name);
    return true;
  } catch (e) {
    setStatus("Couldn't archive the model. Check that the journal server is still running.", true);
    return false;
  }
}
async function eraseModel(name, btn){
  if (!armed(btn, 'Delete forever', "Delete forever? Can't be undone")) return false;
  try {
    const r = await fetch('/api/models/' + name, {method:'DELETE', headers:H});
    if (!r.ok) throw new Error();
    dropModelEverywhere(name, true);
    return true;
  } catch (e) {
    setStatus("Couldn't delete the model. Check that the journal server is still running.", true);
    return false;
  }
}

function selectTab(which){
  for (const [tab, panel, key] of [['tabEntries', 'archEntries', 'entries'], ['tabImages', 'archImages', 'images'],
                                   ['tabArchModels', 'archModels', 'models'], ['tabArchTasks', 'archTasks', 'tasks']]) {
    $(tab).setAttribute('aria-selected', String(which === key));
    $(panel).hidden = which !== key;
  }
  if (which === 'images' || which === 'models') archKind = which;
  $('archNewFolder').hidden = which !== 'images' && which !== 'models';   // folders are for the Images and Models tabs
}
$('archiveBtn').addEventListener('click', openArchive);
$('archiveClose').addEventListener('click', () => $('archive').close());
$('archNewFolder').addEventListener('click', newArchFolder);
$('archive').addEventListener('click', ev => { if (ev.target === $('archive')) $('archive').close(); });
$('tabEntries').addEventListener('click', () => selectTab('entries'));
$('tabImages').addEventListener('click', () => selectTab('images'));
$('tabArchTasks').addEventListener('click', () => selectTab('tasks'));
$('tabArchModels').addEventListener('click', () => selectTab('models'));

/* ---------- Zoom ---------- */
// With Zoom on, the first place in the column right of the text shows the part of the entry under the
// pointer, magnified; any pictures there move one place down. A faint frame over the text marks which part.
// It works the same over the pictures and linked entries on the right: point at one to magnify that part of it.
// The magnified view stays at the top of the right-hand side as the things there are scrolled.
// The freeze shortcut (Shift+Z unless changed in the Menu) freezes that view in first place;
// pressing it again, or Close, lets it follow the pointer again.
const zoom = {on:false, frozen:false, live:false, copy:null, src:null, dirty:true, over:false, overShelf:false, x:0, y:0, frame:0};
const zoomView = $('zoomView'), zoomLens = $('zoomLens');
// A copy of what's being magnified: the entry's text, or a picture or linked entry on the right.
function zoomCopy(src){
  let c;
  if (src === els.body) {
    c = els.body.cloneNode(true);
    for (const a of ['id', 'role', 'aria-multiline', 'aria-label', 'contenteditable', 'data-placeholder', 'spellcheck']) c.removeAttribute(a);
    for (const n of c.querySelectorAll('[contenteditable]')) n.removeAttribute('contenteditable');
    c.style.width = els.body.clientWidth + 'px';
  } else {
    c = src.cloneNode(true);
    const bar = c.querySelector(':scope > .zoom-bar'); if (bar) bar.remove();   // just the picture or the writing, not its buttons
    c.classList.remove('lifted', 'shifting'); c.removeAttribute('aria-label'); c.setAttribute('aria-hidden', 'true');
    c.style.width = src.offsetWidth + 'px'; c.style.height = src.offsetHeight + 'px';
  }
  c.classList.add('zoom-copy');
  zoomView.replaceChildren(c);
  zoom.copy = c; zoom.src = src; zoom.dirty = false;
  if (src !== els.body) syncZoomScroll();
}
// A linked entry on the right may be scrolled part way down: the copy shows the same part of it.
function syncZoomScroll(){
  const v = zoom.src && zoom.src.querySelector('.shelf-entry-view'), cv = zoom.copy && zoom.copy.querySelector('.shelf-entry-view');
  if (v && cv) cv.style.cssText = 'top:' + (-v.scrollTop) + 'px;bottom:auto;right:' + (v.offsetWidth - v.clientWidth) + 'px;overflow:visible';
}
const zoomHintText = () => 'Point at the text, or at a picture or entry on the right, to magnify it. ' + freezeCombo() + ' freezes the view.';
function showZoomPlace(){
  if (!zoomView.hidden) return;
  zoomView.hidden = false; layoutShelf();
}
// What's under the pointer to magnify: the text, a picture or entry on the right, or nothing.
// Over the magnified view itself, it keeps showing what it was showing.
function zoomSource(){
  if (els.page.hidden) return null;
  const b = els.body.getBoundingClientRect();
  if (zoom.over && zoom.x >= b.left && zoom.x <= b.right && zoom.y >= b.top && zoom.y <= b.bottom) return {el:els.body, rect:b};
  if (!zoom.overShelf) return null;
  if (!zoomView.hidden) {
    const v = zoomView.getBoundingClientRect();
    if (zoom.x >= v.left && zoom.x <= v.right && zoom.y >= v.top && zoom.y <= v.bottom) return zoom.live ? 'keep' : null;
  }
  const hit = document.elementFromPoint(zoom.x, zoom.y);
  const item = hit && hit.closest ? hit.closest('#shelfPics > .shelf-item') : null;
  // A picture being drawn on, or being moved, isn't magnified.
  if (!item || item.classList.contains('drawing') || item.classList.contains('inked') || item.classList.contains('lifted')) return null;
  if (item.classList.contains('shelf-model')) return null;   // a 3D model is zoomed by itself (Ctrl and the scroll wheel)
  if (item.classList.contains('shelf-pdf')) return null;   // a PDF is zoomed in its own reader
  return {el:item, rect:item.getBoundingClientRect()};
}
// Zoom is on but the pointer isn't over the text: the first place stays, with a hint.
function zoomIdle(){
  zoom.live = false; zoomLens.hidden = true;
  if (!zoom.on) { zoomView.hidden = true; layoutShelf(); return; }
  if (!zoomView.querySelector('.zoom-hint')) {
    const hint = document.createElement('div'); hint.className = 'zoom-hint'; hint.textContent = zoomHintText();
    zoomView.replaceChildren(hint); zoom.copy = null;
  }
  showZoomPlace();
}
function drawZoom(){
  zoom.frame = 0;
  if (zoom.frozen) return;
  if (!zoom.on || els.page.hidden) return zoomIdle();
  const src = zoomSource();
  if (src === 'keep') return;
  if (!src) return zoomIdle();
  showZoomPlace();
  if ($('shelf').hidden) { zoom.live = false; zoomLens.hidden = true; return; }   // no room beside the text
  if (zoom.dirty || !zoom.copy || zoom.src !== src.el) zoomCopy(src.el);
  else if (src.el !== els.body) syncZoomScroll();
  const b = src.rect, w = zoomView.clientWidth, h = zoomView.clientHeight;
  const z = settings.zoomLevel || 2, px = zoom.x - b.left, py = zoom.y - b.top;
  zoom.copy.style.transform = 'translate(' + (w / 2 - px * z) + 'px,' + (h / 2 - py * z) + 'px) scale(' + z + ')';
  const lw = w / z, lh = h / z;
  Object.assign(zoomLens.style, {left:(zoom.x - lw / 2) + 'px', top:(zoom.y - lh / 2) + 'px', width:lw + 'px', height:lh + 'px'});
  zoomLens.hidden = false; zoom.live = true;
}
function queueZoom(){ if (zoom.on && !zoom.frame) zoom.frame = requestAnimationFrame(drawZoom); }
// Keep the magnified copy up to date as you write.
new MutationObserver(() => { zoom.dirty = true; if (zoom.over) queueZoom(); })
  .observe(els.body, {childList:true, subtree:true, characterData:true, attributes:true});
els.body.addEventListener('pointermove', ev => {
  if (ev.pointerType === 'touch') return;
  zoom.x = ev.clientX; zoom.y = ev.clientY; zoom.over = true; queueZoom();
});
els.body.addEventListener('pointerleave', () => { zoom.over = false; queueZoom(); });
// The same over the pictures and linked entries on the right.
$('shelf').addEventListener('pointermove', ev => {
  if (ev.pointerType === 'touch') return;
  zoom.x = ev.clientX; zoom.y = ev.clientY; zoom.overShelf = true; queueZoom();
});
$('shelf').addEventListener('pointerleave', () => { zoom.overShelf = false; queueZoom(); });
$('shelf').addEventListener('scroll', queueZoom, true);   // the right-hand side, or a linked entry in it, scrolled
new MutationObserver(() => { zoom.dirty = true; if (zoom.overShelf) queueZoom(); })
  .observe($('shelfPics'), {childList:true, subtree:true, characterData:true});
els.scroll.addEventListener('scroll', queueZoom);
window.addEventListener('resize', () => { zoom.dirty = true; queueZoom(); });
$('zoomBtn').addEventListener('mousedown', ev => ev.preventDefault());   // keep the cursor where it is
$('zoomBtn').addEventListener('click', () => {
  zoom.on = !zoom.on;
  $('zoomBtn').setAttribute('aria-pressed', String(zoom.on));
  if (zoom.frozen) unfreezeZoom();
  zoom.dirty = true;
  if (zoom.on) { zoomIdle(); queueZoom(); }
  else { zoomLens.hidden = true; zoom.live = false; zoomView.replaceChildren(); zoom.copy = null; zoom.src = null; zoomView.hidden = true; layoutShelf(); }
});

/* A frozen zoom frame: first in line on the right until the freeze shortcut or its Close button */
const zoomBar = document.createElement('div'); zoomBar.className = 'zoom-bar';
zoomBar.innerHTML = '<span class="zoom-tag"></span><span class="zoom-space"></span>'
  + '<button type="button" class="zoom-save">Save as picture</button><button type="button" class="zoom-close">Close</button>';
const zoomSave = zoomBar.querySelector('.zoom-save');
const frozenTagText = () => 'Frozen · ' + freezeCombo() + ' to release';
function freezeZoom(){
  zoom.frozen = 'zoom'; zoom.live = false;
  if (zoom.frame) { cancelAnimationFrame(zoom.frame); zoom.frame = 0; }
  zoomLens.hidden = true;
  zoomBar.querySelector('.zoom-tag').textContent = frozenTagText();
  zoomSave.disabled = false; zoomSave.textContent = 'Save as picture'; zoomSave.title = '';
  zoomView.classList.add('frozen'); zoomView.append(zoomBar);
}
function unfreezeZoom(){
  zoom.frozen = false;
  zoomView.classList.remove('frozen'); zoomBar.remove();
  zoom.dirty = true;
  if (zoom.on) { zoomIdle(); queueZoom(); }
}
zoomBar.querySelector('.zoom-close').addEventListener('click', unfreezeZoom);

/* The freeze shortcut: one key, or a key with Ctrl / Alt / Shift / Meta, chosen in the Menu */
const NAMED_KEYS = ['Enter', 'Tab', 'Backspace', 'Insert', 'Delete', 'Home', 'End', 'PageUp', 'PageDown', 'ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'];
function comboOf(ev){
  let k = ev.key || '';
  const code = ev.code || '';
  if (k.length === 1 && /[a-z]/i.test(k)) k = k.toUpperCase();
  else if (/^Key[A-Z]$/.test(code)) k = code[3];
  else if (/^Digit\d$/.test(code)) k = code[5];
  else if (/^F([1-9]|1\d|2[0-4])$/.test(k)) { /* function keys as they are */ }
  else if (k === ' ') k = 'Space';
  else if (!NAMED_KEYS.includes(k)) return null;
  return [ev.ctrlKey && 'Ctrl', ev.altKey && 'Alt', ev.shiftKey && 'Shift', ev.metaKey && 'Meta', k].filter(Boolean).join('+');
}
function freezeCombo(){ return settings.freezeKey || 'Shift+Z'; }
document.addEventListener('keydown', ev => {
  if (ev.isComposing || ev.repeat || document.querySelector('dialog[open]')) return;
  if (comboOf(ev) !== freezeCombo()) return;
  if (zoom.frozen) { ev.preventDefault(); ev.stopPropagation(); unfreezeZoom(); }
  else if (zoom.on && zoom.live) { ev.preventDefault(); ev.stopPropagation(); freezeZoom(); }
}, true);
// Keep the words that mention the shortcut in step with the Menu.
function showFreezeCombo(){
  $('zoomBtn').title = 'Show a magnified view of whatever is under the pointer: the text, or a picture or entry on the right. ' + freezeCombo() + ' freezes it';
  const hint = zoomView.querySelector('.zoom-hint'); if (hint) hint.textContent = zoomHintText();
  if (zoom.frozen) zoomBar.querySelector('.zoom-tag').textContent = frozenTagText();
}

/* Pictures on the right: dragged out of the entry, laid out in rows (one per row at full size,
   up to four when shrunk in the Menu); if they don't all fit, the space scrolls. */
function shelfBox(){
  if (els.page.hidden) return null;
  const b = els.body.getBoundingClientRect(), m = els.main.getBoundingClientRect();
  const left = Math.max(b.right + 32, els.scroll.getBoundingClientRect().right + 20), right = m.left + els.main.clientWidth - 32;
  const w = Math.min(right - left, 720);
  const top = Math.max(m.top + 24, els.page.querySelector('.meta').getBoundingClientRect().bottom + 12);
  const h = m.bottom - 24 - top;
  if (w < 180 || h < 120) return null;   // no room beside the text (narrow window)
  return {left, top, w, h};
}
function layoutShelf(){
  const shelf = $('shelf');
  const box = ($('shelfPics').childElementCount || !$('zoomView').hidden) ? shelfBox() : null;
  shelf.hidden = !box;
  if (box) Object.assign(shelf.style, {left:box.left + 'px', top:box.top + 'px', width:box.w + 'px', maxHeight:box.h + 'px'});
}
// Each entry keeps its own pictures on the right; they're saved in the entry's file ("side: …").
// Only pictures that are still in the entry are shown.
// A linked entry is kept in the list as "entry:<id>", and is shown while the entry still links to it.
// A 3D model is kept as "model:<file name>" and is always shown (it lives only on the right, not in the writing).
// A PDF is kept as "pdf:<file name>", and is shown while the entry's writing still has it.
const isEntryRef = n => n.startsWith('entry:');
// A quote in the entry, shown on the right, goes by a short code made from its words: "quote:<code>".
const isQuoteRef = n => n.startsWith('quote:');
// Linked entries and quotes on the right are both read (and drawn or highlighted over) the same way.
const isReadRef = n => isEntryRef(n) || isQuoteRef(n);
// Where a linked entry's or a quote's ink is kept in this entry's "inks": the linked entry's id, or "q-<code>".
const inkKey = ref => isQuoteRef(ref) ? 'q-' + ref.slice(6) : ref.slice(6);
function quoteCode(text){
  text = text.replace(/\s+$/, '');
  let h1 = 0xdeadbeef, h2 = 0x41c6ce57;
  for (let i = 0; i < text.length; i++) {
    const c = text.charCodeAt(i);
    h1 = Math.imul(h1 ^ c, 2654435761); h2 = Math.imul(h2 ^ c, 1597334677);
  }
  h1 = Math.imul(h1 ^ (h1 >>> 16), 2246822507) ^ Math.imul(h2 ^ (h2 >>> 13), 3266489909);
  h2 = Math.imul(h2 ^ (h2 >>> 16), 2246822507) ^ Math.imul(h1 ^ (h1 >>> 13), 3266489909);
  return (h2 >>> 0).toString(36) + (h1 >>> 0).toString(36);
}
const quotesIn = body => parseBody(body).filter(p => p.type === 'quote').map(p => p.text);
// The words of the quote in this entry that a "quote:<code>" stands for ('' if it's no longer there).
function quoteFor(e, ref){
  const code = ref.slice(6);
  return (e ? quotesIn(e.body) : []).find(t => quoteCode(t) === code) || '';
}
function shelfNames(e){
  if (!e || !e.side) return [];
  const links = e.side.some(isEntryRef) ? linksIn(e.body) : [];
  const quotes = e.side.some(isQuoteRef) ? quotesIn(e.body).map(quoteCode) : [];
  const pdfs = e.side.some(isPdfRef) ? pdfsIn(e.body) : [];
  return e.side.filter(n => isEntryRef(n) ? links.includes(n.slice(6)) : isQuoteRef(n) ? quotes.includes(n.slice(6))
    : isPdfRef(n) ? pdfs.includes(n.slice(4)) : isModelRef(n) || isDraftRef(n) || e.images.includes(n));
}
function renameSide(id, old, name){
  const e = entries.get(id);
  if (e && e.side) e.side = e.side.map(n => n === old ? name : n);
}
function titleShelfItem(item, name){
  const e = entries.get(currentId), title = e ? titleIn(e.body, name) : '';
  const tag = item.querySelector('.zoom-tag'); tag.textContent = title || 'Picture'; tag.title = title;
  item.querySelector(':scope > img').alt = title || 'Picture from the entry';
}
function shelfItem(name){
  if (isEntryRef(name)) return shelfEntryItem(name);
  if (isQuoteRef(name)) return shelfQuoteItem(name);
  if (isModelRef(name)) return shelfModelItem(name);
  if (isDraftRef(name)) return shelfDraftItem(name);
  if (isPdfRef(name)) return shelfPdfItem(name);
  const item = document.createElement('div'); item.className = 'shelf-item'; item.dataset.name = name;
  const img = document.createElement('img'); img.src = '/images/' + name; img.draggable = false;
  const bar = document.createElement('div'); bar.className = 'zoom-bar';
  bar.innerHTML = '<span class="zoom-tag"></span><span class="zoom-space"></span>'
    + '<button type="button" class="side-open-btn" title="Open this picture large">Open</button>'
    + '<button type="button" class="side-draw-btn" title="Draw on this picture">Draw</button><button type="button" class="side-close">Close</button>';
  item.append(img, bar);
  titleShelfItem(item, name);
  bar.querySelector('.side-open-btn').addEventListener('click', () => openShelfPicture(item));
  bar.querySelector('.side-draw-btn').addEventListener('click', () => openSideDraw(item));
  wireShelfItem(item, bar);
  return item;
}
// Open on a picture on the right: shows it large, just as clicking it in the writing does (with its title,
// Restore and so on). If it isn't in the writing any more, it's shown large for looking at only.
function openShelfPicture(item){
  const name = item.dataset.name;
  const fig = [...els.body.querySelectorAll('.fig')].find(f => f.dataset.name === name);
  if (fig) { openViewer(fig); return; }
  const e = entries.get(currentId);
  viewOnly('/images/' + name, e ? titleIn(e.body, name) : '');
}
// A linked entry on the right: its title and everything in it, scrolling within the box.
function shelfEntryItem(ref){
  const id = ref.slice(6), e = entries.get(id);
  const item = document.createElement('div'); item.className = 'shelf-item shelf-entry'; item.dataset.name = ref;
  const view = document.createElement('div'); view.className = 'shelf-entry-view';
  // The page holds the entry's writing and, over it, any ink drawn on it from this entry.
  // The dates line sits above the page, so however it wraps it can't move the writing under the ink.
  const frag = entryPreview(id), meta = frag.querySelector('.link-meta');
  if (meta) view.append(meta);
  const page = document.createElement('div'); page.className = 'shelf-entry-page';
  page.append(frag);
  view.append(page);
  const rec = inkRec(entries.get(currentId), id), box = page.querySelector('.link-body');
  item.inkMarks = rec && rec.hl && box ? renderMarks(box, rec.hl) : [];
  if (rec && rec.img) {
    page.append(shelfInk(rec.img));
    if (rec.w) freezePage(page, rec.w, rec.v);
  }
  const bar = document.createElement('div'); bar.className = 'zoom-bar';
  bar.innerHTML = '<span class="zoom-tag"></span><span class="zoom-space"></span>'
    + '<button type="button" class="side-open-btn" title="Preview this entry">Open</button>'
    + '<button type="button" class="side-draw-btn" title="Draw or highlight on this entry">Draw</button><button type="button" class="side-close">Close</button>';
  const tag = bar.querySelector('.zoom-tag'); tag.textContent = linkName(id); tag.title = linkName(id);
  bar.querySelector('.side-open-btn').hidden = !e;
  bar.querySelector('.side-open-btn').addEventListener('click', () => openLinkView(id));
  bar.querySelector('.side-draw-btn').hidden = !e;
  bar.querySelector('.side-draw-btn').addEventListener('click', () => openSideDraw(item));
  item.setAttribute('aria-label', 'Linked entry: ' + linkName(id));
  item.append(view, bar);
  wireShelfItem(item, bar);
  return item;
}
// A quote from the entry on the right: its words in their box, scrolling within it, and like a linked entry
// it can be highlighted and drawn over (the ink is kept with this entry).
function shelfQuoteItem(ref){
  const text = quoteFor(entries.get(currentId), ref);
  const item = document.createElement('div'); item.className = 'shelf-item shelf-entry shelf-quote'; item.dataset.name = ref;
  const view = document.createElement('div'); view.className = 'shelf-entry-view';
  const page = document.createElement('div'); page.className = 'shelf-entry-page';
  const q = makeQuote(text, true), box = q.querySelector('.quote-text');
  box.classList.add('link-body');
  page.append(q); view.append(page);
  const rec = inkRec(entries.get(currentId), inkKey(ref));
  item.inkMarks = rec && rec.hl ? renderMarks(box, rec.hl) : [];
  if (rec && rec.img) {
    page.append(shelfInk(rec.img));
    if (rec.w) freezePage(page, rec.w, rec.v);
  }
  const bar = document.createElement('div'); bar.className = 'zoom-bar';
  bar.innerHTML = '<span class="zoom-tag">Quote</span><span class="zoom-space"></span>'
    + '<button type="button" class="side-open-btn" title="Open this quote large">Open</button>'
    + '<button type="button" class="side-draw-btn" title="Highlight or draw on this quote">Draw</button><button type="button" class="side-close">Close</button>';
  bar.querySelector('.zoom-tag').title = text.length > 300 ? text.slice(0, 300) + '\u2026' : text;
  bar.querySelector('.side-open-btn').hidden = !text;
  bar.querySelector('.side-open-btn').addEventListener('click', () => openQuoteView(text));
  bar.querySelector('.side-draw-btn').addEventListener('click', () => openSideDraw(item));
  item.setAttribute('aria-label', 'Quote from the entry');
  item.append(view, bar);
  wireShelfItem(item, bar);
  return item;
}
/* 3D models on the right.
   A model is a binary glTF file (.glb) kept in journal/models, and on the right it goes by "model:<file name>".
   Every model is drawn by one shared WebGL canvas and copied into its own canvas on the right, so however
   many there are, the browser's limit on 3D canvases is never reached. Nothing is drawn until something
   changes (a model is turned, zoomed or resized), so they cost nothing while they're still. */
const isModelRef = n => n.startsWith('model:');
// A book model saved as a draft is kept as "draft:<its code>", and shown until it's made or thrown away.
const isDraftRef = n => n.startsWith('draft:');
const draftSaved = new Map();   // draft code -> when it was last saved here, so its box on the right is redone
const isModelFile = f => /\.(glb|gltf)$/i.test(f.name || '') || f.type === 'model/gltf-binary';
const M3 = {gl:null, canvas:null, prog:null, loc:null, lost:false, failed:false,
  cache:new Map(),    // file name -> {promise, data, gpu}
  states:new Map(),   // file name -> how it's turned: {yaw, pitch, zoom, panX, panY}
  views:new Set(), queued:new Set(), frame:0};
const M3_FOV = 35 * Math.PI / 180;
const M3_START = () => ({yaw:0.55, pitch:0.28, zoom:1, panX:0, panY:0});   // turned to show its left side: a book's spine

/* Small 4x4 matrix helpers (column-major, as WebGL wants them) */
const m4 = {
  id(){ return [1,0,0,0, 0,1,0,0, 0,0,1,0, 0,0,0,1]; },
  mul(a, b){
    const o = new Array(16);
    for (let c = 0; c < 4; c++) for (let r = 0; r < 4; r++) {
      let s = 0; for (let k = 0; k < 4; k++) s += a[k * 4 + r] * b[c * 4 + k];
      o[c * 4 + r] = s;
    }
    return o;
  },
  trs(t, q, s){
    t = t || [0,0,0]; q = q || [0,0,0,1]; s = s || [1,1,1];
    const [x, y, z, w] = q;
    return [(1 - 2*(y*y + z*z)) * s[0], 2*(x*y + z*w) * s[0], 2*(x*z - y*w) * s[0], 0,
            2*(x*y - z*w) * s[1], (1 - 2*(x*x + z*z)) * s[1], 2*(y*z + x*w) * s[1], 0,
            2*(x*z + y*w) * s[2], 2*(y*z - x*w) * s[2], (1 - 2*(x*x + y*y)) * s[2], 0,
            t[0], t[1], t[2], 1];
  },
  // The matrix that turns normals: the inverse of the transpose of the top-left 3x3.
  normal(m){
    const a = m[0], b = m[1], c = m[2], d = m[4], e = m[5], f = m[6], g = m[8], h = m[9], i = m[10];
    const A = e*i - f*h, B = -(d*i - f*g), C = d*h - e*g;
    const det = a*A + b*B + c*C || 1;
    return [A/det, B/det, C/det, -(b*i - c*h)/det, (a*i - c*g)/det, -(a*h - b*g)/det, (b*f - c*e)/det, -(a*f - c*d)/det, (a*e - b*d)/det];
  },
  perspective(fovy, aspect, near, far){
    const f = 1 / Math.tan(fovy / 2), nf = 1 / (near - far);
    return [f / aspect,0,0,0, 0,f,0,0, 0,0,(far + near) * nf,-1, 0,0,2 * far * near * nf,0];
  },
};

/* Reading a .glb file: its meshes, placed where their nodes put them, with their colours and textures.
   The model is then centred and scaled to fit a ball of radius 1, so every model starts off filling its box. */
const GL_COMP = {5120:[1, 'getInt8', 127], 5121:[1, 'getUint8', 255], 5122:[2, 'getInt16', 32767],
                 5123:[2, 'getUint16', 65535], 5125:[4, 'getUint32', 0], 5126:[4, 'getFloat32', 0]};
const GL_SIZE = {SCALAR:1, VEC2:2, VEC3:3, VEC4:4, MAT2:4, MAT3:9, MAT4:16};
const M3_KNOWN = new Set(['KHR_materials_unlit', 'KHR_materials_emissive_strength', 'KHR_materials_specular', 'KHR_materials_ior',
  'KHR_materials_transmission', 'KHR_materials_volume', 'KHR_materials_clearcoat', 'KHR_materials_sheen', 'KHR_texture_transform', 'KHR_mesh_quantization']);
async function parseGlb(buf){
  const dv = new DataView(buf);
  if (buf.byteLength < 20 || dv.getUint32(0, true) !== 0x46546C67 || dv.getUint32(4, true) !== 2) throw new Error('format');
  let off = 12, json = null, bin = null;
  while (off + 8 <= buf.byteLength) {
    const len = dv.getUint32(off, true), type = dv.getUint32(off + 4, true);
    if (off + 8 + len > buf.byteLength) break;
    if (type === 0x4E4F534A && !json) json = JSON.parse(new TextDecoder().decode(new Uint8Array(buf, off + 8, len)));
    else if (type === 0x004E4942 && !bin) bin = new Uint8Array(buf, off + 8, len);
    off += 8 + len;
  }
  if (!json) throw new Error('format');
  if ((json.extensionsRequired || []).some(x => !M3_KNOWN.has(x))) throw new Error('packed');
  const buffers = [];
  for (const b of json.buffers || []) {
    if (!b.uri) buffers.push(bin);
    else if (b.uri.startsWith('data:')) buffers.push(new Uint8Array(await (await fetch(b.uri)).arrayBuffer()));
    else throw new Error('external');
  }
  const views = json.bufferViews || [], accs = json.accessors || [];
  const viewBytes = i => {
    const v = views[i], b = buffers[v.buffer]; if (!b) throw new Error('format');
    return {dv:new DataView(b.buffer, b.byteOffset + (v.byteOffset || 0), v.byteLength), stride:v.byteStride || 0};
  };
  // An accessor's numbers, as floats (normalised ones scaled to 0..1 or -1..1), or as whole numbers for indices.
  const read = (i, whole) => {
    const a = accs[i]; if (!a) return null;
    const [bytes, get, max] = GL_COMP[a.componentType], n = GL_SIZE[a.type];
    const out = whole ? new Uint32Array(a.count * n) : new Float32Array(a.count * n);
    if (a.bufferView !== undefined) {
      const {dv, stride} = viewBytes(a.bufferView), step = stride || bytes * n, base = a.byteOffset || 0;
      const scale = !whole && a.normalized && max ? 1 / max : 1;
      for (let k = 0; k < a.count; k++) for (let j = 0; j < n; j++) {
        const v = dv[get](base + k * step + j * bytes, true) * scale;
        out[k * n + j] = scale !== 1 && v < -1 ? -1 : v;
      }
    }
    if (a.sparse) {
      const s = a.sparse, idx = viewBytes(s.indices.bufferView), val = viewBytes(s.values.bufferView);
      const [ib, ig] = GL_COMP[s.indices.componentType], [vb, vg, vmax] = GL_COMP[a.componentType];
      const scale = !whole && a.normalized && vmax ? 1 / vmax : 1;
      for (let k = 0; k < s.count; k++) {
        const at = idx.dv[ig]((s.indices.byteOffset || 0) + k * ib, true);
        for (let j = 0; j < n; j++) out[at * n + j] = val.dv[vg]((s.values.byteOffset || 0) + (k * n + j) * vb, true) * scale;
      }
    }
    return {data:out, n};
  };
  // Textures become image bitmaps; each is made once however many parts use it.
  const bitmaps = new Map();
  const bitmap = async ti => {
    const t = (json.textures || [])[ti]; if (!t) return null;
    const src = t.source !== undefined ? t.source : t.extensions && Object.values(t.extensions).map(x => x.source).find(x => x !== undefined);
    const img = (json.images || [])[src]; if (!img) return null;
    if (!bitmaps.has(src)) bitmaps.set(src, (async () => {
      let blob;
      if (img.bufferView !== undefined) {
        const {dv} = viewBytes(img.bufferView);
        blob = new Blob([new Uint8Array(dv.buffer, dv.byteOffset, dv.byteLength)], {type:img.mimeType || 'image/png'});
      } else if (img.uri && img.uri.startsWith('data:')) blob = await (await fetch(img.uri)).blob();
      else return null;
      try { return await createImageBitmap(blob, {premultiplyAlpha:'none', colorSpaceConversion:'none'}); } catch (e) { return null; }
    })());
    return bitmaps.get(src);
  };
  const parts = [];
  const addMesh = (mi, world) => {
    const mesh = (json.meshes || [])[mi]; if (!mesh) return;
    const nm = m4.normal(world);
    for (const p of mesh.primitives || []) {
      const mode = p.mode === undefined ? 4 : p.mode;
      if (mode < 4 || p.attributes.POSITION === undefined) continue;   // points and lines aren't shown
      const pos = read(p.attributes.POSITION).data, count = pos.length / 3;
      for (let k = 0; k < pos.length; k += 3) {
        const x = pos[k], y = pos[k + 1], z = pos[k + 2];
        pos[k] = world[0]*x + world[4]*y + world[8]*z + world[12];
        pos[k + 1] = world[1]*x + world[5]*y + world[9]*z + world[13];
        pos[k + 2] = world[2]*x + world[6]*y + world[10]*z + world[14];
      }
      let nrm = p.attributes.NORMAL !== undefined ? read(p.attributes.NORMAL).data : null;
      if (nrm) for (let k = 0; k < nrm.length; k += 3) {
        const x = nrm[k], y = nrm[k + 1], z = nrm[k + 2];
        const a = nm[0]*x + nm[3]*y + nm[6]*z, b = nm[1]*x + nm[4]*y + nm[7]*z, c = nm[2]*x + nm[5]*y + nm[8]*z;
        const l = Math.hypot(a, b, c) || 1; nrm[k] = a / l; nrm[k + 1] = b / l; nrm[k + 2] = c / l;
      }
      let col = null;
      if (p.attributes.COLOR_0 !== undefined) {
        const c = read(p.attributes.COLOR_0);
        if (c.n === 4) col = c.data;
        else { col = new Float32Array(count * 4); for (let k = 0; k < count; k++) { col.set(c.data.subarray(k * 3, k * 3 + 3), k * 4); col[k * 4 + 3] = 1; } }
      }
      const uv = p.attributes.TEXCOORD_0 !== undefined ? read(p.attributes.TEXCOORD_0).data : null;
      let idx = p.indices !== undefined ? read(p.indices, true).data : Uint32Array.from({length:count}, (_, k) => k);
      if (mode === 5 || mode === 6) {   // strips and fans become plain triangles
        const t = [];
        for (let k = 2; k < idx.length; k++) {
          if (mode === 6) t.push(idx[0], idx[k - 1], idx[k]);
          else if (k % 2) t.push(idx[k - 1], idx[k - 2], idx[k]); else t.push(idx[k - 2], idx[k - 1], idx[k]);
        }
        idx = Uint32Array.from(t);
      }
      if (!nrm) nrm = smoothNormals(pos, idx);
      const mat = (json.materials || [])[p.material] || {}, pbr = mat.pbrMetallicRoughness || {};
      parts.push({pos, nrm, col, uv, idx, base:pbr.baseColorFactor || [1, 1, 1, 1],
        tex:pbr.baseColorTexture && uv ? bitmap(pbr.baseColorTexture.index) : null,
        cut:mat.alphaMode === 'MASK' ? (mat.alphaCutoff === undefined ? .5 : mat.alphaCutoff) : 0,
        lit:!(mat.extensions && mat.extensions.KHR_materials_unlit), name:String(mat.name || '')});
    }
  };
  const nodes = json.nodes || [];
  const walk = (ni, parent, seen) => {
    const node = nodes[ni]; if (!node || seen.has(ni)) return;
    seen.add(ni);
    const world = m4.mul(parent, node.matrix || m4.trs(node.translation, node.rotation, node.scale));
    if (node.mesh !== undefined) addMesh(node.mesh, world);
    for (const c of node.children || []) walk(c, world, seen);
  };
  const scene = (json.scenes || [])[json.scene || 0];
  if (scene) { const seen = new Set(); for (const r of scene.nodes || []) walk(r, m4.id(), seen); }
  else if (nodes.length) {
    const children = new Set(nodes.flatMap(n => n.children || [])), seen = new Set();
    nodes.forEach((n, i) => { if (!children.has(i)) walk(i, m4.id(), seen); });
  } else (json.meshes || []).forEach((_, i) => addMesh(i, m4.id()));
  if (!parts.length) throw new Error('empty');
  // Centre it and scale it to fit a ball of radius 1.
  const lo = [Infinity, Infinity, Infinity], hi = [-Infinity, -Infinity, -Infinity];
  for (const p of parts) for (let k = 0; k < p.pos.length; k += 3) for (let j = 0; j < 3; j++) {
    const v = p.pos[k + j]; if (v < lo[j]) lo[j] = v; if (v > hi[j]) hi[j] = v;
  }
  const mid = lo.map((v, j) => (v + hi[j]) / 2);
  let r = 0;
  for (const p of parts) for (let k = 0; k < p.pos.length; k += 3) r = Math.max(r, Math.hypot(p.pos[k] - mid[0], p.pos[k + 1] - mid[1], p.pos[k + 2] - mid[2]));
  r = r || 1;
  for (const p of parts) for (let k = 0; k < p.pos.length; k += 3) for (let j = 0; j < 3; j++) p.pos[k + j] = (p.pos[k + j] - mid[j]) / r;
  for (const p of parts) p.tex = p.tex ? await p.tex : null;
  return parts;
}
// A model saved without normals gets smooth ones worked out from its triangles.
function smoothNormals(pos, idx){
  const n = new Float32Array(pos.length);
  for (let k = 0; k + 2 < idx.length; k += 3) {
    const a = idx[k] * 3, b = idx[k + 1] * 3, c = idx[k + 2] * 3;
    const ux = pos[b] - pos[a], uy = pos[b + 1] - pos[a + 1], uz = pos[b + 2] - pos[a + 2];
    const vx = pos[c] - pos[a], vy = pos[c + 1] - pos[a + 1], vz = pos[c + 2] - pos[a + 2];
    const x = uy * vz - uz * vy, y = uz * vx - ux * vz, z = ux * vy - uy * vx;
    for (const i of [a, b, c]) { n[i] += x; n[i + 1] += y; n[i + 2] += z; }
  }
  for (let k = 0; k < n.length; k += 3) { const l = Math.hypot(n[k], n[k + 1], n[k + 2]) || 1; n[k] /= l; n[k + 1] /= l; n[k + 2] /= l; }
  return n;
}
function loadModel(name){
  let m = M3.cache.get(name);
  if (!m) {
    m = {data:null, gpu:null};
    // "archive/<name>" is a model in the archive; anything else is in journal/models
    m.promise = fetch(name.startsWith('archive/') ? '/archive/models/' + name.slice(8) : '/models/' + name).then(r => { if (!r.ok) throw new Error('missing'); return r.arrayBuffer(); })
      .then(parseGlb).then(d => { m.data = d; return m; });
    m.promise.catch(() => M3.cache.delete(name));   // a failed load is tried again next time it's shown
    M3.cache.set(name, m);
  }
  return m.promise;
}

/* The shared WebGL canvas. Lighting is fixed to the viewer, so the model turns under a steady light:
   a soft light from above, a key light from the upper left, and a faint fill from the right. */
function m3Gl(){
  if (M3.gl) return M3.gl;
  if (M3.lost || M3.failed) return null;
  const c = M3.canvas || (M3.canvas = document.createElement('canvas'));
  const gl = c.getContext('webgl2', {alpha:true, premultipliedAlpha:true, antialias:true, preserveDrawingBuffer:true});
  if (!gl) { M3.failed = true; return null; }
  if (!c.dataset.watched) {
    c.dataset.watched = '1';
    c.addEventListener('webglcontextlost', ev => {
      ev.preventDefault(); M3.lost = true; M3.gl = null;
      for (const m of M3.cache.values()) m.gpu = null;
    });
    c.addEventListener('webglcontextrestored', () => { M3.lost = false; for (const v of M3.views) m3Queue(v); });
  }
  const vs = `#version 300 es
in vec3 aPos; in vec3 aNrm; in vec4 aCol; in vec2 aUv;
uniform mat4 uProj; uniform mat4 uView;
uniform int uSwing; uniform float uSide; uniform vec2 uHinge; uniform vec2 uCS; uniform float uOpen; uniform float uZo; uniform float uLean; uniform vec2 uWin; uniform float uWinH; uniform float uPy1; uniform vec2 uWinU;
uniform float uGap; uniform float uShift; uniform vec2 uUv;
out vec3 vNrm; out vec4 vCol; out vec2 vUv;
void main(){
  vec3 p = aPos, n = aNrm;
  // A book being read: a board (on the uSide side) swings round its hinge, uCS its angle's cosine and sine, and
  // the spine sinks away under the book as it opens (uOpen). Nothing moves with uSwing 0. As the board stands up
  // it looks larger the nearer it comes (uLean), as if seen from close by; the rest of the book stays as it is.
  // (uSwing 4: the back of the book showing between the boards, as wide on the left and the right, uWin, as the
  // reader has it where the book will lie open; its left part goes over with the board it lies on.)
  // As much of its height shows (uWinH) as the reader has showing: above, the boards hide it.
  vec2 uv = vec2(aUv.x * uUv.x + uUv.y, aUv.y);   // (uUv: a picture squeezed across, as the endpaper is by the joint)
  if (uSwing == 4) {
    p.x = uHinge.x + (p.x - uHinge.x) * (p.z > 0.0 ? uWin.x : uWin.y);
    p.y = sign(p.y) * (uPy1 + (abs(p.y) - uPy1) * uWinH); uv.y = 1.0 - (1.0 - aUv.y) * uWinH;
    // its picture, laid across it from where it lies (uWinU: how far left of the gutter its middle is, and half its width)
    uv.x = 0.5 + ((p.z > 0.0 ? -1.0 : 1.0) * (p.x - uHinge.x) + uWinU.x) / (2.0 * uWinU.y);
  }
  // (The board hinges at its joint, uGap out from the back of the pages, so that it swings clear of them; a page
  // lying on it, uSwing 3, slides along it by uShift as it goes, to come down with its edge at the gutter.)
  if (uSwing == 3) p.x += uShift;
  if (uSwing == 3 || ((uSwing == 1 || uSwing == 4) && uSide * p.z > 0.0)) {
    float hx = uHinge.x - uGap, dx = p.x - hx, dz = p.z - uHinge.y;
    p.x = hx + dx * uCS.x - uSide * dz * uCS.y; p.z = uHinge.y + uSide * dx * uCS.y + dz * uCS.x;
    n = vec3(n.x * uCS.x - uSide * n.z * uCS.y, n.y, uSide * n.x * uCS.y + n.z * uCS.x);
    float k = 1.0 + uLean * max(uSide * (p.z - uHinge.y), 0.0);
    p.x = hx + (p.x - hx) * k; p.y *= k;
  } else if (uSwing == 2) p.z = mix(clamp(p.z, -uZo, uZo), -uSide * uZo, uOpen);   // (raised bands kept within the spine's thickness, not up through the joint)
  vNrm = mat3(uView) * n; vCol = aCol; vUv = uv; gl_Position = uProj * uView * vec4(p, 1.0);
}`;
  const fs = `#version 300 es
precision highp float;
in vec3 vNrm; in vec4 vCol; in vec2 vUv;
uniform vec4 uBase; uniform sampler2D uTex; uniform bool uHasTex; uniform float uCut; uniform bool uLit; uniform float uBright; uniform float uLod;
uniform highp int uSwing; uniform highp float uWinH;
out vec4 outColor;
void main(){
  vec4 c = uBase * vCol;
  if (uHasTex) { vec4 t = texture(uTex, vUv, uLod); c *= vec4(pow(t.rgb, vec3(2.2)), t.a); }
  if (c.a < uCut) discard;
  // the back of the book between the boards: in their shadow just under their edge (see rdSpine)
  vec3 n = normalize(vNrm); if (!gl_FrontFacing) n = -n;
  vec3 light = vec3(1.0);
  if (uLit) {
    float sky = 0.5 + 0.5 * n.y;
    light = vec3(0.34) * mix(0.55, 1.0, sky)
          + vec3(0.88) * max(dot(n, normalize(vec3(-0.45, 0.7, 0.55))), 0.0)
          + vec3(0.26) * max(dot(n, normalize(vec3(0.7, 0.1, 0.35))), 0.0);
    light *= 1.0 + uBright;
  }
  outColor = vec4(pow(c.rgb * light, vec3(1.0 / 2.2)), 1.0);
}`;
  const sh = (type, src) => { const s = gl.createShader(type); gl.shaderSource(s, src); gl.compileShader(s); return s; };
  const prog = gl.createProgram();
  gl.attachShader(prog, sh(gl.VERTEX_SHADER, vs)); gl.attachShader(prog, sh(gl.FRAGMENT_SHADER, fs));
  gl.bindAttribLocation(prog, 0, 'aPos'); gl.bindAttribLocation(prog, 1, 'aNrm');
  gl.bindAttribLocation(prog, 2, 'aCol'); gl.bindAttribLocation(prog, 3, 'aUv');
  gl.linkProgram(prog);
  if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) { M3.failed = true; return null; }
  M3.prog = prog;
  M3.loc = Object.fromEntries(['uProj', 'uView', 'uBase', 'uTex', 'uHasTex', 'uCut', 'uLit', 'uBright', 'uSwing', 'uSide', 'uHinge', 'uCS', 'uOpen', 'uZo', 'uLean', 'uWin', 'uWinH', 'uPy1', 'uWinU', 'uGap', 'uShift', 'uUv', 'uLod']
    .map(u => [u, gl.getUniformLocation(prog, u)]));
  M3.gl = gl;
  return gl;
}
// A model's triangles, handed to the graphics card the first time it's drawn.
// A part's triangles, each wound so that its front is the side its normals face (as the open book's are: obMesh). The
// shader lights the side of a triangle that faces the viewer, turning its normal round when that's the back; a part
// whose triangles are wound the other way round from its normals (as the spine of the journal's book models is) would
// be lit as if from behind, darker than the open book, which is made from the same normals, shows it.
function m3Wound(p){
  const P = p.pos, Nn = p.nrm, I = p.idx;
  if (!P || !Nn || !I) return I;
  const out = I.slice();
  for (let t = 0; t + 2 < out.length; t += 3) {
    const a = out[t], b = out[t + 1], c = out[t + 2];
    const e1 = [0, 1, 2].map(j => P[3 * b + j] - P[3 * a + j]), e2 = [0, 1, 2].map(j => P[3 * c + j] - P[3 * a + j]);
    const cr = [e1[1] * e2[2] - e1[2] * e2[1], e1[2] * e2[0] - e1[0] * e2[2], e1[0] * e2[1] - e1[1] * e2[0]];
    let dot = 0; for (const i of [a, b, c]) for (let j = 0; j < 3; j++) dot += cr[j] * Nn[3 * i + j];
    if (dot < 0) { out[t + 1] = c; out[t + 2] = b; }
  }
  return out;
}
function m3Gpu(gl, m){
  if (m.gpu) return m.gpu;
  const textures = new Map(), made = m.made = [];   // everything made on the graphics card, so it can be freed
  m.gpu = m.data.map(p => {
    const vao = gl.createVertexArray(); gl.bindVertexArray(vao); made.push(['VertexArray', vao]);
    const attr = (loc, data, size, fallback) => {
      if (!data) { gl.disableVertexAttribArray(loc); gl.vertexAttrib4f(loc, ...fallback); return; }
      const b = gl.createBuffer(); made.push(['Buffer', b]); gl.bindBuffer(gl.ARRAY_BUFFER, b); gl.bufferData(gl.ARRAY_BUFFER, data, gl.STATIC_DRAW);
      gl.enableVertexAttribArray(loc); gl.vertexAttribPointer(loc, size, gl.FLOAT, false, 0, 0);
    };
    attr(0, p.pos, 3); attr(1, p.nrm, 3); attr(2, p.col, 4, [1, 1, 1, 1]); attr(3, p.uv, 2, [0, 0, 0, 0]);
    const ib = gl.createBuffer(); made.push(['Buffer', ib]); gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, ib); gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, m3Wound(p), gl.STATIC_DRAW);
    gl.bindVertexArray(null);
    let tex = null;
    if (p.tex) {
      tex = textures.get(p.tex);
      if (!tex) {
        tex = gl.createTexture(); made.push(['Texture', tex]); gl.bindTexture(gl.TEXTURE_2D, tex);
        gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, false); gl.pixelStorei(gl.UNPACK_PREMULTIPLY_ALPHA_WEBGL, false);
        gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, p.tex);
        gl.generateMipmap(gl.TEXTURE_2D);
        gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR_MIPMAP_LINEAR);
        gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
        textures.set(p.tex, tex);
      }
    }
    return {vao, count:p.idx.length, tex, base:p.base, cut:p.cut, lit:p.lit, name:p.name};
  });
  return m.gpu;
}
// A model made in the page (the book being built) rather than loaded from a file: shown as soon as it's set,
// replacing whatever was shown under that name before (null takes it away).
function m3SetPreview(name, data){
  const old = M3.cache.get(name);
  if (old && old.made && M3.gl) for (const [kind, obj] of old.made) M3.gl['delete' + kind](obj);
  if (!data) { M3.cache.delete(name); return; }
  const m = {data, gpu:null}; m.promise = Promise.resolve(m);
  M3.cache.set(name, m);
  m3Redraw(name);
}
function m3State(name){
  if (!M3.states.has(name)) M3.states.set(name, M3_START());
  return M3.states.get(name);
}
// Draws one view: the model is drawn on the shared canvas at this view's size, then copied into its own canvas.
function m3Draw(v){
  const m = M3.cache.get(v.name), cv = v.canvas;
  if (!m || !m.data || !cv.isConnected) return;
  const gl = m3Gl();
  if (!gl) { v.say(M3.failed ? "This browser can't show 3D models (WebGL 2 is turned off or missing)." : ''); return; }
  const dpr = Math.min(window.devicePixelRatio || 1, 2);
  const W = Math.max(1, Math.round(cv.clientWidth * dpr)), H = Math.max(1, Math.round(cv.clientHeight * dpr));
  if (cv.width !== W || cv.height !== H) { cv.width = W; cv.height = H; }
  const g = M3.canvas; if (g.width !== W || g.height !== H) { g.width = W; g.height = H; }
  const s = m3State(v.name), aspect = W / H;
  // A journal book can be shown open (v.open, 0 closed to 1 lying open): its front board swings over round the
  // spine, and it's looked at from far enough off, and round the middle of the open book, for it all to fit.
  const bo = v.open || 0, bd = bo > 0 ? (m.dims === undefined ? (m.dims = bookDims(m.data)) : m.dims) : null;
  // (the view following the board: moving as it moves, and still once it lies down)
  const bm = (1 - Math.cos(Math.PI * bo)) / 2;
  const grow = bd ? 1 + (Math.max(1, Math.hypot(bd.xr - bd.xl, bd.top, bd.zo)) - 1) * bm : 1, cx = bd ? bd.xl * bm : 0;
  // Near enough that the whole model just fits, whichever way the box is longer.
  const half = Math.min(M3_FOV / 2, Math.atan(Math.tan(M3_FOV / 2) * aspect));
  const dist = 1.06 * grow / Math.sin(half) / s.zoom;
  const cy = Math.cos(s.yaw), sy = Math.sin(s.yaw), cp = Math.cos(s.pitch), sp = Math.sin(s.pitch);
  const rotY = [cy,0,-sy,0, 0,1,0,0, sy,0,cy,0, 0,0,0,1], rotX = [1,0,0,0, 0,cp,sp,0, 0,-sp,cp,0, 0,0,0,1];
  const view = m4.mul(m4.trs([s.panX, s.panY, -dist]), m4.mul(m4.mul(rotX, rotY), m4.trs([-cx, 0, 0])));
  gl.viewport(0, 0, W, H);
  gl.clearColor(0, 0, 0, 0); gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
  gl.enable(gl.DEPTH_TEST); gl.disable(gl.CULL_FACE); gl.disable(gl.BLEND);
  gl.useProgram(M3.prog);
  const L = M3.loc; gl.uniform2f(L.uUv, 1, 0);
  gl.uniform1i(L.uSwing, 0); gl.uniform1f(L.uBright, 0);   // as it is, under the usual light (a book being read changes these)
  if (bd) {
    gl.uniform1f(L.uSide, 1); gl.uniform2f(L.uHinge, bd.xl, bd.zi); gl.uniform2f(L.uCS, Math.cos(Math.PI * bo), Math.sin(Math.PI * bo));
    gl.uniform1f(L.uOpen, bo); gl.uniform1f(L.uZo, bd.zo); gl.uniform1f(L.uLean, 0); gl.uniform2f(L.uWin, 2, 2); gl.uniform1f(L.uWinH, 1); gl.uniform1f(L.uPy1, bd.py1); gl.uniform2f(L.uWinU, 0, 2 * (bd.top - bd.py1));
    gl.uniform1f(L.uGap, 0); gl.uniform1f(L.uShift, 0);
  }
  gl.uniformMatrix4fv(L.uProj, false, m4.perspective(M3_FOV, aspect, Math.max(0.01, dist - 1.5 * grow - Math.hypot(s.panX, s.panY)), dist + 3 * grow));
  gl.uniformMatrix4fv(L.uView, false, view);
  gl.uniform1i(L.uTex, 0); gl.uniform1f(L.uLod, 0);
  for (const p of m3Gpu(gl, m)) {
    if (p.name === 'spineWindow' && !bd) continue;   // (only for a book shown open; shut, it's a picture lying where nothing shows it)
    if (bd) gl.uniform1i(L.uSwing, p.name === 'spineWindow' ? 4 : RD3_BOARD.has(p.name) ? 1 : RD3_SPINE.has(p.name) ? 2 : 0);
    gl.uniform4fv(L.uBase, p.base); gl.uniform1f(L.uCut, p.cut); gl.uniform1i(L.uLit, p.lit ? 1 : 0);
    gl.uniform1i(L.uHasTex, p.tex ? 1 : 0);
    gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, p.tex);
    gl.bindVertexArray(p.vao);
    gl.drawElements(gl.TRIANGLES, p.count, gl.UNSIGNED_INT, 0);
  }
  gl.bindVertexArray(null); gl.uniform1i(L.uSwing, 0);
  v.ctx.clearRect(0, 0, W, H);
  v.ctx.drawImage(g, 0, 0);
}
// Drawing waits for the next frame, and a view asked for several times in one frame is drawn once.
function m3Queue(v){
  M3.queued.add(v);
  if (!M3.frame) M3.frame = requestAnimationFrame(() => {
    M3.frame = 0;
    const list = [...M3.queued]; M3.queued.clear();
    for (const x of list) {
      if (!x.canvas.isConnected) { M3.views.delete(x); m3Resize.unobserve(x.canvas); continue; }
      m3Draw(x);
    }
  });
}
// Everything showing this model (on the right and in the large view) follows it as it's turned.
function m3Redraw(name){ for (const v of M3.views) if (v.name === name) m3Queue(v); }
const m3Resize = new ResizeObserver(list => {
  for (const r of list) { const v = [...M3.views].find(x => x.canvas === r.target); if (v) m3Queue(v); }
});
// A view of a model in a canvas: turned by dragging, moved sideways with Shift (or the right button),
// zoomed with Ctrl and the scroll wheel or a pinch (or the plain wheel where wheelZooms is set),
// and put back as it was by a double-click. With the keyboard: arrows turn it, + and - zoom, 0 puts it back.
function m3View(canvas, name, note, wheelZooms, preview){
  const v = {canvas, name, ctx:canvas.getContext('2d'), say(text){ note.textContent = text; note.hidden = !text; }};
  canvas.tabIndex = 0;
  let drag = null;
  canvas.addEventListener('pointerdown', ev => {
    if (ev.button !== 0 && ev.button !== 2) return;
    ev.preventDefault(); ev.stopPropagation();
    canvas.setPointerCapture(ev.pointerId);
    drag = {id:ev.pointerId, x:ev.clientX, y:ev.clientY, pan:ev.shiftKey || ev.button === 2};
    canvas.classList.add('turning');
  });
  canvas.addEventListener('pointermove', ev => {
    if (!drag || ev.pointerId !== drag.id) return;
    const dx = ev.clientX - drag.x, dy = ev.clientY - drag.y, s = m3State(name);
    drag.x = ev.clientX; drag.y = ev.clientY;
    if (drag.pan) {
      const aspect = canvas.clientWidth / Math.max(1, canvas.clientHeight);
      const half = Math.min(M3_FOV / 2, Math.atan(Math.tan(M3_FOV / 2) * aspect));
      const per = 2 * (1.06 / Math.sin(half) / s.zoom) * Math.tan(M3_FOV / 2) / Math.max(1, canvas.clientHeight);
      s.panX += dx * per; s.panY -= dy * per;
    } else {
      s.yaw += dx * 0.01;
      s.pitch = Math.max(-1.55, Math.min(1.55, s.pitch + dy * 0.01));
    }
    m3Redraw(name);
  });
  const stop = ev => { if (drag && ev.pointerId === drag.id) { drag = null; canvas.classList.remove('turning'); } };
  canvas.addEventListener('pointerup', stop); canvas.addEventListener('pointercancel', stop);
  canvas.addEventListener('contextmenu', ev => ev.preventDefault());
  canvas.addEventListener('wheel', ev => {
    if (!ev.ctrlKey && !wheelZooms) return;   // on the right, the plain wheel keeps scrolling past it
    ev.preventDefault(); ev.stopPropagation();
    const dy = ev.deltaY * (ev.deltaMode === 1 ? 16 : ev.deltaMode === 2 ? 400 : 1);
    const s = m3State(name); s.zoom = Math.max(0.3, Math.min(12, s.zoom * Math.exp(-dy * 0.0025)));
    m3Redraw(name);
  }, {passive:false});
  canvas.addEventListener('dblclick', ev => { ev.preventDefault(); M3.states.set(name, M3_START()); m3Redraw(name); });
  canvas.addEventListener('keydown', ev => {
    if (ev.altKey || ev.ctrlKey || ev.metaKey) return;   // Alt+arrows move it to another place on the right
    const s = m3State(name), k = ev.key;
    if (k === 'ArrowLeft') s.yaw -= 0.15; else if (k === 'ArrowRight') s.yaw += 0.15;
    else if (k === 'ArrowUp') s.pitch = Math.max(-1.55, s.pitch - 0.15); else if (k === 'ArrowDown') s.pitch = Math.min(1.55, s.pitch + 0.15);
    else if (k === '+' || k === '=') s.zoom = Math.min(12, s.zoom * 1.2); else if (k === '-' || k === '_') s.zoom = Math.max(0.3, s.zoom / 1.2);
    else if (k === '0' || k === 'Home') M3.states.set(name, M3_START());
    else return;
    ev.preventDefault(); m3Redraw(name);
  });
  M3.views.add(v); m3Resize.observe(canvas);
  if (preview) return v;   // its model is set with m3SetPreview
  v.say('Loading the model\u2026');
  loadModel(name).then(() => { v.say(''); m3Queue(v); }, err => v.say(
    err.message === 'missing' ? "This model's file isn't in journal/models any more."
    : err.message === 'packed' ? "This model is compressed in a way the journal can't read (such as Draco). Save it again without compression."
    : err.message === 'external' ? 'This model keeps its data in separate files. Pack it into a single .glb file.'
    : err.message === 'empty' ? 'This model has nothing in it to show.'
    : "This file couldn't be read as a 3D model."));
  return v;
}
const m3PreviewView = (canvas, name, note) => m3View(canvas, name, note, true, true);
// A model on the right.
function shelfModelItem(ref){
  const name = ref.slice(6);
  const item = document.createElement('div'); item.className = 'shelf-item shelf-model'; item.dataset.name = ref;
  const canvas = document.createElement('canvas'); canvas.className = 'model-canvas';
  canvas.setAttribute('aria-label', '3D model. Drag to turn it, Ctrl and scroll to zoom, double-click to put it back as it was');
  const note = document.createElement('div'); note.className = 'model-note';
  const bar = document.createElement('div'); bar.className = 'zoom-bar';
  bar.innerHTML = '<span class="zoom-tag" title="Drag here to move it to another place">3D model</span><span class="zoom-space"></span>'
    + '<button type="button" class="side-open-btn" title="Show this model large (to archive it or delete it too)">Open</button>'
    + '<button type="button" class="side-close" title="Take it off the right (the model is kept)">Close</button>';
  item.append(canvas, note, bar);
  m3View(canvas, name, note, false);
  bar.querySelector('.side-open-btn').addEventListener('click', () => openModelView(name));
  item.setAttribute('aria-label', '3D model');
  // Made into a book with a PDF: it's called by the PDF's title, and can be read.
  const e = entries.get(currentId), pdf = bookPdf(e, name);
  if (pdf) {
    const title = pdfTitleIn(e.body, pdf) || 'Book', tag = bar.querySelector('.zoom-tag');
    tag.textContent = title; tag.title = title + ' (a book: Read opens it)\nDrag here to move it to another place';
    const read = document.createElement('button'); read.type = 'button'; read.className = 'side-read-btn';
    read.textContent = 'Read'; read.title = 'Open the book and read it';
    read.addEventListener('click', () => readBook(name, canvas));
    bar.querySelector('.side-open-btn').before(read);
    // The page reader got ready beforehand, when nothing else is happening, rather than while the book rises.
    if (!pdfjsLib) (window.requestIdleCallback || setTimeout)(() => loadPdfjs().catch(() => {}), {timeout:4000});
    item.classList.add('shelf-book'); item.setAttribute('aria-label', 'Book: ' + title);
  }
  wireShelfItem(item, bar);
  return item;
}
// A book model saved as a draft, on the right: its front cover (faded), and Continue to carry on making it.
function shelfDraftItem(ref){
  const code = ref.slice(6);
  const item = document.createElement('div'); item.className = 'shelf-item shelf-draft'; item.dataset.name = ref;
  const img = document.createElement('img'); img.draggable = false; img.alt = 'Book model draft'; img.hidden = true;
  const note = document.createElement('div'); note.className = 'model-note'; note.textContent = 'Loading the draft\u2026';
  const bar = document.createElement('div'); bar.className = 'zoom-bar';
  bar.innerHTML = '<span class="zoom-tag" title="Drag here to move it to another place">Book draft</span><span class="zoom-space"></span>'
    + '<button type="button" class="side-open-btn" title="Carry on making this book model">Continue</button>';
  item.append(img, note, bar);
  item.setAttribute('aria-label', 'Book model draft');
  const go = bar.querySelector('.side-open-btn');
  go.addEventListener('click', () => openBookDraft(code));
  fetch('/api/book-drafts/' + code, {headers:H}).then(r => {
    if (r.status === 404) throw new Error('missing');
    if (!r.ok) throw new Error();
    return r.json();
  }).then(d => {
    const front = d.faces && d.faces.front && d.faces.front.pic;
    if (front && IMG_NAME.test(front)) { img.src = '/images/' + front; img.hidden = false; note.textContent = ''; note.hidden = true; }
    else note.textContent = 'A book model draft, with no front cover yet.';
  }, err => {
    go.remove();
    note.textContent = err.message === 'missing' ? "This draft isn't in journal/book drafts any more." : "Couldn't read this draft. Check that the journal server is still running.";
    if (err.message === 'missing') {   // nothing left to carry on with: it can only be taken off
      const close = document.createElement('button'); close.type = 'button'; close.className = 'side-close'; close.textContent = 'Close';
      bar.append(close);
      close.addEventListener('click', () => {
        const e = entries.get(currentId); if (!e) return;
        e.side = shelfNames(e).filter(n => n !== ref); markChanged(currentId); renderShelf();
      });
    }
  });
  wireShelfItem(item, bar);
  return item;
}
// Open: the model large, where the plain scroll wheel zooms. It stays turned however it was left.
let bigModel = null;
function openModelView(name){
  const dlg = $('modelViewer'), old = $('modelCanvas');
  const canvas = old.cloneNode(false); old.replaceWith(canvas);   // a fresh canvas, so no earlier model's handlers linger
  if (bigModel) M3.views.delete(bigModel);
  bigModel = m3View(canvas, name, $('modelNote'), true);
  const inArchive = name.startsWith('archive/');   // an archived model has its own buttons in the Archive
  $('modelArchive').hidden = $('modelForever').hidden = inArchive;
  $('modelArchive').disabled = false; disarm($('modelForever'), 'Delete forever');
  const bound = !inArchive && !!bookPdf(entries.get(currentId), name);
  $('modelRead').hidden = $('modelUnbind').hidden = !bound;
  dlg.showModal();
  canvas.focus({preventScroll:true});
}
$('modelClose').addEventListener('click', () => $('modelViewer').close());
$('modelRead').addEventListener('click', () => { if (bigModel) readBook(bigModel.name, bigModel.canvas); });
$('modelUnbind').addEventListener('click', () => { if (bigModel) { unbindBook(bigModel.name); $('modelRead').hidden = $('modelUnbind').hidden = true; } });
$('modelArchive').addEventListener('click', async () => {
  if (!bigModel) return;
  $('modelArchive').disabled = true;
  if (await archiveModel(bigModel.name)) $('modelViewer').close(); else $('modelArchive').disabled = false;
});
$('modelForever').addEventListener('click', async () => {
  if (bigModel && await eraseModel(bigModel.name, $('modelForever'))) $('modelViewer').close();
});
$('modelReset').addEventListener('click', () => { if (bigModel) { M3.states.set(bigModel.name, M3_START()); m3Redraw(bigModel.name); } });
$('modelViewer').addEventListener('click', ev => { if (ev.target === $('modelViewer')) $('modelViewer').close(); });
$('modelViewer').addEventListener('close', () => { if (bigModel) { M3.views.delete(bigModel); m3Resize.unobserve(bigModel.canvas); bigModel = null; } });
// Models dropped on the entry or picked with the attach button go onto the right of the entry.
async function addModels(files){
  const id = currentId; let problem = '';
  setStatus(files.length === 1 ? 'Adding 3D model\u2026' : 'Adding ' + files.length + ' 3D models\u2026');
  for (const f of files) {
    try {
      if (/\.gltf$/i.test(f.name || '')) throw new Error('gltf');
      const name = await store.uploadModel(f), e = entries.get(id);
      if (!e) continue;
      if (id === currentId) addToShelf('model:' + name);
      else { e.side = shelfNames(e).concat('model:' + name); markChanged(id); }
    } catch (err) {
      problem = err.message === 'gltf' ? f.name + ' is a .gltf file, which keeps its parts in separate files. Save it as a single .glb file (Blender can) and add that.'
        : err.message === 'type' ? f.name + " isn't a .glb 3D model the journal can read."
        : err.message === 'size' ? f.name + ' is too large (the limit is 200 MB).'
        : "Couldn't add " + f.name + '. Check that the journal server is still running.';
    }
  }
  if (id === currentId && problem) setStatus(problem, true);
}
function wireShelfItem(item, bar){
  item.addEventListener('pointerdown', ev => {
    // In a linked entry, pressing on its scrollbar scrolls it rather than moving it.
    if (ev.target.closest && ev.target.closest('.model-canvas')) return;   // a model is turned by dragging it, and moved by its title
    const v = ev.target.closest && ev.target.closest('.shelf-entry-view');
    if (v && ev.clientX > v.getBoundingClientRect().left + v.clientWidth) return;
    startShelfDrag(ev, item);
  });
  // With its Draw or Close button focused, Alt+Left / Alt+Right moves the picture by one place,
  // and Alt+Up / Alt+Down by one row (the same thing, when there's one picture to a row).
  item.addEventListener('keydown', ev => {
    const steps = {ArrowLeft:-1, ArrowRight:1, ArrowUp:-shelfPerRow(), ArrowDown:shelfPerRow()};
    if (!ev.altKey || !(ev.key in steps) || item.classList.contains('drawing')) return;
    ev.preventDefault(); stepShelfItem(item, steps[ev.key]);
  });
  const close = bar.querySelector('.side-close');
  if (close) close.addEventListener('click', () => {
    const e = entries.get(currentId); if (!e || !item.parentElement) return;
    const i = [...item.parentElement.children].indexOf(item);
    const list = shelfNames(e); list.splice(i, 1); e.side = list;
    markChanged(currentId); renderShelf();
  });
}
// What the pictures on the right are showing: when this changes, they're rebuilt.
function shelfKey(e){
  return (currentId || '') + '|' + shelfNames(e).map(n => {
    if (isQuoteRef(n)) return n + '~' + JSON.stringify(inkRec(e, inkKey(n)) || '');
    if (n.startsWith('model:')) { const pdf = bookPdf(e, n.slice(6)); return n + (pdf ? '>' + pdf + '=' + pdfTitleIn(e.body, pdf) : ''); }
    if (isDraftRef(n)) return n + '@' + (draftSaved.get(n.slice(6)) || '');
    if (isPdfRef(n)) return n + '=' + pdfTitleIn(e.body, n.slice(4));
    if (!isEntryRef(n)) return n + '=' + titleIn(e.body, n);
    const linked = entries.get(n.slice(6)), ink = JSON.stringify(inkRec(e, n.slice(6)) || '');
    return n + '=' + (linked ? linked.title + '@' + linked.updated : '') + '~' + ink;
  }).join('\u0001');
}
function renderShelf(){
  const shelf = $('shelf'), pics = $('shelfPics'), e = currentId ? entries.get(currentId) : null;
  const names = shelfNames(e);
  const key = shelfKey(e);
  if (shelf.dataset.key !== key) {
    const sameEntry = (shelf.dataset.key || '').split('|')[0] === (currentId || '');
    shelf.dataset.key = key;
    // A picture being drawn on stays just as it is while it's still here; otherwise its drawing is saved first.
    const keep = side.active && side.id === currentId && names.includes(side.key) ? side.item : null;
    if (side.active && !keep) finishSideDraw();
    let kept = false;
    pics.replaceChildren(...names.map(n => {
      if (keep && !kept && n === side.key) { kept = true; if (side.kind === 'picture') titleShelfItem(keep, n); return keep; }
      return shelfItem(n);
    }));
    if (!sameEntry) {
      shelf.scrollTop = 0;
      if (zoom.frozen) unfreezeZoom();   // a frozen view belongs to the entry it was taken from
    }
  }
  if (shelfEcho) echoShelf(shelfEcho);   // the pictures were rebuilt: keep the glow on the one being hovered
  layoutShelf();
}
// Hovering a picture, a linked entry or a quote in the writing that is also on the right makes it glow there.
var shelfEcho = null;   // var, so renderShelf can read it even if it runs before this line
function echoShelf(name){
  shelfEcho = name;
  for (const el of $('shelfPics').children) el.classList.toggle('echo', !!name && el.dataset.name === name);
}
function shelfNameOf(el){
  if (el.classList.contains('elink')) return el.dataset.link ? 'entry:' + el.dataset.link : null;
  if (el.classList.contains('epdf')) return el.dataset.pdf ? 'pdf:' + el.dataset.pdf : null;
  if (el.classList.contains('quote')) { const t = el.querySelector('.quote-text'); return t ? 'quote:' + quoteCode(t.textContent) : null; }
  return el.dataset.name || null;
}
els.body.addEventListener('pointerover', ev => {
  const el = ev.target.closest ? ev.target.closest('.elink, .fig, .quote') : null;
  const name = el && els.body.contains(el) ? shelfNameOf(el) : null;
  if (name !== shelfEcho) echoShelf(name);
});
els.body.addEventListener('pointerleave', () => { if (shelfEcho) echoShelf(null); });
function addToShelf(name){
  const e = entries.get(currentId); if (!e) return;
  if ((isReadRef(name) || isPdfRef(name)) && shelfNames(e).includes(name)) {   // a linked entry, quote or PDF is shown on the right only once
    const there = [...$('shelfPics').children].find(el => el.dataset.name === name);
    if (there) there.scrollIntoView({block:'nearest'});
    return;
  }
  e.side = shelfNames(e).concat(name);
  markChanged(currentId); renderShelf();
  const last = $('shelfPics').lastElementChild;
  if (last) last.scrollIntoView({block:'nearest'});
}
els.scroll.addEventListener('scroll', layoutShelf);
// Scrolling over the right-hand side. A linked entry with more text than fits scrolls first, to the end of
// its text (or back to the start, scrolling up), and whatever's left of the scroll carries straight on down
// the right-hand side to the next picture or entry. An entry that fits in its box is scrolled past like a picture.
$('shelf').addEventListener('wheel', ev => {
  if (ev.ctrlKey || Math.abs(ev.deltaX) > Math.abs(ev.deltaY)) return;   // zooming the page, or scrolling sideways
  const shelf = $('shelf');
  let dy = ev.deltaY * (ev.deltaMode === 1 ? 16 : ev.deltaMode === 2 ? shelf.clientHeight : 1);
  if (!dy) return;
  ev.preventDefault();
  const view = ev.target.closest ? ev.target.closest('.shelf-entry-view') : null;
  if (view && view.scrollHeight > view.clientHeight + 1) {
    const before = view.scrollTop;
    view.scrollTop = Math.max(0, Math.min(view.scrollHeight - view.clientHeight, before + dy));
    dy -= view.scrollTop - before;
    if (Math.abs(dy) < 1) return;
  }
  shelf.scrollTop += dy;
}, {passive:false});
window.addEventListener('resize', layoutShelf);

/* Moving pictures about on the right.
   Drag one by the picture: the others slide aside to show where it will land, and the space scrolls
   when you hold it near the top or bottom. The new order is saved in the entry's "side:" line. */
let shelfDrag = null;
// The order on screen becomes the order in the entry.
function commitShelfOrder(){
  const e = currentId ? entries.get(currentId) : null; if (!e) return;
  e.side = [...$('shelfPics').children].map(el => el.dataset.name);
  $('shelf').dataset.key = shelfKey(e);   // already showing this order: nothing to rebuild
  markChanged(currentId);
}
// How many pictures sit in the first row.
function shelfPerRow(){
  const list = [...$('shelfPics').children]; if (!list.length) return 1;
  const top = list[0].offsetTop;
  return Math.max(1, list.filter(el => Math.abs(el.offsetTop - top) < 2).length);
}
// Moves a picture by some number of places (negative is towards the start).
function stepShelfItem(item, by){
  const pics = $('shelfPics'), list = [...pics.children];
  const from = list.indexOf(item), to = Math.max(0, Math.min(list.length - 1, from + by));
  if (from < 0 || to === from) return;
  const focused = document.activeElement;
  pics.insertBefore(item, to > from ? list[to].nextElementSibling : list[to]);
  if (focused && item.contains(focused)) focused.focus({preventScroll:true});
  item.scrollIntoView({block:'nearest'});
  commitShelfOrder();
}
function startShelfDrag(ev, item){
  if (ev.button !== 0 || ev.pointerType === 'touch' || shelfDrag) return;   // touch keeps scrolling the space
  if (ev.target.closest('button, .side-draw') || item.classList.contains('drawing') || item.classList.contains('inked')) return;
  const pics = $('shelfPics'), list = [...pics.children];
  if (list.length < 2 || pics.querySelector('.inked')) return;   // not while a picture is open out for drawing
  ev.preventDefault();
  const shelf = $('shelf');
  shelfDrag = {item, list, from:list.indexOf(item), to:list.indexOf(item),
    slots:list.map(el => ({x:el.offsetLeft, y:el.offsetTop})),
    x0:ev.clientX, y0:ev.clientY + shelf.scrollTop, x:ev.clientX, y:ev.clientY, cx:ev.clientX, cy:ev.clientY, started:false, raf:0};
  window.addEventListener('pointermove', moveShelfDrag);
  window.addEventListener('pointerup', endShelfDrag);
  window.addEventListener('pointercancel', endShelfDrag);
}
function moveShelfDrag(ev){
  const d = shelfDrag; if (!d) return;
  d.cx = ev.clientX; d.cy = ev.clientY;
  if (d.started || Math.hypot(d.cx - d.x, d.cy - d.y) < 4) return;
  d.started = true;
  d.item.classList.add('lifted'); document.body.classList.add('moving');
  for (const el of d.list) if (el !== d.item) el.classList.add('shifting');
  d.raf = requestAnimationFrame(shelfDragFrame);
}
function shelfDragFrame(){
  const d = shelfDrag; if (!d || !d.started) return;
  const shelf = $('shelf'), r = shelf.getBoundingClientRect(), edge = 50;
  if (d.cy < r.top + edge) shelf.scrollTop -= Math.ceil((r.top + edge - d.cy) / 4);
  else if (d.cy > r.bottom - edge) shelf.scrollTop += Math.ceil((d.cy - (r.bottom - edge)) / 4);
  // The picture follows the pointer; its place is the slot it's nearest to.
  const dx = d.cx - d.x0, dy = d.cy + shelf.scrollTop - d.y0, s = d.slots, here = s[d.from];
  const px = here.x + dx, py = here.y + dy;
  let to = 0, best = Infinity;
  s.forEach((slot, i) => { const dist = Math.hypot(slot.x - px, slot.y - py); if (dist < best) { best = dist; to = i; } });
  d.item.style.transform = 'translate(' + dx + 'px,' + dy + 'px)';
  if (to !== d.to) {
    d.to = to;
    d.list.forEach((el, i) => {
      if (el === d.item) return;
      const j = d.from < to && i > d.from && i <= to ? i - 1 : d.from > to && i >= to && i < d.from ? i + 1 : i;
      el.style.transform = j !== i ? 'translate(' + (s[j].x - s[i].x) + 'px,' + (s[j].y - s[i].y) + 'px)' : '';
    });
  }
  d.raf = requestAnimationFrame(shelfDragFrame);
}
function endShelfDrag(){
  const d = shelfDrag; if (!d) return;
  shelfDrag = null;
  cancelAnimationFrame(d.raf);
  window.removeEventListener('pointermove', moveShelfDrag);
  window.removeEventListener('pointerup', endShelfDrag);
  window.removeEventListener('pointercancel', endShelfDrag);
  if (!d.started) return;
  document.body.classList.remove('moving');
  const {item, list, from, to} = d, pics = $('shelfPics');
  const was = item.getBoundingClientRect();
  // Put everything in its new place, then let the dropped picture glide the last bit into its slot.
  for (const el of list) { el.classList.remove('shifting'); el.style.transform = ''; }
  if (to !== from && item.parentElement === pics) pics.insertBefore(item, to > from ? list[to].nextElementSibling : list[to]);
  const now = item.getBoundingClientRect(), ox = was.left - now.left, oy = was.top - now.top;
  const settle = () => item.classList.remove('lifted');
  if ((ox || oy) && !calm()) item.animate([{transform:'translate(' + ox + 'px,' + oy + 'px)'}, {transform:'none'}],
    {duration:180, easing:'cubic-bezier(.2,.7,.2,1)'}).finished.then(settle, settle);
  else settle();
  if (to !== from) commitShelfOrder();
}

/* Dropping a picture from the entry into the space on the right */
const zoomDrop = document.createElement('div'); zoomDrop.className = 'zoom-drop'; zoomDrop.hidden = true;
document.body.append(zoomDrop);
function sideDrop(x, y){
  const box = shelfBox(); if (!box) return null;
  const m = els.main.getBoundingClientRect();
  if (x < box.left - 16 || x > m.left + els.main.clientWidth || y < m.top || y > m.bottom) return null;
  return box;
}
function showSideDrop(box){
  zoomDrop.hidden = !box;
  if (box) Object.assign(zoomDrop.style, {left:box.left + 'px', top:box.top + 'px', width:box.w + 'px', height:box.h + 'px'});
}

/* Saving a frozen frame as a picture */
// The frame is drawn onto a canvas by wrapping a copy of it in an SVG image, so it looks just as it does on screen.
let embeddedFontCss = null;
async function embeddedFonts(){
  // The writing font comes from Google Fonts when online; its files are built into the picture.
  // Offline, the picture uses the same fallback font the page does.
  if (embeddedFontCss !== null) return embeddedFontCss;
  try {
    const link = document.querySelector('link[href*="fonts.googleapis"]');
    let css = await (await fetch(link.href)).text();
    for (const url of new Set([...css.matchAll(/url\((https:[^)]+)\)/g)].map(m => m[1]))) {
      css = css.split(url).join(await dataUrl(url));
    }
    embeddedFontCss = css;
  } catch (e) { embeddedFontCss = ''; }
  return embeddedFontCss;
}
async function dataUrl(url){
  const blob = await (await fetch(url)).blob();
  return new Promise((res, rej) => { const r = new FileReader(); r.onload = () => res(r.result); r.onerror = rej; r.readAsDataURL(blob); });
}
async function frameToPng(){
  const w = zoomView.clientWidth, h = zoomView.clientHeight;
  const copy = zoom.copy.cloneNode(true);
  for (const img of copy.querySelectorAll('img')) { try { img.src = await dataUrl(img.src); } catch (e) {} }
  const wrap = document.createElement('div');
  wrap.setAttribute('xmlns', 'http://www.w3.org/1999/xhtml');
  const page = getComputedStyle(document.documentElement), body = getComputedStyle(document.body);
  wrap.style.cssText = 'position:relative;overflow:hidden;width:' + w + 'px;height:' + h + 'px;font-family:' + body.fontFamily
    + ';-webkit-font-smoothing:antialiased;color:' + body.color;
  const css = [...document.querySelectorAll('style')].map(el => el.textContent).join('\n');
  for (const name of new Set(css.match(/--[a-z0-9-]+(?=\s*:)/gi))) wrap.style.setProperty(name, page.getPropertyValue(name));
  wrap.style.background = cssVar('--sheet');
  const style = document.createElement('style'); style.textContent = css + '\n' + await embeddedFonts();
  wrap.append(style, copy);
  const svg = '<svg xmlns="http://www.w3.org/2000/svg" width="' + w + '" height="' + h + '"><foreignObject x="0" y="0" width="100%" height="100%">'
    + new XMLSerializer().serializeToString(wrap) + '</foreignObject></svg>';
  const img = new Image();
  img.src = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg);
  await img.decode();
  const scale = Math.max(2, window.devicePixelRatio || 1);
  const canvas = document.createElement('canvas'); canvas.width = Math.round(w * scale); canvas.height = Math.round(h * scale);
  canvas.getContext('2d').drawImage(img, 0, 0, canvas.width, canvas.height);
  return new Promise((res, rej) => canvas.toBlob(b => b ? res(b) : rej(new Error('png')), 'image/png'));
}
zoomSave.addEventListener('click', async () => {
  if (zoom.frozen !== 'zoom' || !zoom.copy) return;
  zoomSave.disabled = true; zoomSave.textContent = 'Saving…';
  try {
    const png = await frameToPng();
    const r = await fetch('/api/zooms', {method:'POST', headers:{'X-Journal':'1', 'Content-Type':'image/png'}, body:png});
    if (!r.ok) throw new Error();
    const {name} = await r.json();
    zoomSave.textContent = 'Saved'; zoomSave.title = 'Saved in journal/images as ' + name;
  } catch (e) {
    zoomSave.disabled = false; zoomSave.textContent = "Couldn't save. Try again";
  }
});

/* ---------- Links to other entries ----------
   Drag an entry from the list into the writing to link it. The link shows the entry's name in capitals
   inside a border; click it to preview the entry, drag it to move it, or drag it to the right of the text
   to keep a preview of the entry there. */
function linkName(id, fallback){ const e = entries.get(id); return ((e ? e.title : fallback) || '').trim() || 'Untitled'; }
function dressLink(el, id, title, hint){
  const e = entries.get(id), name = linkName(id, title);
  el.classList.add('fig', 'elink'); el.classList.toggle('missing', !e);
  el.dataset.link = id; el.dataset.title = cleanTitle(title);
  el.textContent = name;
  el.title = name + (e ? '' : ' (no longer in the journal)') + '\n' + hint;
  el.setAttribute('aria-label', 'Link to the entry ' + name);
}
// A link in the entry being written: it can be moved about like a picture.
function makeLink(id, title){
  const el = document.createElement('span'); el.contentEditable = 'false';
  dressLink(el, id, title, 'Click to preview, drag to move');
  el.addEventListener('pointerdown', startDrag);
  el.addEventListener('dragstart', ev => ev.preventDefault());
  return el;
}
// A link shown for reading only (in a preview, the Archive and the Tasks menu).
function staticLink(id, title){
  const el = document.createElement('button'); el.type = 'button';
  dressLink(el, id, title, 'Click to preview');
  el.addEventListener('click', ev => { ev.stopPropagation(); openLinkView(id, title); });
  return el;
}
// The linked entry, read-only: when it was begun and last changed, then everything in it.
function entryPreview(id, fallback){
  const frag = document.createDocumentFragment(), e = entries.get(id);
  const note = text => { const p = document.createElement('p'); p.className = 'arch-note'; p.textContent = text; frag.append(p); return frag; };
  if (!e) return note('This entry is no longer in the journal. If it was archived, it can be added back from the Archive.');
  const meta = document.createElement('p'); meta.className = 'link-meta';
  const topic = topicLabel(e);
  meta.textContent = 'Begun ' + fmtDate.format(new Date(e.created)) + ' \u00b7 last changed ' + when(e.updated) + (topic ? ' \u00b7 ' + topic : '');
  frag.append(meta);
  if (!e.body.trim()) return note('Nothing written in this entry yet.');
  const box = readOnlyBody(e.body, name => '/images/' + name, true);
  box.classList.add('link-body');
  frag.append(box);
  return frag;
}
let linkViewId = null;
function openLinkView(id, fallback){
  linkViewId = id;
  $('linkViewTitle').textContent = linkName(id, fallback);
  $('linkViewOpen').hidden = !entries.has(id) || id === currentId;
  $('linkViewPanel').replaceChildren(entryPreview(id, fallback));
  $('linkViewPanel').scrollTop = 0;
  if (!$('linkView').open) $('linkView').showModal();
}
// Open on a quote on the right: its words in the middle of the screen, in the same window as a linked entry.
function openQuoteView(text){
  linkViewId = null;
  $('linkViewTitle').textContent = 'Quote';
  $('linkViewOpen').hidden = true;
  $('linkViewPanel').replaceChildren(makeQuote(text, true));
  $('linkViewPanel').scrollTop = 0;
  if (!$('linkView').open) $('linkView').showModal();
}
$('linkViewClose').addEventListener('click', () => $('linkView').close());
$('linkView').addEventListener('click', ev => { if (ev.target === $('linkView')) $('linkView').close(); });
$('linkViewOpen').addEventListener('click', () => {
  const id = linkViewId;
  for (const d of document.querySelectorAll('dialog[open]')) d.close();
  if (id && entries.has(id)) open(id);
});

/* ---------- PDFs ----------
   A PDF is kept in journal/pdfs and sits in the writing as its title in a box. Like a picture or a linked
   entry, it can be dragged to another place, or to the right of the text to keep it open there; click it
   to read it large. It's shown in the browser's own PDF reader, so it can be scrolled, zoomed and searched. */
const PDF_ICON = '<svg viewBox="0 0 14 16" aria-hidden="true"><path d="M1.5 1.5h7l4 4v9h-11zM8.5 1.5v4h4" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/></svg>';
const isPdfRef = n => n.startsWith('pdf:');
const isPdfFile = f => f.type === 'application/pdf' || /\.pdf$/i.test(f.name || '');
const pdfSrc = name => '/pdfs/' + name;
// The browser's reader opens it fitted to the width, without its sidebar.
const pdfFrameSrc = name => pdfSrc(name) + '#zoom=page-width&pagemode=none';
const pdfTitleOf = file => cleanTitle(String(file.name || '').replace(/\.pdf$/i, '')) || 'PDF';
function dressPdf(el, name, title, hint){
  el.classList.add('fig', 'epdf');
  el.dataset.pdf = name; el.dataset.title = cleanTitle(title);
  el.innerHTML = PDF_ICON;
  el.append(el.dataset.title || 'Untitled PDF');
  el.title = (el.dataset.title || 'Untitled PDF') + '\n' + hint;
  el.setAttribute('aria-label', 'PDF: ' + (el.dataset.title || 'untitled'));
}
// A PDF in the entry being written: it can be moved about like a picture.
function makePdf(name, title){
  const el = document.createElement('span'); el.contentEditable = 'false';
  dressPdf(el, name, title, 'Click to read it, drag to move');
  el.addEventListener('pointerdown', startDrag);
  el.addEventListener('dragstart', ev => ev.preventDefault());
  return el;
}
// A PDF shown for reading only (in a preview, the Archive and the Tasks menu).
function staticPdf(name, title){
  const el = document.createElement('button'); el.type = 'button';
  dressPdf(el, name, title, 'Click to read it');
  el.addEventListener('click', ev => { ev.stopPropagation(); openPdfView(name, title, false); });
  return el;
}
// PDFs dropped on the entry (or picked, or pasted) go into the writing there, one after another.
// Returns where the next thing added should go.
async function addPdfs(files, t){
  const id = currentId;
  let problem = '';
  setStatus(files.length === 1 ? 'Adding PDF\u2026' : 'Adding ' + files.length + ' PDFs\u2026');
  for (const f of files) {
    try {
      const name = await store.uploadPdf(f), title = pdfTitleOf(f);
      if (id !== currentId) {
        // The entry was closed mid-upload: add the PDF at the end of its text.
        const e = entries.get(id);
        if (e) { e.body = serializeParts([...parseBody(e.body), {type:'pdf', name, title}]); markChanged(id); }
        continue;
      }
      const el = makePdf(name, title);
      placeFigure(el, t);
      t = {parent:el.parentNode, ref:el.nextSibling};
      onBodyChange();
    } catch (err) {
      problem = err.message === 'type' ? f.name + " isn't a PDF the journal can read."
        : err.message === 'size' ? f.name + ' is too large (the limit is 200 MB).'
        : "Couldn't add " + f.name + '. Check that the journal server is still running.';
    }
  }
  if (id === currentId && problem) setStatus(problem, true);
  return t;
}
// A PDF on the right: its pages in a frame, under its title, Open and Close. It's moved by its title.
function shelfPdfItem(ref){
  const name = ref.slice(4), e = entries.get(currentId), title = (e ? pdfTitleIn(e.body, name) : '') || 'Untitled PDF';
  const item = document.createElement('div'); item.className = 'shelf-item shelf-pdf'; item.dataset.name = ref;
  const frame = document.createElement('iframe'); frame.className = 'pdf-frame'; frame.loading = 'lazy';
  frame.title = 'PDF: ' + title; frame.src = pdfFrameSrc(name);
  const bar = document.createElement('div'); bar.className = 'zoom-bar';
  bar.innerHTML = '<span class="zoom-tag" title="Drag here to move it to another place"></span><span class="zoom-space"></span>'
    + '<button type="button" class="side-open-btn" title="Read this PDF large">Open</button>'
    + '<button type="button" class="side-read-btn" title="Open it as a book and turn its pages">Read</button>'
    + '<button type="button" class="side-close" title="Take it off the right (it stays in the writing)">Close</button>';
  bar.querySelector('.zoom-tag').textContent = title;
  bar.querySelector('.side-open-btn').addEventListener('click', () => openPdfView(name, pdfTitleIn(entries.get(currentId).body, name), true));
  bar.querySelector('.side-read-btn').addEventListener('click', () => openReader(name, pdfTitleIn(entries.get(currentId).body, name)));
  // Pressing on the title: the frames stop taking the pointer until it's let go, so the PDF can be dragged over them.
  bar.addEventListener('pointerdown', () => {
    document.body.classList.add('holding');
    window.addEventListener('pointerup', () => document.body.classList.remove('holding'), {once:true});
    window.addEventListener('pointercancel', () => document.body.classList.remove('holding'), {once:true});
  });
  item.setAttribute('aria-label', 'PDF: ' + title);
  item.append(frame, bar);
  wireShelfItem(item, bar);
  return item;
}
// Reading a PDF large. From the open entry its title can be changed and it can be deleted; from the
// Archive or a preview it's for reading only.
let pdfViewing = null, pdfShown = null;
function openPdfView(name, title, editable){
  pdfViewing = editable && currentId ? {name, id:currentId} : null;
  pdfShown = {name, title};
  const t = $('pdfViewTitle');
  t.value = cleanTitle(title); t.readOnly = !pdfViewing;
  t.title = pdfViewing ? 'The PDF\'s title. Click to change it' : '';
  $('pdfViewForever').hidden = !pdfViewing;
  disarm($('pdfViewForever'), 'Delete forever');
  $('pdfViewTab').href = pdfSrc(name);
  $('pdfViewFrame').src = pdfFrameSrc(name);
  $('pdfViewFrame').title = 'PDF: ' + (title || 'untitled');
  if (!$('pdfView').open) $('pdfView').showModal();
}
const pdfChips = name => [...els.body.querySelectorAll('.epdf')].filter(el => el.dataset.pdf === name);
// Changing the title changes it everywhere it is in the entry (and on the right).
$('pdfViewTitle').addEventListener('input', () => {
  const v = pdfViewing;
  if (!v || v.id !== currentId || $('pdfViewTitle').readOnly) return;
  const chips = pdfChips(v.name); if (!chips.length) return;
  for (const el of chips) dressPdf(el, v.name, $('pdfViewTitle').value, 'Click to read it, drag to move');
  onBodyChange();
});
$('pdfViewTitle').addEventListener('keydown', ev => { if (ev.key === 'Enter') { ev.preventDefault(); $('pdfViewTitle').blur(); } });
$('pdfViewForever').addEventListener('click', async () => {
  const btn = $('pdfViewForever'), v = pdfViewing;
  if (!v || !armed(btn, 'Delete forever', 'Delete forever? This can\'t be undone')) return;
  $('pdfView').close();
  if (v.id !== currentId) return;
  const e = entries.get(v.id);
  if (e && e.books && Object.values(e.books).includes(v.name))
    e.books = Object.fromEntries(Object.entries(e.books).filter(([, p]) => p !== v.name));
  for (const el of pdfChips(v.name)) detachFigure(el);
  els.body.normalize();
  onBodyChange();
  try {
    await flush(v.id);
    const r = await fetch('/api/pdfs/' + v.name, {method:'DELETE', headers:H});
    if (!r.ok) throw new Error('delete');
    if ((await r.json()).kept) setStatus('Taken out of this entry. The file is kept, as another entry still has it.');
  } catch (err) {
    setStatus("Took the PDF out of the entry, but couldn't erase its file. Check that the journal server is still running.", true);
  }
});
$('pdfViewClose').addEventListener('click', () => $('pdfView').close());
$('pdfViewRead').addEventListener('click', () => { if (pdfShown) openReader(pdfShown.name, $('pdfViewTitle').value || pdfShown.title); });
$('pdfView').addEventListener('click', ev => { if (ev.target === $('pdfView')) $('pdfView').close(); });
$('pdfView').addEventListener('close', () => {
  pdfViewing = null; $('pdfViewFrame').src = 'about:blank';   // stop reading it in the background
  disarm($('pdfViewForever'), 'Delete forever');
});

/* ---------- Reading a PDF as a book ----------
   The PDF opens as a book lying open: two pages side by side on their boards, with the edges of the pages
   already read and still to read showing at the sides. The first page sits alone on the right, as in a book.
   A page is turned by taking hold of it (best by a corner) and dragging it across: it folds along the line
   halfway between where its corner was and where it's been drawn to. The part past that line is drawn turned
   over, showing the back of the page (the next page), and the page after that shows where it has lifted
   away. Let go past the spine (or with a flick) and it turns; otherwise it falls back. Clicking a page, or the
   arrow keys, turns it by itself. The pages are drawn by pdf.js, a few either side of the open pages at a time.

   A PDF made into a book with a book model is read in that book: its boards, the insides of its boards and its
   page edges come from the model, the pages take its shape, and it has covers. It opens on its closed front
   cover, which swings open to where it was left; turned back past the first page it closes again, and on past
   the last, its back cover closes over. A cover doesn't bend: it swings round the spine, its far edge coming
   nearer (so larger) as it stands up. The open book is then "spread" 0 to K; closed at the front it's -1, and
   closed at the back K + 1. */
const RD = {doc:null, task:null, name:'', model:null, look:null, n:0, spread:0, target:null, keep:new Set(), next:[], opening:false, hold:false, drawing:false, aspect:0.7, W:0, H:0, ox:0, oy:0, dpr:1,
  shift:0, cache:new Map(), hi:new Map(), queue:[], busy:false, gen:0, pgen:0, turn:null, raf:0, open:false, faceA:null, faceB:null,
  b3:null, g3:null, v3:false, v3At:0, v3Timer:0,
  skip:0, pdfN:0, ends:false};   // the PDF's pages left out at the start (a book's cover), how many are read, and endpaper leaves (rdSrc)   // the book's model, drawn in 3D while it's closed or a cover swings (rd3Draw)
const READER_PAPER = '#FBFAF6', READER_BOARD = '#4B1E26', READER_EDGE = '#E4DFD3';
const rdCanvas = $('readerCanvas'), rdCtx = rdCanvas.getContext('2d');
let pdfjsLib = null;
async function loadPdfjs(){
  if (pdfjsLib) return pdfjsLib;
  const r = await fetch('/api/pdfjs', {headers:{'X-Journal':'1'}, cache:'no-store'}).catch(() => null);
  if (!r || !r.ok) throw new Error('pdfjs');
  const lib = await import('/pdfjs/build/pdf.min.mjs');
  lib.GlobalWorkerOptions.workerSrc = '/pdfjs/build/pdf.worker.min.mjs';
  return pdfjsLib = lib;
}

/* Books: book models made readable with a PDF, kept with the entry as {model file name: PDF file name}. */
const bookPdf = (e, model) => e && e.books ? e.books[model] || '' : '';
function bindBook(model, pdf){
  const e = entries.get(currentId); if (!e || !pdf) return;
  e.books = Object.assign({}, e.books, {[model]:pdf});
  markChanged(currentId); renderShelf();
  setStatus('Made into a book: Read, on the model, opens it.');
}
function unbindBook(model){
  const e = entries.get(currentId); if (!e || !bookPdf(e, model)) return;
  e.books = Object.assign({}, e.books); delete e.books[model];
  markChanged(currentId); renderShelf();
}
// from: the canvas the model is showing in, for the book to be taken up from there.
function readBook(model, from){
  if (FL.leaving) return;   // (still on its way back to its place)
  const e = entries.get(currentId), pdf = bookPdf(e, model);
  if (pdf) openReader(pdf, pdfTitleIn(e.body, pdf) || 'Book', model, from ? bookLift(model, from) : null);
}
const modelUnder = (x, y) => { const el = document.elementFromPoint(x, y); return el && el.closest ? el.closest('#shelfPics > .shelf-model') : null; };
function markBindTarget(item){
  for (const el of document.querySelectorAll('.bind-target')) if (el !== item) el.classList.remove('bind-target');
  if (item) item.classList.add('bind-target');
}
/* A book model's looks, read from its .glb: the materials the journal's book models are made of (by name),
   each a picture or a colour, and its proportions (the model is 1 tall, its width across, its thickness deep). */
const toSrgb = v => { v = Math.max(0, Math.min(1, v)); return Math.round(255 * (v <= 0.0031308 ? 12.92 * v : 1.055 * Math.pow(v, 1 / 2.4) - 0.055)); };
async function loadBookLook(model){
  const r = await fetch('/models/' + model); if (!r.ok) return null;
  const buf = await r.arrayBuffer(), dv = new DataView(buf);
  if (buf.byteLength < 28 || dv.getUint32(0, true) !== 0x46546C67) return null;
  const jl = dv.getUint32(12, true), json = JSON.parse(new TextDecoder().decode(new Uint8Array(buf, 20, jl)));
  if (!json.asset || json.asset.generator !== 'Journal book models') return null;   // only the journal's own book models
  const bin = 20 + jl + 8, byName = new Map((json.materials || []).map((m, i) => [m.name, m]));
  const hb = byName.get('headband'), headband = hb && hb.extras && Array.isArray(hb.extras.colours) &&
    hb.extras.colours.every(c => typeof c === 'string' && /^#[0-9a-fA-F]{6}$/.test(c)) ? hb.extras.colours.slice(0, 2) : null;
  const mat = async name => {
    const m = byName.get(name); if (!m) return null;
    const pbr = m.pbrMetallicRoughness || {};
    if (pbr.baseColorTexture) {
      const im = json.images[json.textures[pbr.baseColorTexture.index].source], v = json.bufferViews[im.bufferView];
      return {img:await createImageBitmap(new Blob([new Uint8Array(buf, bin + (v.byteOffset || 0), v.byteLength)], {type:im.mimeType || 'image/jpeg'}))};
    }
    return {colour:'rgb(' + (pbr.baseColorFactor || [0.4, 0.15, 0.15]).slice(0, 3).map(toSrgb).join(',') + ')'};
  };
  let aspect = 0, z0 = Infinity, z1 = -Infinity;
  for (const p of json.meshes[0].primitives) {
    const a = json.accessors[p.attributes.POSITION]; if (!a || !a.min) continue;
    z0 = Math.min(z0, a.min[2]); z1 = Math.max(z1, a.max[2]);
    if ((json.materials[p.material] || {}).name === 'front') aspect = (a.max[0] - a.min[0]) / (a.max[1] - a.min[1]);
  }
  if (!(aspect > 0.1 && aspect < 5)) return null;
  const [front, back, insideL, insideR, endpaper, board, edges, paper, endsheet, spine, spineWindow] = await Promise.all(
    ['front', 'back', 'insideFront', 'insideBack', 'endpaper', 'board', 'edges', 'leaf', 'endsheet', 'spine', 'spineWindow'].map(mat));
  // The spine's colour, for its hollow showing between the boards of the open book (a photo's, its average).
  const average = m => {
    if (!m) return null;
    if (!m.img) return m.colour;
    const cv = document.createElement('canvas'); cv.width = cv.height = 8;
    const c = cv.getContext('2d'); c.drawImage(m.img, 0, 0, 8, 8);
    const d = c.getImageData(0, 0, 8, 8).data, sum = [0, 0, 0];
    for (let i = 0; i < d.length; i += 4) for (let j = 0; j < 3; j++) sum[j] += d[i + j];
    return 'rgb(' + sum.map(v => Math.round(v / 64)).join(',') + ')';
  };
  return {aspect, thick:Math.max(0.01, z1 - z0), front:front || board, back:back || front || board,
    insideL:insideL || endpaper || board, insideR:insideR || endpaper || board, board, edges, paper, endsheet,
    spine, spineColour:average(spine) || average(front) || average(board), headband, spineWindow:spineWindow && spineWindow.img || null};
}

/* Taking a book up to read it. The model itself (drawn by the shared WebGL canvas, over the whole screen) floats
   from where it was, on the right or open large, to just in front of you: it rises a little as it comes, grows
   as it nears, and turns to face you with its front cover. It arrives exactly where the reader shows the closed
   book, and stays there, the same model: the reader carries on drawing it (below) until the book lies open.
   Where the model was, it's gone until the book is closed again. With reduced motion asked for, the reader
   simply opens. */
const FL = {active:false, back:null, raf:0, hid:[], lift:null, to:null, arrived:null, arrive:null, landed:false, leaving:false, t:0, ms:0};
const flEase = t => t * t * t * (t * (t * 6 - 15) + 10);   // smootherstep: starts and ends at rest
// How far off the camera is from a book in the reader: far enough that it looks as flat as the pages drawn over
// it. A cover standing up is drawn as if seen from RD3_NEAR, so it's seen coming towards you; only the cover, as
// from that close, the board underneath would look smaller than the pages lying on it.
const RD3_FAR = 80, RD3_NEAR = 7;
// The light a face turned straight at you gets. A book lying still in the reader is lit up by this much more, so
// its faces look just as their photos and colours do, as the reader draws them.
const M3_FACE_LIGHT = (() => {
  const z = (x, y, zz) => Math.max(0, zz / Math.hypot(x, y, zz));
  return 0.34 * 0.775 + 0.88 * z(-0.45, 0.7, 0.55) + 0.26 * z(0.7, 0.1, 0.35);
})(), M3_REST_BRIGHT = 1 / M3_FACE_LIGHT - 1;
/* The shape of one of the journal's own book models (see bookGeometry), from its parts: the front board runs from
   xl (at the spine) to xr and from -top to top, its outside at zo; the page block runs from xl to px1 and from
   -py1 to py1, between the insides of the boards at -zi and zi. Null for any other model. As the reader draws
   the book, a page is the page block's face, and the boards reach past it by sq (a share of the page height). */
function bookDims(data){
  const box = name => {
    let lo = null, hi = null;
    for (const p of data) if (p.name === name) for (let k = 0; k < p.pos.length; k += 3) {
      const v = [p.pos[k], p.pos[k + 1], p.pos[k + 2]];
      lo = lo ? lo.map((x, j) => Math.min(x, v[j])) : v; hi = hi ? hi.map((x, j) => Math.max(x, v[j])) : v;
    }
    return lo && {lo, hi};
  };
  const f = box('front'), e = box('edges');
  if (!f || !e) return null;
  const d = {xl:f.lo[0], xr:f.hi[0], top:f.hi[1], zo:f.hi[2], px1:e.hi[0], py1:e.hi[1], zi:e.hi[2]};
  if (!(d.px1 > d.xl && d.xr >= d.px1 && d.top > d.py1 && d.py1 > 0 && d.zo > d.zi && d.zi > 0)) return null;
  // (how far the spine rounds out past the boards, in pages' heights)
  const sp = box('spine'), round = sp ? Math.max(0, d.xl - sp.lo[0]) / (2 * d.py1) : 0;
  return Object.assign(d, {aspect:(d.px1 - d.xl) / (2 * d.py1), sq:(d.top - d.py1) / (2 * d.py1), round});
}
// The shared canvas made the size of the whole screen and cleared, ready to draw on, and the canvas over the
// reader that it's copied to.
function m3Full(){
  const gl = m3Gl(); if (!gl) return null;
  const cv = $('readerFlight'), dpr = Math.min(window.devicePixelRatio || 1, 2), SW = innerWidth, SH = innerHeight;
  const W = Math.max(1, Math.round(SW * dpr)), H = Math.max(1, Math.round(SH * dpr));
  if (cv.width !== W || cv.height !== H) { cv.width = W; cv.height = H; }
  const g = M3.canvas; if (g.width !== W || g.height !== H) { g.width = W; g.height = H; }
  gl.viewport(0, 0, W, H);
  gl.clearColor(0, 0, 0, 0); gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
  gl.enable(gl.DEPTH_TEST); gl.disable(gl.CULL_FACE); gl.disable(gl.BLEND);
  gl.useProgram(M3.prog); gl.uniform1i(M3.loc.uTex, 0); gl.uniform2f(M3.loc.uUv, 1, 0);
  return {gl, L:M3.loc, cv, g, dpr, SW, SH, W, H};
}
function m3Part(gl, L, p){
  gl.uniform4fv(L.uBase, p.base); gl.uniform1f(L.uCut, p.cut); gl.uniform1i(L.uLit, p.lit ? 1 : 0);
  gl.uniform1i(L.uHasTex, p.tex ? 1 : 0); gl.uniform1f(L.uLod, p.lod || 0);
  gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, p.tex);
  gl.bindVertexArray(p.vao);
  gl.drawElements(gl.TRIANGLES, p.count, gl.UNSIGNED_INT, 0);
}
// A projection for the whole screen with the camera's axis through (x, y) on it, showing what's dist away as
// s pixels to a unit.
function m3Aim(x, y, s, dist, SW, SH, near, far){
  const h = 2 * dist * Math.tan(M3_FOV / 2) * s;
  return m4.mul([h / SW,0,0,0, 0,h / SH,0,0, 0,0,1,0, 2 * x / SW - 1,1 - 2 * y / SH,0,1], m4.perspective(M3_FOV, 1, near, far));
}
function bookLift(name, from){
  const m = M3.cache.get(name);
  if (!m || !m.data || !from.isConnected || !m3Gl()) return null;
  if (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches) return null;
  const r = from.getBoundingClientRect();
  if (r.width < 4 || r.height < 4 || r.bottom < 0 || r.top > innerHeight || r.right < 0 || r.left > innerWidth) return null;
  // The model's extent, for a book that isn't one of the journal's own: its front cover facing +z, 2hy tall and 2hx wide.
  let hx = 0, hy = 0, hz = 0;
  for (const p of m.data) for (let k = 0; k < p.pos.length; k += 3) {
    hx = Math.max(hx, Math.abs(p.pos[k])); hy = Math.max(hy, Math.abs(p.pos[k + 1])); hz = Math.max(hz, Math.abs(p.pos[k + 2]));
  }
  if (!(hy > 0.01)) return null;
  const s = m3State(name), aspect = r.width / r.height;
  const half = Math.min(M3_FOV / 2, Math.atan(Math.tan(M3_FOV / 2) * aspect)), dist = 1.06 / Math.sin(half) / s.zoom;
  return {name, from, hx, hy, hz, rect:{left:r.left, top:r.top, width:r.width, height:r.height},
    x:r.left + r.width / 2, y:r.top + r.height / 2, s:r.height / (2 * dist * Math.tan(M3_FOV / 2)), dist,
    yaw:Math.atan2(Math.sin(s.yaw), Math.cos(s.yaw)), pitch:s.pitch, panX:s.panX, panY:s.panY};
}
function flyBook(lift){
  const st = $('readerStage').getBoundingClientRect(), sw = st.width, sh = st.height;
  if (!sw || !sh) { $('bookReader').classList.remove('flying'); return; }
  let to;
  if (RD.b3 && RD.W) to = rd3Pose(false);
  else {
    // Another model: its front cover as large as the reader's closed book, in the middle.
    const H = readerFit(sw, sh, Math.min(2, Math.max(0.25, lift.hx / lift.hy))), px = H + 2 * Math.max(8, H * 0.024);
    to = {x:st.left + sw / 2, y:st.top + sh / 2, s:px / (2 * lift.hy), dist:Math.max(lift.dist, 2.2), panX:0, panZ:-lift.hz, bright:0};
  }
  const far = Math.hypot(to.x - lift.x, to.y - lift.y), ms = Math.max(750, Math.min(1100, 650 + far * 0.35));
  // Every view of it goes (on the right as well as the large view it may have come from): the book is in your hands.
  const hid = [lift.from, ...[...M3.views].filter(v => v.name === lift.name && v.canvas !== lift.from).map(v => v.canvas)];
  Object.assign(FL, {active:true, hid, lift, to, landed:false, t:0, ms, arrived:new Promise(r => FL.arrive = r)});
  for (const c of hid) c.style.visibility = 'hidden';
  const cv = $('readerFlight'); cv.hidden = false; cv.classList.remove('landing', 'entering');
  // Its first frame now, where it lies, while the reader is still being set up (the canvases made the size of the
  // screen, and so on); it moves from the next. And a frame that's late only holds it back a little: it doesn't
  // leap ahead, so however long the first frames take, it rises smoothly.
  flyFrame(lift, to, 0, 0);
  let clock = 0, prev = 0;
  const step = now => {
    FL.raf = 0;
    if (!FL.active) return;
    clock += prev ? Math.min(now - prev, 34) : 0; prev = now;
    const t = Math.min(1, clock / ms);
    FL.t = t; FL.ms = ms;
    flyFrame(lift, to, t, t < 1 ? 0 : clock - ms);
    if (t >= 1 && FL.arrive) { FL.arrive(); FL.arrive = null; }
    if (!FL.landed) FL.raf = requestAnimationFrame(step);
  };
  FL.raf = requestAnimationFrame(step);
}
// Just as the reader draws a journal book lying closed (rd3Draw), at the front or (back) turned over at the back:
// its spine where the reader has it, the pages the reader's size, seen from far off, and lit as brightly.
function rd3Pose(back){
  const d = RD.b3, st = $('readerStage').getBoundingClientRect(), shift = (back ? 1 : -1) * (RD.W + rdMargin()) / 2;
  return {x:st.left + RD.ox + shift + RD.W, y:st.top + RD.oy + RD.H / 2, s:RD.H / (2 * d.py1), dist:RD3_FAR,
    yaw:back ? Math.PI : 0, panX:back ? d.xl : -d.xl, panZ:-d.zi, bright:M3_REST_BRIGHT, still:true};
}
// One frame of the flight, t going 0 to 1; after that, wait is how long it has hovered.
function flyFrame(a, b, t, wait){
  const m = M3.cache.get(a.name); if (!m || !m.data) return;
  const f = m3Full(); if (!f) return;
  const {gl, L, SW, SH, dpr} = f;
  const lerp = (x, y, k) => x + (y - x) * k;
  // It moves and grows together; it turns a little behind, so it's seen coming round as it rises. As it comes,
  // it's seen from further and further off, and so flattens out, to lie as flat as the reader's pages.
  const e = flEase(t), er = flEase(Math.min(1, Math.max(0, (t - 0.08) / 0.84)));
  const lift = Math.min(70, 0.14 * Math.hypot(b.x - a.x, b.y - a.y)) * Math.sin(Math.PI * e);
  const bob = wait > 0 && !b.still ? Math.sin(wait / 520) * 2 * Math.min(1, wait / 400) : 0;   // hovering while the pages get ready
  const x = lerp(a.x, b.x, e), y = lerp(a.y, b.y, e) - lift + bob, s = Math.exp(lerp(Math.log(a.s), Math.log(b.s), e));
  // (turned the shorter way round to the yaw it arrives at)
  const by = a.yaw + Math.atan2(Math.sin((b.yaw || 0) - a.yaw), Math.cos((b.yaw || 0) - a.yaw));
  const dist = 1 / lerp(1 / a.dist, 1 / b.dist, e), yaw = lerp(a.yaw, by, er), pitch = lerp(a.pitch, 0, er);
  const panX = lerp(a.panX, b.panX, e), panY = lerp(a.panY, 0, e), panZ = lerp(0, b.panZ, e);
  const cy = Math.cos(yaw), sy = Math.sin(yaw), cp = Math.cos(pitch), sp = Math.sin(pitch);
  const rotY = [cy,0,-sy,0, 0,1,0,0, sy,0,cy,0, 0,0,0,1], rotX = [1,0,0,0, 0,cp,sp,0, 0,-sp,cp,0, 0,0,0,1];
  const reach = 1.5 + Math.hypot(panX, panY, panZ);
  gl.uniformMatrix4fv(L.uProj, false, m3Aim(x, y, s, dist, SW, SH, Math.max(0.01, dist - reach), dist + reach + 1.5));
  gl.uniformMatrix4fv(L.uView, false, m4.mul(m4.trs([panX, panY, panZ - dist]), m4.mul(rotX, rotY)));
  gl.uniform1i(L.uSwing, 0); gl.uniform1f(L.uBright, lerp(0, b.bright, e));
  for (const p of m3Gpu(gl, m)) if (p.name !== 'spineWindow') m3Part(gl, L, p);   // (that's only for the flat reader's open book)
  gl.bindVertexArray(null);
  // At first it's still inside the box it was in (cut off where that was, if it was zoomed in); the box
  // opens out as it leaves.
  const c = f.cv.getContext('2d'), k = flEase(Math.min(1, t / 0.4)), r = a.rect;
  const l = lerp(r.left, 0, k), tp = lerp(r.top, 0, k), rw = lerp(r.left + r.width, SW, k), bt = lerp(r.top + r.height, SH, k);
  c.setTransform(1, 0, 0, 1, 0, 0); c.clearRect(0, 0, f.W, f.H);
  c.save(); c.beginPath(); c.rect(l * dpr, tp * dpr, (rw - l) * dpr, (bt - tp) * dpr); c.clip();
  c.drawImage(f.g, 0, 0); c.restore();
}
// Once it has arrived and the reader is ready: a journal book stays as it is, and the reader carries on drawing
// it just the same; any other model fades into the reader's book.
async function flyLand(gen){
  if (!FL.active) return;
  await FL.arrived;
  if (gen !== RD.gen || !FL.active || FL.landed) return;
  FL.landed = true;
  if (FL.raf) { cancelAnimationFrame(FL.raf); FL.raf = 0; }
  $('bookReader').classList.remove('flying');
  if (FL.to && FL.to.still && RD.b3) {
    FL.active = false; RD.v3 = true;
    drawReader();
    return;
  }
  $('readerFlight').classList.add('landing');
  await new Promise(r => setTimeout(r, 320));
  if (gen === RD.gen) flyEnd();
}
function flyEnd(){
  FL.active = false;
  if (FL.back) FL.back();
  if (FL.raf) { cancelAnimationFrame(FL.raf); FL.raf = 0; }
  if (FL.arrive) { FL.arrive(); FL.arrive = null; }
  const cv = $('readerFlight'); cv.hidden = true; cv.classList.remove('landing', 'entering');
  $('bookReader').classList.remove('flying');
}
/* Closing the book: the flight the other way. The book is shut first (its cover swings closed, if it's open), then
   it floats back to where it was taken from (or, if that's gone, to the model on the right), turning back to how it
   lay there, while the room lightens; there the model is itself again. Without anywhere to go back to (or with
   reduced motion asked for), the reader simply closes. */
// Flies it back from t (of the way up) to where it was, over as long as it took to come that far.
function flyBackFrom(lift, to, t, ms, gen){
  const t0 = performance.now(), dur = Math.max(250, ms * t);
  return new Promise(end => {
    // (and if the flight's stopped from outside, the reader closed some other way, it's over then too)
    const done = () => { if (FL.back === done) FL.back = null; end(); };
    FL.back = done;
    const step = now => {
      if (gen !== RD.gen) { done(); return; }
      const u = Math.min(1, (now - t0) / dur);
      flyFrame(lift, to, t * (1 - u), 0);
      if (u < 1) FL.raf = requestAnimationFrame(step); else done();
    };
    FL.raf = requestAnimationFrame(step);
  });
}
async function closeBook(){
  const dlg = $('bookReader');
  if (FL.leaving) return;
  // (held turned, moved or nearer: it's put back as it was first, then it goes back)
  if (RD.doc && !rvHome() && !FL.active) { if (RV.going) return; RV.going = true; try { await rvGoHome(); } finally { RV.going = false; } }
  // The model comes back in the same moment as the reader (and the book flying in it) goes, and the reader lets
  // go of the book then: its 'close' event comes a little after, and a frame could be shown between, with the
  // book nowhere (or a page just drawn could show it again).
  const shut = () => { closeReaderDoc(); if (dlg.open) dlg.close(); };
  // Closed while it's still on its way up: it goes back from where it's got to.
  if (FL.active && !FL.landed && FL.lift && FL.to) {
    const gen = RD.gen, lift = FL.lift, to = FL.to, t = FL.t;
    FL.leaving = true; FL.landed = true;   // the flight up stops here (and won't land)
    if (RD.drawTask) RD.drawTask.cancel();
    if (FL.raf) { cancelAnimationFrame(FL.raf); FL.raf = 0; }
    // The room lightens again from however dark it had got, and the bar goes, as the book goes back.
    const ms = Math.max(250, (FL.ms || 900) * t);
    try {
      for (const an of dlg.getAnimations({subtree:true})) {
        const ct = Math.max(0, Number(an.currentTime) || 0);
        an.reverse(); an.updatePlaybackRate(-Math.max(0.25, ct / ms));
      }
    } catch (e) {}
    try { await flyBackFrom(lift, to, t, FL.ms || 900, gen); }
    finally { shut(); FL.leaving = false; dlg.classList.remove('leaving'); }
    return;
  }
  const lift0 = FL.lift, name = lift0 && lift0.name;
  const target = name && [lift0.from, ...FL.hid].find(c => c && c.isConnected && c.getBoundingClientRect().width > 3);
  if (!target || FL.active || !RD.doc) { shut(); return; }
  FL.leaving = true; RD.next = [];
  if (RD.drawTask) RD.drawTask.cancel();   // (a page being drawn is let go of: it's drawn again if it's needed)
  const gen = RD.gen, K = lastSpread();
  try {
    // Shut: a cover on its way open goes back the way it came; one on its way shut carries on; and from an open
    // spread (or a page being turned), the cover nearer it swings closed over it: the front one in the first half
    // of the book, the back one past the middle.
    if (RD.b3 && RD.look) {
      const t = RD.turn;
      if (t && t.kind === 'rigid') { if (t.to >= 0 && t.to <= K) rdAnimate(t, 'back'); }
      else {
        if (t && t.mode === 'anim') rdSettle();   // (a page on its way over lies down where it was going first)
        RD.turn = null;
        if (RD.spread >= 0 && RD.spread <= K) rdRigid(RD.spread, 2 * RD.spread > K ? K + 1 : -1, 'turn');
      }
      while (gen === RD.gen && RD.turn) await new Promise(r => setTimeout(r, 30));
    }
    if (gen !== RD.gen) return;
    const lift = bookLift(name, target), back = RD.spread > K;
    if (!lift) return;
    const to = RD.b3 && RD.look ? rd3Pose(back) : FL.to;
    if (!to) return;
    FL.active = true; FL.landed = false;   // the reader stops drawing the book; the flight has it now
    const cv = $('readerFlight');
    const fresh = cv.hidden;
    cv.hidden = false; cv.classList.remove('landing', 'entering');
    flyFrame(lift, to, 1, 0);
    if (fresh) { void cv.offsetWidth; cv.classList.add('entering'); }   // a book shown open, not as the model: the model comes in over it
    dlg.classList.add('leaving');
    await new Promise(r => setTimeout(r, fresh ? 200 : 0));
    const far = Math.hypot(to.x - lift.x, to.y - lift.y);
    await flyBackFrom(lift, to, 1, Math.max(750, Math.min(1100, 650 + far * 0.35)), gen);
  } finally {
    // closed first: let go of the lightening before, and the room would be dark again for a moment
    shut();
    FL.leaving = false; dlg.classList.remove('leaving');
  }
}
// Closing the book puts the model back where it was.
function flyStop(){
  flyEnd();
  for (const c of FL.hid) c.style.visibility = '';
  FL.hid = []; FL.lift = FL.to = null;
}

/* The book in the reader while it's closed, or while a cover swings: the journal's book model itself, drawn on
   the canvas over the reader (the one it flew up on), so the book you took up is the book you open. It lies
   facing you, seen from far off so it looks as flat as the pages. A cover swings round its hinge towards you,
   looking larger as it stands up and comes nearer, and the pages the book opens at lie on the page block and on the
   inside of the board. Closing at the back, the book is turned over and its back board swings the same way.
   Once it lies open, the reader's own drawing of the open book (drawn to the model's proportions, and lit the
   same) takes over, and the model fades away over it. */
const RD3_BOARD = new Set(['front', 'back', 'insideFront', 'insideBack', 'endpaper', 'rim', 'board']);
const RD3_SPINE = new Set(['spine', 'headcap', 'tailcap', 'capSide']);
// A flat, textured rectangle in the model from x0 to x1 (the page's height), at z, facing n (1 or -1).
function rd3Quad(gl, d, x0, x1, z, n, flipU){
  const pts = [[x0, d.py1, z], [x1, d.py1, z], [x1, -d.py1, z], [x0, -d.py1, z]], made = [];
  const pos = new Float32Array(pts.flat()), nrm = new Float32Array([0, 0, n, 0, 0, n, 0, 0, n, 0, 0, n]);
  const uv = new Float32Array(flipU ? [1, 0, 0, 0, 0, 1, 1, 1] : [0, 0, 1, 0, 1, 1, 0, 1]);
  const vao = gl.createVertexArray(); gl.bindVertexArray(vao); made.push(['VertexArray', vao]);
  for (const [loc, data, size] of [[0, pos, 3], [1, nrm, 3], [3, uv, 2]]) {
    const b = gl.createBuffer(); made.push(['Buffer', b]); gl.bindBuffer(gl.ARRAY_BUFFER, b); gl.bufferData(gl.ARRAY_BUFFER, data, gl.STATIC_DRAW);
    gl.enableVertexAttribArray(loc); gl.vertexAttribPointer(loc, size, gl.FLOAT, false, 0, 0);
  }
  gl.disableVertexAttribArray(2); gl.vertexAttrib4f(2, 1, 1, 1, 1);
  // Wound so its front is the side it faces (the light falls on the front).
  const ib = gl.createBuffer(); made.push(['Buffer', ib]); gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, ib);
  gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, new Uint32Array(n > 0 ? [0, 2, 1, 0, 3, 2] : [0, 1, 2, 0, 2, 3]), gl.STATIC_DRAW);
  gl.bindVertexArray(null);
  return {vao, count:6, base:[1, 1, 1, 1], cut:0, lit:true, tex:null, made};
}
/* What the book can show once a board swings: on the page block, and on the inside of the swinging board, a page
   (over the block's face) and the edges of the pages beside it (the width m of them, in the board's margin). Where
   each lies in the model, before the board swings, a hair clear of what it lies on, and read the right way round
   once the board has swung over (or, for the back, as the turned-over book shows it). */
const RD3_E1 = 0.0008, RD3_E2 = 0.0016;
const rd3Place = (d, back, slot) => {
  const board = slot === 'board', z = (back ? -1 : 1) * (d.zi - (board ? RD3_E1 : RD3_E2));
  return {z, n:(back ? -1 : 1) * (board ? -1 : 1), flipU:board !== back};
};
function rd3Quads(gl, d){
  const page = (back, slot) => { const q = rd3Place(d, back, slot); return rd3Quad(gl, d, d.xl, d.px1, q.z, q.n, q.flipU); };
  return {front:{board:page(false, 'board'), block:page(false, 'block')}, back:{board:page(true, 'board'), block:page(true, 'block')}};
}
// The edges beside a page, m wide in the model: made again only when their width changes.
function rd3Strip(gl, back, slot, m){
  const g3 = RD.g3, key = [back, slot, m.toFixed(6)].join(), name = slot + 'Edge', old = g3.strips[name];
  if (old && old.key === key) return old;
  if (old) for (const [kind, obj] of old.made) gl['delete' + kind](obj);
  const q = rd3Place(g3.d, back, slot);
  return g3.strips[name] = Object.assign(rd3Quad(gl, g3.d, g3.d.px1, g3.d.px1 + m, q.z, q.n, q.flipU), {key});
}
// Something the reader draws (w wide, the page's height), as a texture, redrawn only when key or entry changes
// (a sharper drawing of the page arrives, or the reader changes size).
function rd3Tex(gl, slot, key, entry, w, draw){
  const rec = RD.g3.tex[slot] || (RD.g3.tex[slot] = {});
  key = [key, RD.H, RD.dpr].join();
  if (rec.tex && rec.key === key && rec.entry === entry) return rec.tex;
  const cv = rec.cv || (rec.cv = document.createElement('canvas'));
  cv.width = Math.max(1, Math.round(w * RD.dpr)); cv.height = Math.max(1, Math.round(RD.H * RD.dpr));
  const c = cv.getContext('2d'); c.setTransform(RD.dpr, 0, 0, RD.dpr, 0, 0); c.clearRect(0, 0, w, RD.H); draw(c);
  if (!rec.tex) rec.tex = gl.createTexture();
  gl.bindTexture(gl.TEXTURE_2D, rec.tex);
  gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, false); gl.pixelStorei(gl.UNPACK_PREMULTIPLY_ALPHA_WEBGL, false);
  gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, cv);
  gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
  gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
  rec.key = key; rec.entry = entry;
  return rec.tex;
}
// Page p as the reader draws it lying on the left (x 0) or the right (x RD.W) of the book open at spread k, with
// the page edges beside it where they lie over its place (e).
const rd3PageTex = (gl, slot, p, x, k, e) => rd3Tex(gl, slot, [p, x, RD.W, k, e.t].join(), RD.cache.get(p) || null, RD.W, c => {
  c.translate(-x, 0);
  // Under it, the inside of the board, just as the reader draws it: it shows where the page's corners dip into the
  // spine (left empty, those would show black on the model).
  const left = x === 0, b = rdMargin();
  rdFill(c, RD.look && (left ? RD.look.insideL : RD.look.insideR), left ? -b : RD.W, -b, RD.W + b, RD.H + 2 * b, READER_BOARD);
  if (e.inn) rdEdges(c, left ? e.inn : 2 * RD.W - e.inn, e.t, left);
  rdSlotAt(c, p, x, k);
});
// The page edges in the board's margin (e.out wide), as the reader draws them on the left or the right.
const rd3EdgeTex = (gl, slot, e, left) => rd3Tex(gl, slot, [e.t, e.out, left].join(), null, e.out, c => {
  if (left) { c.translate(e.out, 0); rdEdges(c, e.inn, e.t, true); } else { c.translate(-2 * RD.W, 0); rdEdges(c, 2 * RD.W - e.inn, e.t, false); }
});
/* How far out from the back of the pages a board's edge lies once it's swung open, in the model's units: it hinges
   at its joint, outside the spine's shoulder, not at the pages, so it swings clear of them and lies down a little
   way out from them, the endpaper running over the joint between (the open book in 3D only; the flat one is drawn
   with the board at the spine). */
const rd3Gap = d => obActive() ? Math.max(1.5 * (d.zo - d.zi), 0.022 * d.py1) : 0;
// How far out a board lies at spread k of the open book (obBuild), in the model's units: the whole gap where the
// spine stands up and the board lies open over it, less the further the spine turns under the book, half of it in
// the middle. (back: the back board)
// The share of the picture inside a board that the board takes at spread k of the open book, the joint having the rest
// (as obBuild's hingeA has it).
function rd3HingeA(d, k, back){
  const G = rd3GapAt(d, k, back); if (!G) return 1;
  return (d.xr - d.xl) / (d.xr - d.xl + G);
}
function rd3GapAt(d, k, back){
  const G = rd3Gap(d); if (!G) return 0;
  const py = 2 * d.py1, Tn = Math.max(0.01, d.zi / d.py1), bt = Math.max(0.004, (d.zo - d.zi) / py);
  const f = Math.min(1, Math.max(0, 2 * k / Math.max(1, RD.n))), sn = Math.sin(Math.PI * f), s = Tn * 0.5 + bt;
  const Lc = 2 * s - (bt + 0.002) * (1 - sn), lam = (bt - 0.002) * (1 - sn);
  const sth = (f < 0.5 ? 1 : -1) * Math.min(1, (Tn * Math.abs(1 - 2 * f) + lam) / Lc);
  return G / 2 * (back ? 1 - sth : 1 + sth);
}
/* The joint as the board swings round it (th, its angle; side, 1 the front board, -1 the back): the covering
   running from the spine's edge (as far down as the spine has sunk, open) round the board's edge, and on the
   inside the endpaper, from the board over the joint to the back of the pages. Nothing while the book is shut.
   Worked out as the shader moves the board (with its lean), and drawn as it is. */
function rd3Joint(gl, L, m, d, side, th, open, lean, G){
  const gpu = m3Gpu(gl, m), part = (...names) => { for (const n of names) { const p = gpu.find(q => q.name === n); if (p) return p; } return null; };
  const hx = d.xl - G / 2, hz = side * d.zi, c = Math.cos(th), sn = Math.sin(th), T = d.top, bt = d.zo - d.zi, tile = rimTile(m.data);
  const at = (px, pz) => {
    const dx = px - hx, dz = pz - hz, z = hz + side * dx * sn + dz * c, k = 1 + lean * Math.max(side * (z - hz), 0);
    return [hx + (dx * c - side * dz * sn) * k, z, k];
  };
  // The joint, from the board's edge (its inside corner bi, outside bo) to the spine and the back of the pages (the
  // top of the pages there, pg): shut, it's nothing; open, it's the board carried on in to the spine (obJointFill).
  const bi = at(d.xl, side * d.zi), bo = at(d.xl, side * d.zo), pg = [d.xl, side * d.zi, 1];
  const strip = (mesh, a, b, u) => {
    const n = [b[1] - a[1], 0, a[0] - b[0]];
    if (Math.hypot(n[0], n[2]) < 1e-7) return;
    obQuad(mesh, [[a[0], T * a[2], a[1]], [b[0], T * b[2], b[1]], [b[0], -T * b[2], b[1]], [a[0], -T * a[2], a[1]]], n, [[u, 0], [u, 0], [u, 1], [u, 1]]);
  };
  const made = [], draw = (mesh, p, fallback) => {
    if (!mesh.idx.length) return;
    const g = obMesh(gl, made, mesh), how = p || {base:fallback, cut:0, lit:true, tex:null};
    m3Part(gl, L, {vao:g.vao, count:g.count, base:how.base || [1, 1, 1, 1], cut:how.cut || 0, lit:how.lit !== false, tex:how.tex || null});
  };
  const us = side > 0 ? 0.998 : 0.002, cover = obNew(), paste = obNew(), ends = obNew();
  // (the endpaper over the joint: the board's own picture of it from beside the spine, true to size, the same way round)
  { const hA = rd3HingeA(d, RD.spread >= 0 && RD.spread <= lastSpread() ? RD.spread : side > 0 ? 0 : lastSpread(), side < 0), ub = side > 0 ? hA : 1 - hA, ug = side > 0 ? 1 : 0;
    const n = [pg[1] - bi[1], 0, bi[0] - pg[0]];
    if (Math.hypot(n[0], n[2]) > 1e-7) obQuad(paste, [[bi[0], T * bi[2], bi[1]], [pg[0], T, pg[1]], [pg[0], -T, pg[1]], [bi[0], -T * bi[2], bi[1]]], n, [[ub, 0], [ug, 0], [ug, 1], [ub, 1]]); }
  // (the spine's end as the shader has it: sunk towards the back as the book opens; from its edge by this board, outwards)
  const zs = z => { const q = Math.max(-d.zo, Math.min(d.zo, z)); return q + (-side * d.zo - q) * open; };
  const arcM = spineArc(m.data), uz = z => (Math.max(-d.zo, Math.min(d.zo, z)) + d.zo) / (2 * d.zo);
  const arc = arcM.map(([x, z]) => [x, zs(z), 1, uz(z)]);
  if (side > 0) arc.reverse();
  const C = [d.xl, zs(side * d.zo), 1, side > 0 ? 1 : 0];
  // (the covering round the joint from the board's photo: the front's runs 0 at the spine, the back's 1)
  const tx = {uS:side > 0 ? 0.006 : 0.994, dir:side > 0 ? 1 : -1, W:d.xr - d.xl};
  if (arc.length) arc[0] = C;
  // (the photo of the board's edges carried on round: along the board from its edge, and across it from its
  // outside to its inside, as the board lies now)
  const along = [c, side * sn], out = [-sn, side * c];
  const cap = p => [((p[0] - bi[0]) * along[0] + (p[1] - bi[1]) * along[1]) / tile,
    Math.min(1, Math.max(0, 1 - ((p[0] - bi[0]) * out[0] + (p[1] - bi[1]) * out[1]) / Math.max(1e-6, bt)))];
  obJointFill(cover, ends, bo, bi, C, pg, arc, T, tx, cap, obGrooveR(d) * (1 - c) / 2, [-along[0], -along[1]]);
  const ins = side > 0 ? part('insideFront', 'endpaper') : part('insideBack', 'endpaper');
  draw(cover, side > 0 ? part('front', 'board') : part('back', 'front', 'board'), [0.3, 0.08, 0.08, 1]); draw(paste, ins, [0.8, 0.77, 0.7, 1]); draw(ends, part('rim', 'board'), [0.3, 0.08, 0.08, 1]);
  gl.bindVertexArray(null);
  for (const [kind, obj] of made) gl['delete' + kind](obj);
}
/* A headband's ends curving down into the spine (so that they aren't seen ending): over the last Rb of its length at
   each end its roll turns, a quarter round, towards -x (into the hollow of the spine), keeping its length. pos (and
   nrm, if given) are changed in place: [x, y, z] with its length along z, its middle at x = cx, its ends at +-zEnd. */
function bendHeadband(pos, nrm, cx, zEnd, Rb){
  Rb = Math.min(Rb, zEnd); const zs = zEnd - Rb;
  for (let i = 0; i < pos.length; i += 3) {
    const sz = Math.sign(pos[i + 2]) || 1, az = Math.abs(pos[i + 2]);
    if (az <= zs) continue;
    const phi = Math.min(1, (az - zs) / Rb) * Math.PI / 2, c = Math.cos(phi), s = Math.sin(phi), dx = pos[i] - cx;
    pos[i] = cx - Rb * (1 - c) + dx * c; pos[i + 2] = sz * (zs + Rb * s + dx * s);
    if (nrm) { const nx = nrm[i], nz = sz * nrm[i + 2]; nrm[i] = nx * c - nz * s; nrm[i + 2] = sz * (nx * s + nz * c); }
  }
}
/* A headband: a roll of silk, radius r, round the line x = cx, y = cy, from z -zEnd to zEnd, in rings along it (closer
   together towards its ends, which curve down into the spine: bendHeadband), its silk repeating reps times along it. */
function headbandTube(cx, cy, r, zEnd, reps, out, room){
  // (room: how deep the hollow of the spine is behind it, at the spine's middle, and how wide the spine is across,
  // [depth, half-width]: its ends are brought in, and curve no further, than they can and stay inside the spine)
  let Rb = 2.5 * r;
  if (room) {
    const [dep, zo] = room, depthAt = z => dep * Math.sqrt(Math.max(0, 1 - (z / zo) * (z / zo)));
    // (it runs the whole way across the leaves; its ends curve in as tightly as they need to, to stay inside the
    // spine there, and only if the spine is too shallow even for that is it brought in a little)
    Rb = Math.min(Rb, depthAt(zEnd + r) - 1.4 * r);
    while (Rb < 0.8 * r && zEnd > 0.6 * zo) { zEnd *= 0.99; Rb = Math.min(2.5 * r, depthAt(zEnd + r) - 1.4 * r); }
    Rb = Math.max(0.3 * r, Rb);
  }
  const M = 16, rings = [], NZ = 40;
  for (let i = 0; i <= NZ; i++) { const t = -1 + 2 * i / NZ; rings.push(zEnd * Math.sign(t) * (1 - Math.pow(1 - Math.abs(t), 1.6))); }
  const o = out || {pos:[], nrm:[], uv:[], idx:[]}, b0 = o.pos.length / 3;
  for (const z of rings) for (let i = 0; i <= M; i++) {
    const a = 2 * Math.PI * i / M, nx = Math.cos(a), ny = Math.sin(a);
    o.pos.push(cx + r * nx, cy + r * ny, z); o.nrm.push(nx, ny, 0); o.uv.push((z + zEnd) / (2 * zEnd) * reps, i / M);
  }
  for (let k = 0; k < rings.length - 1; k++) for (let i = 0; i < M; i++) {
    const a = b0 + k * (M + 1) + i, c = a + M + 1; o.idx.push(a, a + 1, c, a + 1, c + 1, c);
  }
  // (its ends closed, curving down into the spine with the rest)
  for (const [k, sz] of [[0, -1], [rings.length - 1, 1]]) {
    const e0 = o.pos.length / 3;
    o.pos.push(cx, cy, rings[k]); o.nrm.push(0, 0, sz); o.uv.push(0, 0.5);
    for (let i = 0; i <= M; i++) { const a = 2 * Math.PI * i / M; o.pos.push(cx + r * Math.cos(a), cy + r * Math.sin(a), rings[k]); o.nrm.push(0, 0, sz); o.uv.push(0, 0.5); }
    for (let i = 1; i <= M; i++) o.idx.push(e0, e0 + i, e0 + i + 1);
  }
  const from = b0 * 3;
  const P = o.pos.slice(from), N = o.nrm.slice(from);
  bendHeadband(P, N, cx, zEnd, Rb);
  for (let i = 0; i < P.length; i++) { o.pos[from + i] = P[i]; o.nrm[from + i] = N[i]; }
  return o;
}
/* The headband as the open book has it (amt 1; 0, as the model has it, closed; between, on its way): set half into
   the spine, its middle on the back of the pages; long enough to run from joint to joint, less its own thickness,
   so that its ends stay within the leaves however few there are on one side; resting on the heads of the leaves
   rather than sunk into them (open, the leaves dip into the gutter beside it, and it would come up through them);
   and its ends curving down into the spine. */
function obHeadbandShape(p, d, amt, data){
  // (made again from the model's own headbands, their size and place read from it: that way a model made before
  // their ends were curved gets them too, the roll having the rings along it to curve)
  let lo = Infinity, hi = -Infinity, zm = 0, reps = 0, yTop = -Infinity;
  for (let j = 0; j < p.pos.length; j += 3) { lo = Math.min(lo, p.pos[j]); hi = Math.max(hi, p.pos[j]); zm = Math.max(zm, Math.abs(p.pos[j + 2])); yTop = Math.max(yTop, p.pos[j + 1]); }
  if (p.uv) for (let j = 0; j < p.uv.length; j += 2) reps = Math.max(reps, p.uv[j]);
  const r = (hi - lo) / 2, cx0 = (lo + hi) / 2, cy0 = yTop - r;
  const cx = cx0 + (d.xl - cx0) * amt, cy = cy0 + 1.3 * r * amt;
  const zEnd = zm * (1 + (Math.max(1, (d.zo - 2 * r) / Math.max(1e-6, zm)) - 1) * amt), rp = Math.max(1, reps || Math.round(zm / Math.max(1e-6, r))) * zEnd / zm;
  const o = {pos:[], nrm:[], uv:[], idx:[]};
  // (the spine's hollow as deep as its outline at its ends is: not by the raised bands, which don't reach there)
  const arc = data ? spineArc(data) : [], dep = (arc.length ? d.xl - Math.min(...arc.map(q => q[0])) : (d.round || 0) * 2 * d.py1) + (d.xl - cx);
  for (const s of [1, -1]) headbandTube(cx, s * cy, r, zEnd, rp, o, [dep, d.zo]);
  return o;
}
// A flat polygon's triangles (by cutting off its ears one at a time), as indices into it: so that a face that isn't
// convex covers just itself, and nothing beside it (which would flicker against whatever lies there).
function obTriangulate(P){
  const n = P.length; if (n < 3) return [];
  let area = 0; for (let i = 0; i < n; i++) { const a = P[i], b = P[(i + 1) % n]; area += a[0] * b[1] - b[0] * a[1]; }
  const sg = area >= 0 ? 1 : -1, idx = [...Array(n).keys()], out = [];
  const cr = (a, b, c) => (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]);
  let guard = 0;
  while (idx.length > 3 && guard++ < 4 * n) {
    let cut = false;
    for (let i = 0; i < idx.length; i++) {
      const ia = idx[(i + idx.length - 1) % idx.length], ib = idx[i], ic = idx[(i + 1) % idx.length], a = P[ia], b = P[ib], c = P[ic];
      const z = sg * cr(a, b, c);
      if (z < -1e-14) continue;
      if (z <= 1e-14) { idx.splice(i, 1); cut = true; break; }   // (in line: no triangle)
      let inside = false;
      for (const j of idx) {
        if (j === ia || j === ib || j === ic) continue;
        const p = P[j]; if (sg * cr(a, b, p) >= 0 && sg * cr(b, c, p) >= 0 && sg * cr(c, a, p) >= 0) { inside = true; break; }
      }
      if (inside) continue;
      out.push(ia, ib, ic); idx.splice(i, 1); cut = true; break;
    }
    if (!cut) break;
  }
  if (idx.length === 3) out.push(...idx);
  return out;
}
// A flat face at y (+-), the polygon poly of [x, z, k] points (k scaling y), its photo placed by cap.
function obFlat(mesh, poly, Y, cap){
  const P = poly.filter((p, i) => Math.hypot(p[0] - poly[(i + 1) % poly.length][0], p[1] - poly[(i + 1) % poly.length][1]) > 1e-9);
  const tri = obTriangulate(P);
  for (const y of [1, -1]) {
    const b0 = mesh.pos.length / 3;
    for (const p of P) obVert(mesh, [p[0], y * Y * p[2], p[1]], [0, y, 0], cap(p));
    for (const t of tri) mesh.idx.push(b0 + t);
  }
}
/* A joint where a board lies out from the spine, closed like the board itself: the covering running on from the
   board's outside edge (Bo), level with the board, to the spine, so the board and the spine meet across the board's
   whole thickness; and its ends, at the head and the tail (at y = +-Y), filled from the board's edge (inside corner
   Bi, outside Bo) round to the spine's edge (C) and in to the back of the leaves (In). Points are [x, z, k], k scaling
   their y (a board leaning as it stands up). cap(pt) is where the photo of the boards' edges falls on a point of the
   ends; tx, the column of the board's photo for the covering. arc: the spine's outline at its end, from C outwards.
   Where the board lies lower than the spine's edge (towards the covers, the open board lying level with the leaves),
   the covering runs on level until it meets the spine's round, and the spine's edge above that is folded into the
   joint, as a real spine's is there (as much of it as the board lies lower, and none by the middle of the book).
   The covering never goes over the spine otherwise: where the spine turns away from the joint into the inside corner
   they make (as it hangs under the book), it dips into a shallow groove over the last stretch (R) before the spine's
   edge, as at a real book's joint, coming out of it along the spine's own curve, so that the one runs smoothly on
   into the other and all of the spine shows. */
function obJointFill(cover, ends, Bo, Bi, C, In, arc, Y, tx, cap, R, toSpine){
  const ux = C[0] - Bo[0], uz = C[1] - Bo[1], ul = Math.hypot(ux, uz);
  // Where the board's outside, carried on towards the spine (toSpine: along the board), meets the spine's round before
  // its edge (X).
  const tl = Math.hypot(toSpine[0], toSpine[1]) || 1, t = [toSpine[0] / tl, toSpine[1] / tl];
  let X = null, k = -1;
  for (let i = 0; i < arc.length - 1 && !X; i++) {
    const a = arc[i], b = arc[i + 1], e = [b[0] - a[0], b[1] - a[1]], den = t[0] * e[1] - t[1] * e[0];
    if (Math.abs(den) < 1e-14) continue;
    const sB = ((a[0] - Bo[0]) * e[1] - (a[1] - Bo[1]) * e[0]) / den, u = ((a[0] - Bo[0]) * t[1] - (a[1] - Bo[1]) * t[0]) / den;
    if (u >= -1e-9 && u <= 1 + 1e-9 && sB >= -1e-6) { X = [Bo[0] + t[0] * Math.max(0, sB), Bo[1] + t[1] * Math.max(0, sB), (a[2] + b[2]) / 2]; k = i; }
  }
  let path, poly;
  if (X && Math.hypot(X[0] - C[0], X[1] - C[1]) > 1e-6) {
    path = [Bo, X]; poly = [Bi, Bo, X]; for (let i = k; i >= 1; i--) poly.push(arc[i]); poly.push(C, In);
  } else {
    path = [Bo];
    if (ul > 1e-9 && arc.length > 1 && R > 0) {
      const u = [ux / ul, uz / ul], a = arc[1], vl = Math.hypot(a[0] - C[0], a[1] - C[1]) || 1, v = [(a[0] - C[0]) / vl, (a[1] - C[1]) / vl];
      // (an inside corner: the spine turns off the joint's line to the outside, away from the board's inside)
      const cross = (p, q) => p[0] * q[1] - p[1] * q[0];
      if (cross(u, v) * cross(u, [Bi[0] - Bo[0], Bi[1] - Bo[1]]) < 0 && u[0] * v[0] + u[1] * v[1] > -0.5) {
        const l = Math.min(R, 0.8 * ul), P0 = [C[0] - u[0] * l, C[1] - u[1] * l], h = 0.55 * l;
        const P1 = [P0[0] + u[0] * h, P0[1] + u[1] * h], P2 = [C[0] - v[0] * h, C[1] - v[1] * h];
        const k0 = Bo[2] + (C[2] - Bo[2]) * (1 - l / ul);
        for (let i = 0; i < 10; i++) {
          const q = i / 10, a0 = (1 - q) ** 3, a1 = 3 * q * (1 - q) ** 2, a2 = 3 * q * q * (1 - q), a3 = q ** 3;
          path.push([a0 * P0[0] + a1 * P1[0] + a2 * P2[0] + a3 * C[0], a0 * P0[1] + a1 * P1[1] + a2 * P2[1] + a3 * C[1], k0 + (C[2] - k0) * q]);
        }
      }
    }
    path.push(C); poly = [Bi, ...path, In];
  }
  if (obCrosses(poly)) { path = [Bo, C]; poly = [Bi, Bo, C, In]; }
  obCoverStrips(cover, path, tx, Y);
  obFlat(ends, poly, Y, cap);
}
/* The covering round a joint: the board's own photo (the covering runs on from the spine onto the board, and the
   board's photo is of it), a strip of it from just beside the spine, at its true size and the same way round as on the
   board, laid along the path (of [x, z, k] points, ending on the spine) by how far along it each point is: tx = {uS:
   where across the board's photo the spine's end falls, dir: which way across it is away from the spine (+1 or -1), W:
   the board's width}. Along the book's length, y from -Y to Y, the photo's height. */
function obCoverStrips(cover, path, tx, Y){
  // (kept to the plain margin of the photo beside the spine, where there's rarely any decoration: a long way round
  // the joint is squeezed into it a little rather than reaching the tooling further in)
  const run = [0]; for (let i = path.length - 2; i >= 0; i--) run.unshift(run[0] + Math.hypot(path[i + 1][0] - path[i][0], path[i + 1][1] - path[i][1]));
  const most = 0.03, k = Math.min(1, most / Math.max(1e-9, run[0] / Math.max(1e-6, tx.W)));
  const us = run.map(r => tx.uS + tx.dir * k * r / Math.max(1e-6, tx.W));
  for (let i = 0; i < path.length - 1; i++) {
    const a = path[i], b = path[i + 1], n = [b[1] - a[1], 0, a[0] - b[0]];
    if (Math.hypot(n[0], n[2]) <= 1e-9) continue;
    obQuad(cover, [[a[0], Y * a[2], a[1]], [b[0], Y * b[2], b[1]], [b[0], -Y * b[2], b[1]], [a[0], -Y * a[2], a[1]]], n, [[us[i], 0], [us[i + 1], 0], [us[i + 1], 1], [us[i], 1]]);
  }
}
// Whether a closed outline crosses itself (so that it can't be filled as one face).
function obCrosses(P){
  const n = P.length, cr = (o, p, q) => (p[0] - o[0]) * (q[1] - o[1]) - (p[1] - o[1]) * (q[0] - o[0]);
  for (let i = 0; i < n; i++) for (let k = i + 2; k < n; k++) {
    if (i === 0 && k === n - 1) continue;
    const a = P[i], b = P[(i + 1) % n], c = P[k], d = P[(k + 1) % n];
    if (cr(a, b, c) * cr(a, b, d) < -1e-18 && cr(c, d, a) * cr(c, d, b) < -1e-18) return true;
  }
  return false;
}
// How long the groove in a joint is, at most, in the model's units (obJointFill).
const obGrooveR = d => Math.max(1.2 * (d.zo - d.zi), 0.016 * 2 * d.py1);
// The spine's outline at its end, as [x, z] in the model (from its vertices at the head), in order round it.
function spineArc(data){
  const p = data && data.find(q => q.name === 'spine'); if (!p) return [];
  let top = -Infinity; for (let i = 1; i < p.pos.length; i += 3) top = Math.max(top, p.pos[i]);
  const pts = [];
  for (let i = 0; i < p.pos.length; i += 3) if (Math.abs(p.pos[i + 1] - top) < 1e-6) pts.push([p.pos[i], p.pos[i + 2]]);
  pts.sort((a, b) => a[1] - b[1]);
  return pts.filter((q, i) => !i || Math.abs(q[1] - pts[i - 1][1]) + Math.abs(q[0] - pts[i - 1][0]) > 1e-7);
}
// The headband drawn in the model as a cover swings: shaped as far towards the open book's as the book is open
// (obHeadbandShape), and sinking with the spine as it does.
function rd3Headband(gl, L, m, d, amt){
  const data = m.data, i = data.findIndex(q => q.name === 'headband'); if (i < 0) return;
  const g = m3Gpu(gl, m).find(q => q.name === 'headband'); if (!g) return;
  const sh = obHeadbandShape(data[i], d, amt, data), mesh = obNew(), made = [];
  mesh.pos = sh.pos; mesh.nrm = sh.nrm || sh.pos.map(() => 0); mesh.uv = sh.uv || sh.pos.filter((v, j) => j % 3 < 2).map(() => 0);
  mesh.col = []; for (let j = 0; j < sh.pos.length / 3; j++) mesh.col.push(1, 1, 1, 1);
  mesh.idx = Array.from(sh.idx);
  const vm = obMesh(gl, made, mesh);
  gl.uniform1i(L.uSwing, 2);
  gl.bindTexture(gl.TEXTURE_2D, g.tex); if (g.tex) gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.REPEAT);
  m3Part(gl, L, {vao:vm.vao, count:vm.count, base:g.base || [1, 1, 1, 1], cut:g.cut || 0, lit:g.lit !== false, tex:g.tex || null});
  gl.uniform1i(L.uSwing, 0); gl.bindVertexArray(null);
  for (const [kind, obj] of made) gl['delete' + kind](obj);
}
// How long a stretch of the photo of the boards' edges covers along an edge, in the model's units (1, without one).
function rimTile(data){
  const p = data && data.find(q => q.name === 'rim'); if (!p || !p.uv || !p.nrm) return 1;
  let lo = null, hi = null;
  for (let i = 0; i < p.pos.length / 3; i++) if (Math.abs(p.nrm[3 * i + 1]) > 0.9) {
    const v = [p.pos[3 * i], p.uv[2 * i]]; if (!lo || v[0] < lo[0]) lo = v; if (!hi || v[0] > hi[0]) hi = v;
  }
  return lo && hi && Math.abs(hi[1] - lo[1]) > 1e-6 ? Math.abs((hi[0] - lo[0]) / (hi[1] - lo[1])) : 1;
}
// Draws the book (closed, or with t, a cover swinging) and shows it. False when it can't be drawn this way.
function rd3Draw(t){
  const d = RD.b3, m = RD.model && M3.cache.get(RD.model);
  if (!d || !RD.look || !m || !m.data) return false;
  if (FL.active) return true;   // still on its way up: the flight draws it
  const f = m3Full(); if (!f) return false;
  const {gl, L} = f, K = lastSpread();
  if (!RD.g3 || RD.g3.gl !== gl || RD.g3.d !== d) RD.g3 = {gl, d, quads:rd3Quads(gl, d), strips:{}, tex:{}};
  // Which board swings (the back one, turned over, at the end of the book), how far open it is, and the spread it opens at.
  let back = RD.spread > K, o = 0, open = -1;
  if (t && t.kind === 'rigid') {
    back = Math.min(t.from, t.to) >= 0;
    o = t.from < 0 || t.from > K ? t.p : 1 - t.p;
    open = back ? Math.min(t.from, t.to) : Math.max(t.from, t.to);
  }
  const side = back ? -1 : 1, th = Math.PI * o, dist = RD3_FAR;
  const st = $('readerStage').getBoundingClientRect();
  const x = st.left + RD.ox + RD.shift + RD.W + RV.panX, y = st.top + RD.oy + RD.H / 2 + RV.panY, s = RD.H / (2 * d.py1) * RV.zoom;
  const turn = back ? [-1,0,0,0, 0,1,0,0, 0,0,-1,0, 0,0,0,1] : m4.id();
  gl.uniformMatrix4fv(L.uProj, false, m3Aim(x, y, s, dist, f.SW, f.SH, Math.max(0.01, dist - 2.5), dist + 2.5));
  // (turned about the middle of the closed book, moving to the gutter as it opens, where the open book is turned
  // about: so that, turned, the one takes over from the other where it lies. It moves as the board does, easing
  // in and out with it, so that it's still once the board lies down.)
  const om = (1 - Math.cos(th)) / 2, pc = (back ? -1 : 1) * (d.xr - d.xl) / 2 * (1 - om);
  RD.rvLast = {x, y, s, dist, base:m4.mul(m4.trs([back ? d.xl : -d.xl, 0, -d.zi]), turn), pivot:[pc, 0, -d.zi * (1 - om)]};
  gl.uniformMatrix4fv(L.uView, false, rvView(dist, RD.rvLast.pivot, RD.rvLast.base));
  gl.uniform1f(L.uBright, M3_REST_BRIGHT); gl.uniform1f(L.uSide, side);
  gl.uniform2f(L.uHinge, d.xl, side * d.zi); gl.uniform2f(L.uCS, Math.cos(th), Math.sin(th));
  // The board swings round its joint, out from the back of the pages (see rd3Gap), and a page on it slides along it
  // as it goes, to come down at the gutter.
  const G = rd3GapAt(d, open >= 0 ? open : back ? K : 0, back);
  gl.uniform1f(L.uGap, G / 2); gl.uniform1f(L.uShift, -G * om);
  // (the spine keeps its shape as the cover swings, only coming down at its front edge, level with the leaves, as the
  // board goes from over it: just as the open book has it)
  gl.uniform1f(L.uOpen, o * (d.zo - d.zi + 0.002 * 2 * d.py1) / (2 * d.zo)); gl.uniform1f(L.uZo, d.zo); gl.uniform1f(L.uLean, Math.sin(th) / RD3_NEAR);
  // The back of the book between the boards, as wide on each side as the open book will have it (in the model, it's
  // as wide as the boards reach past the pages, on each side).
  const sd = rdSpineSides(open >= 0 ? open : RD.spread), unit = 2 * d.py1 / RD.H / Math.max(1e-6, d.top - d.py1);
  gl.uniform2f(L.uWin, sd.l * unit, sd.r * unit); gl.uniform1f(L.uWinH, sd.h); gl.uniform1f(L.uPy1, d.py1);
  gl.uniform2f(L.uWinU, sd.shift * 2 * d.py1 / RD.H, sd.half * 2 * d.py1 / RD.H);
  const d3 = obActive(), hA = rd3HingeA(d, open >= 0 ? open : back ? K : 0, back);
  for (const p of m3Gpu(gl, m)) {
    // (the flat reader shows the headband and the back of the book in its own picture of it, spineWindow; in 3D, the
    // headband itself is drawn, below, as the open book has it, and the picture isn't)
    if (p.name === 'headband' || (d3 && p.name === 'spineWindow')) continue;
    gl.uniform1i(L.uSwing, p.name === 'spineWindow' ? 4 : RD3_BOARD.has(p.name) ? 1 : RD3_SPINE.has(p.name) ? 2 : 0);
    // (the endpaper inside the board swinging open shared out with the joint, as the open book has it: obBuild)
    const sq3 = d3 && ((p.name === 'insideFront' && !back) || (p.name === 'insideBack' && back)) ? hA : 1;
    gl.uniform2f(L.uUv, sq3, p.name === 'insideBack' && sq3 < 1 ? 1 - sq3 : 0);
    // (the back of the book: the reader's own picture of it, as the open book will show it)
    m3Part(gl, L, p.name === 'spineWindow' ? Object.assign({}, p, {tex:rdWindowTex(gl, open >= 0 ? open : RD.spread)}) : p);
  }
  gl.uniform1i(L.uSwing, 0); gl.uniform2f(L.uUv, 1, 0);
  if (d3) rd3Headband(gl, L, m, d, om);
  if (G > 0 && o > 0) rd3Joint(gl, L, m, d, side, th, o * (d.zo - d.zi + 0.002 * 2 * d.py1) / (2 * d.zo), Math.sin(th) / RD3_NEAR, G);
  if (o > 0 && open >= 0 && open <= K) {
    const q = RD.g3.quads[back ? 'back' : 'front'];
    // At the front, the board carries the left page and the block has the right; at the back, the other way round.
    // Beside each, the edges of the pages under it, just as the reader draws them.
    for (const [slot, pg, left, swing] of [['board', back ? 2 * open + 1 : 2 * open, !back, 3], ['block', back ? 2 * open : 2 * open + 1, back, 0]]) {
      gl.uniform1i(L.uSwing, swing);
      const e = rdEdgeSplit(left, open);
      if (pg >= 1 && pg <= RD.n) m3Part(gl, L, Object.assign({}, q[slot], {tex:rd3PageTex(gl, slot, pg, left ? 0 : RD.W, open, e)}));
      if (e.out) m3Part(gl, L, Object.assign({}, rd3Strip(gl, back, slot, e.out / s), {tex:rd3EdgeTex(gl, slot + 'Edge', e, left)}));
    }
  }
  gl.bindVertexArray(null); gl.uniform1i(L.uSwing, 0); gl.uniform1f(L.uBright, 0); gl.uniform1f(L.uGap, 0); gl.uniform1f(L.uShift, 0);
  const c = f.cv.getContext('2d'); c.setTransform(1, 0, 0, 1, 0, 0); c.clearRect(0, 0, f.W, f.H); c.drawImage(f.g, 0, 0);
  rd3Show();
  return true;
}
// The model coming into view over the reader (fading in, over the open book it starts from), and going again.
function rd3Show(){
  const cv = $('readerFlight');
  clearTimeout(RD.v3Timer);
  if (cv.hidden) { cv.hidden = false; RD.v3At = performance.now(); cv.classList.remove('entering'); void cv.offsetWidth; cv.classList.add('entering'); }
  cv.classList.remove('landing');
  RD.v3 = true;
}
function rd3Leave(){
  if (!RD.v3) return;
  RD.v3 = false;
  const cv = $('readerFlight'); cv.classList.add('landing');
  clearTimeout(RD.v3Timer);
  RD.v3Timer = setTimeout(() => { if (!RD.v3) { cv.hidden = true; cv.classList.remove('landing', 'entering'); } }, 320);
}
/* The open book in 3D (a first try, to judge the look by). A book made with one of the journal's book models,
   lying open, is drawn as a solid book rather than a flat picture: the boards, with the endpapers pasted inside
   them; the two stacks of leaves, as thick as the pages on each side, their top leaves (the pages being read)
   curving down into the gutter where they meet; the back of the book hollow between the boards at the head and the
   tail, with the headbands down in it. A leaf goes over bending round the spine (obLeaf); a cover swings in the
   model itself (rd3Draw). Units: a page's height. */
const OB = {on:true};
/* How the book is being held (3D only): turned (yaw, round the up-and-down of the screen, and pitch), moved (panX,
   panY, in pixels) and brought nearer (zoom). Dragging turns it, Shift-drag (or the right button) moves it, the wheel
   brings it nearer, a double-click puts it back; it's put back before the book goes back where it came from. */
const RV = {yaw:0, pitch:0, zoom:1, panX:0, panY:0};
const rvReset = () => Object.assign(RV, {yaw:0, pitch:0, zoom:1, panX:0, panY:0});
const rvHome = () => Math.abs(RV.yaw) < 1e-3 && Math.abs(RV.pitch) < 1e-3 && Math.abs(RV.zoom - 1) < 1e-3 && Math.abs(RV.panX) < 0.5 && Math.abs(RV.panY) < 0.5;
function rvRot(){
  const cy = Math.cos(RV.yaw), sy = Math.sin(RV.yaw), cp = Math.cos(RV.pitch), sp = Math.sin(RV.pitch);
  return m4.mul([1,0,0,0, 0,cp,sp,0, 0,-sp,cp,0, 0,0,0,1], [cy,0,-sy,0, 0,1,0,0, sy,0,cy,0, 0,0,0,1]);
}
// The view, looking from dist away at pivot (where the book is turned about), after base.
const rvView = (dist, pivot, base) => m4.mul(m4.trs([pivot[0], pivot[1], pivot[2] - dist]), m4.mul(rvRot(), m4.mul(m4.trs(pivot.map(v => -v)), base)));
// Puts the book back as it was, over a moment (resolves once it's there).
function rvGoHome(ms = 380){
  if (rvHome()) { rvReset(); return Promise.resolve(); }
  const from = Object.assign({}, RV), t0 = performance.now();
  // (turned back the shorter way round)
  from.yaw = Math.atan2(Math.sin(from.yaw), Math.cos(from.yaw)); from.pitch = Math.atan2(Math.sin(from.pitch), Math.cos(from.pitch));
  return new Promise(done => {
    const step = now => {
      const u = Math.min(1, (now - t0) / ms), e = 1 - Math.pow(1 - u, 3);
      for (const k of ['yaw', 'pitch', 'panX', 'panY']) RV[k] = from[k] * (1 - e);
      RV.zoom = from.zoom + (1 - from.zoom) * e;
      drawReader();
      if (u < 1) requestAnimationFrame(step); else { rvReset(); drawReader(); done(); }
    };
    requestAnimationFrame(step);
  });
}
try { OB.on = localStorage.getItem('journal-reader-3d') !== '0'; } catch (e) {}
const obActive = () => OB.on && !!RD.b3 && !!RD.look;
function obShowButton(){
  const b = $('reader3d'); b.hidden = !(RD.b3 && RD.look); b.setAttribute('aria-pressed', OB.on ? 'true' : 'false');
  document.querySelector('.reader-help').textContent = obActive()
    ? 'Drag to turn the book, Shift-drag to move it, scroll to zoom, double-click to straighten it; click a page or use the arrow keys'
    : 'Drag a corner, click a page, or use the arrow keys';
}
$('reader3d').addEventListener('click', () => {
  OB.on = !OB.on;
  try { localStorage.setItem('journal-reader-3d', OB.on ? '1' : '0'); } catch (e) {}
  RD.turn = null; if (!OB.on) rvReset();
  obShowButton(); drawReader(); readerWant(); rdCanvas.focus();
});
// A colour ('rgb(…)', '#rrggbb' or [r, g, b]) as the shader takes it.
function obColour(css, fallback){
  let v = Array.isArray(css) ? css : null, m = typeof css === 'string' && /rgba?\(([^)]+)\)/.exec(css);
  if (m) v = m[1].split(',').slice(0, 3).map(Number);
  else if (typeof css === 'string' && /^#[0-9a-f]{6}$/i.test(css)) v = [1, 3, 5].map(i => parseInt(css.slice(i, i + 2), 16));
  return toLinear(v || fallback);
}
// A picture on the graphics card, made again only when key changes.
function obTex(gl, slot, key, src){
  const T = RD.obTex || (RD.obTex = new Map());
  let rec = T.get(slot);
  if (rec && rec.gl === gl && rec.key === key) { rec.used = performance.now(); return rec.tex; }
  if (!rec || rec.gl !== gl) { rec = {gl, tex:gl.createTexture()}; T.set(slot, rec); }
  rec.used = performance.now();
  gl.bindTexture(gl.TEXTURE_2D, rec.tex);
  gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, false); gl.pixelStorei(gl.UNPACK_PREMULTIPLY_ALPHA_WEBGL, false);
  gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, src);
  gl.generateMipmap(gl.TEXTURE_2D);
  gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR_MIPMAP_LINEAR); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
  gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
  const an = gl.getExtension('EXT_texture_filter_anisotropic');
  if (an) gl.texParameterf(gl.TEXTURE_2D, an.TEXTURE_MAX_ANISOTROPY_EXT, Math.min(16, gl.getParameter(an.MAX_TEXTURE_MAX_ANISOTROPY_EXT)));
  rec.key = key;
  return rec.tex;
}
// Page p as a picture: its paper, and the PDF's page on it (at the sharpness it was drawn at). Each page keeps its
// own picture on the graphics card while it's near where the book is open, so a leaf going over (its two sides, and
// the pages under it) doesn't have them made again; those further off are let go of. (A page that isn't in the
// book, as past the last leaf, is plain paper.)
function obPage(gl, p){
  const inBook = p >= 1 && p <= RD.n, src = inBook ? rdSrc(p) : {blank:true}, e = src.pdf && RD.cache.get(p), W = RD.W, H = RD.H;
  const slot = 'pg' + (inBook ? p : 0);
  const hiE = src.pdf && RD.hi.get(p);
  const key = [RD.gen, p, hiE ? 'hi' + hiE.canvas.width : e ? e.pgen + ':' + e.canvas.width : '-', W, H, RD.dpr].join();
  const T = RD.obTex && RD.obTex.get(slot);
  if (T && T.gl === gl && T.key === key) { T.used = performance.now(); return T.tex; }
  if (RD.obTex) {   // (those used longest ago go; those being drawn are used for every picture)
    const pgs = [...RD.obTex.keys()].filter(s => /^pg\d+$/.test(s) && s !== slot && s !== 'pg0');
    if (pgs.length > 7) {
      const used = s => RD.obTex.get(s).used || 0;
      for (const s of pgs.sort((a, b) => used(a) - used(b)).slice(0, pgs.length - 7)) {
        const r = RD.obTex.get(s); if (r.gl === gl) gl.deleteTexture(r.tex); RD.obTex.delete(s);
      }
    }
  }
  // The page drawn for the 3D book (RD.hi), put down pixel for pixel on its paper, the paper around it made to match;
  // until that's drawn, the flat book's drawing of it, stretched to fit.
  const hi = src.pdf && RD.hi.get(p);
  const ratio = hi ? hi.canvas.width / hi.canvas.height : e ? e.ratio : W / H;
  let w = W, h = W / ratio; if (h > H) { h = H; w = H * ratio; }
  const k = hi ? hi.canvas.width / w : RD.dpr * 1.25, cv = document.createElement('canvas');
  cv.width = Math.max(1, Math.round(W * k)); cv.height = Math.max(1, Math.round(H * k));
  const c = cv.getContext('2d'); c.setTransform(k, 0, 0, k, 0, 0);
  if (src.end) rdFill(c, RD.look.endsheet, 0, 0, W, H, READER_PAPER); else rdPaper(c, 0, 0, W, H);
  if (hi || e) {
    c.save(); if (RD.look && RD.look.paper) c.globalCompositeOperation = 'multiply';
    if (hi) {
      const pc = hi.canvas;
      c.setTransform(1, 0, 0, 1, 0, 0); c.drawImage(pc, Math.round((cv.width - pc.width) / 2), Math.round((cv.height - pc.height) / 2));
    } else { c.imageSmoothingQuality = 'high'; c.drawImage(e.canvas, (W - w) / 2, (H - h) / 2, w, h); }
    c.restore();
  } else if (src.pdf) {   // not drawn yet: its number, as the flat book shows it
    c.fillStyle = 'rgba(30,39,35,.3)'; c.font = 'italic ' + Math.round(Math.max(11, H * 0.028)) + 'px Spectral, Georgia, serif';
    c.textAlign = 'center'; c.textBaseline = 'middle'; c.fillText(String(src.pdf), W / 2, H / 2);
  }
  const tex = obTex(gl, slot, key, cv);
  cv.width = cv.height = 0;   // (on the graphics card now: its memory let go of straight away)
  return tex;
}
// Triangles on the graphics card: positions, normals, colours (a shade each), texture positions, and indices.
function obMesh(gl, made, m){
  // Each triangle wound so that its front is the side its normals face (the light falls on the front).
  const P = m.pos, Nn = m.nrm, I = m.idx;
  for (let t = 0; t < I.length; t += 3) {
    const [a, b, c] = [I[t], I[t + 1], I[t + 2]], v = i => [P[3 * i], P[3 * i + 1], P[3 * i + 2]];
    const A = v(a), B = v(b), C = v(c), e1 = B.map((x, i) => x - A[i]), e2 = C.map((x, i) => x - A[i]);
    const cr = [e1[1] * e2[2] - e1[2] * e2[1], e1[2] * e2[0] - e1[0] * e2[2], e1[0] * e2[1] - e1[1] * e2[0]];
    let dot = 0; for (const i of [a, b, c]) for (let j = 0; j < 3; j++) dot += cr[j] * Nn[3 * i + j];
    if (dot < 0) { I[t + 1] = c; I[t + 2] = b; }
  }
  const vao = gl.createVertexArray(); gl.bindVertexArray(vao); made.push(['VertexArray', vao]);
  for (const [loc, data, size] of [[0, m.pos, 3], [1, m.nrm, 3], [2, m.col, 4], [3, m.uv, 2]]) {
    const b = gl.createBuffer(); made.push(['Buffer', b]); gl.bindBuffer(gl.ARRAY_BUFFER, b); gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(data), gl.STATIC_DRAW);
    gl.enableVertexAttribArray(loc); gl.vertexAttribPointer(loc, size, gl.FLOAT, false, 0, 0);
  }
  const ib = gl.createBuffer(); made.push(['Buffer', ib]); gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, ib);
  gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, new Uint32Array(m.idx), gl.STATIC_DRAW);
  gl.bindVertexArray(null);
  return {vao, count:m.idx.length};
}
const obNew = () => ({pos:[], nrm:[], col:[], uv:[], idx:[]});
function obVert(m, p, n, uv, shade){
  const l = Math.hypot(...n) || 1, s = Math.pow(shade === undefined ? 1 : shade, 2.2);
  m.pos.push(...p); m.nrm.push(n[0] / l, n[1] / l, n[2] / l); m.col.push(s, s, s, 1); m.uv.push(...uv);
  return m.pos.length / 3 - 1;
}
// A flat four-sided face, its corners in order round it.
function obQuad(m, pts, n, uvs, shades){
  const i = pts.map((p, j) => obVert(m, p, n, uvs ? uvs[j] : [0, 0], shades ? shades[j] : 1));
  m.idx.push(i[0], i[1], i[2], i[0], i[2], i[3]);
}
/* The book's shape: the parts to draw ({mesh, tex or colour}). Lying open at spread k, each side is as the book open
   at k has it. While a leaf goes over, each side is as it'll be with the leaf off it (spec: the spread each side is as,
   kL and kR, and the page on top of each, pL and pR): the leaf itself is drawn over them (obLeaf).
   The book is the model itself, opened: its two boards, just as the model has them (covers, insides, turn-ins, the
   photos on their edges), and its spine, just as the model has it (its round, as deep as the model's, the spine photo,
   the raised bands, the headcaps and their photos, the headbands), neither of them changed in shape, only moved; and
   between them, the leaves, in two stacks with the model's page edges on them. The pages lie level, as on a reading
   cradle. The spine turns round with the book as it opens: at the endpapers it stands at the end of the closed book on
   the other side, exactly as the model has it closed (the open board lying level with the top of the leaves, as a
   board swung open does); open in the middle, it hangs under the book between the boards, its round down; in between,
   it turns gradually from the one to the other. The leaves end at the back of the book, inside the spine, as in the
   model; the headcaps close the spine's ends over them. */
const OB_BOARD = new Set(['front', 'back', 'insideFront', 'insideBack', 'endpaper', 'rim', 'board']);
const OB_SPINE = new Set(['spine', 'headcap', 'tailcap', 'capSide', 'headWall', 'headband']);
function obBuild(gl, spec){
  const d = RD.b3, look = RD.look, Wp = RD.W / RD.H, sq = rdMargin() / RD.H, k = 1 / (2 * d.py1);
  const mm = M3.cache.get(RD.model), data = mm.data, gpu = m3Gpu(gl, mm);
  const Tn = Math.max(0.01, d.zi / d.py1), bt = Math.max(0.004, (d.zo - d.zi) / (2 * d.py1));
  const n = Math.max(1, RD.n), fOf = kk => Math.min(1, Math.max(0, 2 * kk / n));
  const hasL = 2 * spec.kL >= 1 && spec.pL >= 1, hasR = 2 * spec.kR + 1 <= RD.n && spec.pR <= RD.n;
  // (while a leaf goes over, how far in the book lies open goes on smoothly from where it was to where it'll be,
  // as the leaf goes: spec.fc)
  const fcL = spec.fc === undefined ? fOf(spec.kL) : spec.fc, fcR = spec.fc === undefined ? fOf(spec.kR) : spec.fc;
  const stack = [hasL ? Math.max(0.0015, Tn * fcL) : 0, hasR ? Math.max(0.0015, Tn * (1 - fcR)) : 0];
  const rest = [null, null], shades = [null, null], lay = [null, null];   // (lay: where the top leaf of each side lies, u along it from the fold)   // (the top of each side, and its shade, for the leaf to lie on)
  const Y = 0.5, s = Tn * 0.5 + bt;   // (s: half the closed book's thickness, the width of the spine from joint to joint)
  // How far into the book it's open (0 at the front, 1 at the back); sn is 0 at either end and 1 in the middle.
  const f = (fcL + fcR) / 2, sn = Math.sin(Math.PI * f);
  // The spine's chord (from the front board's side, CL, to the back board's, CR: the model's spine from the front
  // cover's outside to the back cover's), turned so that the pages lie level: upright at either end, level in the
  // middle. The board on the thick side keeps to its end of it; the one on the thin side lies a little lower than its
  // end, level with the top of the leaves, as a board swung open over its joint does (lam, gone by the middle).
  // (towards the ends, the spine's front edge comes down level with the top of the leaves, the board having gone from
  // over it: the spine a little shorter across, Lc, just as the cover swinging open leaves it)
  const Lc = 2 * s - (bt + 0.002) * (1 - sn), lam = (bt - 0.002) * (1 - sn);
  const sth = (f < 0.5 ? 1 : -1) * Math.min(1, (Tn * Math.abs(1 - 2 * f) + lam) / Lc), cth = Math.sqrt(Math.max(0, 1 - sth * sth));
  const Mz = Lc / 2 * Math.abs(sth), CL = [-Lc / 2 * cth, Mz + Lc / 2 * sth], CR = [Lc / 2 * cth, Mz - Lc / 2 * sth];
  const c = [(CR[0] - CL[0]) / Lc, (CR[1] - CL[1]) / Lc], B = [c[1], -c[0]];   // (along the chord; and out, away from the pages)
  // Each board: its outside at z0[side], its inside (the endpaper pasted down, and the leaves on it) at base[side].
  const z0 = f < 0.5 ? [CL[1] - lam, CR[1]] : [CL[1], CR[1] - lam], base = z0.map(z => z + bt);
  const zT = [base[0] + stack[0], base[1] + stack[1]];
  // The model's spine, moved into place: its joint line (x = xl) onto the chord, its round out from it.
  const spineAt = (x, z) => { const a = (d.zo - z) * k * Lc / (2 * s), b = (d.xl - x) * k; return [CL[0] + c[0] * a + B[0] * b, CL[1] + c[1] * a + B[1] * b]; };
  const spineN = (nx, nz) => [-nx * B[0] - nz * c[0], -nx * B[1] - nz * c[1]];
  // Where each board's edge is at the spine: at its end of the chord, as the model has it (where the spine turns past
  // the board on the thin side, it passes inside the board, out of sight, just as it does in the model).
  const xJ = [CL[0], CR[0]];
  // Each board lies out from there by as far as it's swung open from the spine (over the joint, which is out from
  // the back of the pages: rd3Gap), as the board swinging open in the model does: all of it where the spine stands
  // up and the board lies flat, half each in the middle of the book, where the spine hangs under it.
  const G = rd3Gap(d) * k, xB = [xJ[0] - G / 2 * (1 - c[1]), xJ[1] + G / 2 * (1 + c[1])];
  // (and no nearer the spine than where the spine's round comes down to the board's outside: where the round swells
  // out past the board's edge, the board lies out to meet it, rather than sitting on the spine)
  {
    const arcM = spineArc(data);
    for (const [side, sg] of [[0, -1], [1, 1]]) {
      const zq = (f < 0.5 ? [CL[1] - lam, CR[1]] : [CL[1], CR[1] - lam])[side];
      const pts = arcM.map(([x, z]) => spineAt(x, Math.max(-d.zo, Math.min(d.zo, z)))); if (!side) pts.reverse();
      for (let i = 0; i < pts.length - 1; i++) {
        const a = pts[i], b = pts[i + 1];
        if ((a[1] - zq) * (b[1] - zq) <= 0 && Math.abs(b[1] - a[1]) > 1e-12) {
          const xq = a[0] + (b[0] - a[0]) * (zq - a[1]) / (b[1] - a[1]);
          if (sg * (xq - xB[side]) > 0) xB[side] = xq;
          break;
        }
      }
    }
  }
  // Where the leaves of the two sides meet: on the back of the leaves (the chord, inside the spine), as far along it as
  // the book is open (with no leaves on one side, as while the first or the last leaf goes over, at that side's end).
  const fE = !stack[0] ? 0 : !stack[1] ? 1 : f, tf = Math.min(1, Math.max(0, (bt * sn + fE * (Lc - 2 * bt * sn)) / Lc));
  const chordAt = t => [CL[0] + c[0] * Lc * t, CL[1] + c[1] * Lc * t];
  const Gb = chordAt(tf), zG = Gb[1];
  const made = [], parts = [];
  const add = (m, how) => { if (m.idx.length) parts.push(Object.assign({mesh:obMesh(gl, made, m)}, how)); };
  // (the insides of the boards aren't repeated: at their edges, a repeated picture would bring in a sliver of the other edge)
  const mat = i => ({tex:gpu[i].tex || null, base:gpu[i].base || [1, 1, 1, 1], cut:gpu[i].cut || 0, lit:gpu[i].lit !== false,
    repeat:!['insideFront', 'insideBack', 'endpaper'].includes(data[i].name)});
  /* The endpaper running over the joint, from the board's edge (xb) in to the leaves (xg), at z: the board's own
     picture of it, from just beside the spine, at its true size and the same way round, ending at the spine's edge
     of the picture where it goes in among the leaves (as the free endpaper there carries on from it). */
  const obHinge = (xb, xg, z, side) => {
    const m = obNew(), YB = Y + sq;
    const ub = side ? 1 - hingeA[1] : hingeA[0], ug = side ? 0 : 1, xa = Math.min(xb, xg), xz = Math.max(xb, xg), ua = xa === xb ? ub : ug, uz = xa === xb ? ug : ub;
    obQuad(m, [[xa, YB, z], [xz, YB, z], [xz, -YB, z], [xa, -YB, z]], [0, 0, 1], [[ua, 0], [uz, 0], [uz, 1], [ua, 1]]);
    return m;
  };
  // A part of the model, moved: its triangles that keep (by their middle), each point through place().
  const moved = (p, keep, place, uvf) => {
    const m = obNew(), at = new Map();
    const v = i => {
      if (at.has(i)) return at.get(i);
      const r = place([p.pos[3 * i], p.pos[3 * i + 1], p.pos[3 * i + 2]], p.nrm ? [p.nrm[3 * i], p.nrm[3 * i + 1], p.nrm[3 * i + 2]] : [0, 0, 1]);
      const u = p.uv ? p.uv[2 * i] : 0;
      m.pos.push(...r[0]); m.nrm.push(...r[1]); m.col.push(1, 1, 1, 1); m.uv.push(uvf ? uvf(u) : u, p.uv ? p.uv[2 * i + 1] : 0);
      at.set(i, m.pos.length / 3 - 1); return at.get(i);
    };
    for (let t = 0; t < p.idx.length; t += 3) {
      const I = [p.idx[t], p.idx[t + 1], p.idx[t + 2]], mz = I.reduce((a, i) => a + p.pos[3 * i + 2], 0) / 3, mx = I.reduce((a, i) => a + p.pos[3 * i], 0) / 3;
      if (keep(mx, mz)) m.idx.push(v(I[0]), v(I[1]), v(I[2]));
    }
    return m;
  };
  // The boards. The front one lies open on the left, turned over round its joint; the back one on the right, as it is.
  const placeL = ([x, y, z], [nx, ny, nz]) => [[xB[0] - (x - d.xl) * k, y * k, (d.zi - z) * k + base[0]], [-nx, ny, -nz]];
  const placeR = ([x, y, z], [nx, ny, nz]) => [[xB[1] + (x - d.xl) * k, y * k, (z + d.zi) * k + base[1]], [nx, ny, nz]];
  const placeS = ([x, y, z], [nx, ny, nz]) => { const q = spineAt(x, z), nn = spineN(nx, nz); return [[q[0], y * k, q[1]], [nn[0], ny, nn[1]]]; };
  /* The endpaper pasted inside each board runs on over the joint (obHinge) to the leaves, as one sheet: the picture of
     the inside of the board is shared out over the two, the board taking all but the last sliver of it by the spine
     (squeezed by the width of the joint, too little to see), the joint that sliver, so that the pattern runs on
     unbroken from the one to the other. hingeA: the share the board takes, on each side. */
  const hingeA = [0, 1].map(side => {
    const Wb = (d.xr - d.xl) * k, end = stack[side] ? xJ[side] : Gb[0], w = Math.abs(xB[side] - end);
    return Wb / (Wb + w);
  });
  // (the front's picture has the spine at its right, 1; the back's at its left, 0)
  const insideUv = (name, side) => name === 'insideFront' && !side ? (u => u * hingeA[0]) : name === 'insideBack' && side ? (u => 1 - hingeA[1] + u * hingeA[1]) : null;
  let inside = [-1, -1], iSpine = -1;
  data.forEach((p, i) => {
    if (OB_BOARD.has(p.name)) {
      add(moved(p, (x, z) => z > 0, placeL, insideUv(p.name, 0)), mat(i)); add(moved(p, (x, z) => z < 0, placeR, insideUv(p.name, 1)), mat(i));
      if (p.name === 'insideFront' || (p.name === 'endpaper' && inside[0] < 0)) inside[0] = i;
      if (p.name === 'insideBack' || (p.name === 'endpaper' && inside[1] < 0)) inside[1] = i;
    } else if (p.name === 'headband') {
      // The headbands, open (obHeadbandShape): from joint to joint, over the heads (and tails) of all the leaves.
      add(moved(Object.assign({}, p, obHeadbandShape(p, d, 1, data)), () => true, placeS), mat(i));
    } else if (p.name === 'headWall') {
      // (the inside of the spine's end, behind the headband: the whole way across, from joint to joint)
      const pos = p.pos.slice(); for (let j = 2; j < pos.length; j += 3) pos[j] *= d.zo / d.zi;
      add(moved(Object.assign({}, p, {pos}), () => true, placeS), mat(i));
    } else if (OB_SPINE.has(p.name)) {
      if (p.name === 'spine') iSpine = i;
      // (the raised bands rise off the spine a little past its edges, where it meets the boards: open, that would
      // come up through the joint beside the first and last leaves, so they're kept within the spine's thickness)
      // (a headcap photographed reaches in over the leaves, closed; open, the covering turned in by the boards (below)
      // does that instead, and the two, lying together, would flicker)
      const inCap = (p.name === 'headcap' || p.name === 'tailcap') ? (x => x <= d.xl + 1e-6) : p.name === 'capSide' ? (() => false) : () => true;
      add(moved(p, (x) => inCap(x), p.name === 'spine' ? ([x, y, z], n) => placeS([x, y, Math.max(-d.zo, Math.min(d.zo, z))], n) : placeS), mat(i));
    }
  });
  // The joints, where the boards lie out from the spine: the covering running on from the spine's edge round the
  // board's edge, and (on the inside, below) the endpaper running over from the board to the leaves.
  // Each is the board carried on in to the spine, as thick as the board and as long, the covering running taut from
  // the board's outside edge onto the round of the spine (obJointFill), its ends at the head and the tail closed as
  // the board's edges are there; and where the leaves stop short of the ends, its side by them closed too.
  if (G > 0) {
    const YB = Y + sq, cover = obNew(), coverL = obNew(), coverR = obNew(), ends = obNew(), lipTop = obNew(), tile = rimTile(data) * k, arc0 = spineArc(data);
    for (const [side, sg] of [[0, -1], [1, 1]]) {
      const us = side ? 0.002 : 0.998, xe = xB[side], x0 = xJ[side], ze = z0[side], zb = base[side], Cc = side ? CR : CL;
      // (the spine's outline at its end, open, from its edge by this board outwards, halfway round)
      const arc = arc0.map(([x, z]) => { const zc = Math.max(-d.zo, Math.min(d.zo, z)), q = spineAt(x, zc); return [q[0], q[1], 1, (zc + d.zo) / (2 * d.zo)]; });
      if (!side) arc.reverse();
      // (the covering round the joint from this board's photo: the front's, on the left, runs 0 at the spine, the back's 1)
      const C = [Cc[0], Cc[1], 1], tx = {uS:side ? 0.994 : 0.006, dir:side ? -1 : 1, W:(d.xr - d.xl) * k}, jc = side ? coverR : coverL;
      if (arc.length) arc[0] = C;
      const cap = p => [sg * (p[0] - xe) / tile, Math.min(1, Math.max(0, (p[1] - ze) / Math.max(1e-6, zb - ze)))];
      // (the joint, from the board's edge to the spine's; none where the board's edge is right at the spine)
      if (Math.abs(x0 - xe) >= 1e-6) obJointFill(jc, ends, [xe, ze, 1], [xe, zb, 1], C, [x0, zb, 1], arc, YB, tx, cap, obGrooveR(d) * k, [-sg, 0]);
      if (zb - Cc[1] > 1e-6) for (const [ya, yb] of [[Y, YB], [-YB, -Y]])
        obQuad(cover, [[x0, ya, Cc[1]], [x0, yb, Cc[1]], [x0, yb, zb], [x0, ya, zb]], [sg, 0, 0], [[us, 0], [us, 0], [us, 1], [us, 1]]);
      // On the inside, beyond the heads (and tails) of the leaves, the covering turned in over the end of the spine
      // (as a headcap is) from the inside of the board, rounding down onto the back of the leaves by the headband:
      // so the board's end meets the spine across all its thickness, not at its outside edge only.
      const cin = side ? [-c[0], -c[1]] : [c[0], c[1]], up = [-B[0], -B[1]];
      const h = (x0 - Cc[0]) * up[0] + (zb - Cc[1]) * up[1], e = (x0 - Cc[0]) * cin[0] + (zb - Cc[1]) * cin[1];
      if (h > 1e-5) {
        const w = Math.max(e, 0) + h * 1.2, P = [Cc[0] + cin[0] * w, Cc[1] + cin[1] * w], K = [P[0] + up[0] * h, P[1] + up[1] * h], In = [x0, zb];
        const curve = []; for (let i = 0; i <= 12; i++) { const t = i / 12; curve.push([0, 1].map(q => (1 - t) * (1 - t) * P[q] + 2 * t * (1 - t) * K[q] + t * t * In[q])); }
        const poly = [[Cc[0], Cc[1], 1], ...curve.map(p => [p[0], p[1], 1])];
        for (const [ya, yb] of [[Y, YB], [-YB, -Y]]) {
          const Ym = (ya + yb) / 2, Yh = (yb - ya) / 2;
          // its two ends (towards the leaves, and at the book's end) and its rounded top
          // (its end level with the book's end, sharing its edge with the joint's end, so there's no crack between)
          for (const yy of [ya, yb]) {
            // (as the board's end is, so the two read as one)
            const b0 = ends.pos.length / 3, tri = obTriangulate(poly.map(p => [p[0], p[1]]));
            for (const p of poly) obVert(ends, [p[0], yy, p[1]], [0, Math.sign(yy - Ym) || 1, 0], cap(p));
            for (const t of tri) ends.idx.push(b0 + t);
          }
          // (and closed along the back of the leaves, underneath)
          obQuad(lipTop, [[Cc[0], yb, Cc[1]], [P[0], yb, P[1]], [P[0], ya, P[1]], [Cc[0], ya, Cc[1]]], [B[0], 0, B[1]], [[us, 0], [us, 0], [us, 1], [us, 1]]);
          for (let i = 0; i < curve.length - 1; i++) {
            const a = curve[i], b = curve[i + 1], n = [b[1] - a[1], 0, a[0] - b[0]];
            if (Math.hypot(n[0], n[2]) > 1e-9)
              obQuad(lipTop, [[a[0], yb, a[1]], [b[0], yb, b[1]], [b[0], ya, b[1]], [a[0], ya, a[1]]], n, [[us, 0], [us, 0], [us, 1], [us, 1]]);
          }
        }
      }
    }
    add(cover, iSpine >= 0 ? mat(iSpine) : {colour:obColour(look.spineColour, [90, 30, 30])});
    { const iF = data.findIndex(p => p.name === 'front'), iB = data.findIndex(p => p.name === 'back');
      const fb = {colour:obColour(look.spineColour, [90, 30, 30])};
      add(coverL, iF >= 0 ? mat(iF) : fb); add(coverR, iB >= 0 ? mat(iB) : iF >= 0 ? mat(iF) : fb); }
    add(lipTop, iSpine >= 0 ? mat(iSpine) : {colour:obColour(look.spineColour, [90, 30, 30])});

    const iRim = data.findIndex(p => p.name === 'rim'), iBoard = data.findIndex(p => p.name === 'board');
    add(ends, iRim >= 0 ? mat(iRim) : iBoard >= 0 ? mat(iBoard) : {colour:obColour(look.spineColour, [90, 30, 30])});
  }
  // The page edges: the model's (plain, gilt, sprinkled or a photo), laid on as the model lays them.
  const iEdge = data.findIndex(p => p.name === 'edges'), iGilt = data.findIndex(p => p.name === 'giltEdge');
  let reps = 1; if (iEdge >= 0) { const uv = data[iEdge].uv; for (let i = 0; i < uv.length; i += 2) reps = Math.max(reps, Math.round(uv[i])); }
  const faces = {head:obNew(), tail:obNew(), fore:obNew()};
  // (across the edges, from the back board's side, 0, to the front's, 1: each point by the leaf it's on)
  const across = (side, z) => Math.min(1, Math.max(0, side ? (1 - f) * (z - base[1]) / Math.max(1e-6, stack[1]) : 1 - f * (z - base[0]) / Math.max(1e-6, stack[0])));
  // A flat face at the head or the tail (y), between two paths (lists of [x, z]) running the same way, joined up
  // point by point once each is shared out evenly along its length. Along the leaves, the photo runs from the fold to
  // the fore-edge of each leaf (fore(z): where the fore-edge is at that height), as the model has it from the spine
  // to the fore-edge: the leaves fanning out further than a page's width at the bottom of the stack, it's stretched
  // with them to their ends (measured in pages' widths, it would run off its end there and start again).
  const between = (m, y, top, bot, shTop, shBot, side, fore) => {
    const even = (P, N) => {
      const L = [0]; for (let i = 1; i < P.length; i++) L.push(L[i - 1] + Math.hypot(P[i][0] - P[i - 1][0], P[i][1] - P[i - 1][1]));
      const tot = L[L.length - 1], out = [];
      for (let q = 0; q <= N; q++) {
        if (!(tot > 1e-9)) { out.push(P[0]); continue; }
        const at = tot * q / N; let i = 1; while (i < P.length - 1 && L[i] < at) i++;
        const u = (at - L[i - 1]) / Math.max(1e-12, L[i] - L[i - 1]);
        out.push([P[i - 1][0] + (P[i][0] - P[i - 1][0]) * u, P[i - 1][1] + (P[i][1] - P[i - 1][1]) * u]);
      }
      return out;
    };
    const N = 40, A = even(top, N), Bp = even(bot, N), b0 = m.pos.length / 3, sgs = side ? 1 : -1;
    const uvOf = ([x, z]) => [Math.min(1, Math.max(0, sgs * x) / Math.max(1e-6, Math.abs(fore(z)))) * reps, across(side, z)];
    for (let q = 0; q <= N; q++) { obVert(m, [A[q][0], y, A[q][1]], [0, Math.sign(y), 0], uvOf(A[q]), shTop); obVert(m, [Bp[q][0], y, Bp[q][1]], [0, Math.sign(y), 0], uvOf(Bp[q]), shBot); }
    for (let q = 0; q < N; q++) { const a = b0 + 2 * q; m.idx.push(a, a + 1, a + 3, a, a + 3, a + 2); }
  };
  for (const [side, sg] of [[0, -1], [1, 1]]) {
    const x0 = xJ[side], zi = base[side];
    // With no leaves on it, the leaf going over lies down on the board itself; and the endpaper pasted on the board
    // carries on over the joint to where the leaves begin.
    if (!stack[side]) {
      rest[side] = () => zi; lay[side] = u => [Gb[0] + sg * u, zi];
      if (inside[side] >= 0 && Math.abs(Gb[0] - xB[side]) > 1e-5) add(obHinge(xB[side], Gb[0], zi, side), Object.assign(mat(inside[side]), {repeat:false}));
      continue;
    }
    // (the endpaper over the joint, from the board's edge in to the leaves)
    if (inside[side] >= 0 && Math.abs(xB[side] - x0) > 1e-5) add(obHinge(xB[side], x0, zi, side), Object.assign(mat(inside[side]), {repeat:false}));
    // The stack of leaves on it, its top leaf (the page) curving down into the gutter, drawn in to the fold.
    const top = Math.max(zT[side], zG + 0.0005), g = 0.05 * Wp + 1.2 * (top - zG) + 0.02, us = [];
    const gw = Math.max(g, 2.5 * Math.abs(Gb[0])), X = u => sg * u + Gb[0] * Math.pow(Math.max(0, 1 - u / gw), 2);
    for (let i = 0; i <= 28; i++) us.push(g * Math.pow(i / 28, 1.6));
    for (let i = 1; i <= 6; i++) us.push(g + (Wp - g) * i / 6);
    // (over the board it stays on the board, going down to the fold only past the board's edge)
    const zAt0 = u => u >= g ? top : zG + (top - zG) * Math.sqrt(Math.max(0, 1 - Math.pow(1 - u / g, 2)));
    const zAt = u => sg * (X(u) - x0) > 0 ? Math.max(zAt0(u), zi + 0.0003) : zAt0(u);
    const slope = u => { const e = 1e-4; return (zAt(Math.min(Wp, u + e)) - zAt(Math.max(0, u - e))) / (2 * e); };
    const shadeAt = u => 1 - 0.3 * Math.pow(Math.max(0, 1 - u / (g * 1.4)), 2);
    rest[side] = zAt; shades[side] = shadeAt; lay[side] = u => [X(u), zAt(u)];
    const page = obNew();
    for (const u of us) {
      const z = zAt(u), nn = [-sg * slope(Math.max(u, 1e-3)), 0, 1], tu = side ? u / Wp : 1 - u / Wp;
      obVert(page, [X(u), Y, z], nn, [tu, 0], shadeAt(u)); obVert(page, [X(u), -Y, z], nn, [tu, 1], shadeAt(u));
    }
    for (let i = 0; i < us.length - 1; i++) { const a = 2 * i; page.idx.push(a, a + 1, a + 3, a, a + 3, a + 2); }
    add(page, {tex:obPage(gl, side ? spec.pR : spec.pL), colour:[1, 1, 1, 1], lod:OB_LOD});
    // The leaves' edges at the head and the tail: over the board, from the top leaf down to the board; and by the
    // spine, from the top leaf and the fold down to the back of the leaves (the chord), from this side's board to the fold.
    const ue = Math.max(0, sg * x0), over = [ue, ...us.filter(u => u > ue)], near = [...us.filter(u => u < ue), ue].reverse();
    const t0 = side ? 1 - bt * sn / Lc : bt * sn / Lc, backPath = [[x0, zi]];
    for (let i = 0; i <= 12; i++) backPath.push(chordAt(t0 + (tf - t0) * i / 12));
    const topPath = [...near.map(u => [X(u), zAt(u)]), Gb];
    // (each leaf reaches a page's width out from its fold: the bottom one, folded by the board, as far out as the board
    // lets it, the top one to where the page is shown; the fore-edge slopes between them, as the leaves fan out)
    const xFb = backPath[1][0] + sg * Wp, xFt = sg * Wp, zF = zz => xFb + (xFt - xFb) * (zz - zi) / Math.max(1e-6, top - zi);
    const botAt = u => x0 + (xFb - x0) * (u - ue) / Math.max(1e-6, Wp - ue);
    for (const [y, m] of [[Y, faces.head], [-Y, faces.tail]]) {
      between(m, y, over.map(u => [u >= Wp ? xFt : X(u), zAt(u)]), over.map(u => [botAt(u), zi]), 0.97, 0.8, side, zF);
      between(m, y, topPath, backPath, 0.93, 0.8, side, zF);
    }
    const fe = faces.fore, fb = fe.pos.length / 3;
    for (const [yy, zz] of [[Y, zi], [-Y, zi], [-Y, top], [Y, top]]) obVert(fe, [zF(zz), yy, zz], [sg, 0, sg * (xFb - xFt) / Math.max(1e-6, top - zi)], [(0.5 - yy) * reps, across(side, zz)], zz === zi ? 0.8 : 0.97);
    fe.idx.push(fb, fb + 1, fb + 2, fb, fb + 2, fb + 3);
  }
  const edgeMat = i => i >= 0 ? mat(i) : {colour:obColour(look.edges && look.edges.colour, [228, 223, 211])};
  add(faces.head, edgeMat(iGilt >= 0 ? iGilt : iEdge)); add(faces.tail, edgeMat(iEdge)); add(faces.fore, edgeMat(iEdge));
  // The height of what lies on top, anywhere across the book (x): found along each side's top leaf as it lies, drawn
  // in towards the fold as it is, so that a leaf coming down on it, or lifting off it, lies just on it.
  const tops = lay.map(f => { if (!f) return null; const P = []; for (let i = 0; i <= 80; i++) P.push(f(Wp * Math.pow(i / 80, 1.6))); return P; });
  const surfAt = x => {
    const P = tops[x >= Gb[0] ? 1 : 0]; if (!P) return zG;
    const inc = P[P.length - 1][0] > P[0][0], lo = inc ? P[0] : P[P.length - 1], hi = inc ? P[P.length - 1] : P[0];
    if (x <= lo[0]) return lo[1]; if (x >= hi[0]) return hi[1];
    let a = 0, b = P.length - 1;
    while (b - a > 1) { const m = (a + b) >> 1; if ((P[m][0] < x) === inc) a = m; else b = m; }
    const q = (x - P[a][0]) / ((P[b][0] - P[a][0]) || 1e-9); return P[a][1] + (P[b][1] - P[a][1]) * q;
  };
  return {parts, made, zc:zG, geo:{Wp, Y, zG, gx:Gb[0], rest, shades, lay, surfAt}};
}
function obFree(gl){ if (RD.ob && RD.ob.gl === gl) for (const [kind, obj] of RD.ob.made) gl['delete' + kind](obj); RD.ob = null; }
// A leaf going over in 3D (rdAnimate): {kind:'curl', mode:'anim', anim:{d3:true, ...}, u: how far it's gone, 0 to 1}.
const obLeafTurn = t => !!t && t.kind === 'curl' && t.mode === 'anim' && !!t.anim && !!t.anim.d3;
// What lies where: the book open at its spread; or, with a leaf going over, each side as it'll be with the leaf off
// it (the side it leaves already showing the page under it, the side it goes to still the page it'll cover), and the
// leaf's two sides (front, the page going over; back, the page on its other side). As the flat book has them.
function obSpec(t){
  const k = RD.spread, L = 2 * k, R = 2 * k + 1;
  if (!obLeafTurn(t)) return {kL:k, kR:k, pL:L, pR:R};
  const step = t.step || 1, front = t.dir > 0 ? R : L, back = front + t.dir * (2 * step - 1), under = front + 2 * step * t.dir;
  // How far into the book it lies open, going on from the spread it was open at to the one it'll be open at just
  // as the leaf goes over (as obLeaf has it go), so that the spine and the leaves on each side move with it,
  // smoothly, all the way over, rather than at its start and its end.
  const n = Math.max(1, RD.n), fo = kk => Math.min(1, Math.max(0, 2 * kk / n)), p = ease(Math.min(1, Math.max(0, t.u || 0)));
  const fc = fo(k) + (fo(k + t.dir * step) - fo(k)) * p;
  return t.dir > 0 ? {kL:k, kR:k + step, pL:L, pR:under, front, back, fc} : {kL:k - step, kR:k, pL:under, pR:R, front, back, fc};
}
/* The leaf going over. It's fixed at the spine and goes over round it, bending as paper does: its outer edge goes
   ahead as it lifts (as a page taken by its edge does), the part by the spine following, so that in the middle of its
   way it arches over; and the corner it was taken by (the bottom one, turned by a click or a key, as the flat book
   has it) goes a little ahead of the other, so it goes over a little on the slant. Wherever it would go into the
   pages it lies on or comes down on, it lies on them instead: it starts as the top page of the one side, and ends as
   the top page of the other. Its two sides are drawn separately, each with its own page, each seen only from its
   own side. Made once for each turn; its shape is worked out afresh for each picture. */
const OB_NU = 56, OB_NV = 14, OB_LIFT = 0.0025;
function obLeaf(gl, L, t, sp){
  const ob = RD.ob, G = ob.geo, sg = t.dir > 0 ? 1 : -1, NU = OB_NU, NV = OB_NV, cols = NU + 1, rows = NV + 1;
  let lf = ob.leaf;
  if (!lf || lf.sg !== sg) {
    const us = [], uvF = [], uvB = [], idxF = [], idxB = [], N = cols * rows;
    for (let i = 0; i <= NU; i++) us.push(G.Wp * Math.pow(i / NU, 1.5));   // (closer together by the spine, where it bends most)
    for (let j = 0; j < rows; j++) for (let i = 0; i < cols; i++) {
      const a = us[i] / G.Wp, v = j / NV;
      // (each side's page laid on as it lies on its own side of the book: a right-hand page from the spine outwards)
      uvF.push(sg > 0 ? a : 1 - a, v); uvB.push(sg > 0 ? 1 - a : a, v);
    }
    for (let j = 0; j < NV; j++) for (let i = 0; i < NU; i++) {
      const a = j * cols + i, b = a + 1, c = a + cols + 1, d = a + cols, A = [a, c, b, a, d, c], B = [a, b, c, a, c, d];
      idxF.push(...(sg > 0 ? A : B)); idxB.push(...(sg > 0 ? B : A));   // (each wound to face its own way)
    }
    lf = ob.leaf = {sg, us, pos:new Float32Array(3 * N), nf:new Float32Array(3 * N), nb:new Float32Array(3 * N), col:new Float32Array(4 * N)};
    const mk = (target, data, usage) => { const b = gl.createBuffer(); ob.made.push(['Buffer', b]); gl.bindBuffer(target, b); gl.bufferData(target, data, usage); return b; };
    gl.bindVertexArray(null);
    lf.bPos = mk(gl.ARRAY_BUFFER, lf.pos, gl.DYNAMIC_DRAW); lf.bCol = mk(gl.ARRAY_BUFFER, lf.col, gl.DYNAMIC_DRAW);
    lf.bNf = mk(gl.ARRAY_BUFFER, lf.nf, gl.DYNAMIC_DRAW); lf.bNb = mk(gl.ARRAY_BUFFER, lf.nb, gl.DYNAMIC_DRAW);
    const face = (bn, uv, idx) => {
      const vao = gl.createVertexArray(); ob.made.push(['VertexArray', vao]); gl.bindVertexArray(vao);
      for (const [loc, b, size] of [[0, lf.bPos, 3], [1, bn, 3], [2, lf.bCol, 4]]) { gl.bindBuffer(gl.ARRAY_BUFFER, b); gl.enableVertexAttribArray(loc); gl.vertexAttribPointer(loc, size, gl.FLOAT, false, 0, 0); }
      mk(gl.ARRAY_BUFFER, new Float32Array(uv), gl.STATIC_DRAW); gl.enableVertexAttribArray(3); gl.vertexAttribPointer(3, 2, gl.FLOAT, false, 0, 0);
      mk(gl.ELEMENT_ARRAY_BUFFER, new Uint32Array(idx), gl.STATIC_DRAW);
      gl.bindVertexArray(null);
      return {vao, count:idx.length};
    };
    lf.front = face(lf.bNf, uvF, idxF); lf.back = face(lf.bNb, uvB, idxB);
    // Its shadow: a sheet lying over the pages on both sides (following them down into the gutter), each point as
    // dark as the leaf above it makes it, laid over them by multiplying.
    const xs = [], spos = [], sn = [], sc = [], si = [], NS = 36;
    for (let i = -NS; i <= NS; i++) xs.push(Math.sign(i) * G.Wp * Math.pow(Math.abs(i) / NS, 1.4));
    const surf0 = G.surfAt;
    for (let i = 0; i < xs.length; i++) xs[i] += G.gx;
    for (let j = 0; j < rows; j++) for (const x of xs) { spos.push(x, G.Y - 2 * G.Y * j / NV, surf0(x)); sn.push(0, 0, 1); sc.push(1, 1, 1, 1); }
    const sw = xs.length;
    for (let j = 0; j < NV; j++) for (let i = 0; i < sw - 1; i++) { const a = j * sw + i; si.push(a, a + 1, a + sw + 1, a, a + sw + 1, a + sw); }
    lf.sxs = xs; lf.scol = new Float32Array(sc);
    const vao = gl.createVertexArray(); ob.made.push(['VertexArray', vao]); gl.bindVertexArray(vao);
    const at = (loc, data, size, usage) => { const b = mk(gl.ARRAY_BUFFER, data, usage); gl.enableVertexAttribArray(loc); gl.vertexAttribPointer(loc, size, gl.FLOAT, false, 0, 0); return b; };
    at(0, new Float32Array(spos), 3, gl.STATIC_DRAW); at(1, new Float32Array(sn), 3, gl.STATIC_DRAW);
    lf.bScol = at(2, lf.scol, 4, gl.DYNAMIC_DRAW); at(3, new Float32Array(2 * spos.length / 3), 2, gl.STATIC_DRAW);
    mk(gl.ELEMENT_ARRAY_BUFFER, new Uint32Array(si), gl.STATIC_DRAW);
    gl.bindVertexArray(null);
    lf.shadow = {vao, count:si.length};
  }
  // Its shape now. p: how far over it is (easing in and out); the angle it leaves the spine at, and the angle its
  // outer edge is at (0 lying on the side it started from, pi on the other).
  const p = ease(Math.min(1, Math.max(0, t.u || 0))), us = lf.us, pos = lf.pos;
  const aH = Math.PI * Math.pow(p, 1.8), aE = Math.PI * (1 - Math.pow(1 - p, 1.8));
  const lead = 0.42 * Math.sin(Math.PI * p), cs = t.cy > RD.H / 2 ? -1 : 1;   // (the corner taken: the bottom, or the top)
  const surf = G.surfAt, sm = (a, b, v) => { const q = Math.min(1, Math.max(0, (v - a) / (b - a))); return q * q * (3 - 2 * q); };
  // (at its start it's just as its page lay, and at its end just as it'll lie, point for point, so that the print on
  // it doesn't shift as it lifts off or comes down: the bend worked out below is eased into and out of those)
  const lay0 = G.lay[sg > 0 ? 1 : 0], lay1 = G.lay[sg > 0 ? 0 : 1], b0 = lay0 ? 1 - sm(0, 0.22, p) : 0, b1 = lay1 ? sm(0.78, 1, p) : 0;
  for (let j = 0; j < rows; j++) {
    const y = G.Y - 2 * G.Y * j / NV, e = Math.min(Math.PI, Math.max(0, aE + lead * 0.5 * cs * y / G.Y));
    let x = 0, z = G.zG;
    for (let i = 0; i < cols; i++) {
      if (i) {
        const ds = us[i] - us[i - 1], a = aH + (e - aH) * Math.pow((us[i] + us[i - 1]) / 2 / G.Wp, 1.2);
        x += sg * Math.cos(a) * ds; z += Math.sin(a) * ds;
      }
      const o = 3 * (j * cols + i);
      // (drawn in to the fold near the spine, as the pages are, and reaching just as far out as they do)
      const xx = x + G.gx * Math.pow(Math.max(0, 1 - us[i] / (0.3 * G.Wp)), 2);
      const lift = OB_LIFT * Math.min(1, us[i] / 0.02);
      let px = xx, pz = Math.max(z, surf(xx) + lift);
      if (b0 > 0) { const q = lay0(us[i]); px += (q[0] - px) * b0; pz += (q[1] + lift - pz) * b0; }
      if (b1 > 0) { const q = lay1(us[i]); px += (q[0] - px) * b1; pz += (q[1] + lift - pz) * b1; }
      pos[o] = px; pos[o + 1] = y; pos[o + 2] = Math.max(pz, surf(px) + lift);
    }
  }
  // Which way each side faces, from the shape; and its shade, in the gutter as it lies on either side.
  const P = (i, j) => { const o = 3 * (Math.min(rows - 1, Math.max(0, j)) * cols + Math.min(cols - 1, Math.max(0, i))); return [pos[o], pos[o + 1], pos[o + 2]]; };
  const r0 = 1 - sm(0, 0.18, p), r1 = sm(0.82, 1, p), shS = G.shades[sg > 0 ? 1 : 0], shE = G.shades[sg > 0 ? 0 : 1];
  for (let j = 0; j < rows; j++) for (let i = 0; i < cols; i++) {
    const a = P(i + 1, j), b = P(i - 1, j), c = P(i, j - 1), d = P(i, j + 1);
    const du = [a[0] - b[0], a[1] - b[1], a[2] - b[2]], dy = [c[0] - d[0], c[1] - d[1], c[2] - d[2]];
    let n = [du[1] * dy[2] - du[2] * dy[1], du[2] * dy[0] - du[0] * dy[2], du[0] * dy[1] - du[1] * dy[0]];
    const l = (Math.hypot(...n) || 1) * sg; n = n.map(v => v / l);
    const o = 3 * (j * cols + i);
    for (let q = 0; q < 3; q++) { lf.nf[o + q] = n[q]; lf.nb[o + q] = -n[q]; }
    const u = us[i], s = Math.pow(Math.max(0.05, 1 - (1 - (shS ? shS(u) : 1)) * r0 - (1 - (shE ? shE(u) : 1)) * r1), 2.2);
    lf.col.set([s, s, s, 1], 4 * (j * cols + i));
  }
  // The shadow it casts on the pages under it and beside it: the light a little from the left, so a leaf standing
  // up throws its shadow a little to the right; deep where the leaf is close over the page, soft and faint where
  // it's high above. It comes and goes with the leaf's first and last stretch, so there's no jump as it starts and lands.
  const fadeS = sm(0, 0.1, p) * (1 - sm(0.9, 1, p)), sx = lf.sxs, sw = sx.length, hs = new Float32Array(cols), xp = new Float32Array(cols);
  for (let j = 0; j < rows; j++) {
    for (let i = 0; i < cols; i++) { const o = 3 * (j * cols + i), h = Math.max(0, pos[o + 2] - surf(pos[o])); hs[i] = h; xp[i] = pos[o] + 0.35 * h; }
    for (let q = 0; q < sw; q++) {
      let dark = 0;
      for (let i = 0; i < cols; i++) {
        const h = hs[i], sg2 = 0.012 + 0.22 * h, d = (sx[q] - xp[i]) / sg2;
        if (d > -3 && d < 3) { const w = Math.exp(-h / 0.55 - d * d); if (w > dark) dark = w; }
      }
      const v = Math.pow(1 - 0.45 * fadeS * dark, 2.2);
      lf.scol.set([v, v, v, 1], 4 * (j * sw + q));
    }
  }
  for (const [b, data] of [[lf.bPos, pos], [lf.bNf, lf.nf], [lf.bNb, lf.nb], [lf.bCol, lf.col], [lf.bScol, lf.scol]]) { gl.bindBuffer(gl.ARRAY_BUFFER, b); gl.bufferSubData(gl.ARRAY_BUFFER, 0, data); }
  if (fadeS > 0) {
    // (laid on the pages, not over the leaf: drawn before it, leaving no depth of its own, pulled just clear of the pages)
    gl.enable(gl.BLEND); gl.blendFunc(gl.DST_COLOR, gl.ZERO); gl.depthMask(false);
    gl.enable(gl.POLYGON_OFFSET_FILL); gl.polygonOffset(-2, -8);
    m3Part(gl, L, {vao:lf.shadow.vao, count:lf.shadow.count, base:[1, 1, 1, 1], cut:0, lit:false, tex:null});
    gl.disable(gl.POLYGON_OFFSET_FILL); gl.depthMask(true); gl.disable(gl.BLEND);
  }
  gl.enable(gl.CULL_FACE); gl.cullFace(gl.BACK); gl.frontFace(gl.CCW);
  for (const [mesh, pg] of [[lf.front, sp.front], [lf.back, sp.back]]) {
    const tex = obPage(gl, pg);
    gl.bindTexture(gl.TEXTURE_2D, tex); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
    m3Part(gl, L, {vao:mesh.vao, count:mesh.count, base:[1, 1, 1, 1], cut:0, lit:true, tex, lod:OB_LOD});
  }
  gl.disable(gl.CULL_FACE);
}
// Draws the open book in 3D over the reader, where the flat one would be (and a leaf going over, if one is). False
// if it can't be.
function obDraw(){
  const f = m3Full(); if (!f) return false;
  const {gl, L} = f, t = RD.turn, sp = obSpec(t);
  const key = [sp.kL, sp.kR, sp.pL, sp.pR, t && obLeafTurn(t) ? t.dir + ':' + (t.step || 1) : '', sp.fc === undefined ? '' : sp.fc.toFixed(5), RD.n, RD.W, RD.H, RD.dpr, RD.look && RD.look.headband,
    [sp.pL, sp.pR].map(p => { const e = RD.cache.get(p); return e ? e.pgen + ':' + e.canvas.width : '-'; }).join()].join('|');
  if (!RD.ob || RD.ob.gl !== gl || RD.ob.key !== key) { obFree(gl); RD.ob = Object.assign(obBuild(gl, sp), {gl, key}); }
  for (const p of [sp.pL, sp.pR]) obPage(gl, p);   // (the pages lying open kept as used)
  const st = $('readerStage').getBoundingClientRect();
  const x = st.left + RD.ox + RD.shift + RD.W, y = st.top + RD.oy + RD.H / 2;
  // Face on, as the model is drawn as a cover swings (so the one follows on from the other), from as far off (in
  // pages' heights rather than the model's units), and held as RV has it: turned about the gutter.
  const dist = RD3_FAR / (2 * RD.b3.py1), proj = m3Aim(x + RV.panX, y + RV.panY, RD.H * RV.zoom, dist, f.SW, f.SH, Math.max(0.05, dist - 3), dist + 3);
  const view = rvView(dist, [0, 0, 0], m4.trs([0, 0, -RD.ob.zc]));
  gl.uniformMatrix4fv(L.uProj, false, proj);
  gl.uniformMatrix4fv(L.uView, false, view);
  RD.obPV = {pv:m4.mul(proj, view), SW:f.SW, SH:f.SH};
  gl.uniform1f(L.uBright, M3_REST_BRIGHT); gl.uniform1i(L.uSwing, 0);
  for (const p of RD.ob.parts) {
    if (p.tex) { gl.bindTexture(gl.TEXTURE_2D, p.tex); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, p.repeat ? gl.REPEAT : gl.CLAMP_TO_EDGE); }
    m3Part(gl, L, {vao:p.mesh.vao, count:p.mesh.count, base:p.base || (p.tex ? [1, 1, 1, 1] : p.colour), cut:p.cut || 0, lit:p.lit !== false, tex:p.tex || null, lod:p.lod});
  }
  if (obLeafTurn(t)) obLeaf(gl, L, t, sp);
  gl.bindVertexArray(null); gl.uniform1f(L.uBright, 0);
  const cx = f.cv.getContext('2d'); cx.setTransform(1, 0, 0, 1, 0, 0); cx.clearRect(0, 0, f.W, f.H); cx.drawImage(f.g, 0, 0);
  const cv = $('readerFlight');
  clearTimeout(RD.v3Timer); cv.hidden = false; cv.classList.remove('landing', 'entering'); RD.v3 = true;
  return true;
}
function readerSay(text){ const n = $('readerNote'); n.textContent = text || ''; n.hidden = !text; }
const readerKey = name => 'journal-reader:' + name;
/* The book's pages. A PDF read on its own is its pages, 1 to RD.n. Made into a book with a model, the PDF's first
   page (its cover, the model being the cover now) is left out; and with the model's endpapers, the book begins with
   the free endpaper (a leaf of the endpaper, its decorated side facing the one pasted inside the board, its back
   plain) and ends with another, the last facing the back board (with a blank page before it, if the PDF's pages
   would leave it on the wrong side). What page p of the book is: {pdf: the PDF's page}, {end:true} the endpaper's
   decorated side, or {blank:true}. */
function rdSrc(p){
  if (!RD.ends) return {pdf:p + RD.skip};
  if (p === 1 || p === RD.n) return {end:true};
  const q = p - 2;
  return q >= 1 && q <= RD.pdfN ? {pdf:q + RD.skip} : {blank:true};
}
function rdSetPages(numPages){
  RD.skip = RD.model && numPages > 1 ? 1 : 0; RD.pdfN = numPages - RD.skip;
  RD.ends = !!(RD.look && RD.look.endsheet);
  if (!RD.ends) { RD.n = RD.pdfN; return; }
  let a = 2 + RD.pdfN;
  if ((a + 1) % 2 === 0) a++;   // the last leaf starts on a right-hand page
  RD.n = a + 2;
}
const rdReady = p => !rdSrc(p).pdf || RD.cache.has(p);
// The page of the book (p) that shows the PDF's page q (as the PDF numbers it), or the nearest there is.
function rdOfPdf(q){
  const k = Math.max(RD.skip + 1, Math.min(RD.skip + RD.pdfN, q)) - RD.skip;
  return RD.ends ? k + 2 : k;
}
const lastSpread = () => Math.floor(RD.n / 2);
const firstState = () => RD.look ? -1 : 0, lastState = () => RD.look ? lastSpread() + 1 : lastSpread();
async function openReader(name, title, model, lift){
  closeReaderDoc();
  const gen = ++RD.gen;
  const gone = () => gen !== RD.gen || FL.leaving;   // closed, or on its way back (it's set up no further)
  RD.open = true; RD.name = name; RD.model = model || null; rvReset();
  $('readerTitle').textContent = cleanTitle(title) || 'Untitled PDF';
  $('readerPages').textContent = ''; $('readerGo').value = ''; $('readerGo').disabled = true;
  for (const d of document.querySelectorAll('dialog[open]')) if (d !== $('bookReader')) d.close();
  // One of the journal's book models is read in the model itself (rd3Draw), with pages the shape of its page block.
  const mm = model && M3.cache.get(model);
  RD.b3 = mm && mm.data ? bookDims(mm.data) : null;
  if (RD.b3) RD.aspect = RD.b3.aspect;
  if (lift) $('bookReader').classList.add('flying');   // before it shows: the room darkens as the book comes, the reader waits under it
  if (!$('bookReader').open) $('bookReader').showModal();
  readerLayout();
  if (lift) flyBook(lift);
  drawReader();
  try {
    // (only if that's slow: the first time, it's downloaded)
    readerSay('');
    if (!pdfjsLib) setTimeout(() => { if (gen === RD.gen && !pdfjsLib) readerSay('Getting the page reader ready (the first time, this downloads it)\u2026'); }, 800);
    const look = model ? loadBookLook(model).catch(() => null) : Promise.resolve(null);
    const lib = await loadPdfjs();
    if (gone()) return;
    readerSay('');
    const task = lib.getDocument({url:pdfSrc(name), cMapUrl:'/pdfjs/cmaps/', cMapPacked:true,
      standardFontDataUrl:'/pdfjs/standard_fonts/', wasmUrl:'/pdfjs/wasm/', iccUrl:'/pdfjs/iccs/'});
    RD.task = task;
    const doc = await task.promise;
    if (gone()) return;
    const vp = (await doc.getPage(1)).getViewport({scale:1});
    RD.look = await look;
    if (!RD.b3 && RD.look) { const m3 = await loadModel(model).catch(() => null); RD.b3 = m3 && m3.data ? bookDims(m3.data) : null; }
    if (!RD.look) RD.b3 = null;
    obShowButton();
    if (gone()) return;
    RD.doc = doc; rdSetPages(doc.numPages);
    // In a book, the pages take the book's shape; on their own, the first page's.
    RD.aspect = Math.min(2, Math.max(0.25, RD.b3 ? RD.b3.aspect : RD.look ? RD.look.aspect : vp.width / vp.height));
    let saved = 0; try { saved = parseInt(localStorage.getItem(readerKey(name)), 10) || 0; } catch (e) {}
    saved = Math.min(lastSpread(), Math.max(0, saved));
    readerSay('');
    $('readerGo').disabled = false; $('readerGo').min = RD.skip + 1; $('readerGo').max = RD.skip + RD.pdfN;
    if (RD.look) {
      // Closed at first; once the pages it opens at are drawn (or after a moment), the cover swings open, at the
      // start, and then it's leafed through to where it was left (the pages it stops at on the way drawn first).
      const calm = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
      const path = calm ? [] : rdFlickPath(saved), first = path.length ? 0 : saved;
      RD.spread = -1; RD.target = first;
      for (const j of [first, ...path]) RD.keep.add(2 * j).add(2 * j + 1);
      RD.W = 0; readerLayout(); readerPagesText(); drawReader();
      RD.opening = true;
      if (FL.active && FL.arrived) await FL.arrived;   // (its pages are drawn once it's there, keeping still)
      const at = [2 * first, 2 * first + 1].filter(p => p >= 1 && p <= RD.n), t0 = performance.now();
      while (gen === RD.gen && performance.now() - t0 < 1500 && !at.every(rdReady)) await new Promise(r => setTimeout(r, 60));
      await flyLand(gen);
      await new Promise(r => setTimeout(r, 250));
      if (gen === RD.gen && RD.spread === -1 && !RD.turn && !FL.leaving && !FL.active) {
        await rdStill();
        rdRigid(-1, first, 'turn');
        while (gen === RD.gen && RD.turn && RD.turn.kind === 'rigid') await new Promise(r => setTimeout(r, 30));
        if (gen === RD.gen && RD.spread === first) await rdFlick(path, gen);
      }
      if (gen === RD.gen) { RD.keep.clear(); RD.opening = RD.hold = false; readerWant(); }
    } else {
      RD.spread = saved;
      RD.W = 0; readerLayout(); readerPagesText(); drawReader();
      await flyLand(gen);
    }
    rdCanvas.focus();
  } catch (err) {
    if (gone()) return;
    flyLand(gen);
    readerSay(err && err.message === 'pdfjs'
      ? "Couldn't get the page reader (pdf.js). It's downloaded once from the internet into journal/pdfjs: check the connection and try again."
      : "This PDF couldn't be opened as a book. It may be damaged, or locked with a password.");
  }
}
function closeReaderDoc(){
  flyStop();
  RD.b3 = null; RD.v3 = false; clearTimeout(RD.v3Timer);
  RD.gen++; RD.pgen++;
  // (one still loading is let go of once it's loaded: stopped halfway, pdf.js complains)
  if (RD.task) { const task = RD.task, end = () => task.destroy().catch(() => {}); if (RD.doc) end(); else task.promise.then(end, end); }
  RD.task = RD.doc = RD.look = RD.model = RD.target = null; RD.n = RD.skip = RD.pdfN = 0; RD.ends = false; RD.cache.clear(); RD.hi.clear(); RD.keep.clear(); RD.opening = RD.hold = false; RD.next = []; RD.queue = []; RD.turn = null; RD.open = false;
  if (RD.raf) { cancelAnimationFrame(RD.raf); RD.raf = 0; }
}
// The book as large as fits, and the canvas at the screen's own sharpness.
// How far the boards reach past the pages: as far as the model's do, for one of the journal's book models.
const rdMargin = () => RD.b3 ? RD.H * RD.b3.sq : Math.max(8, RD.H * 0.024);
// How tall a page is, for a book of pages this shape lying open (two pages across) on a stage this size.
const readerFit = (sw, sh, aspect) => { const pad = Math.max(28, Math.min(sw, sh) * 0.05); return Math.max(40, Math.min(sh - 2 * pad, (sw - 2 * pad) / (2 * aspect))); };
function readerLayout(){
  const st = $('readerStage'), r = st.getBoundingClientRect(), dpr = window.devicePixelRatio || 1;
  const sw = r.width, sh = r.height;
  if (!sw || !sh) return;
  // The canvas exactly as many of the screen's pixels as it has of its own, lying on whole ones: stretched by even
  // a fraction of a pixel (the stage being a fraction of a pixel wide, or starting part-way into one), the whole
  // book would be blurred a little as it's shown.
  const cw = Math.floor(sw * dpr), ch = Math.floor(sh * dpr);
  if (rdCanvas.width !== cw || rdCanvas.height !== ch) { rdCanvas.width = cw; rdCanvas.height = ch; }
  rdCanvas.style.width = cw / dpr + 'px'; rdCanvas.style.height = ch / dpr + 'px';
  const fx = r.left * dpr - Math.round(r.left * dpr), fy = r.top * dpr - Math.round(r.top * dpr);
  rdCanvas.style.transform = fx || fy ? `translate(${-fx / dpr}px,${-fy / dpr}px)` : '';
  const H = readerFit(sw, sh, RD.aspect), W = H * RD.aspect;
  const changed = Math.abs(W - RD.W) > 0.5 / dpr || Math.abs(H - RD.H) > 0.5 / dpr || dpr !== RD.dpr;   // (a page drawn for a size even a pixel off would have to be stretched)
  RD.W = W; RD.H = H; RD.dpr = dpr; RD.oy = Math.round((sh - H) / 2 * dpr) / dpr;
  // The spine on a line between two of the screen's pixels: there the two pages meet exactly, with no pixel half of
  // one and half of the other (which shows as a pale thread down the middle).
  RD.ox = Math.round(sw / 2 * dpr) / dpr - W;
  if (changed) {
    if (RD.turn) { const t = RD.turn; RD.turn = null; if (t.mode === 'anim' && t.anim.done === 'turn') rdFinish(t); }
    RD.faceA = RD.faceB = null;
    RD.pgen++; readerWant();   // pages are drawn again at the new size (the old ones stand in meanwhile)
  }
}
new ResizeObserver(() => { if (RD.open) { readerLayout(); drawReader(); } }).observe($('readerStage'));
function readerPagesText(){
  const k = RD.spread;
  const all = RD.skip + RD.pdfN;   // pages are numbered as the PDF numbers them
  if (RD.look && (k < 0 || k > lastSpread())) {
    $('readerPages').textContent = (k < 0 ? 'Closed' : 'Closed at the back') + ' (' + all + ' pages)';
    if (document.activeElement !== $('readerGo')) $('readerGo').value = '';
    return;
  }
  const at = [2 * k, 2 * k + 1].filter(p => p >= 1 && p <= RD.n).map(rdSrc), shown = at.filter(s => s.pdf).map(s => s.pdf);
  $('readerPages').textContent = shown.length === 1 ? 'Page ' + shown[0] + ' of ' + all
    : shown.length ? 'Pages ' + shown[0] + '\u2013' + shown[1] + ' of ' + all : at.some(s => s.end) ? 'Endpapers' : '';
  if (document.activeElement !== $('readerGo')) $('readerGo').value = shown[0] || '';
}
function rdGoTo(k){
  RD.spread = Math.max(firstState(), Math.min(lastState(), k)); RD.target = null;
  if (RD.spread >= 0 && RD.spread <= lastSpread()) try { localStorage.setItem(readerKey(RD.name), String(RD.spread)); } catch (e) {}
  readerPagesText(); readerWant();
}
function rdJump(page){
  if (!RD.doc) return;
  RD.turn = null;
  rdGoTo(Math.floor(rdOfPdf(page) / 2));
  drawReader();
}

/* Drawing the pages: those near the open ones (or the ones it's about to open at), nearest first, one at a time. */
function readerWant(){
  if (!RD.doc) return;
  const k = Math.max(0, Math.min(lastSpread(), RD.target !== null ? RD.target : RD.spread)), at = 2 * k + 1;
  // (and, after the open ones, those it's about to be leafed through to: RD.keep)
  const want = p => p >= 1 && p <= RD.n && rdSrc(p).pdf && (RD.cache.get(p) || {}).pgen !== RD.pgen;
  RD.queue = [...new Set([at, at - 1, ...RD.keep, at + 1, at + 2, at - 2, at - 3, at + 3, at + 4, at - 4, at - 5])].filter(want);
  for (const p of [...RD.cache.keys()]) if (Math.abs(p - at) > 12 && !RD.keep.has(p)) RD.cache.delete(p);
  obHiWant(at);
  readerPump();
}
/* Sharper pages for the 3D book. The flat book's pages are drawn exactly as large as they're shown on it; in 3D they're
   seen at a slant and brought nearer, and stretched to that they'd blur. So for the 3D book, the pages near where it's
   open are drawn again (RD.hi), each as the PDF draws it, not stretched: twice as tall as a page shows on the screen,
   so that the graphics card's own half-size copy of it is just the screen's sharpness and, taken a little towards the
   larger one (OB_LOD), stays crisp at a slant; and the two lying open, as much taller again as the book's been brought
   nearer (in steps, so a little nearer doesn't draw them again), up to what the graphics card and memory allow. */
const OB_LOD = -0.5, OB_HI_MAX = 4096, OB_HI_AREA = 12e6, OB_HI_ALL = 48e6;   // (most pixels a side, a page, and all together)
function obHiH(open){
  const base = 2 * RD.H * Math.min(window.devicePixelRatio || 1, 2), z = open ? Math.max(1, RV.zoom) : 1;
  return Math.round(base * Math.pow(2, Math.ceil(Math.log2(z) * 2 - 1e-6) / 2));
}
function obHiWant(at){
  RD.hiQueue = [];
  if (!obActive() || RD.spread < 0 || RD.spread > lastSpread()) return;
  // the two lying open, then those a leaf going over would show (its two sides, and the page under it), either way
  for (const p of [at - 1, at, at + 1, at - 2, at + 2, at - 3]) {
    if (p < 1 || p > RD.n || !rdSrc(p).pdf) continue;
    const h = obHiH(p === at || p === at - 1), e = RD.hi.get(p);
    if (!e || e.h < h) RD.hiQueue.push([p, h]);
  }
  for (const p of [...RD.hi.keys()]) if (p < at - 3 || p > at + 2) RD.hi.delete(p);
}
// Too many pixels altogether: those furthest from where it's open go back to the size a page is drawn at, or go.
function obHiTrim(at){
  let all = 0; for (const e of RD.hi.values()) all += e.canvas.width * e.canvas.height;
  const far = [...RD.hi.keys()].sort((a, b) => Math.abs(b - at + 0.5) - Math.abs(a - at + 0.5));
  for (const p of far) {
    if (all <= OB_HI_ALL) break;
    if (p === at || p === at - 1) continue;
    const e = RD.hi.get(p); all -= e.canvas.width * e.canvas.height; RD.hi.delete(p);
  }
}
async function readerRenderHi(p, h){
  const doc = RD.doc, gen = RD.gen;
  const page = await doc.getPage(rdSrc(p).pdf), vp1 = page.getViewport({scale:1});
  const gl = m3Gl(), most = Math.min(OB_HI_MAX, gl ? gl.getParameter(gl.MAX_TEXTURE_SIZE) : OB_HI_MAX);
  // (as large as it fits on the page, as the flat book has it)
  const s = Math.min(Math.min(RD.W / vp1.width, RD.H / vp1.height) * h / RD.H, most / Math.max(vp1.width, vp1.height),
    Math.sqrt(OB_HI_AREA / (vp1.width * vp1.height)));
  const vp = page.getViewport({scale:s}), c = document.createElement('canvas');
  c.width = Math.max(1, Math.floor(vp.width)); c.height = Math.max(1, Math.floor(vp.height));
  const paper = RD.look && RD.look.paper;
  const task = RD.drawTask = page.render({canvas:c, canvasContext:c.getContext('2d'), viewport:vp, background:paper ? '#FFFFFF' : READER_PAPER});
  try { await task.promise; } finally { if (RD.drawTask === task) RD.drawTask = null; }
  page.cleanup();
  if (doc !== RD.doc || gen !== RD.gen) return;
  const old = RD.hi.get(p);
  if (old && old.h >= h) return;
  RD.hi.set(p, {canvas:c, h});
  obHiTrim(2 * Math.max(0, Math.min(lastSpread(), RD.spread)) + 1);
  drawReader();
}
async function readerPump(){
  if (RD.busy) return;
  RD.busy = true;
  try {
    while (RD.doc && RD.queue.length) {
      const p = RD.queue.shift();
      if ((RD.cache.get(p) || {}).pgen === RD.pgen) continue;
      // Not while anything's moving (drawing a page holds everything else up, and it would stutter): not while the
      // book is on its way up, nor, as it opens, while its cover or a leaf goes over (RD.hold), but between them;
      // and as it opens, only the pages it opens at and is leafed through to (the rest come after).
      if (RD.opening && !RD.keep.has(p)) continue;
      while (RD.doc && ((FL.active && !FL.landed && !FL.leaving && FL.t < 1) || FL.leaving || RD.hold || (RD.opening && RD.turn && RD.turn.mode === 'anim')))
        await new Promise(r => setTimeout(r, 30));
      if (!RD.doc) break;   // (closed meanwhile)
      RD.drawing = true;
      try { await readerRender(p); } catch (err) { /* a page that can't be drawn stays blank */ }
      finally { RD.drawing = false; }
    }
    // Then, for the 3D book, its sharper pages; not while it's being turned about or a leaf goes over (drawing one of
    // those takes a moment), nor while it's opening.
    while (RD.doc && RD.hiQueue && RD.hiQueue.length && !RD.queue.length) {
      if (RD.opening || RD.hold || RD.turn || RH.drag || FL.active || FL.leaving) { await new Promise(r => setTimeout(r, 60)); continue; }
      if (!obActive()) { RD.hiQueue = []; break; }
      const [p, h] = RD.hiQueue.shift(), e = RD.hi.get(p);
      if (e && e.h >= h) continue;
      RD.drawing = true;
      try { await readerRenderHi(p, h); } catch (err) { /* the flat book's drawing of it does */ }
      finally { RD.drawing = false; }
    }
  } finally { RD.busy = false; }
  if (RD.doc && RD.queue.length) readerPump();
}
async function readerRender(p){
  const doc = RD.doc, pgen = RD.pgen;
  const page = await doc.getPage(rdSrc(p).pdf), vp1 = page.getViewport({scale:1});
  // Drawn at exactly the size, in the screen's own pixels, that it's shown at when the book lies open at it: as wide
  // as its place is once the page edges beside it have taken their share (rdSlotAt), and as tall as it is. Shown
  // like that, it's copied onto the screen pixel for pixel, and the writing stays as sharp as pdf.js drew it; drawn
  // at any other size, it would have to be stretched to fit, and every letter would be softened.
  const fit = Math.min(RD.W / vp1.width, RD.H / vp1.height);
  const inn = rdEdgeSplit(p % 2 === 0, Math.floor(p / 2)).inn, sx = (RD.W - inn) / RD.W;
  const cw = Math.max(1, Math.round(vp1.width * fit * sx * RD.dpr)), ch = Math.max(1, Math.round(vp1.height * fit * RD.dpr));
  const ky = ch / vp1.height, vp = page.getViewport({scale:ky});
  const c = document.createElement('canvas'); c.width = cw; c.height = ch;
  const paper = RD.look && RD.look.paper;
  const task = RD.drawTask = page.render({canvas:c, canvasContext:c.getContext('2d'), viewport:vp,
    transform:[cw / (vp1.width * ky), 0, 0, 1, 0, 0], background:paper ? '#FFFFFF' : READER_PAPER});
  try { await task.promise; } finally { if (RD.drawTask === task) RD.drawTask = null; }
  page.cleanup();
  if (doc !== RD.doc) return;
  if (pgen === RD.pgen || !RD.cache.has(p)) RD.cache.set(p, {canvas:c, ratio:vp1.width / vp1.height, pgen});
  drawReader();
}

const polyPath = (c, pts) => { c.beginPath(); pts.forEach((s, i) => i ? c.lineTo(s.x, s.y) : c.moveTo(s.x, s.y)); c.closePath(); };
// The part of a polygon where f is 0 or more (f is a straight line's side, so one cut is enough).
function clipPoly(poly, f){
  const out = [];
  for (let i = 0; i < poly.length; i++) {
    const a = poly[i], b = poly[(i + 1) % poly.length], fa = f(a), fb = f(b);
    if (fa >= 0) out.push(a);
    if ((fa >= 0) !== (fb >= 0)) { const t = fa / (fa - fb); out.push({x:a.x + (b.x - a.x) * t, y:a.y + (b.y - a.y) * t}); }
  }
  return out;
}
// The paper the pages are printed on: the book's own (its model's Paper), or the reader's plain paper.
function rdPaper(c, x, y, w, h){
  const p = RD.look && RD.look.paper;
  if (p && p.img) c.drawImage(p.img, x, y, w, h);
  else { c.fillStyle = p && p.colour || READER_PAPER; c.fillRect(x, y, w, h); }
}
// A picture or a colour from the book, filling a rectangle.
function rdFill(c, m, x, y, w, h, fallback){
  if (m && m.img) c.drawImage(m.img, x, y, w, h);
  else { c.fillStyle = m && m.colour || fallback; c.fillRect(x, y, w, h); }
}
// The shade of a page curving down into the spine, from the spine (0) out to where it lies flat (1): a warm dark,
// as much of it as darkens the paper to those shades. (Laid on as it is, not multiplied in: some browsers, drawing on
// the graphics card, would now and then leave out the last shade multiplied in, so that one page or the other lost its
// shadow once the book lay still, and got it back as soon as anything moved.)
const RD_GUTTER = [[0, 132], [.03, 166], [.08, 192], [.18, 214], [.32, 231], [.5, 243], [.75, 251], [1, 255]]
  .map(([at, v]) => [at, 'rgba(30,22,14,' + Math.min(1, (1 - v / 255) * 1.13).toFixed(3) + ')']);
// The outline of a page lying open, its left edge at x (0 for the left page, W for the right). Curving down into
// the spine, the page sinks away from you there, and so looks a little shorter: its top and bottom edges dip in
// towards the middle over the last stretch before the spine (showing the hollow of the spine behind, above and
// below it).
function rdPageShape(c, x){
  const W = RD.W, H = RD.H, left = x === 0, gw = W * 0.14, dip = Math.min(H * 0.007, gw * 0.12), sx = left ? -1 : 1;
  c.beginPath();
  c.moveTo(left ? 0 : 2 * W, 0); c.lineTo(W + sx * gw, 0); c.quadraticCurveTo(W + sx * gw / 2, 0, W, dip);
  c.lineTo(W, H - dip); c.quadraticCurveTo(W + sx * gw / 2, H, W + sx * gw, H); c.lineTo(left ? 0 : 2 * W, H);
  c.closePath();
}
// Where the page curves down into the spine, it turns away from the light: a little darker at first, then quickly
// deeper, to a dark crease where the two pages meet. (strength: how much of it, 0 to 1)
function rdGutter(c, x, strength){
  if (strength !== undefined && strength <= 0) return;
  const W = RD.W, H = RD.H, left = x === 0, gw = W * 0.14;
  c.save();
  if (strength !== undefined) c.globalAlpha = Math.min(1, strength);
  const g = c.createLinearGradient(W, 0, left ? W - gw : W + gw, 0);
  for (const [at, col] of RD_GUTTER) g.addColorStop(at, col);
  c.fillStyle = g; c.fillRect(left ? W - gw : W, 0, gw, H);
  c.restore();
}
// One page, laid flat with its left edge at x (0 for the left page, W for the right); with shade (0 to 1) as much of
// the shade of the spine as it's in (all of it, lying flat; none, or true, for a leaf that's lifted).
function rdPage(c, p, x, shade){
  const W = RD.W, H = RD.H;
  const src = rdSrc(p), e = src.pdf && RD.cache.get(p);
  c.save();
  rdPageShape(c, x); c.clip();
  if (src.end) rdFill(c, RD.look.endsheet, x, 0, W, H, READER_PAPER);   // the endpaper's decorated side
  else rdPaper(c, x, 0, W, H);
  if (e) {
    let w = W, h = W / e.ratio;
    if (h > H) { h = H; w = H * e.ratio; }
    // On the book's own paper, the page is laid over it so that its white takes on the paper and its print stays
    // as dark as it is (it's drawn on white for that).
    const paper = RD.look && RD.look.paper;
    c.save();
    if (paper) c.globalCompositeOperation = 'multiply';
    const dx = x + (W - w) / 2, dy = (H - h) / 2, m = c.getTransform(), cv = e.canvas;
    // Lying flat where it'll be shown at the size it was drawn at: put down pixel for pixel, on the screen's own
    // pixels. Otherwise (a leaf on its way over, or a page drawn for another size, while it's drawn again) it's
    // scaled as finely as the browser can.
    // (Near enough: turned by less than a third of a pixel from end to end, as a leaf is just as it lands.)
    if (Math.abs(m.b) * w < 0.35 && Math.abs(m.c) * h < 0.35 && Math.abs(m.a * w - cv.width) < 1 && Math.abs(m.d * h - cv.height) < 1 && m.a > 0 && m.d > 0) {
      c.setTransform(1, 0, 0, 1, 0, 0);
      c.drawImage(cv, Math.floor(m.a * dx + m.e + 0.501), Math.floor(m.d * dy + m.f + 0.501));   // (half a pixel always the same way, whatever the rounding in the sums)
    } else {
      c.imageSmoothingQuality = 'high';
      c.drawImage(cv, dx, dy, w, h);
    }
    c.restore();
  } else if (src.pdf) {   // not drawn yet
    c.fillStyle = 'rgba(30,39,35,.3)'; c.font = 'italic ' + Math.round(Math.max(11, H * 0.028)) + 'px Spectral, Georgia, serif';
    c.textAlign = 'center'; c.textBaseline = 'middle'; c.fillText(String(src.pdf), x + W / 2, H / 2);
  }
  if (shade === undefined) rdGutter(c, x); else if (shade !== true) rdGutter(c, x, shade);
  c.restore();
}
// Page p in its place, on the left (x 0) or the right (x RD.W) of the book open at spread k: narrower by the page
// edges showing where its outer edge would be (rdEdgeSplit), drawn in towards the spine.
function rdSlotAt(c, p, x, k, shade){
  if (p < 1 || p > RD.n) return;
  const W = RD.W, inn = rdEdgeSplit(x === 0, k).inn;
  if (!inn) { rdPage(c, p, x, shade); return; }
  c.save(); c.translate(W, 0); c.scale((W - inn) / W, 1); c.translate(-W, 0); rdPage(c, p, x, shade); c.restore();
}
const rdSlot = (c, p, x) => rdSlotAt(c, p, x, RD.spread);
// How thick the edges of the pages on one side look: in a book, its thickness shared out by pages.
/* The edges of the pages on one side of the book open at spread k, seen beside the pages: count pages' worth. How
   much of them shows depends on where in the book it's open: most in the middle, where the pages fan up from the
   spine on both sides, and barely any at the start and the end, where they lie flat. The board is always the same
   size and always reaches past them: they lie first in its margin (out of them), and the rest (inn) where the top
   page's outer edge would be, that page being drawn that much narrower, as it looks curving up from the spine. */
function rdStack(count, k){
  if (!count || !RD.n) return 0;
  // As thick as that many leaves are (a leaf of paper is about a two-thousandth of the page's height; count pages are
  // half as many leaves), up to as much as the book can show.
  const f = Math.min(1, Math.max(0, 2 * k / RD.n)), most = RD.W * (RD.look ? Math.min(0.08, 0.02 + RD.look.thick * 0.3) : 0.035);
  return Math.max(1, Math.min(most, count / 2 * RD.H * 0.00045) * Math.sin(Math.PI * f));
}
function rdEdgeSplit(left, k){
  const t = rdStack(rdCount(left, k), k), out = Math.min(t, rdMargin() * 0.8);
  return {t, out, inn:t - out};
}
// The page edges, t wide, beside a page whose outer edge is at x0 (outwards to the left, for the left page).
function rdEdges(c, x0, t, left){
  const H = RD.H, ex = left ? x0 - t : x0, edges = RD.look && RD.look.edges;
  if (edges && edges.img) {
    const im = edges.img;
    if (im.width > im.height) { c.save(); c.translate(ex + t, 0); c.rotate(Math.PI / 2); c.drawImage(im, 0, 0, H, t); c.restore(); }
    else c.drawImage(im, ex, 0, t, H);
  } else {
    c.fillStyle = edges && edges.colour || READER_EDGE; c.fillRect(ex, 0, t, H);
    c.fillStyle = 'rgba(0,0,0,.09)';
    for (let i = ex + 1; i < ex + t; i += 2) c.fillRect(i, 0, 0.6, H);
  }
  const sh = c.createLinearGradient(x0, 0, left ? x0 - t : x0 + t, 0);   // falling away from the page on top
  sh.addColorStop(0, 'rgba(0,0,0,.18)'); sh.addColorStop(1, 'rgba(0,0,0,0)');
  c.fillStyle = sh; c.fillRect(ex, 0, t, H);
}
// How many pages lie on each side of the book open at spread k.
const rdCount = (left, k) => left ? 2 * k : Math.max(0, RD.n - 2 * k);
// One half of the open book at spread k: its board (the inside of the board, in a book), the edges of its
// pages (count pages' worth, if not all that lie on that side), and (with page) its page. The board of one of the journal's book models is drawn just as the model
// shows it (rd3Draw), so the one can take over from the other unseen.
function rdHalf(c, side, k, page, count){
  const W = RD.W, H = RD.H, b = rdMargin(), left = side === 'L', look = RD.look, model = !!RD.b3;
  const e = count === 0 ? {t:0, out:0, inn:0} : rdEdgeSplit(left, k), x = left ? -b : W, w = W + b;
  c.save();
  rdBoardPath(c, left); c.clip();
  const inside = look && (left ? look.insideL : look.insideR);
  rdFill(c, inside, x, -b, w, H + 2 * b, READER_BOARD);
  // The endpaper pasted down on it dips into the spine just as the pages do: where the pages' corners dip, the
  // covering shows above it (the picture's line just above the pages' edge, carried down), not the endpaper.
  if (model && inside && inside.img) {
    const im = inside.img, gw = W * 0.14, dip = Math.min(H * 0.007, gw * 0.12), sx = left ? -1 : 1, ry = im.height / (H + 2 * b);
    for (const top of [true, false]) {
      c.save();
      if (!top) { c.translate(0, H); c.scale(1, -1); }
      c.beginPath(); c.moveTo(W + sx * gw, 0); c.quadraticCurveTo(W + sx * gw / 2, 0, W, dip); c.lineTo(W, -0.5); c.lineTo(W + sx * gw, -0.5); c.closePath(); c.clip();
      const sy = top ? (b - 2) * ry : (H + b + 1) * ry, sh = ry;
      c.drawImage(im, 0, sy, im.width, sh, x, -1, w, dip + 1.5);
      c.restore();
    }
  }
  if (!model) {
    if (look) { c.lineWidth = 3; c.strokeStyle = look.board && look.board.colour || 'rgba(0,0,0,.4)'; c.stroke(); }   // the board's edge
    const sg = c.createLinearGradient(W, 0, left ? W - b * 2.2 : W + b * 2.2, 0);   // the hollow of the spine
    sg.addColorStop(0, 'rgba(0,0,0,.42)'); sg.addColorStop(1, 'rgba(0,0,0,0)');
    c.fillStyle = sg; c.fillRect(x, -b, w, H + 2 * b);
  }
  c.restore();
  if (e.t) rdEdges(c, left ? e.inn : 2 * W - e.inn, e.t, left);
  if (page) rdSlot(c, left ? 2 * k : 2 * k + 1, left ? 0 : W);
}
/* The spine of the open book. Between the boards, just above and below the pages, a little of the back of the book
   shows, with the joints where the boards hinge on either side of it. It isn't in the middle: the back of the book
   is shared out between the two sides as its leaves are, so that open near the start, the left side's share is small
   and the right's large; in the middle of the book, they're even. Down in the gutter, where the pages meet in the
   spine, the headbands (if the model has them): rolls of silk at the head and the tail of the pages, half of them
   standing past the pages' edges, the rest under the pages. Only for the journal's own book models. */
// How far the back of the book shows on the left and on the right of the middle (more, the more pages the book has);
// how much of its height shows at the gutter (h: all of it shows at the joints); f, how far through it's open (0 to 1).
function rdSpineSides(k){
  const d = RD.b3; if (!d) return {l:0, r:0, h:0, shift:0, half:1, f:0.5};
  const n = Math.max(1, RD.n), half = RD.W * Math.min(0.29, 0.07 + 0.22 * n / 600) / 2;
  const f = Math.min(1, Math.max(0, 2 * (k === undefined ? RD.spread : k) / n)), t = 1 - Math.sin(Math.PI * f);
  // Open near the front, the back of the book lies lower (less of it shows under the boards' edge), and further to
  // the left, the right board's edge with it; the left board, lying over the gutter, hides its left half, so only
  // what's right of the gutter shows. Going in, it rises and comes back to the middle, the left half coming out from
  // under its board, until in the middle of the book it lies square. Near the back, the same the other way round.
  const shift = (f < 0.5 ? 1 : -1) * half * 0.55 * t, x0 = -half - shift, x1 = half - shift;   // (from the gutter)
  const l = Math.max(0, Math.min(-x0, f < 0.5 ? half * (1 - t) : half)), r = Math.max(0, Math.min(x1, f < 0.5 ? half : half * (1 - t)));
  return {l, r, h:1 - 0.45 * t, f, shift, half};
}
// A board's outline as it lies open: its inner edge at the spine alongside the pages, but back at the joint above
// and below them, where the back of the book shows between the boards.
function rdBoardPath(c, left){
  const W = RD.W, H = RD.H, b = rdMargin(), sd = rdSpineSides(), s = left ? sd.l : sd.r, r = RD.b3 ? 0 : b * 0.5, u = 0;
  const o = left ? -b : 2 * W + b, j = left ? W - s : W + s, sx = left ? 1 : -1, t = b * sd.h;
  c.beginPath();
  c.moveTo(o, -b + r); if (r) c.quadraticCurveTo(o, -b, o + sx * r, -b); c.lineTo(W, -b); c.lineTo(W, -t); c.lineTo(j, -t); c.lineTo(j, u); c.lineTo(W, u);
  c.lineTo(W, H - u); c.lineTo(j, H - u); c.lineTo(j, H + t); c.lineTo(W, H + t); c.lineTo(W, H + b); c.lineTo(o + sx * r, H + b); if (r) c.quadraticCurveTo(o, H + b, o, H + b - r);
  c.closePath();
}
// The back of the book between the boards, above and below the pages, with the headband lying in it against the
// pages' edges: the model's own picture of it (so the open book shows just what the model did as the cover came
// down), its left half on the left of the spine and its right half on the right.
/* The picture of the back of the book as it shows between the boards above the pages: across, from the left
   board's edge to the right's; down, from the boards' edge to the pages'. (The tail has the same, the other way
   up.) The covering in the shadow of the hollow, and the headband lying straight across it against the pages. How
   much of it shows depends on where the book is open (rdSpineSides); the same picture goes on the model
   (rdWindowTex), so the two never differ. */
function rdWindowCanvas(k){
  const sd = rdSpineSides(k), look = RD.look || {}, hb = look.headband;
  const key = [hb ? hb.join() : '', look.spineColour].join('|');
  if (RD.winCv && RD.winCv.key === key) return RD.winCv;
  const Wc = 512, Hc = 128, cv = document.createElement('canvas'); cv.width = Wc; cv.height = Hc; cv.key = key;
  const x = cv.getContext('2d');
  const band = Hc * 0.3, rise = 0, up = 1;
  const yAt = u => { const w = up > 0 ? u : 1 - u; return Hc - band / 2 - rise * (1 - Math.sqrt(Math.max(0, 1 - w * w))); };
  // the covering, in the shadow of the hollow of the spine, and under the boards' edge
  x.fillStyle = look.spineColour || READER_BOARD; x.fillRect(0, 0, Wc, Hc);
  const v = x.createLinearGradient(0, 0, 0, Hc);
  v.addColorStop(0, 'rgba(0,0,0,.6)'); v.addColorStop(.25, 'rgba(0,0,0,.3)'); v.addColorStop(1, 'rgba(0,0,0,.45)');
  x.fillStyle = v; x.fillRect(0, 0, Wc, Hc);
  // under the headband's curve: the heads of the pages
  const N = 48, curve = []; for (let i = 0; i <= N; i++) curve.push([i / N * Wc, yAt(i / N)]);
  x.beginPath(); x.moveTo(0, Hc); for (const [px, py] of curve) x.lineTo(px, py + band * 0.3); x.lineTo(Wc, Hc); x.closePath();
  x.fillStyle = look.edges && look.edges.colour || READER_EDGE; x.fill();
  x.save(); x.clip(); x.strokeStyle = 'rgba(0,0,0,.08)'; x.lineWidth = 1;
  for (let yy = 0; yy < Hc; yy += 3) { x.beginPath(); x.moveTo(0, yy); x.lineTo(Wc, yy); x.stroke(); }
  x.restore();
  const line = () => { x.beginPath(); curve.forEach(([px, py], i) => i ? x.lineTo(px, py) : x.moveTo(px, py)); };
  if (hb) {
    x.lineCap = 'butt';
    line(); x.strokeStyle = 'rgba(0,0,0,.45)'; x.lineWidth = band * 1.15; x.stroke();   // its shadow
    line(); x.strokeStyle = hb[0]; x.lineWidth = band; x.stroke();
    line(); x.strokeStyle = hb[1]; x.lineWidth = band * 0.8; x.setLineDash([band * 0.35, band * 0.45]); x.stroke(); x.setLineDash([]);
    x.save(); x.translate(0, -band * 0.22); line(); x.strokeStyle = 'rgba(255,255,255,.22)'; x.lineWidth = band * 0.25; x.stroke(); x.restore();
    x.save(); x.translate(0, band * 0.3); line(); x.strokeStyle = 'rgba(0,0,0,.3)'; x.lineWidth = band * 0.3; x.stroke(); x.restore();
  } else { line(); x.strokeStyle = 'rgba(0,0,0,.35)'; x.lineWidth = 3; x.stroke(); }
  // the joints, where it goes in under the boards
  const s = x.createLinearGradient(0, 0, Wc, 0);
  s.addColorStop(0, 'rgba(0,0,0,.55)'); s.addColorStop(.1, 'rgba(0,0,0,.08)'); s.addColorStop(.9, 'rgba(0,0,0,.08)'); s.addColorStop(1, 'rgba(0,0,0,.55)');
  x.fillStyle = s; x.fillRect(0, 0, Wc, Hc);
  return RD.winCv = cv;
}
// That picture on the graphics card, for the model.
function rdWindowTex(gl, k){
  const cv = rdWindowCanvas(k), g3 = RD.g3;
  if (!g3.win || g3.win.cv !== cv) {
    const tex = g3.win ? g3.win.tex : gl.createTexture();
    gl.bindTexture(gl.TEXTURE_2D, tex);
    gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, false); gl.pixelStorei(gl.UNPACK_PREMULTIPLY_ALPHA_WEBGL, false);
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, cv);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
    g3.win = {cv, tex};
  }
  return g3.win.tex;
}
function rdSpine(c){
  const sd = rdSpineSides(); if (!RD.b3) return;
  const W = RD.W, H = RD.H, b = rdMargin(), img = rdWindowCanvas(RD.spread), iw = img.width, ih = img.height;
  for (const top of [true, false]) {
    c.save();
    if (!top) { c.translate(0, H); c.scale(1, -1); }   // the tail: the head's, the other way up
    // Only what the boards leave uncovered; the picture lies across the whole of it, from where it is, its top
    // (the part under the boards' edge) cut off, the rest (from the pages' edge up) showing.
    const t = b * sd.h;
    c.beginPath(); c.rect(W - sd.l, -t, sd.l + sd.r, t); c.clip();
    c.drawImage(img, 0, ih * (1 - sd.h), iw, ih * sd.h, W - sd.shift - sd.half, -t, 2 * sd.half, t);
    c.restore();
  }
}
/* The faces of a board, for a cover turning or lying closed, drawn onto a canvas the size of the board:
   the cover's outside; or the inside of the board with the page that lies on it (if any). A face for the
   left of the book has the spine along its right edge; one for the right, along its left. */
function rdFace(which, face){
  const W = RD.W, H = RD.H, b = rdMargin(), dpr = RD.dpr, bw = W + b, bh = H + 2 * b;
  let cv = RD[which];
  if (!cv || cv.width !== Math.round(bw * dpr) || cv.height !== Math.round(bh * dpr)) {
    cv = RD[which] = document.createElement('canvas'); cv.width = Math.round(bw * dpr); cv.height = Math.round(bh * dpr);
  }
  const c = cv.getContext('2d'), look = RD.look;
  c.setTransform(dpr, 0, 0, dpr, 0, 0); c.clearRect(0, 0, bw, bh);
  if (face.cover) {
    rdFill(c, look && look[face.cover], 0, 0, bw, bh, READER_BOARD);
    c.lineWidth = 3; c.strokeStyle = look && look.board && look.board.colour || 'rgba(0,0,0,.35)'; c.strokeRect(0, 0, bw, bh);
  } else {
    const left = face.side === 'L';
    rdFill(c, look && (left ? look.insideL : look.insideR), 0, 0, bw, bh, READER_BOARD);
    if (face.page >= 1 && face.page <= RD.n) {
      c.save(); c.translate(left ? b : -W, b); rdPage(c, face.page, left ? 0 : W); c.restore();
    }
  }
  return cv;
}
// A closed book lies with its front cover on the right of the spine (or, closed at the back, its back cover on
// the left), moved over so it's in the middle.
const rdShiftOf = k => !RD.look ? 0 : k < 0 ? -(RD.W + rdMargin()) / 2 : k > lastSpread() ? (RD.W + rdMargin()) / 2 : 0;
function drawReader(){
  const c = rdCtx, dpr = RD.dpr;
  c.setTransform(1, 0, 0, 1, 0, 0); c.clearRect(0, 0, rdCanvas.width, rdCanvas.height);
  if (!RD.n || !RD.W) return;
  const W = RD.W, H = RD.H, t = RD.turn;
  // (as a cover swings, the book comes to the middle as the board goes over, easing in and out as it does: it's
  // still once the board lies down, rather than carrying on after it)
  RD.shift = t && t.kind === 'rigid' ? rdShiftOf(t.from) + (rdShiftOf(t.to) - rdShiftOf(t.from)) * (1 - Math.cos(Math.PI * t.p)) / 2 : rdShiftOf(RD.spread);
  const base = [dpr, 0, 0, dpr, (RD.ox + RD.shift) * dpr, RD.oy * dpr];
  c.setTransform(...base);
  const k = RD.spread, rigid = !!t && t.kind === 'rigid';
  if (RD.b3 && (rigid || k < 0 || k > lastSpread()) && rd3Draw(t)) {
    // Just as the model comes into view over the open book, the open book is still drawn under it.
    if (rigid && performance.now() - RD.v3At < 200) {
      const f = rdRigidFaces(t);
      if (f.open >= 0 && f.open <= lastSpread()) {
        rdHalf(c, 'L', f.open, false); rdHalf(c, 'R', f.open, false); rdSpine(c);
        rdSlotAt(c, 2 * f.open, 0, f.open); rdSlotAt(c, 2 * f.open + 1, RD.W, f.open);
      }
    }
    return;
  }
  // A model book lying open, nothing moving: in 3D (see obDraw).
  if (obActive() && (!t || obLeafTurn(t)) && !FL.active && k >= 0 && k <= lastSpread() && obDraw()) return;
  rd3Leave();
  if (rigid) return drawRigid(c, t, base);
  if (k < 0 || k > lastSpread()) {   // closed
    const b = rdMargin(), front = k < 0, cv = rdFace('faceA', {cover:front ? 'front' : 'back'});
    c.save(); c.shadowColor = 'rgba(0,0,0,.45)'; c.shadowBlur = 30 * dpr; c.shadowOffsetY = 8 * dpr;
    c.fillStyle = READER_BOARD; c.fillRect(front ? W : -b, -b, W + b, H + 2 * b); c.restore();
    c.drawImage(cv, front ? W : -b, -b, W + b, H + 2 * b);
    return;
  }
  // A leaf being turned that's the last on its side takes the edges of the pages with it: none are left there.
  const step = t && t.kind === 'curl' && t.step || 1;   // (leafing through, a turn can go over several leaves at once)
  const last = t && t.kind === 'curl' ? (t.dir > 0 ? RD.n - 2 * (k + step) <= 0 : 2 * (k - step) <= 0) : false;
  rdHalf(c, 'L', k, false, last && t.dir < 0 ? 0 : undefined); rdHalf(c, 'R', k, false, last && t.dir > 0 ? 0 : undefined);
  rdSpine(c);
  const L = 2 * k, R = 2 * k + 1;
  const len = t ? Math.hypot(t.P.x - t.C.x, t.P.y - t.C.y) : 0;
  if (!t || len < 0.5) { rdSlot(c, L, 0); rdSlot(c, R, W); return; }
  // Turning forward, the right page goes over to the left; back, the left page comes over to the right.
  const dir = t.dir, x0 = dir > 0 ? W : 0, xo = dir > 0 ? 0 : W;
  const front = dir > 0 ? R : L, back = front + dir * (2 * step - 1), under = front + 2 * step * dir;
  rdSlot(c, dir > 0 ? L : R, xo);
  const C = t.C, P = t.P, M = {x:(C.x + P.x) / 2, y:(C.y + P.y) / 2}, n = {x:(P.x - C.x) / len, y:(P.y - C.y) / len};
  const side = s => (s.x - M.x) * n.x + (s.y - M.y) * n.y;   // below 0 on the corner's side of the fold
  const rect = [{x:x0, y:0}, {x:x0 + W, y:0}, {x:x0 + W, y:H}, {x:x0, y:H}];
  const lifted = clipPoly(rect, s => -side(s)), rest = clipPoly(rect, side);
  // For cutting the pages along the fold only: reaching well past the page (which has its own outline) on every
  // side, so that the page's own edges aren't cut again (a fraction of a pixel differently, flickering as the turn
  // starts and ends).
  const X = 60, rectX = [{x:x0 - X, y:-X}, {x:x0 + W + X, y:-X}, {x:x0 + W + X, y:H + X}, {x:x0 - X, y:H + X}];
  const liftedX = clipPoly(rectX, s => -side(s)), restX = clipPoly(rectX, side);
  const landK = k + dir * step;   // the spread it'll lie open at
  // The shading of the turn (the shadow the leaf casts, and the curve of it at the fold) fades out over its last
  // stretch, as it comes down flat where it lands: it doesn't all vanish at once as it lands, which flickered.
  const land = {x:2 * W - C.x, y:C.y}, fade = Math.min(1, Math.hypot(P.x - land.x, P.y - land.y) / (W * 0.45));
  // (the shade of the spine, on what's coming to lie in it, only in the very last of the leaf's way down)
  const shade = 1 - Math.min(1, Math.hypot(P.x - land.x, P.y - land.y) / (W * 0.05));
  const fa = a => 'rgba(0,0,0,' + (a * fade).toFixed(4) + ')', fw = a => 'rgba(255,255,255,' + (a * fade).toFixed(4) + ')';
  // Where the page has lifted away: the page after, in the shadow of the fold.
  if (lifted.length > 2) {
    c.save(); polyPath(c, liftedX); c.clip();
    // (as it'll lie once the leaf is over; and not in the shade of the spine until the leaf is all but down on it:
    // beside the leaf coming over, that shade would be seen as its outline, showing through it)
    rdSlotAt(c, under, x0, landK, shade);
    polyPath(c, lifted); c.clip();
    const sw = Math.max(4, Math.min(len * 0.35, W * 0.2)), g = c.createLinearGradient(M.x, M.y, M.x - n.x * sw, M.y - n.y * sw);
    g.addColorStop(0, fa(.3)); g.addColorStop(1, 'rgba(0,0,0,0)');
    c.fillStyle = g; c.fillRect(-W, -H, 4 * W, 3 * H);
    c.restore();
  }
  if (rest.length > 2) { c.save(); polyPath(c, restX); c.clip(); rdSlot(c, front, x0); c.restore(); }
  // The part turned over: the lifted part, mirrored across the fold, showing the back of the page.
  const refl = s => { const d = 2 * side(s); return {x:s.x - d * n.x, y:s.y - d * n.y}; };
  const flap = lifted.map(refl), flapX = liftedX.map(refl);
  if (flap.length > 2) {
    // Its shadow, cast round it (only round it: under it, what shows is what's under the leaf, where its corners dip
    // into the spine, just as it will once it's down).
    c.save();
    c.beginPath(); c.rect(-2 * W, -2 * H, 6 * W, 5 * H);
    flap.forEach((s, i) => i ? c.lineTo(s.x, s.y) : c.moveTo(s.x, s.y)); c.closePath(); c.clip('evenodd');
    c.shadowColor = fa(.32); c.shadowBlur = 16 * dpr * fade;
    polyPath(c, flap); c.fillStyle = RD.look && RD.look.paper && RD.look.paper.colour || READER_PAPER; c.fill(); c.restore();
    c.save(); polyPath(c, flapX); c.clip();
    // The back of the page lies flat on the other side once turned (the page mirrored across the spine), as narrow
    // as it will lie there; on its way over, that's mirrored again across the fold.
    const a = 1 - 2 * n.x * n.x, b = -2 * n.x * n.y, d = 1 - 2 * n.y * n.y, m = 2 * (M.x * n.x + M.y * n.y);
    c.transform(a, b, b, d, m * n.x, m * n.y);
    c.transform(-1, 0, 0, 1, 2 * W, 0);
    const narrow = (x, kk) => { const inn = rdEdgeSplit(x === 0, kk).inn; if (inn) { c.translate(W, 0); c.scale((W - inn) / W, 1); c.translate(-W, 0); } };
    narrow(xo, landK);
    if (back >= 1 && back <= RD.n) rdPage(c, back, xo, true);
    else { c.save(); rdPageShape(c, xo); c.clip(); rdPaper(c, xo, 0, W, H); c.restore(); }
    rdPageShape(c, xo); c.clip();
    c.setTransform(...base);
    // As it comes down, it comes into the shade of the spine, just as much as it will lie in once it's down.
    // (Each side's shade as that side's page lies there: the leaf's where it lands, and beyond the spine, the page
    // that'll lie there.)
    // (Only in the very last of its way down, so that it isn't seen as the shadow showing through the leaf.)
    c.save(); narrow(xo, landK); rdGutter(c, xo, shade); c.restore();
    c.save(); narrow(x0, landK); rdGutter(c, x0, shade); c.restore();
    // The paper curving over: shaded at the fold, catching the light just past it.
    const reach = Math.max(4, ...flap.map(side)), g = c.createLinearGradient(M.x, M.y, M.x + n.x * reach, M.y + n.y * reach);
    g.addColorStop(0, fa(.2)); g.addColorStop(.1, fw(.16)); g.addColorStop(.4, 'rgba(255,255,255,0)');
    g.addColorStop(1, fa(.07));
    c.fillStyle = g; c.fillRect(-W, -H, 4 * W, 3 * H);
    c.restore();
  }
}
/* A cover swinging round the spine: {kind:'rigid', dir, from, to, p}, p going 0 to 1 as it goes over.
   What stays still is the half of the open book on the far side (the book open at whichever of from and to
   is open); the board goes over it, showing face A on the side it starts from and face B on the side it
   lands on. Drawn in thin upright strips, each taller the nearer it has come. */
function rdRigidFaces(t){
  const front = Math.min(t.from, t.to) < 0, open = front ? Math.max(t.from, t.to) : Math.min(t.from, t.to);
  // Faces by where they lie: at the front, the cover is on the right when closed, and the inside of the
  // front board (with the left page of the spread it opens at) on the left; at the back, the inside of the
  // back board (with the right page) on the right, and the back cover on the left.
  const right = front ? {cover:'front'} : {side:'R', page:2 * open + 1}, left = front ? {side:'L', page:2 * open} : {cover:'back'};
  return {open, still:front ? 'R' : 'L', A:t.dir > 0 ? right : left, B:t.dir > 0 ? left : right};
}
function drawRigid(c, t, base){
  const W = RD.W, H = RD.H, b = rdMargin(), dpr = RD.dpr, f = rdRigidFaces(t);
  if (f.open >= 0 && f.open <= lastSpread()) rdHalf(c, f.still, f.open, true);
  const th = t.p * Math.PI, cs = Math.cos(th), sn = Math.sin(th), bw = W + b, bh = H + 2 * b;
  const xo = W + t.dir * bw * cs, onRight = xo > W;
  if (Math.abs(xo - W) < 0.5) return;
  const face = rdFace(onRight === (t.dir > 0) ? 'faceA' : 'faceB', onRight === (t.dir > 0) ? f.A : f.B);
  const grow = u => 1 + 0.12 * sn * u, edgeH = bh * grow(1);
  const outline = [{x:W, y:H / 2 - bh / 2}, {x:xo, y:H / 2 - edgeH / 2}, {x:xo, y:H / 2 + edgeH / 2}, {x:W, y:H / 2 + bh / 2}];
  // Its shadow on the book beneath, deepest as it's about to land.
  c.save(); c.shadowColor = 'rgba(0,0,0,' + (0.2 + 0.3 * Math.abs(cs)) + ')'; c.shadowBlur = (10 + 30 * sn) * dpr; c.shadowOffsetY = 6 * dpr;
  polyPath(c, outline); c.fillStyle = READER_BOARD; c.fill(); c.restore();
  const N = 72, fw = face.width, fh = face.height;
  for (let i = 0; i < N; i++) {
    const u0 = i / N, u1 = (i + 1) / N, x0 = W + (xo - W) * u0, x1 = W + (xo - W) * u1, h = bh * grow((u0 + u1) / 2);
    const sx = (onRight ? u0 : 1 - u1) * fw;
    c.drawImage(face, sx, 0, fw / N, fh, Math.min(x0, x1) - 0.3, H / 2 - h / 2, Math.abs(x1 - x0) + 0.6, h);
  }
  // Stood up, it's turned away from the light.
  polyPath(c, outline); c.fillStyle = 'rgba(0,0,0,' + (0.32 * sn) + ')'; c.fill();
}

/* Turning. A page turn is {kind:'curl', dir, cy, C, P}: which way (1 forward, -1 back), which corner (cy: its
   height, top or bottom), where that corner was (C) and where it is now (P). The corner is held to where a page
   fixed at the spine can reach. A cover is {kind:'rigid', ...} (above). */
// What turning this way from here does: a page turns ('curl'), a cover swings ('rigid'), or nothing.
function rdMove(dir){
  if (!RD.doc) return null;
  const k = RD.spread, K = lastSpread();
  if (RD.look) {
    if (k < 0) return dir > 0 ? {kind:'rigid', to:0} : null;
    if (k > K) return dir < 0 ? {kind:'rigid', to:K} : null;
    if (k === 0 && dir < 0) return {kind:'rigid', to:-1};
    if (k === K && dir > 0) return {kind:'rigid', to:K + 1};
  }
  return (dir > 0 ? 2 * k + 2 <= RD.n : k >= 1) ? {kind:'curl'} : null;
}
const canCurl = dir => { const m = rdMove(dir); return !!m && m.kind === 'curl'; };
const cornerOf = (dir, cy) => ({x:dir > 0 ? 2 * RD.W : 0, y:cy});
function rdClamp(t, p){
  const W = RD.W, H = RD.H, reach = [[{x:W, y:t.cy}, W], [{x:W, y:H - t.cy}, Math.hypot(W, H)]];
  let q = {x:p.x, y:p.y};
  for (let i = 0; i < 3; i++) for (const [a, r] of reach) {
    const dx = q.x - a.x, dy = q.y - a.y, dd = Math.hypot(dx, dy);
    if (dd > r) q = {x:a.x + dx * r / dd, y:a.y + dy * r / dd};
  }
  return q;
}
const newTurn = (dir, cy) => { const C = cornerOf(dir, cy); return {kind:'curl', dir, cy, C, P:{x:C.x, y:C.y}, goal:{x:C.x, y:C.y}, mode:'peek'}; };
const ease = u => u < .5 ? 2 * u * u : 1 - Math.pow(-2 * u + 2, 2) / 2;
function rdFinish(t){
  if (t.kind === 'rigid') rdGoTo(t.anim && t.anim.done === 'back' ? t.from : t.to);
  else rdGoTo(RD.spread + t.dir * (t.step || 1));
}
function rdTick(now){
  RD.raf = 0;
  const t = RD.turn; if (!t) return;
  let more = true;
  if (t.mode === 'anim') {
    const a = t.anim, u = Math.min(1, (now - a.t0) / a.dur), e = ease(u);
    if (t.kind === 'rigid') t.p = a.from + (a.to - a.from) * e;
    else if (a.d3) t.u = u;   // (the leaf eases in and out by itself)
    else t.P = rdClamp(t, {x:a.from.x + (a.to.x - a.from.x) * e, y:a.from.y + (a.to.y - a.from.y) * e + a.lift * Math.sin(Math.PI * e)});
    if (u >= 1) {
      if (t.kind === 'rigid' && RD.v3) drawReader();   // the model lying just so, for the reader's own drawing to take over from
      RD.turn = null; more = false;
      if (a.done === 'turn' || t.kind === 'rigid') rdFinish(t);
      // a turn asked for while this one went over comes next
      const next = RD.next.shift();
      if (next && RD.doc && !FL.leaving && !FL.active) { rdTurn(next); if (RD.turn) return; }
      RD.next = [];
    }
  } else if (t.kind === 'curl') {
    const g = rdClamp(t, t.goal), f = t.mode === 'drag' ? 0.5 : 0.22;
    t.P = {x:t.P.x + (g.x - t.P.x) * f, y:t.P.y + (g.y - t.P.y) * f};
    if (t.mode === 'peek' && Math.hypot(g.x - t.P.x, g.y - t.P.y) < 0.3) {
      more = false;
      if (t.leaving) RD.turn = null;   // back down flat
    }
  } else more = false;   // a cover held still
  drawReader();
  if (more) RD.raf = requestAnimationFrame(rdTick);
}
const rdKick = () => { if (!RD.raf) RD.raf = requestAnimationFrame(rdTick); };
// A page goes over (done 'turn') or falls back ('back') by itself, lifting a little on the way.
// (as fast as the Menu's page turning speed has it)
const rdPace = () => Math.max(0.25, Math.min(2, (settings.turnSpeed || 100) / 100));
function rdAnimate(t, done){
  // In 3D, a leaf goes over round the spine, bending (obLeaf); one that was only lifted just lies down again.
  if (t.kind !== 'rigid' && obActive()) {
    if (done !== 'turn') { RD.turn = null; drawReader(); return; }
    t.mode = 'anim'; t.u = 0;
    t.anim = {d3:true, t0:performance.now(), dur:(t.fast ? t.fast * 1.25 : 820) / rdPace(), done};
    RD.turn = t; rdKick();
    return;
  }
  const over = done === 'turn', pace = rdPace();
  t.mode = 'anim';
  if (t.kind === 'rigid') {
    const to = over ? 1 : 0;
    t.anim = {from:t.p, to, t0:performance.now(), dur:Math.max(200, 1100 * Math.abs(to - t.p)) / pace, done};
  } else {
    const to = over ? {x:t.dir > 0 ? 0 : 2 * RD.W, y:t.cy} : t.C;
    const far = Math.hypot(to.x - t.P.x, to.y - t.P.y) / (2 * RD.W);
    t.anim = {from:{x:t.P.x, y:t.P.y}, to, t0:performance.now(), dur:(t.fast || Math.max(160, (over ? 620 : 380) * Math.min(1, far * 1.2))) / pace,
      lift:(t.cy > RD.H / 2 ? -1 : 1) * RD.H * (over ? 0.16 : 0.03), done};
  }
  RD.turn = t; rdKick();
}
// A cover swinging from one state to another, by itself.
function rdRigid(from, to, done){
  const t = {kind:'rigid', dir:to > from ? 1 : -1, from, to, p:0};
  if (to >= 0 && to <= lastSpread()) RD.target = to;
  readerWant();
  rdAnimate(t, done);
}
/* Leafing through to where the book was left, once its cover is open: a few quick turns, the first pages one at a
   time and then several leaves at a time, however far in that is. Taking hold of it (or closing it) stops it. */
function rdFlickPath(to){
  const n = Math.min(to, 8), path = [];
  for (let i = 1; i <= n; i++) { const j = Math.round(to * Math.pow(i / n, 1.6)); if (j > (path[path.length - 1] || 0)) path.push(j); }
  return path;
}
// Page drawing held (the page being drawn let finish) while the book opens or a leaf goes over by itself.
async function rdStill(){
  RD.hold = true;
  const t0 = performance.now();
  while (RD.drawing && performance.now() - t0 < 1000) await new Promise(r => setTimeout(r, 15));
}
async function rdFlick(path, gen){
  const wait = ms => new Promise(r => setTimeout(r, ms));
  for (const [i, j] of path.entries()) {
    const from = RD.spread, going = () => gen === RD.gen && !FL.leaving && RD.spread === from;
    if (RD.turn && RD.turn.mode === 'peek') RD.turn = null;   // the pointer only resting near a corner
    if (!going() || RD.turn || j <= from) return;
    RD.target = j; RD.hold = false; readerWant();
    const t0 = performance.now();
    while (going() && !RD.turn && performance.now() - t0 < 1200 && ![2 * j, 2 * j + 1].every(p => p < 1 || p > RD.n || rdReady(p))) await wait(40);
    if (RD.turn && RD.turn.mode === 'peek') RD.turn = null;
    if (!going() || RD.turn) return;
    await rdStill();
    if (!going() || (RD.turn && RD.turn.mode !== 'peek')) return;
    RD.turn = null;
    const t = newTurn(1, RD.H);
    t.step = j - from; t.fast = path.length < 3 ? 520 : i === 0 || i === path.length - 1 ? 420 : 300;
    rdAnimate(t, 'turn');
    while (gen === RD.gen && RD.turn === t) await wait(30);
    if (RD.spread !== j) return;
  }
}
// A turn already on its way is finished at once.
function rdSettle(){
  const t = RD.turn; if (!t || t.mode !== 'anim') return;
  RD.turn = null;
  if (t.kind === 'rigid' || t.anim.done === 'turn') rdFinish(t);
}
// Turning by a click or a key. Asked while a page is going over, it waits for that one to land, so pages go over
// no faster than they turn: each click or key press (up to a few) is a turn to come, and a key held down one at a time.
function rdLater(dir, held){
  if (held ? !RD.next.length : RD.next.length < 3) RD.next.push(dir);
}
function rdTurn(dir, cy, held){
  const on = RD.turn;
  if (on && on.mode === 'anim') { if (on.anim.done === 'turn') { rdLater(dir, held); return; } rdSettle(); }
  const m = rdMove(dir);
  if (!m) { drawReader(); return; }
  if (m.kind === 'rigid') { rdRigid(RD.spread, m.to, 'turn'); return; }
  if (cy === undefined) cy = RD.H;
  const t = RD.turn && RD.turn.kind === 'curl' && RD.turn.dir === dir && RD.turn.cy === cy ? RD.turn : newTurn(dir, cy);
  rdAnimate(t, 'turn');
}
const rdPoint = ev => { const r = rdCanvas.getBoundingClientRect(); return {x:ev.clientX - r.left - RD.ox - RD.shift, y:ev.clientY - r.top - RD.oy}; };
// The corner the pointer is near, if that page can be turned: {dir, cy}.
function rdZone(p){
  const z = Math.max(28, Math.min(RD.W, RD.H) * 0.16);
  for (const dir of [1, -1]) {
    if (!canCurl(dir)) continue;
    for (const cy of [RD.H, 0]) { const c = cornerOf(dir, cy); if (Math.abs(p.x - c.x) < z && Math.abs(p.y - c.y) < z) return {dir, cy}; }
  }
  return null;
}
// Which way the page (or cover) under the pointer would turn: 1 on the right, -1 on the left, 0 off the book.
function rdSideAt(p){
  const b = rdMargin(), k = RD.spread;
  if (p.y < -b || p.y > RD.H + b) return 0;
  if (RD.look && k < 0) return p.x >= RD.W && p.x <= 2 * RD.W + b ? 1 : 0;   // the closed front cover
  if (RD.look && k > lastSpread()) return p.x >= -b && p.x <= RD.W ? -1 : 0;
  return p.x < -b || p.x > 2 * RD.W + b ? 0 : p.x >= RD.W ? 1 : -1;
}
rdCanvas.addEventListener('pointermove', ev => {
  if (!RD.doc || obActive()) return;
  const p = rdPoint(ev), t = RD.turn;
  if (t && t.mode === 'drag') {
    if (t.kind === 'rigid') t.p = Math.max(0, Math.min(1, t.p0 - t.dir * (ev.clientX - t.downX) / (2 * (RD.W + rdMargin()))));
    else t.goal = {x:p.x + t.grip.x, y:p.y + t.grip.y};
    if (Math.hypot(ev.clientX - t.downX, ev.clientY - t.downY) > 4) t.moved = true;
    t.trail.push({x:ev.clientX, time:ev.timeStamp}); while (t.trail.length > 2 && ev.timeStamp - t.trail[0].time > 90) t.trail.shift();
    if (t.kind === 'rigid') drawReader(); else rdKick();
    return;
  }
  if (t && t.mode === 'anim') return;
  // Near a corner, the page lifts a little, ready to be taken.
  const zone = obActive() ? null : rdZone(p), dir = rdSideAt(p);   // (in 3D, a page doesn't lift as the pointer nears its corner)
  rdCanvas.style.cursor = zone ? 'grab' : dir && rdMove(dir) ? 'pointer' : '';
  if (zone) {
    const nt = t && t.dir === zone.dir && t.cy === zone.cy ? t : newTurn(zone.dir, zone.cy), k = Math.min(RD.W, RD.H) * 0.07;
    nt.goal = {x:nt.C.x - zone.dir * k, y:nt.C.y + (zone.cy ? -k : k)}; nt.leaving = false;
    RD.turn = nt; rdKick();
  } else if (t) { t.goal = {x:t.C.x, y:t.C.y}; t.leaving = true; rdKick(); }
});
rdCanvas.addEventListener('pointerleave', () => {
  const t = RD.turn; if (obActive()) return;
  if (t && t.mode === 'peek') { t.goal = {x:t.C.x, y:t.C.y}; t.leaving = true; rdKick(); }
});
rdCanvas.addEventListener('pointerdown', ev => {
  if (!RD.doc || ev.button !== 0 || obActive()) return;
  rdCanvas.focus();
  // A page (or cover) still going over: a click comes next, after it.
  const on = RD.turn;
  if (on && on.mode === 'anim' && on.anim.done === 'turn') { const d = rdSideAt(rdPoint(ev)); if (d) rdLater(d); return; }
  rdSettle();
  const p = rdPoint(ev), zone = rdZone(p), dir = zone ? zone.dir : rdSideAt(p), m = dir ? rdMove(dir) : null;
  if (!m) { if (RD.turn && RD.turn.mode === 'peek') RD.turn = null; drawReader(); return; }
  let t;
  if (m.kind === 'rigid') {
    t = {kind:'rigid', dir, from:RD.spread, to:m.to, p:0, p0:0};
    if (m.to >= 0 && m.to <= lastSpread()) { RD.target = m.to; readerWant(); }
  } else {
    const cy = zone ? zone.cy : p.y > RD.H / 2 ? RD.H : 0;
    t = RD.turn && RD.turn.kind === 'curl' && RD.turn.dir === dir && RD.turn.cy === cy ? RD.turn : newTurn(dir, cy);
    // Taken anywhere on the page, it moves with the pointer from there.
    t.grip = {x:t.P.x - p.x, y:t.P.y - p.y}; t.goal = {x:t.P.x, y:t.P.y};
  }
  t.mode = 'drag'; t.moved = false; t.downX = ev.clientX; t.downY = ev.clientY; t.trail = [{x:ev.clientX, time:ev.timeStamp}];
  RD.turn = t; rdCanvas.setPointerCapture(ev.pointerId); rdCanvas.style.cursor = 'grabbing'; rdKick();
});
function rdRelease(ev){
  const t = RD.turn; if (!t || t.mode !== 'drag' || obActive()) return;
  rdCanvas.style.cursor = '';
  if (!t.moved) { rdAnimate(t, 'turn'); return; }   // a click turns the page
  // A flick: still moving fast when let go (held still first, it's not one).
  const a = t.trail[0], z = t.trail[t.trail.length - 1], still = ev && ev.timeStamp - z.time > 100;
  const v = still ? 0 : (z.x - a.x) / Math.max(1, z.time - a.time);
  const past = t.kind === 'rigid' ? t.p > 0.5 : t.dir > 0 ? t.P.x < RD.W : t.P.x > RD.W, flick = v * t.dir < -0.5;
  rdAnimate(t, past || flick ? 'turn' : 'back');
}
rdCanvas.addEventListener('pointerup', rdRelease);
rdCanvas.addEventListener('pointercancel', () => { const t = RD.turn; if (t && t.mode === 'drag' && !obActive()) rdAnimate(t, 'back'); });
/* Holding the book in 3D: drag to turn it, Shift-drag (or the right button) to move it, the wheel to bring it nearer,
   a double-click to put it back. A click (without moving) turns a page: the one on the side of the spine it's on,
   however the book is turned; or, closed, opens the cover (or shuts it back, closed at the back). */
const RH = {drag:null};
// Where the spine runs on the screen, as the open book is drawn: two points on it.
function rvSpineLine(){
  const P = RD.obPV; if (!P) return null;
  const at = y => { const v = [0, y, 0, 1], m = P.pv, o = [0, 1, 2, 3].map(r => m[r] * v[0] + m[4 + r] * v[1] + m[8 + r] * v[2] + m[12 + r] * v[3]);
    return {x:(o[0] / o[3] + 1) / 2 * P.SW, y:(1 - o[1] / o[3]) / 2 * P.SH}; };
  return [at(-0.5), at(0.5)];
}
rdCanvas.addEventListener('pointerdown', ev => {
  if (!RD.doc || !obActive() || FL.active || FL.leaving || (ev.button !== 0 && ev.button !== 2)) return;
  ev.preventDefault(); rdCanvas.focus();
  rdCanvas.setPointerCapture(ev.pointerId);
  RH.drag = {id:ev.pointerId, x:ev.clientX, y:ev.clientY, x0:ev.clientX, y0:ev.clientY, pan:ev.shiftKey || ev.button === 2, moved:false};
});
rdCanvas.addEventListener('pointermove', ev => {
  const g = RH.drag; if (!g || ev.pointerId !== g.id || !obActive()) return;
  const dx = ev.clientX - g.x, dy = ev.clientY - g.y; g.x = ev.clientX; g.y = ev.clientY;
  if (!g.moved && Math.hypot(ev.clientX - g.x0, ev.clientY - g.y0) < 5) return;
  g.moved = true; rdCanvas.style.cursor = 'grabbing';
  if (g.pan) { RV.panX += dx; RV.panY += dy; }
  else { RV.yaw += dx * 0.008; RV.pitch = Math.max(-Math.PI * 0.95, Math.min(Math.PI * 0.95, RV.pitch + dy * 0.008)); }
  drawReader();
});
const rhEnd = ev => {
  const g = RH.drag; if (!g || ev.pointerId !== g.id) return;
  RH.drag = null; rdCanvas.style.cursor = '';
  if (g.moved || ev.type === 'pointercancel' || g.pan) return;
  // a click: which way to turn
  const k = RD.spread, K = lastSpread();
  let dir = k < 0 ? 1 : k > K ? -1 : 0;
  if (!dir) {
    const l = rvSpineLine(); if (!l) return;
    const cross = (l[1].x - l[0].x) * (ev.clientY - l[0].y) - (l[1].y - l[0].y) * (ev.clientX - l[0].x);
    dir = cross > 0 ? 1 : -1;   // (right of the spine as it runs up the page: forward)
  }
  rdTurn(dir);
};
rdCanvas.addEventListener('pointerup', rhEnd);
rdCanvas.addEventListener('pointercancel', rhEnd);
rdCanvas.addEventListener('wheel', ev => {
  if (!RD.doc || !obActive()) return;
  ev.preventDefault();
  RV.zoom = Math.max(0.35, Math.min(6, RV.zoom * Math.exp(-ev.deltaY * (ev.deltaMode === 1 ? 0.05 : 0.0015))));
  drawReader();
  clearTimeout(RD.hiTimer); RD.hiTimer = setTimeout(readerWant, 250);   // (the open pages drawn sharper, once it's stopped)
}, {passive:false});
rdCanvas.addEventListener('dblclick', ev => { if (RD.doc && obActive()) { ev.preventDefault(); rvGoHome(); } });
rdCanvas.addEventListener('contextmenu', ev => { if (obActive()) ev.preventDefault(); });
$('bookReader').addEventListener('keydown', ev => {
  if (ev.target === $('readerGo') || !RD.doc || FL.active || FL.leaving) return;
  const forward = ['ArrowRight', 'PageDown', ' '], backward = ['ArrowLeft', 'PageUp'];
  if (forward.includes(ev.key)) { ev.preventDefault(); rdTurn(1, undefined, ev.repeat); }
  else if (backward.includes(ev.key)) { ev.preventDefault(); rdTurn(-1, undefined, ev.repeat); }
  else if (ev.key === 'Home' || ev.key === 'End') { ev.preventDefault(); RD.turn = null; rdGoTo(ev.key === 'Home' ? 0 : lastSpread()); drawReader(); }
});
$('readerGo').addEventListener('change', () => { const v = parseInt($('readerGo').value, 10); if (v) rdJump(v); });
$('readerGo').addEventListener('keydown', ev => { if (ev.key === 'Enter') { ev.preventDefault(); $('readerGo').blur(); rdCanvas.focus(); } });
$('readerClose').addEventListener('click', closeBook);
// Escape: taken at the key itself, as the browser would let the reader's closing be put off only once (pressed
// again, it would close the reader then and there, cutting the book off on its way back); pressed again while the
// book's going back, it's let be. ('cancel' is for any other way of asking, like a phone's back button.)
$('bookReader').addEventListener('keydown', ev => { if (ev.key === 'Escape') { ev.preventDefault(); ev.stopPropagation(); closeBook(); } }, true);
$('bookReader').addEventListener('cancel', ev => { ev.preventDefault(); closeBook(); });
$('bookReader').addEventListener('close', () => { closeReaderDoc(); $('bookReader').classList.remove('flying', 'leaving'); });

/* Dragging an entry from the list into the writing */
let listDrag = null, listDragEnded = 0;
function startListDrag(ev, id){
  if (ev.button !== 0 || ev.pointerType === 'touch' || listDrag || drag) return;
  listDrag = {id, x0:ev.clientX, y0:ev.clientY, x:ev.clientX, y:ev.clientY, started:false, target:null, self:false, ghost:null, raf:0};
  window.addEventListener('pointermove', moveListDrag);
  window.addEventListener('pointerup', endListDrag);
  window.addEventListener('pointercancel', cancelListDrag);
}
function moveListDrag(ev){
  const d = listDrag; if (!d) return;
  d.x = ev.clientX; d.y = ev.clientY;
  if (!d.started) {
    if (Math.hypot(d.x - d.x0, d.y - d.y0) < 6) return;
    d.started = true;
    document.body.classList.add('moving');
    const g = document.createElement('span'); g.className = 'ghost fig elink'; g.textContent = linkName(d.id);
    document.body.append(g); d.ghost = g;
    d.raf = requestAnimationFrame(listDragFrame);
  }
  d.ghost.style.left = d.x + 'px'; d.ghost.style.top = d.y + 'px';
}
function listDragFrame(){
  const d = listDrag; if (!d || !d.started) return;
  d.target = null; d.self = false;
  const mr = els.main.getBoundingClientRect();
  const overMain = d.x >= mr.left && d.x <= mr.right && d.y >= mr.top && d.y <= mr.bottom;
  if (overMain && currentId && !els.page.hidden && !sideDrop(d.x, d.y)) {
    const edge = 60, sr = els.scroll.getBoundingClientRect();
    if (d.y < sr.top + edge) els.scroll.scrollTop -= Math.ceil((sr.top + edge - d.y) / 4);
    else if (d.y > sr.bottom - edge) els.scroll.scrollTop += Math.ceil((d.y - (sr.bottom - edge)) / 4);
    if (d.id === currentId) d.self = true;   // an entry can't link to itself
    else d.target = dropTarget(d.x, d.y);
  }
  d.ghost.classList.toggle('nodrop', !d.target);
  showMark(d.target);
  d.raf = requestAnimationFrame(listDragFrame);
}
function finishListDrag(){
  const d = listDrag; listDrag = null;
  cancelAnimationFrame(d.raf);
  window.removeEventListener('pointermove', moveListDrag);
  window.removeEventListener('pointerup', endListDrag);
  window.removeEventListener('pointercancel', cancelListDrag);
  document.body.classList.remove('moving');
  if (d.ghost) d.ghost.remove();
  showMark(null);
  return d;
}
function endListDrag(){
  if (!listDrag) return;
  const d = finishListDrag();
  if (!d.started) return;   // a plain click: the entry opens as usual
  listDragEnded = Date.now();
  if (d.self) { setStatus("An entry can't be linked into itself.", true); return; }
  const e = entries.get(d.id);
  if (!d.target || !e || !currentId) return;
  placeFigure(makeLink(d.id, e.title), d.target);
  onBodyChange();
}
function cancelListDrag(){ if (listDrag) finishListDrag(); }

/* ---------- Taking tasks out of entries and putting them back ---------- */
// Changes an entry's writing as a list of parts. For the entry that's open, the page is brought up to date
// first and redrawn after. Returns false if there's no such entry.
function changeEntryBody(id, change){
  const e = entries.get(id); if (!e) return false;
  if (id === currentId) onBodyChange();
  const parts = parseBody(e.body);
  change(parts);
  const body = serializeParts(parts);
  if (body === e.body) return true;
  e.body = body; e.images = imagesIn(body);
  markChanged(id);
  if (id === currentId) fillEditor(false);
  return true;
}
// A task's key leaves out whether it's archived, so a task and its copy in the Archive match.
const taskKey = it => it.state + ' ' + taskLine({...it, archived:''});
// Notes in the entry that the first matching task not yet archived has been archived (it stays where it is).
function markTaskArchivedInParts(parts, key, stamp){
  for (const p of parts) {
    if (p.type !== 'tasks') continue;
    const it = p.items.find(it => !it.archived && taskKey(it) === key);
    if (it) { it.archived = stamp; return true; }
  }
  return false;
}
// De-archiving: the task is still in its entry, so the note goes and it's back in the Tasks menu.
// Returns false if it isn't there (it was archived before tasks stayed in their entries, or was deleted).
function unmarkTaskArchivedInParts(parts, key){
  let plain = false;
  for (const p of parts) {
    if (p.type !== 'tasks') continue;
    for (const it of p.items) {
      if (taskKey(it) !== key) continue;
      if (it.archived) { it.archived = ''; return true; }
      plain = true;
    }
  }
  return plain;   // already in the entry and not archived: nothing to put back
}
// Takes the first task matching `key` out of the parts; a list left with no tasks goes too.
function removeTaskFromParts(parts, key){
  for (let j = 0; j < parts.length; j++) {
    const p = parts[j]; if (p.type !== 'tasks') continue;
    const i = p.items.findIndex(it => taskKey(it) === key); if (i < 0) continue;
    p.items.splice(i, 1);
    if (!p.items.length) {
      parts.splice(j, 1);
      const a = parts[j - 1], b = parts[j];
      if (a && b && a.type === 'text' && b.type === 'text') {
        if (!a.text.endsWith('\n') && !b.text.startsWith('\n')) a.text += '\n';   // the lines either side stay apart
        a.text += b.text; parts.splice(j, 1);
      }
    }
    return true;
  }
  return false;
}
// Puts an archived task back where it was: in its old list and place if that list is still there,
// otherwise in a new list at the end of the entry.
function insertTaskInParts(parts, t){
  const lists = parts.filter(p => p.type === 'tasks');
  const it = {state:t.item.state, text:t.item.text || '', created:t.item.created || '', due:t.item.due || '', marked:t.item.marked || '', urgency:t.item.urgency || ''};
  if (!t.alone && lists.length) {
    const list = lists[Math.min(t.block || 0, lists.length - 1)];
    list.items.splice(Math.min(t.pos || 0, list.items.length), 0, it);
  } else parts.push({type:'tasks', items:[it]});
}
// Archives finished tasks: `picks` maps an entry's id to the numbers of its tasks (counted over the whole entry).
// A copy goes to the Archive; the task stays in its entry, noted as archived, and leaves the Tasks menu.
async function archiveFinishedTasks(picks){
  const records = [];
  for (const [id, ns] of picks) {
    const e = entries.get(id); if (!e) continue;
    let k = 0, b = 0;
    for (const p of parseBody(e.body)) {
      if (p.type !== 'tasks') continue;
      const alone = p.items.every((_, i) => ns.has(k + i));   // the whole list is going
      p.items.forEach((it, i) => {
        if (ns.has(k + i) && taskDone(it) && !it.archived) records.push({entry:id, entryTitle:e.title, block:b, pos:i, alone,
          item:{state:it.state, text:it.text, created:it.created, due:it.due, marked:it.marked, urgency:it.urgency}});
      });
      k += p.items.length; b++;
    }
  }
  if (!records.length) return true;
  const r = await fetch('/api/archive/tasks', {method:'POST', headers:H, body:JSON.stringify({tasks:records})});
  if (!r.ok) throw new Error();
  let saved = [];
  try { saved = (await r.json()).tasks || []; } catch (e) {}
  const stamp = i => (saved[i] && STAMP_RE.test(saved[i].archived || '')) ? saved[i].archived : stampNow();
  for (const id of new Set(records.map(x => x.entry))) {
    changeEntryBody(id, parts => { records.forEach((x, i) => { if (x.entry === id) markTaskArchivedInParts(parts, taskKey(x.item), stamp(i)); }); });
  }
  return true;
}
function tasksMenuNote(text){
  const n = $('tasksPanel').querySelector('.tl-actions .status');
  if (n) { n.textContent = text; n.classList.add('err'); }
}
// An Archive button on a finished task in the Tasks menu.
function taskArchiveButton(id, n){
  const b = document.createElement('button'); b.type = 'button'; b.className = 'task-arch-btn'; b.textContent = 'Archive';
  b.title = 'Keep this task in the Archive and take it out of the Tasks menu (it stays in its entry)';
  b.addEventListener('click', async ev => {
    ev.stopPropagation();
    b.disabled = true;
    try { await archiveFinishedTasks(new Map([[id, new Set([n])]])); renderTasksMenu(); }
    catch (e) { b.disabled = false; tasksMenuNote("Couldn't archive that task. Check that the journal server is still running."); }
  });
  return b;
}
// Above the Done tab: Archive all finished (it asks once more first).
function archiveAllRow(groups){
  const row = document.createElement('div'); row.className = 'tl-actions';
  const note = document.createElement('span'); note.className = 'status'; note.setAttribute('aria-live', 'polite');
  const b = document.createElement('button'); b.type = 'button'; b.className = 'tool'; b.textContent = 'Archive all finished';
  b.addEventListener('click', async () => {
    if (!armed(b, 'Archive all finished', 'Archive them all?')) return;
    const picks = new Map();
    for (const [id, , blocks] of groups) {
      let k = 0; const ns = new Set();
      for (const block of blocks) for (const it of block.items) { if (taskDone(it) && !it.archived) ns.add(k); k++; }
      if (ns.size) picks.set(id, ns);
    }
    b.disabled = true; b.textContent = 'Archiving\u2026';
    try { await archiveFinishedTasks(picks); renderTasksMenu(); }
    catch (e) { b.disabled = false; b.textContent = 'Archive all finished'; note.textContent = "Couldn't archive them. Check that the journal server is still running."; note.classList.add('err'); }
  });
  row.append(note, b);
  return row;
}

/* ---------- Tasks menu ---------- */
// Every task in the journal, gathered from the entries, laid out as they are in each entry.
// Two tabs: Ongoing (tasks not yet marked) and Done (marked as a success or a failure).
let tasksTab = 'ongoing';
const taskDone = it => it.state === 'x' || it.state === '-';
function selectTasksTab(which){
  tasksTab = which;
  $('tabOngoing').setAttribute('aria-selected', String(which === 'ongoing'));
  $('tabDone').setAttribute('aria-selected', String(which === 'done'));
  renderTasksMenu(); $('tasksPanel').scrollTop = 0;
}
$('tabOngoing').addEventListener('click', () => selectTasksTab('ongoing'));
$('tabDone').addEventListener('click', () => selectTasksTab('done'));
function renderTasksMenu(){
  const panel = $('tasksPanel');
  const note = text => { const p = document.createElement('p'); p.className = 'arch-note'; p.textContent = text; panel.replaceChildren(p); };
  const counts = {ongoing:0, done:0}, groups = [];
  const showCounts = () => {
    for (const [tab, key] of [['tabOngoing', 'ongoing'], ['tabDone', 'done']]) {
      const b = $(tab); b.textContent = key === 'ongoing' ? 'Ongoing' : 'Done';
      if (loaded) { const n = document.createElement('span'); n.className = 'tab-n'; n.textContent = counts[key]; b.append(n); }
    }
  };
  if (!loaded) { showCounts(); return note('Opening your journal…'); }
  const wantDone = tasksTab === 'done';
  let any = false;
  for (const [id, e] of [...entries.entries()].sort((a, b) => b[1].updated - a[1].updated)) {
    const blocks = parseBody(e.body).filter(p => p.type === 'tasks');
    if (!blocks.length) continue;
    any = true;
    // Archived tasks stay in their entries but aren't listed here.
    for (const b of blocks) for (const it of b.items) if (!it.archived) counts[taskDone(it) ? 'done' : 'ongoing']++;
    if (blocks.some(b => b.items.some(it => !it.archived && taskDone(it) === wantDone))) groups.push([id, e, blocks]);
  }
  showCounts();
  const sort = tasksSort();
  for (const b of document.querySelectorAll('.task-sort [data-sort]')) b.setAttribute('aria-checked', String(b.dataset.sort === sort));
  if (!any) return note('No tasks yet. Tasks you add to an entry with the Task button will appear here.');
  if (!groups.length) return note(wantDone ? 'No finished tasks here. Tasks marked as a success or a failure appear here until you archive them.' : 'Nothing ongoing: every task has been marked as a success or a failure.');
  if (sort !== 'entries') {
    panel.replaceChildren(sortedTasks(groups, wantDone, sort));
    if (wantDone) panel.prepend(archiveAllRow(groups));
    return;
  }
  const frag = document.createDocumentFragment();
  if (wantDone) frag.append(archiveAllRow(groups));
  for (const [id, e, blocks] of groups) {
    const g = document.createElement('section'); g.className = 'tl-group';
    const t = document.createElement('button'); t.type = 'button';
    t.className = 'tl-entry' + (e.title.trim() ? '' : ' untitled');
    t.textContent = e.title.trim() || 'Untitled';
    t.title = 'Open this entry';
    t.addEventListener('click', () => { $('tasksDialog').close(); open(id); });
    g.append(t);
    let k = 0;
    for (const block of blocks) {
      const div = document.createElement('div'); div.className = 'tasks';
      const ol = document.createElement('ol');
      block.items.forEach((it, i) => {
        const n = k++;   // counted over every task in the entry, so the right one is found when it's clicked
        if (it.archived || taskDone(it) !== wantDone) return;
        const li = staticTask(it); li.dataset.n = i + 1;
        if (wantDone) li.insertBefore(taskArchiveButton(id, n), li.querySelector('.task-box'));
        li.title = 'Go to this task';
        li.addEventListener('click', () => goToTask(id, n));
        ol.append(li);
      });
      if (ol.children.length) { div.append(ol); g.append(div); }   // lists with none of these tasks are left out
    }
    frag.append(g);
  }
  panel.replaceChildren(frag);
}
// How the Tasks menu lists them: under their entries, by urgency, or by the soonest finish time.
// The choice is kept with the settings.
function tasksSort(){ return ['urgency', 'due'].includes(settings.tasksSort) ? settings.tasksSort : 'entries'; }
for (const b of document.querySelectorAll('.task-sort [data-sort]')) b.addEventListener('click', () => {
  changeSetting('tasksSort', b.dataset.sort === 'entries' ? undefined : b.dataset.sort);
  renderTasksMenu(); $('tasksPanel').scrollTop = 0;
});
// All the tasks of one tab in a single order, in sections: High / Medium / Low / No urgency,
// or With a finish time (soonest first) / No finish time. Each says which entry it's from.
function sortedTasks(groups, wantDone, sort){
  const all = [];
  groups.forEach(([id, e, blocks], g) => {
    let k = 0;
    for (const block of blocks) for (const it of block.items) {
      const n = k++;
      if (!it.archived && taskDone(it) === wantDone) all.push({it, id, e, n, g, due:stampDate(it.due), rank:URGENCY[it.urgency] ? URGENCY_RANK[it.urgency] : 3});
    }
  });
  const byDue = (a, b) => (a.due ? 0 : 1) - (b.due ? 0 : 1) || (a.due && b.due ? a.due - b.due : 0);
  const byOrder = (a, b) => a.g - b.g || a.n - b.n;   // otherwise: most recently changed entry first, then as in the entry
  all.sort(sort === 'urgency' ? (a, b) => a.rank - b.rank || byDue(a, b) || byOrder(a, b)
                              : (a, b) => byDue(a, b) || a.rank - b.rank || byOrder(a, b));
  const sections = sort === 'urgency'
    ? [['High', t => t.rank === 0], ['Medium', t => t.rank === 1], ['Low', t => t.rank === 2], ['No urgency', t => t.rank === 3]]
    : [['With a finish time', t => !!t.due], ['No finish time', t => !t.due]];
  const frag = document.createDocumentFragment();
  for (const [label, test] of sections) {
    const list = all.filter(test); if (!list.length) continue;
    const sec = document.createElement('section'); sec.className = 'tl-group';
    const h = document.createElement('span'); h.className = 'tl-head'; h.textContent = label + ' (' + list.length + ')';
    const div = document.createElement('div'); div.className = 'tasks flat';
    const ol = document.createElement('ol');
    for (const t of list) {
      const li = staticTask(t.it);
      const from = document.createElement('span'); from.className = 'task-from';
      from.textContent = t.e.title.trim() || 'Untitled'; from.title = 'In the entry ' + from.textContent;
      li.querySelector('.task-meta').prepend(from);
      if (wantDone) li.insertBefore(taskArchiveButton(t.id, t.n), li.querySelector('.task-box'));
      li.title = 'Go to this task';
      li.addEventListener('click', () => goToTask(t.id, t.n));
      ol.append(li);
    }
    div.append(ol); sec.append(h, div); frag.append(sec);
  }
  return frag;
}
function goToTask(id, n){
  $('tasksDialog').close();
  open(id);
  const li = els.body.querySelectorAll('.task')[n];
  if (li) { li.scrollIntoView({block:'center'}); focusTask(li); }
}
$('tasksMenuBtn').addEventListener('click', () => { renderTasksMenu(); $('tasksPanel').scrollTop = 0; $('tasksDialog').showModal(); });
$('tasksClose').addEventListener('click', () => $('tasksDialog').close());
$('tasksDialog').addEventListener('click', ev => { if (ev.target === $('tasksDialog')) $('tasksDialog').close(); });

/* ---------- Log ----------
   What you did each day. The Log menu lists the days, newest first; each opens to show that day's activities,
   numbered in the order they started. An activity is logged when it starts (it's then ongoing, until it's
   finished) or once it's done. The log shortcut (Ctrl+Shift+L unless changed in the Menu) opens the form here;
   on Windows the same keys work all over the computer, opening a small logging window with a screenshot. */
let logActs = [], logShortcuts = {}, logLoaded = false, logForm = null;
const logOpenDays = new Set();
const logCombo = () => settings.logKey || 'Ctrl+Shift+L';
const shotCombo = () => settings.shotKey || 'Ctrl+Alt+S';
const actWhen = a => a.start || a.end;
const actDay = a => actWhen(a).slice(0, 10);
const actGoing = a => !!a.start && !a.end;
const fmtLogDay = new Intl.DateTimeFormat(undefined, {weekday:'long', day:'numeric', month:'long', year:'numeric'});
const fmtLogTime = new Intl.DateTimeFormat(undefined, {hour:'numeric', minute:'2-digit'});
const fmtLogDate = new Intl.DateTimeFormat(undefined, {day:'numeric', month:'short'});
function todayStamp(){ return stampNow().slice(0, 10); }
async function loadLog(){
  try {
    const r = await fetch('/api/log', {headers:{'X-Journal':'1'}, cache:'no-store'});
    if (!r.ok) throw new Error();
    const d = await r.json();
    logActs = Array.isArray(d.activities) ? d.activities : [];
    logShortcuts = d.shortcuts || {};
    logLoaded = true;
  } catch (e) {
    if (!logLoaded) { logNote("Couldn't open the log. Check that the journal server is still running."); return; }
  }
  renderLog(); showLogShortcuts();
}
function logNote(text){
  const p = document.createElement('p'); p.className = 'arch-note'; p.textContent = text;
  $('logPanel').replaceChildren(p);
}
function howLong(a, b){
  const m = Math.round((stampDate(b) - stampDate(a)) / 60000);
  if (!(m >= 0)) return '';
  if (m < 60) return m + ' min';
  return Math.floor(m / 60) + ' h' + (m % 60 ? ' ' + (m % 60) + ' min' : '');
}
// "09:00–10:15 · 1 h 15 min", "Started 09:00 · ongoing", "Finished 10:15"
function logWhenText(a){
  const t = s => { const d = stampDate(s); return d ? (s.slice(0, 10) === actDay(a) ? '' : fmtLogDate.format(d) + ' ') + fmtLogTime.format(d) : ''; };
  if (a.start && a.end) { const len = howLong(a.start, a.end); return t(a.start) + '\u2013' + t(a.end) + (len ? ' \u00b7 ' + len : ''); }
  if (a.start) return 'Started ' + t(a.start) + ' \u00b7 ongoing';
  return 'Finished ' + t(a.end);
}
function renderLog(){
  if (!$('logDialog').open || !logLoaded) return;
  if (!logActs.length) return logNote('Nothing logged yet. Press ' + logCombo() + ', or the + above, to log what you\u2019re doing.');
  const days = new Map();
  for (const a of logActs.slice().sort((x, y) => actWhen(x).localeCompare(actWhen(y)))) {
    const d = actDay(a);
    if (!days.has(d)) days.set(d, []);
    days.get(d).push(a);
  }
  const frag = document.createDocumentFragment();
  for (const day of [...days.keys()].sort().reverse()) {
    const list = days.get(day), going = list.filter(actGoing).length;
    const det = document.createElement('details'); det.className = 'log-day';
    det.open = logOpenDays.has(day);
    det.addEventListener('toggle', () => { if (det.open) logOpenDays.add(day); else logOpenDays.delete(day); });
    const sum = document.createElement('summary');
    const date = document.createElement('span'); date.className = 'log-date';
    const dd = stampDate(day + 'T00:00'); date.textContent = dd ? fmtLogDay.format(dd) : day;
    if (day === todayStamp()) date.textContent += ' (today)';
    const count = document.createElement('span'); count.className = 'log-count';
    count.textContent = list.length + (list.length === 1 ? ' activity' : ' activities');
    sum.append(date, count);
    if (going) { const g = document.createElement('span'); g.className = 'log-going'; g.textContent = going + ' ongoing'; sum.append(g); }
    const ol = document.createElement('ol'); ol.className = 'log-acts';
    list.forEach((a, i) => ol.append(logActivityItem(a, i + 1)));
    det.append(sum, ol);
    frag.append(det);
  }
  $('logPanel').replaceChildren(frag);
}
function logActivityItem(a, n){
  const li = document.createElement('li'); li.className = 'log-act' + (actGoing(a) ? ' going' : '');
  const num = document.createElement('span'); num.className = 'log-num'; num.textContent = n + '.';
  const main = document.createElement('div'); main.className = 'log-main';
  const head = document.createElement('div'); head.className = 'log-head';
  const title = document.createElement('span'); title.className = 'log-title'; title.textContent = a.title || 'Untitled';
  const when = document.createElement('span'); when.className = 'log-when'; when.textContent = logWhenText(a);
  head.append(title, when);
  main.append(head);
  if (a.description) { const p = document.createElement('p'); p.className = 'log-desc'; p.textContent = a.description; main.append(p); }
  if (a.images && a.images.length) {
    const pics = document.createElement('div'); pics.className = 'log-pics';
    for (const name of a.images) {
      const img = document.createElement('img'); img.src = '/log/images/' + name; img.alt = 'Picture'; img.loading = 'lazy';
      img.title = 'Show it larger';
      img.addEventListener('click', () => { $('logPicImg').src = img.src; $('logPic').showModal(); });
      pics.append(img);
    }
    main.append(pics);
  }
  const btns = document.createElement('div'); btns.className = 'log-btns';
  if (actGoing(a)) {
    const fin = document.createElement('button'); fin.type = 'button'; fin.className = 'tool'; fin.textContent = 'Finished now';
    fin.title = 'Note that you finished this just now';
    fin.addEventListener('click', async () => {
      fin.disabled = true;
      if (await saveActivity(a.id, {end: stampNow()})) loadLog(); else fin.disabled = false;
    });
    btns.append(fin);
  }
  const edit = document.createElement('button'); edit.type = 'button'; edit.className = 'tool'; edit.textContent = 'Edit';
  edit.addEventListener('click', () => openLogForm('edit', a));
  const del = document.createElement('button'); del.type = 'button'; del.className = 'tool log-del'; del.textContent = 'Delete';
  del.addEventListener('click', async () => {
    if (!armed(del, 'Delete', 'Delete it and its pictures?')) return;
    del.disabled = true;
    try {
      const r = await fetch('/api/log/activities/' + a.id, {method:'DELETE', headers:H});
      if (!r.ok && r.status !== 404) throw new Error();
      loadLog();
    } catch (e) { del.disabled = false; del.textContent = "Couldn't. Try again"; }
  });
  btns.append(edit, del);
  main.append(btns);
  li.append(num, main);
  return li;
}
async function saveActivity(id, data){
  try {
    const r = await fetch(id ? '/api/log/activities/' + id : '/api/log/activities', {method: id ? 'PUT' : 'POST', headers:H, body:JSON.stringify(data)});
    if (!r.ok) throw new Error();
    return await r.json();
  } catch (e) { return null; }
}
function openLog(){
  if (!$('logDialog').open) {
    logOpenDays.add(todayStamp());
    $('logDialog').showModal();
  }
  if (!logLoaded) logNote('Opening the log\u2026');
  loadLog();
}

/* The form for logging an activity (and for changing one): "Just started", "Finished" or editing. */
function openLogForm(mode, act){
  if (!$('logDialog').open) openLog();
  const going = logActs.filter(actGoing).sort((x, y) => y.start.localeCompare(x.start));
  logForm = {mode, act: act || null, pics: act ? [...(act.images || [])] : [], added: []};
  $('logModeRow').hidden = mode === 'edit';
  $('logFormTitle').textContent = mode === 'edit' ? 'Change this activity' : 'Log an activity';
  for (const r of document.querySelectorAll('input[name="logMode"]')) r.checked = r.value === (mode === 'finish' ? 'finish' : 'start');
  const sel = $('logWhich'); sel.replaceChildren();
  const add = (v, t) => { const o = document.createElement('option'); o.value = v; o.textContent = t; sel.append(o); };
  for (const g of going) add(g.id, (g.title || 'Untitled') + ' (started ' + logWhenText(g).replace(/^Started | \u00b7 ongoing$/g, '') + ')');
  add('', 'Something not logged yet');
  $('logTitle').value = act ? act.title : '';
  $('logDesc').value = act ? act.description : '';
  $('logWhen').value = mode === 'edit' ? (act.start || act.end) : stampNow();
  $('logEnd').value = mode === 'edit' ? act.end : '';
  $('logBegan').value = '';
  $('logFormNote').textContent = ''; $('logFormNote').classList.remove('err');
  $('logForm').hidden = false; $('logAddBtn').setAttribute('aria-expanded', 'true');
  if (mode === 'finish') { $('logWhich').selectedIndex = 0; logWhichPicked(); }
  logFormLayout();
  renderLogFormPics();
  $('logTitle').focus();
}
function logFormMode(){ return logForm.mode === 'edit' ? 'edit' : document.querySelector('input[name="logMode"]:checked').value; }
function logFormLayout(){
  const mode = logFormMode(), existing = mode === 'finish' && $('logWhich').value;
  $('logWhichRow').hidden = mode !== 'finish';
  $('logWhenLabel').textContent = mode === 'finish' ? 'Finished at' : 'Started at';
  $('logBeganRow').hidden = !(mode === 'finish' && !existing);
  $('logEndRow').hidden = mode !== 'edit';
  $('logSave').textContent = mode === 'edit' ? 'Save changes' : 'Save';
}
// Choosing an ongoing activity to finish fills in its title and description, to change if you like.
function logWhichPicked(){
  const a = logActs.find(x => x.id === $('logWhich').value), was = logActs.find(x => x.id === logForm.filled);
  if (a) { $('logTitle').value = a.title; $('logDesc').value = a.description; logForm.filled = a.id; }
  else if (was && $('logTitle').value === was.title) { $('logTitle').value = ''; if ($('logDesc').value === was.description) $('logDesc').value = ''; logForm.filled = null; }
  logFormLayout();
}
function renderLogFormPics(){
  const box = $('logPics'); box.replaceChildren();
  for (const name of logForm.pics) {
    const s = document.createElement('span'); s.className = 'log-form-pic';
    const img = document.createElement('img'); img.src = '/log/images/' + name; img.alt = 'Picture';
    const x = document.createElement('button'); x.type = 'button'; x.textContent = '\u00d7'; x.title = 'Take this picture off'; x.setAttribute('aria-label', 'Take this picture off');
    x.addEventListener('click', () => {
      logForm.pics = logForm.pics.filter(n => n !== name);
      if (logForm.added.includes(name)) dropLogPic(name);
      renderLogFormPics();
    });
    s.append(img, x); box.append(s);
  }
}
function dropLogPic(name){
  logForm.added = logForm.added.filter(n => n !== name);
  fetch('/api/log/images/' + name, {method:'DELETE', headers:H}).catch(() => {});
}
async function addLogPics(files){
  if (!logForm) return;
  const note = $('logFormNote');
  for (const file of files) {
    if (!/^image\//.test(file.type)) continue;
    note.textContent = 'Adding the picture\u2026'; note.classList.remove('err');
    try {
      const r = await fetch('/api/log/images', {method:'POST', headers:{'X-Journal':'1','Content-Type':file.type||'application/octet-stream'}, body:file});
      if (!r.ok) throw new Error(r.status === 415 ? 'type' : 'x');
      const {name} = await r.json();
      logForm.pics.push(name); logForm.added.push(name);
      note.textContent = '';
    } catch (e) {
      note.textContent = e.message === 'type' ? 'That picture is in a kind the journal can\u2019t keep (it keeps PNG, JPEG, GIF, WebP and AVIF).' : "Couldn't add the picture.";
      note.classList.add('err');
    }
  }
  renderLogFormPics();
}
function closeLogForm(saved){
  if (logForm && !saved) for (const n of [...logForm.added]) dropLogPic(n);   // pictures added to a form that wasn't saved
  logForm = null;
  $('logForm').hidden = true; $('logAddBtn').setAttribute('aria-expanded', 'false');
}
async function saveLogForm(){
  const mode = logFormMode(), note = $('logFormNote');
  const fail = t => { note.textContent = t; note.classList.add('err'); };
  const title = $('logTitle').value.trim(), when = $('logWhen').value;
  if (!title) { $('logTitle').focus(); return fail('Give it a title.'); }
  if (!STAMP_RE.test(when) && !(mode === 'edit' && $('logEnd').value)) return fail('Choose the time.');
  const base = {title, description: $('logDesc').value.replace(/\s+$/, '')};
  let id = null, data;
  if (mode === 'edit') {
    const end = $('logEnd').value;
    if (end && STAMP_RE.test(when) && end < when) return fail('It can\u2019t finish before it started.');
    data = {...base, start: STAMP_RE.test(when) ? when : '', end: STAMP_RE.test(end) ? end : '', images: logForm.pics};
    id = logForm.act.id;
  } else if (mode === 'finish' && $('logWhich').value) {
    const a = logActs.find(x => x.id === $('logWhich').value);
    if (a && when < a.start) return fail('It can\u2019t finish before it started (' + logWhenText(a).replace(/ \u00b7 ongoing$/, '') + ').');
    id = $('logWhich').value;
    data = {...base, end: when, addImages: logForm.pics};
  } else if (mode === 'finish') {
    const began = $('logBegan').value;
    if (began && began > when) return fail('It can\u2019t finish before it started.');
    data = {...base, start: STAMP_RE.test(began) ? began : '', end: when, images: logForm.pics};
  } else data = {...base, start: when, end: '', images: logForm.pics};
  $('logSave').disabled = true; note.textContent = 'Saving\u2026'; note.classList.remove('err');
  const saved = await saveActivity(id, data);
  $('logSave').disabled = false;
  if (!saved) return fail("Couldn't save it. Check that the journal server is still running.");
  logOpenDays.add(actDay(saved));
  closeLogForm(true);
  loadLog();
}
$('logMenuBtn').addEventListener('click', openLog);
$('logClose').addEventListener('click', () => $('logDialog').close());
$('logDialog').addEventListener('click', ev => { if (ev.target === $('logDialog')) $('logDialog').close(); });
$('logDialog').addEventListener('close', () => { if (logForm) closeLogForm(false); });
$('logAddBtn').addEventListener('click', () => { if (logForm) closeLogForm(false); else openLogForm('start'); });
// "Finished" offers the activity started most recently; back to "Just started", what it filled in goes again.
for (const r of document.querySelectorAll('input[name="logMode"]')) r.addEventListener('change', () => {
  if (logFormMode() === 'finish') $('logWhich').selectedIndex = 0;
  else $('logWhich').value = '';
  logWhichPicked();
});
$('logWhich').addEventListener('change', logWhichPicked);
$('logNow').addEventListener('click', () => { $('logWhen').value = stampNow(); });
$('logCancel').addEventListener('click', () => closeLogForm(false));
$('logSave').addEventListener('click', saveLogForm);
$('logPicBtn').addEventListener('click', () => $('logFile').click());
$('logFile').addEventListener('change', ev => { addLogPics([...ev.target.files]); ev.target.value = ''; });
$('logForm').addEventListener('paste', ev => {
  const files = [...(ev.clipboardData ? ev.clipboardData.files : [])].filter(f => /^image\//.test(f.type));
  if (files.length) { ev.preventDefault(); addLogPics(files); }
});
$('logForm').addEventListener('dragover', ev => { if (ev.dataTransfer && [...ev.dataTransfer.types].includes('Files')) { ev.preventDefault(); ev.stopPropagation(); } });
$('logForm').addEventListener('drop', ev => {
  if (!ev.dataTransfer || !ev.dataTransfer.files.length) return;
  ev.preventDefault(); ev.stopPropagation(); addLogPics([...ev.dataTransfer.files]);
});
$('logForm').addEventListener('keydown', ev => {
  ev.stopPropagation();   // typing here isn't writing in the entry
  if (ev.key === 'Enter' && (ev.target.tagName === 'INPUT' ? ev.target.type !== 'file' : ev.ctrlKey || ev.metaKey)) { ev.preventDefault(); saveLogForm(); }
  if (ev.key === 'Escape') { ev.preventDefault(); closeLogForm(false); }
});
$('logPic').addEventListener('click', () => $('logPic').close());
// Logged from the small window while the journal was in the background: show it when you come back.
window.addEventListener('focus', () => { if ($('logDialog').open && !logForm) loadLog(); });
setInterval(() => { if ($('logDialog').open && !logForm && !document.hidden) loadLog(); }, 20000);
// The log shortcut: opens the form for logging an activity, from anywhere in the journal.
document.addEventListener('keydown', ev => {
  if (ev.isComposing || ev.repeat || keyListener) return;
  const combo = comboOf(ev);
  if (combo !== logCombo()) return;
  // A shortcut without Ctrl, Alt or Meta would otherwise be a letter: while writing, it stays one.
  const t = ev.target, typing = t && (t.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName));
  if (!/(Ctrl|Alt|Meta)\+/.test(combo) && typing) return;
  const other = [...document.querySelectorAll('dialog[open]')].some(d => d.id !== 'logDialog');
  if (other) return;
  ev.preventDefault(); ev.stopPropagation();
  if (logForm) { $('logTitle').focus(); return; }
  openLogForm('start');
}, true);
// In the Menu: what the log shortcuts do on this computer.
function showLogShortcuts(){
  const box = $('logKeysNote'); if (!box) return;
  box.replaceChildren();
  const p = (text, cls) => { const e = document.createElement('p'); e.className = 'log-keys-note' + (cls ? ' ' + cls : ''); e.textContent = text; box.append(e); return e; };
  if (logShortcuts.global) {
    const where = logShortcuts.desktop
      ? 'Both work anywhere on the computer, even when the journal isn\u2019t open (they\u2019re kept in ' + logShortcuts.desktop + '\u2019s keyboard shortcuts): '
      : 'Both work anywhere on the computer while the journal is running: ';
    p(where + logCombo() + ' opens a small window for logging an activity (with a screenshot of what you were doing), and '
      + shotCombo() + ' adds a screenshot to the activity you started last.');
    for (const k of ['logKey', 'shotKey']) if (logShortcuts[k]) p(logShortcuts[k], 'err');
  } else {
    if (logShortcuts.note) p(logShortcuts.note, 'err');
    p('Inside the journal, ' + logCombo() + ' opens the form for logging an activity. To log from anywhere on the computer, with a screenshot, give these commands keyboard shortcuts in your system\u2019s keyboard settings:');
    if (logShortcuts.log) {
      p('', 'log-cmd').textContent = 'Log an activity:  ' + logShortcuts.log;
      p('', 'log-cmd').textContent = 'Add a screenshot:  ' + logShortcuts.screenshot;
    }
  }
}
$('menuBtn').addEventListener('click', () => loadLog());

/* ---------- Topics ----------
   Made in the Topics menu and numbered from 1 in the order they're made. Each entry can have several:
   they're chosen with the small button under the title, shown under the title, and shown in brackets
   beside the title in the list of entries, with a dot between each. Topics are kept in journal/topics.json,
   and an entry's topics in its file ("topics: …"). */
let topics = [];
async function loadTopics(){
  try {
    const r = await fetch('/api/topics', {headers:{'X-Journal':'1'}, cache:'no-store'});
    if (r.ok) topics = await r.json();
  } catch (e) {}
  renderListView(); renderList(); renderTopic();
  if ($('topicsDialog').open) renderTopicsMenu();
}
let topicsTimer;
function saveTopics(){
  clearTimeout(topicsTimer);
  topicsTimer = setTimeout(async () => {
    try {
      const r = await fetch('/api/topics', {method:'PUT', headers:H, body:JSON.stringify(topics)});
      if (!r.ok) throw new Error();
    } catch (e) { setStatus("Couldn't save the topics.", true); }
  }, 300);
}
const topicById = id => topics.find(t => t.id === id) || null;
const topicNumber = t => topics.indexOf(t) + 1;
const topicText = t => t.name || 'Topic ' + topicNumber(t);
const TOPIC_SEP = '.';
// An entry's topics that still exist, in the order they're numbered.
function entryTopics(e){ return e && e.topics ? topics.filter(t => e.topics.includes(t.id)) : []; }
function topicLabel(e){ return entryTopics(e).map(topicText).join(TOPIC_SEP); }
function newTopicId(){
  let id;
  do { id = [...crypto.getRandomValues(new Uint8Array(6))].map(b => b.toString(16).padStart(2, '0')).join(''); } while (topicById(id));
  return id;
}
// A topic changed or went: show it everywhere it appears.
function topicsChanged(){ saveTopics(); renderListView(); renderList(); renderTopic(); if (!$('topicPop').hidden) renderTopicPop(); }

// Under the title
function renderTopic(){
  const e = currentId ? entries.get(currentId) : null, label = topicLabel(e);
  $('topicName').textContent = label; $('topicName').hidden = !label;
  $('topicBtn').title = label ? 'Change the topics of this entry' : 'Choose topics for this entry';
}
function setTopics(ids){
  const e = currentId ? entries.get(currentId) : null; if (!e) return;
  if (ids.join() === (e.topics || []).join()) return;
  e.topics = ids;
  markChanged(currentId); renderTopic();
}
function renderTopicPop(){
  const pop = $('topicPop'), e = currentId ? entries.get(currentId) : null;
  pop.replaceChildren();
  if (!topics.length) {
    const p = document.createElement('p'); p.textContent = 'No topics yet.';
    const b = document.createElement('button'); b.type = 'button'; b.textContent = 'Make topics in the Topics menu';
    b.addEventListener('click', () => { closeTopicPop(); openTopicsMenu(); });
    pop.append(p, b); return;
  }
  // Each click adds or takes off one topic; the list stays open so several can be chosen.
  const have = e ? (e.topics || []).filter(id => topicById(id)) : [];
  for (const t of topics) {
    const b = document.createElement('button'); b.type = 'button'; b.dataset.id = t.id;
    const on = have.includes(t.id);
    b.setAttribute('aria-pressed', String(on));
    const num = document.createElement('span'); num.className = 'topic-num'; num.textContent = topicNumber(t);
    const name = document.createElement('span'); name.textContent = topicText(t);
    b.append(num, name);
    b.addEventListener('click', () => {
      setTopics(on ? have.filter(id => id !== t.id) : have.concat(t.id));
      renderTopicPop();
      const again = $('topicPop').querySelector('[data-id="' + t.id + '"]'); if (again) again.focus({preventScroll:true});
    });
    pop.append(b);
  }
  if (have.length) {
    const none = document.createElement('button'); none.type = 'button'; none.className = 'topic-none';
    none.textContent = have.length > 1 ? 'Take off all topics' : 'Take off the topic';
    none.addEventListener('click', () => { setTopics([]); closeTopicPop(true); });
    pop.append(none);
  }
}
function openTopicPop(){
  renderTopicPop();
  $('topicPop').hidden = false; $('topicBtn').setAttribute('aria-expanded', 'true');
  const first = $('topicPop').querySelector('[aria-pressed="true"]') || $('topicPop').querySelector('button');
  if (first) first.focus({preventScroll:true});
}
function closeTopicPop(refocus){
  if ($('topicPop').hidden) return;
  $('topicPop').hidden = true; $('topicBtn').setAttribute('aria-expanded', 'false');
  if (refocus) $('topicBtn').focus({preventScroll:true});
}
$('topicBtn').addEventListener('click', () => { if ($('topicPop').hidden) openTopicPop(); else closeTopicPop(); });
document.addEventListener('pointerdown', ev => { if (!$('topicRow').contains(ev.target)) closeTopicPop(); });
$('topicRow').addEventListener('keydown', ev => {
  if ($('topicPop').hidden) return;
  if (ev.key === 'Escape') { ev.preventDefault(); ev.stopPropagation(); closeTopicPop(true); return; }
  if (ev.key !== 'ArrowDown' && ev.key !== 'ArrowUp') return;
  const list = [...$('topicPop').querySelectorAll('button')], i = list.indexOf(document.activeElement);
  if (!list.length) return;
  ev.preventDefault();
  list[(i + (ev.key === 'ArrowDown' ? 1 : -1) + list.length) % list.length].focus();
});
// Closes when the focus moves elsewhere (checked a moment later, as the list is redrawn after each click).
$('topicRow').addEventListener('focusout', () => setTimeout(() => { if (!$('topicRow').contains(document.activeElement)) closeTopicPop(); }, 0));

// The Topics menu
function renderTopicsMenu(){
  const list = $('topicList');
  const uses = new Map();
  for (const e of entries.values()) for (const id of e.topics || []) uses.set(id, (uses.get(id) || 0) + 1);
  list.replaceChildren(...topics.map(t => {
    const li = document.createElement('li');
    const num = document.createElement('span'); num.className = 'topic-num'; num.textContent = topicNumber(t);
    const input = document.createElement('input'); input.className = 'topic-input'; input.type = 'text'; input.maxLength = 120;
    input.value = t.name; input.placeholder = 'Topic ' + topicNumber(t); input.autocomplete = 'off';
    input.setAttribute('aria-label', 'Name of topic ' + topicNumber(t));
    input.addEventListener('input', () => { t.name = input.value.replace(/\s+/g, ' ').trimStart(); topicsChanged(); });
    input.addEventListener('change', () => { t.name = t.name.trim(); input.value = t.name; topicsChanged(); });
    input.addEventListener('keydown', ev => { if (ev.key === 'Enter') { ev.preventDefault(); input.blur(); } });
    const n = uses.get(t.id) || 0;
    const count = document.createElement('span'); count.className = 'topic-uses';
    count.textContent = n ? n + (n === 1 ? ' entry' : ' entries') : '';
    const del = document.createElement('button'); del.type = 'button'; del.className = 'tool'; del.textContent = 'Delete';
    del.addEventListener('click', () => {
      if (!armed(del, 'Delete', n ? 'Take it off ' + (n === 1 ? '1 entry' : n + ' entries') + '?' : 'Delete topic?')) return;
      topics = topics.filter(x => x !== t);
      // It's taken off the entries that had it, without changing when they were last written in.
      for (const [id, e] of entries) if ((e.topics || []).includes(t.id)) { e.topics = e.topics.filter(x => x !== t.id); dirty.add(id); scheduleSave(id); }
      topicsChanged(); renderTopicsMenu();
    });
    li.append(num, input, count, del);
    return li;
  }));
  $('topicsEmpty').hidden = topics.length > 0;
  $('topicNextNum').textContent = topics.length + 1;
  $('topicNew').placeholder = 'Name of topic ' + (topics.length + 1);
}
function addTopic(){
  const name = $('topicNew').value.replace(/\s+/g, ' ').trim();
  topics.push({id:newTopicId(), name});
  $('topicNew').value = '';
  topicsChanged(); renderTopicsMenu();
  $('topicList').lastElementChild.scrollIntoView({block:'nearest'});
  $('topicNew').focus();
}
function openTopicsMenu(){ renderTopicsMenu(); $('topicsDialog').showModal(); $('topicNew').focus(); }
$('topicAdd').addEventListener('click', addTopic);
$('topicNew').addEventListener('keydown', ev => { if (ev.key === 'Enter') { ev.preventDefault(); addTopic(); } });
$('topicsMenuBtn').addEventListener('click', openTopicsMenu);
/* ---------- Export as PDF ----------
   The Menu's "Export as PDF" sends the open entry to the server, which writes it as journal/exports/<title>.pdf.
   The entry goes as blocks: writing (with its bold, underlining and numerals), each picture on its own, quotes,
   task lists and the days parts were written on. An entry it links to is named where the link is, in small
   raised writing after the word, like a footnote mark, and its own text follows at the end. Nothing in the entry changes. */
// Writing with its <b> and <u> as runs: {s, b, u}.
function exportRuns(text){
  const out = [], re = /<(\/?)([bu])>/g;
  let last = 0, m, b = false, u = false;
  const add = s => { if (s) out.push(Object.assign({s}, b ? {b:1} : {}, u ? {u:1} : {})); };
  while ((m = re.exec(text))) {
    add(text.slice(last, m.index)); last = re.lastIndex;
    if (m[2] === 'b') b = !m[1]; else u = !m[1];
  }
  add(text.slice(last));
  return out;
}
// A task's words: pictures in it are left out, and a linked entry is written as its name.
function exportTaskRuns(text){
  const parts = [], runs = [];
  parseText(text || '', parts);
  for (const p of parts) {
    if (p.type === 'text') runs.push(...exportRuns(p.text));
    else if (p.type === 'link') runs.push({s:linkName(p.id, p.title)});
    else if (p.type === 'pdf') runs.push({s:p.title || 'PDF'});
  }
  return runs;
}
// An entry's body as blocks. With marks (a Map), each linked entry is given a mark, kept in marks in the order
// they first come; without, a link is just written as the linked entry's name.
function exportBlocks(body, marks){
  const blocks = [];
  let runs = [], afterImg = false, subs = 0, subs2 = 0, num = 'I';
  const lastText = () => { const r = runs[runs.length - 1]; return r && r.s !== undefined ? r : null; };
  const flush = () => {
    // A line break just before a block (or the end) only ends the line; it doesn't make an empty one.
    const r = lastText();
    if (r && r.s.endsWith('\n')) r.s = r.s.slice(0, -1);
    if (runs.some(x => x.s === undefined || x.s !== '')) blocks.push({t:'text', runs});
    runs = [];
  };
  for (const p of parseBody(body)) {
    if (p.type === 'text') {
      // A picture takes a line of its own, so the spaces (and a line break) after it go.
      runs.push(...exportRuns(afterImg ? p.text.replace(/^[ \u00a0]*\n?/, '') : p.text));
      afterImg = false; continue;
    }
    afterImg = false;
    if (p.type === 'link') {
      if (marks) {
        let m = marks.get(p.id);
        if (!m) marks.set(p.id, m = {mark:linkName(p.id, p.title), id:p.id, title:p.title});
        const r = lastText(); if (r) r.s = r.s.replace(/[ \u00a0]+$/, '');   // the mark sits right after the word
        runs.push({mark:m.mark});
      } else runs.push({s:linkName(p.id, p.title)});
      continue;
    }
    if (p.type === 'pdf') { runs.push({s:p.title || 'PDF'}); continue; }   // a PDF is written as its title
    if (p.type === 'sub') {
      num = p.level === 2 ? roman(Math.max(subs, 1)) + '.' + roman(++subs2) : roman(++subs);
      if (p.level !== 2) subs2 = 0;
      runs.push({sub:num}); continue;
    }
    if (p.type === 'indent') { runs.push({indent:num}); continue; }
    if (p.type === 'img') {
      const r = lastText(); if (r) r.s = r.s.replace(/[ \u00a0]+$/, '');
      flush();
      blocks.push({t:'img', name:p.name, cap:p.title || ''});
      afterImg = true; continue;
    }
    flush();
    if (p.type === 'quote') blocks.push({t:'quote', s:p.text});
    else if (p.type === 'day') blocks.push({t:'day', s:makeWrittenDay(p.day).textContent});
    else if (p.type === 'tasks') blocks.push({t:'tasks', items:p.items.map(it => ({state:it.state, runs:exportTaskRuns(it.text)}))});
  }
  flush();
  return blocks;
}
// A picture that isn't a JPEG goes as its pixels (on white, at most 3000 across), compressed the way PDFs keep
// them; the server takes JPEGs straight from journal/images.
async function exportPicture(name){
  const img = new Image(); img.src = '/images/' + name;
  await img.decode();
  const k = Math.min(1, 3000 / Math.max(img.naturalWidth, img.naturalHeight));
  const w = Math.max(1, Math.round(img.naturalWidth * k)), h = Math.max(1, Math.round(img.naturalHeight * k));
  const c = document.createElement('canvas'); c.width = w; c.height = h;
  const x = c.getContext('2d');
  x.fillStyle = '#fff'; x.fillRect(0, 0, w, h); x.drawImage(img, 0, 0, w, h);
  const px = x.getImageData(0, 0, w, h).data, rgb = new Uint8Array(w * h * 3);
  for (let i = 0, j = 0; i < px.length; i += 4) { rgb[j++] = px[i]; rgb[j++] = px[i + 1]; rgb[j++] = px[i + 2]; }
  const packed = await new Response(new Blob([rgb]).stream().pipeThrough(new CompressionStream('deflate'))).blob();
  const data = await new Promise((res, rej) => {
    const r = new FileReader(); r.onload = () => res(String(r.result).split(',')[1]); r.onerror = rej; r.readAsDataURL(packed);
  });
  return {w, h, data};
}
// The Menu's PDF sizes (any left unset, the server uses its own defaults for).
function exportSizes(){
  const out = {};
  for (const k of ['exportBody', 'exportMark', 'exportNote', 'exportNoteName', 'exportPicture']) if (settings[k] !== undefined) out[k] = settings[k];
  return out;
}
function syncExport(){
  $('exportBtn').disabled = !(currentId && entries.get(currentId));
  $('exportNote').classList.remove('err');
  $('exportNote').textContent = $('exportBtn').disabled ? 'Open an entry to export it.' : '';
}
async function exportEntry(){
  const id = currentId, e = id && entries.get(id); if (!e) return;
  const btn = $('exportBtn'), note = $('exportNote');
  btn.disabled = true; note.classList.remove('err'); note.textContent = 'Exporting\u2026';
  try {
    const marks = new Map();
    const main = exportBlocks(withLegacyImages(e.body, e.images), marks);
    const notes = [...marks.values()].map(m => {
      const le = entries.get(m.id), title = linkName(m.id, m.title);
      return le ? {mark:m.mark, title, blocks:exportBlocks(withLegacyImages(le.body, le.images), null)} : {mark:m.mark, title, missing:true, blocks:[]};
    });
    const names = new Set();
    for (const b of [main, ...notes.map(n => n.blocks)].flat()) if (b.t === 'img' && !b.name.endsWith('.jpg')) names.add(b.name);
    const pics = {};
    for (const n of names) { try { pics[n] = await exportPicture(n); } catch (err) { /* left out if it can't be read */ } }
    const created = e.created ? 'Begun ' + fmtDate.format(new Date(e.created)) : '';
    const r = await fetch('/api/export', {method:'POST', headers:H, body:JSON.stringify({title:e.title || '', created, main, notes, pics, sizes:exportSizes()})});
    const d = await r.json().catch(() => ({}));
    if (!r.ok) throw new Error(d.error || 'server');
    note.textContent = 'Saved as ' + d.file + ' in journal/exports.';
  } catch (err) {
    note.textContent = err.message === 'font' ? "Couldn't export: no font could be found to set the writing in."
      : "Couldn't export the entry. Check that the journal server is still running.";
    note.classList.add('err');
  }
  btn.disabled = !(currentId && entries.get(currentId));
}
$('exportBtn').addEventListener('click', exportEntry);
$('menuBtn').addEventListener('click', syncExport);
$('quotesMenuBtn').addEventListener('click', openQuotes);
$('quotesClose').addEventListener('click', () => $('quotesDialog').close());
$('topicsClose').addEventListener('click', () => $('topicsDialog').close());
$('topicsDialog').addEventListener('click', ev => { if (ev.target === $('topicsDialog')) $('topicsDialog').close(); });

/* ---------- Which entries the list shows ----------
   Most recent: newest changes first. Most changes: the entries written in on the most days first (the day
   an entry was begun counts, and each later day it was changed). By topic: only the entries that have every
   topic chosen, newest first. The choice is kept with the settings, so it's the same next time. */
const LIST_VIEWS = ['recent', 'changes', 'topic'];
function listView(){ return LIST_VIEWS.includes(settings.listSort) ? settings.listSort : 'recent'; }
function listTopics(){ return (settings.listTopics || []).filter(id => topicById(id)); }
const changeDays = e => 1 + (e.history ? e.history.length : 0);
function renderListView(){
  const view = listView();
  for (const b of document.querySelectorAll('.view-tabs .view-tab')) b.setAttribute('aria-checked', String(b.dataset.view === view));
  const box = $('viewTopics');
  box.hidden = view !== 'topic';
  if (view !== 'topic') return;
  const chosen = listTopics(), hint = text => { const p = document.createElement('p'); p.className = 'view-hint'; p.textContent = text; return p; };
  box.replaceChildren();
  if (!topics.length) { box.append(hint('No topics yet. Make them in the Topics menu.')); return; }
  for (const t of topics) {
    const b = document.createElement('button'); b.type = 'button'; b.className = 'view-chip';
    const on = chosen.includes(t.id);
    b.setAttribute('aria-pressed', String(on)); b.textContent = topicText(t); b.title = topicText(t);
    b.addEventListener('click', () => {
      const next = on ? chosen.filter(id => id !== t.id) : chosen.concat(t.id);
      changeSetting('listTopics', next.length ? next : undefined);
      const again = [...box.querySelectorAll('.view-chip')].find(c => c.textContent === topicText(t)); if (again) again.focus({preventScroll:true});
    });
    box.append(b);
  }
  if (chosen.length) {
    const clear = document.createElement('button'); clear.type = 'button'; clear.className = 'view-chip clear'; clear.textContent = 'Clear';
    clear.addEventListener('click', () => changeSetting('listTopics', undefined));
    box.append(clear);
  }
  box.append(hint(!chosen.length ? 'Choose one or more topics to show only their entries.'
    : chosen.length > 1 ? 'Showing entries that have all of these topics.' : ''));
}
for (const b of document.querySelectorAll('.view-tabs .view-tab')) b.addEventListener('click', () => {
  changeSetting('listSort', b.dataset.view === 'recent' ? undefined : b.dataset.view);
  els.list.scrollTop = 0;
});

/* ---------- Entries ---------- */
function leaveCurrent(){
  if (!currentId) return;
  const id = currentId, e = entries.get(id);
  if (e && unsaved.has(id) && isEmpty(e)) { entries.delete(id); unsaved.delete(id); dirty.delete(id); clearTimeout(timers.get(id)); }
  else if (timers.has(id)) flush(id);
}
function open(id){
  if (!drawing.el.hidden) finishDrawing();
  if (id === currentId) { document.body.classList.add('editing'); return; }
  leaveCurrent();
  currentId = id; lastCaret = null;
  showEditor(); fillEditor(true); renderList();
  els.scroll.scrollTop = 0;
}
function newEntry(){
  if (!store) return;
  const now = Date.now(), id = newId();
  entries.set(id, {title:'', body:'', created:now, updated:now, images:[], history:[], side:[], topics:[], inks:{}, books:{}});
  unsaved.add(id);
  open(id);
  els.title.focus();
}
let armTimer;
function disarmDelete(){
  clearTimeout(armTimer); els.del.classList.remove('arm'); els.del.textContent = 'Archive';
  disarm($('delForever'), 'Delete forever');
}
async function deleteEntry(forever){
  const id = currentId, e = entries.get(id);
  disarmDelete();
  clearTimeout(timers.get(id)); timers.delete(id);
  const wasSaved = !unsaved.has(id), pictures = e ? e.images.concat(Object.keys(e.inks || {}).map(k => inkRec(e, k).img).filter(Boolean)) : [];
  entries.delete(id); dirty.delete(id); unsaved.delete(id);
  currentId = null; showEditor(); renderList();
  if (!store) return;
  try {
    await (writes.get(id) || Promise.resolve());
    if (wasSaved) await store.removeEntry(id, forever);
    else for (const name of pictures) await store.removeImage(name, forever);
    pictures.forEach(n => changed.delete(n));
  } catch (err) {
    els.where.textContent = forever ? "Couldn't delete that entry. Reload and try again." : "Couldn't archive that entry. Reload and try again.";
  }
}
async function onDelete(){
  if (!els.del.classList.contains('arm')) {
    disarm($('delForever'), 'Delete forever');
    els.del.classList.add('arm'); els.del.textContent = 'Archive this entry?';
    armTimer = setTimeout(disarmDelete, 4000); return;
  }
  deleteEntry(false);
}
function onDeleteForever(){
  const btn = $('delForever');
  if (!btn.classList.contains('arm')) { clearTimeout(armTimer); els.del.classList.remove('arm'); els.del.textContent = 'Archive'; }
  if (!armed(btn, 'Delete forever', "Delete forever? This can't be undone")) return;
  deleteEntry(true);
}

/* ---------- Wiring ---------- */
els.title.addEventListener('input', onTitleChange);
els.title.addEventListener('keydown', ev => {
  if (ev.key === 'Enter') {
    ev.preventDefault(); caretToEdge(true);
  }
});
els.body.addEventListener('input', onBodyChange);
// Writing added at the end of an entry on a new day goes in under that day's date.
els.body.addEventListener('beforeinput', ev => {
  if (ev.inputType === 'insertCompositionText') { dayBeforeWriting(); return; }   // typing through an input method
  if (ev.inputType !== 'insertText' && ev.inputType !== 'insertFromPaste') return;
  const text = ev.data != null ? ev.data : ev.dataTransfer ? ev.dataTransfer.getData('text/plain') : '';
  if (!text) return;
  const t = dayBeforeWriting(); if (!t) return;
  ev.preventDefault(); writeAfterDay(t, text);
});
els.body.addEventListener('paste', ev => {
  const files = ev.clipboardData ? [...ev.clipboardData.files] : [];
  if (files.length) { ev.preventDefault(); addFiles(files, caretTarget()); return; }
  if (richFallback) {
    ev.preventDefault();
    const text = ev.clipboardData.getData('text/plain'), t = text ? dayBeforeWriting() : null;
    if (t) writeAfterDay(t, text);
    else document.execCommand('insertText', false, text);
  }
});
els.title.addEventListener('paste', ev => {
  const files = ev.clipboardData ? [...ev.clipboardData.files] : [];
  if (files.length) { ev.preventDefault(); addFiles(files); }
});
// Clicking in the empty space under the last picture puts the cursor at the end
els.page.addEventListener('mousedown', ev => {
  if (ev.target !== els.page && ev.target !== els.body && ev.target !== els.scroll) return;
  const last = els.body.lastChild, r = els.body.getBoundingClientRect();
  const lastBottom = edgeY(last, false);
  if (lastBottom === null || ev.clientY <= lastBottom || ev.clientY > r.bottom + 200) return;
  ev.preventDefault();
  caretToEdge(false);
});
// Puts the cursor at the very start or end of the entry.
function caretToEdge(start){
  els.body.focus({preventScroll:true});
  const sel = document.getSelection();
  if (start) sel.collapse(els.body, 0);
  else sel.collapse(els.body, els.body.childNodes.length);
}

$('attach').addEventListener('click', () => els.file.click());
els.file.addEventListener('change', () => { addFiles(els.file.files); els.file.value = ''; });
$('viewerClose').addEventListener('click', () => els.viewer.close());
$('viewerRemove').addEventListener('click', removeViewing);
$('viewerRestore').addEventListener('click', restoreViewing);
$('viewerForever').addEventListener('click', foreverViewing);
els.viewer.addEventListener('close', () => disarm($('viewerForever'), 'Delete forever'));
$('viewerDraw').addEventListener('click', () => { const fig = viewingFig; els.viewer.close(); if (fig && els.body.contains(fig)) openDrawing(fig); });
els.viewer.addEventListener('click', ev => { if (ev.target === els.viewer) els.viewer.close(); });

const hasFiles = ev => ev.dataTransfer && [...ev.dataTransfer.types].includes('Files');
// While files are dragged over the page, the PDFs shown in frames let them pass, so a file dropped on one
// comes to the entry rather than being opened in that frame.
document.addEventListener('dragenter', ev => { if (hasFiles(ev)) document.body.classList.add('holding'); });
for (const type of ['drop', 'dragend']) document.addEventListener(type, () => document.body.classList.remove('holding'));
document.addEventListener('dragleave', ev => { if (!ev.relatedTarget) document.body.classList.remove('holding'); });
els.main.addEventListener('dragover', ev => {
  if (!hasFiles(ev)) return;
  ev.preventDefault();
  showMark(currentId ? dropTarget(ev.clientX, ev.clientY) : null);
});
els.main.addEventListener('dragleave', ev => { if (!els.main.contains(ev.relatedTarget)) showMark(null); });
els.main.addEventListener('drop', ev => {
  if (!hasFiles(ev)) return;
  ev.preventDefault(); showMark(null);
  const t = currentId ? dropTarget(ev.clientX, ev.clientY) : null;
  addFiles(ev.dataTransfer.files, t || {parent:els.body, ref:null});
});

els.search.addEventListener('input', () => { query = els.search.value; renderList(); });
$('newBtn').addEventListener('click', newEntry);
$('newBtn2').addEventListener('click', newEntry);
$('back').addEventListener('click', () => { leaveCurrent(); document.body.classList.remove('editing'); if (currentId && !entries.has(currentId)) { currentId = null; showEditor(); } renderList(); });
els.del.addEventListener('click', onDelete);
$('delForever').addEventListener('click', onDeleteForever);

/* Book models: a book is a box, so rather than guessing it from one picture, it's built exactly from
   photos of its front, spine and back. For each, the four corners are dragged onto the book's corners
   in the photo, and the photo is straightened out and put on the model at full sharpness. The boards
   overhang the page block a little, the spine is gently rounded (or flat), and the page edges are plain,
   gilt or sprinkled red. The proportions come from the photos and can be set by hand. Nothing is
   downloaded: the model is made in the page, saved in journal/models and shown on the right. */
const BOOK_FACES = ['front', 'spine', 'back', 'pages', 'inside', 'endsheet', 'leaf', 'boardEdges', 'headcap', 'tailcap'];
const BOOK_NAMES = {front:'Front', spine:'Spine', back:'Back', pages:'Page edges', inside:'Inside', endsheet:'Endpaper', leaf:'Paper',
  boardEdges:'Board edges',
  headcap:'Headcap', tailcap:'Tailcap'};
// Raised bands across the spine: where each is, as a fraction of the way down from the head. They start out
// evenly spaced, and each can be moved.
const evenBands = n => Array.from({length:n}, (_, i) => (i + 1) / (n + 1));
const BOOK_LEAVES = ['white', 'cream', 'aged', 'laid', 'rough', 'photo'];
const BOOK_ENDS = ['plain', 'marbled', 'combed', 'stone', 'none', 'photo'];
// The headbands' two silks: the main one, and the one worked over it.
const BOOK_HEADBANDS = {red:['#9A2130', '#EFE8D8'], green:['#2F5B3C', '#EFE8D8'], blue:['#264472', '#EFE8D8'], black:['#1F1D1B', '#EFE8D8'],
  brown:['#6A3F24', '#EFE8D8'], redgold:['#9A2130', '#D2AA4C'], greengold:['#2F5B3C', '#D2AA4C'], bluegold:['#264472', '#D2AA4C']};
const book = {entry:null, draft:null, face:'front', faces:{}, dims:{h:20, w:14, t:3, manual:false}, edges:'plain', leaf:'white', ends:'plain', backFrom:'own', insideBack:'mirror', round:true, bands:[], rimScale:1,
  timer:0, busy:false, drag:null, view:null, seq:0, openRaf:0};
const emptyBookFace = () => ({pic:null, data:null, quad:null, rot:0, extra:[[], [], [], []], zoom:{s:1, px:0, py:0}});
function bookFace(){ return book.faces[book.face]; }

/* Straightening a photo: the four corners (top-left, top-right, bottom-right, bottom-left) are mapped
   onto a rectangle, taking out the perspective of a photo taken at an angle. */
function squareToQuad(q){
  const [[x0, y0], [x1, y1], [x2, y2], [x3, y3]] = q;
  const dx1 = x1 - x2, dx2 = x3 - x2, dx3 = x0 - x1 + x2 - x3, dy1 = y1 - y2, dy2 = y3 - y2, dy3 = y0 - y1 + y2 - y3;
  let g = 0, h = 0;
  const den = dx1 * dy2 - dx2 * dy1;
  if ((dx3 || dy3) && den) { g = (dx3 * dy2 - dx2 * dy3) / den; h = (dx1 * dy3 - dx3 * dy1) / den; }
  return {a:x1 - x0 + g * x1, b:x3 - x0 + h * x3, c:x0, d:y1 - y0 + g * y1, e:y3 - y0 + h * y3, f:y0, g, h};
}
// The corners in the order that gives the photo turned by f.rot quarter turns.
const turnedQuad = f => [0, 1, 2, 3].map(i => f.quad[(i + f.rot) % 4]);
function quadSize(q){
  const d = (p, r) => Math.hypot(p[0] - r[0], p[1] - r[1]);
  return {w:(d(q[0], q[1]) + d(q[3], q[2])) / 2, h:(d(q[0], q[3]) + d(q[1], q[2])) / 2};
}
// The true width:height of a rectangle photographed at an angle (Zhang and He's method, taking the middle of
// the photo as where the camera pointed). When there's too little perspective to tell, the average lengths
// of the sides are used, which are then right anyway.
function trueAspect(q, iw, ih){
  const size = quadSize(q), simple = size.w / Math.max(size.h, 1e-6), u0 = iw / 2, v0 = ih / 2;
  const [m1, m2, m4, m3] = q.map(p => [p[0], p[1], 1]);   // top-left, top-right, bottom-right, bottom-left
  const cross = (a, b) => [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]];
  const dot = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
  const c14 = cross(m1, m4), k2 = dot(c14, m3) / dot(cross(m2, m4), m3), k3 = dot(c14, m2) / dot(cross(m3, m4), m2);
  const n2 = m2.map((v, i) => k2 * v - m1[i]), n3 = m3.map((v, i) => k3 * v - m1[i]);
  const f2 = -((n2[0] * n3[0] - (n2[0] * n3[2] + n2[2] * n3[0]) * u0 + n2[2] * n3[2] * u0 * u0)
             + (n2[1] * n3[1] - (n2[1] * n3[2] + n2[2] * n3[1]) * v0 + n2[2] * n3[2] * v0 * v0)) / (n2[2] * n3[2]);
  if (!(f2 > 0) || !isFinite(f2)) return simple;
  const len = n => ((n[0] - u0 * n[2]) ** 2 + (n[1] - v0 * n[2]) ** 2) / f2 + n[2] * n[2];
  const r = Math.sqrt(len(n2) / len(n3));
  return isFinite(r) && r > simple / 3 && r < simple * 3 ? r : simple;
}
// The four sides in the order that gives the photo turned by f.rot quarter turns. Side k runs from corner k
// to corner k + 1 (top: left to right, right: top to bottom, bottom: right to left, left: bottom to top).
const turnedSides = f => [0, 1, 2, 3].map(i => f.extra[(i + f.rot) % 4]);
function invert3(m){
  const [a, b, c, d, e, f, g, h, i] = m, A = e * i - f * h, B = -(d * i - f * g), C = d * h - e * g, det = a * A + b * B + c * C;
  return [A, -(b * i - c * h), b * f - c * e, B, a * i - c * g, -(a * f - c * d), C, -(a * h - b * g), a * e - b * d].map(v => v / det);
}
const mapQuad = (m, u, v) => { const den = m.g * u + m.h * v + 1; return [(m.a * u + m.b * v + m.c) / den, (m.d * u + m.e * v + m.f) / den]; };
/* The outline of a photo's book: its perspective (from the four corners) and the shape of each side. Points
   added along a side are taken back into the straightened square (by undoing the perspective), and a smooth
   curve is drawn through them, so a single point already makes a good arc for the head of a rounded spine.
   Each side is a function giving how far it's pushed in or out at each point along it (0 to 1).
   Sides in turned order: top (left to right), right (top to bottom), bottom, left. */
function outlineOf(f){
  const m = squareToQuad(turnedQuad(f)), sides = turnedSides(f);
  const inv = invert3([m.a, m.b, m.c, m.d, m.e, m.f, m.g, m.h, 1]);
  const back = ([x, y]) => { const w = inv[6] * x + inv[7] * y + inv[8]; return [(inv[0] * x + inv[1] * y + inv[2]) / w, (inv[3] * x + inv[4] * y + inv[5]) / w]; };
  // A smooth curve through the points (a cubic Hermite spline), as a function of the position along the side.
  const curve = (pts, by, other) => {
    pts = pts.slice().sort((a, b) => a[by] - b[by]);
    const xs = pts.map(p => p[by]), ys = pts.map(p => p[other]), n = xs.length;
    const slope = (i, j) => (ys[j] - ys[i]) / Math.max(xs[j] - xs[i], 1e-9);
    const ms = xs.map((_, k) => k === 0 ? slope(0, 1) : k === n - 1 ? slope(n - 2, n - 1) : slope(k - 1, k + 1));
    return t => {
      t = Math.max(xs[0], Math.min(xs[n - 1], t));
      let k = 0; while (k < n - 2 && xs[k + 1] < t) k++;
      const h = Math.max(xs[k + 1] - xs[k], 1e-9), s = (t - xs[k]) / h, s2 = s * s, s3 = s2 * s;
      return (2 * s3 - 3 * s2 + 1) * ys[k] + (s3 - 2 * s2 + s) * h * ms[k] + (-2 * s3 + 3 * s2) * ys[k + 1] + (s3 - s2) * h * ms[k + 1];
    };
  };
  return {m, back, curved:sides.some(x => x.length),
    top:curve([[0, 0], [1, 0], ...sides[0].map(back)], 0, 1), right:curve([[1, 0], [1, 1], ...sides[1].map(back)], 1, 0),
    bottom:curve([[0, 1], [1, 1], ...sides[2].map(back)], 0, 1), left:curve([[0, 0], [0, 1], ...sides[3].map(back)], 1, 0)};
}
// Where turned side k is, a fraction t of the way along it (left to right, or top to bottom), in the photo.
function outlinePoint(o, k, t){
  return k === 0 ? mapQuad(o.m, t, o.top(t)) : k === 1 ? mapQuad(o.m, o.right(t), t)
    : k === 2 ? mapQuad(o.m, t, o.bottom(t)) : mapQuad(o.m, o.left(t), t);
}
/* Straightening a photo. The four corners are mapped onto a rectangle, taking out the perspective of a photo
   taken at an angle. Where points have been added along the sides (the head and tail of a rounded spine,
   a cover that isn't quite flat), the curved sides are followed, and the inside is blended smoothly between
   them. With only the four corners, it's the plain perspective correction. */
function straighten(f, maxSide){
  const q = turnedQuad(f), size = quadSize(q), k = Math.min(1, maxSide / Math.max(size.w, size.h, 1));
  const W = Math.max(2, Math.round(size.w * k)), H = Math.max(2, Math.round(size.h * k));
  const o = outlineOf(f), m = o.m, src = f.data, sw = src.width, sh = src.height, s = src.data, curved = o.curved;
  const sample = (fn, n) => Float32Array.from({length:n}, (_, i) => fn((i + .5) / n));
  const top = curved && sample(o.top, W), bot = curved && sample(o.bottom, W), left = curved && sample(o.left, H), right = curved && sample(o.right, H);
  const out = new ImageData(W, H), od = out.data;
  for (let y = 0; y < H; y++) {
    const v0 = (y + .5) / H;
    for (let x = 0; x < W; x++) {
      const u0 = (x + .5) / W;
      const u = curved ? (1 - u0) * left[y] + u0 * right[y] : u0, v = curved ? (1 - v0) * top[x] + v0 * bot[x] : v0;
      const den = m.g * u + m.h * v + 1;
      let sx = (m.a * u + m.b * v + m.c) / den - .5, sy = (m.d * u + m.e * v + m.f) / den - .5;
      sx = Math.max(0, Math.min(sw - 1.001, sx)); sy = Math.max(0, Math.min(sh - 1.001, sy));
      const ix = sx | 0, iy = sy | 0, fx = sx - ix, fy = sy - iy;
      const i00 = (iy * sw + ix) * 4, i10 = i00 + 4, i01 = i00 + sw * 4, i11 = i01 + 4, j = (y * W + x) * 4;
      for (let c = 0; c < 3; c++) {
        od[j + c] = (s[i00 + c] * (1 - fx) + s[i10 + c] * fx) * (1 - fy) + (s[i01 + c] * (1 - fx) + s[i11 + c] * fx) * fy;
      }
      od[j + 3] = 255;
    }
  }
  const cv = document.createElement('canvas'); cv.width = W; cv.height = H;
  cv.getContext('2d').putImageData(out, 0, 0);
  return cv;
}
// The colour round the edge of a straightened photo: the cloth or leather of the cover.
function edgeColour(cv){
  const n = 24, c = document.createElement('canvas'); c.width = c.height = n;
  const x = c.getContext('2d', {willReadFrequently:true}); x.drawImage(cv, 0, 0, n, n);
  const d = x.getImageData(0, 0, n, n).data, sum = [0, 0, 0]; let count = 0;
  for (let y = 0; y < n; y++) for (let i = 0; i < n; i++) {
    if (i > 1 && i < n - 2 && y > 1 && y < n - 2) continue;
    const k = (y * n + i) * 4; sum[0] += d[k]; sum[1] += d[k + 1]; sum[2] += d[k + 2]; count++;
  }
  return sum.map(v => v / count);
}
const toLinear = c => c.map(v => Math.pow(v / 255, 2.2)).concat(1);
// The page edges, seen edge-on: fine lines of paper, gold leaf, or paper sprinkled red.
function edgeTexture(kind){
  const W = 64, H = 256, cv = document.createElement('canvas'); cv.width = W; cv.height = H;
  const x = cv.getContext('2d'), img = x.createImageData(W, H), d = img.data;
  let seed = 7; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  const rows = [];
  for (let y = 0; y < H; y++) rows.push(rnd());
  for (let y = 0; y < H; y++) for (let i = 0; i < W; i++) {
    const r = rows[y], k = (y * W + i) * 4, grain = rnd() * 6;
    let c;
    if (kind === 'gilt') { const s = 0.86 + r * 0.14; c = [205 * s + grain, 165 * s + grain, 78 * s]; }
    else {
      const s = 0.9 + r * 0.1;
      c = [236 * s + grain, 226 * s + grain, 204 * s + grain];
      if (kind === 'red' && rnd() < 0.3) c = [168 + grain * 3, 42 + grain, 38 + grain];
    }
    d[k] = c[0]; d[k + 1] = c[1]; d[k + 2] = c[2]; d[k + 3] = 255;
  }
  x.putImageData(img, 0, 0);
  return cv;
}

/* The paper of the pages, made up (a page's worth, the shape of the page, stretched over each): cream, aged
   (yellowed, darker towards the edges, with a few foxing spots), laid (the fine lines and the chain lines of a
   laid mould), or handmade (rough, with fibres). Made the same way every time. */
const leafMade = new Map();
function leafTexture(kind, aspect){
  const W = 768, H = Math.max(256, Math.min(2048, Math.round(W / Math.max(0.3, aspect)))), key = kind + ':' + H;
  if (leafMade.has(key)) return leafMade.get(key);
  let seed = 11; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  // Soft blotches: a few random tones, spread smoothly over the page.
  const cloud = (cols, rows) => {
    const small = document.createElement('canvas'); small.width = cols; small.height = rows;
    const sx = small.getContext('2d'), sd = sx.createImageData(cols, rows);
    for (let i = 0; i < cols * rows; i++) { const v = rnd() * 255; sd.data.set([v, v, v, 255], i * 4); }
    sx.putImageData(sd, 0, 0);
    const big = document.createElement('canvas'); big.width = W; big.height = H;
    const bx = big.getContext('2d'); bx.imageSmoothingQuality = 'high'; bx.drawImage(small, 0, 0, W, H);
    return bx.getImageData(0, 0, W, H).data;
  };
  const base = {cream:[243, 235, 214], aged:[234, 218, 184], laid:[244, 240, 228], rough:[240, 235, 224]}[kind] || [251, 250, 246];
  const big = cloud(6, 8), mid = cloud(24, 32);
  const cv = document.createElement('canvas'); cv.width = W; cv.height = H;
  const x = cv.getContext('2d'), img = x.createImageData(W, H), d = img.data;
  const chain = Math.round(W / 14);
  for (let y = 0; y < H; y++) for (let i = 0; i < W; i++) {
    const k = (y * W + i) * 4, b = (big[k] / 255 - 0.5), m = (mid[k] / 255 - 0.5), grain = rnd() - 0.5;
    let v = 0, warm = 0;
    if (kind === 'cream') v = b * 6 + m * 3 + grain * 5;
    else if (kind === 'aged') {
      const ex = Math.min(i, W - 1 - i) / W, ey = Math.min(y, H - 1 - y) / H, edge = Math.max(0, 0.12 - Math.min(ex, ey)) / 0.12;
      v = b * 16 + m * 7 + grain * 6 - edge * edge * 26; warm = edge * edge * 10 + Math.max(0, -b) * 8;
    } else if (kind === 'laid') {
      v = b * 4 + m * 2 + grain * 4 + (y % 3 === 0 ? -4 : 1);
      const c = i % chain; if (c < 2) v -= 5;
    } else if (kind === 'rough') v = b * 8 + m * 8 + grain * 16;
    d[k] = base[0] + v; d[k + 1] = base[1] + v - warm * 0.4; d[k + 2] = base[2] + v - warm; d[k + 3] = 255;
  }
  x.putImageData(img, 0, 0);
  if (kind === 'aged') {   // foxing: a few small brown spots
    for (let n = 0; n < 26; n++) {
      const cx = rnd() * W, cy = rnd() * H, r = 1.5 + rnd() * 6, g = x.createRadialGradient(cx, cy, 0, cx, cy, r);
      g.addColorStop(0, 'rgba(150,100,50,' + (0.18 + rnd() * 0.25) + ')'); g.addColorStop(1, 'rgba(150,100,50,0)');
      x.fillStyle = g; x.fillRect(cx - r, cy - r, 2 * r, 2 * r);
    }
  }
  if (kind === 'rough') {   // fibres
    x.lineCap = 'round';
    for (let n = 0; n < 900; n++) {
      const cx = rnd() * W, cy = rnd() * H, a = rnd() * Math.PI, l = 4 + rnd() * 14;
      x.strokeStyle = 'rgba(120,105,80,' + (0.05 + rnd() * 0.08) + ')'; x.lineWidth = 0.6 + rnd() * 0.6;
      x.beginPath(); x.moveTo(cx, cy); x.quadraticCurveTo(cx + Math.cos(a) * l / 2 + rnd() * 3, cy + Math.sin(a) * l / 2, cx + Math.cos(a) * l, cy + Math.sin(a) * l); x.stroke();
    }
  }
  leafMade.set(key, cv);
  return cv;
}

/* Endpaper, made up: a whole sheet, two pages wide (aspect is a page's), folded down the middle into the half pasted
   inside the board and the free leaf. Plain, marbled (colours drawn out into swirls and veins), combed (bands of
   colour combed into fine waves) or stone (Turkish marbling: drops of colour lying side by side). The pattern is
   the same size whatever the page's shape, and made the same way every time. */
const endMade = new Map();
// A headband's silk: the main colour, worked over with slanting stitches of the other.
// The back of the book as it shows between the boards of the open book, above the pages (below them at the tail, the
// same the other way up): across, from the left board's edge to the right's; down, from the boards' edge to the
// pages'. The covering's colour, in shadow at the joints and a little in the middle, the edge of the leather turned
// in over it at the top, and the headband (if there is one) lying across it against the pages, running on under the
// boards at both ends.
function spineWindowTexture(colour, headband){
  const W = 256, H = 128, cv = document.createElement('canvas'); cv.width = W; cv.height = H;
  const x = cv.getContext('2d'), rgb = 'rgb(' + colour.map(v => Math.round(v)).join(',') + ')';
  x.fillStyle = rgb; x.fillRect(0, 0, W, H);
  const v = x.createLinearGradient(0, 0, 0, H);   // the turned-in edge of the covering, and deeper down towards the pages
  v.addColorStop(0, 'rgba(0,0,0,.45)'); v.addColorStop(.08, 'rgba(0,0,0,.25)'); v.addColorStop(.3, 'rgba(0,0,0,.3)'); v.addColorStop(1, 'rgba(0,0,0,.45)');
  x.fillStyle = v; x.fillRect(0, 0, W, H);
  if (headband) {
    const y0 = Math.round(H * 0.68), h = H - y0;
    x.fillStyle = headband[0]; x.fillRect(0, y0, W, h);
    x.strokeStyle = headband[1]; x.lineWidth = 7;
    x.beginPath(); for (let i = -40; i < W + 40; i += 14) { x.moveTo(i, H); x.lineTo(i + 12, y0); } x.stroke();
    const g = x.createLinearGradient(0, y0, 0, H);   // round: lit along its top, shadowed underneath where it meets the pages
    g.addColorStop(0, 'rgba(0,0,0,.35)'); g.addColorStop(.18, 'rgba(255,255,255,.25)'); g.addColorStop(.5, 'rgba(0,0,0,0)'); g.addColorStop(1, 'rgba(0,0,0,.45)');
    x.fillStyle = g; x.fillRect(0, y0, W, h);
  }
  const s = x.createLinearGradient(0, 0, W, 0);   // the joints, where it goes in under the boards
  s.addColorStop(0, 'rgba(0,0,0,.55)'); s.addColorStop(.1, 'rgba(0,0,0,.1)'); s.addColorStop(.5, 'rgba(0,0,0,.12)'); s.addColorStop(.9, 'rgba(0,0,0,.1)'); s.addColorStop(1, 'rgba(0,0,0,.55)');
  x.fillStyle = s; x.fillRect(0, 0, W, H);
  return cv;
}
function headbandTexture(colours){
  const cv = document.createElement('canvas'); cv.width = 256; cv.height = 64;
  const x = cv.getContext('2d');
  x.fillStyle = colours[0]; x.fillRect(0, 0, 256, 64);
  // (four stitches across the texture, which repeats about once for each width of the roll along it)
  x.strokeStyle = colours[1]; x.lineWidth = 28;
  x.beginPath(); for (let i = -128; i < 384; i += 64) { x.moveTo(i, 64); x.lineTo(i + 40, 0); } x.stroke();
  x.strokeStyle = 'rgba(0,0,0,.28)'; x.lineWidth = 5;
  x.beginPath(); for (let i = -128; i < 384; i += 64) { x.moveTo(i + 17, 64); x.lineTo(i + 57, 0); } x.stroke();
  return cv;
}
function endTexture(kind, aspect){
  const H = 1000, W = Math.max(300, Math.min(4000, Math.round(2 * H * aspect))), key = kind + ':' + W;
  if (endMade.has(key)) return endMade.get(key);
  let seed = 23; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  const cv = document.createElement('canvas'); cv.width = W; cv.height = H;
  const x = cv.getContext('2d');
  const pal = [[34, 52, 96], [142, 38, 36], [196, 152, 64], [232, 222, 196], [38, 74, 62], [112, 72, 40]];
  if (kind === 'stone') {
    x.fillStyle = 'rgb(222,208,176)'; x.fillRect(0, 0, W, H);
    for (let n = 0, all = Math.round(2600 * W * H / (768 * 1097)); n < all; n++) {
      const cx = rnd() * W, cy = rnd() * H, r = 5 + Math.pow(rnd(), 2) * 30, c = pal[(rnd() * pal.length) | 0];
      x.beginPath();
      for (let a = 0; a <= 24; a++) { const t = a / 24 * Math.PI * 2, rr = r * (0.85 + rnd() * 0.3); x.lineTo(cx + Math.cos(t) * rr, cy + Math.sin(t) * rr); }
      x.closePath(); x.fillStyle = 'rgb(' + c.join(',') + ')'; x.fill();
      x.lineWidth = 0.8 + rnd(); x.strokeStyle = 'rgba(20,16,12,.55)'; x.stroke();
    }
  } else if (kind === 'marbled' || kind === 'combed') {
    const img = x.createImageData(W, H), d = img.data, n = pal.length;
    for (let y = 0; y < H; y++) for (let i = 0; i < W; i++) {
      const u = 1.9 * i / H, v = 1.4 * y / H, k = (y * W + i) * 4;
      let t;
      if (kind === 'marbled') {
        const wx = u + 0.07 * Math.sin(v * 17 + 3 * Math.sin(u * 7)) + 0.025 * Math.sin(v * 53 + u * 13);
        const wy = v + 0.05 * Math.sin(u * 15 + 2 * Math.sin(v * 9));
        t = wx * 7 + 0.6 * Math.sin(wy * 11 + wx * 4);
      } else t = u * 34 + 0.9 * Math.sin(v * 70 + u * 5) + 0.25 * Math.sin(v * 260);
      const band = Math.floor(t), f = t - band, c = pal[((band % n) + n) % n], next = pal[(((band + 1) % n) + n) % n];
      const vein = kind === 'marbled' ? Math.max(0, 1 - Math.abs(f - 0.5) * 40) * 0.5 : 0;   // dark veins between colours
      const m = f > 0.85 ? (f - 0.85) / 0.15 : 0, g = (rnd() - 0.5) * 8;
      for (let j = 0; j < 3; j++) d[k + j] = (c[j] * (1 - m) + next[j] * m) * (1 - vein) + g;
      d[k + 3] = 255;
    }
    x.putImageData(img, 0, 0);
  } else {   // plain: a sheet of cream paper
    const half = leafTexture('cream', aspect);
    x.drawImage(half, 0, 0, W / 2, H); x.drawImage(half, W / 2, 0, W / 2, H);
    x.fillStyle = 'rgba(214,196,160,.35)'; x.fillRect(0, 0, W, H);
  }
  endMade.set(key, cv);
  return cv;
}
/* The inside of a board as a rebound book has it: the covering turned in over the edges of the board (under: the
   photo of the inside of a board, or a colour), and the endpaper (sheet) pasted over it, stopping short of the edges at the head, fore-edge and tail and
   running into the joint at the spine (on the right, as the board lies open). */
// One half of a sheet (0 the left, 1 the right).
function sheetHalf(cv, i){
  const h = document.createElement('canvas'); h.width = Math.round(cv.width / 2); h.height = cv.height;
  h.getContext('2d').drawImage(cv, -i * h.width, 0);
  return h;
}
function pastedown(sheet, under, aspect, spineLeft, inset){
  const H = 1400, W = Math.max(200, Math.round(H * aspect)), cv = document.createElement('canvas'); cv.width = W; cv.height = H;
  const x = cv.getContext('2d');
  if (Array.isArray(under)) { x.fillStyle = 'rgb(' + under.map(v => Math.round(v)).join(',') + ')'; x.fillRect(0, 0, W, H); }
  else x.drawImage(under, 0, 0, W, H);
  // (spineLeft: for the back board, as it lies open, with the spine on its left)
  // (just the size of the pages: in from the head, tail and fore-edge by as far as the boards reach past them)
  const ins = inset || 0.016, ix = Math.round(W * ins / aspect), iy = Math.round(H * ins), sx = spineLeft ? 0 : ix, ex = spineLeft ? W - ix : W;
  x.drawImage(sheet, sx, iy, W - ix, H - 2 * iy);
  // the sheet's edge, a little raised over the leather
  x.strokeStyle = 'rgba(0,0,0,.28)'; x.lineWidth = 2;
  const fx = spineLeft ? ex : sx, jx = spineLeft ? 0 : W;
  x.beginPath(); x.moveTo(jx, iy); x.lineTo(fx, iy); x.lineTo(fx, H - iy); x.lineTo(jx, H - iy); x.stroke();
  return cv;
}

/* The book's shape. Units don't matter (the viewer scales every model to fit); the height is 1.
   Up is +Y, the front cover faces +Z, and the spine is at -X, as when you hold a book to read it. */
function bookGeometry(p){
  const H = 1, W = p.w / p.h, T = p.t / p.h;
  const bt = Math.min(0.013, T * 0.09), sq = Math.min(0.016, W * 0.04), d = p.round ? T * 0.2 : T * 0.02;
  const xl = -W / 2, xr = W / 2, zo = T / 2, zi = T / 2 - bt, top = H / 2;
  const groups = new Map();   // material name -> {pos, nrm, uv, idx}
  const g = name => { if (!groups.has(name)) groups.set(name, {pos:[], nrm:[], uv:[], idx:[]}); return groups.get(name); };
  // A flat four-sided face: corners in order round it, its outward normal, and the texture position of each corner.
  const quad = (mat, pts, n, uvs) => {
    const o = g(mat), b = o.pos.length / 3;
    const e1 = pts[1].map((v, i) => v - pts[0][i]), e2 = pts[2].map((v, i) => v - pts[0][i]);
    const cr = [e1[1] * e2[2] - e1[2] * e2[1], e1[2] * e2[0] - e1[0] * e2[2], e1[0] * e2[1] - e1[1] * e2[0]];
    const flip = cr[0] * n[0] + cr[1] * n[1] + cr[2] * n[2] < 0;
    pts.forEach((pt, i) => { o.pos.push(...pt); o.nrm.push(...n); o.uv.push(...uvs[i]); });
    o.idx.push(...(flip ? [b, b + 2, b + 1, b, b + 3, b + 2] : [b, b + 1, b + 2, b, b + 2, b + 3]));
  };
  const box = (x0, x1, y0, y1, z0, z1, mats, uvFor) => {
    const faces = {
      px:[[[x1, y0, z0], [x1, y0, z1], [x1, y1, z1], [x1, y1, z0]], [1, 0, 0]],
      py:[[[x0, y1, z0], [x1, y1, z0], [x1, y1, z1], [x0, y1, z1]], [0, 1, 0]],
      ny:[[[x0, y0, z0], [x1, y0, z0], [x1, y0, z1], [x0, y0, z1]], [0, -1, 0]],
      pz:[[[x0, y0, z1], [x1, y0, z1], [x1, y1, z1], [x0, y1, z1]], [0, 0, 1]],
      nz:[[[x0, y0, z0], [x1, y0, z0], [x1, y1, z0], [x0, y1, z0]], [0, 0, -1]]};
    for (const [f, mat] of Object.entries(mats)) quad(mat, faces[f][0], faces[f][1], faces[f][0].map(pt => uvFor(f, pt)));
  };
  // The boards: the photo on the outside, endpaper inside, the covering's colour round the edges. A photo of the
  // inside is put over the whole inner face of each board, as it was taken (turned round for the back, where the
  // spine is on the other side); only its outer edge shows, above the page edges at the head, fore-edge and tail.
  // The outer edges of the boards (head, fore-edge and tail of both) share one photo of a stretch of edge, laid
  // along each edge from the spine (or, on the fore-edge, from the head), its top on the outside of the board, and
  // repeated at its true size: its depth fills the board's thickness, so each copy is as long as the photo's own
  // proportions make it (times p.rim.scale). Nothing is stretched, whatever the length of the edge.
  // p.rim = {aspect, scale}: the straightened photo's length:depth.
  const across = z => (zo - Math.abs(z)) / (zo - zi);
  const tile = p.rim ? Math.max(1e-4, p.rim.aspect * bt * (p.rim.scale || 1)) : 1;
  const coverUv = (f, [x, y, z]) => f === 'pz' ? [(x - xl) / W, (top - y) / H] : f === 'nz' ? [(xr - x) / W, (top - y) / H]
    : f === 'px' ? [(top - y) / tile, across(z)] : [(x - xl) / tile, across(z)];
  const rims = p.rim ? {px:'rim', py:'rim', ny:'rim'} : {px:'board', py:'board', ny:'board'};
  box(xl, xr, -top, top, zi, zo, Object.assign({pz:'front', nz:p.inside ? 'insideFront' : 'endpaper'}, rims), coverUv);
  box(xl, xr, -top, top, -zo, -zi, Object.assign({nz:'back', pz:p.inside ? 'insideBack' : 'endpaper'}, rims), coverUv);
  // The page block, set in from the edges of the boards; the lines of the pages run along its edges.
  // (A photo of the page edges is stretched once over each; the made-up paper and gilt repeat along them.)
  const reps = p.edges === 'photo' ? 1 : 4, px1 = xr - sq, py1 = top - sq, edgeUv = (f, [x, y, z]) => {
    const across = (z + zi) / (2 * zi);
    return f === 'px' ? [(py1 - y) / (2 * py1) * reps, across] : [(x - xl) / (px1 - xl) * reps, across];
  };
  box(xl, px1, -py1, py1, -zi, zi, {px:'edges', py:p.edges === 'giltTop' ? 'giltEdge' : 'edges', ny:'edges'}, edgeUv);
  // The paper of the pages, on the two faces of the page block that the boards lie on, just under them: seen only
  // once the book is open, as it's read (the reader lays the PDF's pages on it).
  // Over it, the free endpapers: the first and last leaves, their decorated side facing the boards.
  for (const [mat, on, zl] of [['leaf', p.leaf, Math.max(zi * 0.5, zi - 0.004)], ['endsheet', p.ends, Math.max(zi * 0.75, zi - 0.002)]]) {
    if (!on) continue;
    for (const back of [false, true]) {
      const z = back ? -zl : zl, pts = [[xl, -py1, z], [px1, -py1, z], [px1, py1, z], [xl, py1, z]];
      quad(mat, pts, [0, 0, back ? -1 : 1], pts.map(([x, y]) => [back ? (px1 - x) / (px1 - xl) : (x - xl) / (px1 - xl), (py1 - y) / (2 * py1)]));
    }
  }
  // The spine: an arc from the back board round to the front, carrying the spine photo, closed at head and tail.
  const N = p.round ? 20 : 2, sp = g('spine'), sb = sp.pos.length / 3;
  const arc = [];
  for (let i = 0; i <= N; i++) {
    const th = -Math.PI / 2 + Math.PI * i / N, x = xl - d * Math.cos(th), z = zo * Math.sin(th);
    const n = [-zo * Math.cos(th), 0, d * Math.sin(th)], l = Math.hypot(...n) || 1;
    arc.push([x, z]);
    for (const y of [top, -top]) {
      sp.pos.push(x, y, z); sp.nrm.push(n[0] / l, 0, n[2] / l); sp.uv.push((z + zo) / T, y > 0 ? 0 : 1);
    }
  }
  for (let i = 0; i < N; i++) { const a = sb + i * 2; sp.idx.push(a, a + 2, a + 1, a + 1, a + 2, a + 3); }
  // Raised bands: ridges across the spine, carrying the spine's photo just as the spine under them does. Each is a
  // rounded bump, full height across the back of the spine and dying away towards the joints.
  if (p.bands && p.bands.length) {
    const M = 32, K = 8, bw = Math.min(0.022, Math.max(0.012, T * 0.14)), bh = Math.max(0.004, Math.min(0.011, T * 0.06));
    const dd = Math.max(d, T * 0.02);
    for (const f of p.bands) {
      const yc = top - Math.max(bw, Math.min(H - bw, f * H)), o = g('spine'), b = o.pos.length / 3;
      for (let i = 0; i <= M; i++) {
        const t = i / M, th = -Math.PI / 2 + Math.PI * t, x = xl - dd * Math.cos(th), z = zo * Math.sin(th);
        const nl = Math.hypot(zo * Math.cos(th), dd * Math.sin(th)) || 1, nx = -zo * Math.cos(th) / nl, nz = dd * Math.sin(th) / nl;
        const taper = Math.min(1, Math.min(t, 1 - t) / 0.1);
        for (let j = 0; j <= K; j++) {
          const sj = j / K, off = bh * taper * Math.sin(Math.PI * sj), slope = bh * taper * Math.PI * Math.cos(Math.PI * sj);
          const y = yc + bw * (0.5 - sj);   // from the head side of the band to the tail side
          o.pos.push(x + nx * (off + 0.0004), y, z + nz * (off + 0.0004));
          const n = [nx * bw, slope, nz * bw], l = Math.hypot(...n) || 1;
          o.nrm.push(n[0] / l, n[1] / l, n[2] / l);
          o.uv.push((z + zo) / T, (top - y) / H);
        }
      }
      for (let i = 0; i < M; i++) for (let j = 0; j < K; j++) {
        const a = b + i * (K + 1) + j, c = a + K + 1;
        o.idx.push(a, c, a + 1, a + 1, c, c + 1);
      }
    }
  }
  // With a photo of the headcap (or tailcap), the end of the spine reaches a little way in over the pages, as the
  // leather turned over the headband does, and the photo covers it all: the outside of the spine at the photo's top,
  // seen from above for the head and from below for the tail.
  for (const [y, ny, mat, has] of [[top, 1, 'headcap', p.head], [-top, -1, 'tailcap', p.tail]]) {
    const band = has ? Math.min(px1 - xl, Math.max(sq * 2, T * 0.12)) : 0, depth = d + band || 1;
    const capUv = (x, z) => has ? [ny > 0 ? (zo - z) / T : (z + zo) / T, (x - (xl - d)) / depth] : [0, 0];
    const cap = g(mat), cb = cap.pos.length / 3;
    cap.pos.push(xl, y, 0); cap.nrm.push(0, ny, 0); cap.uv.push(...capUv(xl, 0));
    for (const [x, z] of arc) { cap.pos.push(x, y, z); cap.nrm.push(0, ny, 0); cap.uv.push(...capUv(x, z)); }
    for (let i = 1; i <= N; i++) cap.idx.push(...(ny > 0 ? [cb, cb + i + 1, cb + i] : [cb, cb + i, cb + i + 1]));
    if (!band) continue;
    const xb = xl + band, flat = [[xl, y, -zi], [xb, y, -zi], [xb, y, zi], [xl, y, zi]];
    quad(mat, flat, [0, ny, 0], flat.map(([x, , z]) => capUv(x, z)));
    quad('capSide', [[xb, ny * py1, -zi], [xb, y, -zi], [xb, y, zi], [xb, ny * py1, zi]], [1, 0, 0], [[0, 0], [0, 0], [0, 0], [0, 0]]);
  }
  // The headbands: a little roll of silk at the head and the tail of the pages, along the back of the page block
  // where it meets the spine, half of it set into the spine, standing a little proud of the pages' edges (but not of
  // the boards).
  if (p.headband) {
    const r = Math.min(sq * 0.3, Math.max(0.002, T * 0.025)), cx = xl, reps = Math.max(1, Math.round(zi / r));
    for (const s of [1, -1]) {
      headbandTube(cx, s * (py1 - r * 0.3), r, zi, reps, g('headband'), [d, zo]);
      // Behind it, the inside of the spine's end (the covering turned in over the headband): it stays put as the
      // book opens, so the headband always has it at its back.
      const wall = [[xl, s * py1, -zi], [xl, s * top, -zi], [xl, s * top, zi], [xl, s * py1, zi]];
      quad('headWall', wall, [1, 0, 0], [[0, 0], [0, 0], [0, 0], [0, 0]]);
    }
  }
  // The back of the book between the boards, above and below the pages, as the reader shows it when the book lies
  // open: a strip on the inside of each board by the spine, the width of the boards' reach past the pages (the
  // reader sets how wide each side of it is), the front board's going over with it. Closed, it's out of sight.
  for (const s of [1, -1]) for (const back of [false, true]) {
    const z = back ? -(zi - 0.0006) : zi - 0.0006, y0 = s * py1, y1 = s * top, x1 = xl + sq;
    const pts = [[xl, y1, z], [x1, y1, z], [x1, y0, z], [xl, y0, z]];
    quad('spineWindow', pts, [0, 0, back ? 1 : -1], pts.map(([x, y]) => [back ? 0.5 + 0.5 * (x - xl) / sq : 0.5 - 0.5 * (x - xl) / sq, (y1 - y) / (y1 - y0)]));
  }
  return groups;
}

/* Writing the model as a binary glTF file (.glb), with the photos inside it as JPEGs. */
async function canvasJpeg(cv, quality){
  const blob = await new Promise(r => cv.toBlob(r, 'image/jpeg', quality));
  return new Uint8Array(await blob.arrayBuffer());
}
function writeGlb(groups, materials, images){
  const json = {asset:{version:'2.0', generator:'Journal book models'}, scene:0, scenes:[{nodes:[0]}], nodes:[{mesh:0, name:'Book'}],
    meshes:[{primitives:[]}], accessors:[], bufferViews:[], buffers:[{byteLength:0}], materials:[], textures:[], images:[],
    samplers:[{magFilter:9729, minFilter:9987, wrapS:10497, wrapT:10497}]};
  const chunks = []; let length = 0;
  const addView = (bytes, target) => {
    const pad = (4 - length % 4) % 4; if (pad) { chunks.push(new Uint8Array(pad)); length += pad; }
    json.bufferViews.push(Object.assign({buffer:0, byteOffset:length, byteLength:bytes.byteLength}, target ? {target} : {}));
    chunks.push(new Uint8Array(bytes.buffer, bytes.byteOffset, bytes.byteLength)); length += bytes.byteLength;
    return json.bufferViews.length - 1;
  };
  const addAccessor = (arr, type, comp, target, minmax) => {
    const n = {VEC2:2, VEC3:3, SCALAR:1}[type], acc = {bufferView:addView(arr, target), componentType:comp, count:arr.length / n, type};
    if (minmax) {
      acc.min = [Infinity, Infinity, Infinity]; acc.max = [-Infinity, -Infinity, -Infinity];
      for (let i = 0; i < arr.length; i++) { const j = i % 3; acc.min[j] = Math.min(acc.min[j], arr[i]); acc.max[j] = Math.max(acc.max[j], arr[i]); }
    }
    json.accessors.push(acc); return json.accessors.length - 1;
  };
  const imageIndex = new Map();
  for (const [key, bytes] of images) {
    json.images.push({bufferView:addView(bytes), mimeType:'image/jpeg'});
    json.textures.push({sampler:0, source:json.images.length - 1});
    imageIndex.set(key, json.textures.length - 1);
  }
  const matIndex = new Map();
  for (const [name, m] of Object.entries(materials)) {
    if (!groups.has(name)) continue;
    const pbr = {metallicFactor:0, roughnessFactor:0.85};
    if (m.tex) pbr.baseColorTexture = {index:imageIndex.get(m.tex)}; else pbr.baseColorFactor = toLinear(m.colour);
    json.materials.push(Object.assign({name, pbrMetallicRoughness:pbr}, m.extras ? {extras:m.extras} : {})); matIndex.set(name, json.materials.length - 1);
  }
  for (const [name, o] of groups) {
    if (!matIndex.has(name)) continue;
    json.meshes[0].primitives.push({material:matIndex.get(name), attributes:{
      POSITION:addAccessor(new Float32Array(o.pos), 'VEC3', 5126, 34962, true),
      NORMAL:addAccessor(new Float32Array(o.nrm), 'VEC3', 5126, 34962),
      TEXCOORD_0:addAccessor(new Float32Array(o.uv), 'VEC2', 5126, 34962)},
      indices:addAccessor(new Uint32Array(o.idx), 'SCALAR', 5125, 34963)});
  }
  const binPad = (4 - length % 4) % 4; if (binPad) { chunks.push(new Uint8Array(binPad)); length += binPad; }
  json.buffers[0].byteLength = length;
  let js = new TextEncoder().encode(JSON.stringify(json));
  const jsPad = (4 - js.length % 4) % 4;
  if (jsPad) { const t = new Uint8Array(js.length + jsPad).fill(0x20); t.set(js); js = t; }
  const total = 12 + 8 + js.length + 8 + length, out = new Uint8Array(total), dv = new DataView(out.buffer);
  dv.setUint32(0, 0x46546C67, true); dv.setUint32(4, 2, true); dv.setUint32(8, total, true);
  dv.setUint32(12, js.length, true); dv.setUint32(16, 0x4E4F534A, true); out.set(js, 20);
  let at = 20 + js.length;
  dv.setUint32(at, length, true); dv.setUint32(at + 4, 0x004E4942, true); at += 8;
  for (const c of chunks) { out.set(c, at); at += c.length; }
  return out.buffer;
}
// The whole book as a .glb, its photos straightened at up to maxSide pixels.
// A photo turned round left to right: the inside of one board, used for the other when only one was photographed.
function mirrored(cv){
  const m = document.createElement('canvas'); m.width = cv.width; m.height = cv.height;
  const x = m.getContext('2d'); x.translate(cv.width, 0); x.scale(-1, 1); x.drawImage(cv, 0, 0);
  return m;
}
async function buildBookGlb(maxSide){
  const f = book.faces, img = {};
  for (const k of BOOK_FACES) if (f[k].data) img[k] = straighten(f[k], k === 'headcap' || k === 'tailcap' ? Math.min(maxSide, 1024) : maxSide);
  const board = img.front ? edgeColour(img.front) : [110, 40, 40];
  // The back cover can be the front's photo, flipped across the spine (as a binding decorated alike on both sides
  // is), or just as it is.
  if (book.backFrom !== 'own' && img.front) img.back = book.backFrom === 'mirror' ? mirrored(img.front) : img.front;
  // The inside of the back board is the front's, flipped across the spine or just as it is. As the boards lie
  // open, the front's has its spine on the right, the back's on the left.
  const flip = book.insideBack !== 'same', under = img.inside;
  // The endpapers: a photo of endpaper, or one made up; pasted inside the boards over the turned-in covering (the
  // photo of the inside of a board, if there is one, or the cover's colour), and the free leaf at each end.
  if (book.ends === 'none' || (book.ends === 'photo' && !img.endsheet)) delete img.endsheet;
  else {
    // A made-up sheet is folded: its left half pasted down, its right half the free leaf, the pattern running on
    // from one to the other across the fold. A photo does for both.
    let paste = img.endsheet;
    if (book.ends !== 'photo') { const whole = endTexture(book.ends, book.dims.w / book.dims.h); paste = sheetHalf(whole, 0); img.endsheet = sheetHalf(whole, 1); }
    const aspect = book.dims.w / book.dims.h, turnIn = under || board.map(v => v * 0.9);
    // (level with the pages at head and tail, as far in as the page block is from the boards' edges)
    const inset = Math.min(0.016, aspect * 0.04);
    img.inside = pastedown(paste, turnIn, aspect, false, inset);
    // Just as it is, the endpaper and the turned-in covering aren't flipped, but it's still pasted into the joint.
    if (!flip) img.insideBack = pastedown(paste, turnIn, aspect, true, inset);
  }
  if (img.inside && !img.insideBack) img.insideBack = flip ? mirrored(img.inside) : img.inside;
  const dark = c => c.map(v => v * 0.82);
  const capColour = dark(img.spine ? edgeColour(img.spine) : board), endpaper = [232, 224, 204];
  const materials = {
    front:img.front ? {tex:'front'} : {colour:board},
    back:img.back ? {tex:'back'} : {colour:board},
    spine:img.spine ? {tex:'spine'} : {colour:board},
    headcap:img.headcap ? {tex:'headcap'} : {colour:capColour},
    tailcap:img.tailcap ? {tex:'tailcap'} : img.headcap ? {tex:'headcap'} : {colour:capColour},
    capSide:{colour:dark(img.headcap || img.tailcap ? edgeColour(img.headcap || img.tailcap) : capColour)},
    headWall:{colour:dark(dark(img.spine ? edgeColour(img.spine) : board))},
    board:{colour:dark(board)},
    endpaper:{colour:endpaper},
    insideFront:img.inside ? {tex:'inside'} : {colour:endpaper},
    insideBack:img.inside ? {tex:'insideBack'} : {colour:endpaper},
    rim:img.boardEdges ? {tex:'boardEdges'} : {colour:dark(board)},
    edges:{tex:book.edges === 'photo' && img.pages ? 'pages' : book.edges === 'gilt' ? 'gilt' : book.edges === 'red' ? 'red' : 'paper'},
    giltEdge:{tex:'gilt'},
    endsheet:{tex:'endsheet'},
    headband:{tex:'headband', extras:{colours:BOOK_HEADBANDS[book.headband] || null}},
    spineWindow:{tex:'spineWindow'},
    leaf:book.leaf === 'photo' && img.leaf ? {tex:'leaf'} : book.leaf === 'white' || book.leaf === 'photo' ? {colour:[251, 250, 246]} : {tex:'leaf-' + book.leaf}};
  const groups = bookGeometry({h:book.dims.h, w:book.dims.w, t:book.dims.t, round:book.round, edges:img.pages && book.edges === 'photo' ? 'photo' : book.edges,
    inside:!!img.inside, bands:book.bands,
    rim:img.boardEdges ? {aspect:img.boardEdges.width / img.boardEdges.height, scale:book.rimScale} : null,
    head:!!img.headcap, tail:!!(img.tailcap || img.headcap), leaf:true, ends:!!img.endsheet, headband:!!BOOK_HEADBANDS[book.headband]});
  // Only the pictures the model's parts actually use go into the file.
  const used = new Set(Object.entries(materials).filter(([name]) => groups.has(name)).map(([, m]) => m.tex).filter(Boolean)), images = [];
  for (const [k, cv] of Object.entries(img)) if (used.has(k)) images.push([k, await canvasJpeg(cv, 0.9)]);
  for (const k of ['paper', 'gilt', 'red']) if (used.has(k)) images.push([k, await canvasJpeg(edgeTexture(k), 0.85)]);
  if (used.has('headband')) images.push(['headband', await canvasJpeg(headbandTexture(BOOK_HEADBANDS[book.headband]), 0.9)]);
  if (used.has('spineWindow')) images.push(['spineWindow', await canvasJpeg(spineWindowTexture(img.spine ? edgeColour(img.spine) : board, BOOK_HEADBANDS[book.headband] || null), 0.92)]);
  for (const k of BOOK_LEAVES) if (used.has('leaf-' + k)) images.push(['leaf-' + k, await canvasJpeg(leafTexture(k, book.dims.w / book.dims.h), 0.88)]);
  return writeGlb(groups, materials, images);
}

/* The dialog */
// With a draft ({code, data}), everything is put back as it was when the draft was saved.
async function openBookMaker(picture, draft){
  const e = entries.get(currentId); if (!e) return;
  const d = draft ? draft.data || {} : null;
  book.entry = currentId; book.draft = draft ? draft.code : null; book.face = 'front';
  book.dims = {h:20, w:14, t:3, manual:false}; book.edges = 'plain'; book.leaf = 'white'; book.ends = 'plain'; book.headband = 'red'; book.backFrom = 'own'; book.insideBack = 'mirror'; book.round = true; book.bands = []; book.rimScale = 1;
  for (const k of BOOK_FACES) book.faces[k] = emptyBookFace();
  if (d) {
    const dm = d.dims || {}, ok = v => typeof v === 'number' && v > 0;
    if (ok(dm.h) && ok(dm.w) && ok(dm.t)) book.dims = {h:dm.h, w:dm.w, t:dm.t, manual:!!dm.manual};
    if (['plain', 'gilt', 'giltTop', 'red', 'photo'].includes(d.edges)) book.edges = d.edges;
    if (BOOK_LEAVES.includes(d.leaf)) book.leaf = d.leaf;
    if (BOOK_ENDS.includes(d.ends)) book.ends = d.ends;
    if (d.headband === 'none' || BOOK_HEADBANDS[d.headband]) book.headband = d.headband;
    if (['own', 'mirror', 'same'].includes(d.backFrom)) book.backFrom = d.backFrom;
    if (['mirror', 'same'].includes(d.insideBack)) book.insideBack = d.insideBack;
    book.round = d.round !== false;
    if (Array.isArray(d.bands) && d.bands.length <= 5 && d.bands.every(v => typeof v === 'number' && v > 0 && v < 1))
      book.bands = d.bands.slice();
    // drafts saved while there were two insides: the front's photo is the one
    if (d.faces && !d.faces.inside) d.faces.inside = d.faces.insideFront || d.faces.insideBack;
    // and while each board edge had its own photo: the first there was does for them all
    if (d.faces && !d.faces.boardEdges) d.faces.boardEdges = d.faces.edgeFore || d.faces.edgeHead || d.faces.edgeTail;
    if (typeof d.rimScale === 'number' && d.rimScale >= 0.25 && d.rimScale <= 4) book.rimScale = d.rimScale;
    if (BOOK_FACES.includes(d.face)) book.face = d.face;
  }
  $('bookEdges').value = book.edges === 'photo' ? 'plain' : book.edges; $('bookSpine').value = book.round ? 'round' : 'flat';
  $('bookBands').value = String(book.bands.length); showBookBands(); $('bookEdgesPhoto').disabled = true;
  $('bookLeaf').value = book.leaf === 'photo' ? 'white' : book.leaf; $('bookLeafPhoto').disabled = true;
  $('bookEnds').value = book.ends === 'photo' ? 'plain' : book.ends; $('bookEndsPhoto').disabled = true;
  $('bookBackFrom').value = book.backFrom; $('bookInsideBack').value = book.insideBack; $('bookHeadband').value = book.headband;
  $('bookDiscard').hidden = !book.draft; disarm($('bookDiscard'), 'Discard draft');
  M3.states.delete('book-preview');
  $('bookDialog').showModal();
  if (!book.view) book.view = m3PreviewView($('bookPreview'), 'book-preview', $('bookPreviewNote'));
  cancelAnimationFrame(book.openRaf); book.view.open = 0; $('bookOpen').setAttribute('aria-pressed', 'false'); $('bookOpen').textContent = 'Show open';
  showBookFace();
  const saved = d && d.faces && typeof d.faces === 'object' ? BOOK_FACES.filter(k => d.faces[k] && IMG_NAME.test(d.faces[k].pic || '')) : [];
  if (saved.length) {
    await Promise.all(saved.map(k => setBookPicture(k, d.faces[k].pic, d.faces[k])));
    if (book.edges === 'photo' && !book.faces.pages.data) book.edges = 'plain';
    if (book.leaf === 'photo' && !book.faces.leaf.data) book.leaf = 'white';
    if (book.ends === 'photo' && !book.faces.endsheet.data) book.ends = 'plain';
    $('bookEdges').value = book.edges; $('bookLeaf').value = book.leaf; $('bookEnds').value = book.ends;
  } else if (picture) await setBookPicture('front', picture);
  else { showBookDims(); showBookPreview(); }
}
async function openBookDraft(code){
  try {
    const r = await fetch('/api/book-drafts/' + code, {headers:H});
    if (!r.ok) throw new Error();
    await openBookMaker(null, {code, data:await r.json()});
  } catch (err) { setStatus("Couldn't open the draft. Check that the journal server is still running.", true); }
}
// A picture from the entry for one side of the book. The corners start a little in from the photo's edges,
// or, from a draft, where they were left.
async function setBookPicture(face, picture, saved){
  const f = book.faces[face];
  Object.assign(f, emptyBookFace(), {pic:picture});
  if (face === 'pages' && !saved) pagesPhoto(!!picture);
  if (face === 'leaf' && !saved) leafPhoto(!!picture);
  if (face === 'endsheet' && !saved) endsPhoto(!!picture);
  showBookFace();
  if (!picture) { bookChanged(); return; }
  try {
    const im = new Image(); im.src = '/images/' + picture; await im.decode();
    const k = Math.min(1, 3000 / Math.max(im.naturalWidth, im.naturalHeight));
    const cv = document.createElement('canvas'); cv.width = Math.round(im.naturalWidth * k); cv.height = Math.round(im.naturalHeight * k);
    const x = cv.getContext('2d', {willReadFrequently:true}); x.drawImage(im, 0, 0, cv.width, cv.height);
    if (f.pic !== picture) return;   // another picture was chosen meanwhile
    f.data = x.getImageData(0, 0, cv.width, cv.height); f.source = cv;
    const pt = p => Array.isArray(p) && p.length === 2 && p.every(v => typeof v === 'number' && isFinite(v));
    if (saved && Array.isArray(saved.quad) && saved.quad.length === 4 && saved.quad.every(pt)) {
      // the corners were kept in the photo's own pixels; if it's been read at another size, they're scaled to it
      const sx = saved.w > 0 ? cv.width / saved.w : 1, sy = saved.h > 0 ? cv.height / saved.h : 1, sc = ([a, b]) => [a * sx, b * sy];
      f.quad = saved.quad.map(sc); f.rot = ((saved.rot | 0) % 4 + 4) % 4;
      f.extra = [0, 1, 2, 3].map(i => Array.isArray(saved.extra) && Array.isArray(saved.extra[i]) ? saved.extra[i].filter(pt).map(sc) : []);
    } else {
      const mx = cv.width * 0.08, my = cv.height * 0.08;
      f.quad = [[mx, my], [cv.width - mx, my], [cv.width - mx, cv.height - my], [mx, cv.height - my]];
    }
    if (face === 'pages') $('bookEdgesPhoto').disabled = false;
    if (face === 'leaf') $('bookLeafPhoto').disabled = false;
    if (face === 'endsheet') $('bookEndsPhoto').disabled = false;
  } catch (err) { f.pic = null; setStatus("That picture couldn't be read.", true); }
  showBookFace(); bookChanged();
}
// A photo of the page edges goes on all three of them (head, fore-edge and tail) in place of the plain paper.
function pagesPhoto(on){
  $('bookEdgesPhoto').disabled = !on;
  if (on) book.edges = 'photo'; else if (book.edges === 'photo') book.edges = 'plain';
  $('bookEdges').value = book.edges;
}
// A photo of a page's paper goes on the pages in place of the paper chosen under Paper.
function leafPhoto(on){
  $('bookLeafPhoto').disabled = !on;
  if (on) book.leaf = 'photo'; else if (book.leaf === 'photo') book.leaf = 'white';
  $('bookLeaf').value = book.leaf;
}
// A photo of endpaper goes on the endpapers in place of the pattern chosen under Endpapers.
function endsPhoto(on){
  $('bookEndsPhoto').disabled = !on;
  if (on) book.ends = 'photo'; else if (book.ends === 'photo') book.ends = 'plain';
  $('bookEnds').value = book.ends;
}
// What to choose for each side, when it has no photo yet, and what to do with the photo once it has.
const BOOK_NOTES = {
  front:'Choose a photo of the front cover from the pictures below.',
  pages:'Choose a photo of the page edges below, to put on the head, fore-edge and tail. Without one, they\u2019re as set under Page edges.',
  inside:'Choose a photo of the inside of a board, opened out, showing the covering turned in over its edges. It goes inside both boards, and the endpaper (as set under Endpapers) is pasted over it, leaving its edges showing round it; with Endpapers set to None, it\u2019s seen whole. Without one, the turn-ins are the colour of the cover.',
  endsheet:'Choose a photo of endpaper (marbled, patterned or plain): a sheet of it, or a stretch of it. It\u2019s pasted inside both boards, leaving the turned-in edges of the covering showing round it, and makes the free leaf at the start and the end of the book. Without one, it\u2019s as set under Endpapers.',
  leaf:'Choose a photo of a blank page (or any paper), to be the paper the book\u2019s pages are printed on as it\u2019s read: it\u2019s stretched over each page, under the print. Without one, the paper is as set under Paper.',
  boardEdges:'Choose a photo of the edge of a board (its narrow outer edge, where the gilt roll or the leather\u2019s edge is). A short stretch is enough: it\u2019s repeated along the head, fore-edge and tail of both boards. Without one, they\u2019re the colour of the cover.',
  headcap:'Choose a photo of the head of the spine, seen from above. Without one, it\u2019s the colour of the spine.',
  tailcap:'Choose a photo of the tail of the spine, seen from below. Without one, the headcap\u2019s photo is used (or the colour of the spine).'};
const BOOK_HINTS = {
  pages:'Drag the corners onto the edges of the pages, then Turn it until the lines of the pages run from side to side.',
  leaf:'Drag the corners onto the corners of the page (or round the stretch of paper to use), and Turn it until its top is marked Top. Whole photo uses all of it.',
  endsheet:'Drag the corners round the endpaper (or the stretch of it to use), and Turn it until its top is marked Top. Whole photo uses all of it.',
  inside:'Drag the corners onto the corners of the board, and Turn it until the top is marked Top: the spine should be on the right, as when the book lies open.',
  boardEdges:'Drag the corners tightly round a stretch of the edge (just its depth, nothing above or below), and Turn it until it runs from side to side, with the outside of the board marked Top.',
  headcap:'Drag the corners round the end of the spine, and Turn it until the outside of the spine is marked Top.',
  tailcap:'Drag the corners round the end of the spine, and Turn it until the outside of the spine is marked Top.'};
function showBookFace(){
  for (const b of document.querySelectorAll('#bookTabs .tab')) {
    const on = b.dataset.face === book.face, f = book.faces[b.dataset.face];
    b.setAttribute('aria-selected', String(on));
    b.textContent = BOOK_NAMES[b.dataset.face] + (!(f && f.pic) && b.dataset.face === 'front' ? ' (needed)' : '');
    b.classList.toggle('has', !!(f && f.pic));   // a dot marks the sides that have a photo
  }
  const f = bookFace(), e = entries.get(book.entry);
  $('bookCropNote').textContent = f.pic ? '' : BOOK_NOTES[book.face]
    || 'Choose a photo of the ' + book.face + ' below, or leave it without one: it will be the colour of the cover.';
  $('bookFaceHint').textContent = (BOOK_HINTS[book.face]
    || 'Drag the corners onto the book\u2019s corners, and Turn it until the top is marked Top. Drag a + to add a point where a side curves.')
    + ' Scroll to zoom in.';
  $('bookCropNote').hidden = !!f.pic;
  if (book.face === 'back' && book.backFrom !== 'own') {   // the back is the front's photo: said over whatever's here
    $('bookCropNote').textContent = 'The back cover is the front\u2019s photo, ' + (book.backFrom === 'mirror' ? 'mirrored across the spine' : 'just as it is')
      + ' (as set under Back cover). Choose Its own photo there to give it one of its own.';
    $('bookCropNote').hidden = false;
  }
  $('bookTurn').disabled = $('bookWhole').disabled = !f.data;
  $('bookNone').hidden = book.face === 'front'; $('bookNone').disabled = !f.pic;
  const pics = $('bookPics'); pics.replaceChildren();
  for (const name of (e ? e.images : [])) {
    const b = document.createElement('button'); b.type = 'button'; b.className = 'book-pic' + (name === f.pic ? ' on' : '');
    const im = document.createElement('img'); im.src = '/images/' + name; im.alt = e ? titleIn(e.body, name) || 'Picture' : 'Picture';
    b.title = im.alt; b.setAttribute('aria-pressed', String(name === f.pic));
    b.append(im); b.addEventListener('click', () => setBookPicture(book.face, name));
    pics.append(b);
  }
  if (!pics.childElementCount) { const p = document.createElement('p'); p.className = 'book-empty'; p.textContent = 'This entry has no pictures yet. Add photos of the book to it first.'; pics.append(p); }
  $('bookMake').disabled = !book.faces.front.data || book.busy;
  drawBookCrop();
}
// The photo with its outline: the part inside is what goes on the book.
function cropLayout(){
  const cv = $('bookCrop'), f = bookFace(), box = cv.parentElement;
  const W = box.clientWidth, H = box.clientHeight;
  if (!f.data) return {W, H, k:1, ox:0, oy:0};
  const k0 = Math.min((W - 40) / f.data.width, (H - 40) / f.data.height), z = f.zoom, k = k0 * z.s;
  return {W, H, k, k0, ox:(W - f.data.width * k) / 2 + z.px, oy:(H - f.data.height * k) / 2 + z.py};
}
/* Zooming into the photo, to put the corners exactly: the scroll wheel zooms in and out where the pointer is,
   and dragging the photo (anywhere but on the outline's points) moves it about. Fit, or a double-click beside
   the outline, shows the whole photo again. */
function zoomBookCrop(s, mx, my){
  const f = bookFace(); if (!f.data) return;
  const L = cropLayout(), z = f.zoom;
  s = Math.max(1, Math.min(16, s));
  const ix = (mx - L.ox) / L.k, iy = (my - L.oy) / L.k, k = L.k0 * s;   // the point under the pointer stays put
  z.s = s; z.px = mx - ix * k - (L.W - f.data.width * k) / 2; z.py = my - iy * k - (L.H - f.data.height * k) / 2;
  clampBookCrop();
}
// The photo is kept at least half on screen, and centred again once it's back to its whole size.
function clampBookCrop(){
  const f = bookFace(); if (!f.data) return;
  const z = f.zoom;
  if (z.s <= 1.0001) { z.s = 1; z.px = z.py = 0; }
  else {
    const L = cropLayout(), w = f.data.width * L.k, h = f.data.height * L.k, bx = (L.W - w) / 2, by = (L.H - h) / 2;
    z.px = Math.max(L.W / 2 - w, Math.min(L.W / 2, bx + z.px)) - bx;
    z.py = Math.max(L.H / 2 - h, Math.min(L.H / 2, by + z.py)) - by;
  }
  drawBookCrop();
}
// Side i as a chain of points: its corner, the points added along it, and the next corner.
const sideChain = (f, i) => [f.quad[i], ...f.extra[i], f.quad[(i + 1) % 4]];
// Side i (in the photo's own order) drawn as the curve that will be followed, from its corner to the next.
function sideCurve(f, i, o = outlineOf(f)){
  const k = (i - f.rot + 4) % 4, rev = k >= 2, pts = [];   // bottom and left run the other way round
  for (let n = 0; n <= 32; n++) pts.push(outlinePoint(o, k, rev ? 1 - n / 32 : n / 32));
  return pts;
}
// Everything that can be dragged, where it is on screen: the corners, the points added along the sides,
// and a small + halfway along each stretch of side, which becomes a new point when dragged.
function cropHandles(f, L){
  const at = ([a, b]) => [L.ox + a * L.k, L.oy + b * L.k], hs = [];
  for (let i = 0; i < 4; i++) {
    hs.push({kind:'corner', i, p:at(f.quad[i])});
    f.extra[i].forEach((pt, j) => hs.push({kind:'point', i, j, p:at(pt)}));
  }
  const o = outlineOf(f);
  for (let i = 0; i < 4; i++) {
    // halfway along each stretch of the curve, so a new point lands on it and changes nothing until moved
    const c = sideChain(f, i), k = (i - f.rot + 4) % 4, by = k % 2 ? 1 : 0;
    for (let j = 0; j < c.length - 1; j++) {
      const t = (o.back(c[j])[by] + o.back(c[j + 1])[by]) / 2, mid = outlinePoint(o, k, t);
      hs.push({kind:'add', i, j, img:mid, p:at(mid)});
    }
  }
  return hs;
}
// A band across the straightened spine, a fraction v of the way down, as a line through the photo: the same
// mapping as straighten() uses, so it's exactly where the band will go on the model.
function bandLine(o, v){
  const pts = [];
  for (let n = 0; n <= 24; n++) {
    const u0 = n / 24, u = (1 - u0) * o.left(v) + u0 * o.right(v), w = (1 - v) * o.top(u0) + v * o.bottom(u0);
    pts.push(mapQuad(o.m, u, w));
  }
  return pts;
}
// The bands are shown on the spine's photo, each with a handle in its middle to drag it by.
const bandsOnPhoto = () => book.face === 'spine' && book.bands.length > 0;
const bandsMovable = bandsOnPhoto;
function cropHit(f, L, mx, my){
  if (bandsMovable()) {   // a band's handle comes first: it lies inside the outline, away from its points
    const o = outlineOf(f);
    for (let i = 0; i < book.bands.length; i++) {
      const line = bandLine(o, book.bands[i]), mid = line[12], p = [L.ox + mid[0] * L.k, L.oy + mid[1] * L.k];
      if (Math.hypot(p[0] - mx, p[1] - my) < 13) return {kind:'band', i};
    }
  }
  let best = null, dist = Infinity;
  for (const h of cropHandles(f, L)) {
    const d = Math.hypot(h.p[0] - mx, h.p[1] - my), reach = h.kind === 'add' ? 10 : 16;
    if (d < reach && (d < dist || (best && best.kind === 'add' && h.kind !== 'add'))) { best = h; dist = d; }
  }
  return best;
}
function drawBookCrop(){
  const cv = $('bookCrop'), f = bookFace(), L = cropLayout(), dpr = window.devicePixelRatio || 1;
  cv.width = Math.round(L.W * dpr); cv.height = Math.round(L.H * dpr);
  const x = cv.getContext('2d'); x.setTransform(dpr, 0, 0, dpr, 0, 0); x.clearRect(0, 0, L.W, L.H);
  $('bookStraight').disabled = !f.data || !f.extra.some(e => e.length);   // disabled rather than hidden, so nothing moves while dragging
  $('bookFit').disabled = !f.data || f.zoom.s === 1;
  if (!f.data) return;
  x.drawImage(f.source, L.ox, L.oy, f.data.width * L.k, f.data.height * L.k);
  const at = ([a, b]) => [L.ox + a * L.k, L.oy + b * L.k];
  const o = outlineOf(f), outline = [0, 1, 2, 3].flatMap(i => sideCurve(f, i, o).slice(0, -1)).map(at);
  const path = () => { x.beginPath(); x.moveTo(...outline[0]); for (const p of outline.slice(1)) x.lineTo(...p); x.closePath(); };
  // Shade everything outside the outline.
  x.save(); x.fillStyle = 'rgba(0,0,0,.45)'; x.beginPath(); x.rect(0, 0, L.W, L.H);
  x.moveTo(...outline[0]); for (const p of outline.slice(1).reverse()) x.lineTo(...p); x.closePath(); x.fill('evenodd'); x.restore();
  const accent = getComputedStyle(document.documentElement).getPropertyValue('--accent').trim() || '#7A2E3A', drag0 = book.drag;
  x.strokeStyle = '#fff'; x.lineWidth = 1.5; path(); x.stroke();
  // The side that will be the top is marked, so a turn shows which way up it is.
  const topSide = sideCurve(f, f.rot, o).map(at);
  x.lineCap = 'round'; x.lineJoin = 'round';
  for (const [colour, width] of [['#fff', 9], [accent, 5]]) {
    x.strokeStyle = colour; x.lineWidth = width; x.beginPath(); x.moveTo(...topSide[0]); for (const p of topSide.slice(1)) x.lineTo(...p); x.stroke();
  }
  // and labelled "Top", just outside it
  const t0 = topSide[0], t1 = topSide[topSide.length - 1], mx = (t0[0] + t1[0]) / 2, my = (t0[1] + t1[1]) / 2;
  const cx = outline.reduce((a, p) => a + p[0], 0) / outline.length, cy = outline.reduce((a, p) => a + p[1], 0) / outline.length;
  const dl = Math.hypot(mx - cx, my - cy) || 1, lx = mx + (mx - cx) / dl * 20, ly = my + (my - cy) / dl * 20;
  x.font = 'italic 600 14px Spectral, Georgia, serif'; x.textAlign = 'center'; x.textBaseline = 'middle';
  const tw = x.measureText('Top').width + 14;
  x.fillStyle = '#fff'; x.beginPath(); x.roundRect(lx - tw / 2, ly - 11, tw, 22, 11); x.fill();
  x.fillStyle = accent; x.fillText('Top', lx, ly);
  if (bandsOnPhoto()) {
    for (let i = 0; i < book.bands.length; i++) {
      const line = bandLine(o, book.bands[i]).map(at), mid = line[12], on = drag0 && drag0.kind === 'band' && drag0.i === i;
      x.setLineDash([7, 5]);
      for (const [colour, width] of [['rgba(255,255,255,.9)', 4], [accent, 2]]) {
        x.strokeStyle = colour; x.lineWidth = width; x.beginPath(); x.moveTo(...line[0]); for (const p of line.slice(1)) x.lineTo(...p); x.stroke();
      }
      x.setLineDash([]);
      if (!bandsMovable()) continue;
      x.beginPath(); x.arc(mid[0], mid[1], 7, 0, Math.PI * 2); x.fillStyle = on ? accent : '#fff'; x.fill();
      x.strokeStyle = accent; x.lineWidth = 2; x.stroke();
    }
  }
  const drag = book.drag;
  for (const h of cropHandles(f, L)) {
    const on = drag && drag.kind === h.kind && drag.i === h.i && drag.j === h.j;
    x.beginPath();
    if (h.kind === 'add') {   // a small + to pull out into a new point
      x.arc(h.p[0], h.p[1], 5.5, 0, Math.PI * 2); x.fillStyle = 'rgba(255,255,255,.85)'; x.fill();
      x.strokeStyle = accent; x.lineWidth = 1.2; x.stroke();
      x.beginPath(); x.moveTo(h.p[0] - 3, h.p[1]); x.lineTo(h.p[0] + 3, h.p[1]); x.moveTo(h.p[0], h.p[1] - 3); x.lineTo(h.p[0], h.p[1] + 3); x.stroke();
      continue;
    }
    x.arc(h.p[0], h.p[1], h.kind === 'corner' ? 8 : 6.5, 0, Math.PI * 2);
    x.fillStyle = on ? accent : h.kind === 'corner' ? '#fff' : '#f3e7c9'; x.fill();
    x.strokeStyle = accent; x.lineWidth = 2; x.stroke();
  }
}
const cropPoint = (ev, L, f) => {
  const r = $('bookCrop').getBoundingClientRect();
  return [Math.max(0, Math.min(f.data.width, (ev.clientX - r.left - L.ox) / L.k)), Math.max(0, Math.min(f.data.height, (ev.clientY - r.top - L.oy) / L.k))];
};
$('bookCrop').addEventListener('pointerdown', ev => {
  const f = bookFace(); if (!f.data || ev.button !== 0) return;
  const r = $('bookCrop').getBoundingClientRect(), L = cropLayout();
  const h = cropHit(f, L, ev.clientX - r.left, ev.clientY - r.top);
  if (!h) {   // dragging the photo itself moves it about, when zoomed in
    if (f.zoom.s === 1) return;
    ev.preventDefault(); $('bookCrop').setPointerCapture(ev.pointerId);
    book.drag = {kind:'pan', id:ev.pointerId, x:ev.clientX, y:ev.clientY}; $('bookCrop').style.cursor = 'grabbing';
    return;
  }
  ev.preventDefault(); $('bookCrop').setPointerCapture(ev.pointerId);
  if (h.kind === 'band') book.drag = {kind:'band', i:h.i, id:ev.pointerId};
  else if (h.kind === 'add') { f.extra[h.i].splice(h.j, 0, h.img); book.drag = {kind:'point', i:h.i, j:h.j, id:ev.pointerId}; bookChanged(); }
  else book.drag = {kind:h.kind, i:h.i, j:h.j, id:ev.pointerId};
  drawBookCrop();
});
$('bookCrop').addEventListener('pointermove', ev => {
  const f = bookFace(), r = $('bookCrop').getBoundingClientRect(), L = cropLayout();
  if (!book.drag) {   // the pointer shows what's under it
    const h = f.data && cropHit(f, L, ev.clientX - r.left, ev.clientY - r.top);
    $('bookCrop').style.cursor = !h ? (f.data && f.zoom.s > 1 ? 'grab' : 'default') : h.kind === 'add' ? 'copy' : 'move';
    $('bookCrop').title = h && h.kind === 'point' ? 'Double-click to take this point away' : h && h.kind === 'add' ? 'Drag to add a point here'
      : h && h.kind === 'band' ? 'Drag to move this band along the spine' : '';
    return;
  }
  if (ev.pointerId !== book.drag.id) return;
  if (book.drag.kind === 'pan') {
    f.zoom.px += ev.clientX - book.drag.x; f.zoom.py += ev.clientY - book.drag.y;
    book.drag.x = ev.clientX; book.drag.y = ev.clientY;
    clampBookCrop(); return;
  }
  const pt = cropPoint(ev, L, f), d = book.drag;
  if (d.kind === 'band') {   // how far down the straightened spine the pointer is
    book.bands[d.i] = Math.max(0.03, Math.min(0.97, outlineOf(f).back(pt)[1]));
    showBookBands(); drawBookCrop(); bookChanged(); return;
  }
  if (d.kind === 'corner') f.quad[d.i] = pt; else f.extra[d.i][d.j] = pt;
  drawBookCrop(); bookChanged();
});
const endBookDrag = () => {
  if (!book.drag) return;
  const pan = book.drag.kind === 'pan'; book.drag = null; $('bookCrop').style.cursor = '';
  drawBookCrop(); if (!pan) bookChanged();
};
$('bookCrop').addEventListener('pointerup', endBookDrag); $('bookCrop').addEventListener('pointercancel', endBookDrag);
// Double-clicking a point added along a side takes it away again.
$('bookCrop').addEventListener('dblclick', ev => {
  const f = bookFace(); if (!f.data) return;
  const r = $('bookCrop').getBoundingClientRect(), h = cropHit(f, cropLayout(), ev.clientX - r.left, ev.clientY - r.top);
  if (h && h.kind === 'point') { f.extra[h.i].splice(h.j, 1); drawBookCrop(); bookChanged(); }
  else if (!h && f.zoom.s > 1) { f.zoom.s = 1; clampBookCrop(); }   // beside the outline: the whole photo again
});
$('bookCrop').addEventListener('wheel', ev => {
  const f = bookFace(); if (!f.data) return;
  ev.preventDefault();
  const r = $('bookCrop').getBoundingClientRect(), dy = ev.deltaY * (ev.deltaMode === 1 ? 16 : ev.deltaMode === 2 ? 400 : 1);
  zoomBookCrop(f.zoom.s * Math.exp(-dy * 0.0025), ev.clientX - r.left, ev.clientY - r.top);
}, {passive:false});
$('bookFit').addEventListener('click', () => { const f = bookFace(); if (f.data) { f.zoom.s = 1; clampBookCrop(); } });
$('bookStraight').addEventListener('click', () => { const f = bookFace(); f.extra = [[], [], [], []]; drawBookCrop(); bookChanged(); });
new ResizeObserver(() => { if ($('bookDialog').open) clampBookCrop(); }).observe($('bookCrop').parentElement);
for (const b of document.querySelectorAll('#bookTabs .tab')) b.addEventListener('click', () => { book.face = b.dataset.face; showBookFace(); });
$('bookTurn').addEventListener('click', () => { const f = bookFace(); f.rot = (f.rot + 3) % 4;   // the left side becomes the top, as for a spine photographed with the book lying face up
  drawBookCrop(); bookChanged(); });
$('bookWhole').addEventListener('click', () => {
  const f = bookFace(); if (!f.data) return;
  const w = f.data.width, h = f.data.height;
  f.quad = [[0, 0], [w, 0], [w, h], [0, h]]; f.extra = [[], [], [], []];
  drawBookCrop(); bookChanged();
});
$('bookNone').addEventListener('click', () => setBookPicture(book.face, null));
// The size, as the photos suggest it unless it's been typed in. Only the proportions matter.
function bookDimsFromPhotos(){
  const f = book.faces; if (!f.front.data) return;
  const h = 20, w = h * trueAspect(turnedQuad(f.front), f.front.data.width, f.front.data.height);
  let t = h * 0.12;
  if (f.spine.data) t = h * trueAspect(turnedQuad(f.spine), f.spine.data.width, f.spine.data.height);
  Object.assign(book.dims, {h, w:Math.round(w * 10) / 10, t:Math.round(t * 10) / 10});
}
function showBookDims(){
  $('bookH').value = book.dims.h; $('bookW').value = book.dims.w; $('bookT').value = book.dims.t;
  showBookRim();
}
// A slider for each band, from the head (left) to the tail (right).
function showBookBands(){
  const box = $('bookBandPos'), n = book.bands.length, movable = n > 0;
  box.hidden = !movable;
  if (!movable) { box.replaceChildren(); return; }
  if (box.childElementCount !== n) {
    box.replaceChildren(...book.bands.map((_, i) => {
      const l = document.createElement('label'); l.textContent = n === 1 ? 'Band' : 'Band ' + (i + 1);
      const r = document.createElement('input'); r.type = 'range'; r.min = '3'; r.max = '97'; r.step = '0.5';
      r.title = 'Where the band is, from the head of the spine (left) to the tail (right)';
      r.addEventListener('input', () => { book.bands[i] = parseFloat(r.value) / 100; drawBookCrop(); bookChanged(); });
      l.append(r); return l;
    }));
  }
  [...box.querySelectorAll('input')].forEach((r, i) => { if (document.activeElement !== r) r.value = String(Math.round(book.bands[i] * 200) / 2); });
}
// How large the board edges' photo is repeated along the edges, shown once there is one.
function showBookRim(){
  $('bookRimBox').hidden = !book.faces.boardEdges.pic;
  $('bookRim').value = String(Math.round(book.rimScale * 100)); $('bookRimPct').textContent = Math.round(book.rimScale * 100) + '%';
}
$('bookRim').addEventListener('input', () => {
  book.rimScale = parseInt($('bookRim').value, 10) / 100; $('bookRimPct').textContent = $('bookRim').value + '%'; bookChanged();
});
$('bookBands').addEventListener('change', () => {
  book.bands = evenBands(parseInt($('bookBands').value, 10) || 0);
  showBookBands(); drawBookCrop(); bookChanged();
});
for (const id of ['bookH', 'bookW', 'bookT']) $(id).addEventListener('input', () => {
  const v = parseFloat($(id).value); if (!(v > 0)) return;
  book.dims[{bookH:'h', bookW:'w', bookT:'t'}[id]] = v; book.dims.manual = true; bookChanged();
});
$('bookFromPhotos').addEventListener('click', () => { book.dims.manual = false; bookChanged(); });
$('bookEdges').addEventListener('change', () => { book.edges = $('bookEdges').value; bookChanged(); });
$('bookLeaf').addEventListener('change', () => { book.leaf = $('bookLeaf').value; bookChanged(); });
$('bookEnds').addEventListener('change', () => { book.ends = $('bookEnds').value; bookChanged(); });
$('bookHeadband').addEventListener('change', () => { book.headband = $('bookHeadband').value; bookChanged(); });
$('bookBackFrom').addEventListener('change', () => { book.backFrom = $('bookBackFrom').value; showBookFace(); bookChanged(); });
$('bookInsideBack').addEventListener('change', () => { book.insideBack = $('bookInsideBack').value; bookChanged(); });
$('bookSpine').addEventListener('change', () => { book.round = $('bookSpine').value === 'round'; bookChanged(); });
// Anything changed: the preview follows a moment later.
function bookChanged(){
  if (!book.dims.manual) bookDimsFromPhotos();
  showBookDims();
  $('bookFromPhotos').hidden = !book.dims.manual;
  $('bookMake').disabled = !book.faces.front.data || book.busy;
  clearTimeout(book.timer); book.timer = setTimeout(showBookPreview, book.drag ? 120 : 60);
}
async function showBookPreview(){
  if (!book.faces.front.data) { m3SetPreview('book-preview', null); book.view.say('The book appears here once it has a front cover.'); return; }
  const seq = ++book.seq;
  const buf = await buildBookGlb(640);
  if (seq !== book.seq || !$('bookDialog').open) return;
  m3SetPreview('book-preview', await parseGlb(buf));
  book.view.say('');
}
// Show open: the preview's front board swings open (or shut again), to see the book as it lies open at its endpapers.
function bookOpenTo(to){
  const v = book.view; if (!v) return;
  $('bookOpen').setAttribute('aria-pressed', String(to > 0)); $('bookOpen').textContent = to > 0 ? 'Show closed' : 'Show open';
  cancelAnimationFrame(book.openRaf);
  const from = v.open || 0, t0 = performance.now(), ms = 700 * Math.abs(to - from);
  const step = now => {
    const u = ms ? Math.min(1, (now - t0) / ms) : 1;
    v.open = from + (to - from) * ease(u); m3Redraw('book-preview');
    if (u < 1) book.openRaf = requestAnimationFrame(step);
  };
  book.openRaf = requestAnimationFrame(step);
}
$('bookOpen').addEventListener('click', () => bookOpenTo($('bookOpen').getAttribute('aria-pressed') === 'true' ? 0 : 1));
$('bookCancel').addEventListener('click', () => $('bookDialog').close());
$('bookDialog').addEventListener('close', () => { clearTimeout(book.timer); book.seq++; m3SetPreview('book-preview', null); });
$('bookMake').addEventListener('click', async () => {
  const id = book.entry, e = entries.get(id); if (!e || !book.faces.front.data) return;
  book.busy = true; $('bookMake').disabled = true; $('bookMake').textContent = 'Making\u2026';
  try {
    const front = book.faces.front.pic, buf = await buildBookGlb(2048);
    const name = await store.uploadModel(new Blob([buf], {type:'model/gltf-binary'}));
    const side = shelfNames(e), at = side.indexOf(front), ref = 'model:' + name;
    const was = book.draft ? side.indexOf('draft:' + book.draft) : -1;   // a draft made into its model: the model takes its place
    if (was >= 0) side[was] = ref; else if (at < 0) side.push(ref); else side.splice(at + 1, 0, ref);
    e.side = side; markChanged(id);
    if (book.draft) fetch('/api/book-drafts/' + book.draft, {method:'DELETE', headers:H}).catch(() => {});
    $('bookDialog').close();
    if (id === currentId) {
      renderShelf();
      const el = [...$('shelfPics').children].find(x => x.dataset.name === ref);
      if (el) el.scrollIntoView({block:'nearest'});
    }
  } catch (err) {
    setStatus(err.message === 'size' ? 'The book model is too large to save.' : "Couldn't save the book model. Check that the journal server is still running.", true);
  } finally { book.busy = false; $('bookMake').textContent = 'Make model'; $('bookMake').disabled = !book.faces.front.data; }
});

/* Save draft: everything chosen so far (which photos, where their corners are, the size and the options) is kept
   in journal/book drafts, and the draft is shown on the right of the entry, next to its front cover, to be
   carried on with later. Saving a draft that's been opened again keeps it in the same place. */
function bookDraftData(){
  const faces = {};
  for (const k of BOOK_FACES) {
    const f = book.faces[k]; if (!f.pic) continue;
    faces[k] = f.data ? {pic:f.pic, quad:f.quad, rot:f.rot, extra:f.extra, w:f.data.width, h:f.data.height} : {pic:f.pic};
  }
  return {entry:book.entry, saved:Date.now(), face:book.face, faces, dims:Object.assign({}, book.dims), edges:book.edges, leaf:book.leaf, ends:book.ends, headband:book.headband, backFrom:book.backFrom, insideBack:book.insideBack, round:book.round, bands:book.bands.slice(), rimScale:book.rimScale};
}
$('bookDraft').addEventListener('click', async () => {
  const id = book.entry, e = entries.get(id), btn = $('bookDraft'); if (!e || book.busy) return;
  const code = book.draft || [...crypto.getRandomValues(new Uint8Array(8))].map(b => b.toString(16).padStart(2, '0')).join('');
  btn.disabled = true; btn.textContent = 'Saving\u2026';
  try {
    const r = await fetch('/api/book-drafts/' + code, {method:'PUT', headers:H, body:JSON.stringify(bookDraftData())});
    if (!r.ok) throw new Error();
    const ref = 'draft:' + code, side = shelfNames(e);
    if (!side.includes(ref)) {
      const at = side.indexOf(book.faces.front.pic);
      if (at < 0) side.push(ref); else side.splice(at + 1, 0, ref);
      e.side = side; markChanged(id);
    }
    book.draft = code; draftSaved.set(code, Date.now());
    $('bookDialog').close();
    if (id === currentId) {
      renderShelf();
      const el = [...$('shelfPics').children].find(x => x.dataset.name === ref);
      if (el) el.scrollIntoView({block:'nearest'});
    }
  } catch (err) {
    setStatus("Couldn't save the draft. Check that the journal server is still running.", true);
  } finally { btn.disabled = false; btn.textContent = 'Save draft'; }
});
$('bookDiscard').addEventListener('click', async () => {
  const btn = $('bookDiscard'), code = book.draft, id = book.entry;
  if (!code || !armed(btn, 'Discard draft', 'Discard? Can\u2019t be undone')) return;
  try {
    const r = await fetch('/api/book-drafts/' + code, {method:'DELETE', headers:H});
    if (!r.ok) throw new Error();
  } catch (err) { setStatus("Couldn't discard the draft. Check that the journal server is still running.", true); return; }
  const e = entries.get(id), ref = 'draft:' + code;
  if (e && e.side && e.side.includes(ref)) { e.side = e.side.filter(n => n !== ref); markChanged(id); }
  draftSaved.delete(code); book.draft = null;
  $('bookDialog').close();
  if (id === currentId) renderShelf();
});

/* Right-clicking a picture offers to make a book model with it as the front cover.
   (Shift and right-click still gives the browser's own menu.) */
const picMenu = document.createElement('div'); picMenu.className = 'pic-menu'; picMenu.hidden = true; picMenu.setAttribute('role', 'menu');
picMenu.innerHTML = '<button type="button" role="menuitem" data-act="book">Make book model</button><button type="button" role="menuitem" data-act="open">Open large</button>';
document.body.append(picMenu);
let picMenuFor = null;
const IMG_NAME = /^[a-f0-9]{32}\.(png|jpg|gif|webp|avif)$/;
function openPicMenu(ev, picture, open){
  ev.preventDefault();
  picMenuFor = {picture, open};
  picMenu.hidden = false;
  picMenu.style.left = Math.min(ev.clientX, innerWidth - picMenu.offsetWidth - 8) + 'px';
  picMenu.style.top = Math.min(ev.clientY, innerHeight - picMenu.offsetHeight - 8) + 'px';
  picMenu.querySelector('button').focus({preventScroll:true});
}
function closePicMenu(){ picMenu.hidden = true; picMenuFor = null; }
picMenu.addEventListener('click', ev => {
  const b = ev.target.closest('button'); if (!b || !picMenuFor) return;
  const {picture, open} = picMenuFor; closePicMenu();
  if (b.dataset.act === 'book') openBookMaker(picture); else open();
});
picMenu.addEventListener('keydown', ev => {
  const list = [...picMenu.querySelectorAll('button')], i = list.indexOf(document.activeElement);
  if (ev.key === 'Escape') { ev.preventDefault(); closePicMenu(); }
  else if (ev.key === 'ArrowDown' || ev.key === 'ArrowUp') { ev.preventDefault(); list[(i + (ev.key === 'ArrowDown' ? 1 : list.length - 1)) % list.length].focus(); }
});
window.addEventListener('pointerdown', ev => { if (!picMenu.hidden && !picMenu.contains(ev.target)) closePicMenu(); }, true);
window.addEventListener('blur', closePicMenu);
window.addEventListener('scroll', closePicMenu, true);
els.body.addEventListener('contextmenu', ev => {
  if (ev.shiftKey) return;
  const fig = ev.target.closest && ev.target.closest('.fig');
  if (!fig || fig.classList.contains('elink') || !IMG_NAME.test(fig.dataset.name || '')) return;
  openPicMenu(ev, fig.dataset.name, () => openViewer(fig));
});
$('shelfPics').addEventListener('contextmenu', ev => {
  if (ev.shiftKey) return;
  const item = ev.target.closest && ev.target.closest('.shelf-item');
  if (!item || item.classList.contains('drawing') || !IMG_NAME.test(item.dataset.name || '')) return;
  openPicMenu(ev, item.dataset.name, () => openShelfPicture(item));
});
$('viewerBook').addEventListener('click', () => {
  const fig = viewingFig; els.viewer.close();
  if (fig && els.body.contains(fig)) openBookMaker(fig.dataset.name);
});

init();
</script>
</body>
</html>
'''

if __name__ == "__main__":
    if "--save-picture" in sys.argv[1:]:
        save_picture_for_browser()
    elif "--log" in sys.argv[1:]:
        quick_log_window()
    elif "--screenshot" in sys.argv[1:]:
        screenshot_to_log()
    else:
        main()
