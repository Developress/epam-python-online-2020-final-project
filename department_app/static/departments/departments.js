fetch("http://localhost:5000/api/departments")
        .then( (response) => response.json())
        .then((data)=> {
            responseReceived(data);
        })// output will be the required data
        .catch( (error) => console.log(error))

function responseReceived(data){
    console.log(data);
    if(data.length == 0){
        empty = document.getElementById("empty");
        let text = document.createTextNode("No departments were found");
        empty.appendChild(text);
    } else {
        let dataToDisplay = formDataToDisplay(data);
        let table = document.querySelector("table");
        generateTable(table, dataToDisplay, Object.keys(dataToDisplay[0]));
        generateTableHead(table, Object.keys(dataToDisplay[0]).slice(1));
    }
}

function formDataToDisplay(returnedJson) {
    let dataToDisplay = [];
    for(let i = 0; i < returnedJson.length; i++){
        object = returnedJson[i];
        employeeCount = object['employees'].length;
        let averageSalary = 0;
        if(employeeCount > 0){
            for(let j = 0; j < object['employees'].length; j++){
            employee = object['employees'][j];
            averageSalary += employee['salary'];
        }
            averageSalary /= employeeCount;
        }
        department = {
            'id': object['id'],
            'Name': object['name'],
            'Description': object['description'],
            'Employee count': employeeCount,
            'Average salary': averageSalary
        }
        dataToDisplay.push(department);
    }
    return dataToDisplay;
}

function generateTableHead(table, data) {
    let thead = table.createTHead();
    let row = thead.insertRow();
    data.push('Edit');
    data.push('Delete');
    for (let key of data) {
        let th = document.createElement("th");
        let text = document.createTextNode(key);
        th.appendChild(text);
        row.appendChild(th);
    }
}

function generateTable(table, data, keys) {
    for(let i = 0; i < data.length; i++) {
        let element = data[i];
        console.log(keys)
        let row = table.insertRow();
        for(let j = 1; j < keys.length; j++) {
            let cell = row.insertCell();
            let text = document.createTextNode(element[keys[j]]);
            cell.appendChild(text);
        }
        let cell = row.insertCell();
        let a = document.createElement("a");
        a.setAttribute("href", `/departments/edit/${element['id']}`);
        let text = document.createTextNode("Edit");
        a.appendChild(text);
        cell.appendChild(a);
        cell = row.insertCell();
        a = document.createElement("a");
        a.setAttribute("onclick", `sendDeleteRequest(${element['id']})`)
        a.setAttribute("href", "#");
        text = document.createTextNode("Delete");
        a.appendChild(text);
        cell.appendChild(a);
    }
}

function sendDeleteRequest(id){
    fetch(`http://localhost:5000/api/departments/${id}`, {
        method: 'DELETE'
    })
    .then(res => {
        window.location.href = `/departments/delete/${id}`;
    }) // or res.json()
    .then(res => console.log(res))
}