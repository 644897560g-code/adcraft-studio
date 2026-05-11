#!/usr/bin/env python3
output = r"/Users/xiaowu/WorkBuddy/Claw/ad-video-product/app/index.html"
html = open(output, 'w', encoding='utf-8') if False else None

def w(s):
    with open(output, 'a', encoding='utf-8') as f:
        f.write(s + '\n')

# Start fresh
with open(output, 'w', encoding='utf-8') as f:
    f.write('')

print("Starting generation...")
print(f"Output: {output}")
import os
print(f"Dir exists: {os.path.dirname(output)}")
