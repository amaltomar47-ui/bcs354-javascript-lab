/*
  INVERTIS UNIVERSITY, BAREILLY
  B.Tech CSE - Second Year | JavaScript Programming Lab (BCS354)
  Assignment 9: DOM, Validation, Storage and Quiz - Task 1
  Student Name: Amal Singh Tomar
  Roll Number: 2510303070
*/

// Simulating DOM Heading and Button click in pure JavaScript
let headingText = "Welcome";
console.log("Initial Heading:", headingText);

function onButtonClick() {
    headingText = "Button clicked";
}

onButtonClick();
console.log("Updated Heading:", headingText);
