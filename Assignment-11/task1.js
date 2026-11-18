/*
  INVERTIS UNIVERSITY, BAREILLY
  B.Tech CSE - Second Year | JavaScript Programming Lab (BCS354)
  Assignment 11: Scope and Closures - Task 1
  Student Name: Amal Tomar
  Roll Number: 2510303070
*/

let level = "outer";

{
    let level = "inner";
    console.log(level);
}

console.log(level);
