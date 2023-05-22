import os
import xml.etree.ElementTree as ET

def combine_svgs(directory):
    combined_svg = ET.Element('svg')
    
    for filename in os.listdir(directory):
        if filename.endswith('.svg'):
            file_path = os.path.join(directory, filename)
            svg_tree = ET.parse(file_path)
            root = svg_tree.getroot()
            
            # Append the SVG root element to the combined SVG
            combined_svg.extend(root)
    
    # Generate the spritemap.tsx React component
    spritemap_content = f'''
    import {{ FunctionComponent }} from 'react';
    
    export const icons = {{
    
        defaultTheme: {{
            {ET.tostring(combined_svg).decode()}
        }},
    }};
    '''

    spritemap_content = spritemap_content + '''
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
    );
    '''
    
    with open('spritemap.tsx', 'w') as f:
        f.write(spritemap_content)

# Call the combine_svgs function and provide the directory path where your SVG files are stored
combine_svgs('/Users/linus/Documents/Git/candis-icons/svg')