<script>
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
      if (content.type == "PATIENT") {
        window.location.href = '/patient';
        console.log(content.last_name);
      }
      else {
        window.location.href = '/specialist';
        console.log(content.email);
      }
    } catch {


    }
  }
</script>

<style>
@import "/static/styles.css";
</style>

<body>
  <div>
  <h1 class="h1Pink">Учиться говорить - легко!</h1>
  <p>
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
  <!-- <label>
    <input type="checkbox" name="remember_me" value="1">
    запомнить меня
  </label> -->
  <label>
    Еще нет аккаунта?
    <button class='registerButton' type="button">Зарегистрироваться</button>
  </label>
  </form>
</container>
</body>