from pathlib import Path
import re

src = Path('../martysai.github.io/_posts')
dst = Path('src/content/posts')
dst.mkdir(parents=True, exist_ok=True)

for p in sorted(src.glob('*.md')):
    text = p.read_text()
    m = re.match('^---\n(.*?)\n---\n(.*)$', text, re.S)
    if not m:
        continue
    fm, body = m.group(1), m.group(2)

    keep = []
    skip_block = False
    for line in fm.splitlines():
        if re.match(r'^(header):\s*$', line):
            skip_block = True
            continue
        if skip_block and (line.startswith(' ') or line.startswith('\t')):
            continue
        skip_block = False
        if re.match(r'^(author_profile|toc|classes|related|share):', line):
            continue
        keep.append(line)

    date = p.name[:10]
    if not any(l.startswith('pubDate:') for l in keep):
        keep.append(f'pubDate: {date}')

    body = re.sub(r'(!\[[^\]]*\]\([^\)]+\))\{:[^\}]+\}', r'\1', body)
    slug = p.name[11:]
    out = '---\n' + '\n'.join(keep).strip() + '\n---\n\n' + body.strip() + '\n'
    (dst / slug).write_text(out)
