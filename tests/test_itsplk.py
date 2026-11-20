import unittest
import update_itsplk

class ItsplkTests(unittest.TestCase):
    def test_project_page_fills_description_and_firmware(self):
        item = {"name": "ps5upload", "description": "catalog", "source": "https://github.com/phantomptr/ps5upload/releases"}
        readme = '<img alt="firmware" src="https://img.shields.io/badge/PS5_firmware-1.00_–_14.10_supported_•_5.10,_9.60_&_13.60_tested-brightgreen" />'
        updated = update_itsplk.with_project_page(item, readme)
        self.assertEqual(updated["description"], update_itsplk.HOMEPAGE_SUMMARY["ps5upload"])
        self.assertEqual(updated["firmware"], "1.00–14.10（5.10、9.60、13.60 已测试）")
        self.assertEqual(item["description"], "catalog")

    def test_firmware_reads_homepage_support_statements(self):
        cases = [
            ("Supports firmwares <b>6.00&ndash;13.60</b>.", "6.00–13.60"),
            ("A PS5 able to run payloads (Jailbroken 1.00 - 13.60).", "1.00–13.60"),
            ("Tested on firmware **11.60**.", "11.60 已测试"),
            ("**Compatibility:** Supports all Jailbroken PS5 firmwares running **[Kstuff-lite v1.07+](https://github.com/EchoStretch/kstuff-lite)**.", "全部已越狱固件（需 kstuff-lite v1.07+）"),
            ("FW  4.03 about 20 MB/s", "未声明"),
        ]
        for text, expected in cases:
            self.assertEqual(update_itsplk.firmware_from_readme(text), expected, text)
        self.assertIsNone(update_itsplk.github_repo("https://git.etawen.dev/earthonion/garlic-savemgr/releases"))
        with self.assertRaises(ValueError):
            update_itsplk.fetch_text("https://example.com/README.md")

    def test_fetch_rejects_unexpected_url(self):
        with self.assertRaises(ValueError):
            update_itsplk.fetch_json("https://example.com/payloads_v2.json")

    def test_table_matches_existing_columns_and_proxied_links(self):
        icon = "data:image/png;base64,aGVsbG8="
        payloads = [{
            "name": "Demo|Name",
            "version": "v1",
            "description": "line\ntwo",
            "last_update": "2026-11-20",
            "source": "https://gh-proxy.farquer.eu.org/https://github.com/someone/demo/releases",
            "url": "https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/Demo.elf",
            "icon_key": "abc",
        }]
        table, files = update_itsplk.render_table(payloads, {"abc": icon})
        self.assertTrue(table.startswith("| 图标 | 名称 | 版本 | 说明 | 支持固件 | 最近更新 | 源码 | 下载 |"))
        self.assertIn("**Demo\\|Name**", table)
        self.assertIn("line two", table)
        self.assertIn("| 未声明 |", table)
        self.assertIn("readme-icons-itsplk/Demo_Name.png", table)
        self.assertIn("gh-proxy.farquer.eu.org/https://github.com/", table)
        self.assertEqual(files["Demo_Name.png"], b"hello")

    def test_readme_update_keeps_existing_table_and_usage(self):
        content = """## 使用方式

### itsPLK 官方源国内加速

https://gh-proxy.farquer.eu.org/https://raw.githubusercontent.com/farquer/ps5-payloads-mirror/main/payloads_itsplk_ghproxy.json

## 注意

keep me

<!-- PAYLOADS_START -->
local table
<!-- PAYLOADS_END -->

### itsPLK 官方源
"""
        updated = update_itsplk.update_readme_text(content, "| row |")
        self.assertIn("local table", updated)
        self.assertIn("keep me", updated)
        self.assertIn("### itsPLK 官方源国内加速", updated)
        self.assertIn("## itsPLK 国内加速", updated)
        self.assertNotIn("\n### itsPLK 官方源\n", updated)
        self.assertEqual(updated.count("payloads_itsplk_ghproxy.json"), 1)
        again = update_itsplk.update_readme_text(updated, "| next |")
        self.assertIn("| next |", again)
        self.assertNotIn("| row |", again)
        self.assertEqual(again.count("## itsPLK 国内加速"), 1)

if __name__ == "__main__":
    unittest.main()
