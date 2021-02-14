<template>
	<section class="py-6 px-6">
		<div class="rounded-lg bg-white p-6 pb-12 shadow-lg">
			<header class="flex justify-between py-4 mb-4 border-b-2 border-blue-500">
				<h1 class="text-5xl font-bold">Shells ({{ items.length }})</h1>
				<button class="text-3xl font-bold hover:text-blue-500 focus:outline-none" @click="createItem">+ Add a shell</button>
			</header>
			<table class="w-full">
				<tr v-for="(item, new_index) in items">
					<td class="text-xl py-4">
						<a :href="`https://devcop.brightspace.com/d2l/le/content/${item.id}/Home`" target="_blank">{{ item.title }}</a>
					</td>
					<td class="uppercase text-right">Shell id: {{ item.id }}</td>
				</tr>
				<tr v-show="showCreateItem">
					<td colspan="3">
						<input ref="item_title" v-model="new_item.id" @blur="cancel" @keyup.13="submit" class="w-full py-2 px-2 text-xl border-b-2" type="text" name="title" placeholder="Enter shell id">
					</td>
				</tr>
			</table>
		</div>
	</section>
</template>

<script>
import Request from '../api/Request.js';

export default {
	data() {
		return {
			showCreateItem: false,
			new_item: {
				id: ''
			},
			new_items: [
				'Computer Machinery',
				'Statistics',
				'Software Engineering',
				'Information Ethics',
			],
			new_index: 0,
			items: [
				{
					id: 7855,
					title: 'Computer Basics',
				},
				{
					id: 7032,
					title: 'Physics',
				},
			]
		};
	},

	methods: {
		createItem() {
			this.showCreateItem = true;
			this.$nextTick(() => {
    			this.$refs.item_title.focus();
			})
			
		},
		submit() {
			this.items.push({
				id: this.new_item.id,
				title: this.new_items[this.new_index++]
			});

			this.new_item.id = '';

			this.$refs.item_title.blur();
			this.showCreateItem = false;
		},
		cancel() {
			this.$refs.item_title.blur();
			this.showCreateItem = false;
		},
		checkItem() {

		},
		deleteItem(index) {
			array.splice(index, 1);
		}
	}
}
</script>