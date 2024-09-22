const express = require('express');
const countStudents = require('./3-read_file_async');

const database = process.argv[2];
const port = 1245;
const app = express();
module.exports = app;

app.get('/', (req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  res.write('This is the list of our students\n');
  countStudents(database).then((data) => {
    res.end(data.join('\n'));
  }).catch((error) => {
    res.end(`${error.message}`);
  });
});

app.listen(port);
