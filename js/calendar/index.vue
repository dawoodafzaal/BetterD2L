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
import interactionPlugin from '@fullcalendar/interaction';

import Request from '../api/ChecklistRequest.js';

export default {
	data() {
		return {
			items: []
		};
	},

	methods: {
		retrieve() {
			let request = new Request({});

			request.retrieve().then(response => {
		        this.items = response;
		        this.loading = false;

		        var i;
				for(i = 0; i < this.items.length; i++){
				    this.items[i].start = this.items[i]['duedate'];
				    delete this.items[i].duedate;
				}

				console.log(this.items);

				const calendarEl = document.getElementById('calendar');



				let calendar = new Calendar(calendarEl, {
					plugins: [ interactionPlugin, dayGridPlugin, timeGridPlugin, listPlugin ],
					initialView: 'dayGridMonth',
					editable: true,
					headerToolbar: {
					left: 'prev,next today',
					center: 'title',
					right: 'dayGridMonth,timeGridWeek,listWeek'
					},
				  	events: this.items
				});

				calendar.render();	
		    });
		},
	},

	created() {
		this.retrieve()
	},

	mounted() {
		const calendarEl = document.getElementById('calendar');

		let events;



		let calendar = new Calendar(calendarEl, {
			plugins: [ interactionPlugin, dayGridPlugin, timeGridPlugin, listPlugin ],
			initialView: 'dayGridMonth',
			editable: true,
			headerToolbar: {
			left: 'prev,next today',
			center: 'title',
			right: 'dayGridMonth,timeGridWeek,listWeek'
			},
		  	events: this.items
		});

		calendar.render();	
	}
}
</script>