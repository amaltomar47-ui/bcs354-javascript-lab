/*
  INVERTIS UNIVERSITY, BAREILLY
  B.Tech CSE - Second Year | JavaScript Programming Lab (BCS354)
  Assignment 14: Timers and Intervals - Task 2
  Student Name: Amal Tomar
  Roll Number: 2510303070
*/

const timerId = setTimeout(() => {
    console.log("Not shown");
}, 1000);

clearTimeout(timerId);
console.log("Cancelled");
