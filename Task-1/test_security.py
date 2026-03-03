from vulnerable_server import vulnerable_login
from defended_server import defended_login

# TEST HELPERS
passed = 0
failed = 0

def test(name, condition):
    global passed, failed
    if condition:
        print(f"  PASS: {name}")
        passed += 1
    else:
        print(f"  FAIL: {name}")
        failed += 1

# TESTS: VULNERABLE SERVER

print("=" * 55)
print("TESTING: vulnerable_server.py")
print("=" * 55)

# Normal login should work
result = vulnerable_login("admin")
test("Normal login returns one user", len(result) == 1)
test("Normal login returns correct user", result[0]["username"] == "admin")

# SQL injection should succeed (server is vulnerable)
payload = "' OR '1'='1' --"
result = vulnerable_login(payload)
test("SQL injection leaks all records", len(result) == 3)
test("Injection returns admin record", any(u["username"] == "admin" for u in result))
test("Injection returns asha record", any(u["username"] == "asha" for u in result))
test("Injection returns bikash record", any(u["username"] == "bikash" for u in result))

# Wrong username should return empty on normal query
result = vulnerable_login("nonexistent_user")
test("Unknown user returns empty result", len(result) == 0)


# TESTS: DEFENDED SERVER

print()
print("=" * 55)
print("TESTING: defended_server.py")
print("=" * 55)

# Normal login should still work
result = defended_login("admin")
test("Normal login returns one user", len(result) == 1)
test("Normal login returns correct user", result[0]["username"] == "admin")

# SQL injection should FAIL (server is defended)
payload = "' OR '1'='1' --"
result = defended_login(payload)
test("SQL injection blocked — zero records returned", len(result) == 0)

# Double encoded attack should also fail
payload2 = "%2527 OR 1=1 --"
result = defended_login(payload2)
test("Double encoded attack blocked", len(result) == 0)

# Base64 encoded payload should also fail
payload3 = "JyBPUiAnMSc9JzEnIC0t"
result = defended_login(payload3)
test("Base64 encoded attack blocked", len(result) == 0)

# Wrong username returns empty
result = defended_login("nonexistent_user")
test("Unknown user returns empty result", len(result) == 0)

# SUMMARY

print()
print("=" * 55)
print(f"RESULTS: {passed} passed  |  {failed} failed  |  {passed + failed} total")
print("=" * 55)

if failed == 0:
    print("All tests passed. Security functions working correctly.")
else:
    print(f"WARNING: {failed} test(s) failed. Review security functions.")