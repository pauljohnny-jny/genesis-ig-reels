# genesis-ig-reels

Hosting and production toolkit for the silent Tamil CNC reels on @genesis.managementsolutions.

- `reels/` – final MP4s approved for publishing (served via raw.githubusercontent.com so the publishing tool can fetch them). Files are kept byte-for-byte, including their content credentials.
- `captions/` – the final caption for each reel.
- `toolkit/` – the renderer: HTML/SVG scenes → Playwright Chromium → ffmpeg (1080×1920, 30 fps, H.264).

Educational content only. No job offers, client material or candidate data are stored here.
