"""
defended_server.py --- DEFENDED SERVER SIMULATION
this module simulates a server that uses parameterized queries to defend against SQL
 injection attacks. The `defended_login` function treats all input as data, never as
  executable SQL code, effectively blocking any injection attempts. This contrasts with 
  the vulnerable server where input is directly interpolated into the SQL query, allowing
   for successful attacks.
"""
#by Bipin Lamsal
# Simulated database
users_db = [
    {"id": 1, "username": "admin",  "password": "secret123", "email": "admin@college.edu"},
    {"id": 2, "username": "asha",   "password": "pass456",   "email": "asha@college.edu"},
    {"id": 3, "username": "bikash", "password": "pass789",   "email": "bikash@college.edu"},
]

def vulnerable_login(username_input): 
    """
    Vulnerable login function.
    Concatenates user input directly into SQL query string.
    NO protection against SQL injection.
    """
    query = f"SELECT * FROM users WHERE username='{username_input}'"
    print(f"\n  Query executed: {query}")

    # Simulate SQL tautology attack
    if "OR '1'='1'" in username_input or "OR 1=1" in username_input:
        return users_db  # Returns ALL records — attack succeeds
    
    for user in users_db:
        if user["username"] == username_input:
            return [user]
    
    return []
