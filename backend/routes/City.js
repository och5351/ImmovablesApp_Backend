var express = require('express');
var router = express.Router();

var dbConObj = require('../lib/dbConnector');
var conn = dbConObj.init();


router.get('/', function(req, res, next) {
    res.send('respond with a resource');
});

// 시/도 읽어 오기
router.get('/getCity', function(req, res, next) {
    console.log(3);
    conn.query('SELECT * FROM city', function(err, row) {
        console.log(3);
        res.send(row);  
    });
});
// 시/군/구읽어오기
router.get('/getGunCity', function(req, res, next) {
    console.log(4);
    conn.query('SELECT * FROM contry', function(err, row) {
        console.log(3);
        res.send(row);  
    });
});
module.exports = router;
