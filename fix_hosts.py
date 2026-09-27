# -*- coding: utf-8 -*-
# 修复 hosts：移除指向 127.0.0.1 的 GitHub 相关条目，保留其他内容（含 Steam 条目）
import sys

path = r'C:\Windows\System32\drivers\etc\hosts'

with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

keywords = ('github.com', 'githubusercontent.com', 'github.io',
            'githubassets.com', 'github.net')

kept, removed = [], []
for line in lines:
    low = line.strip().lower()
    if (low and not low.startswith('#') and '127.0.0.1' in low
            and any(k in low for k in keywords)):
        removed.append(line)
    else:
        kept.append(line)

# 系统目录内再留一份备份
with open(path + '.bak-github', 'w', encoding='utf-8') as f:
    f.writelines(lines)

with open(path, 'w', encoding='utf-8') as f:
    f.writelines(kept)

print('REMOVED_COUNT=%d' % len(removed))
for r in removed:
    print('REMOVED:', r.strip())
