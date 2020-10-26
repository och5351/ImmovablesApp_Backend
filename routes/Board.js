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

////////////////////////////////////////////////////////

// 최근 본방에 추가
router.put('/putRecentList', function(req, res, next) {
    var params = [req.body._email, req.body._idx, req.body._option, req.body._email, req.body._idx, req.body._option];
    //var insertQuery2 = 'INSERT INTO recentlist(email, board_idx, type) VALUES (?, ?, ?)';

    // recentlist에 해당 Component의 정보가 있으면 넘어가고, 만약 존재하지 않는다면 INSERT 해줍니다.
    var insertQuery =   'INSERT INTO recentlist (email, board_idx, type) ' + 
                        'SELECT ?, ?, ? FROM DUAL ' +
                        'WHERE NOT EXISTS (SELECT num FROM recentlist WHERE email=? AND board_idx=? AND type=?)';

    conn.query(insertQuery, params, function(err) {
        if (err)
            console.log(err);        
    });
});

// 현재 찜한 상태를 가져옴(로딩부분)
router.post('/postLikeStatus', function(req, res, next)
{
    var params = [req.body._email, req.body._idx, req.body._option];
    var selectQuery = 'SELECT * FROM likelist WHERE email=? AND board_idx=? AND type=?';
    
    conn.query(selectQuery, params, function(err, result){
        if (err) {
            console.log(err);
        }
        else {
            res.send(result);
        }
    });
});

// 찜한 방에 추가
router.put('/putLikeList', function(req, res, next) {
    var params = [req.body._email, req.body._idx, req.body._option];
    var insertQuery = 'INSERT INTO likelist(email, board_idx, type) VALUES (?, ?, ?)';

    conn.query(insertQuery, params, function(err) {
        if (err) {
            console.log(err);
        }
    });
});

// 찜한 방에서 삭제
// router.delete body 문제로 post 대체함.
router.post('/deleteLikeList', function(req, res, next) {
    var params = [req.body._email, req.body._idx, req.body._option];;
    var deleteQuery = 'DELETE FROM likelist WHERE email=? AND board_idx=? AND type=?';

    conn.query(deleteQuery, params, function(err) {
        if (err)
            console.log(err);
    });
});

////////////////////////////////////////////////////////

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
    conn.query('SELECT * FROM dealinfo', function(err, row) {
        res.send(row);        
    });
});

// 구매 희망 본문 읽어 오기
router.get('/getWishPost', function(req, res, next) {
    conn.query('SELECT * FROM wishinfo', function(err, row) {
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