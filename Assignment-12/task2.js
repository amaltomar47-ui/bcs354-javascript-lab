/*
  INVERTIS UNIVERSITY, BAREILLY
  B.Tech CSE - Second Year | JavaScript Programming Lab (BCS354)
  Assignment 12: Callbacks and Higher-Order Functions - Task 2
  Student Name: Amal Tomar
  Roll Number: 2510303070
*/

function formatMarks(marks, callback) {
    return callback(marks);
}

console.log(formatMarks(76, (marks) => `Marks: ${marks}/100`));
