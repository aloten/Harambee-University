function addStudent() {
  const form = document.forms['newStudent'];
  const firstName = form.querySelector('input[name="firstName"]').value;
  const lastName = form.querySelector('input[name="lastName"]').value;
  const classYear = form.querySelector('input[name="classYear"]').value;

  const url = '/addStudent';
  const newStudent = {
    firstName,
    lastName,
    classYear,
  };

  const options = {
    method: 'POST',
    body: JSON.stringify(newStudent),
    headers: {
      'Content-Type': 'application/json',
    },
  };

  fetch(url, options)
    .then((res) => res.json())
    .then((res) => console.log(res));
  getStudents();
}

async function getStudents() {
  const url = '/students';
  let res = await fetch(url);
  let json = await res.json();
  let students = json.students;

  console.log(students);
  const studentsDiv = document.querySelector('.students');

  for (student of students) {
    const studentEl = document.createElement('div');
    studentEl.innerHTML = `${student.id}, ${student.f_name}, ${student.l_name}`;
    studentsDiv.appendChild(studentEl);
  }
}

getStudents();
