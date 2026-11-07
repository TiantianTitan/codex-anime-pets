# Albedo README update

Albedo is character **49**. The collection now contains **49 characters / 50 editions**, with **14 Genshin Impact characters**. English, French, Simplified Chinese and Japanese README files have matching totals, download links and localized names.

New Arrivals contains Kallen, Jingliu and Albedo (047–049). All four localized arrivals animations and collection walls were rebuilt with the existing showcase generator, and their README cache keys advanced to `v=49`. The collection wall includes the numbered Albedo card; Raiden Mei keeps 05A and 05B. The gallery adds Albedo at normal column width beside the next-companion placeholder. English, French and Chinese add archive 49; Japanese retains its existing compact gallery/download format.

Albedo's idle asset is a byte-identical copy of the approved final-atlas preview. The archive portrait uses the established 220×240 canvas, 198px silhouette height and 220px baseline. The existing hero, motion film, direction orbit, parades and community panel remain unchanged. Hash comparison protects 121 existing README assets. The product atlas and ZIP also remain byte-identical to the approved release.

Reproduction: run `build-readme.py` with the bundled workspace Python, then `validate-readme.py`. [readme-validation.json](readme-validation.json) records 1,285 successful local path/anchor checks, collection and download counts, gallery structure, animation duration, final-atlas pixels, product integrity and protected asset hashes. [readme-browser-validation.json](readme-browser-validation.json) records background-only browser checks of all four languages, the archive link, card dimensions and the 390px gallery. The local Markdown preview approximates GitHub styling; it is not a live GitHub render.

The frontend-design review preserved the established collection style and aligned the new card with the existing size and baseline. Screenshots were reviewed locally under `output/playwright/albedo-readme/`. The headless browser and read-only preview server were closed after inspection. No commit or push was performed during this README update.
