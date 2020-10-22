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
// 시/군/구 읽어오기
router.get('/getContry/:seq', function(req, res, next) {
    let city_code  = req.params.seq;
    conn.query('SELECT * FROM contry WHERE pre_code = ?',[city_code], function(err, row) {
        res.send(row);  
    });
});
// 동/면/읍 읽어오기
router.get('/getTown/:seq', function(req, res, next) {
    let town_code  = req.params.seq;
    conn.query('SELECT * FROM town WHERE pre_code = ?',[town_code], function(err, row) {
        res.send(row);  
    });
});
// 아파트 특정 단어 검색
router.get('/getApart?/:cityCode/:contryCode/:townCode/:searchWord', function(req, res, next) {
    let cityCode  = req.params.cityCode;
    let contryCode  = req.params.contryCode;
    let townCode  = req.params.townCode;
    let searchWord  = '%'+req.params.searchWord+'%';
    conn.query("SELECT immovable_name, rea FROM apartimmovables WHERE cityCode = ? AND contryCode = ? AND townCode = ? AND immovable_name LIKE ?",
    [cityCode,contryCode,townCode,searchWord], function(err, row) {
        res.send(row);  
    });
});
// 오피스텔 특정 단어 검색
router.get('/getOfficetel?/:cityCode/:contryCode/:townCode/:searchWord', function(req, res, next) {
    let cityCode  = req.params.cityCode;
    let contryCode  = req.params.contryCode;
    let townCode  = req.params.townCode;
    let searchWord  = '%'+req.params.searchWord+'%';
    conn.query("SELECT immovable_name, rea FROM officetelimmovables WHERE cityCode = ? AND contryCode = ? AND townCode = ? AND immovable_name LIKE ?",
    [cityCode,contryCode,townCode,searchWord], function(err, row) {
        res.send(row);  
    });
});
// 빌라 특정 단어 검색
router.get('/getVilla?/:cityCode/:contryCode/:townCode/:searchWord', function(req, res, next) {
    let cityCode  = req.params.cityCode;
    let contryCode  = req.params.contryCode;
    let townCode  = req.params.townCode;
    let searchWord  = '%'+req.params.searchWord+'%';
    conn.query("SELECT immovable_name, rea FROM villaimmovables WHERE cityCode = ? AND contryCode = ? AND townCode = ? AND immovable_name LIKE ?",
    [cityCode,contryCode,townCode,searchWord], function(err, row) {
        res.send(row);  
    });
});

module.exports = router;
