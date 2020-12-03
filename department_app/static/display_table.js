let script = document.getElementById('get');
let query = script.classList
let url = query[0]
let headers = []
let keys = []

for(let i = 1; i < script.classList.length; i++){
  string = query[i]
  header =  (string.charAt(0).toUpperCase() + string.slice(1)).replace(/_/g, " ")
  headers.push(header)
  keys.push(string)
}

fetch(url)
  .then( (response) => response.json())
  .then((data)=> {
    console.log(data);
    let table = document.querySelector("table");
    generateTable(table, data, keys);
    generateTableHead(table, headers);
  })// output will be the required data
  .catch( (error) => console.log(error))

function generateTableHead(table, data) {
  let thead = table.createTHead();
  let row = thead.insertRow();
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
    for(let j = 0; j < keys.length; j++) {
      let cell = row.insertCell();
      let text = document.createTextNode(element[keys[j]]);
      cell.appendChild(text);
    }
  }
}
