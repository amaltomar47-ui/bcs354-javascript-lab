/*
  INVERTIS UNIVERSITY, BAREILLY
  B.Tech CSE - Second Year | JavaScript Programming Lab (BCS354)
  Assignment 9: DOM, Validation, Storage and Quiz - Task 4
  Student Name: Amal Singh Tomar
  Roll Number: 2510303070
*/

// Question: What is 2 + 3?
function checkQuizAnswer(chosenAnswer) {
    if (chosenAnswer === 5) {
        return "Correct";
    } else {
        return "Try again";
    }
}

console.log("Checking answer 4:", checkQuizAnswer(4));
console.log("Checking answer 5:", checkQuizAnswer(5));
console.log("Checking answer 6:", checkQuizAnswer(6));
