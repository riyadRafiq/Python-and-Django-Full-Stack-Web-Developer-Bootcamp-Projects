var firstName = prompt("Enter your First Name: ")
var lastName = prompt("Enter your Last Name: ")
var age = prompt("Enter your Age: ")
var height = prompt("Enter your Height: ")
var petName = prompt("Enter your pet's name: ")

alert("Thank you for your information!")

if(firstName[0]==lastName[0] && (age<30 && age>20) && height>=170 && petName[petName.length - 1]=="y") {
  console.log("Welcome Comrade! You've passed the Spy Test.");
}
else {
  console.log("Sorry, nothing to see here.");
}
