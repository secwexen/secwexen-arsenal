APP_DIR="/opt/secwexen"
REPO_URL="https://github.com/secwexen/secwexen-arsenal.git"

echo "[+] Starting deployment..."

if ! command -v git >/dev/null 2>&1; then
    echo "[+] Installing Git..."
    apt-get update && apt-get install -y git
fi

if ! command -v python3 >/dev/null 2>&1; then
    echo "[+] Installing Python3..."
    apt-get update && apt-get install -y python3 python3-venv
fi

if [ ! -d "$APP_DIR" ]; then
    echo "[+] Cloning repository..."
    git clone "$REPO_URL" "$APP_DIR"
else
    echo "[+] Updating repository..."
    cd "$APP_DIR" && git pull
fi

echo "[+] Setting up Python environment..."
cd "$APP_DIR"
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

echo "[+] Deployment completed successfully."
