import os
from pathlib import Path

for root, _, files in os.walk('./pyscf'):
    for f in files:
        p = Path(root) / f
        if p.is_symlink():
            data = p.read_bytes()
            p.unlink()
            p.write_bytes(data)
