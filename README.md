Grafiken zur Deutschen Amateurfunkprüfung
=========================================

Ziel dieses Projektes ist es die Grafiken aus dem Fragenkatalog der BNetzA in Form von Vektorgrafiken nachhaltig zu digitalisieren. Dazu wird LaTeX verwendet sowie die LaTeX-Bibliotheken Tikz und CircuiTikz.

Vorraussetzungen
================

- LaTeX
- pdftocairo
- make
- svgo

Generierung der Grafiken
========================

```bash
make
```

Danach erscheinen die Grafiken in ./build/pdf und ./build/svg
