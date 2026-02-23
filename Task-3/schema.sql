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