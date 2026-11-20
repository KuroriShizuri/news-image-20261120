# SPDX-License-Identifier: MIT
"""Copy the bundled front-page artwork to the output directory.

Reads entry.png from this script's own directory, validates it (PNG magic
bytes and exactly 1024x1024 pixels), copies it to
$MAKEFUN_OUTPUT_DIR/entry.png (/output by default), then re-validates the
copy itself (magic bytes and dimensions) and verifies it by file size and
SHA-256 digest, printing the byte count and digest.

Python 3.13, standard library only, no network.
"""

import hashlib
import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
EXPECTED_SIZE = (1024, 1024)


def read_dimensions(path):
    """Return (width, height) from a PNG's IHDR chunk, after magic check."""
    with open(path, "rb") as fh:
        header = fh.read(8)
        if header != PNG_MAGIC:
            raise ValueError("not a PNG file: bad magic bytes")
        chunk_len = fh.read(4)
        chunk_type = fh.read(4)
        if chunk_type != b"IHDR":
            raise ValueError("not a PNG file: first chunk is not IHDR")
        ihdr = fh.read(13)
        width, height = struct.unpack(">II", ihdr[:8])
    return width, height


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def main():
    width, height = read_dimensions(SOURCE)
    if (width, height) != EXPECTED_SIZE:
        raise ValueError(
            "entry.png must be 1024x1024, got %dx%d" % (width, height)
        )
    source_size = os.path.getsize(SOURCE)
    source_hash = sha256_of(SOURCE)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)

    # Re-validate the copy itself: a truncated or corrupted write must
    # fail here, not pass on size/digest luck alone.
    dest_width, dest_height = read_dimensions(dest)
    if (dest_width, dest_height) != EXPECTED_SIZE:
        raise ValueError(
            "copied entry.png must be 1024x1024, got %dx%d"
            % (dest_width, dest_height)
        )

    dest_size = os.path.getsize(dest)
    dest_hash = sha256_of(dest)
    if dest_size != source_size or dest_hash != source_hash:
        raise ValueError("copy verification failed: size or SHA-256 mismatch")
    print("wrote %s (%d bytes, sha256 %s)" % (dest, dest_size, dest_hash))
    return 0


if __name__ == "__main__":
    sys.exit(main())
