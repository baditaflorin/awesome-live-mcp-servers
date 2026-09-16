#!/usr/bin/env bash
# scripts/fleet-sync-cron.sh
# Scheduled synchronization job executed on the self-hosted fleet infrastructure.
# Runs via cron / systemd timer on 0docker_docker_prod or 0mcp_runtime_control.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

cd "${REPO_DIR}"

echo "[$(date -u +"%Y-%m-%dT%H:%M:%SZ")] Starting MCP Directory Fleet Sync..."

# Ensure clean working tree and fetch latest changes
git fetch origin main || true
git checkout main || true
git pull origin main --ff-only || true

# Execute the directory synchronizer and liveness prober
python3 scripts/sync_mcp_servers.py

# Check if data or README changed
if [[ -n $(git status --porcelain) ]]; then
  echo "[$(date -u +"%Y-%m-%dT%H:%M:%SZ")] Changes detected. Staging updates..."
  git add README.md data/mcp-servers.json data/mcp-servers.csv
  
  COMMIT_MSG="chore(fleet-sync): weekly benchmark update [skip ci]"
  git commit -m "${COMMIT_MSG}"
  
  echo "[$(date -u +"%Y-%m-%dT%H:%M:%SZ")] Pushing updates to origin main..."
  git push origin main
  echo "[$(date -u +"%Y-%m-%dT%H:%M:%SZ")] Fleet sync completed successfully."
else
  echo "[$(date -u +"%Y-%m-%dT%H:%M:%SZ")] No directory changes detected. Directory is up-to-date."
fi
