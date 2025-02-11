#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2]; // Get the file path from the command-line argument

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
