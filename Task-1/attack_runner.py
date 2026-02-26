"""
TASK 1: SQL INJECTION ATTACK DEMONSTRATION
this script simulates two attacks on a vulnerable and a defended server using the
 same SQL injection payload. It shows how base64 encoding fails to protect against
  SQL injection, while parameterized queries successfully block the attack. The
   results are printed in a clear format for easy comparison.
"""

import base64
from vulnerable_server import vulnerable_login
from defended_server import defended_login

print("=" * 60)
print("TASK 1: SQL INJECTION ATTACK DEMONSTRATION")
print("=" * 60)

                                # ATTACK 1: Base64 Encoding Only - VULNERABLE SERVER

print("\n" + "=" * 60)
print("ATTACK 1: BASE64 ENCODING ONLY — VULNERABLE SERVER")
print("=" * 60)

original_payload = "' OR '1'='1' --"
encoded_payload  = base64.b64encode(original_payload.encode()).decode()
decoded_payload  = base64.b64decode(encoded_payload).decode()

print(f"\n  Original payload : {original_payload}")
print(f"  Base64 encoded   : {encoded_payload}")
print(f"  Server decodes to: {decoded_payload}")

results = vulnerable_login(decoded_payload)

if results:
    print(f"\n  RESULT: {len(results)} rows returned — DATA LEAKED")
    for user in results:
        print(f"    → {user['username']} / {user['password']} / {user['email']}")
    print("\n  CONCLUSION: Base64 encoding provided ZERO protection.")
else:
    print("\n  RESULT: No data returned.")