//for initial page load, load the top 10 ranked games
d3.json('static/data/RA.json').then( function(data){
    console.log(data);});