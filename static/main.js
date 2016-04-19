createGraph()

function createGraph() {
    // fetch data
    data = document.getElementById("data").getAttribute("data");
    data = JSON.parse(data);
    data.forEach(function(d){
        d.personality = d.personality;
        d.probability = d.probability;
    });
    
    // main config
    var w = 1000,
        h = 800,
        outerRadius = 300,
        innerRadius = 80;
    var x = w / 2,
        y = h / 2;

    // pie chart config
    var pie = d3.layout.pie()
            .value(function(d){ return d.probability;})
            .sort(null)
            .pad    
                
    //arc config
    var arc = d3.svg.arc()
                    .innerRadius(innerRadius)
                    .outerRadius(outerRadius);

    // create SVG element
    var svg = d3.select("#chart")
                .append("svg")
                .attr("height", h)
                .attr("width", w);

    // set up groups
    var arcs = svg.selectAll("g.arc")
                    .data(pie(data))
                    .enter()
                    .append("g")
                    .attr("class", "arc")
                    .attr("transform", "translate("+x+ "," + y+")");
                
    // draw arc paths
    arcs.append("path")
        .attr("d",arc)
        .attr("stroke","black");

    // label arcs
    arcs.append("svg:text")
        .attr("transform", function(d, i) {
            var c = arc.centroid(d);
            return "translate(" + (c[0]*2-30)+","+c[1]*2+")";
        })
        .style("fill", "black")
        .style("font", "bold 14px Arial")
        .text(function(d, i) { 
            return data[i].personality; 
        });

    arcs.append("svg:text")
        .attr("transform", function(d, i) {
            var c = arc.centroid(d);
            return "translate(" + c[0]+","+c[1]+")";
        })
        .style("fill", "white")
        .style("font", "bold 12px Arial")
        .text(function(d, i){ return d3.round(data[i].probability,2); });

};

