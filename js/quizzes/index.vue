<template>
	<section class="py-6 px-6">
		<div class="rounded-lg bg-white p-6 pb-12 shadow-lg">
			<header class="flex justify-between py-4 mb-4 border-b-2 border-blue-500">
				<h1 class="text-5xl font-bold">Quizzes</h1>
			</header>
			<div v-for="(course, name) in items">
				<h2 class="w-full text-lg border-b mt-6 mb-2 py-2 font-bold">{{ name }}</h2>
				<table class="w-full">
					<tr v-for="item in course">
						<td class="align-top w-1/2">
							<a class="text-xl" :href="item.link" target="_blank">{{ item.title }}</a>
						</td>
						<td class="align-top">
							<span v-if="item.submitted_on">Submitted: {{ item.submitted_on }}</span>
						</td>
						<td class="text-right pb-4">
							<div v-if="!item.submitted_on">
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

export default {
	data() {
		return {
			items: {
				'CPSC 329': [
					{
						title: 'Quiz 1',
						submitted_on: '2/11/2021',
						due_on: 'Tomorrow',
						link: 'https://devcop.brightspace.com'
					},
				],
				'STAT 213': [
					{
						title: 'Lab Quiz 2',
						submitted_on: '2/11/2021',
						due_on: 'Tomorrow',
						link: 'https://devcop.brightspace.com'
					},
				]
			}
		};
	},
}
</script>