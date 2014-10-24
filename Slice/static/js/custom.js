$(document).ready(function(){

	$('#id_start_date').datetimepicker({
	 lang:'en',
	 i18n:{
	  de:{
	   months:[
	    'January','Feburary','March','April',
	    'May','June','July','August',
	    'September','October','November','December',
	   ],
	   dayOfWeek:[
	    "Sun", "Mon", "Tue", "Wed", 
	    "Thur", "Fri", "Sat",
	   ]
	  }
	 },
	 format: 'd/m/Y H:i',
	});

	$('#id_end_date').datetimepicker({
	 lang:'en',
	 i18n:{
	  de:{
	   months:[
	    'January','Feburary','March','April',
	    'May','June','July','August',
	    'September','October','November','December',
	   ],
	   dayOfWeek:[
	    "Sun", "Mon", "Tue", "Wed", 
	    "Thur", "Fri", "Sat",
	   ]
	  }
	 },
	 format: 'd/m/Y H:i',
	});

});
