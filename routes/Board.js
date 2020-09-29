var express = require('express');
var router = express.Router();
var fs = require('fs')

// mysql 선언
var dbConObj = require('../lib/dbConnector');
var conn = dbConObj.init();

/* GET comments listing. */
router.get('/', function(req, res, next) {
    res.send('respond with a resource');
});

// 구매 희망 글
router.get('/getPost', function(req, res, next) {
    conn.query('SELECT * FROM wishinfo', function(err, row) {
        res.send(row);        
    });
});

// 거래 희망 글
router.get('/getPost2', function(req, res, next) {
    conn.query('SELECT * FROM wishinfo', function(err, row) {
        res.send(row);        
    });
});

// 구매 희망 본문 읽어 오기
router.get('/getWishPost', function(req, res, next) {
    conn.query('SELECT * FROM WishInfo', function(err, row) {
        res.send(row);        
    });
});

router.get('/getSellImg/:name', function(req,res, next){
    var filename = req.params.name;
    var path = 'public/images/sellImages/'
    fs.readFile(path + filename,              
        function (err, data)
        {
            res.writeHead(200, { "Context-Type": "image/jpg" });
            res.write(data);   
            res.end();  
        }
    );
})

module.exports = router;