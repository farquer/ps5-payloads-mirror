import json
import os
from pathlib import Path
import tempfile
import unittest
import catalog

class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.previous = Path.cwd()
        self.temporary = tempfile.TemporaryDirectory()
        os.chdir(self.temporary.name)
    def tearDown(self):
        os.chdir(self.previous)
        self.temporary.cleanup()
    def test_shared_images_publish_separately_and_survive_catalog_updates(self):
        image = 'data:image/png;base64,aGVsbG8='
        first, second = {'name':'One'}, {'name':'Two'}
        catalog.assign_icon(first, image)
        self.assertTrue(Path('farquer/icons.json').exists())
        self.assertFalse(Path('farquer/payloads.json').exists())
        catalog.assign_icon(second, image)
        self.assertEqual(first['icon_key'], second['icon_key'])
        self.assertEqual(len(catalog.load_icons()), 1)
        first['version'] = '2.0'
        catalog.save_catalog([first, second])
        saved = json.loads(Path('farquer/payloads.json').read_text())
        self.assertEqual(saved['name'], 'PS5 Payloads')
        self.assertEqual(saved['icons_url'], 'icons.json')
        self.assertEqual(saved['payloads'][0]['version'], '2.0')
        self.assertEqual(list(saved['payloads'][0]), [key for key in catalog.PUBLIC_KEYS if key in saved['payloads'][0]])
        self.assertTrue(all('icon' not in entry for entry in saved['payloads']))
        self.assertEqual(catalog.payload_icon(first), image)
        first.pop('icon_key'); catalog.save_catalog([first,second])
        self.assertIsNone(catalog.payload_icon(first))
        self.assertEqual(catalog.payload_icon(second), image)
        self.assertEqual(catalog.load_catalog(), [first, second])
    def test_invalid_images_do_not_change_files_or_entries(self):
        for image in ['https://bad.invalid/image.png', 'data:image/png;base64,', 'data:image/png;base64,!bad', 'data:image/png;base64,'+'A'*13000]:
            entry={'name':'One'}
            with self.assertRaises(ValueError):catalog.assign_icon(entry,image)
            self.assertEqual(entry, {'name':'One'})
            self.assertFalse(Path('farquer/icons.json').exists())
    def test_ghproxy_catalog_matches_v2_with_github_urls_prefixed(self):
        payloads = [{
            'name': 'Demo',
            'filename': 'Demo_v1.elf',
            'url': 'https://raw.githubusercontent.com/farquer/ps5-payloads-mirror/main/farquer/elf/Demo_v1.elf',
            'source': 'https://github.com/someone/demo/releases',
            'source_direct': 'https://github.com/someone/demo/releases/download/v1/Demo.elf',
            'firmware': '未声明',
            'note': 'https://example.com/keep',
        }]
        catalog.save_catalog(payloads)
        saved = json.loads(Path('farquer/payloads.json').read_text())
        proxied = json.loads(Path('farquer/payloads_ghproxy.json').read_text())
        self.assertEqual(saved['payloads'][0]['url'], payloads[0]['url'])
        self.assertNotIn('firmware', saved['payloads'][0])
        self.assertNotIn('note', saved['payloads'][0])
        item = proxied['payloads'][0]
        self.assertEqual(item['url'], 'https://cdn.jsdelivr.net/gh/farquer/ps5-payloads-mirror@main/farquer/elf/Demo_v1.elf')
        self.assertEqual(item['source'], payloads[0]['source'])
        self.assertEqual(item['source_direct'], payloads[0]['source_direct'])
        self.assertEqual(catalog.load_catalog()[0]['firmware'], '未声明')
        saved['name'] = 'farquer PS5 Payloads source'
        proxied['name'] = 'farquer PS5 Payloads source (proxy)'
        Path('farquer/payloads.json').write_text(json.dumps(saved))
        Path('farquer/payloads_ghproxy.json').write_text(json.dumps(proxied))
        catalog.save_catalog(payloads)
        self.assertEqual(json.loads(Path('farquer/payloads.json').read_text())['name'], 'farquer PS5 Payloads source')
        self.assertEqual(json.loads(Path('farquer/payloads_ghproxy.json').read_text())['name'], 'farquer PS5 Payloads source (proxy)')
    def test_load_catalog_handles_wrapped_and_bare_formats(self):
        catalog.CATALOG.parent.mkdir(parents=True, exist_ok=True)
        catalog.CATALOG.write_text(json.dumps({'payloads': [{'name': 'Two'}]}))
        self.assertEqual(catalog.load_catalog(), [{'name': 'Two'}])

if __name__ == '__main__':unittest.main()
