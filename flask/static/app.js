let cities = document.querySelectorAll(".loc");
let srch_loc = document.querySelector(".srch_location");
let srch_btn = document.querySelector(".btn_srch");
let currentCity = document.querySelector(".currCity");
let temper = document.querySelector(".temperature");
let cloudy = document.querySelector("#cstatus");
let humidity = document.querySelector("#hstatus");
let wind = document.querySelector("#wstatus");
let condition = document.querySelector(".condition");
let dateput = document.querySelector(".dateput");
let timeput = document.querySelector(".timeput");
let icon = document.querySelector(".icon");

let current_loc = "New Delhi";

cities.forEach((city) => {
  city.addEventListener("click", (e) => {
    current_loc = e.target.innerText;
    fetchWeatherData();
  });
});

srch_btn.addEventListener("click", (e) => {
  if (srch_loc.value.length == 0) {
    alert("Enter any location in input box!");
  } else {
    current_loc = srch_loc.value;
    fetchWeatherData();
    srch_loc.value = "";
  }
  e.preventDefault();
});

function dayOfTheWeek(day, month, year) {
  const weekday = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
  ];
  const dt = new Date(day / month / year).getDay();
  return weekday[dt];
}

function redirect() {
  if(document.getElementById("toggle").checked)
  window.location.href="web2.html";
  else
  window.location.href="app.html";

  document.getElementById("toggle").checked=false;
}

function fetchWeatherData() {
  fetch(
    `http://api.weatherapi.com/v1/current.json?key=14c2e437a3aa4af68f9155229222202&q=${current_loc}&aqi=no`
  )
    .then(function (response) {
      let data = response.json();
      return data;
    })
    .then(function (data) {
      console.log(data);

      currentCity.innerText = data.location.name;
      temper.innerHTML = data.current.temp_c + "&#176" + "C";

      cloudy.innerHTML = data.current.cloud + "%";
      humidity.innerHTML = data.current.humidity + "%";
      wind.innerHTML = data.current.wind_kph + "km/h";
      condition.innerHTML = data.current.condition.text;

      const iconId = data.current.condition.icon.substr(
        "//cdn.weatherapi.com/weather/64x64/".length
      ); // day/143.png
      icon.src = "./icons/" + iconId;

      const date = data.location.localtime;
      const y = parseInt(date.substr(0, 4));
      const m = parseInt(date.substr(5, 2));
      const d = parseInt(date.substr(8, 2));
      const time = date.substr(11);
      dateput.innerHTML = `${dayOfTheWeek(d, m, y)} - ${d}/${m}/${y}`;
      timeput.innerHTML = time;

      let timeOfDay = "day";
      const code = data.current.condition.code;

      if (!data.current.is_day) {
        timeOfDay = "night";
      }

      if (code == 1000) {
        document.body.style.backgroundImage = `url(./images/${timeOfDay}/clear.jpg)`;

        srch_btn.style.background = "#e5ba92";
        if (timeOfDay == "night") {
          srch_btn.style.background = "#181e27";
        }
      } else if (
        code == 1003 ||
        code == 1006 ||
        code == 1009 ||
        code == 1030 ||
        code == 1069 ||
        code == 1087 ||
        code == 1135 ||
        code == 1273 ||
        code == 1276 ||
        code == 1279 ||
        code == 1282
      ) {
        document.body.style.backgroundImage = `url(./images/${timeOfDay}/cloudy.jpg)`;
        srch_btn.style.background = "#fa6d1b";
        if (timeOfDay == "night") {
          srch_btn.style.background = "#181e27";
        }
      } else if (
        code == 1063 ||
        code == 1069 ||
        code == 1072 ||
        code == 1150 ||
        code == 1153 ||
        code == 1180 ||
        code == 1183 ||
        code == 1189 ||
        code == 1192 ||
        code == 1195 ||
        code == 1204 ||
        code == 1207 ||
        code == 1240 ||
        code == 1243 ||
        code == 1246 ||
        code == 1249 ||
        code == 1252
      ) {
        document.body.style.backgroundImage = `url(./images/${timeOfDay}/rainy.jpg)`;
        srch_btn.style.background = "#647d75";
        if (timeOfDay == "night") {
          srch_btn.style.background = "#325c80";
        }
      } else {
        document.body.style.backgroundImage = `url(./images/${timeOfDay}/snowy.jpg)`;
        srch_btn.style.background = "#4d72aa";
        if (timeOfDay == "night") {
          srch_btn.style.background = "#1b1b1b";
        }
      }
      document.body.style.opacity = "1";
    });
  /*
    .catch(()=>{
        alert('City not found, please try again!');
        document.body.style.opacity="1";
    });
    */
}

fetchWeatherData();
document.body.style.opacity = "1";