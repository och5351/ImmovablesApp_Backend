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
    conn.query('SELECT * FROM wishinfo;', function(err, row) {
        if (err)
            console.log(err)
        else
            res.send(row);        
    });
});

// 거래 희망 글
router.get('/getDealPost', function(req, res, next) {
    conn.query('SELECT * FROM dealinfo;', function(err, row) {
    
        res.send(row);        
    });
});

// 구매 희망 본문 읽어 오기
router.get('/getWishPost', function(req, res, next) {
    conn.query('SELECT * FROM wishInfo', function(err, row) {
        res.send(row);        
    });
});

router.get('/getWishImg/:name', function(req,res, next){
    var filename = req.params.name;
    var path = 'public/images/wishImages/'
    fs.readFile(path + filename,              
        function (err, data)
        {
            res.writeHead(200, { "Context-Type": "image/jpg" });
            res.write(data);   
            res.end();  
        }
    );
})
router.get('/getDealImg/:name', function(req,res, next){
    var filename = req.params.name;
    var path = 'public/images/dealImages/'
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