var express = require('express');
var router = express.Router();
var bodyParser = require('body-parser')
router.use(bodyParser.json())
const multer = require('multer')
// mysql 선언
var dbConObj = require('../lib/dbConnector');
var conn = dbConObj.init();

// multer 정리


const Storage = multer.diskStorage({
    destination(req, file, callback) {
      callback(null, 'images/');
    },
    filename(req, file, callback) {
      callback(null, `${file.uri}_${Date.now()}`);
    },
    limits: { fileSize: 5 * 1024 * 1024 },
  });
const upload = multer({ storage: Storage });



/* GET comments listing. */
router.get('/', function(req, res, next) {
    res.send('respond with a resource');
});

// 방 구매하기 작성글 post
router.post('/postSell', upload.single('photo'),function(req,res,next){
    
    console.log(req.files)
    console.log(req.body)
    res.status(200).json({
        message: 'success!',
    })
    
})


module.exports = router;