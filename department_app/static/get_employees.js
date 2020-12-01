fetch("http://localhost:5000/api/employees")
        .then( (response) => response.json())
        .then((data)=> console.log(data))// output will be the required data
        .catch( (error) => console.log(error))