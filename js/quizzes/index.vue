<template>
	<section class="py-6 px-6">
		<div class="rounded-lg bg-white p-6 pb-12 shadow-lg">
			<header class="flex justify-between py-4 mb-4 border-b-2 border-blue-500">
				<h1 class="text-5xl font-bold">Quizzes</h1>
			</header>
			<div>
				<!-- <h2 class="w-full text-lg border-b mt-6 mb-2 py-2 font-bold">{{ name }}</h2> -->
				<table class="w-full">
					<tr v-for="item in items">
						<td class="align-top w-1/2 py-4">
							<a class="text-xl" target="_blank">{{ item.title }}</a>
						</td>
						<td class="align-top py-4">
							<span v-if="item.num_of_attempts > 0">Attempts: {{ item.num_of_attempts }}</span>
						</td>
						<td class="text-right pb-4 py-4">
							<div v-if="item.num_of_attempts">
								<button @click="createChecklistItem(`Study for ${item.title} (Quiz)`, item.end_date)" class="uppercase text-sm py-2 px-4 bg-blue-500 text-white rounded font-bold mb-2">Add to checklist</button>
							</div>
							<span>Closed by <strong>{{ item.end_date }}</strong></span>
						</td>
					</tr>
				</table>
			</div>
		</div>
	</section>
</template>

<script>
import axios from 'axios';
import ChecklistRequest from '../api/ChecklistRequest';

export default {
	data() {
		return {
			items: {
			}
		};
	},

	methods: {
		retrieve() {
			axios.get('http://127.0.0.1:5000/quizzes', {
			}).then((response) => {
				this.items = response.data;
			});
		},

		createChecklistItem(title, date) {
			let request = new ChecklistRequest({
				title: title,
				duedate: date,
			});
			request.store().then((response) => {
				this.retrieve();
			});
		}
	},

	created() {
		this.retrieve();
	}
}
</script>