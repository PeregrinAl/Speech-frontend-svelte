export async function handle({ event, resolve }) {
	if (event.url.pathname === '/specialist') {
        if (event.cookies.get('type') != "SPECIALIST") {
            return new Response('Вы не авторизованы, ваша кука все про вас рассказала!!!!');
        }
	}
	
    if (event.url.pathname === '/patient') {
        if (event.cookies.get('type') != "PATIENT") {
            return new Response('Вы не авторизованы, ваша кука все про вас рассказала!!!!');
        }
	}
	
	return await resolve(event, {
		// transformPageChunk: ({ html }) => html.replace(
		// 	'<body',
		// 	'<body style="color: hotpink"'
		// )
	});
}