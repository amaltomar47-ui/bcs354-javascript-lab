/*
  INVERTIS UNIVERSITY, BAREILLY
  B.Tech CSE - Second Year | JavaScript Programming Lab (BCS354)
  Assignment 6: JSON Text - Task 1
  Student Name: Amal Tomar
  Roll Number: 2510303070
*/

const student = {
    name: "Rohan",
    marks: [70, 80]
};

const jsonText = JSON.stringify(student);
console.log(jsonText);
