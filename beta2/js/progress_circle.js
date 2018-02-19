
d3.csv('data/recent_activities.csv', function(data){

   var parent = d3.select('div#everest-tracker');
   var color = '#90FFC4';
   var radius = parent.node().getBoundingClientRect().width / 2;
   var border = 7.5;
   var padding = 5;
   var startPercent = 0;

   var totalElev = d3.sum(data.map(function(d){ return d.elevation}));
   var endPercent = totalElev / 8848;

   var twoPi = Math.PI * 2;
   var formatPercent = d3.format('.0%');
   var boxSize = (radius + padding) * 2;
   var width = boxSize;
   var height = boxSize;

   var count = Math.abs((endPercent - startPercent) / 0.01);
   var step = endPercent < startPercent ? - 0.01 : 0.01;

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
       .attr('class', 'everest-tracker')
       .attr('transform', 'translate(' + boxSize / 2 + ',' + boxSize / 2 + ')');

   var everestImg = g.append('image')
       .attr("xlink:href", "img/003-mountain-1.svg")
       .attr('width', boxSize / 2)
       .attr('height', boxSize / 2)
       .attr('x', -(boxSize/4))
       .attr('y', -(boxSize/4 + 3*padding));

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
       .attr('dy', radius - 4*padding);

   function updateProgress(progress) {
       foreground.attr('d', arc.endAngle(twoPi * progress));
       front.attr('d', arc.endAngle(twoPi * progress));
       numberText.text(formatPercent(progress));
   }

   var progress = startPercent;

   $(window).scroll(function() {
   var hT = $('#strava').offset().top,
       hH = $('#strava').outerHeight(),
       wH = $(window).height(),
       wS = $(this).scrollTop();
   if (wS > (hT+hH-wH)){
      (function loops() {
          updateProgress(progress);
          if (count > 0) {
             count--;
             progress += step;
             setTimeout(loops, 200);
          }
      })();
   }
   });
});
