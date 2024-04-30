<script>
  import Nav from '$lib/Navigation.svelte';
  import { goto } from '$app/navigation';
  import { Datepicker } from 'flowbite-svelte';
  let first_name = ''; 
  let last_name = '';
  let email = '';
  let type = 'PATIENT';
  let password='';
  let date_of_birth = '';
  const submit = async() => {
    try {
      const response = await fetch('http://localhost:8000/auth/patientregister', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          credentials: "include", // 'first_name', 'last_name', 'email', 'type','password', 'date_of_birth'
          body: JSON.stringify({
            first_name,
            last_name,
            email,
            type,
            password,
            date_of_birth,
          })
      });
      const content = await response.json();
      goto('/auth');
      console.log(date_of_birth);
    } catch {
      console.log('reg failed');
    }
  }
  export let role="пациента";
</script>
<Nav/>
<div class="isolate bg-white px-6 py-24 sm:py-32 lg:px-8">
  <div class="mx-auto max-w-2xl text-center">
    <h2 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">Регистрация для {role}</h2>
    <p class="mt-2 text-lg leading-8 text-gray-600">Привет! Давайте заполним необходимые поля</p>
  </div>
  <form on:submit|preventDefault={submit} method="POST" class="mx-auto mt-16 max-w-xl sm:mt-20">
    <div class="grid grid-cols-1 gap-x-8 gap-y-6 sm:grid-cols-2">
      <div>
        <label for="first-name" class="block text-sm font-semibold leading-6 text-gray-900">Имя</label>
        <div class="mt-2.5">
          <input  bind:value={first_name} type="text" name="first-name" id="first-name" autocomplete="given-name" class="block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
        </div>
      </div>
      <div>
        <label for="last-name" class="block text-sm font-semibold leading-6 text-gray-900">Фамилия</label>
        <div class="mt-2.5">
          <input bind:value={last_name} type="text" name="last-name" id="last-name" autocomplete="family-name" class="block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
        </div>
      </div>
      <div class="sm:col-span-2">
        <label for="email" class="block text-sm font-semibold leading-6 text-gray-900">Email</label>
        <div class="mt-2.5">
          <input bind:value={email} type="email" name="email" id="email" autocomplete="email" class="block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
        </div>
      </div>
      <div class="sm:col-span-2">
        <label for="email" class="block text-sm font-semibold leading-6 text-gray-900">Пароль</label>
        <div class="mt-2.5">
          <input bind:value={password} type="password" name="password" id="password" autocomplete="new-password" class="block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
        </div>
      </div>
      <Datepicker bind:value={date_of_birth} name="date_of_birth" datepickerFormat="yyyy-mm-dd" datepickerOrientation="right"/>
    </div>
    <div class="mt-10">
      <button type="submit" class="block w-full rounded-md bg-indigo-600 px-3.5 py-2.5 text-center text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Зарегистрироваться</button>
    </div>
  </form>
  <div class="absolute top-[-10rem] -z-10 transform-gpu overflow-hidden blur-3xl sm:top-[-20rem]">
    <div class="relative left-1/2 -z-10 aspect-[1155/678] w-[36.125rem] max-w-none -translate-x-1/2 rotate-[30deg] bg-gradient-to-tr from-[#ff80b5] to-[#9089fc] opacity-30 sm:left-[calc(50%-40rem)] sm:w-[72.1875rem]" style="clip-path: polygon(74.1% 44.1%, 100% 61.6%, 97.5% 26.9%, 85.5% 0.1%, 80.7% 2%, 72.5% 32.5%, 60.2% 62.4%, 52.4% 68.1%, 47.5% 58.3%, 45.2% 34.5%, 27.5% 76.7%, 0.1% 64.9%, 17.9% 100%, 27.6% 76.8%, 76.1% 97.7%, 74.1% 44.1%)"></div>
  </div>
</div>