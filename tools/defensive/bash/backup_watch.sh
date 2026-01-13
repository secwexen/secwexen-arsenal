#!/bin/bash

SOURCE_DIR="/opt/secwexen"
BACKUP_DIR="/var/backups/secwexen"
LOG_FILE="/var/log/secwexen_backup.log"

# Create backup directory if missing
mkdir -p "$BACKUP_DIR"

log() {
    timestamp=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$timestamp] $1" | tee -a "$LOG_FILE"
}

backup() {
    timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
    archive="$BACKUP_DIR/backup_$timestamp.tar.gz"

    log "[+] Change detected. Creating backup: $archive"
    tar -czf "$archive" "$SOURCE_DIR"

    if [ $? -eq 0 ]; then
        log "[✓] Backup completed successfully."
    else
        log "[!] Backup failed."
    fi
}

log "[+] Starting backup watcher..."
log "    Watching: $SOURCE_DIR"
log "    Backup dir: $BACKUP_DIR"

# Check if inotifywait exists
if ! command -v inotifywait >/dev/null 2>&1; then
    log "[!] inotify-tools not installed. Installing..."
    apt-get update && apt-get install -y inotify-tools
fi

# Monitor directory for changes
inotifywait -m -r -e modify,create,delete,move "$SOURCE_DIR" | while read path action file; do
    log "[~] Change detected: $action on $file"
    backup
done
