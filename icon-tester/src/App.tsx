import React from 'react';
import { Spritemap, icons, ThemeKey, IconKey } from './spritemap';

const App: React.FC = () => {
  const theme: ThemeKey = 'defaultTheme';
  const iconKeys: IconKey[] = Object.keys(icons[theme]) as IconKey[];

  return (
    <div className="App">
      <Spritemap />
      {iconKeys.map(icon => (
        <svg key={icon} width="20" height="20">
          <use xlinkHref={`#icon-${icon}`} />
        </svg>
      ))}
    </div>
  );
}

export default App;
