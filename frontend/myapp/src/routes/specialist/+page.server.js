import { patients } from './data.js';

export function load() {
	return {
		summaries: patients.map((patient) => ({
            id: patient.id,
			first_name: patient.first_name,
			last_name: patient.last_name,
            date_of_birth: patient.date_of_birth
		}))
	};
}