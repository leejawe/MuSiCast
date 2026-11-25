from pathlib import Path
import json
import numpy as np

root = Path(__file__).resolve().parents[1]
metadata = json.loads((root / "data/metadata.json").read_text())
with np.load(root / "data/meteopair_scc_v1_demo.npz", allow_pickle=False) as data:
    assert len(data.files) == 8
    for name in data.files:
        field = data[name]
        assert field.shape == (64, 64)
        assert np.isfinite(field).all()
        print(name, field.shape, field.dtype, metadata["fields"][name]["units"])
print("Valid time:", metadata["valid_time_utc"])
