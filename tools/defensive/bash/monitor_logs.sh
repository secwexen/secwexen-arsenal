LOG_FILE="/var/log/syslog"
ALERT_LOG="/var/log/secwexen_log_monitor.log"

mkdir -p "$(dirname "$ALERT_LOG")"

log_alert() {
    timestamp=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$timestamp] $1" | tee -a "$ALERT_LOG"
}

if [ ! -f "$LOG_FILE" ]; then
    log_alert "[!] System log file not found: $LOG_FILE"
    exit 1
fi

log_alert "[+] Starting log monitor..."
log_alert "    Monitoring: $LOG_FILE"

KEYWORDS=(
    "failed"
    "unauthorized"
    "denied"
    "segfault"
    "panic"
    "error"
    "attack"
    "malware"
    "ssh"
)

PATTERN=$(printf "|%s" "${KEYWORDS[@]}")
PATTERN=${PATTERN:1}

tail -Fn0 "$LOG_FILE" | while read line; do
    if echo "$line" | grep -Ei "$PATTERN" >/dev/null; then
        log_alert "[!] Suspicious event detected:"
        log_alert "    $line"
    fi
done
