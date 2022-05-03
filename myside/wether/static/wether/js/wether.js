
const wetherApi = document.querySelectorAll('td');

let dateTime = [];
let tepm2m = [];
let windSpeed = [];
let windDir = [];
let pressure = [];
let precipt1H = [];
let precipt24H = [];
let uv = [];
let sunRise = [];
let sunSet = [];

parameters = [dateTime, tepm2m, windSpeed, windDir, 
    pressure, precipt1H, precipt24H, uv, sunRise, sunSet];

wetherApi.forEach(row => {
    let counter = 0;
    parameters[counter].push(row);
    if(counter == 9) {
        counter = 0;
    }
    else {
        counter += 1;
    }
});


new Chart("graf", {
    type: "line",
    data: {
        labels: dateTime,
        datasets: [{
            fill: false,
            lineTension: 0,
            backgroundColor: "rgba(0,0,255,1.0)",
            borderColor: "rgba(0,0,255,0.1)",
            data: windSpeed
        }]
    },
    options: {
        legend: {display:false},
    }
})

// new Chart('graf', {
//     type: 'line',
//     date: {
//         labels: dateTime,
//         datasets: [{
//             data: tepm2m,
//             borderColor: "red",
//             fill: false
//         }]
//     },
//     options: {
//         legend: {display: false}
//     }
// });
