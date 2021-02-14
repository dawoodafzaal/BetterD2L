<template>
	<div>
		<nav class="fixed h-screen w-1/4 bg-blue-600">
			<section class="px-8 py-4">
				<div class="grid grid-cols-2 gap-4">
					<div class="py-16 bg-blue-500 rounded-lg text-white text-center">
						<router-link to="/calendar" class="text-lg font-bold text-white">Calendar</router-link>
					</div>
					<div class="py-16 bg-blue-500 rounded-lg text-white text-center">
						<router-link to="/checklist" class="text-lg font-bold text-white">Checklist</router-link>
					</div>
					<div class="py-16 bg-blue-500 rounded-lg text-white text-center">
						<router-link to="/communication" class="text-lg font-bold text-white">Communication</router-link>
					</div>
					<div class="py-16 bg-blue-500 rounded-lg text-white text-center">
						<router-link to="/dropbox" class="text-lg font-bold text-white">Dropbox</router-link>
					</div>
				</div>
			</section>
		</nav>
		<section class="w-3/4 min-h-screen" style="margin-left: 25%;">
			<router-view></router-view>
		</section>
	</div>
</template>

<script>
export default {
	data: () => {
		return {

		};
	}
}
</script>