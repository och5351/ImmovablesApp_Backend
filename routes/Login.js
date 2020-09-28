var express = require('express');
var router = express.Router();

// mysql 선언
var dbConObj = require('../lib/dbConnector');
var conn = dbConObj.init();


// 유저가 현재 Immovables.uesr 테이블에 존재하는지 체크
router.post('/checkUser', function(req, res) {  
  var data = [ req.body._email, req.body._uid, req.body._name];
  var selectQuery = 'SELECT count(*) as id FROM user WHERE email = ? ';
  let count = -1;
  conn.query(selectQuery, data[0], function(err, result) {
      if(!err) {
        count = result[0].id;
      }
      else{
        console.log(err);
      }
  });
  // 회원정보가 db에 저장되어있지 않으면 추가해줍니다.
  if (count == 0){    
    var insertQuery = 'INSERT INTO user(email, uid, name) VALUES (?, ?, ?)';
    conn.query(insertQuery, [data[0], data[1], data[2]], function(err){
      if(err){
        console.log(err);
      }
    });
  }
  // 회원정보가 db에 저장되어있다면 update 해줍니다 (이름. uid는 고정값이라 변동이 없습니다.).
  else{
    var updateQuery = 'UPDATE user SET name=? WHERE email=?';
    conn.query(updateQuery, [data[2], data[0]], function(err){
      if(err){
        console.log(err);
      }
    });
  }
});

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