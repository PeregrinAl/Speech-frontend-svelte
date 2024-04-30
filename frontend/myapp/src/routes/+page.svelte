<script>
  import {authenticated} from '../stores/auth';
  import { goto } from '$app/navigation';

</script>
  <div class="container mx-auto rounded-md text-center px-40 py-10">
    <h1 class="text-3xl font-mono font-bold tracking-tight text-gray-900 sm:text-6xl">Сервис для логопедов и людей с нарушениями речи</h1>
    <p class="mt-6 text-xl font-mono leading-8 text-gray-700">Серис предназначен для обеспечения удаленного взаимодействия логопедов и людей с нарушениями речи</p>
  </div>
  <div class="columns-2 text-center rounded-md">
    <div class="rounded-md bg-gradient-to-b from-indigo-100 py-5">
      <h1 class="font-mono font-bold sm:text-4xl">Если Вы - логопед</h1>
      <p class="m-8 font-mono text-xl py-30 leading-8 text-gray-700">Сервис даст Вам возможность создавать сценарии работы, состоящие из подготовленных нашим специалистом упражнений. Комбинируйте их, используйте повторно и назначайте своим пациентам!</p>
      <a href="/register/specialist" class="rounded-md px-10 py-2.5 text-white font-semibold shadow-sm transition transform hover:-translate-y-1 rounded-md bg-gradient-to-r from-indigo-400 to-teal-400 hover:from-indigo-500 hover:to-green-500">Зарегистрироваться</a>  
    </div>
    
    <div class="rounded-md bg-gradient-to-b from-indigo-100 py-5">
      <h1 class="font-mono font-bold sm:text-4xl">Если Вы - пациент</h1>
      <p class="m-8 font-mono text-xl py-30 leading-8 text-gray-700">Сервис станет помощником для Вас и Вашего специалиста по работе с речью. Регистрируйтесь, делитесь своим идентификатором со специалистом, получайте от него домашние задания и отслеживайте свой прогресс!</p>
      <a href="/register/patient" class="rounded-md px-10 py-2.5 text-white font-semibold shadow-sm transition transform hover:-translate-y-1 rounded-md bg-gradient-to-r from-indigo-400 to-teal-400 hover:from-indigo-500 hover:to-green-500">Зарегистрироваться</a>  
    </div>
  </div>