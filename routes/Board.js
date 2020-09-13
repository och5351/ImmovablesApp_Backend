var express = require('express');
var router = express.Router();

// mysql 선언
var dbConObj = require('../lib/dbConnector');
var conn = dbConObj.init();

/* GET comments listing. */
router.get('/', function(req, res, next) {
    res.send('respond with a resource');
});

// 본문 읽어 오기
router.get('/getPost', function(req, res, next) {
    console.log(2);
    conn.query('SELECT * FROM wishinfo WHERE att = 1', function(err, row) {
        res.send(row);        
    });
});

// 본문 읽어 오기
router.get('/getPost2', function(req, res, next) {
    console.log(2);
    conn.query('SELECT * FROM wishinfo WHERE att = 2', function(err, row) {
        res.send(row);        
    });
});

// 구매 희망 본문 읽어 오기
router.get('/getWishPost', function(req, res, next) {
    console.log(2);
    conn.query('SELECT * FROM WishInfo', function(err, row) {
        res.send(row);        
    });
});


module.exports = router;