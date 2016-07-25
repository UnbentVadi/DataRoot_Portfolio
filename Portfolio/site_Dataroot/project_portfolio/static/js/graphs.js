google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);
function drawChart() {

	var data1 = google.visualization.arrayToDataTable([
		['status', 'count'],
		['Finish', 7],
		['Processing', 7],
		['New', 7],
	]);

	var data2 = google.visualization.arrayToDataTable([
			['month', 'count'],
			['May', 2],
			['June', 5],
			['July', 4]
		]);

	
	var options1 = {
		legend : 'none',
		colors : ['#4DA544', '#7B7B7C', '#000'],
		pieSliceBorderColor : 'none',
		pieSliceTextStyle : {color: '#ccc', fontSize: 20},
		tooltip : {trigger: 'none'},
		chartArea : {top:"50",right: "200", width:'280', height:'280'}
}

	var options2 = {
		legend: "none",
		areaOpacity : "0.7",
		colors: ['#499E41'],
		chartArea : {top:"50",  width:'480', height:'270'}
	};

	var chart1 = new google.visualization.PieChart(document.getElementById('graph-circle'));

	var chart2 = new google.visualization.AreaChart(document.getElementById('graph-area'));
		


	chart1.draw(data1, options1);
	chart2.draw(data2, options2);
}
