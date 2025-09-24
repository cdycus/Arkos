📝 Changed Files in This Patch
🆕 New Files:

spine/crypto/identity.py — sovereign signature utility with HMAC signing

spine/crypto/skippy_secret.key — root key used for payload signing

🧾 Release Notes (Patch 6 - Sovereign Identity Propagation)
✨ New Features:

Introduced identity propagation logic via sign_payload() and verify_signature().

Secret key is stored locally (development mode) and used for HMAC SHA-256 signing.

Ensures all outbound Skippy communications can be verified as sovereign-originated.

✅ Git Commit Notes