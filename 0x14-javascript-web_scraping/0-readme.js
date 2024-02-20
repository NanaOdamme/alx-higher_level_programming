#!/usr/bin/node

const fs = require('fs');
const fileName = process.argv[2];

if (process.argv.length !== 3) {
  console.error('Usage: node read-file.js <file-name>');
  process.exit(1);
}

fs.readFile(fileName, 'utf-8', (err, data) => {
  if (err) {
 reading
    console.error(err);
  } else {
    console.log(data);
  }
});
