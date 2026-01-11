import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Feet Calculator", layout="centered")

html_code = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #f9f9f9;
}
h2 {
    text-align: center;
    margin: 15px;
    color: #333;
}
.calc {
    max-width: 420px;
    margin: auto;
}
.display {
    background: black;
    color: white;
    font-size: 30px;
    padding: 20px;
    text-align: right;
    border-radius: 12px;
    min-height: 70px;
    box-sizing: border-box;
}
.grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10px;
    margin-top: 15px;
}
button {
    height: 70px;
    font-size: 22px;
    border-radius: 14px;
    border: none;
    cursor: pointer;
}
.op { background: linear-gradient(45deg, #ff9500, #ffcc00); color: white; }
.num { background: #e0e0e0; }
.clear { background: #ff3b30; color: white; }
.equal { background: #34c759; color: white; }
.histBtn { background: #5856d6; color: white; }
#history {
    margin-top: 15px;
    font-size: 16px;
    color: #555;
    max-height: 150px;
    overflow-y: auto;
    display: none;
    background: #f1f1f1;
    padding: 10px;
    border-radius: 10px;
}
</style>
</head>

<body>
<h2>Feet Calculator</h2>
<div class="calc">
    <div id="display" class="display"></div>
    <div class="grid">
        <!-- Top row with functions -->
        <button class="clear" onclick="clr()">C</button>
        <button class="op" onclick="press('( )')">( )</button>
        <button class="histBtn" onclick="toggleHistory()">History</button>
        <button class="num" onclick="del()">⌫</button>

        <!-- Numbers and operators -->
        <button class="num" onclick="press('7')">7</button>
        <button class="num" onclick="press('8')">8</button>
        <button class="num" onclick="press('9')">9</button>
        <button class="op" onclick="press('/')">÷</button>

        <button class="num" onclick="press('4')">4</button>
        <button class="num" onclick="press('5')">5</button>
        <button class="num" onclick="press('6')">6</button>
        <button class="op" onclick="press('*')">×</button>

        <button class="num" onclick="press('1')">1</button>
        <button class="num" onclick="press('2')">2</button>
        <button class="num" onclick="press('3')">3</button>
        <button class="op" onclick="press('-')">−</button>

        <button class="num" onclick="press('0')">0</button>
        <button class="num" onclick="press('.')">.</button>
        <button class="op" onclick="press('+')">+</button>
        <button class="equal" onclick="calc()">=</button>
    </div>
    <div id="history"></div>
</div>

<script>
let display = document.getElementById("display");
let expr = "";

function press(v) {
    // Add spacing around operators
    if (['+', '-', '*', '/', '( )'].includes(v)) {
        if (v === '( )') {
            expr += " ( ) ";
        } else {
            expr += " " + v + " ";
        }
    } else if (v === ".") {
        // If user types ".3", convert to "0.3"
        if (expr === "" || expr.slice(-1) === " ") {
            expr += "0.";
        } else {
            expr += ".";
        }
    } else {
        expr += v;
    }
    display.innerText = expr;
}

function del() {
    expr = expr.trimEnd();
    expr = expr.slice(0, -1);
    display.innerText = expr;
}

function clr() {
    expr = "";
    display.innerText = "";
}

function feetToInch(n) {
    if (n.includes(".")) {
        let p = n.split(".");
        return (parseInt(p[0]) * 12) + parseInt(p[1]);
    }
    return parseInt(n) * 12;
}

function calc() {
    try {
        let div = (expr.includes("*") || expr.includes("/")) ? 144 : 12;
        let tokens = expr.split(/([+\\-*/()])/).map(t => t.trim()).filter(t => t !== "");
        let converted = tokens.map(t => {
            if (!isNaN(t) && t !== "") return feetToInch(t);
            return t;
        });
        let resultInch = eval(converted.join(" "));
        let result = resultInch / div;
        let final = result.toFixed(2);

        document.getElementById("history").innerHTML += expr + " = " + final + "<br>";
        expr = final;
        display.innerText = expr;
    } catch {
        display.innerText = "Error";
        expr = "";
    }
}

function toggleHistory() {
    let h = document.getElementById("history");
    h.style.display = (h.style.display === "none") ? "block" : "none";
}
</script>
</body>
</html>
"""

components.html(html_code, height=800)
