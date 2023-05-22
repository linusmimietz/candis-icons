import React from 'react';
import { Spritemap, icons, ThemeKey, IconKey } from './spritemap';

const App: React.FC = () => {
  const theme: ThemeKey = 'defaultTheme';
  const iconKeys: IconKey[] = Object.keys(icons[theme]) as IconKey[];

  return (
    <div className="App" style={{ margin: '64px' }}>
      <h1 style={{ marginBottom: '32px' }}>{`${iconKeys.length} Icons`}</h1>
      <Spritemap />
      {iconKeys.map(icon => (
        <div key={icon} style={{ display: 'flex', alignItems: 'center', marginBottom: '16px' }}>
          <svg width="20" height="20">
            <use xlinkHref={`#icon-${icon}`} />
          </svg>
          <span style={{ marginLeft: '10px' }}>{icon}</span>
        </div>
      ))}
    </div>
  );
}

export default App;
