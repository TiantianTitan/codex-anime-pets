"""Attach state-specific temporal plans and compact reference/layout boards."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageOps

RUN = Path(__file__).resolve().parents[1]
plans = {
    "idle": "Six quiet breathing phases: neutral; small inhale; soft chest lift and minute head tilt; exhale; cloth/ribbon settles; return close to neutral. Both golden eyes comfortably open in all six. Feet planted. Calm expression, no prolonged blink or wink.",
    "running-right": "Eight genuinely different alternating gait phases facing SCREEN RIGHT throughout: first leg contact, compress, passing, lift; opposite leg contact, compress, passing, lift closing into frame 0. Arm swing opposes legs, knees/ankles change clearly. Anatomical skull/torso scale constant, no two-pose repetition.",
    "running-left": "Draw independently, NOT a mirror. Eight genuinely different alternating gait phases facing SCREEN LEFT: first leg contact, compress, passing, lift; opposite leg contact, compress, passing, lift. Opposing arm swing. Yellow RIGHT glove, dark LEFT glove, dark LEFT sleeve/yellow armband and LEFT back quiver retain real anatomical sides. Reference right gait for scale/style only.",
    "waving": "Four phases: relaxed hand starting to lift; yellow RIGHT hand raised beside shoulder; small friendly open-palm wrist wave; arm lowers close to relaxed position. Subtle easy smile. End near rest rather than peak; no detached motion marks.",
    "jumping": "Five phases: shallow knee-bend anticipation; boots lift a little; modest airborne peak with knees tucked slightly; descending/legs extend; grounded soft near-upright landing. Constant skull/torso dimensions as canonical idle. Small hop, not a deep squat or huge leap; keep hair/quiver/boots complete and reserve upper headroom. Ground endpoints share baseline; airborne feet rise.",
    "failed": "Eight standing reaction/recovery phases: calm start; slight surprise; eyebrows soften; small shoulder droop; brief rueful downward look; head starts rising; small resigned smile; calm nearly-neutral finish. No collapse or deep bow, no crying icons, tears, smoke or tools. Close smoothly into idle.",
    "waiting": "Six expectant phases: attentive start; small questioning eyebrow; dark LEFT empty palm turns up at waist; gentle questioning head tilt; palm lowers; expectant near-rest recovery. Both feet planted. Distinct from high greeting and chin-touch work.",
    "running": "Six task-processing phases, NOT foot-running: focused start; yellow RIGHT fingers approach chin; thoughtful chin touch; small considering head turn; hand starts lowering; focused near-rest recovery. Feet planted. No phone, screen, paper or weapon.",
    "review": "Six inspection phases: attentive rest; gaze lowers slightly; short forward head inclination; restrained approving nod; head rises; returns to rest. Hands stay at sides. Distinct from chin-touch work and palm-up waiting. No tool or paper."
}
for state, plan in plans.items():
    for folder in ("rows", "row-retries"):
        path = RUN / f"prompts/{folder}/{state}.md"
        path.write_text(path.read_text() + "\nHarumasa temporal plan (left to right): " + plan + "\n")

jobs = json.loads((RUN / "imagegen-jobs.json").read_text())
identity_path = RUN / "references/reference-01.png"
identity = Image.open(identity_path).convert("RGB")
provenance = []
for job in jobs["jobs"]:
    if not job["id"].startswith("look-"):
        continue
    guide_path = RUN / f"references/layout-guides/{job['id']}.png"
    guide = ImageOps.contain(Image.open(guide_path).convert("RGB"), (1400, 400))
    board = Image.new("RGB", (1400, 880 + guide.height), "white")
    board.paste(identity, (0, 0))
    board.paste(guide, ((1400-guide.width)//2, 880))
    output = RUN / f"references/{job['id']}-identity-layout.png"
    board.save(output)
    job["input_images"] = [{"path": str(output.relative_to(RUN)),
        "role": "top: outfit/front/face/chibi identity references; bottom: matching invisible layout only, NEVER copy its guide graphics"}] + [item for item in job["input_images"]
        if not item["path"].startswith(("references/reference-", "references/layout-guides/"))]
    provenance.append({"output": str(output.relative_to(RUN)), "sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
        "inputs": [{"path": str(path.relative_to(RUN)), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()} for path in (identity_path, guide_path)],
        "operation": "Unaltered reference/layout composition; no new sprite content"})
(RUN / "imagegen-jobs.json").write_text(json.dumps(jobs, indent=2) + "\n")
(RUN / "qa/reference-board-provenance.json").write_text(json.dumps(provenance, indent=2) + "\n")
(RUN / "qa/production-progress.json").write_text(json.dumps({"started_at": datetime.now(timezone.utc).isoformat(),
    "stage": "base", "scope": "2D only; product/ZIP and work QA; root README and live installation outside this request", "completed_jobs": [], "failures": []}, indent=2)+"\n")
print(json.dumps({"state_plans":len(plans), "max_input_images":max(len(job["input_images"]) for job in jobs["jobs"])}))
