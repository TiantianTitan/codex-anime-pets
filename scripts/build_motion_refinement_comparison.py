#!/usr/bin/env python3
"""Build a relative-asset comparison of all existing pets, with native timing."""
import argparse
import json
import os
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
RUN = ROOT / 'work/motion-refinement-2026-11-06'

def build(public=False):
    inventory = json.loads((RUN / 'inventory.json').read_text())
    candidates = json.loads((RUN / 'candidates.json').read_text())
    changes = {p['id']: p for p in candidates['editions']}
    out = ROOT / 'docs/pet-motion-refinement.html' if public else RUN / 'preview.html'
    assets = ROOT / 'docs/pet-motion-refinement-assets'
    data = []
    for p in inventory['editions']:
        changed = changes.get(p['id'], {})
        rows = {r['row']: r for r in changed.get('rows', [])}
        atlas = ROOT / (p['atlas'] if public or not changed else changed['atlas'])
        after_version = changed.get('sha256', p['sha256'])[:12]
        pet = {'id': p['id'], 'name': p['name'], 'changes': list(rows), 'rows': []}
        for r in p['rows']:
            row = r['row']
            before = ROOT / p['atlas']
            y = row * 208
            if row in rows:
                before = ROOT / r['strip']
                y = 0
                if public:
                    assets.mkdir(exist_ok=True)
                    before = assets / (p['id'] + '--' + r['state'] + '-before.webp')
                    Image.open(ROOT / r['strip']).save(before, format='WEBP', lossless=True, exact=True)
                method = rows[row]['method']
                note = {'same-state-complete-frames':'调整同一动作内的完整帧顺序，保留角色外观，让反应与恢复衔接更自然。',
                        'source-arc-registration':'统一人物比例并调整现有跳跃弧线，在原生画布内保留起落，让动作与待机的尺寸衔接更自然。',
                        'source-reextraction':'从原始完整素材统一缩放、重新提取，保留动作起伏并修复原有配准问题。',
                        'generated-row':'整行动作重绘，保持角色身份，修复道具或姿态断裂；帧数保持不变。'}[method]
            else:
                note = '本动作保留原样；本轮未确认需要替换的明显问题。'
            pet['rows'].append({'row': row, 'durations': r['durations_ms'], 'note': note,
                'before': {'src': os.path.relpath(before, out.parent) + '?v=' + p['sha256'][:12], 'y': y},
                'after': {'src': os.path.relpath(atlas, out.parent) + '?v=' + after_version, 'y': row * 208}})
        data.append(pet)
    html = (ROOT / 'scripts/motion-review/refinement.template.html').read_text()
    payload = json.dumps({'pets': data, 'baseline': inventory['baseline_commit']}, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    out.write_text(html.replace('/* DATA */', payload))
    print(out)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--public', action='store_true')
    build(parser.parse_args().public)
