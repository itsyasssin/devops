# tiny-cicd

Train → test → Docker build → release on GitHub → auto-deploy to a server.

## Run locally
    pip install -r requirements-dev.txt
    python train.py && pytest
    uvicorn app.main:app --reload      # http://localhost:8000

## Pipeline
| Workflow | Trigger | Does |
|---|---|---|
| `ci.yml` | push to main / PR | train, pytest, docker build (dev), container smoke test, upload model artifact |
| `release.yml` | tag `v*` | train, pytest, build + push image to GHCR, GitHub Release with `model.joblib` + `metrics.json`, SSH deploy |

## One-time setup
1. Server: install Docker, open port 80, add your public SSH key.
2. Repo → Settings → Secrets and variables → Actions:
   `SERVER_HOST`, `SERVER_USER`, `SERVER_SSH_KEY` (private key).
3. Release:
       git tag v0.1.0 && git push --tags
