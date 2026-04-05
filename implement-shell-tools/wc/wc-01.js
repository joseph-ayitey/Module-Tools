const fs = require("fs");

const args = process.argv.slice(2);

let flagL = false;
let flagW = false;
let flagC = false;
const files = [];

for (const arg of args) {
  if (arg === "-l") flagL = true;
  else if (arg === "-w") flagW = true;
  else if (arg === "-c") flagC = true;
  else files.push(arg);
}

const noFlags = !flagL && !flagW && !flagC;

let totalLines = 0;
let totalWords = 0;
let totalBytes = 0;

for (const file of files) {
  const content = fs.readFileSync(file, "utf-8");
  const bytes = fs.statSync(file).size;
  const lines = content.split("\n").length - 1;
  const words = content.split(/\s+/).filter(w => w !== "").length;

  totalLines += lines;
  totalWords += words;
  totalBytes += bytes;

  const parts = [];
  if (flagL || noFlags) parts.push(String(lines).padStart(8));
  if (flagW || noFlags) parts.push(String(words).padStart(8));
  if (flagC || noFlags) parts.push(String(bytes).padStart(8));
  parts.push(" " + file);

  console.log(parts.join(""));
}

if (files.length > 1) {
  const parts = [];
  if (flagL || noFlags) parts.push(String(totalLines).padStart(8));
  if (flagW || noFlags) parts.push(String(totalWords).padStart(8));
  if (flagC || noFlags) parts.push(String(totalBytes).padStart(8));
  parts.push(" total");

  console.log(parts.join(""));
}