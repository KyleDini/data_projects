// node -v
// npm install faker
// mysql-ctl start
// Root User: root
// mysql-ctl cli in separate terminal
// npm install mysql

// ls
// cd (file name you want to use)

var faker = require('faker');
var mysql = require('mysql');

var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  database : 'join_us'
});

// SELECTING DATA EXAMPLE:
// var q = 'SELECT * FROM users';

// connection.query(q, function (error, results, fields) {
//	  if (error) throw error;
//	  console.log(results);
// });

// INSERTING DATA DYNAMICALLY EXAMPLE:
// var person = {
//     email: faker.internet.email(),
//     created_at: faker.date.past()
// };
 
// var end_result = connection.query('INSERT INTO users SET ?', person, function(err, result) {
//   if (err) throw err;
//   console.log(result);
// });

//SOME MySQL/NODE MAGIC: Converts Faker date format to proper SQL format!

// INSERTING LOTS OF DATA: -----------------------------------------------------------
var data = [];
for(var i = 0; i < 500; i++){
	data.push([
		faker.internet.email(),
		faker.date.past()
	]);
}

var q = 'INSERT INTO users (email, created_at) VALUES ?';

connection.query(q, [data], function(err, result) {
	console.log(err);
   console.log(result);
});

connection.end();