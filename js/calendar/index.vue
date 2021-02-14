<template>
	<section class="py-6 px-6">
		<div id="calendar" class="rounded-lg bg-white p-6 pb-12 shadow-lg""></div>
	</section>
</template>

<script>
import { Calendar } from '@fullcalendar/core';
import dayGridPlugin from '@fullcalendar/daygrid';
import timeGridPlugin from '@fullcalendar/timegrid';
import listPlugin from '@fullcalendar/list';

export default {
	data() {
		return {

		};
	},

	mounted() {
		const calendarEl = document.getElementById('calendar');

		let calendar = new Calendar(calendarEl, {
			plugins: [ dayGridPlugin, timeGridPlugin, listPlugin ],
			initialView: 'dayGridMonth',
			headerToolbar: {
			left: 'prev,next today',
			center: 'title',
			right: 'dayGridMonth,timeGridWeek,listWeek'
			},
		  	events: [
				{
					title: 'Submit Worksheet 5 (CPSC 329 Dropbox)',
					start: '2021-02-14',
				},
	    	]
		});

		calendar.render();	
	}
}
</script>