const express = require('express');
const port = 3000;
const app = express();
const routes = require("./routes");

app.use('/', routes);

app.listen(port, function() {
    console.log("Server is running on port: " + port + " port.");
});

// app.get("/", async(req, res) => {
//     res.send("<h1>Hello World!<h1>");
// });

