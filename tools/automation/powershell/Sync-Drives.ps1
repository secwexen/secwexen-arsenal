param(
    [Parameter(Mandatory = $true)]
    [string]$Source,

    [Parameter(Mandatory = $true)]
    [string]$Destination,

    [bool]$Mirror = $false,

    [string]$LogFile = ""
)

function Write-Log {
    param([string]$Message)

    $timestamp = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
    $entry = "[$timestamp] $Message"

    Write-Host $entry

    if ($LogFile -ne "") {
        Add-Content -Path $LogFile -Value $entry
    }
}

if (-not (Test-Path $Source)) {
    Write-Log "[!] Source path not found: $Source"
    exit 1
}

if (-not (Test-Path $Destination)) {
    Write-Log "[+] Destination not found. Creating: $Destination"
    New-Item -ItemType Directory -Path $Destination | Out-Null
}

Write-Log "[+] Starting drive synchronization..."
Write-Log "    Source: $Source"
Write-Log "    Destination: $Destination"
Write-Log "    Mirror Mode: $Mirror"

Write-Log "[+] Syncing new and updated files..."

$sourceFiles = Get-ChildItem -Path $Source -Recurse -File

foreach ($file in $sourceFiles) {
    $relativePath = $file.FullName.Substring($Source.Length)
    $destFile = Join-Path $Destination $relativePath

    $destDir = Split-Path $destFile

    if (-not (Test-Path $destDir)) {
        New-Item -ItemType Directory -Path $destDir -Force | Out-Null
    }

    if (-not (Test-Path $destFile)) {
        Write-Log "[+] Copying new file: $relativePath"
        Copy-Item -Path $file.FullName -Destination $destFile
    }
    else {
        if ($file.LastWriteTime -gt (Get-Item $destFile).LastWriteTime) {
            Write-Log "[~] Updating file: $relativePath"
            Copy-Item -Path $file.FullName -Destination $destFile -Force
        }
    }
}

if ($Mirror) {
    Write-Log "[+] Mirror mode enabled. Checking for removed files..."

    $destFiles = Get-ChildItem -Path $Destination -Recurse -File

    foreach ($file in $destFiles) {
        $relativePath = $file.FullName.Substring($Destination.Length)
        $sourceFile = Join-Path $Source $relativePath

        if (-not (Test-Path $sourceFile)) {
            Write-Log "[-] Removing file: $relativePath"
            Remove-Item -Path $file.FullName -Force
        }
    }
}

Write-Log "[✓] Drive synchronization completed successfully."
