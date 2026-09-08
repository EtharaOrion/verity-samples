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
covers_canonical_payload_hash: sha256:37f1a307ac591fa5668eab5a47f671cc648951b64dca79b4dcbe5d74eaf78a0c
covers_canonical_bundle_hash: 08ee013e26877a4d2a6029c7c357d25d0654677c6fa2192ad9f100aae4e4747d
covers_pinned_image_digest: verity-algoperf@sha256:e3bd3156e388c84ba8f2909dc757042c01e18a52b2dfbeb6a350f2b5e6c26a05
gap: attestation-unavailable
