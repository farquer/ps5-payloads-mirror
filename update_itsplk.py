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
README_BRANCHES = ("main", "master")
README_NAMES = ("README.md", "readme.md", "README.MD", "Readme.md")
README_URL = re.compile(
    r"https://raw\.githubusercontent\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+/(?:main|master)/(?:README\.md|readme\.md|README\.MD|Readme\.md)"
)
# 各项目 README 首页的一句话说明。定时任务仍会重新读取 README 来更新固件。
HOMEPAGE_SUMMARY = {
    "ps5upload": "把游戏、应用和自制程序传到已越狱 PS5，断线后可以续传。",
    "ps5-dump-forge": "在 PS5、Windows、macOS 和 Linux 上转换并编辑游戏转储和多种封装格式。",
    "NeoEnabler": "让 PS4 游戏在 PS5 上以 PS4 Pro 模式和更高分辨率运行。",
    "PS5Save": "用 USB 自动备份已越狱 PS5 的游戏存档和文件。",
    "ps4mount": "不安装到主机，直接从 USB 在已越狱 PS5 上运行 PS4 假 PKG。",
    "garlic-savemgr": "在已越狱 PS5 上解密、加密和浏览存档，自带网页界面。",
    "ps5-web-file-manager": "带网页界面的 PS5 文件管理器，用来把游戏转储从 USB 拷到内置存储。",
    "LiveShell": "给 PS5 主界面使用可下载的动画壁纸。",
    "WebKit-Autoloader-Installer": "自动加载 WebKit 漏洞和 ELF payload。",
    "ftpsrv": "在已越狱 PS4 或 PS5 上运行的 FTP 服务器，端口 2121。",
    "ShadowMountPlus": "在已越狱 PS5 后台自动挂载镜像。",
    "CheatRunner": "在已越狱 PS5 上通过网页使用的金手指训练器。",
    "zftpd": "零拷贝 FTP 服务，同时提供主机 payload。",
    "WelcomeHubActivator": "在 PS5 上启用 Welcome Hub。",
    "elfldr": "给已越狱 PS5 用的 ELF 加载器，加载后在后台持续运行。",
    "pldmgr": "用网页管理、导入并自动加载 PS5 payload。",
    "ps5-exporter": "给已越狱 PS5 用的 Prometheus 导出器。",
    "onionHEN": "面向 PS5 的一体化 HEN 和工具箱。",
    "ps-patch-system": "应用补丁系统。",
    "PKG-Manager": "在 PS5 上浏览并安装 USB、光盘或 SMB 共享中的 PKG。",
    "ps5-app-dumper": "把 PS5 应用文件从 pfsmnt 导出到已连接的 USB 存储。",
    "ps5debug-NG": "运行在已越狱 PS5 用户态里的调试 payload。",
    "kstuff-lite": "kstuff 的精简版。",
    "ftpsrv-drakmor": "drakmor 维护的 ftpsrv，在已越狱 PS4 或 PS5 上提供 FTP。",
    "ps5-linux-loader": "利用 HV 漏洞，在 PS5 Phat、Slim 和 Pro 上启动 Linux。",
    "ps5-date-time-sync": "用公共 NTP 服务器恢复 PS5 的系统日期和时间。",
    "BFpilot": "在 PS5 上通过浏览器使用的轻量文件管理器。",
    "nanoDNS": "在 PS4 或 PS5 上运行的本地 DNS 代理。",
    "websrv": "在已越狱 PS5 上运行的简易网页服务器，端口 8080。",
    "shsrv": "在已越狱 PS5 上提供类 telnet 的简易 shell，端口 2323。",
    "klogsrv": "把已越狱主机的 /dev/klog 转发到端口 3232。",
    "Lapy-JB-Daemon": "模仿 etaHEN 按需越狱接口的独立守护进程。",
    "BackPork": "游戏启动时自动挂载系统库，用来旁加载。",
    "etaHEN": "一体化的 PS5 Homebrew Enabler。",
}


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


def direct_url(url):
    if isinstance(url, str) and url.startswith(GH_PROXY):
        return url[len(GH_PROXY):]
    return url


def github_repo(source):
    if not isinstance(source, str):
        return None
    if source.startswith(GH_PROXY):
        source = source[len(GH_PROXY):]
    match = re.match(r"https://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)(?:/|$)", source)
    if not match:
        return None
    return match.group(1), match.group(2)


def fetch_text(url):
    if not README_URL.fullmatch(url):
        raise ValueError("Unexpected README URL")
    opener = urllib.request.build_opener(RejectRedirect)
    request = urllib.request.Request(url, headers={"User-Agent": "ps5-payloads-mirror"})
    with opener.open(request, timeout=20) as response:
        payload = response.read(500_001)
    if len(payload) > 500_000:
        raise ValueError("README is too large")
    return payload.decode("utf-8", "replace")


def fetch_readme(owner, repo):
    for branch in README_BRANCHES:
        for name in README_NAMES:
            url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{name}"
            try:
                return fetch_text(url)
            except Exception:
                continue
    return ""


def clean_inline(text):
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = text.replace("&ndash;", "-").replace("&mdash;", "-")
    text = re.sub(r"[*_`>#]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def version_key(value):
    parts = [int(part) for part in value.split(".")]
    return tuple(parts + [0] * (3 - len(parts)))


def compress_versions(values):
    items = sorted(set(values), key=version_key)
    if not items:
        return ""
    ranges = []
    start = previous = items[0]
    for value in items[1:]:
        if version_key(value)[0] - version_key(previous)[0] > 1:
            ranges.append((start, previous))
            start = value
        previous = value
    ranges.append((start, previous))
    return "、".join(start if start == end else f"{start}–{end}" for start, end in ranges)


def versions_between(text, start, end):
    begin = text.find(start)
    if begin < 0:
        return []
    finish = text.find(end, begin + len(start))
    chunk = text[begin:finish if finish > begin else None]
    return re.findall(r"\*\*(\d+\.\d+(?:\.\d+)?)\*\*", chunk)


def firmware_from_readme(text):
    badge = re.search(
        r"PS5_firmware-(\d+\.\d+)_–_(\d+\.\d+)_supported(?:_[^\"']*?_([0-9._,&]+)_tested)?",
        text,
    )
    if badge:
        tested = "、".join(re.findall(r"\d+\.\d+", (badge.group(3) or "").replace("_", " ")))
        span = f"{badge.group(1)}–{badge.group(2)}"
        return f"{span}（{tested} 已测试）" if tested else span
    if "**PS5 Phat and Slim:**" in text and "**PS5 Pro:**" in text:
        phat = compress_versions(versions_between(text, "**PS5 Phat and Slim:**", "**PS5 Pro:**"))
        pro = compress_versions(versions_between(text, "**PS5 Pro:**", "Support for 1.xx"))
        if phat or pro:
            return f"Phat/Slim {phat}；Pro {pro}"
    plain = clean_inline(text)
    matched = re.search(r"Supports all Jailbroken PS5 firmwares running.*?[Kk]stuff-lite v([0-9.]+)\+", plain)
    if matched:
        return f"全部已越狱固件（需 kstuff-lite v{matched.group(1)}+）"
    matched = re.search(r"[Ss]upports firmwares?\s+(\d+\.\d+)\s*-\s*(\d+\.\d+)", plain)
    if matched:
        return f"{matched.group(1)}–{matched.group(2)}"
    matched = re.search(r"[Jj]ailbroken\s+(\d+\.\d+)\s*-\s*(\d+\.\d+)", plain)
    if matched:
        return f"{matched.group(1)}–{matched.group(2)}"
    matched = re.search(r"on firmware\s+(\d+\.\d+)\s+to\s+(\d+\.\d+)\s*\(tested on ([^)]+)\)", plain, re.I)
    if matched:
        tested = "、".join(re.findall(r"\d+\.\d+", matched.group(3)))
        span = f"{matched.group(1)}–{matched.group(2)}"
        return f"{span}（{tested} 已测试）" if tested else span
    matched = re.search(r"firmware\s+(\d+\.\d+)\s*[–-]\s*(\d+\.\d+)", plain, re.I)
    if matched:
        return f"{matched.group(1)}–{matched.group(2)}"
    if "Any firmware with fake PKG support" in text and "tested on 13.20" in text:
        return "5.50+（6.00 起常规注册，13.20 已测试）"
    if "Fully Verified" in text and "## Supported firmwares" in text:
        section = text[text.find("## Supported firmwares"):text.find("## Supported firmwares") + 2500]
        span = compress_versions(re.findall(r"\d+\.\d+(?:\.\d+)?", section))
        if span:
            return f"{span}（列出的点版本已完全验证）"
    matched = re.search(r"[Tt]ested on firmware\s+(\d+\.\d+)", plain)
    if matched:
        return f"{matched.group(1)} 已测试"
    matched = re.search(r"[Vv]erified on .{0,120}?firmware\s+(\d+\.\d+)", plain)
    if matched:
        return f"{matched.group(1)} 已验证"
    return "未声明"


def description_from_readme(text, fallback):
    stripped = re.sub(r"```.*?```", " ", text, flags=re.S)
    chunks = []
    for line in stripped.splitlines():
        raw = line.strip()
        if not raw or raw.startswith(("##", "#", "|", "---", "<!--", "- ", "* ", "!")):
            continue
        sentence = clean_inline(raw)
        if len(sentence) < 30 or re.search(r"https?://|Discord|Repository:|buy me a coffee|work in progress", sentence, re.I):
            continue
        chunks.append(sentence)
        if sum(len(item) for item in chunks) > 80:
            break
    blob = " ".join(chunks)
    matched = re.search(r".{30,200}?[.。]", blob)
    sentence = (matched.group(0) if matched else blob[:180]).strip(" -")
    if len(sentence) < 30 or sentence[:1].islower() or "[" in sentence:
        return fallback or "未提供说明"
    return sentence


def with_project_page(item, readme_text):
    updated = dict(item)
    summary = HOMEPAGE_SUMMARY.get(item.get("name"))
    if summary:
        updated["description"] = summary
    elif readme_text:
        updated["description"] = description_from_readme(readme_text, item.get("description"))
    updated["firmware"] = firmware_from_readme(readme_text) if readme_text else (item.get("firmware") or "未声明")
    return updated


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
        source = direct_url(item.get("source")) or "#"
        url = direct_url(item.get("url")) or "#"
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
    shown = []
    for item in proxied["payloads"]:
        repo = github_repo(item.get("source"))
        readme_text = fetch_readme(*repo) if repo else ""
        shown.append(with_project_page(item, readme_text))
    table, files = render_table(shown, icons)
    write_icons(files)
    content = README.read_text(encoding="utf-8") if README.exists() else ""
    README.write_text(update_readme_text(content, table), encoding="utf-8")


if __name__ == "__main__":
    main()
