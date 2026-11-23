"""Catalog and separately published, content-addressed icon data."""
import base64
import hashlib
import json
import os
import re
import tempfile
from pathlib import Path

FARQUER = Path("farquer")
CATALOG = FARQUER / "payloads.json"
CATALOG_GHPROXY = FARQUER / "payloads_ghproxy.json"
META = FARQUER / "meta.json"
ICONS = FARQUER / "icons.json"
PUBLIC_KEYS = (
    "name", "filename", "url", "source", "source_direct", "description",
    "last_update", "version", "category", "checksum", "icon_key",
)
META_KEYS = ("asset_pattern", "extract_file", "firmware")

def atomic_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=path.name + ".", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(value, stream, indent=2, ensure_ascii=False)
            stream.write("\n")
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)

def public_item(item):
    return {key: item[key] for key in PUBLIC_KEYS if key in item and item[key] is not None}

def rewrite_github_url(url):
    if not isinstance(url, str) or url.startswith("https://cdn.jsdelivr.net/gh/"):
        return url
    raw = re.match(r"https://raw\.githubusercontent\.com/([^/]+)/([^/]+)/([^/]+)/(.+)", url)
    if raw:
        owner, repo, ref, path = raw.groups()
        return f"https://cdn.jsdelivr.net/gh/{owner}/{repo}@{ref}/{path}"
    blob = re.match(r"https://github\.com/([^/]+)/([^/]+)/(?:blob|raw)/([^/]+)/(.+)", url)
    if blob:
        owner, repo, ref, path = blob.groups()
        return f"https://cdn.jsdelivr.net/gh/{owner}/{repo}@{ref}/{path}"
    return url

def catalog_name(path, default="PS5 Payloads"):
    path = Path(path)
    if path.exists():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            data = None
        if isinstance(data, dict):
            name = data.get("name")
            if isinstance(name, str) and name.strip():
                return name
    return default

def proxy_catalog(catalog):
    payloads = []
    for item in catalog.get("payloads", []):
        copied = dict(item)
        if isinstance(copied.get("url"), str):
            copied["url"] = rewrite_github_url(copied["url"])
        payloads.append(copied)
    return {
        "name": catalog.get("name", "PS5 Payloads"),
        "icons_url": catalog.get("icons_url", "icons.json"),
        "payloads": payloads,
    }

def load_catalog():
    if not CATALOG.exists():
        return []
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    payloads = data.get("payloads", []) if isinstance(data, dict) else data
    meta = json.loads(META.read_text(encoding="utf-8")) if META.exists() else {}
    merged = []
    for item in payloads:
        item = dict(item)
        item.update(meta.get(item.get("name"), {}))
        merged.append(item)
    return merged

def save_catalog(payloads):
    public = [public_item(item) for item in payloads]
    direct_name = catalog_name(CATALOG)
    proxy_name = catalog_name(CATALOG_GHPROXY, direct_name)
    wrapped = {
        "name": direct_name,
        "icons_url": "icons.json",
        "payloads": public,
    }
    atomic_json(CATALOG, wrapped)
    proxied = proxy_catalog(wrapped)
    proxied["name"] = proxy_name
    atomic_json(CATALOG_GHPROXY, proxied)
    meta = {}
    for item in payloads:
        extra = {key: item[key] for key in META_KEYS if item.get(key)}
        if extra and item.get("name"):
            meta[item["name"]] = extra
    atomic_json(META, meta)

def load_icons():
    if not ICONS.exists():
        return {}
    return json.loads(ICONS.read_text(encoding="utf-8"))["icons"]

def payload_icon(payload):
    return load_icons().get(payload.get("icon_key"))

def assign_icon(payload, data):
    if not data.startswith(("data:image/png;base64,", "data:image/jpeg;base64,", "data:image/svg+xml;base64,")) or len(data) > 12288:
        raise ValueError("Expected a bounded base64 PNG, JPEG or SVG icon")
    if not base64.b64decode(data.split(",", 1)[1], validate=True):
        raise ValueError("Empty icon data")
    key = hashlib.sha256(data.encode("ascii")).hexdigest()
    icons = load_icons()
    icons[key] = data
    atomic_json(ICONS, {"icons": icons})
    payload.pop("icon", None)
    payload["icon_key"] = key
