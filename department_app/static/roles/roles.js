// perform a GET request to receive all the departments
fetch("http://localhost:5000/api/departments")
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
        generateTable(table, dataToDisplay, Object.keys(dataToDisplay[0]));
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

function generateTableHead(table, headers) {
    // create the table head
    let thead = table.createTHead();
    // create the table row
    let row = thead.insertRow();
    // push edit and delete values to the headers array
    headers.push('Edit');
    headers.push('Delete');
    for (let key of headers) {
        // create a table header element and fill it with data
        let th = document.createElement("th");
        let text = document.createTextNode(key);
        th.appendChild(text);
        row.appendChild(th);
    }
}

function generateTable(table, data, keys) {
    for(let i = 0; i < data.length; i++) {
        // get the element from data array
        let element = data[i];
        // create a new row
        let row = table.insertRow();
        // start loop from 1, to omit the id property
        for(let j = 1; j < keys.length; j++) {
            // create a new cell and fill it with data
            let cell = row.insertCell();
            let text = document.createTextNode(element[keys[j]]);
            cell.appendChild(text);
        }
        // create a new cell for "Edit" link
        let cell = row.insertCell();
        let a = document.createElement("a");
        // specify the hyperlink for the element
        a.setAttribute("href", `/departments/edit/${element['id']}`);
        // bound the text of link and join the element to the table row
        let text = document.createTextNode("Edit");
        a.appendChild(text);
        cell.appendChild(a);

        // create a new cell for "Delete" link
        cell = row.insertCell();
        a = document.createElement("a");
        // sendDeleteRequest will be called on the element click
        a.setAttribute("onclick", `sendDeleteRequest(${element['id']})`)
        // to make element clickable
        a.setAttribute("href", "#");
        // bound the text of link and join the element to the table row
        text = document.createTextNode("Delete");
        a.appendChild(text);
        cell.appendChild(a);
    }
}

function sendDeleteRequest(id){
    // perform a DELETE request to delete the specific department
    fetch(`http://localhost:5000/api/departments/${id}`, {
            method: 'DELETE'
        })
        .then((response) => response.json())
        .then((data)=> {
            // when the response is received, redirect to the given page
            window.location.href = `/departments/delete/${id}`;
        })
        .catch((error) => console.log(error))
}