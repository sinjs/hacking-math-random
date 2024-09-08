import readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";

const rl = readline.createInterface({ input, output });

console.log("Number Guessing Game");

console.log(
  "The game will print 5 numbers and you will have to guess the next number in the sequence. If you get the number right you win the game!"
);

console.log("\nYour lucky numbers are:");

const initialLuckyNumbers = Array.from(Array(5), Math.random);

for (const luckyNumber of initialLuckyNumbers) {
  console.log(luckyNumber);
}

console.log("\nNow, time to guess the next number!");

const numberGuess = await rl
  .question("What is the next lucky number? ")
  .then((response) => parseFloat(response));

rl.close();

if (Number.isNaN(numberGuess)) {
  console.error("Error: You entered an invalid number!");
  process.exit(1);
}

const nextLuckyNumber = Math.random();

if (numberGuess !== nextLuckyNumber) {
  console.error(
    "\nThat's the wrong number, the correct number was",
    nextLuckyNumber
  );
  process.exit(1);
}

console.log('\nGood job and nice "guess", you won the game!');
