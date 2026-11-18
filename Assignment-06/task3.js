/*
  INVERTIS UNIVERSITY, BAREILLY
  B.Tech CSE - Second Year | JavaScript Programming Lab (BCS354)
  Assignment 6: JSON Text - Task 3
  Student Name: Amal Singh Tomar
  Roll Number: 2510303070
*/

const invalidJson = "{name: Rohan}";

try {
    JSON.parse(invalidJson);
} catch (error) {
    console.log("Invalid JSON");
}
