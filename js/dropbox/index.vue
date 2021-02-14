<template>
	<div class="py-8 px-8">
		<header class="text-center">
			<h1 class="text-5xl border-b-2 border-blue-600 font-bold">Dropboxes</h1>
		</header>
		<div v-for="(course, name) in items">
			<h2 class="w-full text-lg border-b mt-4 mb-2">{{ name }}</h2>
			<table class="w-full">
				<tr v-for="item in course">
					<td class="align-top">
						<a class="text-xl" :href="item.link" target="_blank">{{ item.title }}</a>
						<br>
						<span v-if="item.submitted_on">Submitted: {{ item.submitted_on }}</span>
					</td>
					<td class="text-right pb-4">
						<div v-if="!item.submitted_on">
							<button  class="uppercase text-sm py-2 px-4 bg-blue-500 text-white rounded">Add to checklist</button>
						</div>
						<span>Will be closed: <strong>{{ item.due_on }}</strong></span>
					</td>
				</tr>
			</table>
		</div>
	</div>
</template>

<script>
import axios from 'axios';

export default {
	data() {
		return {
			items: {
				'CPSC 329': [
					{
						title: 'Worksheet 5',
						submitted_on: '2/10/2021',
						due_on: 'Tomorrow',
						link: 'https://devcop.brightspace.com'
					},
				],
				'CPSC 359': [
					{
						title: 'Project Part 1',
						submitted_on: null,
						due_on: '2/24/2021',
						link: 'https://devcop.brightspace.com'
					},
				],
				'STAT 213': [
					{
						title: 'Assignment 3',
						submitted_on: '2/11/2021',
						due_on: 'Tomorrow',
						link: 'https://devcop.brightspace.com'
					},
				]
			}
		};
	},

	created() {
		

		const token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjYzYzc5ZjIzLWZiMTAtNGI4YS1hMjdlLWI4YTc4NGJmNWI5MCJ9.eyJpc3MiOiJodHRwczovL2FwaS5icmlnaHRzcGFjZS5jb20vYXV0aCIsImF1ZCI6Imh0dHBzOi8vYXBpLmJyaWdodHNwYWNlLmNvbS9hdXRoL3Rva2VuIiwiZXhwIjoxNjEzMjU0MjM1LCJuYmYiOjE2MTMyNTA2MzUsInN1YiI6IjEyNTUiLCJ0ZW5hbnRpZCI6IjUyNzMxMzE3LTM3MmEtNGRiNC1iNDlkLTQ5NTAyY2U0M2YyYiIsImF6cCI6IjVkMjc0NTBmLTJjZTktNGRjZS05NTcwLTBiMjM0NTgwZGZkZCIsInNjb3BlIjoiY29udGVudDoqOiogY29yZToqOiogZGF0YWh1YjoqOiogZGlzY3Vzc2lvbnM6KjoqIGVucm9sbG1lbnQ6KjoqIGdyYWRlczoqOiogcXVpenppbmc6KjoqIHJlcG9ydGluZzoqOiogcm9sZToqOiogdXNlcnM6KjoqIiwianRpIjoiNGUyOTdkYTEtZDg4Ni00ODI3LTgyN2ItZmE4OGM0MWM5ZjExIn0.k4ndXz5MuMjwu20AXhb6kpOwfVy-iClslOsm7XglIrzO1TKBy1key-iO0MDOhNrAC5A4CpZyWUk3VtOLL8DAM-RGRSXYxEBXpJ8Hnbb2kgUVtBU9ZB7kagfulIRihH5lgEIX08smsokviWowZVT2pUNWxBFpIoJjCdIoXTJ5NAis0pVTPa0EzjELnNFuSuGk91X8Jpv5Gh7sFzDerm9rgjHCzi6it3hW--7Mxh4Rpge8dbEinbC3ugbj4YeCorkScTH65prXGyzbovX1cuNAqTyst0sRxNC7PG0F__d-OW7Q--SYckrYSdMkkg8Q19g2UpQI9pbzk23tGifeFGlHlQ"

		// const instance = axios.create({
  // 			baseURL: 'https://devcop.brightspace.com',
	 //  		headers: {'Authorization': 'basic '+ token}
		// });

		// instance.get('/d2l/api/le/1.41/7855/dropbox/folders/')
		// .then(response => {
		// 	console.log(response.data);

	 //    	return response.data;
		// })
		// 
		const oauth = require('axios-oauth-client');
		const getAuthorizationCode = oauth.client(axios.create(), {
		  url: 'https://oauth.com/2.0/token',
		  grant_type: 'authorization_code',
		  client_id: 'foo',
		  client_secret: 'bar',
		  redirect_uri: '...',
		  code: '...',
		  scope: 'baz',
		});
	}
}
</script>