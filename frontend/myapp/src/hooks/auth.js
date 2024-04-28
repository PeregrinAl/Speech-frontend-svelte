// import { getSession } from '@sveltejs/kit'

// export async function handle({ request, resolve }) {
//   const session = await getSession(request.headers)

//   if (session && session.role === 'PATIENT') {
//     return resolve(request)
//   } 
//   else if (session && session.role === 'SPECIALIST') {
//     return resolve(request)
//   } else {
//     return {
//       status: 302,
//       headers: {
//         location: '/login' // Перенаправляем пользователя на страницу аутентификации
//       }
//     }
//   }
// }