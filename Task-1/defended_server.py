"""
defended_server.py --- DEFENDED SERVER SIMULATION
this module simulates a server that is protected against SQL injection attacks using 
parameterized queries. The defended_login function treats all input as data, never as 
executable SQL code, effectively blocking any injection attempts. This contrasts with
 the vulnerable server where input is directly interpolated into SQL statements, allowing
  for successful attacks. The users_db simulates a simple user database for demonstration
   purposes.
"""

# Simulated database
users_db = [
    {"id": 1, "username": "admin",  "password": "secret123", "email": "admin@college.edu"},
    {"id": 2, "username": "asha",   "password": "pass456",   "email": "asha@college.edu"},
    {"id": 3, "username": "bikash", "password": "pass789",   "email": "bikash@college.edu"},
]

def defended_login(username_input):
    """
    Defended login function.
    Uses parameterized query simulation.
    Input is treated as a typed data value, never interpreted as SQL syntax.
    Equivalent to: SELECT * FROM users WHERE username = ?
    """
    print(f"\n  Parameterized query: SELECT * FROM users WHERE username = ?")
    print(f"  Binding value as data: '{username_input}'")

    # Input is treated as pure data - exact string match only
    for user in users_db:
        if user["username"] == username_input:
            return [user]
    
    return []  # SQL injection payload never matches any real username
