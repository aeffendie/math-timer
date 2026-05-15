import React, {useState, useEffect} from 'react';
import axios from 'axios';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './components/Login';
import Register from './components/Register';
import Homepage from './components/Homepage';
import Navbar from './components/Navbar';
import './App.css'; // Import the styles.css file

const slug = "https://math-timer.com/";     // change as needed

function GetProblem(
    type = "simple"
) {
    var resp = null;
    const [ posts, setPosts ] = useState([]);

    let config = {
        headers: {
            "Content-Type" : "application/json"
        }
    }

    let data = {
        "PROBLEM_TYPE" : type
    }

    useEffect(() => {
        axios.post(slug + "/getproblem", data, config)
            .then(response => {
                resp = response.data;
            // setPosts(response.data);
        })
        .catch(error => {
            console.error(error);
        });
    }, []);

    return resp;
}

function SolveProblem(
    problem: String,
    solution: String
) {
    var resp = null;
    const [ posts, setPosts ] = useState([]);

    let config = {
        headers: {
            "Content-Type" : "application/json"
        }
    }

    let data = {
        "PROBLEM" : problem,
        "SOLUTION" : solution
    }

    useEffect(() => {
        axios.post(slug + "/solveproblem", data, config)
            .then(response => {
                resp = response.data;
            }).catch(error => {
                console.error(error);
            });
    }, []);

    return resp;
}

function submitSolution() {
    alert("submitted Solution!");
}

function nextProblem() {
    alert("submitted Solution!");
}

function getPage() {
    return (
        <>
        <head>
            <meta charset="UTF-8"></meta>
            <meta name="viewport" content="width=device-width, initial-scale=1.0"></meta>
        </head>
        
        <body>
            <h1>a better name for a math trainer</h1>
            <form id="math_trainer_form">
                <div>
                    <h3>Enter Solution</h3>
                    <input type="text" 
                           name="solution"
                           id="solution_form"></input>
                </div>
                <button type="submit">Add</button>
            </form>
            <div>
                <h3 id="solution_form"></h3>
            </div>
            <script src="math_trainer_input.js"></script>   
        </body>
        </>
    );
}

function App() {
    const [posts, setPosts] = useState([]);
    var problem = null;
    var solveAttempt = false;
    
    // problem = GetProblem();
    // setPosts(problem);

    // TODO: Get Form Data on Button / Keybind ENTER, send, then get result, change button.
    // After 

    if (solveAttempt) {
        return (
            <>
                <div>Under Construction</div>
                <div>
                    <button onClick={() => submitSolution()}>Submit</button>
                </div>
            </>
        );
    } else {
        return (
            <>
                <div>
                    <button onClick={() => nextProblem()}>Next Problem</button>
                </div>
            </>
        );
    }
}
export default App;
