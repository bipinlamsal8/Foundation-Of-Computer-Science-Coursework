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
