const fs = require('fs');

function countStudents(path) {
  try {
    const lines = fs.readFileSync(path, { encoding: 'utf8' }).split(/\r?\n/);
    let countStudents = 0;
    const fields = {};

    for (let i = 1; i < lines.length; i += 1) {
      const line = lines[i].trim();
      if (line !== '') {
        countStudents += 1;
        const [fname, , , field] = line.split(',');
        if (!fields[field]) {
          fields[field] = {
            countField: 1,
            students: [fname],
          };
        } else {
          fields[field].countField += 1;
          fields[field].students.push(fname);
        }
      }
    }
    console.log(`Number of students: ${countStudents}`);
    for (const field of Object.keys(fields)) {
      const n = fields[field].countField;
      const names = fields[field].students.join(', ');
      console.log(`Number of students in ${field}: ${n}. List: ${names}`);
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
