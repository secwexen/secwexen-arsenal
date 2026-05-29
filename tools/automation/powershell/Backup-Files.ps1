param(
    [Parameter(Mandatory = $true)]
    [string]$SourcePath,

    [Parameter(Mandatory = $true)]
    [string]$BackupPath,

    [int]$RetentionDays = 7
)

Write-Host "[+] Starting backup process..." -ForegroundColor Cyan

if (-not (Test-Path $SourcePath)) {
    Write-Host "[!] Source directory not found: $SourcePath" -ForegroundColor Red
    exit 1
}

if (-not (Test-Path $BackupPath)) {
    Write-Host "[+] Creating backup directory..." -ForegroundColor Yellow
    New-Item -ItemType Directory -Path $BackupPath | Out-Null
}

$Timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$ArchiveName = "backup_$Timestamp.zip"
$ArchivePath = Join-Path $BackupPath $ArchiveName

Write-Host "[+] Creating backup archive..."
Write-Host "    Source: $SourcePath"
Write-Host "    Output: $ArchivePath"

try {
    Compress-Archive -Path $SourcePath -DestinationPath $ArchivePath -Force
    Write-Host "[✓] Backup created successfully." -ForegroundColor Green
}
catch {
    Write-Host "[!] Backup failed: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

Write-Host "[+] Removing backups older than $RetentionDays days..."
$OldBackups = Get-ChildItem -Path $BackupPath -Filter "*.zip" | Where-Object {
    $_.LastWriteTime -lt (Get-Date).AddDays(-$RetentionDays)
}

foreach ($file in $OldBackups) {
    Remove-Item $file.FullName -Force
    Write-Host "    Deleted old backup: $($file.Name)"
}

Write-Host "[✓] Backup process completed." -ForegroundColor Green
