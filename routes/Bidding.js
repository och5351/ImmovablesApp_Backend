var express = require('express');
var router = express.Router();

// mysql 선언
var dbConObj = require('../lib/dbConnector');
var conn = dbConObj.init();

// 입찰 post
router.post('/Bidding', function(req,res,next){
    var params = [req.body.email , req.body.author, req.body.idx];
    conn.query('UPDATE dealinfo SET participant = CASE WHEN participantCount < 5 THEN concat(participant, ?) ELSE participant END, participantCount = CASE WHEN participantCount < 5 THEN participantCount + 1 ELSE participantCount END WHERE author = ? and idx = ?',
    params, function(err, row) {
      if(err){
        console.log(err)
        res.send(err)
      }else{
        res.status(200).json({
          message: 'success!',
        })
      }
    })
  });