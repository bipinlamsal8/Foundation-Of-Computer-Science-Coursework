"""
jwt_demo.py --- JWT SECURITY DEMONSTRATION
this script demonstrates the security properties of JSON Web Tokens (JWTs). It shows how JWTs
"""

import base64
import json
import hmac
import hashlib

print("=" * 60)
print("TASK 1: JWT SECURITY DEMONSTRATION")
print("=" * 60)


                            # STEP 1: Create a JWT Token

print("\n[STEP 1] SERVER CREATES JWT TOKEN")
print("-" * 60)

server_secret = "super_secret_key_known_only_to_server"

header  = {"alg": "HS256", "typ": "JWT"}
payload = {
    "username": "admin",
    "role":     "administrator",
    "email":    "admin@college.edu"
}

def base64url_encode(data):
    json_bytes    = json.dumps(data, separators=(',', ':')).encode()
    b64           = base64.urlsafe_b64encode(json_bytes)
    return b64.rstrip(b'=').decode()

def create_signature(header_enc, payload_enc, secret):
    message   = f"{header_enc}.{payload_enc}".encode()
    signature = hmac.new(secret.encode(), message, hashlib.sha256).digest()
    b64       = base64.urlsafe_b64encode(signature)
    return b64.rstrip(b'=').decode()

header_enc    = base64url_encode(header)
payload_enc   = base64url_encode(payload)
signature_enc = create_signature(header_enc, payload_enc, server_secret)

jwt_token = f"{header_enc}.{payload_enc}.{signature_enc}"

print(f"\n  Payload created  : {json.dumps(payload)}")
print(f"\n  JWT Token generated:")
print(f"  {jwt_token}")


                                    # STEP 2: Attacker Decodes Payload WITHOUT Secret Key

print("\n[STEP 2] ATTACKER INTERCEPTS AND DECODES TOKEN")
print("-" * 60)
print("\n  Attacker splits token by '.' separator:")

parts = jwt_token.split('.')
print(f"\n  Part 1 (Header)   : {parts[0]}")
print(f"  Part 2 (Payload)  : {parts[1]}")
print(f"  Part 3 (Signature): {parts[2]}")

                                            # Decode payload without any key
padding        = 4 - len(parts[1]) % 4
decoded_bytes  = base64.urlsafe_b64decode(parts[1] + "=" * padding)
decoded_payload = json.loads(decoded_bytes)

print(f"\n  Attacker decodes Part 2 WITHOUT any key:")
print(f"  Result: {json.dumps(decoded_payload, indent=4)}")
print(f"\n  USERNAME : {decoded_payload['username']}")
print(f"  ROLE     : {decoded_payload['role']}")
print(f"  EMAIL    : {decoded_payload['email']}")
print("\n  CONCLUSION: Full payload readable with ZERO cryptographic knowledge.")
print("  Base64URL is encoding — NOT encryption.")


                                # STEP 3: Attacker Tries to Tamper with Token

print("\n[STEP 3] ATTACKER TRIES TO TAMPER WITH TOKEN")
print("-" * 60)

tampered_payload        = {"username": "admin", "role": "superuser", "email": "admin@college.edu"}
tampered_payload_enc    = base64url_encode(tampered_payload)
fake_signature          = "fakesignatureattemptedbyhacker"
tampered_token          = f"{header_enc}.{tampered_payload_enc}.{fake_signature}"

print(f"\n  Attacker changes role from 'administrator' to 'superuser'")
print(f"  Tampered token: {tampered_token}")

                                                # Verify signature
expected_sig = create_signature(header_enc, tampered_payload_enc, server_secret)
is_valid     = hmac.compare_digest(fake_signature, expected_sig)

print(f"\n  Server verifies signature...")
print(f"  Signature valid: {is_valid}")
print(f"\n  CONCLUSION: Tampering detected — HMAC signature prevents modification.")
print("  BUT the original payload was already fully readable before tampering.")


                                            # SUMMARY

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print("  JWT provides INTEGRITY (via HMAC signature)")
print("  JWT does NOT provide CONFIDENTIALITY (payload is Base64URL)")
print("  Anyone intercepting a JWT can read: username, role, email")
print("  Solution: Always transmit JWT over HTTPS (TLS)")
print("  For payload confidentiality: use JWE (RFC 7516)")
print("\n  Source: Perez-Botero et al. (2021), RFC 7519 (Jones et al., 2015)")
print("=" * 60)
