<script>
    import {authenticated} from "../stores/auth";
    
    let auth = false;

    authenticated.subscribe(a => auth = a);
    
    const logout = async () => {
        await fetch('http://localhost:8000/auth/logout', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            credentials: 'include',
        });
        authenticated.set(false);
    }
</script>

<style scoped>
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #97a0d6;
}

li {
  float: right;
}

li a {
    font-family: "Roboto", sans-serif;
    font-size: 18px;
    display: block;
    color: white;
    text-align: center;
    padding: 16px 16px;
    text-decoration: none;
}

/* Change the link color to #111 (black) on hover */
li a:hover {
  background-color: #dcb9e7;
}

</style>

<ul class="navbar-nav me-auto mb-2 mb-md-0">
    <li class="nav-item">
        <a href="/" class="nav-link" on:click={logout}>Выйти</a>
    </li>
    <li class="nav-item">
        <a href="/" class="nav-link">О себе</a>
    </li>
</ul>