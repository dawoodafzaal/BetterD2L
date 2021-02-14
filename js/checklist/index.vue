<template>
	<section class="py-6 px-6">
		<div class="rounded-lg bg-white p-6 pb-12 shadow-lg">
			<header class="flex justify-between py-4 mb-4 border-b-2 border-blue-500">
				<h1 class="text-5xl font-bold">Reminders ({{ items.length }})</h1>
				<button class="text-3xl font-bold hover:text-blue-500 focus:outline-none" @click="createItem">+ New reminder</button>
			</header>
			<table class="w-full">
				<tr v-for="item in items">
					<td class="w-2"><md-checkbox v-model="item.checked_at"></md-checkbox></td>
					<td class="text-xl">
						<router-link v-if="item.related" :to="`${item.related.type}/${item.related.id}`">{{ item.title }}</router-link>
						<span v-else>{{ item.title }}</span>
					</td>
					<td class="uppercase text-right">{{ item.due_on }}</td>
				</tr>
				<tr v-show="showCreateItem">
					<td colspan="3">
						<input ref="item_title" @blur="cancel" class="w-full py-2 px-2 text-xl border-b-2" type="text" name="title" placeholder="">
					</td>
				</tr>
			</table>
		</div>
	</section>
</template>

<script>
export default {
	data() {
		return {
			showCreateItem: false,
			new_item: {
				title: '',
				due_on: ''
			},
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
		createItem() {
			this.showCreateItem = true;
			this.$nextTick(() => {
    			this.$refs.item_title.focus();
			})
			
		},
		submit() {

		},
		cancel() {
			this.$refs.item_title.blur();
			this.showCreateItem = false;
		},
		checkItem() {

		},
		deleteItem() {

		}
	}
}
</script>