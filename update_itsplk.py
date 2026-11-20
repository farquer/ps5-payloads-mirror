"""Mirror the itsPLK catalog through gh-proxy and refresh its README table."""
import base64
import json
import re
import urllib.request
from pathlib import Path

from catalog import GH_PROXY, atomic_json, rewrite_github_values

UPSTREAM_V2 = "https://raw.githubusercontent.com/itsPLK/ps5-payloads-mirror/main/payloads_v2.json"
UPSTREAM_ICONS = "https://raw.githubusercontent.com/itsPLK/ps5-payloads-mirror/main/icons.json"
ALLOWED_URLS = {UPSTREAM_V2, UPSTREAM_ICONS}
OUTPUT = Path("payloads_itsplk_ghproxy.json")
ICON_DIR = Path("readme-icons-itsplk")
README = Path("README.md")
MAX_BYTES = 8_000_000
START = "<!-- ITSPLK_START -->"
END = "<!-- ITSPLK_END -->"
HEADING = "## itsPLK 国内加速"
SOURCE_LINE = "基于 https://github.com/itsPLK/ps5-payloads-mirror/blob/main/payloads_v2.json"


class RejectRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def fetch_json(url):
    if url not in ALLOWED_URLS:
        raise ValueError("Unexpected upstream URL")
    opener = urllib.request.build_opener(RejectRedirect)
    request = urllib.request.Request(url, headers={"User-Agent": "ps5-payloads-mirror"})
    with opener.open(request, timeout=30) as response:
        payload = response.read(MAX_BYTES + 1)
    if len(payload) > MAX_BYTES:
        raise ValueError("Upstream response is too large")
    return json.loads(payload.decode("utf-8"))


def parse_icon(data):
    if not isinstance(data, str) or "," not in data:
        return None
    header, encoded = data.split(",", 1)
    if not header.startswith("data:image/") or ";base64" not in header:
        return None
    kind = header.split("/")[-1].split(";")[0]
    ext = {"png": "png", "jpeg": "jpg", "svg+xml": "svg"}.get(kind)
    if not ext:
        return None
    try:
        raw = base64.b64decode(encoded, validate=True)
    except Exception:
        return None
    if not raw or len(raw) > 65536:
        return None
    return ext, raw


def cell(value, fallback):
    text = fallback if value is None or value == "" else str(value)
    return text.replace("\\", "\\\\").replace("|", "\\|").replace("\r", " ").replace("\n", " ").strip()


def icon_markup(item, icons):
    parsed = parse_icon(icons.get(item.get("icon_key")) if isinstance(icons, dict) else None)
    if not parsed:
        return "", None
    ext, raw = parsed
    filename = re.sub(r"[^A-Za-z0-9._-]", "_", item.get("name") or "icon") + "." + ext
    return f'<img src="readme-icons-itsplk/{filename}" width="36" alt="">', (filename, raw)


def render_table(payloads, icons):
    rows = [
        "| 图标 | 名称 | 版本 | 说明 | 支持固件 | 最近更新 | 源码 | 下载 |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    files = {}
    for item in payloads:
        markup, icon_file = icon_markup(item, icons)
        if icon_file:
            files[icon_file[0]] = icon_file[1]
        source = item.get("source") or "#"
        url = item.get("url") or "#"
        rows.append(
            "| {icon} | **{name}** | `{version}` | {description} | {firmware} | `{updated}` | [源码]({source}) | [下载]({url}) |".format(
                icon=markup,
                name=cell(item.get("name"), "Unknown"),
                version=cell(item.get("version"), "Unknown"),
                description=cell(item.get("description"), "未提供说明"),
                firmware=cell(item.get("firmware"), "未声明"),
                updated=cell(item.get("last_update"), "Unknown"),
                source=cell(source, "#"),
                url=cell(url, "#"),
            )
        )
    return "\n".join(rows), files


def update_readme_text(content, table):
    block = f"{START}\n{table}\n{END}"
    if START in content and END in content:
        pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
        return pattern.sub(block, content, count=1)
    section = f"{HEADING}\n\n{SOURCE_LINE}\n\n{block}\n"
    lines = content.splitlines(keepends=True)
    for index, line in enumerate(lines):
        if line.strip() == "### itsPLK 官方源":
            newline = "\n" if line.endswith("\n") else ""
            lines[index] = section.rstrip() + newline
            return "".join(lines)
    if "<!-- PAYLOADS_END -->" in content:
        return content.replace("<!-- PAYLOADS_END -->", "<!-- PAYLOADS_END -->\n\n---\n\n" + section, 1)
    return content.rstrip() + "\n\n" + section


def write_icons(files):
    ICON_DIR.mkdir(exist_ok=True)
    for name, raw in files.items():
        (ICON_DIR / name).write_bytes(raw)
    for path in ICON_DIR.iterdir():
        if path.is_file() and path.name not in files:
            path.unlink()


def main():
    catalog = fetch_json(UPSTREAM_V2)
    if not isinstance(catalog, dict) or not isinstance(catalog.get("payloads"), list):
        raise ValueError("Upstream catalog is not a payloads_v2 document")
    icons_doc = fetch_json(UPSTREAM_ICONS)
    icons = icons_doc.get("icons", {}) if isinstance(icons_doc, dict) else {}
    proxied = rewrite_github_values(catalog)
    atomic_json(OUTPUT, proxied)
    table, files = render_table(proxied["payloads"], icons)
    write_icons(files)
    content = README.read_text(encoding="utf-8") if README.exists() else ""
    README.write_text(update_readme_text(content, table), encoding="utf-8")


if __name__ == "__main__":
    main()
