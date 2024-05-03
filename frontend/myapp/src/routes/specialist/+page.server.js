export async function load() {
    
	const response = await fetch('http://127.0.0.1:8000/auth/getpatients', {
			method: 'GET',
			credentials: "include"
		});	
        
	const data = await response.json();
    if (!response.ok) {
        return {
            summaries: { error: data.message }
        };
    }
    return {
        summaries: data
    };
}
