/*
  INVERTIS UNIVERSITY, BAREILLY
  B.Tech CSE - Second Year | JavaScript Programming Lab (BCS354)
  Assignment 7: Constructor Functions and Classes - Task 1
  Student Name: Amal Tomar
  Roll Number: 2510303070
*/

function Student(name, marks) {
    this.name = name;
    this.marks = marks;
}

const s1 = new Student("Asha", 88);
console.log(s1.name);
console.log(s1.marks);
