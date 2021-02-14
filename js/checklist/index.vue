<template>
	<section class="py-6 px-6">
		<div class="rounded-lg bg-white p-6 pb-12 shadow-lg">
			<header class="flex justify-between py-4 mb-4 border-b-2 border-blue-500">
				<h1 class="text-5xl font-bold">Reminders ({{ items.length }})</h1>
				<button class="text-3xl font-bold hover:text-blue-500 focus:outline-none" @click="createItem">+ New reminder</button>
			</header>
			<table class="w-full">
				<tr v-for="item in items">
					<td class="w-2"><md-checkbox v-model="item.checkedat" @change="checkItem(item.id, true)"></md-checkbox></td>
					<td class="text-xl">
						<a v-if="item.link != 'None'" target="_blank" :href="item.link">{{ item.title }}</a>
						<span v-else>{{ item.title }}</span>
					</td>
					<td class="uppercase text-right">
						<span><strong>Due Date: </strong>{{ item.duedate }}</span>
					</td>
					<td class="text-right">
						<button class="bg-red-500 text-white rounded py-4 px-2 font-semibold" @click="deleteItem(item.id)">Delete Reminder</button>
					</td>
				</tr>
				<tr v-show="showCreateItem">
					<td colspan="4">
						<div class="flex justify-between mt-8">
							<div class="flex flex-grow">
								<input ref="item_title" v-model="new_item.title" class="flex-grow py-2 px-2 text-xl border-b-2" type="text" name="title" placeholder="">
								<input class="border-b-2 text-xl py-2 px-2" ref="item_date" v-model="new_item.duedate" type="date">
							</div>
							<button @click="submit" class="text-lg py-2 px-4 text-white bg-green-500 rounded font-semibold">Add Reminder</button>
						</div>
					</td>
				</tr>
			</table>
		</div>
	</section>
</template>

<script>
import Request from '../api/ChecklistRequest.js';
import axios from 'axios';

export default {
	data() {
		return {
			showCreateItem: false,
			showEditDate: false,
			loading: true,
			new_item: {
				title: '',
				duedate: ''
			},
			new_date: '',
			items: [
				{
					id: 1,
					title: 'Submit Worksheet 5 (CPSC 329 Dropbox)',
					related: {
						type:'dropbox',
						id: 1
					},
					checked_at: false,
					due_on: 'Tomorrow',
				},
				{
					id: 2,
					title: 'Start Computing Machinery Project',
					checked_at: true,
					due_on: 'Yesterday',
				},
				{
					id: 3,
					title: 'Study for STAT 213',
					checked_at: true,
					due_on: 'Tomorrow',
				},
				{
					id: 4,
					title: 'Clean desk',
					checked_at: false,
					due_on: 'Last Week',
				},
			]
		};
	},

	methods: {
		retrieve() {
			let request = new Request({});

			request.retrieve().then(response => {
		        this.items = response;
		        this.loading = false;
		    });
		},
		createItem() {
			this.showCreateItem = true;
			this.$nextTick(() => {
    			this.$refs.item_title.focus();
			});
			
		},
		updatedate(id, date) {
			axios.patch('http://127.0.0.1:5000/checklist', {
				data: JSON.stringify({
					'id': id,
					'duedate': date
				})
			}).then((response) => {
				this.retrieve();
			});
		},
		submit() {
			let request = new Request(this.new_item);
			request.store().then((response) => {
				this.retrieve();
				this.showCreateItem = false;
			});

			this.new_item.title = '';
		},
		cancel() {
			this.$refs.item_title.blur();
			this.showCreateItem = false;
		},
		checkItem(id, checked) {
			let d = new Date();
  			let n = d.toISOString();

			axios.patch('http://127.0.0.1:5000/checklist', {
				data: JSON.stringify({
					id: id,
					checkedat: n
				})
			}).then((response) => {
				// this.retrieve();
			});
		},
		deleteItem(id) {
			axios.delete('http://127.0.0.1:5000/checklist', {
				data: JSON.stringify({
					'id': id
				})
			}).then((response) => {
				this.retrieve();
			});
		}
	},

	created() {
		this.retrieve();
	}
}
</script>