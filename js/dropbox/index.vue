<template>
	<section class="py-6 px-6">
		<div class="rounded-lg bg-white p-6 pb-12 shadow-lg">
			<header class="flex justify-between py-4 mb-4 border-b-2 border-blue-500">
				<h1 class="text-5xl font-bold">Dropboxes</h1>
			</header>
			<div v-if="!loading" v-for="(course, name) in items">
				<h2 class="w-full text-lg border-b mt-6 mb-2 py-2 font-bold">{{ name }}</h2>
				<table class="w-full">
					<tr v-for="item in course">
						<td class="align-top w-1/2 py-4">
							<a class="text-xl" target="_blank">{{ item.title }}</a>
						</td>
						<td class="align-top py-4">
							<span v-if="item.latest_submission">{{item.num_of_submissions}} submissions</span>
							<br>
							<span v-if="item.latest_submission">Last Submitted: {{ item.latest_submission }}</span>
						</td>
						<td class="text-right py-4">
							<div v-if="!item.latest_submission">
								<button class="uppercase text-sm py-2 px-4 bg-blue-500 text-white rounded font-bold mb-2">Add to checklist</button>
							</div>
							<span>Closed by <strong>{{ item.due_on }}</strong></span>
						</td>
					</tr>
				</table>
			</div>
		</div>
	</section>
</template>

<script>
import Request from '../api/DropboxRequest';

export default {
	data() {
		return {
			loading: true,
			items: {
				// 'CPSC 329': [
				// 	{
				// 		title: 'Worksheet 5',
				// 		submitted_on: '2/10/2021',
				// 		due_on: 'Tomorrow',
				// 		link: 'https://devcop.brightspace.com'
				// 	},
				// ],
				// 'CPSC 359': [
				// 	{
				// 		title: 'Project Part 1',
				// 		submitted_on: null,
				// 		due_on: '2/24/2021',
				// 		link: 'https://devcop.brightspace.com'
				// 	},
				// ],
				// 'STAT 213': [
				// 	{
				// 		title: 'Assignment 3',
				// 		submitted_on: '2/11/2021',
				// 		due_on: 'Tomorrow',
				// 		link: 'https://devcop.brightspace.com'
				// 	},
				// ]
			}
		};
	},


	methods: {
		retrieve() {
			let request = new Request({});

			request.retrieve().then(response => {
		        this.items = response;
		        this.loading = false;
		    });
		}
	},

	created() {
		this.retrieve();
	}
}
</script>