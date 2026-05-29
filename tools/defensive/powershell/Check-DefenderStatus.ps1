Write-Host "[+] Checking Windows Defender status..." -ForegroundColor Cyan

if (-not (Get-Command Get-MpComputerStatus -ErrorAction SilentlyContinue)) {
    Write-Host "[!] Windows Defender module not found. This system may not support Defender." -ForegroundColor Red
    exit 1
}

$status = Get-MpComputerStatus

Write-Host ""
Write-Host "===== Windows Defender Status =====" -ForegroundColor Yellow

Write-Host "Real-Time Protection: $($status.RealTimeProtectionEnabled)"
Write-Host "Behavior Monitoring:  $($status.BehaviorMonitorEnabled)"
Write-Host "IOAV Protection:      $($status.IOAVProtectionEnabled)"
Write-Host "NIS Protection:       $($status.NISEnabled)"
Write-Host "Antivirus Enabled:    $($status.AntivirusEnabled)"
Write-Host "Antispyware Enabled:  $($status.AntispywareEnabled)"
Write-Host "Full Scan Age:        $($status.FullScanAge) days"
Write-Host "Quick Scan Age:       $($status.QuickScanAge) days"
Write-Host "Last Update:          $($status.AntivirusSignatureLastUpdated)"
Write-Host "Signature Version:    $($status.AntivirusSignatureVersion)"

Write-Host ""
Write-Host "===== Threat History =====" -ForegroundColor Yellow

$threats = Get-MpThreatDetection 2>$null

if ($threats) {
    foreach ($t in $threats) {
        Write-Host "[!] Threat Detected:" -ForegroundColor Red
        Write-Host "    Name:        $($t.ThreatName)"
        Write-Host "    Severity:    $($t.SeverityID)"
        Write-Host "    Action:      $($t.ActionSuccess)"
        Write-Host "    Date:        $($t.InitialDetectionTime)"
        Write-Host ""
    }
} else {
    Write-Host "[✓] No threats detected." -ForegroundColor Green
}

Write-Host ""
Write-Host "[+] Defender status check completed." -ForegroundColor Green
