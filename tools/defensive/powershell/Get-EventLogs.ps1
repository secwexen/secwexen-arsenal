param(
    [int]$Days = 1,
    [string]$Output = ""
)

Write-Host "[+] Collecting Windows Event Logs..." -ForegroundColor Cyan
Write-Host "    Time Range: Last $Days day(s)"

function Write-Log {
    param([string]$Message)

    Write-Host $Message
    if ($Output -ne "") {
        Add-Content -Path $Output -Value $Message
    }
}

$StartTime = (Get-Date).AddDays(-$Days)

$Channels = @(
    "Security",
    "System",
    "Application"
)

Write-Log ""
Write-Log "===== Event Log Summary ====="

foreach ($Channel in $Channels) {
    Write-Log ""
    Write-Log "----- $Channel Logs -----"

    try {
        $Events = Get-WinEvent -FilterHashtable @{
            LogName = $Channel
            StartTime = $StartTime
        } -ErrorAction Stop

        if ($Events.Count -eq 0) {
            Write-Log "No events found."
            continue
        }

        foreach ($Event in $Events) {
            $msg = "[EventID: $($Event.Id)] [$($Event.TimeCreated)] $($Event.ProviderName) - $($Event.Message)"
            Write-Log $msg
        }
    }
    catch {
        Write-Log "[!] Failed to read $Channel logs: $($_.Exception.Message)"
    }
}

Write-Log ""
Write-Log "[✓] Event log collection completed."

if ($Output -ne "") {
    Write-Host "[+] Logs saved to: $Output" -ForegroundColor Green
}
