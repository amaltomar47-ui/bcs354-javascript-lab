/*
  INVERTIS UNIVERSITY, BAREILLY
  B.Tech CSE - Second Year | JavaScript Programming Lab (BCS354)
  Assignment 8: Inheritance, Methods and Composition - Task 2
  Student Name: Amal Singh Tomar
  Roll Number: 2510303070
*/

class Locker {
    constructor() {
        this.pin = 1234;
    }

    checkPin(number) {
        return number === this.pin;
    }
}

const myLocker = new Locker();
console.log(myLocker.checkPin(1111));
console.log(myLocker.checkPin(1234));
