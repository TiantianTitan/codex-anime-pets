"""Add Rita-specific temporal plans and combine existing identity/layout inputs."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageOps

RUN = Path(__file__).resolve().parents[1]
plans = {
    "idle": "Six quiet breathing phases: neutral poised stance; small inhale; soft chest lift and minute head tilt; exhale; skirt/hair settles; return close to neutral. The naturally visible RIGHT wine-red eye stays comfortably open. LEFT eye remains covered by the same long side-swept bangs, not closed or artificially exposed. Feet planted, small pleasant smile; no blink or wink holds.",
    "running-right": "Eight genuinely distinct alternating gait phases facing SCREEN RIGHT throughout: first leg contact, compression, passing, lift; opposite leg contact, compression, passing, lift closing into frame zero. Small controlled running steps and opposing arm swing; skirts follow without changing lengths. Constant skull/torso scale and actual rose/covered-eye sides. No two-pose repetition.",
    "running-left": "Draw independently, NEVER mirror. Eight genuinely distinct alternating gait phases facing SCREEN LEFT: first leg contact, compression, passing, lift; opposite leg contact, compression, passing, lift. Modest steps and opposing arm swing, consistent skirt shape. Anatomical RIGHT temple rose and anatomical LEFT covered eye stay on real sides; occlude naturally in profile instead of swapping. Right strip is scale/cadence evidence, not a mirrored source.",
    "waving": "Four graceful greeting phases: anatomical RIGHT empty gloved hand starts lifting; open palm beside shoulder; restrained friendly wrist wave; hand lowers near relaxed rest. No big overhead gesture, detached wave lines or effects; consistent small smile and head size.",
    "jumping": "Five phases: shallow knee bend; both shoes lift a little; modest airborne peak with knees softly bent; descent with legs extending; grounded soft near-upright landing. Constant head/torso dimensions matching idle, small hop not deep squat or huge leap. Full maid headband/hair/skirt/shoes with clear headroom. Ground endpoints share baseline; airborne feet rise naturally.",
    "failed": "Eight standing reaction/recovery phases: poised start; small surprised brow; faint concern; shoulders soften; brief rueful downward look; head begins to rise; reserved reassuring smile; near-neutral recovery. No collapse or deep bow. Do not add tears, symbols, smoke or tools. Comfortable last hold and return to idle.",
    "waiting": "Six expectant phases: attentive rest; slight questioning brow; anatomical LEFT empty gloved palm opens upward at waist; small questioning head tilt; palm starts lowering; expectant near-rest recovery. Feet planted, no chin touch. Distinct from raised greeting and task-processing gesture.",
    "running": "Six active task-processing phases, NOT foot-running: focused rest; anatomical RIGHT gloved fingers approach chin; thoughtful chin touch; small considering head turn; hand starts lowering; focused near-rest recovery. Feet planted, no phone, screen, paper, weapon or other tool.",
    "review": "Six inspection phases: attentive rest with hands composed low; visible gaze lowers slightly; modest head inclination; restrained approving nod; head rises; return close to poised rest. Feet planted. Keep same head size even while nodding. No new prop. Distinct from chin-touch work and palm-up waiting."
}
for state, plan in plans.items():
    for folder in ("rows", "row-retries"):
        path = RUN / f"prompts/{folder}/{state}.md"
        source = path.read_text()
        assert "Rita temporal plan" not in source, "Configure once only"
        path.write_text(source + "\nRita temporal plan (left to right): " + plan + "\n")

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
        "role": "top: classic maid outfit/front/face/chibi identity references (NO WEAPON); bottom: matching invisible layout only, NEVER copy its graphics"}] + [item for item in job["input_images"]
        if not item["path"].startswith(("references/reference-", "references/layout-guides/"))]
    provenance.append({"output": str(output.relative_to(RUN)), "sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
        "inputs": [{"path": str(path.relative_to(RUN)), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()} for path in (identity_path, guide_path)],
        "operation": "Existing reference/layout composition only, no new sprite art"})
(RUN / "imagegen-jobs.json").write_text(json.dumps(jobs, indent=2) + "\n")
(RUN / "qa/reference-board-provenance.json").write_text(json.dumps(provenance, indent=2) + "\n")
(RUN / "qa/production-progress.json").write_text(json.dumps({"started_at": datetime.now(timezone.utc).isoformat(),
    "stage": "base", "scope": "2D only; product/ZIP and work QA; no root README, live installation, commit or push", "completed_jobs": [], "failures": []}, indent=2)+"\n")
print(json.dumps({"state_plans":len(plans), "max_input_images":max(len(job["input_images"]) for job in jobs["jobs"])}))
