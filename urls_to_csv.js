const fs = require("fs");
var f35 = require("./data.js");
var f22 = require("./data.js");
var f16 = require("./data.js");

var csv_f22 = f22.f22.join(",\n");
var csv_f16 = f16.f16.join(",\n");
var csv_f35 = f35.f35.join(",\n");

fs.writeFile("csv_f22.csv", csv_f22, function(err) {
  if (err) {
    return console.log(err);
  }

  console.log("The file was saved csv_f22!");
});

fs.writeFile("csv_f16.csv", csv_f16, function(err) {
  if (err) {
    return console.log(err);
  }

  console.log("The file was saved csv_f16!");
});

fs.writeFile("csv_f35.csv", csv_f35, function(err) {
  if (err) {
    return console.log(err);
  }

  console.log("The file was saved csv_f35!");
});
