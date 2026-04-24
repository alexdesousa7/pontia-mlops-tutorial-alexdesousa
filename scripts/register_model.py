import os
from pathlib import Path
from datetime import datetime
import json

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_DIR = PROJECT_ROOT / "models"
REGISTRY_DIR = PROJECT_ROOT / "model_registry"
REGISTRY_DIR.mkdir(exist_ok=True)

run_id = os.getenv("RUN_ID", "unknown")
model_name = os.getenv("MODEL_NAME", "adult-income-model")

registry_entry = {
    "model_name": model_name,
    "run_id": run_id,
    "timestamp": datetime.now().isoformat(),
    "artifacts": {
        "model": str(MODEL_DIR / "model.pkl"),
        "scaler": str(MODEL_DIR / "scaler.pkl"),
        "encoders": str(MODEL_DIR / "encoders.pkl")
    }
}

output_file = REGISTRY_DIR / f"{model_name}_{run_id}.json"
with open(output_file, "w") as f:
    json.dump(registry_entry, f, indent=4)

print(f"Model registered at {output_file}")
