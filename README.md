# Foundation of Computer Science - ST4015CMD
**Softwarica College of IT & E-Commerce | In Collaboration with Coventry University**

**Student:** Bipin Lamsal
**Student ID:** 250510
**Programme:** BSc (Hons) Ethical Hacking and Cybersecurity
**Module:** ST4015CMD - Foundations of Computer Science
**Submitted to:** Rupak Rajbanshi Sir

---

## Repository Structure

```
Foundation-Of-Computer-Science-Coursework/
│
├── Task-1/
│   ├── Screenshots/                         # Diagrams used in the report
│   ├── attack_ran_demo__JWT_demo_screenshots/ # Output screenshots from running the scripts
│   ├── Dockerfile                           # Docker setup for running all scripts
│   ├── attack_runner.py                     # Runs both SQL injection attacks
│   ├── defended_server.py                   # Parameterized query defence simulation
│   ├── vulnerable_server.py                 # Vulnerable server simulation
│   ├── jwt_demo.py                          # JWT and Base64 security demonstration
│   ├── test_security.py                     # Automated security tests
│   └── requirements.txt                     # Python dependencies
│
├── Task-2/
│   └── Images/
│       ├── Brute Force Steps and Heuristic Steps.png
│       ├── Factorial Growth.png
│       ├── HEURISTIC ALGORITHM FOR CLASSROOM SEATING.png
│       └── Time (Seconds Approx.) vs Students.png
│
└── Task-3/
    ├── images/                              # ER diagram and MySQL screenshots
    └── schema.sql                           # Full MySQL schema with constraints and queries
```

---

## Task 1 - Secure Data Exchange with Encoding Formats

### What it covers
- Evaluation of Base64, URL encoding, ASCII, and hexadecimal encoding formats
- How encoding is used in HTTP, SMTP, TLS, OAuth, and JWT
- SQL injection attacks using encoded payloads
- Double encoding and XSS through encoding
- Proposed defence strategy using parameterized queries and layered security

### What the scripts do

| File | Description |
|---|---|
| `vulnerable_server.py` | Simulates a server that concatenates user input directly into SQL queries |
| `defended_server.py` | Simulates a server that uses parameterized queries to block injection |
| `attack_runner.py` | Runs Attack 1 (encoding only) and Attack 2 (with parameterized queries) and shows results |
| `jwt_demo.py` | Demonstrates how JWT tokens use Base64URL and why the payload is not hidden |
| `test_security.py` | Automated tests that verify vulnerable server leaks data and defended server blocks all attacks |

### How to run with Docker

**Pull the image from Docker Hub:**
```bash
docker pull bipin819/foundation-task1:latest
```

**Run the SQL injection demonstration:**
```bash
docker run bipin819/foundation-task1:latest
```

**Run the JWT demonstration:**
```bash
docker run bipin819/foundation-task1:latest python3 jwt_demo.py
```

**Run the automated security tests:**
```bash
docker run bipin819/foundation-task1:latest python3 test_security.py
```

### How to run locally without Docker

Make sure Python 3 is installed, then:

```bash
cd Task-1
python3 attack_runner.py
python3 jwt_demo.py
python3 test_security.py
```

### How to build Docker image yourself

```bash
cd Task-1
docker build -t foundation-task1 .
docker run foundation-task1
```

### CI/CD

This repository uses GitHub Actions. On every push to main:
1. Python tests run automatically
2. Docker image is built
3. All scripts run inside the container
4. Docker image is pushed to Docker Hub

---

## Task 2 - Classroom Seating Arrangement Problem (P vs NP)

### What it covers
- Explanation of P and NP problems using the classroom seating scenario
- Why checking an arrangement is O(n) but finding one requires n! steps
- Brute force approach and why it fails beyond 12 students
- Greedy heuristic approach that reduces complexity to O(n²)
- Critical reflection on the gap between theoretical and practical complexity

### Diagrams

| File | Description |
|---|---|
| `Factorial Growth.png` | Shows how n! grows as student count increases |
| `Time (Seconds Approx.) vs Students.png` | Shows time required for brute force at each class size |
| `HEURISTIC ALGORITHM FOR CLASSROOM SEATING.png` | Flowchart of the heuristic strategy |
| `Brute Force Steps and Heuristic Steps.png` | Comparison of steps required by each approach |

---

## Task 3 - College Club Membership Database

### What it covers
- Identifying data problems in an unnormalised flat table
- Normalisation through 1NF, 2NF, and 3NF
- Boyce-Codd Normal Form (BCNF) analysis
- Entity Relationship (ER) diagram
- Full MySQL implementation with constraints, CASCADE rules, and indexes
- SQL JOIN query to display student and club membership data

### How to run the SQL schema

**Using Docker with MySQL:**
```bash
docker run --name mysql-task3 -e MYSQL_ROOT_PASSWORD=root -d mysql:8.0
docker exec -i mysql-task3 mysql -uroot -proot < Task-3/schema.sql
```

**Using MySQL directly:**
```bash
mysql -u root -p < Task-3/schema.sql
```

**The schema.sql file includes:**
- CREATE TABLE statements for Student, Club, and Membership
- FOREIGN KEY constraints with CASCADE rules
- UNIQUE constraints on Email and ClubName
- Indexes for JOIN performance
- INSERT statements for all sample data
- SELECT queries including the three-table JOIN

---

## Key Findings

**Task 1:** Encoding formats provide zero security. Base64-encoded SQL injection payloads bypass Web Application Firewalls 73% of the time. Parameterized queries block 100% of attacks regardless of encoding.

**Task 2:** At 20 students, brute force requires 77,000 years. The greedy heuristic solves the same problem in under a second by reducing complexity from O(n! × n) to approximately O(n²).

**Task 3:** Normalisation eliminates all update, insert, and deletion anomalies. After normalisation, every fact exists in exactly one place, making data inconsistency structurally impossible.

---

## Docker Hub

The Task 1 image is publicly available:
```
docker pull bipin819/foundation-task1:latest
```

---

## References

Key academic sources used across all three tasks:

- Josefsson, S. (2006). RFC 4648 — Base64 encoding
- Olatunji et al. (2020). SQL injection detection and prevention
- Muttaqin et al. (2020). Parameterized query defence
- Sipser, M. (2013). Introduction to the Theory of Computation
- Garey & Johnson (1979). Computers and Intractability
- Codd, E. F. (1970). A Relational Model of Data
- Silberschatz et al. (2019). Database System Concepts

Full reference list is available in the submitted report.
