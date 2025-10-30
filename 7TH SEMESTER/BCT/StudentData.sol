// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {
    // Structure to store student details
    struct Student {
        uint id;
        string name;
        uint age;
        string course;
    }

    // Dynamic array to store students
    Student[] public students;

    // Event to log student addition
    event StudentAdded(uint id, string name, uint age, string course);

    // Function to add a new student
    function addStudent(
        uint _id,
        string memory _name,
        uint _age,
        string memory _course
    ) public {
        students.push(Student(_id, _name, _age, _course));
        emit StudentAdded(_id, _name, _age, _course);
    }

    // Function to get total number of students
    function getStudentCount() public view returns (uint) {
        return students.length;
    }

    // Function to get student details by index
    function getStudent(uint index) public view returns (uint, string memory, uint, string memory) {
        require(index < students.length, "Invalid index");
        Student memory s = students[index];
        return (s.id, s.name, s.age, s.course);
    }

    // Fallback function (triggered if non-existing function is called)
    fallback() external payable {
        // Accept Ether silently
    }

    // Receive function to accept plain Ether transfers
    receive() external payable {}

  
}
