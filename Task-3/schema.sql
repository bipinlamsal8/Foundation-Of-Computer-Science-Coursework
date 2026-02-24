--Task 3: College Club Membership Management sql schema

-- Create Student table
CREATE TABLE Student (
    StudentID   INT          PRIMARY KEY,
    StudentName VARCHAR(100) NOT NULL,
    Email       VARCHAR(100) NOT NULL UNIQUE
); 

-- Create Club table
CREATE TABLE Club (
    ClubID     INT          PRIMARY KEY,
    ClubName   VARCHAR(100) NOT NULL UNIQUE,
    ClubRoom   VARCHAR(50),
    ClubMentor VARCHAR(100)
);

-- Create Membership table
CREATE TABLE Membership (
    MembershipID INT  PRIMARY KEY,
    StudentID    INT  NOT NULL,
    ClubID       INT  NOT NULL,
    JoinDate     DATE NOT NULL,
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID)
        ON DELETE CASCADE  
        ON UPDATE CASCADE, 
    FOREIGN KEY (ClubID) REFERENCES Club(ClubID)
        ON DELETE CASCADE
        ON UPDATE CASCADE, 
    UNIQUE (StudentID, ClubID) 
);

-- Create indexes for JOIN performance
CREATE INDEX idx_membership_student ON Membership(StudentID);
CREATE INDEX idx_membership_club    ON Membership(ClubID);

-- Insert Students
INSERT INTO Student VALUES (1, 'Asha',   'asha@email.com');
INSERT INTO Student VALUES (2, 'Bikash', 'bikash@email.com');
INSERT INTO Student VALUES (3, 'Nisha',  'nisha@email.com');
INSERT INTO Student VALUES (4, 'Rohan',  'rohan@email.com');
INSERT INTO Student VALUES (5, 'Suman',  'suman@email.com');
INSERT INTO Student VALUES (6, 'Pooja',  'pooja@email.com');
INSERT INTO Student VALUES (7, 'Aman',   'aman@email.com'); 

-- Insert Clubs
INSERT INTO Club VALUES (1, 'Music Club',  'R101', 'Mr. Raman');
INSERT INTO Club VALUES (2, 'Sports Club', 'R202', 'Ms. Sita');
INSERT INTO Club VALUES (3, 'Drama Club',  'R303', 'Mr. Kiran');
INSERT INTO Club VALUES (4, 'Coding Club', 'Lab1', 'Mr. Anil');

-- Insert Memberships
INSERT INTO Membership VALUES (1,  1, 1, '2024-01-10');
INSERT INTO Membership VALUES (2,  2, 2, '2024-01-12');
INSERT INTO Membership VALUES (3,  1, 2, '2024-01-15');
INSERT INTO Membership VALUES (4,  3, 1, '2024-01-20');
INSERT INTO Membership VALUES (5,  4, 3, '2024-01-18');
INSERT INTO Membership VALUES (6,  5, 1, '2024-01-22');
INSERT INTO Membership VALUES (7,  2, 3, '2024-01-25');
INSERT INTO Membership VALUES (8,  6, 2, '2024-01-27');
INSERT INTO Membership VALUES (9,  3, 4, '2024-01-28');
INSERT INTO Membership VALUES (10, 7, 4, '2024-01-30');

-- Required Operations

-- 1. Insert a new student
INSERT INTO Student VALUES (8, 'Riya', 'riya@email.com');

-- 2. Insert a new club
INSERT INTO Club VALUES (5, 'Art Club', 'R404', 'Ms. Priya');

-- 3. Display all students
SELECT * FROM Student;

-- 4. Display all clubs
SELECT * FROM Club;

-- 5. Display all memberships
SELECT * FROM Membership;

-- SQL JOIN Query

SELECT
    s.StudentName,
    c.ClubName,
    m.JoinDate
FROM Membership m
JOIN Student s ON m.StudentID = s.StudentID
JOIN Club c    ON m.ClubID   = c.ClubID
ORDER BY s.StudentName;
