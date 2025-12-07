#!/bin/bash
# Generate SVG logo placeholder for Dingo OS

cat > "$(dirname "$0")/dingo-logo.svg" << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<svg width="512" height="512" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="gradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#E65100;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#FF8F00;stop-opacity:1" />
    </linearGradient>
  </defs>
  
  <!-- Kangaroo silhouette with circuit board pattern -->
  <g transform="translate(256,256)">
    <!-- Body -->
    <ellipse cx="0" cy="20" rx="80" ry="100" fill="url(#gradient)"/>
    
    <!-- Head -->
    <circle cx="0" cy="-60" r="50" fill="url(#gradient)"/>
    
    <!-- Ears -->
    <ellipse cx="-25" cy="-95" rx="15" ry="40" fill="url(#gradient)"/>
    <ellipse cx="25" cy="-95" rx="15" ry="40" fill="url(#gradient)"/>
    
    <!-- Tail -->
    <path d="M -60 40 Q -120 60 -100 120" stroke="url(#gradient)" stroke-width="20" fill="none" stroke-linecap="round"/>
    
    <!-- Legs -->
    <ellipse cx="-30" cy="100" rx="15" ry="40" fill="url(#gradient)"/>
    <ellipse cx="30" cy="100" rx="15" ry="40" fill="url(#gradient)"/>
    
    <!-- Circuit board pattern overlay -->
    <g opacity="0.3">
      <line x1="-40" y1="-20" x2="40" y2="-20" stroke="#FFF" stroke-width="2"/>
      <line x1="0" y1="-40" x2="0" y2="60" stroke="#FFF" stroke-width="2"/>
      <circle cx="-40" cy="-20" r="4" fill="#FFF"/>
      <circle cx="40" cy="-20" r="4" fill="#FFF"/>
      <circle cx="0" cy="0" r="4" fill="#FFF"/>
      <circle cx="0" cy="40" r="4" fill="#FFF"/>
    </g>
  </g>
  
  <!-- Text -->
  <text x="256" y="460" font-family="Ubuntu, sans-serif" font-size="48" font-weight="bold" text-anchor="middle" fill="#333">
    DINGO OS
  </text>
</svg>
EOF

echo "Logo generated: dingo-logo.svg"
