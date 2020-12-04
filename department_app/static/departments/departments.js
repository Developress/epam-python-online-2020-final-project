// perform a GET request to receive all the departments
fetch("/api/departments")
    .then((response) => response.json())
    .then((data)=> {
        // if the request was successful, call the function
        responseReceived(data);
    })
    .catch((error) => console.log(error))

function responseReceived(data){
    // if the department list is empty
    if(data.length == 0){
        // set set to empty element to indicate that the department list is empty
        let empty = document.getElementById("empty");
        let text = document.createTextNode("No departments were found");
        empty.appendChild(text);
    } else {
        // get the data which will be displayed in table
        let dataToDisplay = formDataToDisplay(data);
        // get the table to display data
        let table = document.querySelector("table");
        // generate table, passing the table element, table data, and table headers
        generateTable(table, dataToDisplay, Object.keys(dataToDisplay[0]), 'departments');
        // generate table head, passing the table element and table headers
        generateTableHead(table, Object.keys(dataToDisplay[0]).slice(1));
    }
}

function formDataToDisplay(data) {
    // declare an array with objects representing the table rows
    let dataToDisplay = [];
    for(let i = 0; i < data.length; i++){
        // get the element of data array
        let object = data[i];
        // get the amount of employees related to the current department
        let employeeCount = object['employees'].length;
        // declare a variable which will store the average salary of the current department
        let averageSalary = 0;
        // if employee list is not empty
        if(employeeCount > 0){
            for(let j = 0; j < object['employees'].length; j++){
                // get the employee from employee list
                employee = object['employees'][j];
                // add the employee's salary to the current sum
                averageSalary += employee['salary'];
            }
            // calculate the average salary
            averageSalary /= employeeCount;
        }
        // form an object which will be represented in table
        let department = {
            'id': object['id'],
            'Name': object['name'],
            'Description': object['description'],
            'Employee count': employeeCount,
            'Average salary': averageSalary
        }
        // push an object to the array
        dataToDisplay.push(department);
    }
    return dataToDisplay;
}

function sendDeleteRequest(id){
    // perform a DELETE request to delete the specific department
    fetch(`/api/departments/${id}`, {
            method: 'DELETE'
        })
        .then((response) => response.json())
        .then((data)=> {
            // when the response is received, redirect to the given page
            window.location.href = `/departments/delete/${id}`;
        })
        .catch((error) => console.log(error))
}