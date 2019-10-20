const express = require('express');
const port = 8080;
const app = express();
const routes = require("./routes");
const bodyParser = require('body-parser')

app.use(bodyParser.json());
app.use(
    bodyParser.urlencoded({
        extended: true,
    })
)
app.use('/', routes);

app.listen(port, function() {
    console.log("Server is running on port: " + port + " port.");
});

