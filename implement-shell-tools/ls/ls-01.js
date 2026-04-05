const fs = require("fs");

const args = process.argv.slice(2);

let flagA = false;
let dir = ".";

for (const arg of args) {
  if (arg === "-a") flagA = true;
  else if (arg === "-1") continue;//always list one per line
  else dir = arg;
}

const entries = fs.readdirSync(dir);

for (const entry of entries.sort()) {
  if (!flagA && entry.startsWith(".")) continue;
  console.log(entry);
}