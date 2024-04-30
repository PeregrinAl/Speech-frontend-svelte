<script>
  import {authenticated} from '../../stores/auth';
  import { goto } from '$app/navigation';
  import Nav from '$lib/Navigation.svelte';

  let email = '', password = ''
  
  const submit = async() => {
    try {
      const response = await fetch('http://localhost:8000/auth/login', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          credentials: "include",
          body: JSON.stringify({
              email,
              password
          })
      });
      const content = await response.json();
      if (content.type == "SPECIALIST") {
        authenticated.set(true);
        goto('/specialist');
      }
      else if (content.type == "PATIENT")  {
        authenticated.set(true);
        goto('/patient');
      }
      else {
        
      }
    } catch {
      authenticated.set(false);
      console.log('fail');
    }
  }
</script>
<Nav/>
<div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Войти в аккаунт</h2>
    </div>
  
    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" on:submit|preventDefault={submit} method="POST">
        <div>
          <label for="email" class="block text-sm font-semibold leading-6 text-gray-900">Email</label>
          <div class="mt-2">
            <input bind:value={email} id="email" name="email" type="email" autocomplete="email" required class="block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
          </div>
        </div>
  
        <div>
          <div class="flex items-center justify-between">
            <label for="password" class="block text-sm font-semibold leading-6 text-gray-900">Пароль</label>
            <div class="text-sm">
              <a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500">Забыли пароль?</a>
            </div>
          </div>
          <div class="mt-2">
            <input bind:value={password} id="password" name="password" type="password" autocomplete="current-password" required class="block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
          </div>
        </div>
  
        <div>
          <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Войти</button>
        </div>
      </form>
  
      <p class="mt-10 text-center text-sm text-gray-500">
        Еще нет аккаунта?
        <a href="/register" class="font-semibold leading-6 text-indigo-600 hover:text-indigo-500">Зарегистрируйтесь</a>
      </p>
    </div>
  </div>
  