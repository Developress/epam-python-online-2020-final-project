// perform a GET request to receive all the employees
fetch("http://localhost:5000/api/employees")
    .then((response) => response.json())
    .then((data)=> {
        // if the request was successful, call the function
        responseReceived(data);
    })
    .catch((error) => console.log(error))

function responseReceived(data){
    // if the employee list is empty
    if(data.length === 0){
        // set set to empty element to indicate that the employee list is empty
        let empty = document.getElementById('empty');
        let text = document.createTextNode('No employees were found');
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
        // form an object which will be represented in table
        if(object['department'] === null){
            object['department'] = '-'
        }
        let employee = {
            'id': object['id'],
            'Name': object['name'],
            'Surname': object['surname'],
            'Department': object['department'],
            'Salary': object['salary'],
            'Date of birth': object['date_of_birth']
        }
        // push an object to the array
        dataToDisplay.push(employee);
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
        a.setAttribute("href", `/employees/edit/${element['id']}`);
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
    // perform a DELETE request to delete the specific employee
    fetch(`http://localhost:5000/api/employees/${id}`, {
            method: 'DELETE'
        })
        .then((response) => response.json())
        .then((data)=> {
            // when the response is received, redirect to the given page
            window.location.href = `/employees/delete/${id}`;
        })
        .catch((error) => console.log(error))
}

function getEmployeesBornOn(){
    let datepicker = document.getElementById('datepicker');
    let date = "'" + datepicker.value + "'";
    let table = document.querySelector("table");
    while (table.rows.length > 0 ) {
        table.deleteRow(0);
    }
    fetch('http://localhost:5000/api/employees?date=' + date)
        .then((response) => response.json())
        .then((data)=> {
            console.log(data);
            if (data.length > 0){
                let h1 = document.querySelector("h1");
                h1.innerHTML = "Search results";
                let dataToDisplay = formDataToDisplay(data);
                // get the table to display data
                let table = document.querySelector("table");
                // generate table, passing the table element, table data, and table headers
                generateTable(table, dataToDisplay, Object.keys(dataToDisplay[0]));
                generateTableHead(table, Object.keys(dataToDisplay[0]).slice(1));
            }

        })
        .catch((error) => console.log(error))
}

function getEmployeesBornBetween(){
    let datepicker_start = document.getElementById('start_date');
    let datepicker_end = document.getElementById('end_date');
    let start_date = "'" + datepicker_start.value + "'";
    let end_date = "'" + datepicker_end.value + "'";
    let table = document.querySelector("table");
    while (table.rows.length > 0 ) {
        table.deleteRow(0);
    }
    fetch('http://localhost:5000/api/employees?start_date=' + start_date + "&end_date=" + end_date)
        .then((response) => response.json())
        .then((data)=> {
            console.log(data);
            if (data.length > 0){
                let h1 = document.querySelector("h1");
                h1.innerHTML = "Search results";
                let dataToDisplay = formDataToDisplay(data);
                // get the table to display data
                let table = document.querySelector("table");
                // generate table, passing the table element, table data, and table headers
                generateTable(table, dataToDisplay, Object.keys(dataToDisplay[0]));
                generateTableHead(table, Object.keys(dataToDisplay[0]).slice(1));
            }
        })
        .catch((error) => console.log(error))
}