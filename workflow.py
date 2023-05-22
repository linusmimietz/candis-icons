from bs4 import BeautifulSoup
import os

def kebab_to_camel(kebab):
    words = kebab.split('-')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

endOfFile = """
export type ThemeKey = keyof typeof icons;
export type IconKey = keyof (typeof icons)[ThemeKey];

export interface SpritemapProps {
theme?: ThemeKey;
}

export const Spritemap: FunctionComponent<SpritemapProps> = ({
theme = 'defaultTheme',
}) => (
<svg width="0" height="0" style={{ display: 'none' }}>
    <defs>
    {Object.entries(icons[theme]).map(([key, value]) => (
        <g id={`icon-${key}`} key={key} fill="currentColor">
        {value}
        </g>
    ))}
    </defs>
</svg>
);"""

svg_dir = './svg'
output_file = './spritemap.tsx'

svg_files = os.listdir(svg_dir)

icons = {}

for svg_file in svg_files:
    with open(os.path.join(svg_dir, svg_file), 'r') as file:
        data = file.read()
    soup = BeautifulSoup(data, 'xml')
    paths = soup.find_all('path')
    icon_name = kebab_to_camel(os.path.splitext(svg_file)[0])  # convert to camelCase
    icons[icon_name] = [path.attrs for path in paths]  # get all attributes of each path

with open(output_file, 'w') as file:
    file.write("import { FunctionComponent } from 'react';\n\n")
    file.write("export const icons = {\n  defaultTheme: {\n")
    for icon_name, paths in icons.items():
        file.write(f"    {icon_name}: (\n")
        if len(paths) > 1:
            file.write("      <>\n")
        for path_attrs in paths:
            attrs_str = ' '.join(f'{k}="{v}"' for k, v in path_attrs.items())
            file.write(f'        <path {attrs_str} />\n')
        if len(paths) > 1:
            file.write("      </>\n")
        file.write("    ),\n")
    file.write("  },\n};\n")
    file.write(endOfFile)
