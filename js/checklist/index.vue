<template>
	<div class="py-8 px-8">
		<header class="text-center">
			<h1 class="text-5xl border-b-2 border-blue-600 font-bold">Checklist</h1>
		</header>
		<table class="w-full">
			<tr v-for="item in items">
				<td><md-checkbox v-model="item.checked_at"></md-checkbox></td>
				<td class="text-xl">
					<router-link v-if="item.related" :to="`${item.related.type}/${item.related.id}`">{{ item.title }}</router-link>
					<span v-else>{{ item.title }}</span>
				</td>
				<td class="uppercase text-right">{{ item.due_on }}</td>
			</tr>
		</table>
	</div>
</template>

<script>
export default {
	data() {
		return {
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
}
</script>