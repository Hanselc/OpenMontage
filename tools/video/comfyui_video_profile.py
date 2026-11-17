"""Bridge to the workspace-local ComfyUI profile provider.

OpenMontage's normal registry discovery imports this module and registers the
subclass below. The implementation, profiles, and workflows live under
``<workspace>/src/providers/video_generation/``.
"""

from __future__ import annotations

import sys
from pathlib import Path

_WORKSPACE = Path(__file__).resolve().parents[3]
if str(_WORKSPACE) not in sys.path:
    sys.path.insert(0, str(_WORKSPACE))

try:
    from src.providers.video_generation.comfyui import (
        ComfyUIVideoProfile as _LocalComfyUIVideoProfile,
    )
except Exception:  # pragma: no cover - keep OpenMontage usable without the workspace
    _LocalComfyUIVideoProfile = None


if _LocalComfyUIVideoProfile is not None:

    class ComfyUIVideoProfile(_LocalComfyUIVideoProfile):
        """Local ComfyUI profile provider discovered as a normal OpenMontage tool."""

        pass
