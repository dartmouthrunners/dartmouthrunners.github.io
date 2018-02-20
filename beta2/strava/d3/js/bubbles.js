(function() {

   // Define the height and width of the SVG
   var parent = d3.select('div.strava-kms-crushed');
   var width = parent.node().getBoundingClientRect().width,
       height = parent.node().getBoundingClientRect().height;

   // Define the center of the SVG
   var center = {
      x: width / 2,
      y: height / 2
   };

   // Select the div to plot the SVG
   var svg = d3.select("#strava-kms")
      .append("svg")
      .attr("height", height)
      .attr("width", width)
      .append("g");

   // Initialize the svg definitions and other D3 parameters
   var defs = svg.append("defs");
   var radiusScale = d3.scalePow().domain([1, 1]).exponent(0.5).range([1, 65]);
   var forceStrength = 0.03;

   // Define the force simulation
   var simulation = d3.forceSimulation()
       .velocityDecay(0.2)
       .force("x", d3.forceX().strength(forceStrength).x(center.x))
       .force("y", d3.forceY().strength(forceStrength).y(center.y))
       .force("collide", d3.forceCollide(function(d) { return radiusScale(d.distance) + 1 }))

   // read the data and await calling of the 'ready' function
   d3.queue().defer(d3.csv, "strava/data/recent_activities.csv").await(ready);

   //
   function ready(error, data) {
      var maxAmount = d3.max(data, function(d) { return +d.distance; });
          radiusScale.domain([0, maxAmount]);

      // create a new SVG definition for each athlete
      defs.selectAll(".athlete-pattern")
         .data(data)
         .enter().append("pattern")
         .attr("class", "athlete-pattern")
         .attr("id", function(d) { return 'profile_' + d.id })
         .attr("height", "100%")
         .attr("width", "100%")
         .attr("patternContentUnits", "objectBoundingBox")
         .append("image")
         .attr("height", 1)
         .attr("width", 1)
         .attr("preserveAspectRatio", "none")
         .attr("xmlns:xlink", "http://www.w3.org/1999/xlink")
         .attr("xlink:href", function(d) { return d.profile });

      // append a circle for each athlete with their profile image as the fill
      var circles = svg.selectAll(".athlete")
         .data(data)
         .enter().append("circle")
         .attr("class", "athlete")
         .attr("r", function(d) { return radiusScale(d.distance) })
         .attr("stroke", '#90FFC4')
         .attr("stroke-width", "4")
         .attr("fill", function(d) { return 'url(#profile_' + d.id + ')'})
         .attr('fill-opacity', '.8')
         .on('mouseover', showDetail)
         .on('mouseout', hideDetail);

      // define the moseover function
      function showDetail(d) {
         d3.select(this)
            .attr('stroke-width', '8')
            .attr('fill-opacity', '1')
            .append('svg:title')
            .text(function(d) { return d.name; });
      }

      // define the mouseout function
      function hideDetail(d) {
         d3.select(this)
            .attr('stroke-width', '4')
            .attr('fill-opacity', '.8');
      }

      // helper function for the simulation
      function ticked() {
         circles.attr("cx", function(d) { return d.x })
                .attr("cy", function(d) { return d.y })
      }

      // run the simulation
      simulation.nodes(data).on('tick', ticked);

      // include a toolbar for the hover
      $('svg circle').tipsy({
         gravity: 'w',
         html: true,
         opacity: 1,
         title: function() {
            var d = this.__data__, name = d.firstname, dist = Math.round(d.distance / 1000);
            return name  + ' has run ' + dist + ' KMs this month!';
         }
      });
   }
})();
