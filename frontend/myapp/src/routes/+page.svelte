<script>


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
<form id="email" action="/apply/" method="POST">
  <label>
    Email:
    <input
      type="text"
      name="name"
      id="name"
      placeholder="Email"
      required
    >
  </label>

  <label>
    Пароль:
    <input type="text" name="password" required>
  </label>
  <button type="submit">Войти</button>
  <!-- <label>
    <input type="checkbox" name="remember_me" value="1">
    запомнить меня
  </label> -->
  <label>
    Еще нет аккаунта?:
    <button type="submit">Зарегистрироваться</button>
  </label>
  </form>
</container>
</body>