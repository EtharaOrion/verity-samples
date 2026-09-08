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
covers_canonical_payload_hash: sha256:1bfad44820e503606a18996df238b5d9607d51f912ad8975eb87f95d23d18da8
covers_canonical_bundle_hash: 932601ccc184a4152137df5c9837fe9e0a3e72d7c518eb06c8d5d60a10dc9826
covers_pinned_image_digest: verity-algoperf@sha256:e3bd3156e388c84ba8f2909dc757042c01e18a52b2dfbeb6a350f2b5e6c26a05
gap: attestation-unavailable
