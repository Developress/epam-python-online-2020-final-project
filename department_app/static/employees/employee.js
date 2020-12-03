// declare the needed globals, id - for the id of employee being edited,
// add - to indicate whether the employee is being adding or editing
let id = 0;
let add = true;

createDropDownList();

if(document.title === "Edit Employee"){
    add = false;
    // get the id, which will be the last element of url
    id = document.URL.substring(document.URL.lastIndexOf('/') + 1);
    // perform a GET request to receive the needed department
    fetch(`http://localhost:5000/api/employees/${id}`)
        .then((response) => response.json())
        .then((data)=> {
            // set the input values
            setValues(data);
        })
        .catch((error) => console.log(error))
}

function setValues(data){
    // get the name input and set a value to it
    let name = document.getElementById('name');
    name.setAttribute('value', data['name']);
    // get the surname input and set a value to it
    let surname = document.getElementById('surname');
    surname.setAttribute('value', data['surname']);
    // set the selected element of dropdown list
    let departments = getDepartmentList(data);
    for(const department in departments){
        if(department['name'] === data['department']){
            document.getElementById('department').value = department['id'];
            break;
        }
    }
    // get the salary input and set a value to it
    let salary = document.getElementById('salary');
    salary.setAttribute('value', data['salary']);
    // get the date of birth input and set a value to it
    let date_of_birth = document.getElementById('datepicker');
    date_of_birth.value = data['date_of_birth'];
    console.log(date_of_birth.value)
}

function createDropDownList(){
    // get all the departments
    fetch("http://localhost:5000/api/departments")
    .then((response) => response.json())
    .then((data)=> {
        let departments = getDepartmentList(data);
        let select = document.getElementById('department');
        for (const department of departments) {
            var option = document.createElement("option");
            option.value = department['id'];
            option.text = department['name']
            select.appendChild(option);
        }
    })
    .catch((error) => console.log(error))
}

function getDepartmentList(data){
    let departments = [];
    for(let i = 0; i < data.length; i++){
        let object = data[i];
        let department = {
            'id': object['id'],
            'name': object['name']
        }
        departments.push(department)
    }
    return departments;
}

function onSubmitClicked(){
    // get the inputs
    let name = document.getElementById('name');
    let surname = document.getElementById('surname');
    let department = document.getElementById('department');
    let salary = document.getElementById('salary');
    let date_of_birth = document.getElementById('datepicker');
    // form a body for post or put request
    if (department.value === ''){
        department.setAttribute('value', null)
    }
    data = {
        'name': name.value,
        'surname': surname.value,
        'department': department.value,
        'salary': salary.value,
        'date_of_birth': date_of_birth.value
    }
    console.log(data)
    // if we are adding the element
    if(add){
        fetch(`http://localhost:5000/api/employees`, {
                method: 'POST',
                headers: {
                  'Accept': 'application/json',
                  'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
            .then((response) => response.json())
            .then((data)=> {
                // redirect to another page
                window.location = '/employees/add?added=' + true;
            })
            .catch((error) => console.log(error))
    } else {
        fetch(`http://localhost:5000/api/employees/${id}`, {
                method: 'PUT',
                headers: {
                  'Accept': 'application/json',
                  'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
            .then((response) => response.json())
            .then((data)=> {
                // redirect to another page
                window.location = `/employees/edit/${id}?edited=` + true;
            })
            .catch((error) => console.log(error))
    }
}