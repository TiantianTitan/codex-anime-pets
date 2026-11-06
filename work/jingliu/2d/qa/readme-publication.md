# Jingliu README update

This update adds character **48**, Jingliu, to the English, French, Simplified Chinese and Japanese README files. The collection now contains **48 characters / 49 editions**, including 13 Honkai: Star Rail characters. The historical November 6 compatibility batch counts remain unchanged.

New arrivals are Wanderer, Kallen and Jingliu (046–048). All four localized arrivals images and collection walls were rebuilt with the existing showcase generator. Cache keys were advanced to `v=48`. The final gallery row remains three columns, and the next-companion placeholder occupies its own full-width row. English, French and Chinese receive archive 48; Japanese keeps its established compact gallery/download format.

Jingliu's lossless idle asset is a byte-identical copy of the approved final-atlas preview. The archive card follows the existing 220×240 canvas, 198px silhouette height and 220px baseline. The hero, motion reel, direction orbit, parades, community panel and other existing assets were not rebuilt. The protected-asset hash check covers 119 existing files.

Validation: [readme-validation.json](readme-validation.json) checks 1,261 local paths and anchors, all four counts and download groups, retained character numbering, the final three-column row, preview timing/pixels, and protected assets. It reports no errors. [readme-browser-validation.json](readme-browser-validation.json) records the background-only browser checks.

The browser check used a local Markdown renderer with GitHub-like styling, not GitHub's production renderer. Screenshots were kept locally under `output/playwright/jingliu-readme/`; the browser was explicitly headless. No live pets were installed or changed.

Publication scope: these README changes, ten associated showcase assets, the showcase roster configuration, Jingliu's product folder/ZIP, and selected reproducible source/QA evidence. User reference images, rejected/redundant candidates, browser logs, unrelated skill changes and other character folders are excluded. Requested commit subject: `Jingliu`; author and committer: `TiantianTitan <haotianx4@gmail.com>`.
