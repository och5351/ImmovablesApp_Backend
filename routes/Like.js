var express = require('express');
var router = express.Router();

// mysql 선언
var dbConObj = require('../lib/dbConnector');
var conn = dbConObj.init();

/* GET comments listing. */
router.get('/', function(req, res, next) {
    res.send('respond with a resource');
});

// 최근 확인한 방 가져오기
router.post('/recentData', function(req, res, next) {
    console.log("### like/recentData 실행...");
    
    // 유저 이메일 확인 후 type 1 인경우 wishinfo 에서 정보 가져옴.
    let selectWishinfoQuery = 'select w.* from wishinfo w, recentlist r where r.email=? and r.type=1 and r.board_idx=w.idx'; 
    // 유저 이메일 확인 후 type 2 인경우 dealinfo 에서 정보 가져옴.
    let selectDealinfoQuery = 'select d.* from dealinfo d, recentlist r where r.email=? and r.type=2 and r.board_idx=d.idx';
    
    
    
    conn.query(req.body._option == 0 ? selectWishinfoQuery : selectDealinfoQuery, req.body._email, function(err, result) {
        // let _log;
        if (err) {
            console.log(err);
        } 
        else {
            console.log("### SELECT문 완료, res.send() 호출...");            
            res.send(result);
        }
    });
});

router.post('/likeData', function(req, res, next) {
    console.log("### like/likeData 실행...");

    // 유저 이메일 확인 후 type 1 인경우 wishinfo 에서 정보 가져옴.
    let selectWishinfoQuery = 'select w.* from wishinfo w, likelist l where l.email=? and l.type=1 and l.board_idx=w.idx'; 
    // 유저 이메일 확인 후 type 2 인경우 dealinfo 에서 정보 가져옴.
    let selectDealinfoQuery = 'select d.* from dealinfo d, likelist l where l.email=? and l.type=2 and l.board_idx=d.idx'; 

    conn.query(req.body._option == 0 ? selectWishinfoQuery : selectDealinfoQuery, req.body._email, function(err, result) {
        if (err) {            
            console.log(err);
        } 
        else {
            console.log("### SELECT문 완료, res.send() 호출...");
            res.send(result);
        }
    });
});

module.exports = router;