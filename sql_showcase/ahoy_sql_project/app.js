var express = require('express');
var mysql = require('mysql');
var bodyParser = require("body-parser");
var app = express();

app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static(__dirname + "/public"));

var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  database : 'join_us'
});

app.post('/register', function(req,res){
 var person = {email: req.body.email};
 connection.query('INSERT INTO users SET ?', person, function(err, result) {
 console.log(err);
 console.log(result);
 res.redirect("/");
 });
});

app.get("/", function(req, res){
 var q = 'SELECT COUNT(*) as count FROM users';
 connection.query(q, function (error, results) {
 if (error) throw error;
 var count = results[0].count;
 res.render("home", {count: count});
 });
});

app.get("/goober", function(req, res){
 var pics = "Send puppy pics to (224) 616-4748";
 res.send(pics);
});

app.get("/random_num", function(req, res){
 var number = Math.floor(Math.random() * 10) +1;
 res.send("Your random number is " + number);
});

app.listen(3000, () => {
	console.log('Server running on 3000!');
});
