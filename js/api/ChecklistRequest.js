import Request from './Request';

class ChecklistRequest extends Request{
    retrieve() {
        return this.get('http://127.0.0.1:5000/checklist');
    }

    store() {
    	return this.post('http://127.0.0.1:5000/checklist');
    }

    update(id) {
    	return this.patch('http://127.0.0.1:5000/checklist/' + id);
    }

    destroy() {
        return this.delete('http://127.0.0.1:5000/checklist');
    }
}

export default ChecklistRequest