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

function generateTable(table, data, keys, object) {
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
        a.setAttribute("href", `/${object}/edit/${element['id']}`);
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