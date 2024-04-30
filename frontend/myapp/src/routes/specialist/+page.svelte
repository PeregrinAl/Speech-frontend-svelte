<script>
    import Modal from '$lib/Modal.svelte';
    let showModal = false;
    let patientId = 0;
	const addUser = async() => {
		showModal = true;
		try {
			const response = await fetch('http://localhost:8000/main/addUser', {
				method: 'POST',
				headers: {'Content-Type': 'application/json'},
				credentials: "include",
				body: JSON.stringify({
					patientId
				})
			});
			const content = await response.json();
			if (content.message == "success") {
				// TODO:
			}
			else if (content.message == "already exist")  {
				// TODO:
			}
			else {
				// TODO:
			}
		} 
		
		catch {

		}
  }
</script>

<style>
	.specialistPage {
		display: flex;
		justify-content: space-between;
        background-color: #ececf8;
	}
    
	button {
		display: block;
		min-width: 210px;
		border: 2px solid transparent;
		border-radius: 6px;
		margin: 10px;
		padding: 9px 15px;
		color: rgb(135, 138, 184);
		font-size: 18px;
		font-weight: 300;
        font-family: "Roboto", sans-serif;
		transition: background-color 0.2s linear;
	}
	button:hover {
		background-color: #bbe4b6;
		cursor: pointer;
		transition: background-color 0.2s linear;
	}
	
	button:focus-visible {
		border: 2px solid #bbe4b6;
		outline: none;
	}
    button:focus {
		border: 2px solid #bbe4b6;
		outline: none;
	}
    button:disabled {
		opacity: 0.5;
		cursor: not-allowed;
	}
    label {
        font-size: 18px;
        color: rgb(135, 138, 184);
        font-family: "Roboto", sans-serif;
    }
</style>

<Modal bind:showModal>
    <label>
        Идентификатор пациента
        <input
          bind:value={patientId}
          type='number'
          name="name"
          id="name"
          placeholder="Идентификатор"
          required
          >
      </label>
</Modal>
<dev class='specialistPage'>
<dev class='scenarios'>
	<button>Добавить сценарий</button>
</dev>

<dev class='patients'>
	<button on:click={addUser}>Добавить пациента</button>
</dev>
</dev>