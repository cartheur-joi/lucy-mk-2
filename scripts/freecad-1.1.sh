#!/usr/bin/env bash
set -euo pipefail

APPIMAGE="/home/cartheur/ame/programs/freecad/FreeCAD_1.1rc2-Linux-aarch64-py311.AppImage"
HOME_DIR="/tmp/fc11home"

if [[ ! -f "$APPIMAGE" ]]; then
  echo "FreeCAD 1.1 AppImage not found: $APPIMAGE" >&2
  exit 1
fi

mkdir -p "$HOME_DIR"
chmod +x "$APPIMAGE"

exec env HOME="$HOME_DIR" QT_QPA_PLATFORM=offscreen \
  "$APPIMAGE" --appimage-extract-and-run freecadcmd "$@"
