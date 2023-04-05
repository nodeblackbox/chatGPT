const express = require("express");
const app = express();
const path = require("path");
const fs = require("fs");
const ejs = require("ejs");

app.set("view engine", "ejs");

// Serve static files from the public directory
//Before the conversion to react
// app.use(express.static(path.join(__dirname, "public")));
//Attempt of react conversion
app.use(express.static(path.join(__dirname, "public")));

// Define a route to read the conversation from the JSON file and render it in an HTML page
// app.get("/", (req, res) => {
//   fs.readFile(
//     path.join(__dirname, "conversation.json"),
//     "utf8",
//     (err, data) => {
//       if (err) {
//         console.error(err);
//         res.status(500).send("Error reading conversation data");
//         return;
//       }
//       const conversation = JSON.parse(data);
//       res.render("index", { conversation });
//     }
//   );
// });
// });
app.get("/", function (req, res) {
  res.sendFile(path.join(__dirname, "public", "index.html"));
});

// Start the server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
