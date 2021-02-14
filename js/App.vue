<template>
	<div>
		<nav class="fixed h-screen w-1/4 bg-blue-600 shadow-lg">
			<section class="px-8 py-4">
				<div class="grid grid-cols-2 gap-4">
					<div class="py-16 bg-blue-500 rounded-lg text-white text-center">
						<router-link style="color: white;" to="/calendar" class="text-lg font-bold text-white">
							<svg class="w-6 h-6 align-top inline-block" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
</svg>
						Calendar</router-link>
					</div>
					<div class="py-16 bg-blue-500 rounded-lg text-white text-center">
						<router-link style="color: white;" to="/checklist" class="text-lg font-bold text-white">
							<svg class="w-6 h-6 align-top inline-block" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4" />
</svg>
						Checklist</router-link>
					</div>
					<div class="py-16 bg-blue-500 rounded-lg text-white text-center">
						<router-link style="color: white;" to="/communication" class="text-lg font-bold text-white">
							<svg class="w-6 h-6 align-top inline-block" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
  <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
</svg>
						Quizzes</router-link>
					</div>
					<div class="py-16 bg-blue-500 rounded-lg text-white text-center">
						<router-link style="color: white;" to="/dropbox" class="text-lg font-bold text-white">
							<svg class="w-6 h-6 align-top inline-block" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
</svg>
						Dropbox</router-link>
					</div>
				</div>
			</section>
		</nav>
		<section class="bg-gray-200 w-3/4 min-h-screen" style="margin-left: 25%;">
			<nav class="flex w-full py-8 px-6 bg-white shadow justify-between">
				<div>
					<h1 class="text-3xl font-bold">BetterD2L</h1>
				</div>
				<div class="text-xl font-semibold pr-4 pl-2">Hello, {{ firstName }} {{ lastName }}</div>
			</nav>
			<router-view></router-view>
		</section>
	</div>
</template>

<script>
import axios from 'axios';

export default {
	data() {
		return {
			firstName: '',
			lastName: ''
		};
	},

	created() {
		var config = {
		method: 'get',
		url: 'https://devcop.brightspace.com/d2l/api/lp/1.28/users/whoami',
		headers: { 
			'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjYzYzc5ZjIzLWZiMTAtNGI4YS1hMjdlLWI4YTc4NGJmNWI5MCJ9.eyJpc3MiOiJodHRwczovL2FwaS5icmlnaHRzcGFjZS5jb20vYXV0aCIsImF1ZCI6Imh0dHBzOi8vYXBpLmJyaWdodHNwYWNlLmNvbS9hdXRoL3Rva2VuIiwiZXhwIjoxNjEzMjg1NTI5LCJuYmYiOjE2MTMyODE5MjksInN1YiI6IjE5NSIsInRlbmFudGlkIjoiNTI3MzEzMTctMzcyYS00ZGI0LWI0OWQtNDk1MDJjZTQzZjJiIiwiYXpwIjoiNWQyNzQ1MGYtMmNlOS00ZGNlLTk1NzAtMGIyMzQ1ODBkZmRkIiwic2NvcGUiOiJjb250ZW50Oio6KiBjb3JlOio6KiBkYXRhaHViOio6KiBkaXNjdXNzaW9uczoqOiogZW5yb2xsbWVudDoqOiogZ3JhZGVzOio6KiBxdWl6emluZzoqOiogcmVwb3J0aW5nOio6KiByb2xlOio6KiB1c2VyczoqOioiLCJqdGkiOiIxNGI2Njk5Mi0xNTlhLTRmMzYtYTYyZi1kOTg5YzE4NDE4ZDIifQ.bKbpi3zugXsxh7QoLaKMYog4wYZEIML0E1xDg3KJI3QTuMet8RSmEWlo_aUN-XFULl_Bs2ZLcqzkWH9okdSLMcI_-WpZyAG53kaBi7tJIxHfRFmmWVQAZWYtXz8A4YqcUf-cs6U4kaqnlpSXb6doZKGXfTI8hMoVCOmzT_-YCZuWxGqALiTTzP6FRxj8xVk2pKnzZ3COAaI_5iMGd4w4ie-YlETmM0u3mPOBO3IJX1LnlYPZubnGNWOLpFG5aFZrFfXGDtQUxOAFgT2c5MU75izpOMWiZ1ADpS4Q97H8s3tduirKQSnuNfHO11uE33PLVfwEcnkGDOr0dcrVzg34Ow'
		}
		};

		axios(config)
		.then((response) => {
		  this.firstName = response.data.FirstName;
		  this.lastName = response.data.LastName;
		})
		.catch((error) => {
		  console.log(error);
		});
	}
}
</script>