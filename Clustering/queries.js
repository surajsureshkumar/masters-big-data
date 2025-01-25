db.movie.aggregate([
    {
        $match:{
            'titleType': 'movie',
            'numVotes':{$gt:10000},
            'startYear':{$ne : null},
            'averageRating':{$ne : null}
        }
    },
    {
        $out : 'movie_cluster'
    }
])



db.movie_cluster.aggregate([
{"$setWindowFields": {
    "output": {
      "maxYear": {$max: "$startYear"},
      "minYear": {$min: "$startYear"},
      "maxRating": {$max: "$averageRating"},
      "minRating": {$min: "$averageRating"}
    }
  },
},
{$out : 'movies_norm'}])

db.movies_norm.aggregate([
{$addFields : {
        'kmeansNorm': [{
            $divide :[
            {$subtract : ['$startYear', '$minYear']},
            {$subtract :['$maxYear', '$minYear']}
            ]
        },{
            $divide :[
            {$subtract : ['$averageRating', '$minRating']},
            {$subtract :['$maxRating', '$minRating']}
            ]
        }]
        
    }
},
{$out : 'movies_norm'}])


--task2
var g = 'Action';
var k = 20
var i = 1;
db.movies_norm.aggregate([
    {$unwind:"$genre"},
    {$match:{genre : g,genre:{$ne : null}}},
    {$sample : {size: k}},
    {$project: {"kmeansNorm":1}}
]).forEach(function(doc) {
    db.centroid.insertOne({ID:i, kmeansNorm:doc.kmeansNorm});
    i = i+1;
});



db.createCollection("centroid");


db.movies_norm.aggregate([
    {$unwind:"$genre"},
    {$match:{genre : g,genre:{$ne : null}}}]).forEach(function(doc) {
        
    });

