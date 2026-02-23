--Task 3: College Club Membership Management sql schema

-- Create Student table
CREATE TABLE Student (
    StudentID   INT          PRIMARY KEY,
    StudentName VARCHAR(100) NOT NULL,
    Email       VARCHAR(100) NOT NULL UNIQUE
); 