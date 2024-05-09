<script>
    import { authenticated } from "../stores/auth";
    import { csrfToken } from '../stores/auth';
    import { onMount } from 'svelte';
    let csrfTokenValue = '';

    csrfToken.subscribe((value) => {
		    csrfTokenValue = value;
	    });

    function getCookie(name) {
        let cookieValue = null;
        console.log(document.cookie);
        if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        console.log(cookies);
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
            }
        }
        }
        return cookieValue;
    }
    function getCSRF(){
    fetch("http://localhost:8000/auth/csrf", {
      credentials: "same-origin",
    })
    .then((res) => {
      let csrfToken = getCookie("X-CSRFToken");
      csrfToken.set(csrfToken);
      console.log(csrfTokenValue);
    })
    .catch((err) => {
      console.log(err);
    });
  }

  function getSession(){
    fetch("http://localhost:8000/auth/session", {
      credentials: "same-origin",
    })
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      if (data.isAuthenticated) {
        authenticated.set(true);
        console.log('logout: authenticated !!');
      } else {
        authenticated.set(false);
        console.log('logout: not authenticated ')
        getCSRF();
      }
    })
    .catch((err) => {
      console.log(err);
    });
  }
  let auth = false;
    onMount(() => {
        getSession();
    });

    


    authenticated.subscribe(a => auth = a);
    function logout() {
        console.log(csrfTokenValue)
        fetch("http://localhost:8000/auth/logout", {
            credentials: "same-origin",
            'X-CSRFToken': csrfTokenValue,
            method: "POST"
        })
        .then(this.isResponseOk)
        .then((data) => {
            console.log(data, 'logging out');
            authenticated.set(false);
            console.log('generating new csrf');
            getCSRF();
        })
        .catch((err) => {
            console.log(err, 'logout error');
        });
    };
    
    // const logout = async () => {
    //     console.log(csrfTokenValue);
    //     await fetch('http://localhost:8000/auth/logout', {
    //         method: 'POST',
    //         headers: {'Content-Type': 'application/json',
    //         'X-CSRFToken': csrfTokenValue
    //         },
    //         credentials: 'include',
    //     });
    //     authenticated.set(false);
    // }
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
    {#if auth == true}
    <li class="nav-item">
        <a href="/" class="nav-link" on:click={logout}>Выйти</a>
    </li>
    <li class="nav-item">
        <a href="/" class="nav-link">О себе</a>
    </li>
    {:else}
    <li>
        <a href="/" class="nav-link">О сервисе</a>
    </li>
    <li>
        <a href="/auth" class="nav-link">Войти</a>
    </li>
    {/if}
</ul>