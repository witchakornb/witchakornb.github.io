#!/usr/bin/env python3
import re

# Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define replacements
replacements = [
    # Background colors
    (r'class="([^"]*)\s*bg-white\s*([^"]*)"', r'class="\1 \2" style="background-color: var(--bg-primary);"'),
    (r'class="([^"]*)\s*bg-gray-50\s*([^"]*)"', r'class="\1 \2" style="background-color: var(--bg-secondary);"'),
    (r'class="([^"]*)\s*bg-gray-100\s*([^"]*)"', r'class="\1 \2" style="background-color: var(--bg-tertiary);"'),
    
    # Text colors
    (r'text-gray-500', r'text-gray-500" style="color: var(--text-tertiary);'),
    (r'text-gray-600', r'text-gray-600" style="color: var(--text-tertiary);'),
    (r'text-gray-700', r'text-gray-700" style="color: var(--text-secondary);'),
    
    # Border colors  
    (r'border-gray-200', r'border" style="border-color: var(--border-color);'),
]

# Apply replacements
for pattern, replacement in replacements:
    content = re.sub(pattern, replacement, content)

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Theme update complete!")
