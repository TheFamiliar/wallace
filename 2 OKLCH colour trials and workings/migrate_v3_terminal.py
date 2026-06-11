#!/usr/bin/env python3
"""Migrate Wallace .terminal themes from v2 to v3 colours (PyObjC).

Reads v3_hex_map.json (written by migrate_v3.py), unarchives every NSColor
blob in each .terminal plist, maps its sRGB hex through the table
(preserving alpha), re-archives, and writes the plist back as XML.

Run with a python that has pyobjc-framework-Cocoa installed:
    /opt/homebrew/bin/python3.9 migrate_v3_terminal.py

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""

import json
import plistlib
from pathlib import Path

from AppKit import NSColor, NSColorSpace
from Foundation import NSData, NSKeyedArchiver, NSKeyedUnarchiver

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
HEX_MAP = json.loads((HERE / "v3_hex_map.json").read_text())
FILES = [ROOT / "5 Terminal Theme" / f"Wallace {s}.terminal"
         for s in ("AA", "AAA")]


def srgb(colour):
    return colour.colorUsingColorSpace_(NSColorSpace.sRGBColorSpace())


def hex_of(colour):
    c = srgb(colour)
    return "#" + "".join(f"{round(v * 255):02x}"
                         for v in (c.redComponent(), c.greenComponent(),
                                   c.blueComponent()))


def colour_from(hex_, alpha):
    v = int(hex_[1:], 16)
    return NSColor.colorWithSRGBRed_green_blue_alpha_(
        ((v >> 16) & 0xFF) / 255, ((v >> 8) & 0xFF) / 255,
        (v & 0xFF) / 255, alpha)


def main():
    for path in FILES:
        plist = plistlib.loads(path.read_bytes())
        replaced, kept = 0, 0
        for key, value in plist.items():
            if not isinstance(value, bytes):
                continue
            data = NSData.dataWithBytes_length_(value, len(value))
            old, err = NSKeyedUnarchiver.unarchivedObjectOfClass_fromData_error_(
                NSColor, data, None)
            if old is None:
                continue
            old_hex = hex_of(old)
            new_hex = HEX_MAP.get(old_hex)
            if new_hex is None:
                kept += 1
                print(f"  {path.name}: {key} {old_hex} not in map, kept")
                continue
            fresh = colour_from(new_hex, srgb(old).alphaComponent())
            blob, err = NSKeyedArchiver.archivedDataWithRootObject_requiringSecureCoding_error_(
                fresh, False, None)
            if blob is None:
                raise SystemExit(f"archive failed for {key}: {err}")
            plist[key] = bytes(blob)
            replaced += 1
        path.write_bytes(plistlib.dumps(plist, fmt=plistlib.FMT_XML))
        print(f"{path.name}: {replaced} colours mapped, {kept} left untouched")


if __name__ == "__main__":
    main()
