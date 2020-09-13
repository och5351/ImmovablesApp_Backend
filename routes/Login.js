var express = require('express');
var router = express.Router();

// mysql 선언
var dbConObj = require('../lib/dbConnector');
var conn = dbConObj.init();

router.post('/chinfo', function(req, res){
  var data = [req.body.id,req.body.pw];
  var sql = "SELECT count(*) as id FROM test WHERE id = ? ";

  conn.query(sql,data[0],(err, result,rows)=>{
    console.log(data[0])
    if(err){ console.log(err);}
    else{
      console.log(result[0].id)
      if(result[0].id == 1)
        {
          res.send({
            values: "중복"
          });
        }
      else{
        res.send({
          values: "중복아님"
        });
      }
      console.log(result);

    }
  });
});


router.post('/data', function(req, res){
  console.log(req.body); 
  var data = [req.body.id,req.body.pw];
  var sql = "INSERT INTO test(id,pw) values(?) ";
  conn.query(sql,[data],(err, result)=>{
    if(err) throw err;
    else{
      console.log(result);
      res.send({
        result: "완료"
      });
    }
  });
});

module.exports = router;