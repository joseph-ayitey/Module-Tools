const fs = require("fs");

const args = process.argv.slice(2);

let flagN = false;
let flagB = false;
const files = [];

for (const arg of args) {
  if (arg === "-n") flagN = true;
  else if (arg === "-b") flagB = true;
  else files.push(arg);
}

let lineNumber = 1;

for (const file of files) {
  const content = fs.readFileSync(file, "utf-8");
  const lines = content.split("\n");

  // readFileSync adds a trailing \n which creates an extra empty line
  if (lines[lines.length - 1] === "") lines.pop();

  for (const line of lines) {
    if (flagB) {
      if (line === "") {
        console.log("");
      } else {
        console.log(`     ${lineNumber}\t${line}`);
        lineNumber++;
      }
    } else if (flagN) {
      console.log(`     ${lineNumber}\t${line}`);
      lineNumber++;
    } else {
      console.log(line);
    }
  }
}