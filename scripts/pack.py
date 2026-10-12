"""把 template.html 打包成自包含单文件（两张 logo 转 base64 内联）。

用法：
    python pack.py                      # 输出到当前目录 / 三棵树汇报模板.html
    python pack.py D:/out/我的汇报.html  # 指定输出路径

打包后的 HTML 只有一个文件，可直接微信/邮件发给别人，双击即开，不依赖任何素材。
"""
import base64
import os
import re
import sys

SKILL_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(SKILL_ROOT, 'template.html')
ASSETS = os.path.join(SKILL_ROOT, 'assets')
IMAGES = ['nav_logo_x2.png', 'skshu_logo.png']


def pack(out_path):
    src = open(SRC, encoding='utf-8').read()
    for name in IMAGES:
        p = os.path.join(ASSETS, name)
        if not os.path.exists(p):
            print('[warn] 缺少素材，跳过:', p)
            continue
        b64 = base64.b64encode(open(p, 'rb').read()).decode()
        src = src.replace('assets/%s' % name, 'data:image/png;base64,%s' % b64)
    d = os.path.dirname(os.path.abspath(out_path))
    if d and not os.path.isdir(d):
        os.makedirs(d, exist_ok=True)          # 输出目录不存在时自动创建
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(src)
    left = re.findall(r'assets/["\')\s]*[^"\')]+', src)
    print('已生成:', out_path)
    print('体积  :', os.path.getsize(out_path), 'bytes')
    print('未内联引用:', left if left else '无（完全自包含）')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        out = sys.argv[1]
    else:
        out = os.path.join(os.getcwd(), '三棵树汇报模板.html')
    pack(out)
