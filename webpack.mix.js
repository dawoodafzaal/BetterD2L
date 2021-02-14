let mix = require('laravel-mix');

mix.js('js/app.js', 'dist').vue({ version: 2 })
	.postCss("css/app.css", "dist", [
		require("tailwindcss"),
    ]);