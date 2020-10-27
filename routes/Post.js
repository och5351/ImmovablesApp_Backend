var express = require('express');
var router = express.Router();
var fs = require('fs')
var bodyParser = require('body-parser')
router.use(bodyParser.json())
router.use(bodyParser.urlencoded({extended: true}));
const multer = require('multer')
// mysql 선언
var dbConObj = require('../lib/dbConnector');
var conn = dbConObj.init();

// multer 정리
multer({
  limits: {fieldSize: 25 * 1024 * 1024},
});
const wishStorage = multer.diskStorage({
    destination(req, file, callback) {
      callback(null, 'public/images/wishImages');
    },
    filename(req, file, callback) {
       callback(null, `${file.originalname}_${Date.now()}`);
     },
  });

const sellStorage = multer.diskStorage({
  destination(req, file, callback) {
    callback(null, 'public/images/dealImages');
  },
  filename(req, file, callback) {
      callback(null, `${file.originalname}_${Date.now()}`);
    },
});

const wishUpload = multer({ storage: wishStorage });
const sellUpload = multer({ storage: sellStorage });

/* GET comments listing. */
router.get('/', function(req, res, next) {
    res.send('respond with a resource');
});

// 본인 작성글 삭제하기
router.post('/postDelete', function(req, res, next) {
  res.send('respond with a resource');
});

// 방 구매하기 작성글 post
router.post('/postWish', wishUpload.any('photo',5),function(req,res,next){
  
  var imgTemp = req.files
  let imgPathString = ''

  imgTemp.forEach(element => {
    imgPathString += element.path.split('/').pop() + ',';
  });
 
  imgPathString=imgPathString!=''?imgPathString:0
  preference = req.body.preference!=''?req.body.preference:0
  conn.query('INSERT INTO wishinfo(title, author, content, price, location, img, preference) VALUES(?, ?, ?, ?, ?, ?, ?)',
  [req.body.title, req.body.user, req.body.contents, req.body.price, req.body.location,  imgPathString ,preference], function(err, row) {
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

//방 거래하기 작성글 post
router.post('/postTrade', sellUpload.any('photo',5),function(req,res,next){
  var imgTemp = req.files
  let imgPathString = ''

  imgTemp.forEach(element => {
    imgPathString += element.path.split('/').pop() + ',';
  });

  imgPathString=imgPathString!=''?imgPathString:0
  preference = req.body.preference!=null?req.body.preference:0
  conn.query('INSERT INTO dealinfo(title, author, content, price, location, img, preference, deposit, area, floor, '+
  'parking, immovabletype, purchasetype, management, heater, loan, option_, pet) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,? ,? ,? ,? ,? ,? ,? ,?)',
  [req.body.title, req.body.user, req.body.contents, req.body.price, req.body.address, imgPathString , preference, req.body.deposit, req.body.area, req.body.floor,
  req.body.park, req.body.immovabletype,req.body.purchasetype ,req.body.management, req.body.heater, req.body.loan, req.body.option_, req.body.pet], function(err, row) {
    if(err){
      res.send(err) 
      console.log()
    }else{
      res.status(200).json({
        message: 'success!',
      })
    }
  })
});

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

module.exports = router;