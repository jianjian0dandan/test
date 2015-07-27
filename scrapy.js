var connection = function(port,dbname){
	if(!port){
		port = 27019;
	}
	if(!dbname){
		dbname = "54api_weibo_v2"
	}
	db = connect("219.224.135.47:"+port+"/"+dbname)
	return db;
}
while (1){
	var start = db.random_weibo.find().count()
	var start_time = (new Date()).getTime()
	Delay 60000
	var finish = db.random_weibo.find().count()
	var finish_time = (new Date()).getTime()
	var counts = finish_count = finish-start
	print (counts + "in one minute")
}