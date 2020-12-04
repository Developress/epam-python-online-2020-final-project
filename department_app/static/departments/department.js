// declare the needed globals, id - for the id of department being edited,
// add - to indicate whether the department is being adding or editing
let id = 0;
let add = true;

if(document.title === "Edit Department"){
    add = false;
    // get the id, which will be the last element of url
    id = document.URL.substring(document.URL.lastIndexOf('/') + 1);
    // perform a GET request to receive the needed department
    fetch(`/api/departments/${id}`)
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
    // get the description input and set a value to it
    let description = document.getElementById('description');
    let text = document.createTextNode(data['description']);
    description.appendChild(text);
}

function onSubmitClicked(){
    // get the name and description inputs
    let name = document.getElementById('name');
    let description = document.getElementById('description');
    // form a body for post or put request
    data = {
        'name': name.value,
        'description': description.value
    }
    // if we are adding the element
    if(add){
        fetch(`/api/departments`, {
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
                window.location = '/departments/add?added=' + true;
            })
            .catch((error) => console.log(error))
    } else {
        fetch(`pi/departments/${id}`, {
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
                window.location = `/departments/edit/${id}?edited=` + true;
            })
            .catch((error) => console.log(error))
    }
}