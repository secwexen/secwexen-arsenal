$LogFile = "C:\computer\logs\process_monitor.log"
$SuspiciousNames = @("mimikatz", "meterpreter", "cobalt", "beacon", "powersploit", "keylogger")

$logDir = Split-Path $LogFile
if (-not (Test-Path $logDir)) {
    New-Item -ItemType Directory -Path $logDir | Out-Null
}

function Write-Log {
    param([string]$Message)

    $timestamp = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
    $entry = "[$timestamp] $Message"

    Write-Host $entry
    Add-Content -Path $LogFile -Value $entry
}

Write-Log "[+] Starting process monitor..."
Write-Log "    Log file: $LogFile"

while ($true) {
    $processes = Get-Process | Sort-Object CPU -Descending

    foreach ($proc in $processes) {
        if ($proc.CPU -gt 50) {
            Write-Log "[!] High CPU usage detected: $($proc.ProcessName) - CPU: $([math]::Round($proc.CPU,2))"
        }

        if ($proc.WorkingSet64 -gt 500MB) {
            Write-Log "[!] High memory usage detected: $($proc.ProcessName) - RAM: $([math]::Round($proc.WorkingSet64/1MB,2)) MB"
        }

        foreach ($name in $SuspiciousNames) {
            if ($proc.ProcessName -match $name) {
                Write-Log "[!] Suspicious process detected: $($proc.ProcessName)"
            }
        }
    }

    Start-Sleep -Seconds 5
}
