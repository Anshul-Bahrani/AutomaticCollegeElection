myData = $('#takeData').val();
if(myData != null) {
    console.log(myData);
    parsedData = JSON.parse(myData);
    console.log(parsedData);
    wannabelabels = []
    for(var i = 0;i<parsedData.length;i ++) {
      if(wannabelabels.indexOf(parsedData[i][2]) == -1) {
        wannabelabels.push(parsedData[i][2]);
      }
    }
    console.log(wannabelabels);
    wannabedata = []
    for(var i = 0;i<parsedData.length;i ++) {
      if(wannabedata.indexOf(parsedData[i][0]) == -1) {
        wannabedata.push(parsedData[i][0]);
      }
    }
    console.log(wannabedata);
    function zeros(dimensions) {
      var array = [];

      for (var i = 0; i < dimensions[0]; ++i) {
          array.push(dimensions.length == 1 ? 0 : zeros(dimensions.slice(1)));
      }

      return array;
    }
    final = zeros([wannabedata.length, wannabelabels.length]);

    for(var i = 0;i < parsedData.length;i++) {
      if(wannabedata.indexOf(parsedData[i][0]) != -1 && wannabelabels.indexOf(parsedData[i][2]) != -1) {

        final[wannabedata.indexOf(parsedData[i][0])][wannabelabels.indexOf(parsedData[i][2])] = parsedData[i][1];

      }
    }
    var data ={
      labels : wannabelabels,
      series : final
    };
  }
  else {
    var data ={
      labels: ['Post1', 'Post2', 'Post3', 'Post4', 'Post5', 'Post6', 'Post7', 'Post8', 'Post9', 'Post10', 'Post11', '12'],
      series: [
        [12, 9, 7, 8, 5, 4, 6, 2, 3, 3, 4, 6],
        [4,  5, 3, 7, 3, 5, 5, 3, 4, 4, 5, 5],
        [5,  3, 4, 5, 6, 3, 3, 4, 5, 6, 3, 4],
        [3,  4, 5, 6, 7, 6, 4, 5, 6, 7, 6, 3],

      ]
  };
  }
var options={
chartPadding: {
top : 10,
right : 10
}
};
var chart = new Chartist.Line('#linechart', data, options);

  // Let's put a sequence number aside so we can use it in the event callbacks
  var seq = 0,
    delays = 200,
    durations = 500;

  // Once the chart is fully created we reset the sequence
  chart.on('created', function() {
    seq = 0;
  });

  // On each drawn element by Chartist we use the Chartist.Svg API to trigger SMIL animations
  chart.on('draw', function(data) {
    seq++;

    if(data.type === 'line') {
      // If the drawn element is a line we do a simple opacity fade in. This could also be achieved using CSS3 animations.
      data.element.animate({
        opacity: {
          // The delay when we like to start the animation
          begin: seq * delays + 1000,
          // Duration of the animation
          dur: durations,
          // The value where the animation should start
          from: 0,
          // The value where it should end
          to: 1
        }
      });
    } else if(data.type === 'label' && data.axis === 'x') {
      data.element.animate({
        y: {
          begin: seq * delays,
          dur: durations,
          from: data.y + 100,
          to: data.y,
          // We can specify an easing function from Chartist.Svg.Easing
          easing: 'easeOutQuart'
        }
      });
    } else if(data.type === 'label' && data.axis === 'y') {
      data.element.animate({
        x: {
          begin: seq * delays,
          dur: durations,
          from: data.x - 100,
          to: data.x,
          easing: 'easeOutQuart'
        }
      });
    } else if(data.type === 'point') {
      data.element.animate({
        x1: {
          begin: seq * delays,
          dur: durations,
          from: data.x - 10,
          to: data.x,
          easing: 'easeOutQuart'
        },
        x2: {
          begin: seq * delays,
          dur: durations,
          from: data.x - 10,
          to: data.x,
          easing: 'easeOutQuart'
        },
        opacity: {
          begin: seq * delays,
          dur: durations,
          from: 0,
          to: 1,
          easing: 'easeOutQuart'
        }
      });
    } else if(data.type === 'grid') {
      // Using data.axis we get x or y which we can use to construct our animation definition objects
      var pos1Animation = {
        begin: seq * delays,
        dur: durations,
        from: data[data.axis.units.pos + '1'] - 30,
        to: data[data.axis.units.pos + '1'],
        easing: 'easeOutQuart'
      };

      var pos2Animation = {
        begin: seq * delays,
        dur: durations,
        from: data[data.axis.units.pos + '2'] - 100,
        to: data[data.axis.units.pos + '2'],
        easing: 'easeOutQuart'
      };

      var animations = {};
      animations[data.axis.units.pos + '1'] = pos1Animation;
      animations[data.axis.units.pos + '2'] = pos2Animation;
      animations['opacity'] = {
        begin: seq * delays,
        dur: durations,
        from: 0,
        to: 1,
        easing: 'easeOutQuart'
      };

      data.element.animate(animations);
    }
  });

  // For the sake of the example we update the chart every time it's created with a delay of 10 seconds
  chart.on('created', function() {
    if(window.__exampleAnimateTimeout) {
      clearTimeout(window.__exampleAnimateTimeout);
      window.__exampleAnimateTimeout = null;
    }
    window.__exampleAnimateTimeout = setTimeout(chart.update.bind(chart), 1200000);
  });







  // var data = {
  //   labels: ['Winner 1', 'Winner 2', 'Winner 3', 'Winner 4', 'Winner 5'],
  //   series: [
  //     [1, 2, 4, 8, 6]
  //   ]
  // };

  // var options = {
  //   high: 5,
  //   low: 0,
  //   axisX: {
  //     labelInterpolationFnc: function(value, index) {
  //       return value;
  //     }
  //   },
  //   seriesBarDistance: 30
  // };

  // var responsiveOptions = [
  //   ['screen and (max-width: 640px)', {
  //     seriesBarDistance: 5,
  //     axisX: {
  //       labelInterpolationFnc: function (value) {
  //         return value[0];
  //       }
  //     }
  //   }]
  // ];



  var data= {
    labels: ['Anshul Bahrani', 'Avinash Bhawnani', 'Devansh Ahuja', 'Priya Karsi', 'ABC'],
    series: [
      [12, 20, 100, 200, 5],

    ]
  };
  var option ={
    axisY: {
      onlyInteger: true
    },
    fullWidth: true,
    chartPadding: {
      top : 10,
      bottom: 0,
      left: 10,
    }
  };
  new Chartist.Bar('#bar-chart', data, option);

  var data = {

    series: [{
      value: 20,
      className: "cmpn"
    },
    {
      value: 10,
      className: "it"
    },
    {
      value: 30,
      className: "extc"
    },
    {
      value: 40,
      className: "etrx"
    }
  ]};


  var options = {
      donut: true,
      donutWidth: 50,
      showLabel: false,

    labelInterpolationFnc: function(value) {
      return value[0]
    }
  };

  var responsiveOptions = [
    ['screen and (min-width: 640px)', {
      chartPadding: 30,
      labelOffset: 100,
      labelDirection: 'explode',
      labelInterpolationFnc: function(value) {
        return value;
      }
    }],
    ['screen and (min-width: 1024px)', {
      labelOffset: 80,
      chartPadding: 0
    }]
  ];

  new Chartist.Pie('.ct-square', data, options, responsiveOptions);
