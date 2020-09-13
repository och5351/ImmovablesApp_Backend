var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');

//module 등록
var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');
var BoardRouter = require('./routes/Board');
var CityRouter = require('./routes/City');
var LoginRouter = require('./routes/Login')
var Map = require('./routes/Map')

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');
app.set('port', process.env.PORT || 3000);

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

// 경로 확인
app.use('/', indexRouter);
app.use('/api/city', CityRouter);
app.use('/api/users', usersRouter);
app.use('/api/board', BoardRouter)
app.use('/api/login', LoginRouter)
app.use('/api/map', Map)

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;

var server = app.listen(app.get('port'), function(){
  console.log('Express server listening on port ' + server.address().port);
})