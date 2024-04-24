<script>
  import {authenticated} from '../stores/auth';
  import { goto } from '$app/navigation';

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
      console.log(auth);
    }
  }
</script>

<style>
@import "/static/styles.css";
</style>

<div class="login">
  <div>
  <h1 class="h1welcome">Учиться говорить - легко!</h1>
  <p class="pwelcome">
      Добро пожаловать в сервис 
      «Говорить - легко»! 
      <br>

      <br>Мы здесь, чтобы помочь улучшить вашу речь<br>
      
      <br>Начните свой путь к улучшению речи вместе с нами сегодня!
  </p>
  </div>

<div class ="container">
<container>
<form on:submit|preventDefault={submit}>
  <label>
    Email:
    <input
      bind:value={email}
      type="text"
      name="name"
      id="name"
      placeholder="Email"
      required
    >
  </label>

  <label>
    Пароль:
    <input bind:value={password} type="text" name="password" required>
  </label>
  <button type="submit">Войти</button>
  <label>
    Еще нет аккаунта?
    <button class='registerButton' type="button">Зарегистрироваться</button>
  </label>
  </form>
</container>
</div>
</div>