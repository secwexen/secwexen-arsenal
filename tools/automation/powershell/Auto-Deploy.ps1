Write-Host "[+] Starting Secwexen Auto Deployment..." -ForegroundColor Cyan

$RepoURL   = "https://github.com/secwexen/secwexen-arsenal.git"
$InstallDir = "C:\Secwexen"
$VenvPath   = "$InstallDir\.venv"

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "[!] Git not found. Installing Git..." -ForegroundColor Yellow
    winget install --id Git.Git -e
}

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "[!] Python not found. Installing Python..." -ForegroundColor Yellow
    winget install --id Python.Python.3 -e
}

if (-not (Test-Path $InstallDir)) {
    Write-Host "[+] Cloning repository..." -ForegroundColor Green
    git clone $RepoURL $InstallDir
} else {
    Write-Host "[+] Updating repository..." -ForegroundColor Green
    Set-Location $InstallDir
    git pull
}

Write-Host "[+] Setting up Python virtual environment..." -ForegroundColor Cyan

if (-not (Test-Path $VenvPath)) {
    python -m venv $VenvPath
}

# Activate venv
$ActivateScript = "$VenvPath\Scripts\Activate.ps1"
. $ActivateScript

Write-Host "[+] Installing Python dependencies..." -ForegroundColor Cyan
pip install --upgrade pip
pip install -r "$InstallDir\requirements.txt"

Write-Host ""
Write-Host "[✓] Secwexen Deployment Completed Successfully!" -ForegroundColor Green
Write-Host "Location: $InstallDir"
Write-Host "Virtual Env: $VenvPath"
Write-Host ""
Write-Host "You can now run the framework using:" -ForegroundColor Cyan
Write-Host "    .\.venv\Scripts\Activate.ps1" -ForegroundColor Yellow
Write-Host "    python examples\osint_demo.py" -ForegroundColor Yellow
