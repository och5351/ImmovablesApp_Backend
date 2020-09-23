var express = require('express');
var router = express.Router();

var dbConObj = require('../lib/dbConnector');
var conn = dbConObj.init();


router.get('/', function(req, res, next) {
    res.send('respond with a resource');
});

// 시/도 읽어 오기
router.get('/getCity', function(req, res, next) {
    conn.query('SELECT * FROM city', function(err, row) {
        res.send(row);  
    });
});
// 시/군/구읽어오기 ..
router.get('/getGunCity:seq', function(req, res, next) {
    let city_code  = req.params.seq;
    
    conn.query('SELECT * FROM contry WHERE pre_code = ?',[city_code], function(err, row) {
        res.send(row);  
    });
});
module.exports = router;
