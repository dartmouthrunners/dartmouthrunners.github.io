function drawCircle() {
   d3.csv('strava/data/recent_activities.csv', function(data) {

      var parent = d3.select('div.strava-elevation');
      var parentWidth = parent.node().getBoundingClientRect().width
      var parentHeight = parent.node().getBoundingClientRect().height
      var color = '#90FFC4';

      if (parentWidth < 378) {
         var radius = (Math.min(parentWidth * 0.85, parentHeight * 0.85)) / 2;
      } else {
         var radius = (Math.min(parentWidth * 0.90, parentHeight * 0.90)) / 2;
      }

      var border = 5;
      var padding = 10;
      var startPercent = 0;

      var totalElev = d3.sum(data.map(function(d) {
         return d.elevation
      }));
      var endPercent = totalElev / 8848;

      var twoPi = Math.PI * 2;
      var formatPercent = d3.format('.0%');
      var boxSize = (radius + padding) * 2;
      var width = boxSize;
      var height = boxSize;

      var count = Math.abs((endPercent - startPercent) / 0.01);
      var step = endPercent < startPercent ? -0.01 : 0.01;

      var arc = d3.arc()
         .startAngle(0)
         .innerRadius(radius)
         .outerRadius(radius - border);

      var svg = parent.append('svg')
         .attr('width', width)
         .attr('height', height);

      var defs = svg.append('defs');

      var filter = defs.append('filter')
         .attr('id', 'blur');

      filter.append('feGaussianBlur')
         .attr('in', 'SourceGraphic')
         .attr('stdDeviation', '4');

      var g = svg.append('g')
         .attr('class', 'everest')
         .attr('transform', 'translate(' + boxSize / 2 + ',' + boxSize / 2 + ')');

      var everestImg = g.append('image')
         .attr("xlink:href", "img/003-mountain-1.svg")
         .attr('width', boxSize / 2)
         .attr('height', boxSize / 2)
         .attr('x', -(boxSize / 4))
         .attr('y', -(boxSize / 4 + 3 * padding));

      var meter = g.append('g')
         .attr('class', 'progress-meter');

      meter.append('path')
         .attr('class', 'background')
         .attr('fill', '#ccc')
         .attr('fill-opacity', 0.5)
         .attr('d', arc.endAngle(twoPi));

      var foreground = meter.append('path')
         .attr('class', 'foreground')
         .attr('fill', color)
         .attr('fill-opacity', 1)
         .attr('stroke', color)
         .attr('stroke-width', 5)
         .attr('stroke-opacity', 1)
         .attr('filter', 'url(#blur)');

      var front = meter.append('path')
         .attr('class', 'foreground')
         .attr('fill', color)
         .attr('fill-opacity', 1);

      var numberText = g.append('text')
         .attr('fill', '#343E5A')
         .attr('text-anchor', 'middle')
         .attr('dx', padding)
         .attr('dy', radius - 4 * padding);

      function updateProgress(progress) {
         foreground.attr('d', arc.endAngle(twoPi * progress));
         front.attr('d', arc.endAngle(twoPi * progress));
         numberText.text(formatPercent(progress));
      }

      var progress = startPercent;

      (function loops() {
         updateProgress(progress);
         if (count > 0) {
            count--;
            progress += step;
            setTimeout(loops, 10);
         }
      })();
   });

   firstScroll = true;
}

function drawBubbles() {

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

   if (width < 378) {
      var radiusScale = d3.scalePow().domain([1, 1]).exponent(0.5).range([1, 65]);
   } else {
      var radiusScale = d3.scalePow().domain([1, 1]).exponent(0.5).range([1, 85]);
   }

   var forceStrength = 0.03;

   // Define the force simulation
   var simulation = d3.forceSimulation()
      .velocityDecay(0.2)
      .force("x", d3.forceX().strength(forceStrength).x(center.x))
      .force("y", d3.forceY().strength(forceStrength).y(center.y))
      .force("collide", d3.forceCollide(function(d) {
         return radiusScale(d.distance) + 1
      }))

   // read the data and await calling of the 'ready' function
   d3.queue().defer(d3.csv, "strava/data/recent_activities.csv").await(ready);

   //
   function ready(error, data) {
      var maxAmount = d3.max(data, function(d) {
         return +d.distance;
      });
      radiusScale.domain([0, maxAmount * 1.25]);

      // create a new SVG definition for each athlete
      defs.selectAll(".athlete-pattern")
         .data(data)
         .enter().append("pattern")
         .attr("class", "athlete-pattern")
         .attr("id", function(d) {
            return 'profile_' + d.id
         })
         .attr("height", "100%")
         .attr("width", "100%")
         .attr("patternContentUnits", "objectBoundingBox")
         .append("image")
         .attr("height", 1)
         .attr("width", 1)
         .attr("preserveAspectRatio", "none")
         .attr("xmlns:xlink", "http://www.w3.org/1999/xlink")
         .attr("xlink:href", function(d) {
            return d.profile
         });

      // append a circle for each athlete with their profile image as the fill
      var circles = svg.selectAll(".athlete")
         .data(data)
         .enter().append("circle")
         .attr("class", "athlete")
         .attr("r", function(d) {
            return radiusScale(d.distance)
         })
         .attr("stroke", '#90FFC4')
         .attr("stroke-width", "4")
         .attr("fill", function(d) {
            return 'url(#profile_' + d.id + ')'
         })
         .attr('fill-opacity', '.8')
         .on('mouseover', showDetail)
         .on('mouseout', hideDetail);

      // define the moseover function
      function showDetail(d) {
         d3.select(this)
            .attr('stroke-width', '8')
            .attr('fill-opacity', '1')
            .append('svg:title')
            .text(function(d) {
               return d.name;
            });
      }

      // define the mouseout function
      function hideDetail(d) {
         d3.select(this)
            .attr('stroke-width', '4')
            .attr('fill-opacity', '.8');
      }

      // helper function for the simulation
      function ticked() {
         circles.attr("cx", function(d) {
               return d.x
            })
            .attr("cy", function(d) {
               return d.y
            })
      }

      // run the simulation
      simulation.nodes(data).on('tick', ticked);

      // include a toolbar for the hover
      $('svg circle').tipsy({
         html: true,
         opacity: 1,

         title: function() {
            var d = this.__data__,
               name = d.firstname,
               dist = Math.round(d.distance / 1000);
            return name + ' has run ' + dist + ' KMs this month!';
         }
      });
   }
}


var firstScroll = false;

$(window).on('scroll', function() {
   if (isScrolledIntoView('#strava-kms') && !firstScroll) {
      drawCircle();
      drawBubbles();
   }
});

// The function to check if div.animation_container is scrolled into view
function isScrolledIntoView(elem) {
   var docViewTop = $(window).scrollTop();
   var docViewBottom = docViewTop + $(window).height();

   var elemTop = $(elem).offset().top;
   var elemBottom = elemTop + $(elem).height();

   return ((elemTop <= docViewBottom) && (elemTop >= docViewTop));
}
