const express = require("express")
const app = express();

app.use("/", (req, res, nex) => {
    res.send("Express server response");
})

app.get("/result", (req, res, nex) => {
    res.send("result received");
})

app.listen((3000), () => {
    console.log("Server is Running");
})
