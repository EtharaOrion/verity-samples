# Detached signature over the canonical payload. UNSIGNED.
#
# Item 10i requires an external signature naming a signer and verifying against an outside trust
# root. No signer exists: seed/pilot.yaml records that the workflow holding the private half does
# not exist. This file records what would be signed and states plainly that nothing signed it, so
# the absence is resolvable from the delivered unit rather than inferred from a missing file.
# Without a valid signature the producer claim is not authenticated and the bundle caps at
# HOLD:PILOT_REQUIRED, which is where the shakedown ceiling already sits.
signature_state: absent
signer: none
trust_root: none
covers_canonical_payload_hash: sha256:7d26c0d6bfe9d2000142a3d0d0ff948e8e0db42f833047317e5ab3b9a9a873b6
covers_canonical_bundle_hash: 8f30156b9112e8686f7aa3d723d3d16f44fa395b4f34c3230a46580bd8d8516f
covers_pinned_image_digest: verity-algoperf@sha256:e3bd3156e388c84ba8f2909dc757042c01e18a52b2dfbeb6a350f2b5e6c26a05
gap: attestation-unavailable
