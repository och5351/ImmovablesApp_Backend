var express = require('express');
var router = express.Router();

// mysql 선언
var dbConObj = require('../lib/dbConnector');
var conn = dbConObj.init();

/* GET comments listing. */
router.get('/', function(req, res, next) {
    console.log(1)
    conn.query('SELECT * FROM city', function(err, row){
        try{
            res.json(row);
        }catch(err){
            console.log(err)
        }
        
    })
});

// 본문 읽어 오기
router.get('/getPost', function(req, res, next) {
    conn.query('SELECT * FROM imformation', function(err, row) {
        res.send(row);        
    });
});


module.exports = router;