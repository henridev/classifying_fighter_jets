urls = Array.from(document.querySelectorAll(".rg_di .rg_meta")).map(
  el => JSON.parse(el.textContent).ou
)(function(console) {
  console.save = function(data, filename) {
    if (!data) {
      console.error("Console.save: No data");
      return;
    }

    if (!filename) filename = "console.json";

    if (typeof data === "object") {
      data = JSON.stringify(data, undefined, 4);
    }

    var blob = new Blob([data], { type: "text/json" }),
      e = document.createEvent("MouseEvents"),
      a = document.createElement("a");

    a.download = filename;
    a.href = window.URL.createObjectURL(blob);
    a.dataset.downloadurl = ["text/json", a.download, a.href].join(":");
    e.initMouseEvent(
      "click",
      true,
      false,
      window,
      0,
      0,
      0,
      0,
      0,
      false,
      false,
      false,
      false,
      0,
      null
    );
    a.dispatchEvent(e);
  };
})(console);

console.save(urls);

// will give you the file under
// open this in vscode as a js file
