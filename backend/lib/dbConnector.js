var mysql = require('mysql');

var dbconnInfo = {
    host: 'localhost',
    user: 'root',
    //password: 'iclab4',
    password: '0000',
    database: 'immovables'
};


var connection = {
    init : () => {
        return mysql.createConnection(dbconnInfo);
    },

    open : (con) => {
        con.connect(function(err){
            if(err){
                console.error("mysql connection error : " + err);
            }else{
                console.info("mysql connection successfully.");
            }
        });
    }
};


module.exports = connection;
